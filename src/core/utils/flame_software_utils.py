#!/usr/bin/env python3
# -------------------------------------------------------------------------- #
# Filename:     flame_software_utils.py
# Purpose:      Utilities for interacting with Autodesk Flame software.
# Description:  This module contains functions for detecting installed Flame
#               versions, sanitizing version names, and parsing Flame configs.

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

import os
import re
import platform


def get_installed_flame_versions() -> list[str]:
    directory = "/opt/Autodesk"
    flame_family_prefixes = [
        "flame",
        "flare",
        "flame_assist",
    ]

    def _sort_key(directory_name):
        pattern = (
            r"(\w+)_(\d+)(?:\.(\d+))?(?:\.(\d+))?(?:\.(pr\d+))?"
        )
        match = (
            re.search(
                pattern,
                directory_name
            )
        )
        if not match:
            return (0, 0, 0, 0, 0)

        name = match.group(1)
        major = int(match.group(2)) if match.group(2) else 0
        minor = int(match.group(3)) if match.group(3) else 0
        patch = int(match.group(4)) if match.group(4) else 0
        prerelease = match.group(5) or ""

        app_importance = {
            "flame": 3,
            "flare": 2,
            "flame_assist": 1,
        }
        app_value = app_importance.get(name, 0)

        prerelease_value = (
            999 if not prerelease else int(prerelease[2:])
        )

        return (
            app_value,
            major,
            minor,
            patch,
            prerelease_value,
        )

    try:
        if not os.path.exists(directory):
            print(f"Directory {directory} does not exist")
            return []

        entries = os.listdir(directory)

        flame_dirs = [
            entry
            for entry in entries
            if any(
                entry.startswith(prefix) for prefix in flame_family_prefixes
            )
            and os.path.isdir(os.path.join(directory, entry))
        ]

        flame_dirs = sorted(
            flame_dirs,
            key=_sort_key,
            reverse=True,
        )

        # Return raw directory names
        return flame_dirs

    except PermissionError:
        print(f"Permission denied accessing {directory}")
        return []
    except Exception as e:
        print(f"An error occurred while scanning {directory}: {e}")
        return []


def sanitize_flame_version_name(name: str) -> str:
    """Sanitizes a Flame version name (e.g., 'Flame' -> 'flame')."""
    return name.lower().replace(" ", "_")


def sanitize_flame_version_number(app_name: str) -> str:
    """Sanitizes a Flame version number from the full application name string.

    Example: 'flame_2026.1.pr224' -> '2026_1'
            (or '2026_1_pr224' if prerelease is kept)
    """
    # Regex to capture the version part (e.g., 2026.1.pr224 or 2026.pr219)
    pattern = r"_(\d+(?:\.\d+)*(?:\.pr\d+)?)$"
    match = re.search(pattern, app_name)

    if match:
        version_part = match.group(1)
        # Remove 'pr' and subsequent numbers if present, and replace
        # dots with underscores
        # This assumes you want '2026_1' from '2026.1.pr224'
        # If you want to keep the 'pr' part, adjust the regex or this line
        sanitized_version = (
            re.sub(r"\.pr\d+", "", version_part).replace(".", "_")
            )
        return sanitized_version

    return ""


def parse_flame_config(config_content: str) -> dict:
    """Parses Flame configuration content (e.g., sysconfig.cfg) and
    returns a dictionary.
    This is a placeholder and would need actual parsing logic based
    on the config format.
    """
    print("Parsing Flame config content...")
    # Example: if it's a simple key-value pair per line
    parsed_data = {}
    for line in config_content.splitlines():
        if ":" in line:
            key, value = line.split(":", 1)
            parsed_data[key.strip()] = value.strip()
    return parsed_data


def get_cache_format_id(cache_string: str) -> str:
    """Extracts a code/ID from a cache string
    (e.g., '10-bit Log' -> '10bitlog').
    This is a placeholder and would need actual parsing logic.
    """
    return cache_string.lower().replace("-", "").replace(" ", "")


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
