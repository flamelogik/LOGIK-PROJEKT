#!/usr/bin/env python3
# -------------------------------------------------------------------------- #
# Filename:     get_resolution_values.py
# Purpose:      Retrieves resolution values from JSON configuration files.
# Description:  This script reads resolution data from multiple JSON files,
#               following a specified load order, to populate UI selection options.

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
import os
from src.core.functions.get.get_application_paths import GetApplicationPaths


def get_resolution_values() -> list[dict]:
    resolution_path = GetApplicationPaths.RESOLUTION_PATH
    load_order_file = GetApplicationPaths.RESOLUTION_LOAD_ORDER_FILE
    resolutions = []
    try:
        with open(load_order_file, 'r') as f:
            load_order = json.load(f)

        for filename in load_order:
            json_file_path = os.path.join(
                resolution_path,
                filename
            )
            if os.path.exists(
                json_file_path
            ):
                with open(
                    json_file_path,
                    'r'
                ) as f_res:
                    data = json.load(
                        f_res
                    )
                if "items" in data:
                    for item_group in data["items"]:
                        if "items" in item_group:
                            for resolution in item_group["items"]:
                                if "resolution_name" in resolution:
                                    resolutions.append(
                                        resolution
                                    )
        return resolutions
    except FileNotFoundError:
        print(
            f"Error: Resolution config files not found."
        )
        return []
    except json.JSONDecodeError:
        print(
            f"Error: Could not decode JSON from resolution config files."
        )
        return []
    except Exception as e:
        print(
            f"Error loading resolution values: {e}"
        )
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
