#!/usr/bin/env python3
# -------------------------------------------------------------------------- #
# Filename:     create_banners.py
# Purpose:      Generates display banners for Python scripts.
# Description:  This module provides functions to create formatted banner lines
#               for use in script output or comments, ensuring consistent
#               visual separation and emphasis.

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


def repeat_char(
    char,
    count
):
    """
    function to repeat a character n times.
    """
    return char * count


def make_line_79_chars(
    line
):
    """
    function to ensure a line is exactly 79 characters.
    """
    current_length = len(line)

    # calculate the number of additional "=" characters needed
    pad = 79 - current_length

    # add the required pad before the " #" at the end
    line = line[:-2] + repeat_char(
        "=",
        pad
    ) + " #"

    return line


def generate_banner_line(
    banner
):
    """
    function to generate banner line.
    """
    total_length = 79

    # calculate pad on each side of the banner
    banner_pad_length = (
        total_length - len(banner) - 8
    ) // 2

    # generate the banner_line
    banner_line = (
        f"# {repeat_char('=', banner_pad_length)} {banner} "
        f"{repeat_char('=', banner_pad_length)} #"
    )

    # ensure banner_line is exactly 79 characters
    banner_line = make_line_79_chars(
        banner_line
    )

    return banner_line


def generate_banner_line_end(
    banner_end
):
    """
    function to generate banner end line.
    """
    total_length = 79

    # calculate pad on each side of the banner_end
    banner_end_pad_length = (
        total_length - len(banner_end) - 8
    ) // 2

    # generate the banner_end_line
    banner_end_line = (
        f"# {repeat_char('=', banner_end_pad_length)} {banner_end} "
        f"{repeat_char('=', banner_end_pad_length)} #"
    )

    # ensure banner_end_line is exactly 79 characters
    banner_end_line = make_line_79_chars(
        banner_end_line
    )

    return banner_end_line


def generate_banner_line_start(
    banner_start
):
    """
    function to generate banner start line.
    """
    total_length = 79

    # calculate pad on each side of the banner_start
    banner_start_pad_length = (
        total_length - len(banner_start) - 8
    ) // 2

    # generate the banner_start_line
    banner_start_line = (
        f"# {repeat_char('=', banner_start_pad_length)} {banner_start} "
        f"{repeat_char('=', banner_start_pad_length)} #"
    )

    # ensure banner_start_line is exactly 79 characters
    banner_start_line = make_line_79_chars(
        banner_start_line
    )

    return banner_start_line


# if run directly, test the functions
if __name__ == "__main__":
    print(
        generate_banner_line("test banner")
    )
    print(
        generate_banner_line_start("start")
    )
    print(
        generate_banner_line_end("end")
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
