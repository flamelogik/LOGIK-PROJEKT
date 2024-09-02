#

# -------------------------------------------------------------------------- #

# DISCLAIMER:       This file is part of LOGIK-PROJEKT.
#                   Copyright © 2024 man-made-mekanyzms
                
#                   LOGIK-PROJEKT creates directories, files, scripts & tools
#                   for use with Autodesk Flame and other software.

#                   LOGIK-PROJEKT is free software.

#                   You can redistribute it and/or modify it under the terms
#                   of the GNU General Public License as published by the
#                   Free Software Foundation, either version 3 of the License,
#                   or any later version.
 
#                   This program is distributed in the hope that it will be
#                   useful, but WITHOUT ANY WARRANTY; without even the
#                   implied warranty of MERCHANTABILITY or FITNESS FOR A
#                   PARTICULAR PURPOSE.

#                   See the GNU General Public License for more details.

#                   You should have received a copy of the GNU General
#                   Public License along with this program.

#                   If not, see <https://www.gnu.org/licenses/>.
                
#                   Contact: phil_man@mac.com

# -------------------------------------------------------------------------- #

# File Name:        layout_left.py
# Version:          0.9.9
# Created:          2024-01-19
# Modified:         2024-08-31

# ========================================================================== #
# This section defines the import statements and directory paths.
# ========================================================================== #

# Standard library imports
import argparse
import ast
import base64
import collections
import datetime
import getpass
import grp
import importlib
import io
import json
import os
import platform
import re
import shutil
import socket
import subprocess
import sys
import unittest
import xml

# -------------------------------------------------------------------------- #

def get_base_path():
    if getattr(sys, 'frozen', False):
        return sys._MEIPASS
    else:
        return os.path.abspath(
            os.path.join(
                os.path.dirname(__file__), '..', '..', '..'
            )
        )
    
# -------------------------------------------------------------------------- #

def get_resource_path(relative_path):
    base_path = get_base_path()
    return os.path.join(
        base_path,
        relative_path
    )

# -------------------------------------------------------------------------- #

# Set the path to the 'modules' directory
modules_dir = get_resource_path('modules')
# Set the path to the 'resources' directory
resources_dir = get_resource_path('resources')
# Append the modules path to the system path
if modules_dir not in sys.path:
    sys.path.append(modules_dir)

# ========================================================================== #
# This section defines third party imports.
# ========================================================================== #

from PySide6.QtWidgets import (
    QWidget,
    QVBoxLayout,
    QHBoxLayout,
    QLabel,
    QLineEdit,
    QTextEdit,
    QComboBox,
    QPushButton,
    QMessageBox,
    QFileDialog,
)

from PySide6.QtGui import Qt

from PySide6.QtCore import Signal

from modules.widgets.line_edit.serial_number import WidgetSerialNumber
from modules.widgets.line_edit.client_name import WidgetClientName
from modules.widgets.line_edit.campaign_name import WidgetCampaignName
from modules.widgets.line_edit.projekt_name import WidgetProjektName
from modules.widgets.combo_box.resolution import WidgetResolution
from modules.widgets.line_edit.width import WidgetWidth
from modules.widgets.line_edit.height import WidgetHeight
from modules.widgets.line_edit.storage_aspect_ratio import WidgetStorageAspectRatio
from modules.widgets.line_edit.display_aspect_ratio import WidgetDisplayAspectRatio
from modules.widgets.line_edit.pixel_aspect_ratio import WidgetPixelAspectRatio
from modules.widgets.line_edit.aspect_ratio import WidgetAspectRatio
from modules.widgets.combo_box.bit_depth import WidgetBitDepth
from modules.widgets.combo_box.frame_rate import WidgetFrameRate
from modules.widgets.combo_box.scan_mode import WidgetScanMode
from modules.widgets.combo_box.start_frame import WidgetStartFrame
from modules.widgets.combo_box.init_config import WidgetInitConfig
from modules.widgets.combo_box.color_science import WidgetColorScience
from modules.functions.string.string_utilities import string_clean
from modules.functions.export.export_template import export_template_as_json
from modules.widgets.style_sheet.projekt_style_sheet import (
    ProjektStyleSheet,
    ButtonColor1StyleSheet,
    ButtonColor2StyleSheet,
    ButtonColor3StyleSheet,
)

