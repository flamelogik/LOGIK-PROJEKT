#!/usr/bin/env python3
# -------------------------------------------------------------------------- #
# Filename:     flame_home_dir_widget.py
# Purpose:      Provides a button widget to select the Flame home directory.
# Description:  A QPushButton widget that opens a directory dialog.

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
    QPushButton,
    QHBoxLayout
)
from PySide6.QtCore import Qt


class FlameHomeDirWidget(QWidget):
    def __init__(self, master=None, command=None):
        super().__init__(master)
      
        self.layout = QHBoxLayout(self)
        self.layout.setContentsMargins(0, 0, 0, 0)
      
        self.label = QLabel("Flame Home Dir:")
        self.label.setAlignment(
            Qt.AlignRight | Qt.AlignVCenter
        )
        self.layout.addWidget(self.label)
      
        self.button = QPushButton("Select Directory")
        self.button.setObjectName("flameHomeDirButton")
      
        if command:
            self.button.clicked.connect(command)
      
        self.layout.addWidget(self.button)
      
        self._base_path = ""
        self._project_name = ""

    def set_project_name(self, name: str):
        self._project_name = name
        self._update_displayed_path()

    def set_path(self, path: str):
        self._base_path = path
        self._update_displayed_path()

    def get_path(self) -> str:
        # This method returns the actual path that would be used for project creation
        if "<project name>" in self._base_path:
            if self._project_name:
                return self._base_path.replace(
                    "<project name>",
                    self._project_name
                )
            # Return with placeholder if project name is empty
            return self._base_path
        elif self._project_name:
            return f"{self._base_path}/{self._project_name}"
      
        return self._base_path

    def _update_displayed_path(self):
        # This method updates the text displayed on the button
        displayed_text = self._base_path
      
        if "<project name>" in self._base_path:
            if self._project_name:
                displayed_text = self._base_path.replace(
                    "<project name>",
                    self._project_name
                )
        elif self._project_name:
            displayed_text = f"{self._base_path}/{self._project_name}"
      
        self.button.setText(displayed_text)


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
