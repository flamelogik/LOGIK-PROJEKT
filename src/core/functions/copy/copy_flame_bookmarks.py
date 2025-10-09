#!/usr/bin/env python3
# -------------------------------------------------------------------------- #
# Filename:     copy_flame_bookmarks.py
# Purpose:      Copies Flame bookmarks to a specified directory.
# Description:  This script handles the copying of the cf_bookmarks.json file
#               to ensure consistent Flame project configurations.

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

import os
import shutil
import logging

logger = logging.getLogger(__name__)


def copy_flame_bookmarks(source_path: str, destination_dir: str):
    """
    Copies the cf_bookmarks.json file to the specified destination directory.

    Args:
        source_path (str): The absolute path to the source
            cf_bookmarks.json file.
        destination_dir (str): The absolute path to the destination
            directory (e.g., flame_projekt_setups_dir/status/).
    """
    try:
        os.makedirs(destination_dir, exist_ok=True)

        destination_path = os.path.join(
            destination_dir,
            os.path.basename(source_path)
        )

        shutil.copy2(source_path, destination_path)

        logger.info(
            "Successfully copied Flame bookmarks from %s to %s",
            source_path,
            destination_path
        )

    except FileNotFoundError:
        logger.error(
            "Source Flame bookmarks file not found: %s",
            source_path
        )
        raise

    except Exception as e:
        logger.error("Error copying Flame bookmarks: %s", e)
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
