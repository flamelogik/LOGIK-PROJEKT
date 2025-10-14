#!/usr/bin/env python3
# -------------------------------------------------------------------------- #
# Filename:     create_flame_setup_dirs.py
# Purpose:      Creates a predefined set of subdirectories within the 
#               Flame project's setup directory.
# Description:  This script reads a JSON configuration to create a standardized
#               directory structure for Flame project setups.

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
def create_flame_setup_dirs(setups_dir_path: str):
    """
    Creates a predefined set of subdirectories within the Flame project's
    setup directory.

    Args:
        setups_dir_path (str): The absolute path to the Flame project's
        'setups' directory.
    """
    os.makedirs(setups_dir_path, exist_ok=True)

    try:
        repository_root_dir = get_repository_root_dir()
        json_config_path = (
            repository_root_dir /
            (
                "pref/site-prefs/default-prefs/"
                "logik-projekt-prefs/flame_setup_dirs.json"
            )
        )

        with open(json_config_path, 'r', encoding='utf-8') as f:
            data = json.load(f)

        subdirectories = data.get("flame_setup_dirs.json", [])

        if not subdirectories:
            logging.warning(
                "No subdirectories found in the JSON configuration file."
            )
            return

        logging.info(
            f"Creating Flame setup subdirectories in: {setups_dir_path}"
        )
        created_count = 0
        for subdir in subdirectories:
            full_path = os.path.join(setups_dir_path, subdir)
            try:
                os.makedirs(full_path, exist_ok=True)
                logging.info(f"Created: {full_path}")
                created_count += 1
            except OSError as e:
                logging.error(f"Error creating directory {full_path}: {e}")

        logging.info(
            f"Successfully created {created_count} setup directories."
        )

    except FileNotFoundError:
        logging.error(f"Configuration file not found at: {json_config_path}")
    except json.JSONDecodeError as e:
        logging.error(f"Error decoding JSON from {json_config_path}: {e}")
    except Exception as e:
        logging.error(f"An unexpected error occurred: {e}")


if __name__ == "__main__":
    # Example usage for direct script execution and testing
    if len(sys.argv) != 2:
        print(
            (
                "Usage: python create_flame_setup_dirs.py "
                "<path_to_flame_setups_dir>"
            )
        )
        sys.exit(1)

    target_setups_dir = sys.argv[1]
  
    # For testing, create the base directory if it doesn't exist
    if not os.path.exists(target_setups_dir):
        print(f"Creating test directory: {target_setups_dir}")
        os.makedirs(target_setups_dir)
      
    create_flame_setup_dirs(target_setups_dir)


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
