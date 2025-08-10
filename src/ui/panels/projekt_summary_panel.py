#!/usr/bin/env python3
# -------------------------------------------------------------------------- #
# Filename:     projekt_summary_panel.py
# Purpose:      Panel for displaying project summary and creation controls.
# Description:  This panel presents a summary of the project configuration and
#               provides controls for initiating the project creation process.

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

import logging

import io
import contextlib

from src.ui import ui_config
from PySide6.QtWidgets import (
    QWidget,
    QGridLayout,
    QLabel,
    QTextEdit,
    QVBoxLayout,
    QMessageBox
)
from PySide6.QtCore import Qt

from src.ui.widgets.button.create_projekt_widget import (
    CreateProjektWidget
)
from src.ui.widgets.display.projekt_summary_widget import (
    ProjektSummaryWidget
)
from src.core.utils import validation_utils


class ProjektSummaryPanel(QWidget):
    """Panel for displaying project summary and creation controls."""
  
    def __init__(self, master=None):
        """Initialize the ProjektSummaryPanel widget.
      
        Args:
            master: Parent widget
        """
        super().__init__(master)
        self.projekt_data = {}
        self._setup_layout()
        self._create_widgets()

    def _setup_layout(self):
        """Set up the main grid layout with proper spacing and margins."""
        self.layout = QGridLayout(self)
        self.layout.setColumnMinimumWidth(0, 160)  # Label column
        self.layout.setColumnStretch(1, 1)  # Widget column takes remaining space
        self.layout.setSpacing(ui_config.PANEL_LAYOUT_SPACING)
        self.layout.setContentsMargins(*ui_config.PANEL_PADDING)

    def _create_widgets(self):
        """Create and add all widgets to the layout."""
        main_row_counter = 0

        # Add Projekt Summary to main layout
        projekt_summary_label = QLabel("Projekt Summary:")
        projekt_summary_label.setAlignment(
            Qt.AlignRight | Qt.AlignVCenter
        )
        self.layout.addWidget(
            projekt_summary_label,
            main_row_counter,
            0,
            Qt.AlignRight | Qt.AlignVCenter
        )

        # Use the refactored ProjektSummaryWidget
        self.projekt_summary_display_widget = ProjektSummaryWidget(self)
        self.layout.addWidget(
            self.projekt_summary_display_widget,
            main_row_counter,
            1
        )
        main_row_counter += 1

        # Create Projekt Button
        self.create_projekt_button = CreateProjektWidget(self)
        # Set object name for QSS
        self.create_projekt_button.button.setObjectName(
            "createProjektButton"
        )
        self.layout.addWidget(
            self.create_projekt_button,
            main_row_counter,
            0,
            1,
            2
        )
        # The connection is now made in the AppWindow
        main_row_counter += 1

        # Shell Output
        shell_output_label = QLabel("Shell Output:")
        shell_output_label.setAlignment(
            Qt.AlignRight | Qt.AlignVCenter
        )
        self.layout.addWidget(
            shell_output_label,
            main_row_counter,
            0,
            Qt.AlignRight | Qt.AlignVCenter
        )
      
        self.shell_output_text = QTextEdit()
        self.shell_output_text.setReadOnly(True)
        # Adjust height as needed
        self.shell_output_text.setMinimumHeight(28)
        self.layout.addWidget(
            self.shell_output_text,
            main_row_counter,
            1
        )
        main_row_counter += 1

    def set_projekt_summary_data(self, data):
        """Set project summary data.
      
        Args:
            data (dict): Project summary data dictionary
        """
        self.projekt_data = data
        self.projekt_summary_display_widget.set_data(data)

    def run_validation(self) -> bool:
        """Run validation checks and update the shell output.
      
        Returns:
            bool: True if validation passes, False otherwise
        """
        validation_header = (
            "\n" + "=" * 20 +
            " New PROJEKT Creation Attempt " +
            "=" * 20 + "\n"
        )
        self.shell_output_text.append(validation_header)

        projekt_name = self.projekt_data.get('logik_projekt_name', '')
        is_valid, message = validation_utils.validate_logik_projekt_name(
            projekt_name
        )

        if not is_valid:
            self.shell_output_text.append(message)
            return False

        # If validation passes, log a success message and return True
        logging.info("Validation passed. Proceeding with project creation...")
      
        return True


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
