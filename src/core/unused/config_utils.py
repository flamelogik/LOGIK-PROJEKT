import json
from pathlib import Path
import os
from src.core.utils.path_utils import get_repository_root_dir

def find_json_dir_path(subdirectory=None):
    repository_root_dir = get_repository_root_dir()
    json_path = repository_root_dir / "config" / "flame-configuration"
    if subdirectory:
        json_path = json_path / subdirectory

    if not json_path.exists():
        raise FileNotFoundError(f"JSON directory not found: {json_path}")

    return json_path


def find_xml_directory(subdirectory=None):
    repository_root_dir = get_repository_root_dir()
    xml_path = repository_root_dir / "config" / "parameters" / "xml"

    if subdirectory:
        xml_path = xml_path / subdirectory

    if not xml_path.exists():
        raise FileNotFoundError(f"XML directory not found: {xml_path}")

    return xml_path


def find_cfg_directory(subdirectory=None):
    repository_root_dir = get_repository_root_dir()
    cfg_path = repository_root_dir / "config" / "flame-configuration"

    if subdirectory:
        cfg_path = cfg_path / subdirectory

    if not cfg_path.exists():
        raise FileNotFoundError(f"CFG directory not found: {cfg_path}")

    return cfg_path


def find_txt_directory(subdirectory=None):
    repository_root_dir = get_repository_root_dir()
    txt_path = repository_root_dir / "config" / "parameters" / "txt"

    if subdirectory:
        txt_path = txt_path / subdirectory

    if not txt_path.exists():
        raise FileNotFoundError(f"TXT directory not found: {txt_path}")

    return txt_path


def find_parameters_directory(file_type, subdirectory=None):
    file_type = file_type.lower()

    if file_type == "json":
        return find_json_dir_path(subdirectory)
    elif file_type == "xml":
        return find_xml_directory(subdirectory)
    elif file_type == "cfg":
        return find_cfg_directory(subdirectory)
    elif file_type == "txt":
        return find_txt_directory(subdirectory)
    else:
        raise ValueError(f"Unsupported file type: {file_type}. Must be one of: json, xml, cfg, txt")



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
