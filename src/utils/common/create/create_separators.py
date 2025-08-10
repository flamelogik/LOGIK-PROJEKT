#!/usr/bin/env python3
# -------------------------------------------------------------------------- #
# Filename:     create_separators.py
# Purpose:      Generates display separators for Python scripts.
# Description:  This module provides functions to create formatted separator
#               lines for use in script output or comments, enhancing readability.

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


def get_separator_variables():
    """
    generate separator variables in the same format as the bash script.
    """
    # define a variable called 'separator_plus'
    separator_plus = (
        '+ ' + '-' * 75 + ' +'
    )

    # define a variable called 'separator_hash'
    separator_hash = (
        '# ' + '-' * 75 + ' #'
    )

    return (
        separator_plus,
        separator_hash
    )


# if imported as a module, these variables will be available
separator_plus, separator_hash = get_separator_variables()

# if run directly, print the variables
if __name__ == "__main__":
    print(
        f"separator_plus: {separator_plus}"
    )
    print(
        f"separator_hash: {separator_hash}"
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
