#!/usr/bin/env python3
# -------------------------------------------------------------------------- #
# Filename:     flame_options_panel.py
# Purpose:      Panel for configuring Flame software options and directory paths.
# Description:  This panel allows users to select Flame software versions and define
#               various directory paths related to Flame projects.

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

from src.ui import ui_config
from PySide6.QtWidgets import (
    QWidget,
    QGridLayout,
    QFileDialog
)
from PySide6.QtCore import (
    Signal,
    Slot
)

from src.ui.widgets.combobox.flame_software_choice_widget import (
    FlameSoftwareChoiceWidget
)
from src.ui.widgets.button.flame_home_dir_widget import (
    FlameHomeDirWidget
)
from src.ui.widgets.button.flame_setups_dir_widget import (
    FlameSetupsDirWidget
)
from src.ui.widgets.button.flame_media_dir_widget import (
    FlameMediaDirWidget
)
from src.ui.widgets.button.flame_catalog_dir_widget import (
    FlameCatalogDirWidget
)
from src.ui.widgets.combobox.projekt_config_widget import (
    ProjektConfigWidget
)

from src.core.functions.get.get_sysconfig_flame_home_dir import get_sysconfig_flame_home_dir
from src.core.functions.get.get_sysconfig_flame_setups_dir import get_sysconfig_flame_setups_dir
from src.core.functions.get.get_sysconfig_flame_media_dir import get_sysconfig_flame_media_dir
from src.core.functions.get.get_sysconfig_flame_catalog_dir import get_sysconfig_flame_catalog_dir
from src.core.functions.get.get_flame_software_versions import get_flame_software_versions
from src.core.functions.get.get_logik_projekt_config_values import get_logik_projekt_config_values


