#!/usr/bin/env python3
# -------------------------------------------------------------------------- #
# Filename:     create_flame_launcher_script.py
# Purpose:      Creates a Flame launcher script for the project.
# Description:  This script generates a shell script to launch Autodesk Flame
#               with the correct project and environment settings.

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


def create_flame_launcher_script(
    repository_root_dir: str,
    logik_projekt_path: str,
    current_workstation: str,
    current_os: str,
    the_projekts_dir: str,
    the_projekt_flame_dirs: str,
    the_adsk_dir: str,
    the_adsk_dir_linux: str,
    the_adsk_dir_macos: str,
    logik_projekt_name: str,
    the_projekt_flame_name: str,
    flame_software_sanitized_version: str,
    flame_software_choice: str,
    flame_projekt_setups_dir: str,
):
    """
    Creates a Flame launcher script for the project.

    Args:
        repository_root_dir (str): Root directory of the application.
        logik_projekt_path (str): Full path to the created PROJEKT directory.
        current_workstation (str): Hostname of the workstation.
        current_os (str): Operating system of the project.
        the_projekts_dir (str): Root directory for all projects.
        the_projekt_flame_dirs (str): Root directory for Flame projects.
        the_adsk_dir (str): Autodesk installation directory.
        the_adsk_dir_linux (str): The Autodesk install dir for Linux.
        the_adsk_dir_macos (str): The Autodesk install dir for macOS.
        logik_projekt_name (str): The name of the project.
        the_projekt_flame_name (str): The Flame-specific project name.
        flame_software_sanitized_version (str): Sanitized software version.
        flame_software_choice (str): The full software version.
    """

    logger.info(
        f"Creating PROJEKT flame launcher script for {logik_projekt_name} "
        f"on {current_workstation}."
    )

    the_projekt_dir_path = os.path.join(
        the_projekts_dir,
        logik_projekt_name
    )
    the_projekt_flame_dir_path = os.path.join(
        the_projekt_flame_dirs,
        the_projekt_flame_name
    )

    os.umask(0)

    tgt_launcher_script = os.path.join(
        repository_root_dir,
        'pref',
        'session-preferences',
        'current_session-flame_launcher.sh'
    )

    os.makedirs(
        os.path.dirname(tgt_launcher_script),
        exist_ok=True
    )

    src_launcher_template = (
        "cfg/"
        "site-cfg/"
        "flame-cfg/"
        "flame-templates/"
        "flame-launcher-templates/"
        "flame_launcher_template.sh"
    )

    with open(src_launcher_template, 'r') as f:
        template_content = f.read()

    app_starter = ""
    software_choice_lower = flame_software_choice.lower()

    # Initialize replacements with default values
    replacements = {
        "%%FLAME_STARTUP_SCRIPT_PY%%": (
            "scripts/startup/flame_startup_script.py"
        ),
        "%%LAUNCHER_SCRIPT_PROJEKT%%": the_projekt_flame_name,
        "%%SCRIPT_CREATION_DATE%%": datetime.datetime.now().strftime(
            "%Y-%m-%d %H:%M:%S"
        ),
        "%%LOGIK_PROJEKT_PATH%%": logik_projekt_path,
        "%%LOGIK_PROJEKT_NAME%%": logik_projekt_name,
        "%%FLAME_PROJEKT_NAME%%": the_projekt_flame_name,
        "%%CURRENT_WORKSTATION%%": current_workstation,
        "%%FLAME_FIRST_RUN_NAME%%": "current_session-flame_launcher.log",
        "%%FLAME_SOFTWARE_CHOICE%%": flame_software_choice,
        "%%APPLICATION_STARTER%%": app_starter,  # Will be updated below
        "%%FLAME_PROJEKT_SETUPS_DIR%%": flame_projekt_setups_dir,
    }

    if 'flame' in software_choice_lower:
        app_starter = 'startFlame'
    elif 'flare' in software_choice_lower:
        app_starter = 'startFlare'
    elif 'assist' in software_choice_lower:
        app_starter = 'startFlameAssist'

    # Update the app_starter in replacements after it's determined
    replacements["%%APPLICATION_STARTER%%"] = app_starter

    for placeholder, value in replacements.items():
        template_content = (
            template_content.replace(placeholder, str(value))
        )

    with open(tgt_launcher_script, 'w') as f:
        f.write(template_content)

    os.chmod(tgt_launcher_script, 0o755)

    logger.info(
        f"Successfully modified PROJEKT flame launcher: {tgt_launcher_script}"
    )

    # Define the additional target path
    additional_target_dir = os.path.join(
        flame_projekt_setups_dir,
        "scripts",
        "startup"
    )
    additional_target_path = os.path.join(
        additional_target_dir,
        "flame_launcher_script.sh"
    )

    # Ensure the additional target directory exists
    os.makedirs(additional_target_dir, exist_ok=True)

    # Copy the launcher script to the additional target
    shutil.copy2(tgt_launcher_script, additional_target_path)
    os.chmod(additional_target_path, 0o755)  # Ensure it's executable

    logger.info(
        f"Copied Flame launcher script to: {additional_target_path}"
    )

    return tgt_launcher_script


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
