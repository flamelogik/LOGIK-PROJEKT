#!/usr/bin/env python3
# -------------------------------------------------------------------------- #
# Filename:     template_summary_widget.py
# Purpose:      Displays a summary of the template configuration.
# Description:  A widget that presents key template details in a read-only grid layout.

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


class TemplateSummaryWidget(QWidget):
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
      
        # 17 lines @ 23px - Round up to Even Number
        self.setFixedHeight(392)

        self.fields = {}
        summary_fields = [
            ("Template Serial #:", "template_serial_number"),
            ("Template Client:", "template_client_name"),
            ("Template Campaign:", "template_campaign_name"),
            ("Template Name:", "template_calculated_name"),
            ("Template Description:", "template_description"),
            ("Template Resolution:", "template_resolution"),
            ("Template Width:", "template_resolution_w"),
            ("Template Height:", "template_resolution_h"),
            ("Template Aspect Ratio:", "template_aspect_ratio"),
            ("Template Bit Depth:", "template_bit_depth"),
            ("Template Framerate:", "template_framerate"),
            ("Template Scan Mode:", "template_scan_mode"),
            ("Template Start Frame:", "template_start_frame"),
            ("Template Init Config:", "template_init_config"),
            # ("Template OCIO Config:", "template_ocio_config"),  # Hidden in UI
            # ("Template OCIO Path:", "template_ocio_path"),  # Hidden in UI
            ("Template OCIO Name:", "template_ocio_name"),
            # ("Template Cache Integer ID:", "template_cache_integer_id"),  # Hidden in UI
            ("Template Cache Integer:", "template_cache_integer"),
            # ("Template Cache Float ID:", "template_cache_float_id"),  # Hidden in UI
            ("Template Cache Float:", "template_cache_float"),
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

    def set_template_summary_widget_data(self, data):
        for key, label_widget in self.fields.items():
            label_widget.setText(
                str(data.get(key, ""))
            )

    def get_template_summary_widget_data(self):
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
