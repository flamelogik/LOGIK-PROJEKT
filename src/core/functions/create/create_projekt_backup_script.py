#!/usr/bin/env python3
# -------------------------------------------------------------------------- #
# Filename:     create_projekt_backup_script.py
# Purpose:      Creates backup scripts for a project.
# Description:  This script generates a shell script for project backup and
#               a corresponding crontab entry for automated backups.

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
import stat
import logging
from datetime import datetime

logger = logging.getLogger(__name__)


def create_projekt_backup_script(
        projekt_summary_data: dict,
        backup_template_path: str,
        backup_script_dir: str
):
    """
    Creates a backup script and a crontab entry for a project.

    Args:
        projekt_summary_data (dict): Data for the project.
        backup_template_path (str): Path to the backup script template.
        backup_script_dir (str): Directory to save the generated scripts.
    """
    logger.info(
        f"Creating PROJEKT backup infrastructure for "
        f"{projekt_summary_data['logik_projekt_name']} on "
        f"{projekt_summary_data['current_workstation']}."
    )

    os.umask(0)

    # Ensure the backup script directory exists
    os.makedirs(backup_script_dir, exist_ok=True)

    # --- Create Backup Script ---
    backup_script_name = (
        f"backup-"
        f"{projekt_summary_data['logik_projekt_name']}-"
        f"{projekt_summary_data['current_workstation']}.sh"
    )
    tgt_projekt_backup_script = os.path.join(
        backup_script_dir,
        backup_script_name
    )

    with open(backup_template_path, 'r') as f:
        template_content = f.read()

    script_creation_date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    replacements = {
        "%%BACKUP_SCRIPT_NAME%%": backup_script_name,
        "%%BACKUP_SCRIPT_PROJEKT%%": projekt_summary_data[
            'logik_projekt_name'
        ],
        "%%SCRIPT_CREATION_DATE%%": script_creation_date,
        "%%LOGIK_PROJEKT_NAME%%": projekt_summary_data[
            'logik_projekt_name'
        ],
        "%%FLAME_PROJEKT_NAME%%": projekt_summary_data[
            'flame_projekt_name'
        ],
        "%%CURRENT_WORKSTATION%%": projekt_summary_data[
            'current_workstation'
        ],
        "%%LOGIK_PROJEKT_DIRECTORIES%%": os.path.dirname(
            projekt_summary_data['logik_projekt_path']
        ),
    }

    for placeholder, value in replacements.items():
        template_content = template_content.replace(placeholder, str(value))

    with open(tgt_projekt_backup_script, 'w') as f:
        f.write(template_content)

    os.chmod(tgt_projekt_backup_script, 0o755)

    logger.info(
        f"Successfully created PROJEKT backup script at: "
        f"{tgt_projekt_backup_script}"
    )

    # --- Copy and rename the exclusion_list.txt template ---
    exclusion_list_template_path = (
        "cfg/"
        "site-cfg/"
        "logik-projekt-cfg/"
        "logik-projekt-templates/"
        "rsync-backup-templates/"
        "exclusion_list.txt"
    )
    exclusion_list_output_name = (
        f"backup-"
        f"{projekt_summary_data['logik_projekt_name']}-"
        f"{projekt_summary_data['current_workstation']}-exclusion_list.txt"
    )
    exclusion_list_output_path = os.path.join(
        backup_script_dir,
        exclusion_list_output_name
    )

    with open(exclusion_list_template_path, 'r') as f_src:
        exclusion_list_content = f_src.read()

    with open(exclusion_list_output_path, 'w') as f_dst:
        f_dst.write(exclusion_list_content)

    logger.info(
        f"Exclusion list created at: {exclusion_list_output_path}"
    )

    # --- Create Crontab Script ---
    crontab_template_path = (
        "cfg/"
        "site-cfg/"
        "logik-projekt-cfg/"
        "logik-projekt-templates/"
        "rsync-backup-templates/"
        "backup_crontab_template.sh"
    )
    crontab_script_name = (
        f"add_backup_script_to_crontab-"
        f"{projekt_summary_data['logik_projekt_name']}-"
        f"{projekt_summary_data['current_workstation']}.sh"
    )
    tgt_projekt_crontab_script = os.path.join(
        backup_script_dir,
        crontab_script_name
    )

    with open(crontab_template_path, 'r') as f:
        crontab_template_content = f.read()

    crontab_replacements = {
        "%%LOGIK_PROJEKT_NAME%%": projekt_summary_data['logik_projekt_name'],
        "%%FLAME_PROJEKT_NAME%%": projekt_summary_data['flame_projekt_name'],
        "%%CURRENT_WORKSTATION%%": projekt_summary_data['current_workstation'],
        "%%LOGIK_PROJEKT_DIRECTORIES%%": os.path.dirname(
            projekt_summary_data['logik_projekt_path']
        ),
        "%%BACKUP_SCRIPT_NAME%%": backup_script_name,
    }

    for placeholder, value in crontab_replacements.items():
        crontab_template_content = crontab_template_content.replace(
            placeholder,
            str(value)
        )

    with open(tgt_projekt_crontab_script, 'w') as f:
        f.write(crontab_template_content)

    os.chmod(tgt_projekt_crontab_script, 0o755)

    logger.info(
        f"Backup crontab script created at: {tgt_projekt_crontab_script}"
    )


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