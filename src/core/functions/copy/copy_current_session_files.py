#!/usr/bin/env python3
# -------------------------------------------------------------------------- #
# Filename:     copy_current_session_files.py
# Purpose:      Copies current session files to the project's setups directory.
# Description:  This script handles the copying of session-related files,
#               including preferences & logs, to a specified project directory.

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
import shutil
import glob
from pathlib import Path

from src.core.utils.path_utils import get_repository_root_dir
from src.core.functions.get.get_application_paths import GetApplicationPaths


def copy_current_session_files(
        logik_projekt_path: str,
        current_workstation: str
):
    """
    Copies current session files to the project's setups directory.

    Args:
        logik_projekt_path (str): The absolute path to the LOGIK-PROJEKT
        project's root directory.
        current_workstation (str): The name of the current workstation.
    """
    logging.info("Copying current session files...")

    try:
        repository_root_dir = get_repository_root_dir()

        # 1. Rsync pref/session-preferences/* to
        # logik_projekt_path/logs/current_workstation
        session_files_source = (
            repository_root_dir / GetApplicationPaths.SESSION_PREFERENCES_DIR
            )
        session_files_destination = (
            Path(logik_projekt_path) / "logs" / current_workstation
        )

        # Create the destination directory if it doesn't exist
        session_files_destination.mkdir(
            parents=True,
            exist_ok=True
        )

        if session_files_source.exists() and session_files_source.is_dir():
            rsync_command = (
                f"rsync -avh --ignore-existing "
                f"{session_files_source}/ {session_files_destination}"
            )
            logging.info(f"Executing: {rsync_command}")
            os.system(rsync_command)
            logging.info(
                f"Successfully rsynced {session_files_source} to "
                f"{session_files_destination}"
            )
        else:
            logging.warning(
                "Source directory not found or not a directory: "
                f"{session_files_source}"
            )

        # 2. Find and copy the most recent session log
        log_dir = repository_root_dir / GetApplicationPaths.SESSION_LOGS_DIR
        log_files = glob.glob(
            str(log_dir / '**' / '*.log'),
            recursive=True
        )

        if not log_files:
            logging.warning("No session log files found.")
            return

        latest_log_file = max(log_files, key=os.path.getmtime)
        log_file_destination = (
            Path(logik_projekt_path) / "logs" / current_workstation
        )

        if os.path.exists(latest_log_file):
            shutil.copy(latest_log_file, log_file_destination)
            logging.info(
                f"Successfully copied {latest_log_file} to "
                f"{log_file_destination}"
            )
        else:
            logging.warning(f"Log file not found: {latest_log_file}")

    except FileNotFoundError as e:
        logging.error(f"Error finding project root: {e}")
    except Exception as e:
        logging.error(
            "An unexpected error occurred during session file copy: "
            f"{e}"
        )


if __name__ == "__main__":
    # Example usage for direct script execution and testing
    if len(sys.argv) != 3:
        print(
            "Usage: python copy_current_session_files.py "
            "<logik_projekt_path> <current_workstation>"
        )
        sys.exit(1)

    logik_path = sys.argv[1]
    workstation_name = sys.argv[2]

    # For testing, create the base directories if they don't exist
    if not os.path.exists(logik_path):
        print(f"Creating test directory: {logik_path}")
        os.makedirs(logik_path)

    copy_current_session_files(logik_path, workstation_name)


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
