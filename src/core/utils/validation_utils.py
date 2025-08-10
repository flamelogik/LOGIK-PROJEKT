#!/usr/bin/env python3
# -------------------------------------------------------------------------- #
# Filename:     validation_utils.py
# Purpose:      Provides utilities for input validation.
# Description:  This module contains functions to validate various input
#               parameters used throughout the application.

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

def validate_client_campaign_names(client_name: str, campaign_name: str) -> tuple[bool, str]:
    """
    Validates that client_name and campaign_name are not empty.
    """
    if not client_name.strip():
        return False, "Client Name cannot be empty."
    if not campaign_name.strip():
        return False, "Campaign Name cannot be empty."
    return True, ""


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


def validate_init_config(init_config_name: str, resolution_w: str, resolution_h: str, frame_rate: str) -> tuple[bool, str]:
    """
    Validates that the init_config name matches the resolution and framerate.
    """
    import re

    mismatch_found = False
    warning_message_parts = []

    # 1. Validate Resolution
    expected_resolution_string = f"{resolution_w}x{resolution_h}"
    if expected_resolution_string not in init_config_name:
        mismatch_found = True
        warning_message_parts.append("resolution")

    # 2. Validate Framerate
    # Extract numeric part from init_config_name (e.g., "1920x1080@25000p.cfg" -> "25000")
    init_config_framerate_match = re.search(r'@(\d+)(p|psf)?\.cfg', init_config_name)
    init_config_framerate_num = ""
    if init_config_framerate_match:
        init_config_framerate_num = init_config_framerate_match.group(1)

    # Extract numeric part from selected frame_rate (e.g., "25.000 fps" -> "25000")
    selected_frame_rate_num = frame_rate.replace(".", "").replace(" fps", "").strip()

    if init_config_framerate_num != selected_frame_rate_num:
        mismatch_found = True
        warning_message_parts.append("framerate")

    if mismatch_found:
        message = "Your " + " and / or ".join(warning_message_parts) + " do not match your Init Config. Continue anyway?"
        return False, message
    else:
        return True, ""


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

def validate_logik_projekt_name(logik_projekt_name: str) -> tuple[bool, str]:
    """
    Validates that logik_projekt_name is not empty.
    """
    if not logik_projekt_name.strip():
        return False, "LOGIK Projekt Name cannot be empty."
    return True, ""


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
