#!/usr/bin/env python3
# -------------------------------------------------------------------------- #
# Filename:     copy_flame_python_scripts.py
# Purpose:      Copies Flame Python scripts to the project's setups directory.
# Description:  This script ensures that necessary Python scripts are available
#               within the Flame project environment.

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
import logging
import sys
from pathlib import Path

from src.core.utils.path_utils import get_repository_root_dir
from src.core.functions.get.get_application_paths import GetApplicationPaths


def modify_openclip_python_config_paths(scripts_destination: Path):
    """
    Modifies the base_python_path in copied Python scripts.

    Args:
        scripts_destination (Path): The directory containing the Python
            scripts.
    """
    logging.info("Modifying Python script paths in copied scripts...")
    old_path_string = (
        "base_python_path = Path('/opt/Autodesk/shared/python')"
    )
    new_path_string = f"base_python_path = Path('{scripts_destination}')"

    if not scripts_destination.is_dir():
        logging.warning(f"Script directory not found: {scripts_destination}")
        return

    for filepath in scripts_destination.rglob("*.py"):
        try:
            content = filepath.read_text()
            if old_path_string in content:
                logging.info(f"Updating path in: {filepath.name}")
                content = content.replace(old_path_string, new_path_string)
                filepath.write_text(content)
        except Exception as e:
            logging.error(f"Failed to modify {filepath.name}: {e}")


def copy_flame_python_scripts(flame_projekt_setups_dir: str):
    """
    Copies Flame Python scripts to the project's setups directory.

    Args:
        flame_projekt_setups_dir (str): The absolute path to
            the Flame project's "setups" directory.
    """
    logging.info("Copying Flame Python scripts...")

    try:
        repository_root_dir = get_repository_root_dir()

        # Rsync flame-python/* to flame_projekt_setups_dir/python
        flame_scripts_source = (
            repository_root_dir / GetApplicationPaths.FLAME_PYTHON_SCRIPTS_DIR
        )
        flame_scripts_destination = (
            Path(flame_projekt_setups_dir) / "python"
        )

        # Create the destination directory if it doesn't exist
        flame_scripts_destination.mkdir(parents=True, exist_ok=True)

        if flame_scripts_source.exists() and flame_scripts_source.is_dir():
            rsync_command = (
                f"rsync -avh --ignore-existing "
                f"{flame_scripts_source}/ {flame_scripts_destination}"
            )
            logging.info(f"Executing: {rsync_command}")
            os.system(rsync_command)
            logging.info(
                "Successfully rsynced %s to %s",
                flame_scripts_source,
                flame_scripts_destination,
            )
            modify_openclip_python_config_paths(flame_scripts_destination)
        else:
            logging.warning(
                "Source directory not found or not a directory: %s",
                flame_scripts_source
            )

    except FileNotFoundError as e:
        logging.error("Error finding project root: %s", e)
    except Exception as e:
        logging.error(
            "An unexpected error occurred during script copy: %s", e
        )


if __name__ == "__main__":
    # Example usage for direct script execution and testing
    if len(sys.argv) != 2:
        print(
            "Usage: python copy_flame_python_scripts.py "
            "<flame_projekt_setups_dir>"
        )
        sys.exit(1)

    setups_path = sys.argv[1]

    # For testing, create the base directories if they don't exist
    if not os.path.exists(setups_path):
        print(f"Creating test directory: {setups_path}")
        os.makedirs(setups_path)

    copy_flame_python_scripts(setups_path)


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
