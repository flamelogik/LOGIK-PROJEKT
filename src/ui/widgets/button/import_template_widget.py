#!/usr/bin/env python3
# -------------------------------------------------------------------------- #
# Filename:     import_template_widget.py
# Purpose:      Provides a button widget to import a template.
# Description:  A QPushButton widget that triggers the template import process.

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
    QPushButton,
    QHBoxLayout,
    QLabel
)
from PySide6.QtCore import Qt
from src.ui import ui_config


class ImportTemplateWidget(QWidget):
    def __init__(self, master=None, command=None):
        super().__init__(master)
      
        self.layout = QHBoxLayout(self)
        self.layout.setContentsMargins(0, 0, 0, 0)
      
        # self.label = QLabel("Import Template:")
        self.label = QLabel("")
        self.label.setAlignment(
            Qt.AlignRight | Qt.AlignVCenter
        )
        self.label.setFixedWidth(160)
        self.layout.addWidget(self.label)
      
        self.button = QPushButton(
            "Import LOGIK-PROJEKT Template"
        )
        self.button.setObjectName("importTemplateButton")
        self.button.setFixedHeight(
            ui_config.BUTTON_HEIGHT
        )  # Set fixed height
      
        if command:
            self.button.clicked.connect(command)
      
        self.layout.addWidget(self.button)


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
