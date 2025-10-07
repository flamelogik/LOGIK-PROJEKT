#!/usr/bin/env python3
# -------------------------------------------------------------------------- #
# Filename:     copy_init_config.py
# Purpose:      Copy a Flame init.cfg file to the projekt setups directory
# Description:  This script copies a specified init.cfg file to the 'cfg'
#               subdirectory of a Flame project's setup directory.
# Author:       phil_man@mac.com
# Copyright:    Copyright (c) 2025
# License:      GNU General Public License v3.0 (GPL-3.0).
# -------------------------------------------------------------------------- #

import os
import shutil
import logging
from pathlib import Path

from src.core.utils.path_utils import get_repository_root_dir

logger = logging.getLogger(__name__)

def copy_init_config(init_config_filename: str, setups_dir: str, flame_projekt_name: str):
    """
    Copies the Flame init.cfg file to the project's setup directory and
    renames it to <flame_projekt_name>.cfg.

    Args:
        init_config_filename (str): The filename of the init.cfg file to copy.
        setups_dir (str): The path to the Flame project's setups directory.
        flame_projekt_name (str): The name of the Flame project.
    """
    if not init_config_filename:
        logger.warning("No init.cfg filename provided. Skipping copy.")
        return

    if not flame_projekt_name:
        logger.error("No flame_projekt_name provided. Cannot rename init.cfg.")
        return

    try:
        repo_root = Path(get_repository_root_dir())
        source_path = repo_root / 'cfg/site-cfg/flame-cfg/flame-value-lists/init_config' / init_config_filename

        if not source_path.is_file():
            logger.warning(f"Source init.cfg file not found: {source_path}")
            return

        destination_dir = Path(setups_dir) / 'cfg'
        destination_path = destination_dir / f"{flame_projekt_name}.cfg"

        logger.info(f"Copying init.cfg from '{source_path}' to '{destination_path}'")
        destination_dir.mkdir(parents=True, exist_ok=True)
        shutil.copy2(source_path, destination_path)
        logger.info("Successfully copied and renamed init.cfg.")

    except Exception as e:
        logger.error(f"Failed to copy init.cfg: {e}")


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
