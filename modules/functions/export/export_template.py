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

# File Name:        layout_main.py
# Version:          1.9.9
# Created:          2024-01-19
# Modified:         2024-12-25

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

from PySide6.QtWidgets import QMessageBox, QLineEdit, QComboBox

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

def export_template_as_json(self):
    # Collect the names and values of all widgets
    template_summary_data = {}
    for widget_instance, label_instance in self.widgets_and_labels:
        widget_name = widget_instance.get_widget_parameters().get("widget_label_name")
        if isinstance(widget_instance, QLineEdit):
            widget_value = widget_instance.text()
        elif isinstance(widget_instance, QComboBox):
            widget_value = widget_instance.currentText()
        else:
            continue  # Skip unknown widget types

        template_summary_data[widget_name] = widget_value

    try:
        # Check if critical fields are empty
        required_fields = ["template_client_name", "template_campaign_name", "template_name"]
        for field in required_fields:
            widget = self.widget_dict.get(field)
            if not widget or not widget.text().strip():
                raise ValueError(f"{field.replace('_', ' ').title()} must not be empty.")

        # Check if the numeric value of template_frame_rate is part of template_init_config
        frame_rate_widget = self.widget_dict.get("template_frame_rate")
        init_config_widget = self.widget_dict.get("template_init_config")

        if not frame_rate_widget or not init_config_widget:
            raise ValueError("Frame Rate or Init Config widget not found.")

        frame_rate = frame_rate_widget.currentText().strip()
        init_config = init_config_widget.currentText().strip()

        # Check for specific exceptions in init config
        permitted_configs = ["film.cfg", "film_ntsc.cfg", "ntsc.cfg", "pal.cfg"]
        if init_config not in permitted_configs:
            # Extract the numeric part of the frame rate and remove any period
            numeric_frame_rate = frame_rate.split()[0].replace('.', '')

            if numeric_frame_rate not in init_config:
                raise ValueError(f"Frame rate '{numeric_frame_rate}' does not match the init config '{init_config}'.")

        # Define relative and absolute paths for the current projekt temp directory
        current_projekt_tmp_rel_dir = os.path.join(os.path.dirname(__file__), '..', '..', '..', 'resources', 'tmp')
        # current_projekt_tmp_rel_dir = os.path.join(os.path.dirname(__file__), '..', '..', '..', 'resources', 'tmp')
        current_projekt_tmp_abs_dir = os.path.abspath(current_projekt_tmp_rel_dir)

        # Create the directory if it doesn't exist
        os.makedirs(current_projekt_tmp_abs_dir, exist_ok=True)
        
        # Define the path for the current projekt template file
        current_projekt_template_path = os.path.join(current_projekt_tmp_abs_dir, 'current_projekt_template.json')

        # Save the summary data as JSON
        with open(current_projekt_template_path, 'w', encoding='utf-8') as f:
            json.dump(template_summary_data, f, ensure_ascii=False, indent=4)

        QMessageBox.information(
            self,
            "Save Successful",
            f"PROJEKT Template successfully exported to:\n\n{current_projekt_template_path}.\n\n Now configure Flame Version & Framestore.\n\n Then Create PROJEKT"
        )
    except ValueError as ve:
        QMessageBox.critical(self, "Error", str(ve))
    except Exception as e:
        QMessageBox.critical(self, "Error", f"Error exporting template: {str(e)}")

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
# Version:          1.9.9
# modified:         2024-12-25 - 09:50:13
# comments:         Preparation for future features
# -------------------------------------------------------------------------- #
