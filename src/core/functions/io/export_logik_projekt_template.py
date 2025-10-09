#!/usr/bin/env python3
# -------------------------------------------------------------------------- #
# Filename:     export_logik_projekt_template.py
# Purpose:      Exports template data to a JSON file.
# Description:  This script takes template information and parameters, formats
#               them, and saves them to a JSON file for later use.

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
from src.core.utils import ocio_utils


def export_logik_projekt_template(
    template_info_data: dict,
    template_params_data: dict,
) -> str:
    """
    Export template data to current_session-template.json file.

    Args:
        template_info_data: Template information dictionary
        template_params_data: Template parameters dictionary

    Returns:
        Success message string

    Raises:
        Exception: If export fails
    """
    # Get OCIO details directly from template_params_data
    ocio_config_path = template_params_data.get("template_ocio_config", "")
    template_ocio_name, template_ocio_path = (
        ocio_utils.get_ocio_details_from_relative_path(ocio_config_path)
    )

    # Map the template info and parameters data to the desired keys for
    # the current_session-template.json
    exported_data = {
        "Template Serial Number: ": template_info_data.get(
            "template_serial_number",
            "",
        ),
        "Template Client Name: ": template_info_data.get(
            "template_client_name",
            "",
        ),
        "Template Campaign Name: ": template_info_data.get(
            "template_campaign_name",
            "",
        ),
        "Template Name: ": template_info_data.get(
            "template_calculated_name",
            "",
        ),
        "Template Description: ": template_info_data.get(
            "template_description",
            "",
        ),
        "Template Resolution: ": template_params_data.get(
            "template_resolution",
            "",
        ),
        "Template Width: ": template_params_data.get(
            "template_resolution_w",
            "",
        ),
        "Template Height: ": template_params_data.get(
            "template_resolution_h",
            "",
        ),
        "Template Aspect Ratio: ": template_params_data.get(
            "template_aspect_ratio",
            "",
        ),
        "Template Bit Depth: ": template_params_data.get(
            "template_bit_depth",
            "",
        ),
        "Template Framerate: ": template_params_data.get(
            "template_framerate",
            "",
        ),
        "Template Scan Mode: ": template_params_data.get(
            "template_scan_mode",
            "",
        ),
        "Template Start Frame: ": template_params_data.get(
            "template_start_frame",
            "",
        ),
        "Template Init Config: ": template_params_data.get(
            "template_init_config",
            "",
        ),
        "Template OCIO Config: ": ocio_config_path,
        "Template OCIO Path: ": template_ocio_path,
        "Template OCIO Name: ": template_ocio_name,
        "Template Cache Integer: ": template_params_data.get(
            "template_cache_integer",
            "",
        ),
        "Template Cache Integer ID: ": template_params_data.get(
            "template_cache_integer_id",
            "",
        ),
        "Template Cache Float: ": template_params_data.get(
            "template_cache_float",
            "",
        ),
        "Template Cache Float ID: ": template_params_data.get(
            "template_cache_float_id",
            "",
        ),
    }

    # Define the output path
    output_dir = "pref/session-preferences"
    output_filename = "current_session-template.json"
    output_path = os.path.join(output_dir, output_filename)

    # Ensure the directory exists
    os.makedirs(output_dir, exist_ok=True)

    # Write the JSON data to the file
    try:
        with open(output_path, 'w') as f:
            json.dump(exported_data, f, indent=4)
        return f"Template exported successfully to {output_path}"
    except Exception as e:
        raise Exception(f"Error exporting template to {output_path}: {e}")


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
