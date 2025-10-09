#!/usr/bin/env python3
# -------------------------------------------------------------------------- #
# Filename:     get_flame_bookmarks_path.py
# Purpose:      Retrieves the path to the Flame bookmarks JSON file.
# Description:  This script determines the absolute path to the Flame bookmarks
#               file based on the LOGIK-PROJEKT configuration name.

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

import json
import os
from pathlib import Path
import logging

from src.core.functions.get.get_application_paths import (
    GetApplicationPaths
)
from src.core.utils.path_utils import get_repository_root_dir

logger = logging.getLogger(__name__)


def get_flame_bookmarks_path(logik_projekt_config_name: str) -> str:
    """
    Retrieves the path to the Flame bookmarks JSON file based on the
    LOGIK-PROJEKT configuration name.

    Args:
        logik_projekt_config_name (str): The name of the LOGIK-PROJEKT
                                         configuration.

    Returns:
        str: The absolute path to the Flame bookmarks JSON file.

    Raises:
        FileNotFoundError: If the site preferences file or the specified
                           bookmarks file is not found.
        ValueError: If the LOGIK-PROJEKT configuration name is not found.
    """
    try:
        repository_root_dir = get_repository_root_dir()
        site_prefs_file = (
            repository_root_dir / GetApplicationPaths.LOGIK_PROJEKT_SITE_PREFS
        )

        if not site_prefs_file.exists():
            error_message = (
                f"Site preferences file not found: {site_prefs_file}"
            )
            raise FileNotFoundError(error_message)

        with open(site_prefs_file, 'r') as f:
            site_prefs_data = json.load(f)

        for config_entry in site_prefs_data.get("PROJEKT Configurations", []):
            if (
                config_entry.get("PROJEKT Configuration Name")
                == logik_projekt_config_name
            ):
                relative_bookmarks_path = config_entry.get(
                    "PROJEKT Flame Bookmarks"
                )
                if relative_bookmarks_path:
                    absolute_bookmarks_path = (
                        repository_root_dir / relative_bookmarks_path
                    )
                    if not absolute_bookmarks_path.exists():
                        error_message = (
                            "Flame bookmarks file not found: "
                            f"{absolute_bookmarks_path}"
                        )
                        raise FileNotFoundError(error_message)
                    return str(absolute_bookmarks_path)
                else:
                    error_message = (
                        f"'PROJEKT Flame Bookmarks' path not found for "
                        f"configuration: {logik_projekt_config_name}"
                    )
                    raise ValueError(error_message)

        error_message = (
            f"LOGIK-PROJEKT configuration not found: "
            f"{logik_projekt_config_name}"
        )
        raise ValueError(error_message)

    except Exception as e:
        logger.error(f"Error getting Flame bookmarks path: {e}")
        raise


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