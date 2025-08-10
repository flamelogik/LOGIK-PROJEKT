#!/usr/bin/env python3
# -------------------------------------------------------------------------- #
# Filename:     projekt_template_widget.py
# Purpose:      Displays a summary of the project template configuration.
# Description:  A widget that presents key project template details in a read-only grid layout.

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


class ProjektTemplateWidget(QWidget):
    def __init__(self, master=None):
        super().__init__(master)
      
        self.layout = QGridLayout(self)
        self.layout.setContentsMargins(
            *ui_config.PANEL_PADDING
        )
        self.layout.setSpacing(0)
        self.layout.setHorizontalSpacing(4)
      
        # Labels column: take minimum space
        self.layout.setColumnStretch(0, 0)
        # Values column: take all remaining space
        self.layout.setColumnStretch(1, 1)
      
        # 13 lines @ 23px - Round up to Even Number
        self.setFixedHeight(300)

        self.fields = {}
        template_fields = [
            # ("Projekt Serial #:", "projekt_serial_number"),
            # ("Projekt Client:", "projekt_client_name"),
            # ("Projekt Campaign:", "projekt_campaign_name"),
            ("Projekt Name:", "projekt_calculated_name"),
            ("Projekt Description:", "projekt_description"),
            # ("Projekt Resolution:", "projekt_resolution"),
            ("Projekt Width:", "projekt_resolution_w"),
            ("Projekt Height:", "projekt_resolution_h"),
            ("Projekt Aspect Ratio:", "projekt_aspect_ratio"),
            ("Projekt Bit Depth:", "projekt_bit_depth"),
            ("Projekt Framerate:", "projekt_framerate"),
            ("Projekt Scan Mode:", "projekt_scan_mode"),
            ("Projekt Start Frame:", "projekt_start_frame"),
            ("Projekt Init Config:", "projekt_init_config"),
            ("Projekt OCIO Name:", "projekt_ocio_name"),
            # ("Projekt Cache Integer:", "projekt_cache_integer"),
            ("Projekt Cache Integer ID:", "projekt_cache_integer_id"),
            # ("Projekt Cache Float:", "projekt_cache_float"),
            ("Projekt Cache Float ID:", "projekt_cache_float_id"),
        ]

        for i, (label_text, key) in enumerate(template_fields):
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
