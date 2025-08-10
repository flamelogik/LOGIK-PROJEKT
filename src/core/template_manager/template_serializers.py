#!/usr/bin/env python3
# -------------------------------------------------------------------------- #
# Filename:     template_serializers.py
# Purpose:      Serialize and deserialize template data to/from JSON.
# Description:  This module provides the `TemplateSerializer` class, which
#               handles the conversion of `TemplateInfo` and
#               `TemplateParameters` objects to and from JSON format for
#               persistent storage and retrieval.

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

import json
from src.core.template_manager.template_models import (
    TemplateInfo,
    TemplateParameters
)


class TemplateSerializer:
    @staticmethod
    def save_to_json(
        template_info: TemplateInfo,
        template_parameters: TemplateParameters,
        file_path: str
    ):
        data = {
            "Template Serial Number": template_info.serial_number,
            "Template Client Name": template_info.client_name,
            "Template Campaign Name": template_info.campaign_name,
            "Template Name": template_info.calculated_name,
            "Template Description": template_info.description,
            "Template Resolution": template_parameters.resolution,
            "Template Width": template_parameters.resolution_w,
            "Template Height": template_parameters.resolution_h,
            "Template Aspect Ratio": template_parameters.aspect_ratio,
            "Template Bit Depth": template_parameters.bit_depth,
            "Template Framerate": template_parameters.framerate,
            "Template Scan Mode": template_parameters.scan_mode,
            "Template Start Frame": template_parameters.start_frame,
            "Template Init Config": template_parameters.init_config,
            "Template OCIO Config": template_parameters.ocio_config,
            "Template OCIO Path": template_parameters.ocio_path,
            "Template OCIO Name": template_parameters.ocio_name,
            "Template Cache Integer": template_parameters.cache_integer,
            "Template Cache Integer ID": template_parameters.cache_integer_id,
            "Template Cache Float": template_parameters.cache_float,
            "Template Cache Float ID":
                template_parameters.cache_float_id,
        }
        with open(file_path, 'w') as f:
            json.dump(data, f, indent=4)

    @staticmethod
    def load_from_json(file_path: str) -> dict:
        with open(file_path, 'r') as f:
            return json.load(f)

    @staticmethod
    def deserialize_template_data(
        data: dict
    ) -> tuple[TemplateInfo, TemplateParameters]:
        info = TemplateInfo(
            serial_number=data.get("Template Serial Number", ""),
            client_name=data.get("Template Client Name", ""),
            campaign_name=data.get("Template Campaign Name", ""),
            calculated_name=data.get("Template Name", ""),
            description=data.get("Template Description", "")
        )
        params = TemplateParameters(
            resolution=data.get("Template Resolution", ""),
            resolution_w=data.get("Template Width", ""),
            resolution_h=data.get("Template Height", ""),
            aspect_ratio=data.get("Template Aspect Ratio", ""),
            bit_depth=data.get("Template Bit Depth", ""),
            framerate=data.get("Template Framerate", ""),
            scan_mode=data.get("Template Scan Mode", ""),
            start_frame=data.get("Template Start Frame", ""),
            init_config=data.get("Template Init Config", ""),
            ocio_config=data.get("Template OCIO Config", ""),
            ocio_path=data.get("Template OCIO Path", ""),
            ocio_name=data.get("Template OCIO Name", ""),
            cache_integer=data.get("Template Cache Integer", ""),
            cache_integer_id=data.get("Template Cache Integer ID", ""),
            cache_float=data.get("Template Cache Float", ""),
            cache_float_id=data.get("Template Cache Float ID", "")
        )
        return info, params


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
