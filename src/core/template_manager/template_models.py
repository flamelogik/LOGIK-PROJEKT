#!/usr/bin/env python3
# -------------------------------------------------------------------------- #
# Filename:     template_models.py
# Purpose:      Define data models for project templates.
# Description:  This module defines `TemplateInfo` and `TemplateParameters`
#               dataclasses, used to structure data for project templates
#               within the LOGIK-PROJEKT application.

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

from dataclasses import dataclass, field
from typing import Optional


@dataclass
class TemplateInfo:
    template_serial_number: str = ""
    template_client_name: str = ""
    template_campaign_name: str = ""
    template_calculated_name: str = ""
    template_description: str = ""


@dataclass
class TemplateParameters:
    template_resolution: str = ""
    template_resolution_w: str = ""
    template_resolution_h: str = ""
    template_aspect_ratio: str = ""
    template_bit_depth: str = ""
    template_framerate: str = ""
    template_scan_mode: str = ""
    template_start_frame: str = ""
    template_init_config: str = ""
    template_ocio_config: str = ""
    template_ocio_name: str = ""
    template_ocio_path: str = ""
    template_cache_integer: str = ""
    template_cache_integer_id: str = ""
    template_cache_float: str = ""
    template_cache_float_id: str = ""


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
