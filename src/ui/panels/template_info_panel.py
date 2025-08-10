#!/usr/bin/env python3
# -------------------------------------------------------------------------- #
# Filename:     template_info_panel.py
# Purpose:      Panel for entering template information.
# Description:  This panel provides input fields for template details such as
#               serial number, client, campaign, and description, and calculates
#               a project name based on these inputs.

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
    QGridLayout
)
from PySide6.QtCore import Signal

from src.ui import ui_config
from src.ui.widgets.entry.serial_number_widget import (
    SerialNumberWidget
)
from src.ui.widgets.entry.client_name_widget import (
    ClientNameWidget
)
from src.ui.widgets.entry.campaign_name_widget import (
    CampaignNameWidget
)
from src.ui.widgets.entry.calculated_name_widget import (
    CalculatedNameWidget
)
from src.ui.widgets.entry.description_widget import (
    DescriptionWidget
)
from src.core.utils.calculated_name_utils import get_calculated_name


class TemplateInfoPanel(QWidget):
    """Panel for entering template information."""
    calculated_name_updated = Signal()
  
    def __init__(self, master=None):
        """Initialize the TemplateInfoPanel widget.
      
        Args:
            master: Parent widget
        """
        super().__init__(master)
        self._setup_layout()
        self._create_widgets()
        self._connect_signals()

    def _setup_layout(self):
        """Set up the main grid layout with proper spacing and margins."""
        self.layout = QGridLayout(self)
        self.layout.setSpacing(ui_config.PANEL_LAYOUT_SPACING)
        self.layout.setContentsMargins(*ui_config.PANEL_PADDING)
      
        # Label column
        self.layout.setColumnMinimumWidth(0, 160)
        # Widget column takes remaining space
        self.layout.setColumnStretch(1, 0)

    def _create_widgets(self):
        """Create all widgets and add them to the layout."""
        # Create widgets
        self.serial_number_widget = SerialNumberWidget(self)
        self.client_name_widget = ClientNameWidget(self)
        self.campaign_name_widget = CampaignNameWidget(self)
        self.calculated_name_widget = CalculatedNameWidget(self)
        self.description_widget = DescriptionWidget(self)

        # Add widgets to layout
        row = 0
        self.layout.addWidget(
            self.serial_number_widget.label,
            row,
            0
        )
        self.layout.addWidget(
            self.serial_number_widget.entry,
            row,
            1
        )
        row += 1
      
        self.layout.addWidget(
            self.client_name_widget.label,
            row,
            0
        )
        self.layout.addWidget(
            self.client_name_widget.entry,
            row,
            1
        )
        row += 1
      
        self.layout.addWidget(
            self.campaign_name_widget.label,
            row,
            0
        )
        self.layout.addWidget(
            self.campaign_name_widget.entry,
            row,
            1
        )
        row += 1
      
        self.layout.addWidget(
            self.calculated_name_widget.label,
            row,
            0
        )
        self.layout.addWidget(
            self.calculated_name_widget.entry,
            row,
            1
        )
        row += 1
      
        self.layout.addWidget(
            self.description_widget.label,
            row,
            0
        )
        self.layout.addWidget(
            self.description_widget.entry,
            row,
            1
        )

    def _connect_signals(self):
        """Connect widget signals to update calculated name."""
        # Bind events to update calculated name
        self.serial_number_widget.entry.textChanged.connect(
            self._update_calculated_name
        )
        self.client_name_widget.entry.textChanged.connect(
            self._update_calculated_name
        )
        self.campaign_name_widget.entry.textChanged.connect(
            self._update_calculated_name
        )
        self.description_widget.entry.textChanged.connect(
            self._update_calculated_name
        )

    def _update_calculated_name(self):
        """Update the calculated name based on serial, client, and campaign."""
        serial = self.serial_number_widget.get()
        client = self.client_name_widget.get()
        campaign = self.campaign_name_widget.get()
      
        calculated_name = get_calculated_name(serial, client, campaign)
        self.calculated_name_widget.set(calculated_name)
        self.calculated_name_updated.emit()

    def get_template_info(self):
        """Get template information as a dictionary.
      
        Returns:
            dict: Dictionary containing all template information
        """
        return {
            "template_serial_number": (
                self.serial_number_widget.get()
            ),
            "template_client_name": (
                self.client_name_widget.get()
            ),
            "template_campaign_name": (
                self.campaign_name_widget.get()
            ),
            "template_calculated_name": (
                self.calculated_name_widget.get()
            ),
            "template_description": (
                self.description_widget.get()
            )
        }

    def set_template_info(self, info):
        """Set template information from a dictionary.
      
        Args:
            info (dict): Dictionary containing template information
        """
        template_serial_number = info.get("template_serial_number", "")
        self.serial_number_widget.set(template_serial_number)
      
        template_client_name = info.get("template_client_name", "")
        self.client_name_widget.set(template_client_name)
      
        template_campaign_name = info.get("template_campaign_name", "")
        self.campaign_name_widget.set(template_campaign_name)
      
        template_calculated_name = info.get("template_calculated_name", "")
        self.calculated_name_widget.set(template_calculated_name)
      
        template_description = info.get("template_description", "")
        self.description_widget.set(template_description)


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
