#!/usr/bin/env python3
# -------------------------------------------------------------------------- #
# Filename:     logik_projekt_utils.py
# Purpose:      Provides utility functions for LOGIK-PROJEKT configurations.
# Description:  This module contains functions for locating and parsing
#               LOGIK-PROJEKT configuration preferences from JSON files.

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

import json
from pathlib import Path
from src.core.utils.path_utils import get_repository_root_dir


def get_logik_projekt_config_prefs():
    repository_root_dir = get_repository_root_dir()
    prefs_file = (
        repository_root_dir
        / "pref"
        / "site-prefs"
        / "logik-projekt-site-prefs.json"
    )
    if not prefs_file.exists():
        return []
    try:
        with open(
            prefs_file,
            "r"
        ) as f:
            data = json.load(f)

        projekt_configs = data.get(
            "PROJEKT Configurations",
            []
        )

        if isinstance(projekt_configs, list):
            # Ensure each item in the list is a dictionary
            if all(isinstance(item, dict) for item in projekt_configs):
                return projekt_configs
            else:
                print(
                    f"Warning: 'PROJEKT Configurations' list "
                    f"contains non-dictionary items."
                )
                return []
        else:
            print("Warning: 'PROJEKT Configurations' is not a list.")
            return []

    except (
        json.JSONDecodeError,
        IOError
    ):
        return []


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