class FlameOptionsPanel(QWidget):
    """Panel for configuring Flame software options and directory paths."""
  
    path_changed = Signal()  # Custom signal
  
    def __init__(self, master=None, default_params: dict = None):
        """Initialize the FlameOptionsPanel widget.
      
        Args:
            master: Parent widget
        """
        super().__init__(master)
        self.default_params = default_params or {}
        self._setup_layout()
        self._create_widgets()
        self._populate_widgets()

    def _setup_layout(self):
        """Set up the main grid layout with proper spacing and margins."""
        self.layout = QGridLayout(self)
        self.layout.setSpacing(ui_config.PANEL_LAYOUT_SPACING)
        self.layout.setContentsMargins(*ui_config.PANEL_PADDING)
        self.layout.setColumnMinimumWidth(0, 160)
        self.layout.setColumnStretch(1, 1)

    def _create_widgets(self):
        """Create and add all widgets to the layout."""
        row = 0
      
        # Flame Software Choice
        self.flame_software_choice_widget = FlameSoftwareChoiceWidget(self)
        self.layout.addWidget(
            self.flame_software_choice_widget.label,
            row,
            0
        )
        self.layout.addWidget(
            self.flame_software_choice_widget.combobox,
            row,
            1
        )
        self.flame_software_choice_widget.label.setFixedWidth(160)
        row += 1

        # Flame Projekt Directory
        self.flame_home_dir_widget = FlameHomeDirWidget(
            self,
            command=self._select_flame_home_dir
        )
        default_home_dir = get_sysconfig_flame_home_dir()
        self.flame_home_dir_widget.set_path(default_home_dir)
        self.layout.addWidget(
            self.flame_home_dir_widget.label,
            row,
            0
        )
        self.layout.addWidget(
            self.flame_home_dir_widget.button,
            row,
            1
        )
        self.flame_home_dir_widget.label.setFixedWidth(160)
        row += 1

        # Flame Setups Directory
        self.flame_setups_dir_widget = FlameSetupsDirWidget(
            self,
            command=self._select_flame_setups_dir
        )
        default_setups_dir = get_sysconfig_flame_setups_dir()
        self.flame_setups_dir_widget.set_path(default_setups_dir)
        self.layout.addWidget(
            self.flame_setups_dir_widget.label,
            row,
            0
        )
        self.layout.addWidget(
            self.flame_setups_dir_widget.button,
            row,
            1
        )
        self.flame_setups_dir_widget.label.setFixedWidth(160)
        row += 1

        # Flame Media Directory
        self.flame_media_dir_widget = FlameMediaDirWidget(
            self,
            command=self._select_flame_media_dir
        )
        default_media_dir = get_sysconfig_flame_media_dir()
        self.flame_media_dir_widget.set_path(default_media_dir)
        self.layout.addWidget(
            self.flame_media_dir_widget.label,
            row,
            0
        )
        self.layout.addWidget(
            self.flame_media_dir_widget.button,
            row,
            1
        )
        self.flame_media_dir_widget.label.setFixedWidth(160)
        row += 1

        # Flame Catalog Directory
        self.flame_catalog_dir_widget = FlameCatalogDirWidget(
            self,
            command=self._select_flame_catalog_dir
        )
        self.layout.addWidget(
            self.flame_catalog_dir_widget.label,
            row,
            0
        )
        self.layout.addWidget(
            self.flame_catalog_dir_widget.button,
            row,
            1
        )
        self.flame_catalog_dir_widget.label.setFixedWidth(160)
        row += 1
      
        default_catalog_dir = get_sysconfig_flame_catalog_dir()
        self.flame_catalog_dir_widget.set_path(default_catalog_dir)

        # LOGIK-PROJEKT Config
        self.logik_projekt_config_widget = ProjektConfigWidget(self)
        self.layout.addWidget(
            self.logik_projekt_config_widget.label,
            row,
            0
        )
        self.layout.addWidget(
            self.logik_projekt_config_widget.combobox,
            row,
            1
        )
        self.logik_projekt_config_widget.label.setFixedWidth(160)
        row += 1

        # Connect comboboxes to emit path_changed signal
        self.flame_software_choice_widget.combobox.currentIndexChanged.connect(self._emit_path_changed)
        self.logik_projekt_config_widget.combobox.currentIndexChanged.connect(self._emit_path_changed)

    def _emit_path_changed(self):
        self.path_changed.emit()

    def _populate_widgets(self):
        """Populate widgets with data from app logic."""
        flame_versions = get_flame_software_versions()
        self.flame_software_choice_widget.set_values(flame_versions)
      
        projekt_config_values = get_logik_projekt_config_values()
        self.logik_projekt_config_widget.set_values(projekt_config_values)
      
        # Set default value for ProjektConfigWidget
        default_config_name = self.default_params.get("template_logik_projekt_config_name", "")
        if default_config_name:
            self.logik_projekt_config_widget.set(default_config_name)

    def _select_flame_home_dir(self):
        """Open dialog to select Flame home directory."""
        dir_path = QFileDialog.getExistingDirectory(
            self,
            "Select Flame Home Directory"
        )
        if dir_path:
            self.flame_home_dir_widget.set_path(dir_path)
            self.path_changed.emit()

    def _select_flame_setups_dir(self):
        """Open dialog to select Flame setups directory."""
        dir_path = QFileDialog.getExistingDirectory(
            self,
            "Select Flame Setups Directory"
        )
        if dir_path:
            self.flame_setups_dir_widget.set_path(dir_path)
            self.path_changed.emit()

    def _select_flame_media_dir(self):
        """Open dialog to select Flame media directory."""
        dir_path = QFileDialog.getExistingDirectory(
            self,
            "Select Flame Media Directory"
        )
        if dir_path:
            self.flame_media_dir_widget.set_path(dir_path)
            self.path_changed.emit()

    def _select_flame_catalog_dir(self):
        """Open dialog to select Flame catalog directory."""
        dir_path = QFileDialog.getExistingDirectory(
            self,
            "Select Flame Catalog Directory"
        )
        if dir_path:
            self.flame_catalog_dir_widget.set_path(dir_path)
            self.path_changed.emit()

    def get_flame_options(self):
        """Get current flame options as a dictionary.
      
        Returns:
            dict: Dictionary containing all flame option values
        """
        return {
            "flame_software_choice": (
                self.flame_software_choice_widget.get()
            ),
            "flame_home_directory": (
                self.flame_home_dir_widget.get_path()
            ),
            "flame_setups_directory": (
                self.flame_setups_dir_widget.get_path()
            ),
            "flame_media_directory": (
                self.flame_media_dir_widget.get_path()
            ),
            "flame_catalog_directory": (
                self.flame_catalog_dir_widget.get_path()
            ),
            "logik_projekt_config": (
                self.logik_projekt_config_widget.get_selected_config_data()
            )
        }

    def set_flame_options(self, options):
        """Set flame options from a dictionary.
      
        Args:
            options (dict): Dictionary containing flame option values
        """
        flame_software_choice = options.get("flame_software_choice", "")
        self.flame_software_choice_widget.set(flame_software_choice)
      
        flame_home_directory = options.get("flame_home_directory", "")
        self.flame_home_dir_widget.set_path(flame_home_directory)
      
        flame_setups_directory = options.get("flame_setups_directory", "")
        self.flame_setups_dir_widget.set_path(flame_setups_directory)
      
        flame_media_directory = options.get("flame_media_directory", "")
        self.flame_media_dir_widget.set_path(flame_media_directory)
      
        flame_catalog_directory = options.get("flame_catalog_directory", "")
        self.flame_catalog_dir_widget.set_path(flame_catalog_directory)
      
        logik_projekt_config_data = options.get("logik_projekt_config", {}) # Expect a dictionary
        if isinstance(logik_projekt_config_data, dict):
            config_name = logik_projekt_config_data.get("PROJEKT Configuration Name", "")
            self.logik_projekt_config_widget.set(config_name)
        else:
            # Fallback for old string-based config if necessary
            self.logik_projekt_config_widget.set(str(logik_projekt_config_data))

    def set_project_name(self, project_name: str):
        """Set the project name for the home directory widget.
      
        Args:
            project_name (str): Name of the project
        """
        self.flame_home_dir_widget.set_project_name(project_name)


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
