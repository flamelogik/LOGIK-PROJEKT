#!/usr/bin/env python3
# -------------------------------------------------------------------------- #
# Filename:     get_sysconfig_flame_home_dir.py
# Purpose:      Retrieves the default Flame home directory from sysconfig.
# Description:  This script reads the sysconfig.cfg file to obtain the
#               predefined default path for Flame project home directories.

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
from src.core.functions.get.get_application_paths import GetApplicationPaths


def get_sysconfig_flame_home_dir() -> str:
    """
    Load default Flame home directory from configuration.

    Returns:
        Default home directory path string
    """
    sysconfig_cfg_path = GetApplicationPaths.SYSCONFIG_CFG
    default_path = "/var/opt/Autodesk/flame/projects/<project name>"

    try:
        with open(sysconfig_cfg_path, 'r') as f:
            config_data = json.load(f)

        return (
            config_data.get("configuration", {})
            .get("settings", {})
            .get("project_folders", {})
            .get("default_home", default_path)
        )
    except FileNotFoundError:
        print(
            f"Error: sysconfig.cfg not found at:"
            f"{sysconfig_cfg_path}"
        )
        return default_path
    except json.JSONDecodeError:
        print(
            f"Error: Could not decode JSON from:"
            f"{sysconfig_cfg_path}"
        )
        return default_path
    except Exception as e:
        print(
            f"Error loading default Flame catalog directory:"
            f"{e}"
        )
        return default_path


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
