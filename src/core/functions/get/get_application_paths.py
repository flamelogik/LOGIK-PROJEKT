#!/usr/bin/env python3
# -------------------------------------------------------------------------- #
# Filename:     get_application_paths.py
# Purpose:      Defines centralized paths for application resources.
# Description:  This module provides a single source of truth for various file
#               and directory paths used throughout the LOGIK-PROJEKT
#               application.

# Author:       phil_man@mac.com
# Copyright:    Copyright (c) 2025
# Disclaimer:   Disclaimer at bottom of script.
# License:      GNU General Public License v3.0 (GPL-3.0).
#               https://www.gnu.org/licenses/gpl-3.0.en.html

# Version:      2026.1.0
# Status:       Production
# Type:         Module
# Created:      2025-07-01
# Modified:     2025-10-08

# Changelog:    Changelog at bottom of script.
# -------------------------------------------------------------------------- #

import os

# Common Path Components
CFG_DIR = "cfg/"
SITE_CFG_DIR = CFG_DIR + "site-cfg/"
FLAME_CFG_DIR = SITE_CFG_DIR + "flame-cfg/"
FLAME_VALUE_LISTS_DIR = FLAME_CFG_DIR + "flame-value-lists/"
FLAME_TEMPLATES_DIR = FLAME_CFG_DIR + "flame-templates/"
PREF_DIR = "pref/"
SITE_PREFS_DIR = PREF_DIR + "site-prefs/"


class GetApplicationPaths:
    AUTODESK_SHARED_DIR = "/opt/Autodesk/shared/"
    BIT_DEPTH_LIST_VALUES = (
        FLAME_VALUE_LISTS_DIR +
        "bit_depth/" +
        "bit_depth_list_values.json"
    )
    CACHE_FLOAT_LIST_VALUES = (
        FLAME_VALUE_LISTS_DIR +
        "cache_format/" +
        "cache_float_list_values.json"
    )
    CACHE_INTEGER_LIST_VALUES = (
        FLAME_VALUE_LISTS_DIR +
        "cache_format/" +
        "cache_integer_list_values.json"
    )
    DEFAULT_TEMPLATE_VALUES = (
        SITE_PREFS_DIR +
        "default-prefs/" +
        "default_template_values.json"
    )
    FLAME_PRESETS_DIR = (
        FLAME_CFG_DIR +
        "flame-presets"
    )
    FLAME_PYTHON_SCRIPTS_DIR = (
        FLAME_CFG_DIR +
        "flame-python"
    )
    FRAME_RATE_LIST_VALUES = (
        FLAME_VALUE_LISTS_DIR +
        "frame_rate/" +
        "frame_rate_list_values.json"
    )
    INIT_CONFIG_DIR = (
        FLAME_VALUE_LISTS_DIR +
        "init_config"
    )
    LOGIK_PROJEKT_SITE_PREFS = (
        SITE_PREFS_DIR +
        "logik-projekt-site-prefs.json"
    )
    RESOLUTION_PATH = (
        FLAME_VALUE_LISTS_DIR +
        "resolution"
    )
    RESOLUTION_LOAD_ORDER_FILE = os.path.join(
        RESOLUTION_PATH,
        "resolution_load_order.json"
    )
    SCAN_MODE_LIST_VALUES = (
        FLAME_VALUE_LISTS_DIR +
        "scan_mode/" +
        "scan_mode_list_values.json"
    )
    SESSION_LOGS_DIR = (
        "logs/" +
        "session-logs"
    )
    SESSION_PREFERENCES_DIR = (
        PREF_DIR +
        "session-preferences"
    )
    SHARED_PRESETS_DIR = (
        FLAME_CFG_DIR +
        "shared-presets"
    )
    START_FRAME_LIST_VALUES = (
        FLAME_VALUE_LISTS_DIR +
        "start_frame/" +
        "start_frame_list_values.json"
    )
    SYSCONFIG_CFG = (
        FLAME_VALUE_LISTS_DIR +
        "sysconfig/" +
        "sysconfig.cfg"
    )
    WIRETAP_XML_TEMPLATE = (
        FLAME_TEMPLATES_DIR +
        "wiretap-templates/" +
        "wiretap_IFFFS_project_EXAMPLE.xml"
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
