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

# File Name:        layout_right.py
# Version:          2.0.0
# Created:          2024-01-19
# Modified:         2024-12-31

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
    QApplication,
    QComboBox,
    QFileDialog,
    QHBoxLayout,
    QLabel,
    QLineEdit,
    QMessageBox,
    QPushButton,
    QTextEdit,
    QVBoxLayout,
    QWidget,
)

from PySide6.QtGui import Qt

# from PySide6.QtCore import Slot
from PySide6.QtCore import QProcess

from functions.get.get_environment import GetEnvironment

from functions.get.get_flame_software import (
    get_flame_family_apps_list,
    sanitize_app_name,
    sanitize_app_version,
)

from functions.get.get_framestores import get_framestore_list

from modules.functions.string.string_utilities import string_clean_camel
from modules.functions.string.string_utilities import string_clean_lower
from modules.functions.string.string_utilities import string_clean_uc
from modules.functions.string.string_utilities import string_clean_upper

from widgets.line_edit.flame_projekt_directory import WidgetFlameProjektDirectory
from widgets.line_edit.flame_projekt_media_cache import WidgetFlameProjektMediaCache
from widgets.line_edit.flame_projekt_setups_dir import WidgetFlameProjektSetupsDir

from widgets.style_sheet.projekt_style_sheet import (
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

class WidgetLayoutRight(QWidget):
    def __init__(self):
        super().__init__()

        # Initialize layout
        self.layout = QVBoxLayout()
        self.setLayout(self.layout)

        # Apply stylesheet
        self.setStyleSheet(ProjektStyleSheet)

        # Set the maximum width for labels and widgets
        self.label_fixed_width = 160
        self.widget_fixed_width = 792
        self.widget_min_height = 32

        # Add widgets
        self.add_import_template_button()
        self.projekt_summary = self.add_text_edit("Projekt Summary:", True, fixed_height=300)
        self.initialize_projekt_summary()
        self.combo_box_software_version = self.add_combobox("Software Version:")
        self.combo_box_framestore = self.add_combobox("Framestore:")
        self.add_labeled_widget("Projekt Flame Directory:", WidgetFlameProjektDirectory())
        self.add_labeled_widget("Setups Directory:", WidgetFlameProjektSetupsDir())
        self.add_labeled_widget("Media Cache:", WidgetFlameProjektMediaCache())
        self.environment_summary = self.add_text_edit("Environment Summary:", True, fixed_height=220)
        # self.create_projekt_button = self.add_button("Create Projekt")
        self.add_create_projekt_button()
        self.command_monitor = self.add_text_edit("Command Monitor:", True, fixed_height=240)

        # Load data into widgets
        self.load_software_versions()
        self.load_framestores()
        self.load_command_monitor()

        # Connect signals
        self.combo_box_software_version.currentIndexChanged.connect(self.update_environment_summary)
        self.combo_box_framestore.currentIndexChanged.connect(self.update_environment_summary)
        self.projekt_summary.textChanged.connect(self.update_environment_summary)

        # Connect the import template button to the new method
        self.import_template_button.clicked.connect(self.import_template)

        # Add this line to connect the button
        self.create_projekt_button.clicked.connect(self.create_projekt)

        # Initial call to update environment summary
        self.update_environment_summary()

        # Initialize logging code ...
        self.process = QProcess()
        self.process.readyReadStandardOutput.connect(self.handle_stdout)
        self.process.readyReadStandardError.connect(self.handle_stderr)

    def add_import_template_button(self):
        self.import_template_button = self.add_button("Import PROJEKT Template")
        self.import_template_button.setStyleSheet(ButtonColor2StyleSheet)

    def add_create_projekt_button(self):
        self.create_projekt_button = self.add_button("Create PROJEKT")
        self.create_projekt_button.setStyleSheet(ButtonColor3StyleSheet)

    def add_text_edit(self, label_text, read_only=False, fixed_height=32):
        text_edit = QTextEdit()
        text_edit.setReadOnly(read_only)
        text_edit.setFixedHeight(fixed_height)
        self.add_labeled_widget(label_text, text_edit)
        return text_edit

    def add_combobox(self, label_text):
        combobox = QComboBox()
        self.add_labeled_widget(label_text, combobox)
        return combobox

    def add_line_edit(self, label_text):
        line_edit = QLineEdit()
        self.add_labeled_widget(label_text, line_edit)
        return line_edit

    def add_button(self, button_text):
        button = QPushButton(button_text)
        button.setMinimumHeight(self.widget_min_height)
        self.add_labeled_widget(button_text, button)
        return button

    def add_labeled_widget(self, label_text, widget):
        widget.setFixedWidth(self.widget_fixed_width)
        widget.setMinimumHeight(self.widget_min_height)
        label = QLabel(label_text)
        label.setBuddy(widget)
        label.setFixedWidth(self.label_fixed_width)
        label.setAlignment(Qt.AlignRight | Qt.AlignVCenter)

        row_layout = QHBoxLayout()
        row_layout.addWidget(label)
        row_layout.addWidget(widget)
        self.layout.addLayout(row_layout)

    def initialize_projekt_summary(self):
        keys = [
            "Serial Number:",
            "Client Name:",
            "Campaign Name:",
            "Projekt Name:",
            "Resolution:",
            "Width:",
            "Height:",
            # "Storage Aspect Ratio:",
            # "Display Aspect Ratio:",
            # "Pixel Aspect Ratio:",
            "Aspect Ratio:",
            "Bit Depth:",
            "Framerate:",
            "Scan Mode:",
            "Start Frame:",
            "Init Config:",
            "Color Science:",
            "OCIO Config:"
        ]
        self.projekt_summary.setPlainText("\n".join(keys))

    def update_projekt_summary_from_emitted(self, data):
        # This is your existing update_projekt_summary method
        field_mapping = {
            "template_serial_number": "Serial Number:",
            "template_client_name": "Client Name:",
            "template_campaign_name": "Campaign Name:",
            "template_name": "Projekt Name:",
            "template_resolution": "Resolution:",
            "template_width": "Width:",
            "template_height": "Height:",
            "template_storage_aspect_ratio": "Storage Aspect Ratio:",
            "template_display_aspect_ratio": "Display Aspect Ratio:",
            "template_pixel_aspect_ratio": "Pixel Aspect Ratio:",
            "template_aspect_ratio": "Aspect Ratio:",
            "template_bit_depth": "Bit Depth:",
            "template_frame_rate": "Framerate:",
            "template_scan_mode": "Scan Mode:",
            "template_start_frame": "Start Frame:",
            "template_init_config": "Init Config:",
            "template_color_science": "Color Science:",
            "template_ocio_config": "OCIO Config:"
        }

        current_text = self.projekt_summary.toPlainText()
        lines = current_text.split('\n')

        for template_field, projekt_field in field_mapping.items():
            if template_field in data:
                new_value = data[template_field]
                for i, line in enumerate(lines):
                    if line.startswith(projekt_field):
                        lines[i] = f"{projekt_field} {new_value}"
                        break

        updated_text = '\n'.join(lines)
        self.projekt_summary.setPlainText(updated_text)
        self.update_environment_summary()

    def update_projekt_summary_from_imported(self, data):
        current_text = self.projekt_summary.toPlainText()
        lines = current_text.split('\n')

        for i, line in enumerate(lines):
            key = line.split(':', 1)[0] + ': '  # Add the colon and space to match JSON keys
            if key in data:
                lines[i] = f"{key}{data[key]}"

        updated_text = '\n'.join(lines)
        self.projekt_summary.setPlainText(updated_text)
        self.update_environment_summary()

    # def import_template(self):
    #     file_dialog = QFileDialog()
    #     file_dialog.setStyleSheet("")  # Reset stylesheet to default
    #     file_path, _ = file_dialog.getOpenFileName(self, "Import PROJEKT Template", "", "JSON Files (*.json)")

    #     if file_path:
    #         try:
    #             with open(file_path, 'r') as file:
    #                 data = json.load(file)
    #                 self.update_projekt_summary_from_imported(data)
    #         except Exception as e:
    #             QMessageBox.critical(self, "Import Error", f"An error occurred while importing the template:\n{e}")

    def import_template(self):
        file_dialog = QFileDialog()
        file_dialog.setStyleSheet("")  # Reset stylesheet to default
        file_path, _ = file_dialog.getOpenFileName(self, "Import PROJEKT Template", "", "JSON Files (*.json)")

        if file_path:
            try:
                # Define the destination path and backup path
                destination_path = 'resources/tmp/current_projekt_template.json'
                backup_path = 'resources/tmp/current_projekt_template.json.bak'

                # Backup the existing file if it exists
                if os.path.exists(destination_path):
                    shutil.copy(destination_path, backup_path)

                # Copy the imported file to 'resources/tmp/current_projekt_template.json'
                shutil.copy(file_path, destination_path)

                # Read the JSON data from the imported file
                with open(destination_path, 'r') as file:
                    data = json.load(file)
                    self.update_projekt_summary_from_imported(data)
            except Exception as e:
                QMessageBox.critical(self, "Import Error", f"An error occurred while importing the template:\n{e}")
               
    def update_from_layout_left(self, data):
        self.update_projekt_summary(data)

    def display_summary(self, data):
        summary_text = json.dumps(data, indent=4)
        self.projekt_summary.setPlainText(summary_text)

    def load_software_versions(self):
        try:
            software_versions = get_flame_family_apps_list()
            self.combo_box_software_version.addItems(software_versions)
        except Exception as e:
            print(f"Error loading software versions: {e}")

    def load_framestores(self):
        try:
            framestores = get_framestore_list()
            if framestores:
                self.combo_box_framestore.addItems(framestores)
            else:
                print("No framestores found or error retrieving framestores.")
        except Exception as e:
            print(f"Error loading framestores: {e}")

# =========================================================================== #

    # def load_command_monitor(self):
    #     self.command_monitor.setPlainText("Command Monitor initialized.")

    def load_command_monitor(self):
        self.update_command_monitor("Process Monitor initialized.")
        self.update_command_monitor("")
        self.update_command_monitor("Creating a PROJEKT will take a heartbeat.")
        self.update_command_monitor("")
        self.update_command_monitor("PROJEKT will process your parameters.")
        self.update_command_monitor("")
        self.update_command_monitor("PROJEKT will try to launch FLAME.")
        self.update_command_monitor("")
        self.update_command_monitor("Please be patient...")
        self.update_command_monitor("")

# =========================================================================== #

    def load_environment_summary(self):
        try:
            software_version = self.combo_box_software_version.currentText()
            sanitized_sw_ver = sanitize_app_name(software_version)
            sanitized_version = sanitize_app_version(software_version)

            # Get the the_projekt_name from the Projekt Summary
            the_projekt_serial_number = self.get_projekt_summary_value("Projekt Serial:")
            the_projekt_client_name = self.get_projekt_summary_value("Projekt Client:")
            the_projekt_campaign_name = self.get_projekt_summary_value("Projekt Campaign:")
            the_projekt_name = self.get_projekt_summary_value("Projekt Name:")
            the_projekt_width = self.get_projekt_summary_value("Width:")
            the_projekt_height = self.get_projekt_summary_value("Height:")
            the_projekt_aspect_ratio = self.get_projekt_summary_value("Aspect Ratio:")
            the_projekt_bit_depth = self.get_projekt_summary_value("Bit Depth:")
            the_projekt_frame_rate = self.get_projekt_summary_value("Framerate:")
            the_projekt_scan_mode = self.get_projekt_summary_value("Scan Mode:")
            the_projekt_start_frame = self.get_projekt_summary_value("Start Frame:")
            the_projekt_init_config = self.get_projekt_summary_value("Init Config:")
            the_projekt_color_science = self.get_projekt_summary_value("Color Science:")

            # Get the_hostname
            the_hostname = GetEnvironment.projekt_hostname() or 'N/A'
            # the_hostname = GetEnvironment.projekt_workstation_name() or 'N/A'

            # =========================================================================== #

            # Retrieve values from relevant widgets
            projekt_flame_directory = self.get_widget_value("Projekt Flame Directory:")
            setups_directory = self.get_widget_value("Setups Directory:")
            media_cache_directory = self.get_widget_value("Media Cache:")

            software_version = self.combo_box_software_version.currentText()
            sanitized_sw_ver = sanitize_app_name(software_version)
            sanitized_version = sanitize_app_version(software_version)

            # Calculate projekt_flame_name
            if the_projekt_name and sanitized_version and the_hostname != 'N/A':
                the_projekt_flame_name = f"{the_projekt_name}_{sanitized_version}_{the_hostname}"
            else:
                the_projekt_flame_name = "N/A"
                the_projekt_name = "N/A"

            # Calculate xml_project_dir, xml_setup_dir, and xml_media_dir
            xml_project_dir = projekt_flame_directory.replace("<project_name>",  the_projekt_flame_name) or f"/opt/Autodesk/project/{the_projekt_flame_name}"
            xml_setup_dir = setups_directory.replace("<project_home>",  xml_project_dir) or f"{xml_project_dir}/setups"
            xml_media_dir = media_cache_directory.replace("<project_nickname>", the_projekt_name).replace("<project_name>", the_projekt_flame_name) or f"{xml_project_dir}/media"

            # =========================================================================== #

            # Update the environment summary dictionary
            env_data = {
                'Username': GetEnvironment.projekt_user_name() or 'N/A',
                'Group': GetEnvironment.projekt_primary_group() or 'N/A',
                'Operating System': GetEnvironment.projekt_os() or 'N/A',
                'Hostname': the_hostname,
                # 'Workstation Name': GetEnvironment.projekt_workstation_name() or 'N/A',
                # 'FQDN': GetEnvironment.projekt_computername() or 'N/A',
                # 'Network Address': GetEnvironment.projekt_localhostname() or 'N/A',
                'Framestore': self.combo_box_framestore.currentText() or 'N/A',
                'Software Version': software_version or 'N/A',
                # 'Sanitized App Ver': sanitized_sw_ver or 'N/A',
                # 'Sanitized Version#': sanitized_version or 'N/A',
                'Projekt Flame Name': the_projekt_flame_name,
                'Projekt Flame Directory': xml_project_dir,
                'Setups Directory': xml_setup_dir,
                'Media Cache': xml_media_dir,
            }

            # Update environment summary text
            summary_text = '\n'.join(f"{key}: {value}" for key, value in env_data.items())
            self.environment_summary.setPlainText(summary_text)
        except Exception as e:
            print(f"Error loading environment data: {e}")
            QMessageBox.critical(self, "Error", f"An error occurred while loading environment data:\n{e}")

    def get_widget_value(self, label_text):
          """Retrieve the value of a widget based on its label text."""
          for i in range(self.layout.count()):
              item = self.layout.itemAt(i)
              if isinstance(item, QHBoxLayout):
                    label = item.itemAt(0).widget()
                    widget = item.itemAt(1).widget()
                    if isinstance(label, QLabel) and label.text() == label_text:
                        return widget.text() if hasattr(widget, "text") else ""
          return ""

            # =========================================================================== #

        #     # Update environment summary text
        #     summary_text = '\n'.join(f"{key}: {value}" for key, value in env_data.items())
        #     self.environment_summary.setPlainText(summary_text)
        # except Exception as e:
        #     print(f"Error loading environment data: {e}")
        #     QMessageBox.critical(self, "Error", f"An error occurred while loading environment data:\n{e}")

    def get_projekt_summary_value(self, key):
        text = self.projekt_summary.toPlainText()
        for line in text.split('\n'):
            if line.startswith(key):
                return line.split(':', 1)[1].strip()
        return ''

    def update_environment_summary(self):
        self.load_environment_summary()

# =========================================================================== #

    # Add check for Projekt Client before creating the Projekt
    # Add check for Projekt Campaign before creating the Projekt

    # def create_projekt(self):
    #     projekt_name = self.get_projekt_summary_value("Projekt Name:")
    #     if not projekt_name:
    #         QMessageBox.critical(self, "Error", "The PROJEKT information is missing.\n\nFill out the information & Export a PROJEKT Template\n\nOR\n\nImport a PROJEKT template\n\nThen choose the flame version & framestore.\n\nThen create a PROJEKT.")
    #         return

    #     self.update_command_monitor("  Starting PROJEKT creation...")

    #     # Gather information from variables
    #     projekt_info = self.gather_projekt_info()

    #     projekt_creation_script_path = 'modules/functions/create/create_projekt.py'

    #     try:
    #         python_executable = "/usr/bin/python3"  # Replace with the correct path
    #         os.environ["PATH"] += os.pathsep + os.path.dirname(python_executable)

    #         # Execute the script and capture output
    #         result = subprocess.run([python_executable, projekt_creation_script_path],
    #                                 input=json.dumps(projekt_info),
    #                                 text=True,
    #                                 capture_output=True,
    #                                 check=True)
           
    #         # Update Command Monitor with script output
    #         self.update_command_monitor(f"  Executed {projekt_creation_script_path}:\n{result.stdout}")
    #     except subprocess.CalledProcessError as e:
    #         # Handle errors
    #         self.update_command_monitor(f"  Error executing {projekt_creation_script_path}:\n{e.stderr}")

    #     self.update_command_monitor("  PROJEKT creation completed.")

    #     # =========================================================================== #

    #     self.update_command_monitor("  Starting FLAME Launcher...")

    #     # Gather information from variables
    #     projekt_info = self.gather_projekt_info()

    #     flame_launcher_script_path = 'modules/functions/run/run_flame_launcher_script.py'

    #     try:
    #         python_executable = "/usr/bin/python3"  # Replace with the correct path
    #         os.environ["PATH"] += os.pathsep + os.path.dirname(python_executable)

    #         # Execute the script and capture output
    #         result = subprocess.run([python_executable, flame_launcher_script_path],
    #                                 input=json.dumps(projekt_info),
    #                                 text=True,
    #                                 capture_output=True,
    #                                 check=True)
           
    #         # Update Command Monitor with script output
    #         self.update_command_monitor(f"  Executed {flame_launcher_script_path}:\n{result.stdout}")
    #     except subprocess.CalledProcessError as e:
    #         # Handle errors
    #         self.update_command_monitor(f"  Error executing {flame_launcher_script_path}:\n{e.stderr}")

    #     self.update_command_monitor("  FLAME Launcher completed.")

    def handle_stdout(self):
        data = self.process.readAllStandardOutput()
        stdout = bytes(data).decode("utf8")
        self.update_command_monitor(stdout)

    def handle_stderr(self):
        data = self.process.readAllStandardError()
        stderr = bytes(data).decode("utf8")
        self.update_command_monitor(stderr)

    # def update_command_monitor(self, message):
    #     self.command_monitor.append(message)
    #     self.command_monitor.verticalScrollBar().setValue(
    #         self.command_monitor.verticalScrollBar().maximum()
    #     )

    def create_projekt(self):
        projekt_name = self.get_projekt_summary_value("Projekt Name:")
        if not projekt_name:
            QMessageBox.critical(self, "Error", "The PROJEKT information is missing.\n\nFill out the information & Export a PROJEKT Template\n\nOR\n\nImport a PROJEKT template\n\nThen choose the flame version & framestore.\n\nThen create a PROJEKT.")
            return

        self.update_command_monitor("Starting PROJEKT creation...")
        
        # Gather information from variables
        projekt_info = self.gather_projekt_info()
        
        # Initialize QProcess if not already done
        if not hasattr(self, 'processes'):
            self.processes = []
        
        # Create processes for both scripts
        for script_path in ['modules/functions/create/create_projekt.py', 
                        'modules/functions/run/run_flame_launcher_script.py']:
            process = QProcess()
            process.setProcessChannelMode(QProcess.MergedChannels)
            
            # Connect signals for output handling
            process.readyReadStandardOutput.connect(
                lambda p=process: self.handle_process_output(p))
            process.finished.connect(
                lambda code, status, p=process, script=script_path: 
                self.handle_process_finished(code, status, p, script))
            
            self.processes.append((process, script_path))

        # Start the first process
        self.start_next_process()

    def start_next_process(self):
        if not self.processes:
            self.update_command_monitor("All processes completed.")
            return
            
        process, script_path = self.processes[0]
        python_executable = "/usr/bin/python3"
        
        try:
            projekt_info = self.gather_projekt_info()
            process.start(python_executable, [script_path])
            process.write(json.dumps(projekt_info).encode())
            process.closeWriteChannel()
            
            self.update_command_monitor(f"Started execution of {script_path}")
        except Exception as e:
            self.update_command_monitor(f"Error starting {script_path}: {str(e)}")
            self.processes.pop(0)
            self.start_next_process()

    def handle_process_output(self, process):
        output = process.readAllStandardOutput().data().decode()
        self.update_command_monitor(output)

    def handle_process_finished(self, exit_code, exit_status, process, script_path):
        if exit_code == 0:
            self.update_command_monitor(f"Successfully completed {script_path}")
        else:
            self.update_command_monitor(f"Error executing {script_path}. Exit code: {exit_code}")
        
        # Remove the completed process and start the next one
        self.processes.pop(0)
        self.start_next_process()

    def update_command_monitor(self, message):
        self.command_monitor.append(message.strip())
        # Force an immediate update
        QApplication.processEvents()
        # Scroll to bottom
        self.command_monitor.verticalScrollBar().setValue(
            self.command_monitor.verticalScrollBar().maximum()
        )

    def gather_projekt_info(self):
        # Extract projekt summary information
        projekt_summary = self.projekt_summary.toPlainText()
        summary_dict = {}
        for line in projekt_summary.split('\n'):
            if ':' in line:
                key, value = line.split(':', 1)
                summary_dict[key.strip()] = value.strip()

        # Extract environment summary information
        env_summary = self.environment_summary.toPlainText()
        env_dict = {}
        for line in env_summary.split('\n'):
            if ':' in line:
                key, value = line.split(':', 1)
                env_dict[key.strip()] = value.strip()

        the_projekt_flame_name = env_dict.get("Projekt Flame Name", "")
        # xml_project_dir = f"{the_projekt_flame_dirs}/{the_projekt_flame_name}"
        # xml_setup_dir = f"{xml_project_dir}/setups"
        # xml_media_dir = f"{xml_project_dir}/media"
        xml_project_dir = env_dict.get("Projekt Flame Directory", f"{the_projekt_flame_dirs}/{the_projekt_flame_name}")
        xml_setup_dir = env_dict.get("Setups Directory", f"{xml_project_dir}/setups_fail")
        xml_media_dir = env_dict.get("Media Cache", f"{xml_project_dir}/media_fail")
        # xml_ocio_config = f"/opt/Autodesk/colour_mgmt/configs/flame_configs/example_config/config.ocio"
        xml_ocio_config = f"/opt/Autodesk/colour_mgmt/configs/flame_configs/2026.0/aces2.0_config/config.ocio"
        # Below line is for Uncompressed DPX and EXR PIZ
        # xml_intermediates_profile = f"0:596088"
        # The line below is for ProRes4444 and EXR DWAA
        xml_intermediates_profile = f"65540:1120376"

        return {
            "the_projekt_serial_number": summary_dict.get("Serial Number", ""),
            "the_projekt_client_name": summary_dict.get("Client Name", ""),
            "the_projekt_campaign_name": summary_dict.get("Campaign Name", ""),
            "the_projekt_name": summary_dict.get("Projekt Name", ""),
            "the_projekt_resolution": summary_dict.get("Resolution", ""),
            "the_projekt_width": summary_dict.get("Width", ""),
            "the_projekt_height": summary_dict.get("Height", ""),
            "the_projekt_storage_aspect_ratio": summary_dict.get("Storage Aspect Ratio", ""),
            "the_projekt_display_aspect_ratio": summary_dict.get("Display Aspect Ratio", ""),
            "the_projekt_pixel_aspect_ratio": summary_dict.get("Pixel Aspect Ratio", ""),
            "the_projekt_aspect_ratio": summary_dict.get("Aspect Ratio", ""),
            "the_projekt_bit_depth": summary_dict.get("Bit Depth", ""),
            "the_projekt_frame_rate": summary_dict.get("Framerate", ""),
            "the_projekt_scan_mode": summary_dict.get("Scan Mode", ""),
            "the_projekt_start_frame": summary_dict.get("Start Frame", ""),
            "the_projekt_init_config": summary_dict.get("Init Config", ""),
            "the_projekt_color_science": summary_dict.get("Color Science", ""),

            "the_projekt_user_name": env_dict.get("Username", ""),
            "the_projekt_primary_group": env_dict.get("Group", ""),
            "the_projekt_os": env_dict.get("Operating System", ""),
            "the_hostname": env_dict.get("Hostname", ""),
            "the_projekt_localhostname": env_dict.get("Local Hostname", ""),
            "the_projekt_computername": env_dict.get("Computer Name", ""),
            "the_software_version": env_dict.get("Software Version", ""),
            "the_framestore": env_dict.get("Framestore", ""),
            "the_sanitized_sw_ver": env_dict.get("Sanitized App Ver", ""),
            "the_sanitized_version": env_dict.get("Sanitized Version#", ""),
            "the_projekt_flame_name": the_projekt_flame_name,
            "xml_project_dir": xml_project_dir,
            "xml_setup_dir": xml_setup_dir,
            "xml_media_dir": xml_media_dir,
            "xml_ocio_config": xml_ocio_config,
            "xml_intermediates_profile": xml_intermediates_profile,
        }

# =========================================================================== #

if __name__ == "__main__":
    app = QApplication(sys.argv)
    widget = WidgetLayoutRight()
    widget.show()
    sys.exit(app.exec())

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
# version:          1.9.9
# modified:         2024-12-25 - 09:50:18
# comments:         Preparation for future features
# -------------------------------------------------------------------------- #
# version:          2.0.0
# modified:         2024-12-31 - 11:17:26
# comments:         Improved legibility and minor modifications
# -------------------------------------------------------------------------- #
