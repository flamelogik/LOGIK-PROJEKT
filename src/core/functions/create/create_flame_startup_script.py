#!/usr/bin/env python3
# -------------------------------------------------------------------------- #
# Filename:     create_flame_setup_dirs.py
# Purpose:      Creates a predefined set of subdirectories within the
#               Flame project's setup directory.
# Description:  This script reads a JSON configuration to create a
#               standardized directory structure for Flame project setups.

# Author:       phil_man@mac.com
# Copyright:    Copyright (c) 2025
# Disclaimer:   Disclaimer at bottom of script.
# License:      GNU General Public License v3.0 (GPL-3.0).
#               https://www.gnu.org/licenses/gpl-3.0.en.html

# Version:      2026.1.0
# Status:       Production
# Type:         Utility
# Created:      2025-07-01
# Modified:     2025-10-08

# Changelog:    Changelog at bottom of script.
# -------------------------------------------------------------------------- #

import os
import json
import logging
import sys
from pathlib import Path

from src.core.utils.path_utils import get_repository_root_dir


# Configure logging
def create_flame_startup_script(
        flame_projekt_setups_dir: str,
        logik_projekt_config_workspace_path: str
):
    """
    Creates a Flame startup script by combining a template with a 
    workspace layout.

    Args:
        flame_projekt_setups_dir (str): The absolute path to the Flame 
        project's 'setups' directory.
    """
    logging.info("Creating Flame startup script...")

    try:
        repository_root_dir = get_repository_root_dir()

        # 1. Define paths for the template, workspace JSON, and output script
        template_path = (
            repository_root_dir
            / 'cfg'
            / 'site-cfg'
            / 'flame-cfg'
            / 'flame-scripts'
            / 'flame-startup-scripts'
            / 'flame_startup_script_template.py'
        )
        output_script_dir = (
            Path(flame_projekt_setups_dir)
            / 'scripts'
            / 'startup'
        )
        output_script_path = (
            output_script_dir
            / 'flame_startup_script.py'
        )
        output_workspace_path = (
            Path(flame_projekt_setups_dir)
            / 'scripts'
            / 'startup'
            / 'flame-workspace.json'
        )

        # Ensure the destination directory exists
        os.makedirs(output_script_dir, exist_ok=True)

        # 2. Read the content of the template
        if not template_path.exists():
            logging.error(
                f"Startup script template not found at: {template_path}"
            )
            return

        with open(template_path, 'r', encoding='utf-8') as f:
            script_template = f.read()

        # Inject the absolute path of flame-workspace.json into the template
        # The template expects a variable named 'workspace_file'
        injected_script_content = script_template.replace(
            'workspace_file = "flame-workspace.json"',
            f'workspace_file = "{output_workspace_path}"'
        )

        # 3. Write the modified template content to flame_startup_script.py
        with open(output_script_path, 'w', encoding='utf-8') as f:
            f.write(injected_script_content)
        logging.info(
            (
                "Successfully created Flame startup script at: "
                f"{output_script_path}"
            )
        )

        # 4. Read, validate, and write the workspace data
        try:
            with open(
                logik_projekt_config_workspace_path,
                'r',
                encoding='utf-8'
            ) as f:
                workspace_data = json.load(f)

            with open(output_workspace_path, 'w', encoding='utf-8') as f:
                json.dump(workspace_data, f, indent=4)
            logging.info(
                f"Successfully created Flame workspace JSON at: "
                f"{output_workspace_path}"
            )
        except FileNotFoundError:
            logging.error(
                f"Workspace JSON file not found at: "
                f"{logik_projekt_config_workspace_path}"
            )
            return
        except json.JSONDecodeError:
            logging.error(
                f"Error decoding JSON from: "
                f"{logik_projekt_config_workspace_path}"
            )
            return

    except Exception as e:
        logging.error(
            "An unexpected error occurred during startup script creation: "
            f"{e}"
        )


if __name__ == "__main__":
    # Example usage for direct script execution and testing
    if len(sys.argv) != 3:
        print(
            "Usage: python create_flame_startup_script.py "
            "<flame_projekt_setups_dir> "
            "<logik_projekt_config_workspace_json_path>"
        )
        sys.exit(1)

    setups_path = sys.argv[1]
    workspace_json_path = sys.argv[2]

    # For testing, create the base directory if it doesn't exist
    if not os.path.exists(setups_path):
        print(f"Creating test directory: {setups_path}")
        os.makedirs(setups_path)

    create_flame_startup_script(setups_path, workspace_json_path)


# -------------------------------------------------------------------------- #

# DISCLAIMER:   This file is part of LOGIK-PROJEKT.

#               Copyright © 2025 STRENGTH IN NUMBERS

#               LOGIK-PROJEKT creates directories, files, scripts & tools
#               for use with Autodesk Flame and other software.

#               LOGIK-PROJEKT is free software.

#               You can redistribute it and/or modify it under the terms
#               of the GNU General Public License as published by the
#               Free Software Foundation, either version 3 of the License,
#               or any later version.

#               This program is distributed in the hope that it will be
#               useful, but WITHOUT ANY WARRANTY; without even the
#               implied warranty of MERCHANTABILITY or
#               FITNESS FOR A PARTICULAR PURPOSE.

#               See the GNU General Public License for more details.
#               You should have received a copy of the GNU General
#               Public License along with this program.

#               If not, see <https://www.gnu.org/licenses/gpl-3.0.en.html>.

#               Contact: phil_man@mac.com

# -------------------------------------------------------------------------- #
# C2 A9 32 30 32 35 53 54 52 45 4E 47 54 48 2D 49 4E 2D 4E 55 4D 42 45 52 53 #
# -------------------------------------------------------------------------- #
# Changelog:
# -------------------------------------------------------------------------- #
