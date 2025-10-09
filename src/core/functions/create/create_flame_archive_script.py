#!/usr/bin/env python3
# -------------------------------------------------------------------------- #
# Filename:     create_flame_archive_script.py
# Purpose:      Creates a Flame archive script for a project.
# Description:  This script generates a shell script to archive Flame projects
#               and a corresponding crontab entry for automated archiving.

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
import datetime
import shutil

logger = logging.getLogger(__name__)


def create_flame_archive_script(projekt_summary_data: dict):

    logger.info(
        f"Creating PROJEKT flame archive script for "
        f"{projekt_summary_data['logik_projekt_name']} on "
        f"{projekt_summary_data['current_workstation']}."
    )

    the_projekt_dir = (
        projekt_summary_data['logik_projekt_path']
    )

    os.umask(0)

    tgt_flame_archive_dir = os.path.join(
        the_projekt_dir,
        'flame',
        'archive',
    )

    os.makedirs(
        tgt_flame_archive_dir,
        exist_ok=True
    )

    tgt_workstation_flame_archive_dir = os.path.join(
        the_projekt_dir,
        'flame',
        'archive',
        projekt_summary_data['current_workstation'],
    )

    os.makedirs(
        tgt_workstation_flame_archive_dir,
        exist_ok=True
    )

    src_archive_template = (
        "cfg/"
        "site-cfg/"
        "flame-cfg/"
        "flame-templates/"
        "flame-archive-templates/"
        "archive_script_template"
    )

    src_archive_crontab_template = (
        "cfg/"
        "site-cfg/"
        "flame-cfg/"
        "flame-templates/"
        "flame-archive-templates/"
        "archive_script_to_crontab_template.sh"
    )

    archive_script_name = (
        f"archive_script-"
        f"{projekt_summary_data['logik_projekt_name']}-"
        f"{projekt_summary_data['current_workstation']}.sh"
    )

    tgt_projekt_archive_script = os.path.join(
        tgt_flame_archive_dir,
        "scripts",
        archive_script_name
    )

    tgt_projekt_archive_crontab = os.path.join(
        tgt_flame_archive_dir,
        "scripts",
        f"add_archive_script_to_crontab-"
        f"{projekt_summary_data['logik_projekt_name']}-"
        f"{projekt_summary_data['current_workstation']}.sh"
    )

    with open(src_archive_template, 'r') as f:
        template_content = f.read()

    replacements = {
        "%%ARCHIVE_SCRIPT_NAME%%": archive_script_name,
        "%%ARCHIVE_SCRIPT_PROJEKT%%": projekt_summary_data[
            'flame_projekt_name'
        ],
        "%%SCRIPT_CREATION_DATE%%": datetime.datetime.now().strftime(
            '%Y-%m-%d %H:%M:%S'
        ),
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
        template_content = (
            template_content.replace(
                placeholder,
                str(value)
            )
        )

    os.makedirs(
        os.path.dirname(tgt_projekt_archive_script),
        exist_ok=True
    )
    with open(tgt_projekt_archive_script, 'w') as f:
        f.write(template_content)

    os.chmod(
        tgt_projekt_archive_script,
        0o755
    )

    logger.info(
        f"Successfully created PROJEKT flame archive script to: "
        f"{tgt_projekt_archive_script}"
    )

    os.makedirs(
        os.path.dirname(tgt_projekt_archive_crontab),
        exist_ok=True
    )
    with open(src_archive_crontab_template, 'r') as f:
        crontab_template_content = f.read()

    crontab_replacements = {
        "%%LOGIK_PROJEKT_NAME%%": projekt_summary_data['logik_projekt_name'],
        "%%FLAME_PROJEKT_NAME%%": projekt_summary_data['flame_projekt_name'],
        "%%CURRENT_WORKSTATION%%": projekt_summary_data['current_workstation'],
        "%%LOGIK_PROJEKT_DIRECTORIES%%": os.path.dirname(
            projekt_summary_data['logik_projekt_path']
        ),
        "%%ARCHIVE_SCRIPT_NAME%%": archive_script_name,
    }

    for placeholder, value in crontab_replacements.items():
        crontab_template_content = crontab_template_content.replace(
            placeholder,
            str(value)
        )

    with open(tgt_projekt_archive_crontab, 'w') as f:
        f.write(crontab_template_content)

    os.chmod(
        tgt_projekt_archive_crontab,
        0o755
    )

    logger.info(
        f"Successfully created PROJEKT flame archive crontab script to: "
        f"{tgt_projekt_archive_crontab}"
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
