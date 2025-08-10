#!/usr/bin/env python3
# -------------------------------------------------------------------------- #
# Filename:     resolution_widget.py
# Purpose:      Provides a widget for resolution selection.
# Description:  A QComboBox widget for selecting the resolution.

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


class ResolutionWidget(QWidget):
    def __init__(self, master=None):
        super().__init__(master)
      
        self.resolutions = []
      
        self.layout = QHBoxLayout(self)
        self.layout.setContentsMargins(0, 0, 0, 0)
      
        self.label = QLabel("Resolution:")
        self.label.setAlignment(
            Qt.AlignRight | Qt.AlignVCenter
        )
        self.layout.addWidget(self.label)
      
        self.combobox = QComboBox()
        self.combobox.setFixedHeight(
            ui_config.COMBOBOX_HEIGHT
        )  # Set fixed height
        self.layout.addWidget(self.combobox)

    def set_values(self, values: list[dict]):
        self.resolutions = values
        self.combobox.clear()
      
        if self.resolutions:
            resolution_names = [
                res.get("resolution_name", "")
                for res in self.resolutions
            ]
            self.combobox.addItems(resolution_names)
            self.combobox.setCurrentIndex(0)

    def get(self):
        return self.combobox.currentText()

    def get_selected_resolution_data(self) -> dict | None:
        index = self.combobox.currentIndex()
      
        if 0 <= index < len(self.resolutions):
            return self.resolutions[index]
      
        return None

    def set(self, value):
        if not self.resolutions:
            return
      
        for i, res_data in enumerate(self.resolutions):
            if res_data.get("resolution_name") == value:
                self.combobox.setCurrentIndex(i)
                break


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