# ========================================================================== #
# This section defines environment specific variables.
# ========================================================================== #

# These paths should be passed from the main app.
the_hostname = "delta"
the_projekt_os = "Linux"
the_software_version = "flame_2025.1.pr199"
the_sanitized_version = "2025_1"
the_framestore = "stonefs"

'''
Print the variables for debugging
print(f"  Debug: the_hostname:              {the_hostname}")
print(f"  Debug: the_projekt_os:            {the_projekt_os}")
print(f"  Debug: the_software_version:      {the_software_version}")
print(f"  Debug: the_sanitized_version:     {the_sanitized_version}")
'''

# ========================================================================== #
# This section defines common paths.
# ========================================================================== #

projekt_roots_config_path = os.path.join(
    resources_dir,
    'cfg',
    'projekt_configuration',
    'roots',
    'projekt_roots.json'
)

# Read the JSON configuration file
try:
    with open(projekt_roots_config_path, 'r') as config_file:
        config = json.load(config_file)
except Exception as e:
    print(f"  Error reading JSON configuration file: {e}")
    config = {}

# Define common directory paths
the_projekts_dir = config.get(
    'the_projekts_dir',
    "/PROJEKTS"
)

the_projekt_flame_dirs = config.get(
    'the_projekt_flame_dirs',
    "/opt/Autodesk/project"
)

the_adsk_dir = config.get(
    'the_adsk_dir',
    "/opt/Autodesk"
)

the_adsk_dir_linux = config.get(
    'the_adsk_dir_linux',
    "/opt/Autodesk"
)

the_adsk_dir_macos = config.get(
    'the_adsk_dir_macos',
    "/Applications/Autodesk"
)

'''
Print the variables for debugging
print(f"  Debug: projekt_roots_config_path: {projekt_roots_config_path}")
print(f"  Debug: the_projekts_dir:          {the_projekts_dir}")
print(f"  Debug: the_projekt_flame_dirs:    {the_projekt_flame_dirs}")
print(f"  Debug: the_adsk_dir:              {the_adsk_dir}")
print(f"  Debug: the_adsk_dir_linux:        {the_adsk_dir_linux}")
print(f"  Debug: the_adsk_dir_macos:        {the_adsk_dir_macos}")
'''

# ========================================================================== #
# This section defines projekt specific paths.
# ========================================================================== #

# These paths should be passed from the main app.
the_projekt_name = "8888_new_job"
the_projekt_flame_name = f"{the_projekt_name}_{the_sanitized_version}_{the_hostname}"

separator = '# ' + '-' * 75 + ' #'

# ========================================================================== #
# This section defines the primary functions for the script.
# ========================================================================== #

