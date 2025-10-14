#!/usr/bin/env python3
# -------------------------------------------------------------------------- #
# Filename:     import_logik_projekt_template.py
# Purpose:      Imports a LOGIK projekt template from a JSON file.
# Description:  This script reads template data from a JSON file, maps it to
#               internal data structures, and updates the current session.

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
from src.core.template_manager.template_models import (
    TemplateInfo,
    TemplateParameters,
)
from src.core.functions.io.export_logik_projekt_template import (
    export_logik_projekt_template
)


def import_logik_projekt_template(
    file_path: str,
) -> tuple[TemplateInfo, TemplateParameters, str]:
    """
    Import a LOGIK projekt template from a JSON file.

    Args:
        file_path: Path to the template JSON file

    Returns:
        Tuple containing TemplateInfo, TemplateParameters, and success message

    Raises:
        FileNotFoundError: If template file is not found
        json.JSONDecodeError: If JSON cannot be decoded
        Exception: For other unexpected errors
    """
    try:
        with open(file_path, 'r') as f:
            imported_data = json.load(f)

        # Map imported data to template_info_data and template_parameters_data
        template_info_data = {
            "template_serial_number": imported_data.get(
                "Template Serial Number: ",
                "",
            ),
            "template_client_name": imported_data.get(
                "Template Client Name: ",
                "",
            ),
            "template_campaign_name": imported_data.get(
                "Template Campaign Name: ",
                "",
            ),
            "template_calculated_name": imported_data.get(
                "Template Name: ",
                "",
            ),
            "template_description": imported_data.get(
                "Template Description: ",
                "",
            ),
        }

        template_parameters_data = {
            "template_resolution": imported_data.get(
                "Template Resolution: ",
                "",
            ),
            "template_resolution_w": imported_data.get(
                "Template Width: ",
                "",
            ),
            "template_resolution_h": imported_data.get(
                "Template Height: ",
                "",
            ),
            "template_aspect_ratio": imported_data.get(
                "Template Aspect Ratio: ",
                "",
            ),
            "template_bit_depth": imported_data.get(
                "Template Bit Depth: ",
                "",
            ),
            "template_framerate": imported_data.get(
                "Template Framerate: ",
                "",
            ),
            "template_scan_mode": imported_data.get(
                "Template Scan Mode: ",
                "",
            ),
            "template_start_frame": imported_data.get(
                "Template Start Frame: ",
                "",
            ),
            "template_init_config": imported_data.get(
                "Template Init Config: ",
                "",
            ),
            "template_ocio_config": imported_data.get(
                "Template OCIO Config: ",
                "",
            ),
            "template_cache_integer": imported_data.get(
                "Template Cache Integer: ",
                "",
            ),
            "template_cache_integer_id": imported_data.get(
                "Template Cache Integer ID: ",
                "",
            ),
            "template_cache_float": imported_data.get(
                "Template Cache Float: ",
                "",
            ),
            "template_cache_float_id": imported_data.get(
                "Template Cache Float ID: ",
                "",
            ),
        }

        # Call export_logik_projekt_template to update
        # current_session-template.json
        export_message = export_logik_projekt_template(
            template_info_data,
            template_parameters_data
        )

        # Return TemplateInfo and TemplateParameters objects for UI updates
        template_info = TemplateInfo(**template_info_data)
        template_parameters = TemplateParameters(**template_parameters_data)

        success_message = (
            f"Template successfully imported from: {file_path}\n"
            f"{export_message}"
        )

        return template_info, template_parameters, success_message

    except FileNotFoundError:
        raise FileNotFoundError(
            f"Error: Template file not found at {file_path}"
        )
    except json.JSONDecodeError as e:
        raise json.JSONDecodeError(
            f"Error: Could not decode JSON from {file_path}",
            doc=e.doc,
            pos=e.pos,
        )
    except Exception as e:
        raise Exception(
            f"An unexpected error occurred during import from {file_path}: {e}"
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
