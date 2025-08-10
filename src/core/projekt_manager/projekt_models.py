#!/usr/bin/env python3
# -------------------------------------------------------------------------- #
# Filename:     projekt_models.py
# Purpose:      Define the data model for Autodesk Flame project configurations.
# Description:  This module defines the `ProjektParameters` dataclass, which encapsulates all the necessary parameters for creating and managing an Autodesk Flame project within the LOGIK-PROJEKT application.

# Author:       phil_man@mac.com
# Copyright:    Copyright (c) 2025
# Disclaimer:   Disclaimer at bottom of script.
# License:      GNU General Public License v3.0 (GPL-3.0).
#               https://www.gnu.org/licenses/gpl-3.0.en.html

# Version:      2026.1.0
# Status:       Production
# Type:         Module
# Created:      2025-07-01
# Modified:     2025-08-03

# Changelog:    Changelog at bottom of script.
# -------------------------------------------------------------------------- #

from dataclasses import (
    dataclass,
    field
)

from typing import (
    Optional
)


@dataclass
class ProjektParameters:
    # Environment Data
    current_user: str = ""
    current_group: str = ""
    current_workstation: str = ""
    current_os: str = ""

    # Flame Software Data
    flame_software_choice: str = ""
    flame_software_name: str = ""
    flame_software_version: str = ""
    flame_software_sanitized_name: str = ""
    flame_software_sanitized_version: str = ""

    # Flame Projekt Data
    flame_projekt_name: str = ""
    flame_projekt_nickname: str = ""
    flame_projekt_shotgun_name: str = ""
    flame_projekt_description: str = ""
    flame_projekt_home: str = ""
    flame_projekt_setups_dir: str = ""
    flame_projekt_media_dir: str = ""
    flame_projekt_catalog_dir: str = ""
    flame_projekt_width: str = ""
    flame_projekt_height: str = ""
    flame_projekt_ratio: str = ""
    flame_projekt_depth: str = ""
    flame_projekt_rate: str = ""
    flame_projekt_mode: str = ""
    flame_projekt_start: str = ""
    flame_projekt_init: str = ""
    flame_projekt_ocio: str = ""
    flame_projekt_ocio_path: str = ""
    flame_projekt_ocio_name: str = ""
    flame_projekt_cachef: str = ""
    flame_projekt_cachef_id: str = ""
    flame_projekt_cachei: str = ""
    flame_projekt_cachei_id: str = ""

    # LOGIK PROJEKT Data
    logik_projekt_name: str = ""
    logik_projekt_path: str = ""
    logik_projekt_config_name: str = ""
    logik_projekt_config_tree: str = ""
    logik_projekt_config_bookmarks: str = ""
    logik_projekt_config_workspace: str = ""

    # Workflow Options
    launch_flame_after_creation: bool = False


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
