#!/usr/bin/env python3
# -------------------------------------------------------------------------- #
# Filename:     template_handler.py
# Purpose:      Manage template saving, loading, and retrieval.
# Description:  This module provides the `TemplateHandler` class for saving,
#               loading, and listing project templates. It uses
#               `TemplateSerializer` for data persistence and interacts with
#               `TemplateInfo` and `TemplateParameters` models.

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

from src.core.template_manager.template_models import (
    TemplateInfo,
    TemplateParameters
)
from src.core.template_manager.template_serializers import (
    TemplateSerializer
)
from src.core.utils.path_utils import (
    get_repository_root_dir,
    create_directory
)
import os


class TemplateHandler:
    def __init__(self):
        self.template_serializer = TemplateSerializer()

    def export_template(
            self,
            template_info: TemplateInfo,
            template_parameters: TemplateParameters,
            file_name: str
        ):
        # Define the path where templates will be saved
        template_dir = (
            os.path.join(
                get_repository_root_dir(),
                "config",
                "logik-projekt-configuration",
                "logik-projekt-templates"
            )
        )
        create_directory(
            template_dir
        )
        file_path = os.path.join(
            template_dir,
            file_name
        )
        self.template_serializer.save_to_json(
            template_info,
            template_parameters,
            file_path
        )
        print(
            f"Template saved to: {file_path}"
            )

    def import_template(self, file_path: str) -> tuple[TemplateInfo, TemplateParameters]:
        loaded_data = (
            self.template_serializer.load_from_json(file_path)
        )
        template_info, template_parameters = (
            self.template_serializer.deserialize_template_data(loaded_data)
        )
        print(
            f"Template loaded from: {file_path}"
        )
        return template_info, template_parameters

    def get_available_templates(self) -> list[str]:
        template_dir = os.path.join(get_repository_root_dir(), "config", "logik-projekt-configuration", "logik-projekt-templates")
        if not os.path.exists(template_dir):
            return []
        return [f for f in os.listdir(template_dir) if f.endswith(".json")]


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
