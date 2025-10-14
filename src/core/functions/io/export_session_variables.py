#!/usr/bin/env python3
# -------------------------------------------------------------------------- #
# Filename:     export_session_variables.py
# Purpose:      Exports session variables to a JSON file.
# Description:  This script takes a dictionary of project summary data and
#               saves it as a JSON file, representing the current session's 
#               variables.

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


def export_session_variables(
        projekt_summary_data: dict
):
    output_dir = (
        "pref/"
        "session-preferences"
    )
    output_filename = (
        "current_session-variables.json"
    )
    output_path = (
        os.path.join(
            output_dir,
            output_filename
        )
    )

    os.makedirs(
        output_dir,
        exist_ok=True
    )

    try:
        with open(
            output_path,
            'w'
        ) as f:
            json.dump(
                projekt_summary_data,
                f,
                indent=4
            )
        print(
            f"Projekt summary data exported successfully to {output_path}"
        )
    except Exception as e:
        print(
            f"Error exporting projekt summary data to {output_path}: {e}"
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
