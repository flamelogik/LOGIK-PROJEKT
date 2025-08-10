#!/usr/bin/env python3
# -------------------------------------------------------------------------- #
# Filename:     path_utils.py
# Purpose:      Provides utility functions for path manipulation.
# Description:  This module contains functions for determining the project root
#               directory and creating directories safely.

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
from pathlib import Path
import logging

logger = logging.getLogger(__name__)


def get_repository_root_dir(start_path=None):
    if start_path is None:
        current_path = Path(__file__).resolve()
    else:
        current_path = Path(start_path).resolve()

    # Primary method: Look for .git and src
    for parent in [current_path] + list(current_path.parents):
        git_exists = (parent / ".git").exists()
        src_exists = (parent / "src").exists()
        if git_exists and src_exists:
            return parent

    # Fallback method: Look for .repository_root.dir marker file
    for parent in [current_path] + list(current_path.parents):
        if (parent / ".repository_root.dir").exists():
            return parent

    logger.error("Could not find project root.")
    raise FileNotFoundError(
        f"Could not find project root. "
        f"Looked for (.git and src) or .repository_root.dir."
    )


def create_directory(path: str):
    """Creates a directory if it does not exist."""
    os.makedirs(path, exist_ok=True)


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
