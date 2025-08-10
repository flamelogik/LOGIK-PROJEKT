#!/usr/bin/env python3
# -------------------------------------------------------------------------- #
# Filename:     projekt_config_widget.py
# Purpose:      Provides a widget for project config selection.
# Description:  A QComboBox widget for selecting the project configuration.

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

from PySide6.QtWidgets import (
    QWidget,
    QLabel,
    QComboBox,
    QHBoxLayout
)
from PySide6.QtCore import Qt
from src.ui import ui_config


class ProjektConfigWidget(QWidget):
    def __init__(self, master=None):
        super().__init__(master)
      
        self.all_configs = []  # To store the full list of config dictionaries
        self.layout = QHBoxLayout(self)
        self.layout.setContentsMargins(0, 0, 0, 0)
      
        self.label = QLabel("Projekt Config:")
        self.label.setAlignment(
            Qt.AlignRight | Qt.AlignVCenter
        )
        self.layout.addWidget(self.label)
      
        self.combobox = QComboBox()
        self.combobox.setFixedHeight(
            ui_config.COMBOBOX_HEIGHT
        )  # Set fixed height
        self.layout.addWidget(self.combobox)

    def set_values(self, configs: list[dict]):
        self.all_configs = configs
        self.combobox.clear()
      
        for config in configs:
            name = config.get("PROJEKT Configuration Name", "")
            if name:
                self.combobox.addItem(name)
      
        if configs:
            pass

    def get(self) -> str:
        """Returns the name of the currently selected configuration."""
        return self.combobox.currentText()

    def get_selected_config_data(self) -> dict:
        """Returns the full dictionary of the currently selected configuration."""
        selected_name = self.get()
        for config in self.all_configs:
            if config.get("PROJEKT Configuration Name") == selected_name:
                return config
        return {} # Return empty dict if not found

    def set(self, value: str):
        """Sets the selected configuration by name."""
        index = self.combobox.findText(value)
        if index != -1:
            self.combobox.setCurrentIndex(index)
        else:
            print(f"Warning: Could not find config '{value}' in combobox.")


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
