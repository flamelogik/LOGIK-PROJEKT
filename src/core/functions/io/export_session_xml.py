#!/usr/bin/env python3
# -------------------------------------------------------------------------- #
# Filename:     export_session_xml.py
# Purpose:      Processes an XML template and exports the result.
# Description:  This script takes an XML template, replaces placeholders with
#               data from a dictionary, and saves the processed XML to a file.

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

import xml.etree.ElementTree as ET
import os
import logging
from src.core.functions.get.get_application_paths import GetApplicationPaths

logger = logging.getLogger(__name__)


def export_session_xml(data: dict, template_path: str, output_path: str):
    """
    Processes an XML template, replacing placeholders with values from
    a dictionary, and writes the result to an output XML file.

    Args:
        data (dict): The dictionary containing data to populate the template.
        template_path (str): The absolute path to the XML template file.
        output_path (str): The absolute path where the processed XML file
        will be saved.
    """
    try:
        tree = ET.parse(GetApplicationPaths.WIRETAP_XML_TEMPLATE)
        root = tree.getroot()

        def replace_placeholders(element, data_dict):
            # Sort keys by length in descending order to avoid
            # partial replacements
            sorted_keys = sorted(data_dict.keys(), key=len, reverse=True)
            for child in element:
                if child.text:
                    for key in sorted_keys:
                        value = data_dict[key]
                        placeholder = f"{key}"
                        if placeholder in child.text:
                            child.text = child.text.replace(
                                placeholder,
                                str(value)
                            )
                replace_placeholders(child, data_dict)

        replace_placeholders(root, data)

        os.makedirs(os.path.dirname(output_path), exist_ok=True)
        tree.write(output_path, encoding="utf-8", xml_declaration=True)
        logging.info(
            f"XML generated successfully from template "
            f"and saved to {output_path}")

    except FileNotFoundError:
        logging.error(f"Error: Template file not found at {template_path}")
    except Exception as e:
        logging.error(f"Error processing XML template: {e}")


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
