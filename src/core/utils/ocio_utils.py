#!/usr/bin/env python3
# -------------------------------------------------------------------------- #
# Filename:     ocio_utils.py
# Purpose:      Provides utilities for OpenColorIO (OCIO) config management.
# Description:  This module contains functions to discover OCIO configurations
#               on the system and extract relevant details from them.

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


def get_ocio_config_name(file_path):
    try:
        with open(file_path, 'r') as f:
            for line in f:
                if line.strip().startswith("name:"):
                    return line.split("name:", 1)[1].strip()
    except Exception:
        pass
    return None


def GetOCIOConfigs(
        base_dir=(
            "/opt/"
            "Autodesk/"
            "colour_mgmt/"
            "configs"
        )
):
    ocio_configs = []

    for root, dirs, files in os.walk(base_dir):
        if "flame_internal_use" in root:
            continue
        if "config.ocio" in files:
            ocio_cfg_path = (
                os.path.join(
                    root,
                    "config.ocio"
                )
            )
            relative_dir = (
                os.path.relpath(
                    root,
                    base_dir
                )
            )
            ocio_name = (
                get_ocio_config_name(
                    ocio_cfg_path
                )
            )
            ocio_configs.append(
                (
                    relative_dir,
                    ocio_name
                )
            )

    return ocio_configs


def get_ocio_details_from_relative_path(
    relative_path: str,
) -> tuple[str, str]:
    base_dir = (
        "/opt/"
        "Autodesk/"
        "colour_mgmt/"
        "configs"
    )
    full_path = os.path.join(
        base_dir,
        relative_path,
        "config.ocio",
    )
    ocio_name = get_ocio_config_name(full_path)
    return ocio_name, full_path


def get_ocio_name(ocio_config_string: str) -> str:
    """Extracts the OCIO name from a given OCIO config string.
    This is a placeholder and would need actual parsing logic.
    """
    if "/" in ocio_config_string:
        return (
            ocio_config_string.split("/")[-1]
            .replace(".ocio", "")
        )
    return ocio_config_string


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
