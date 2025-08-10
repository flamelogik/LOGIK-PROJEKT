#!/usr/bin/env python3
# -------------------------------------------------------------------------- #
# Filename:     calculated_name_utils.py
# Purpose:      Provides utility functions for generating calculated names.
# Description:  This module contains functions to sanitize and combine input
#               parts (serial, client, campaign) into a standardized calculated name.

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

"""
Utility functions for generating calculated names.
"""
import re
from datetime import datetime


def _sanitize_part(part: str) -> str:
    """
    Sanitizes a single part of a name.

    - Replaces spaces with underscores.
    - Removes any characters that are not alphanumeric, underscore,
      or hyphen.
    """
    # Replace spaces and other problematic characters with underscores
    part = re.sub(r'[\s/:]+', '_', part)
    # Remove any remaining characters that are not standard for filenames
    part = re.sub(r'[^a-zA-Z0-9_-]', '', part)
    return part


def get_calculated_name(serial: str, client: str, campaign: str) -> str:
    """
    Generates and sanitizes a calculated name from serial, client,
    and campaign parts.

    --- ARTIST-FRIENDLY MODIFICATION AREA ---
    To change the naming convention, please follow these steps:
    1. Choose ONE of the "RECIPE" options below.
    2. Make sure the line for your chosen recipe starts with
    "calculated_name =".
    3. To disable a recipe, add a '#' at the beginning of its line.
    4. Make sure only ONE "calculated_name =" line is active (not commented out).
    ---
    """
    # --- Pre-Sanitization (do not modify) ---
    # Clean up each part before combining them.
    s_serial = _sanitize_part(serial)
    s_client = _sanitize_part(client)
    s_campaign = _sanitize_part(campaign)

    # --- RECIPE 1: Serial, lowercase client, lowercase campaign ---
    # This is the default.
    calculated_name = f"{s_serial}_{s_client.lower()}_{s_campaign.lower()}"

    # --- RECIPE 2: Serial, UPPERCASE client, UPPERCASE campaign ---
    # To use this recipe, remove the '#' from the line below and add a '#'
    # to the beginning of the line for RECIPE 1.
    # calculated_name = f"{s_serial}_{s_client.upper()}_{s_campaign.upper()}"

    # --- RECIPE 3: No serial, lowercase client, lowercase campaign ---
    # calculated_name = f"{s_client.lower()}_{s_campaign.lower()}"

    # --- RECIPE 4: Serial, Title Case client, Title Case campaign ---
    # calculated_name = f"{s_serial}_{s_client.title()}_{s_campaign.title()}"

    # --- RECIPE 5: Date (YYYY-MM-DD) serial, lowercase client, lowercase campaign ---
    # This recipe ignores the 'serial' input and uses today's date.
    # date_serial_long = datetime.now().strftime('%Y-%m-%d')
    # calculated_name = f"{date_serial_long}_{s_client.lower()}_{s_campaign.lower()}"

    # --- RECIPE 6: Date (YYMMDD) serial, lowercase client, lowercase campaign ---
    # This recipe ignores the 'serial' input and uses today's date.
    # date_serial_short = datetime.now().strftime('%y%m%d')
    # calculated_name = f"{date_serial_short}_{s_client.lower()}_{s_campaign.lower()}"

    # --- RECIPE 7: Lowercase client, lowercase campaign, serial ---
    # calculated_name = f"{s_client.lower()}_{s_campaign.lower()}_{s_serial}"

    # --- RECIPE 8: UPPERCASE client, UPPERCASE campaign, serial ---
    # calculated_name = f"{s_client.upper()}_{s_campaign.upper()}_{s_serial}"

    # --- RECIPE 9: Title Case client, Title Case campaign, serial ---
    # calculated_name = f"{s_client.title()}_{s_campaign.title()}_{s_serial}"


    # --- Final Sanitization (do not modify below this line) ---
    # Replace double underscores (from empty parts) with single underscores
    while "__" in calculated_name:
        calculated_name = calculated_name.replace("__", "_")

    # Remove any leading or trailing underscores
    calculated_name = calculated_name.strip('_')

    return calculated_name


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
