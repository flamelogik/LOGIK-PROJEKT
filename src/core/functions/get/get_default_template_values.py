#!/usr/bin/env python3
# -------------------------------------------------------------------------- #
# Filename:     get_default_template_values.py
# Purpose:      Retrieves default template values from a configuration file.
# Description:  This script loads predefined default parameters for templates
#               from a JSON file, mapping them to appropriate keys.

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


def get_default_template_values() -> dict:
    """
    Load default template parameters from configuration file.

    Returns:
        Dictionary containing mapped default parameters
    """
    default_template_values_path = GetApplicationPaths.DEFAULT_TEMPLATE_VALUES

    try:
        with open(default_template_values_path, 'r') as f:
            defaults = json.load(f)

        # Map JSON keys to TemplateParameters keys
        mapped_defaults = {
            "template_resolution": defaults.get(
                "Default Resolution: ",
                ""
            ),
            "template_resolution_w": defaults.get(
                "Default Width: ",
                ""
            ),
            "template_resolution_h": defaults.get(
                "Default Height: ",
                ""
            ),
            "template_aspect_ratio": defaults.get(
                "Default Aspect Ratio: ",
                ""
            ),
            "template_bit_depth": defaults.get(
                "Default Bit Depth: ",
                ""
            ),
            "template_framerate": defaults.get(
                "Default Framerate: ",
                ""
            ),
            "template_scan_mode": defaults.get(
                "Default Scan Mode: ",
                ""
            ),
            "template_start_frame": defaults.get(
                "Default Start Frame: ",
                ""
            ),
            "template_init_config": defaults.get(
                "Default Init Config: ",
                ""
            ),
            "template_ocio_config": defaults.get(
                "Default OCIO Config: ",
                ""
            ),
            "template_cache_integer": defaults.get(
                "Default Cache Integer: ",
                "",
            ),
            "template_cache_integer_id": defaults.get(
                "Default Cache Integer ID: ",
                "",
            ),
            "template_cache_float": defaults.get(
                "Default Cache Float: ",
                ""
            ),
            "template_cache_float_id": defaults.get(
                "Default Cache Float ID: ",
                "",
            ),
            "template_logik_projekt_config_name": defaults.get(
                "Default Logik Projekt Config",
                "",
            ),
        }
        return mapped_defaults

    except FileNotFoundError:
        print(
            f"Error: Default values file not found at:"
            f"{default_template_values_path}"
        )
        return {}
    except json.JSONDecodeError:
        print(
            f"Error: Could not decode JSON from"
            f"{default_template_values_path}"
        )
        return {}


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
