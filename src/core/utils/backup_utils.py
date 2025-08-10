
#!/usr/bin/env python3
# -------------------------------------------------------------------------- #
# Filename:     backup_utils.py
# Purpose:      Provides utilities for managing project backups.
# Description:  This module contains functions for constructing rsync commands,
#               running backups, and scheduling them via cron.

# Author:       phil_man@mac.com
# Copyright:    Copyright (c) 2025
# Disclaimer:   Disclaimer at bottom of script.
# License:      GNU General Public License v3.0 (GPL-3.0).
#               https://www.gnu.org/licenses/gpl-3.0.en.html

# Version:      2026.1.0
# Status:       Production
# Type:         Utility
# Created:      2025-07-01
# Modified:     2025-08-03

# Changelog:    Changelog at bottom of script.
# -------------------------------------------------------------------------- #

import subprocess
import os


def get_rsync_backup_command(projekt_summary_data, source_dir, dest_dir):
    """
    Constructs the rsync command based on the projekt_summary_data.
    """
    # Extract relevant data from projekt_summary_data
    projekt_name = (
        projekt_summary_data.get(
            "projekt_name",
            "default_projekt"
        )
    )
    flame_workstation_name = (
        projekt_summary_data.get(
            "flame_workstation_name",
            "default_workstation"
        )
    )

    # Define paths and exclusion list
    rsync_log_dir = (
        os.path.join(
            dest_dir,
            "rsync_logs"
        )
    )
    os.makedirs(
        rsync_log_dir,
        exist_ok=True
    )

    log_file = (
        os.path.join(
            rsync_log_dir,
            f"{projekt_name}_backup.log"
        )
    )
    exclusion_file = (
        os.path.join(
            source_dir,
            "backup",
            "backup-scripts",
            flame_workstation_name,
            f"backup-"
            f"{projekt_name}-"
            f"{flame_workstation_name}-"
            f"exclusion_list.txt"
        )
    )

    # Construct the rsync command
    rsync_command = [
        "rsync",
        "-av",
        "--copy-links",
        "--exclude='.DS_Store'",
        f"--log-file={log_file}",
        f"--exclude-from={exclusion_file}",
        source_dir,
        dest_dir
    ]
  
    return rsync_command


def run_rsync_backup(rsync_command):
    """
    Runs the rsync backup command.
    """
    try:
        subprocess.run(
            rsync_command,
            check=True
        )
        print(
            f"Backup completed successfully."
        )
    except subprocess.CalledProcessError as e:
        print(
            f"Error during backup: {e}"
        )


def get_rsync_backup_script_path(projekt_summary_data):
    """
    Returns the path to the backup script.
    """
    projekt_name = (
        projekt_summary_data.get(
            "projekt_name",
            "default_projekt"
        )
    )
    flame_workstation_name = (
        projekt_summary_data.get(
            "flame_workstation_name",
            "default_workstation"
        )
    )

    backup_script_path = (
        os.path.join(
            projekt_summary_data.get(
                "projekt_root_dir"
            ),
            projekt_name,
            "backup",
            "backup-scripts",
            flame_workstation_name,
            f"backup_{projekt_name}.sh"
        )
    )

    return backup_script_path


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
