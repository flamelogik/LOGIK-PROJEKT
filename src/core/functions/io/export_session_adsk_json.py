#!/usr/bin/env python3
# -------------------------------------------------------------------------- #
# Filename:     export_session_adsk_json.py
# Purpose:      Exports a JSON file with project data for Autodesk software.
# Description:  This script generates a JSON file containing a subset of
#               project data, formatted specifically for consumption by
#               Autodesk applications.

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

import json
import os
import logging

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)


def export_session_adsk_json(projekt_summary_data: dict):
    """
    Exports a JSON file with a subset of the project data
    for Autodesk software.
    """
    output_dir = "pref/session-preferences"
    output_filename = "current_session-adsk.json"
    output_path = os.path.join(output_dir, output_filename)

    os.makedirs(output_dir, exist_ok=True)

    def to_int(value):
        try:
            return int(float(value))
        except (ValueError, TypeError):
            logging.warning(f"Could not convert '{value}' to int.")
            return value

    def to_float(value):
        try:
            return float(value)
        except (ValueError, TypeError):
            logging.warning(f"Could not convert '{value}' to float.")
            return value

    adsk_data = {
        "Name": projekt_summary_data.get(
            "flame_projekt_name",
            ""
        ),
        "ProjectDir": projekt_summary_data.get(
            "flame_projekt_home",
            ""
        ),
        "SetupDir": projekt_summary_data.get(
            "flame_projekt_setups_dir", ""),
        "MediaDir": projekt_summary_data.get(
            "flame_projekt_media_dir", ""),
        "Resolution": {
            "FrameWidth": to_int(
                projekt_summary_data.get(
                    "flame_projekt_width"
                )
            ),
            "FrameHeight": to_int(
                projekt_summary_data.get(
                    "flame_projekt_height"
                )
            ),
            "FrameDepth": projekt_summary_data.get(
                "flame_projekt_depth",
                ""
            ),
            "AspectRatio": to_float(
                projekt_summary_data.get(
                    "flame_projekt_ratio"
                )
            ),
            "FieldDominance": projekt_summary_data.get(
                "flame_projekt_mode",
                ""
            )
        },
        "StartFrame": to_int(
            projekt_summary_data.get(
                "flame_projekt_start"
            )
        ),
        "ConfigTemplate": projekt_summary_data.get(
            "flame_projekt_init",
            ""
        ),
        "FrameRate": projekt_summary_data.get(
            "flame_projekt_rate",
            ""
        ),
        "IntermediatesProfile": to_int(
            projekt_summary_data.get(
                "flame_projekt_cachei_id"
            )
        ),
        "FloatIntermediates": to_int(
            projekt_summary_data.get(
                "flame_projekt_cachef_id"
                )
            ),
        "ColourPolicyName": projekt_summary_data.get(
            "flame_projekt_ocio_name",
            ""
        )
    }

    try:
        with open(output_path, 'w') as f:
            json.dump(adsk_data, f, indent=4)
        logging.info(
            f"ADSK session data exported successfully "
            f"to {output_path}")
    except Exception as e:
        logging.error(
            f"Error exporting ADSK session data "
            f"to {output_path}: {e}")


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
