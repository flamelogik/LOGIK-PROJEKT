#!/usr/bin/env python3
# -------------------------------------------------------------------------- #
# Filename:     get_projekt_summary_data.py
# Purpose:      Generates a summary of project data.
# Description:  This script compiles various pieces of information related to
#               the project, including environment details, Flame software
#               data, and LOGIK-PROJEKT configurations, into a single
#               dictionary.

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

from src.core.template_manager.template_models import (
    TemplateInfo,
    TemplateParameters,
)
from src.core.utils.system_info_utils import (
    get_current_user,
    get_primary_group,
    get_short_hostname,
)
from src.core.utils.flame_software_utils import (
    get_installed_flame_versions,
    sanitize_flame_version_name,
    sanitize_flame_version_number,
)
from src.core.utils import ocio_utils


def get_projekt_summary_data(
    template_info: TemplateInfo,
    template_parameters: TemplateParameters,
    flame_options_data: dict,
) -> dict:
    """
    Generate project summary data from template and flame options.

    Args:
        template_info: Template information object
        template_parameters: Template parameters object
        flame_options_data: Flame configuration options

    Returns:
        Dictionary containing all project summary data
    """
    # Environment Data
    current_user = get_current_user()["username"]
    current_group = get_primary_group()
    current_workstation = get_short_hostname()
    current_os = "linux"  # Placeholder for actual OS detection

    # Flame Software Data
    flame_software_choice = flame_options_data.get(
        "flame_software_choice", ""
    )

    # Extract software name (e.g., 'flame')
    flame_software_name = (
        flame_software_choice.split("_")[0]
        if "_" in flame_software_choice
        else flame_software_choice
    )
    flame_software_version = (
        flame_software_choice.split("_", 1)[1]
        if "_" in flame_software_choice
        else ""
    )

    flame_software_sanitized_name = sanitize_flame_version_name(
        flame_software_name
    )
    flame_software_sanitized_version = sanitize_flame_version_number(
        flame_software_choice
    )

    # Flame Projekt Data
    flame_projekt_name = (
        f"{template_info.template_calculated_name}_"
        f"{flame_software_sanitized_version}_"
        f"{current_workstation}"
    )
    flame_projekt_nickname = template_info.template_calculated_name
    flame_projekt_shotgun_name = template_info.template_calculated_name
    flame_projekt_description = template_info.template_description
    flame_projekt_home = flame_options_data.get("flame_home_directory", "")
    flame_projekt_setups_dir_raw = flame_options_data.get(
        "flame_setups_directory",
        "",
    )

    # Resolve flame_projekt_setups_dir based on rules
    if "<project home>" in flame_projekt_setups_dir_raw:
        flame_projekt_setups_dir = f"{flame_projekt_home}/setups"
    elif (
        flame_projekt_setups_dir_raw
        and template_info.template_calculated_name
    ):
        flame_projekt_setups_dir = (
            f"{flame_projekt_setups_dir_raw}/"
            f"{template_info.template_calculated_name}/setups"
        )
    else:
        flame_projekt_setups_dir = flame_projekt_setups_dir_raw

    flame_projekt_media_dir_raw = flame_options_data.get(
        "flame_media_directory",
        "",
    )

    # Resolve flame_projekt_media_dir based on rules
    if "<project home>" in flame_projekt_media_dir_raw:
        flame_projekt_media_dir = f"{flame_projekt_home}/media"
    elif (
        flame_projekt_media_dir_raw
        and template_info.template_calculated_name
    ):
        flame_projekt_media_dir = (
            f"{flame_projekt_media_dir_raw}/"
            f"{template_info.template_calculated_name}/media"
        )
    else:
        flame_projekt_media_dir = flame_projekt_media_dir_raw

    flame_projekt_catalog_dir_raw = flame_options_data.get(
        "flame_catalog_directory",
        "",
    )

    # Resolve flame_projekt_catalog_dir based on rules
    if "<project home>" in flame_projekt_catalog_dir_raw:
        flame_projekt_catalog_dir = f"{flame_projekt_home}/catalog"
    elif (
        flame_projekt_catalog_dir_raw
        and template_info.template_calculated_name
    ):
        # If user chose a custom path and project name is available,
        # append project name and /catalog
        flame_projekt_catalog_dir = (
            f"{flame_projekt_catalog_dir_raw}/"
            f"{template_info.template_calculated_name}/catalog"
        )
    else:
        # Fallback for empty path or no project name yet
        flame_projekt_catalog_dir = flame_projekt_catalog_dir_raw

    flame_projekt_width = template_parameters.template_resolution_w
    flame_projekt_height = template_parameters.template_resolution_h
    flame_projekt_ratio = template_parameters.template_aspect_ratio
    flame_projekt_depth = template_parameters.template_bit_depth
    flame_projekt_rate = template_parameters.template_framerate
    flame_projekt_mode = template_parameters.template_scan_mode
    flame_projekt_start = template_parameters.template_start_frame
    flame_projekt_init = template_parameters.template_init_config
    flame_projekt_ocio = template_parameters.template_ocio_config

    (
        flame_projekt_ocio_name,
        flame_projekt_ocio_path,
    ) = ocio_utils.get_ocio_details_from_relative_path(flame_projekt_ocio)

    flame_projekt_cachef = template_parameters.template_cache_float
    flame_projekt_cachef_id = template_parameters.template_cache_float_id
    flame_projekt_cachei = template_parameters.template_cache_integer
    flame_projekt_cachei_id = (
        template_parameters.template_cache_integer_id
    )

    # LOGIK PROJEKT Data
    logik_projekt_name = template_info.template_calculated_name
    logik_projekt_path = (
        f"/PROJEKTS/{template_info.template_calculated_name}"
    )
    logik_projekt_config_data = flame_options_data.get(
        "logik_projekt_config", {}
    )
    logik_projekt_config_name = logik_projekt_config_data.get(
        "PROJEKT Configuration Name", ""
    )
    logik_projekt_config_tree = logik_projekt_config_data.get(
        "PROJEKT Filesystem Tree", ""
    )
    logik_projekt_config_bookmarks = logik_projekt_config_data.get(
        "PROJEKT Flame Bookmarks", ""
    )
    logik_projekt_config_workspace = logik_projekt_config_data.get(
        "PROJEKT Flame Workspace", ""
    )

    return {
        "current_user": current_user,
        "current_group": current_group,
        "current_workstation": current_workstation,
        "current_os": current_os,
        "flame_software_choice": flame_software_choice,
        "flame_software_name": flame_software_name,
        "flame_software_version": flame_software_version,
        "flame_software_sanitized_name":
            flame_software_sanitized_name,
        "flame_software_sanitized_version":
            flame_software_sanitized_version,
        "flame_projekt_name": flame_projekt_name,
        "flame_projekt_nickname": flame_projekt_nickname,
        "flame_projekt_shotgun_name":
            flame_projekt_shotgun_name,
        "flame_projekt_description": flame_projekt_description,
        "flame_projekt_home": flame_projekt_home,
        "flame_projekt_setups_dir": flame_projekt_setups_dir,
        "flame_projekt_media_dir": flame_projekt_media_dir,
        "flame_projekt_catalog_dir": flame_projekt_catalog_dir,
        "flame_projekt_width": flame_projekt_width,
        "flame_projekt_height": flame_projekt_height,
        "flame_projekt_ratio": flame_projekt_ratio,
        "flame_projekt_depth": flame_projekt_depth,
        "flame_projekt_rate": flame_projekt_rate,
        "flame_projekt_mode": flame_projekt_mode,
        "flame_projekt_start": flame_projekt_start,
        "flame_projekt_init": flame_projekt_init,
        "flame_projekt_ocio": flame_projekt_ocio,
        "flame_projekt_ocio_path": flame_projekt_ocio_path,
        "flame_projekt_ocio_name": flame_projekt_ocio_name,
        "flame_projekt_cachef": flame_projekt_cachef,
        "flame_projekt_cachef_id": flame_projekt_cachef_id,
        "flame_projekt_cachei": flame_projekt_cachei,
        "flame_projekt_cachei_id": flame_projekt_cachei_id,
        "logik_projekt_name": logik_projekt_name,
        "logik_projekt_path": logik_projekt_path,
        "logik_projekt_config_name": logik_projekt_config_name,
        "logik_projekt_config_tree": logik_projekt_config_tree,
        "logik_projekt_config_bookmarks":
            logik_projekt_config_bookmarks,
        "logik_projekt_config_workspace":
            logik_projekt_config_workspace,
    }


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