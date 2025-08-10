#!/usr/bin/env python3
# -------------------------------------------------------------------------- #
# Filename:     create_timestamp.py
# Purpose:      Generates timestamp variables for Python processes.
# Description:  This module provides functions to create formatted date and time
#               strings, useful for logging, file naming, and tracking.

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

import datetime

def get_timestamp_variables():
    """
    generate timestamp variables in the same format as the bash script.
    """
    now = datetime.datetime.now()

    # define 'projekt_date' (use underscores instead of hyphens)
    projekt_date = now.strftime(
        "%Y_%m_%d"
    )

    # define 'projekt_time' (use underscores instead of colons)
    projekt_time = now.strftime(
        "%H_%M_%S"
    )

    # define 'projekt_now' (separated by a hyphen)
    projekt_now = f"{projekt_date}-{projekt_time}"

    return (
        projekt_date,
        projekt_time,
        projekt_now
    )


# if imported as a module, these variables will be available
projekt_date, projekt_time, projekt_now = get_timestamp_variables()


# if run directly, print the variables
if __name__ == "__main__":
    print(
        f"projekt_date: {projekt_date}"
    )
    print(
        f"projekt_time: {projekt_time}"
    )
    print(
        f"projekt_now: {projekt_now}"
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
