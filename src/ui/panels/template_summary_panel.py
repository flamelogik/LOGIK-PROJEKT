#!/usr/bin/env python3
# -------------------------------------------------------------------------- #
# Filename:     template_summary_panel.py
# Purpose:      Panel for displaying template summary and export controls.
# Description:  This panel presents a summary of the template configuration and
#               provides controls for initiating the template export process.

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
    QLabel,
    QVBoxLayout,
    QMessageBox
)
from PySide6.QtCore import Qt

from src.ui.widgets.display.template_summary_widget import (
    TemplateSummaryWidget
)
from src.ui.widgets.button.export_template_widget import (
    ExportTemplateWidget
)
from src.core.app_logic import AppLogic


class TemplateSummaryPanel(QWidget):
    """Panel for displaying template summary and export controls."""
  
    def __init__(self, master=None):
        """Initialize the TemplateSummaryPanel widget.
      
        Args:
            master: Parent widget
        """
        super().__init__(master)
        self.app_logic = AppLogic()
        # Set object name for QSS
        self.setObjectName("TemplateSummaryPanel")
        self._setup_layout()
        self._create_widgets()

    def _setup_layout(self):
        """Set up the main grid layout with proper spacing and margins."""
        self.layout = QGridLayout(self)
        # Label column
        self.layout.setColumnMinimumWidth(0, 160)
        # Widget column takes remaining space
        self.layout.setColumnStretch(1, 1)
        self.layout.setSpacing(ui_config.PANEL_LAYOUT_SPACING)
        self.layout.setContentsMargins(*ui_config.PANEL_PADDING)

    def _create_widgets(self):
        """Create and add all widgets to the layout."""
        # "Template Summary:" label
        template_summary_label = QLabel("Template Summary:")
        # Align to top
        template_summary_label.setAlignment(
            Qt.AlignRight | Qt.AlignTop
        )
        # Ensure consistent width
        template_summary_label.setFixedWidth(160)
        # Place at (0,0)
        self.layout.addWidget(
            template_summary_label,
            0,
            0,
            Qt.AlignRight | Qt.AlignVCenter
        )

        # Use the refactored TemplateSummaryWidget
        self.template_summary_display_widget = TemplateSummaryWidget(self)
        # Place container at (0,1)
        self.layout.addWidget(
            self.template_summary_display_widget,
            0,
            1
        )

        # Create and add export button
        self.export_button = ExportTemplateWidget(self)
        # Set object name for QSS
        self.export_button.button.setObjectName("exportButton")
        # Adjust row index to be after summary content
        self.layout.addWidget(
            self.export_button,
            1,
            0,
            1,
            2
        )

    def set_template_summary_panel_data(self, data):
        """Set template summary panel data.
      
        Args:
            data (dict): Template summary data dictionary
        """
        self.template_summary_display_widget.set_template_summary_widget_data(
            data
        )


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
