#!/usr/bin/env python3
# -------------------------------------------------------------------------- #
# Filename:     copy_flame_presets.py
# Purpose:      Copies Flame presets to project directories.
# Description:  This script handles the copying of site-level presets and
#               configurations to the newly created project directories.

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
import shutil
import logging
import sys
from pathlib import Path

from src.core.utils.path_utils import get_repository_root_dir
from src.core.functions.get.get_application_paths import GetApplicationPaths


def copy_flame_presets(logik_projekt_path: str, flame_projekt_setups_dir: str):
    """
    Copies site-level presets and configurations to the newly created
    project directories.

    Args:
        logik_projekt_path (str): The absolute path to the LOGIK-PROJEKT
            directory.
        flame_projekt_setups_dir (str): The absolute path to the Flame
            project's "setups" directory.
    """
    logging.info("Copying project presets...")

    try:
        repository_root_dir = get_repository_root_dir()

        # 1. Rsync flame-presets to flame_projekt_setups_dir
        flame_presets_source = (
            repository_root_dir / GetApplicationPaths.FLAME_PRESETS_DIR
        )
        flame_presets_destination = flame_projekt_setups_dir

        if flame_presets_source.exists() and flame_presets_source.is_dir():
            rsync_command_flame = (
                f"rsync -avh --ignore-existing "
                f"{flame_presets_source}/ {flame_presets_destination}"
            )
            logging.info(f"Executing: {rsync_command_flame}")
            os.system(rsync_command_flame)
            logging.info(
                "Successfully rsynced %s to %s",
                flame_presets_source,
                flame_presets_destination
            )
        else:
            logging.warning(
                "Source directory not found or not a directory: %s",
                flame_presets_source
            )

        # 2. Rsync shared-presets to /opt/Autodesk/shared/
        shared_presets_source = (
            repository_root_dir / GetApplicationPaths.SHARED_PRESETS_DIR
        )
        shared_presets_destination = GetApplicationPaths.AUTODESK_SHARED_DIR

        if shared_presets_source.exists() and shared_presets_source.is_dir():
            rsync_command_shared = (
                f"rsync -avh --ignore-existing "
                f"{shared_presets_source}/ {shared_presets_destination}"
            )
            logging.info(f"Executing: {rsync_command_shared}")
            logging.warning(
                "Note: Copying to /opt/Autodesk/shared/ "
                "might require root privileges."
            )
            os.system(rsync_command_shared)
            logging.info(
                "Successfully rsynced %s to %s",
                shared_presets_source,
                shared_presets_destination
            )
        else:
            logging.warning(
                "Source directory not found or not a directory: %s",
                shared_presets_source
            )

    except FileNotFoundError as e:
        logging.error("Error finding project root: %s", e)
    except Exception as e:
        logging.error("An unexpected error occurred during preset copy: %s", e)


if __name__ == "__main__":
    # Example usage for direct script execution and testing
    if len(sys.argv) != 3:
        print(
            "Usage: python copy_flame_presets.py "
            "<logik_projekt_path> <flame_projekt_setups_dir>"
        )
        sys.exit(1)

    logik_path = sys.argv[1]
    setups_path = sys.argv[2]

    # For testing, create the base directories if they don't exist
    if not os.path.exists(logik_path):
        print(f"Creating test directory: {logik_path}")
        os.makedirs(logik_path)

    if not os.path.exists(setups_path):
        print(f"Creating test directory: {setups_path}")
        os.makedirs(setups_path)

    copy_flame_presets(logik_path, setups_path)


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
