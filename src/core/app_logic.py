#!/usr/bin/env python3
# -------------------------------------------------------------------------- #
# Filename:     app_logic.py
# Purpose:      Handle core application logic for LOGIK-PROJEKT.
# Description:  This module provides the `AppLogic` class, which orchestrates
#               the import/export of project templates, retrieval of default
#               values, generation of project summary data, and the creation
#               of new Autodesk Flame projects.

# Author:       phil_man@mac.com
# Copyright:    Copyright (c) 2025
# Disclaimer:   Disclaimer at bottom of script.
# License:      GNU General Public License v3.0 (GPL-3.0).
#               https://www.gnu.org/licenses/gpl-3.0.en.html

# Version:      2026.1.0
# Status:       Production
# Type:         Module
# Created:      2025-07-01
# Modified:     2025-08-03

# Changelog:    Changelog at bottom of script.
# -------------------------------------------------------------------------- #

import json
import os


# from core.unused import config_utils
from src.core.projekt_manager.projekt_creator import (
    ProjektCreator
)
from src.core.projekt_manager.projekt_models import (
    ProjektParameters
)
from src.core.template_manager.template_handler import (
    TemplateHandler
)
from src.core.template_manager.template_models import (
    TemplateInfo,
    TemplateParameters,
)
from src.core.utils import (
    ocio_utils
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
    get_cache_format_id,
)
from src.core.functions.io.export_logik_projekt_template import (
    export_logik_projekt_template
)
from src.core.functions.io.import_logik_projekt_template import (
    import_logik_projekt_template
)
from src.core.functions.get.get_default_template_values import (
    get_default_template_values
)
from src.core.functions.get.get_projekt_summary_data import (
    get_projekt_summary_data
)


from src.core.projekt_manager.projekt_creator import (
    create_projekt
)


class AppLogic:
    """Application logic handler for template and project management."""

    def __init__(self):
        """Initialize the AppLogic with required handlers."""
        self.template_handler = TemplateHandler()
        self.projekt_creator = ProjektCreator()

    def import_logik_projekt_template(
        self,
        file_path: str,
    ) -> tuple[TemplateInfo, TemplateParameters, str]:
        """
        Import a LOGIK projekt template from a JSON file.
      
        Args:
            file_path: Path to the template JSON file
          
        Returns:
            Tuple containing TemplateInfo, TemplateParameters,
            and success message
          
        Raises:
            FileNotFoundError: If template file is not found
            json.JSONDecodeError: If JSON cannot be decoded
            Exception: For other unexpected errors
        """
        return import_logik_projekt_template(file_path)

    def export_logik_projekt_template(
        self,
        template_info_data: dict,
        template_params_data: dict
    ) -> str:
        """
        Export template data to current_session-template.json file.
      
        Args:
            template_info_data: Template information dictionary
            template_params_data: Template parameters dictionary
          
        Returns:
            Success message string
          
        Raises:
            Exception: If export fails
        """
        return export_logik_projekt_template(
            template_info_data,
            template_params_data
        )

    def get_default_template_values(self) -> dict:
        """
        Load default template parameters from configuration file.
      
        Returns:
            Dictionary containing mapped default parameters
        """
        return get_default_template_values()

    def get_projekt_summary_data(
        self,
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
        return get_projekt_summary_data(
            template_info,
            template_parameters,
            flame_options_data
        )

    def create_projekt(self, projekt_summary_data: dict):
        """
        Create a new project using the provided summary data.
      
        Args:
            projekt_summary_data:   Dictionary containing all
                                    project configuration data
        """
        create_projekt(projekt_summary_data)


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