class LayoutLeft(QWidget):
    widgets_updated = Signal()
    data_exported = Signal(dict)  # New signal for exporting data

    def __init__(self):
        super().__init__()

        # Initialize layout
        layout = QVBoxLayout()

        # Apply stylesheet
        self.setStyleSheet(ProjektStyleSheet)

        # Set the maximum width for labels and widgets
        label_max_width = 160
        widget_max_width = 480
        widget_min_height = 32

        # List of widget instances and their corresponding labels
        self.widgets_and_labels = [
            (WidgetSerialNumber(), QLabel()),
            (WidgetClientName(), QLabel()),
            (WidgetCampaignName(), QLabel()),
            (WidgetProjektName(), QLabel()),
            (WidgetResolution(), QLabel()),
            (WidgetWidth(), QLabel()),
            (WidgetHeight(), QLabel()),
            (WidgetStorageAspectRatio(), QLabel()),
            (WidgetDisplayAspectRatio(), QLabel()),
            (WidgetPixelAspectRatio(), QLabel()),
            (WidgetAspectRatio(), QLabel()),
            (WidgetBitDepth(), QLabel()),
            (WidgetFrameRate(), QLabel()),
            (WidgetScanMode(), QLabel()),
            (WidgetStartFrame(), QLabel()),
            (WidgetInitConfig(), QLabel()),
            (WidgetColorScience(), QLabel()),
        ]

        # Set minimum height for each widget and align labels and widgets horizontally
        self.widget_dict = {}
        for widget_instance, label_instance in self.widgets_and_labels:
            widget_instance.setMinimumHeight(widget_min_height)
            widget_instance.setMaximumWidth(widget_max_width)
            widget_name = widget_instance.get_widget_parameters()["widget_label_name"]
            label_instance.setText(widget_name)
            label_instance.setBuddy(widget_instance)
            label_instance.setMaximumWidth(label_max_width)
            label_instance.setAlignment(Qt.AlignRight | Qt.AlignVCenter)

            # Create a horizontal layout for each row
            row_layout = QHBoxLayout()
            row_layout.addWidget(label_instance)
            row_layout.addWidget(widget_instance)

            # Add the row layout to the main vertical layout
            layout.addLayout(row_layout)

            # Store widgets in widget_dict for easier access
            widget_key = widget_instance.get_widget_parameters()["widget_name"]
            self.widget_dict[widget_key] = widget_instance

            # Connect resolution_changed signal to update_widgets slot
            if isinstance(widget_instance, WidgetResolution):
                widget_instance.resolution_changed.connect(self.update_widgets)

            # Connect signals for dynamic updates
            if isinstance(widget_instance, QLineEdit):
                widget_instance.textChanged.connect(self.on_text_changed)
            elif isinstance(widget_instance, QComboBox):
                widget_instance.currentIndexChanged.connect(self.on_text_changed)

        # Add the summary QTextEdit widget in a row layout
        self.template_summary = QTextEdit()
        self.template_summary.setReadOnly(True)
        self.template_summary.setMaximumWidth(widget_max_width)
        self.template_summary.setMinimumHeight(352)
        summary_label = QLabel("Template Summary:")
        summary_label.setBuddy(self.template_summary)
        summary_label.setMaximumWidth(label_max_width)
        summary_label.setAlignment(Qt.AlignRight | Qt.AlignVCenter)

        summary_layout = QHBoxLayout()
        summary_layout.addWidget(summary_label)
        summary_layout.addWidget(self.template_summary)
        layout.addLayout(summary_layout)

        # Connect widgets_updated signal to the update_summary slot
        self.widgets_updated.connect(self.update_summary)

        # Add Save button in a row layout
        self.export_template_button = QPushButton("Export PROJEKT Template")
        self.export_template_button.setStyleSheet(ButtonColor1StyleSheet)
        self.export_template_button.setMinimumHeight(widget_min_height)
        self.export_template_button.setMaximumWidth(widget_max_width)
        export_template_button_label = QLabel()
        export_template_button_label.setMaximumWidth(label_max_width)

        export_template_button_layout = QHBoxLayout()
        export_template_button_layout.addWidget(export_template_button_label)
        export_template_button_layout.addWidget(self.export_template_button)
        layout.addLayout(export_template_button_layout)
        # self.export_template_button.clicked.connect(lambda: export_template_as_json(self))

        self.export_template_button.clicked.connect(self.export_and_transmit_template)

        self.setLayout(layout)

        # Initialize the summary with existing widget data
        self.update_summary()

        # Connect textChanged signals to update_template_name method
        self.widget_dict["template_serial_number"].textChanged.connect(self.update_template_name)
        self.widget_dict["template_client_name"].textChanged.connect(self.update_template_name)
        self.widget_dict["template_campaign_name"].textChanged.connect(self.update_template_name)

    def update_widgets(self, resolution_detail):
        print(f"Received resolution detail: {resolution_detail}")

        # Update other widgets based on resolution detail
        for widget_instance, label_instance in self.widgets_and_labels:
            try:
                widget_name = widget_instance.get_widget_parameters()["widget_name"]
                print(f"Widget instance: {widget_instance} with name: {widget_name}")
            except KeyError:
                print(f"Widget instance {widget_instance} does not have 'widget_name' parameter.")
                continue

            # Construct template_name without redundant prefix
            template_name = widget_name
            if template_name.startswith("template_"):
                template_name = template_name[len("template_"):]

            if template_name in resolution_detail:
                value = resolution_detail[template_name]
                value_type = type(value).__name__
                print(f"Updating {template_name} widget with value: {value}")

                # Ensure the value is converted to string
                value = str(value)

                widget_instance.setText(value)
            else:
                print(f"No matching value found for {template_name}")

        # Emit the widgets_updated signal after updating all widgets
        self.widgets_updated.emit()

    def on_text_changed(self):
        # Emit the widgets_updated signal whenever a widget's text or selection changes
        self.widgets_updated.emit()

    def update_summary(self):
        # Collect the names and values of all widgets
        summary = []
        for widget_instance, label_instance in self.widgets_and_labels:
            widget_name = widget_instance.get_widget_parameters()["widget_label_name"]
            if isinstance(widget_instance, QLineEdit):
                widget_value = widget_instance.text()
            elif isinstance(widget_instance, QComboBox):
                widget_value = widget_instance.currentText()
            # summary.append(f"{widget_name}: {widget_value}")
            summary.append(f"{widget_name}{widget_value}")

        # Update the template_summary QTextEdit widget with the summary
        self.template_summary.setText("\n".join(summary))

    def update_template_name(self):
        try:
            serial_number = string_clean(self.widget_dict["template_serial_number"].text())
            client_name = string_clean(self.widget_dict["template_client_name"].text())
            campaign_name = string_clean(self.widget_dict["template_campaign_name"].text())

            if serial_number:
                template_name = f"{serial_number}_{client_name}_{campaign_name}".strip('_')
            else:
                template_name = f"{client_name}_{campaign_name}".strip('_')

            self.widget_dict["template_name"].setText(template_name)
            self.update_summary()
        except KeyError:
            pass

    def export_and_transmit_template(self):
        # Collect data from all widgets
        data = {}
        for widget_instance, label_instance in self.widgets_and_labels:
            widget_name = widget_instance.get_widget_parameters()["widget_name"]
            if isinstance(widget_instance, QLineEdit):
                data[widget_name] = widget_instance.text()
            elif isinstance(widget_instance, QComboBox):
                data[widget_name] = widget_instance.currentText()

        # Export template as JSON (existing functionality)
        export_template_as_json(self)

        # Emit the data_exported signal with the collected data
        self.data_exported.emit(data)

# ========================================================================== #
# C2 A9 32 30 32 34 2D 4D 41 4E 2D 4D 41 44 45 2D 4D 45 4B 41 4E 59 5A 4D 53 #
# ========================================================================== #

# Changelist:       

# -------------------------------------------------------------------------- #
# version:          0.0.1
# created:          2024-01-19 - 12:34:56
# comments:         scripts to create flame projekts, presets & templates.
# -------------------------------------------------------------------------- #
# version:          0.1.0
# modified:         2024-04-20 - 16:20:00
# comments:         refactored monolithic program into separate functions.
# -------------------------------------------------------------------------- #
# version:          0.5.0
# modified:         2024-05-24 - 20:24:00
# comments:         merged flame_colortoolkit with projekt.
# -------------------------------------------------------------------------- #
# version:          0.6.0
# modified:         2024-05-25 - 15:00:03
# comments:         started conversion to python3.
# -------------------------------------------------------------------------- #
# version:          0.7.0
# modified:         2024-06-21 - 18:21:03
# comments:         started gui design with pyside6.
# -------------------------------------------------------------------------- #
# version:          0.9.9
# modified:         2024-08-31 - 16:51:09
# comments:         prep for release - code appears to be functional
# -------------------------------------------------------------------------- #
