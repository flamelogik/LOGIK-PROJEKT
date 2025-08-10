#!/usr/bin/env python3
# -------------------------------------------------------------------------- #
# Filename:     projekt_template_panel.py
# Purpose:      Panel for managing project templates.
# Description:  This panel provides functionality to import project templates
#               and displays a summary of the selected template.

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
    QVBoxLayout
)
from PySide6.QtCore import Qt

from src.ui.widgets.button.import_template_widget import (
    ImportTemplateWidget
)
from src.ui.widgets.display.projekt_template_widget import (
    ProjektTemplateWidget
)


class ProjektTemplatePanel(QWidget):
    """Panel for managing project templates."""
  
    def __init__(self, master=None):
        """Initialize the ProjektTemplatePanel widget.
      
        Args:
            master: Parent widget
        """
        super().__init__(master)
        self._setup_layout()
        self._create_widgets()

    def _setup_layout(self):
        """Set up the main grid layout with proper spacing and margins."""
        self.layout = QGridLayout(self)
        self.layout.setColumnMinimumWidth(0, 160)
        self.layout.setColumnStretch(1, 0)
        self.layout.setSpacing(ui_config.PANEL_LAYOUT_SPACING)
        self.layout.setContentsMargins(*ui_config.PANEL_PADDING)

    def _create_widgets(self):
        """Create and add all widgets to the layout."""
        # Add the import button
        self.import_button = ImportTemplateWidget(self)
        self.layout.addWidget(
            self.import_button.label,
            0,
            0
        )
        self.layout.addWidget(
            self.import_button,
            0,
            1
        )

        # Add a label for the template section
        template_section_label = QLabel("Projekt Template:")
        template_section_label.setAlignment(
            Qt.AlignRight | Qt.AlignVCenter
        )
        template_section_label.setFixedWidth(160)
        self.layout.addWidget(
            template_section_label,
            1,
            0
        )

        # Use the refactored ProjektTemplateWidget
        self.projekt_template_display_widget = ProjektTemplateWidget(self)
        self.layout.addWidget(
            self.projekt_template_display_widget,
            1,
            1
        )

    def set_projekt_template_data(self, data):
        """Set project template data.
      
        Args:
            data (dict): Project template data dictionary
        """
        self.projekt_template_display_widget.set_data(data)


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
