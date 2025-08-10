#!/usr/bin/env python3
# -------------------------------------------------------------------------- #
# Filename:     projekt_summary_widget.py
# Purpose:      Displays a summary of the project configuration.
# Description:  A widget that presents key project details in a read-only grid layout.

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
    QGridLayout
)
from PySide6.QtCore import Qt
from src.ui import ui_config


class ProjektSummaryWidget(QWidget):
    def __init__(self, master=None):
        super().__init__(master)
      
        self.layout = QGridLayout(self)
        self.layout.setContentsMargins(
            *ui_config.PANEL_PADDING
        )
        self.layout.setSpacing(
            ui_config.PANEL_LAYOUT_SPACING
        )
        self.layout.setHorizontalSpacing(4)
      
        # Labels column: take minimum space
        self.layout.setColumnStretch(0, 0)
        # Values column: take all remaining space
        self.layout.setColumnStretch(1, 1)
      
        # 15 lines @ 23px - Round up to Even Number
        self.setFixedHeight(300)

        self.fields = {}
        summary_fields = [
            ("Current User:", "current_user"),
            ("Current Group:", "current_group"),
            ("Current Workstation:", "current_workstation"),
            ("Current OS:", "current_os"),
            ("Flame Software Choice:", "flame_software_choice"),
            ("Flame Projekt Name:", "flame_projekt_name"),
            ("Flame Projekt Description:", "flame_projekt_description"),
            ("Flame Projekt Home Dir:", "flame_projekt_home"),
            ("Flame Projekt Setups Dir:", "flame_projekt_setups_dir"),
            ("Flame Projekt Media Dir:", "flame_projekt_media_dir"),
            ("Flame Projekt Catalog Dir:", "flame_projekt_catalog_dir"),
            ("LOGIK-PROJEKT Name:", "logik_projekt_name"),
            ("LOGIK-PROJEKT Path:", "logik_projekt_path"),
            # ("LOGIK-PROJEKT Config:", "logik_projekt_config_name"),
            # ("LOGIK-PROJEKT Cfg Tree:", "logik_projekt_config_tree"),
            # ("LOGIK-PROJEKT Cfg Bookmarks:", "logik_projekt_config_bookmarks"),
            # ("LOGIK-PROJEKT Cfg Workspace:", "logik_projekt_config_workspace"),
        ]

        for i, (label_text, key) in enumerate(summary_fields):
            label = QLabel(label_text)
            label.setAlignment(
                Qt.AlignLeft | Qt.AlignVCenter
            )
            self.layout.addWidget(label, i, 0)
          
            value_label = QLabel("")
            value_label.setAlignment(
                Qt.AlignLeft | Qt.AlignVCenter
            )
            self.layout.addWidget(value_label, i, 1)
          
            self.fields[key] = value_label

    def set_data(self, data):
        for key, label_widget in self.fields.items():
            label_widget.setText(
                str(data.get(key, ""))
            )

    def get_data(self):
        # This widget is primarily for display, but if needed,
        # can gather current displayed data
        data = {}
      
        for key, label_widget in self.fields.items():
            data[key] = label_widget.text()
      
        return data


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
