# -------------------------------------------------------------------------- #

# File Name:        logik_projekt_creator.py
# Version:          1.11.0
# Language:         python script
# Author:           Phil MAN - phil_man@mac.com
# Created:          2024-05-23
# Modified:         2024-05-24

# Description:      This program creates a LOGIK-PROJEKT directory structure
#                   based on user input.

# -------------------------------------------------------------------------- #

import sys
import os
import logging
from datetime import datetime
from PySide6.QtWidgets import (QApplication, QMainWindow, QWidget, QVBoxLayout, QLabel, QLineEdit, QPushButton, QTextEdit, QMenuBar, QMenu, QComboBox)
from PySide6.QtGui import QAction, QPalette, QColor
from PySide6.QtCore import Qt

# Add the modules/functions directory to the system path
script_dir = os.path.dirname(os.path.abspath(__file__))
modules_dir = os.path.join(script_dir, 'modules', 'functions')
sys.path.append(modules_dir)

from debug_and_log import setup_logging
from os_check import check_operating_system
from string_utils import string_clean
from projekt_structure import create_logik_projekt_structure  # Corrected import
from define_dropdown_menus import dropdown_menu_definitions  # Import dropdown menu definitions

# ========================================================================== #
# Set up logging
# ========================================================================== #

script_path = os.path.abspath(__file__)
script_directory = os.path.dirname(script_path)

log_filepath = setup_logging(script_dir)

# ========================================================================== #
# Define the GUI application
# ========================================================================== #

class LogikProjektCreatorApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()
        self.update_environment_info()
        
    def initUI(self):
        """Initialize the user interface."""
        self.setWindowTitle('LOGIK-PROJEKT Creator')
        self.setGeometry(100, 100, 1024, 1024)
        self.center_window()

        # Set dark grey background
        self.setStyleSheet("background-color: #333333; color: {white};")

        central_widget = QWidget()
        layout = QVBoxLayout(central_widget)

        # Menu bar
        menu_bar = self.menuBar()

        # Environment information text box
        self.env_info_text = QTextEdit()
        self.env_info_text.setReadOnly(True)
        layout.addWidget(QLabel('Environment Information:'))
        layout.addWidget(self.env_info_text)

        # Base path input
        self.base_path_input = QLineEdit(self)
        layout.addWidget(QLabel('Enter the base path for the LOGIK-PROJEKT:'))
        layout.addWidget(self.base_path_input)

        # Projekt name input
        self.projekt_name_input = QLineEdit(self)
        layout.addWidget(QLabel('Enter the LOGIK-PROJEKT name:'))
        layout.addWidget(self.projekt_name_input)

        # Client Name input
        self.client_name_input = QLineEdit(self)
        layout.addWidget(QLabel('Enter the Client Name:'))
        layout.addWidget(self.client_name_input)

        # Campaign Name input
        self.campaign_name_input = QLineEdit(self)
        layout.addWidget(QLabel('Enter the Campaign Name:'))
        layout.addWidget(self.campaign_name_input)

        # Projekt Resolution dropdown
        self.projekt_resolution_input = QComboBox(self)
        self.projekt_resolution_input.addItems(dropdown_menu_definitions["Projekt Resolution"])
        layout.addWidget(QLabel('Select the Projekt Resolution:'))
        layout.addWidget(self.projekt_resolution_input)

        # Projekt Bit Depth dropdown
        self.projekt_bit_depth_input = QComboBox(self)
        self.projekt_bit_depth_input.addItems(dropdown_menu_definitions["Projekt Bit Depth"])
        layout.addWidget(QLabel('Select the Projekt Bit Depth:'))
        layout.addWidget(self.projekt_bit_depth_input)

        # Projekt Frame Rate dropdown
        self.projekt_frame_rate_input = QComboBox(self)
        self.projekt_frame_rate_input.addItems(dropdown_menu_definitions["Projekt Frame Rate"])
        layout.addWidget(QLabel('Select the Projekt Frame Rate:'))
        layout.addWidget(self.projekt_frame_rate_input)

        # Projekt Color Science dropdown
        self.projekt_color_science_input = QComboBox(self)
        self.projekt_color_science_input.addItems(dropdown_menu_definitions["Projekt Color Science"])
        layout.addWidget(QLabel('Select the Projekt Color Science:'))
        layout.addWidget(self.projekt_color_science_input)

        # Projekt Start Frame dropdown
        self.projekt_start_frame_input = QComboBox(self)
        self.projekt_start_frame_input.addItems(dropdown_menu_definitions["Projekt Start Frame"])
        layout.addWidget(QLabel('Select the Projekt Start Frame:'))
        layout.addWidget(self.projekt_start_frame_input)

        # Create LOGIK-PROJEKT button
        self.create_button = QPushButton('Create LOGIK-PROJEKT Structure', self)
        self.create_button.clicked.connect(self.on_create_button_click)
        layout.addWidget(self.create_button)

        # Create LOGIK-PROJEKT Template button
        self.create_template_button = QPushButton('Create LOGIK-PROJEKT Template', self)
        # Connect the button to a function when implemented
        layout.addWidget(self.create_template_button)

        # Cancel button
        self.cancel_button = QPushButton('Cancel', self)
        self.cancel_button.clicked.connect(self.close)
        layout.addWidget(self.cancel_button)

        # Summary text box
        self.summary_text = QTextEdit()
        self.summary_text.setReadOnly(True)
        layout.addWidget(QLabel('Summary:'))
        layout.addWidget(self.summary_text)

        # Set styles for widgets
        self.set_widget_styles()

        self.setCentralWidget(central_widget)

        # Connect textChanged signals of input fields to update_summary method
        self.base_path_input.textChanged.connect(self.update_summary)
        self.projekt_name_input.textChanged.connect(self.update_summary)
        self.client_name_input.textChanged.connect(self.update_summary)
        self.campaign_name_input.textChanged.connect(self.update_summary)
        self.projekt_resolution_input.currentTextChanged.connect(self.update_summary)
        self.projekt_bit_depth_input.currentTextChanged.connect(self.update_summary)
        self.projekt_frame_rate_input.currentTextChanged.connect(self.update_summary)
        self.projekt_color_science_input.currentTextChanged.connect(self.update_summary)
        self.projekt_start_frame_input.currentTextChanged.connect(self.update_summary)

    def center_window(self):
        """Center the window on the screen."""
        screen = QApplication.primaryScreen().geometry()
        window = self.geometry()
        x = (screen.width() - window.width()) // 2
        y = (screen.height() - window.height()) // 2
        self.move(x, y)

    def set_widget_styles(self):
        """Set the styles for the widgets."""
        dark_grey = "#111111"
        white = "#ffffff"
        red = "#500000"  # Dark red
        sky_blue = "#7F4D00"  # Dark Orange
        mid_green = "#174F00"  # Dark green
        widgets = [
            self.env_info_text, self.base_path_input, self.projekt_name_input, 
            self.client_name_input, self.campaign_name_input, self.projekt_resolution_input, 
            self.projekt_bit_depth_input, self.projekt_frame_rate_input, 
            self.projekt_color_science_input, self.projekt_start_frame_input, 
            self.create_button, self.create_template_button, self.cancel_button, 
            self.summary_text
        ]
        for widget in widgets:
            widget.setStyleSheet(f"background-color: {dark_grey}; color: {white};")

        # Set Cancel button style
        self.cancel_button.setStyleSheet(f"background-color: {red}; color: {white};")

        # Set Create LOGIK-PROJEKT Template button style
        self.create_template_button.setStyleSheet(f"background-color: {sky_blue}; color: {dark_grey};")

        # Set Create LOGIK-PROJEKT Structure button style
        self.create_button.setStyleSheet(f"background-color: {mid_green}; color: {white};")

    def update_environment_info(self):
        """Update the environment information text box."""
        try:
            os_type = check_operating_system()
            env_info = (
                f"Script Path: {script_path}\n"
                f"Script Directory: {script_directory}\n"
                f"Log Directory: {log_filepath}\n"
                f"Operating System: {os_type}\n"
            )
            self.env_info_text.setText(env_info)
        except Exception as e:
            logging.error(f"An error occurred while updating environment info: {e}")
            self.env_info_text.setText(f"An error occurred: {e}")

    def on_create_button_click(self):
        """Handle the create button click event."""
        try:
            base_path = self.base_path_input.text().strip()
            projekt_name = string_clean(self.projekt_name_input.text().strip())
            client_name = self.client_name_input.text().strip()
            campaign_name = self.campaign_name_input.text().strip()
            projekt_resolution = self.projekt_resolution_input.currentText()
            projekt_bit_depth = self.projekt_bit_depth_input.currentText()
            projekt_frame_rate = self.projekt_frame_rate_input.currentText()
            projekt_color_science = self.projekt_color_science_input.currentText()
            projekt_start_frame = self.projekt_start_frame_input.currentText()

            if not base_path or not projekt_name:
                raise ValueError("Both base path and LOGIK-PROJEKT name must be provided.")

            create_logik_projekt_structure(base_path, projekt_name)

            self.env_info_text.append("\nLOGIK-PROJEKT structure created successfully.")
            self.env_info_text.append(f"Client Name: {client_name}")
            self.env_info_text.append(f"Campaign Name: {campaign_name}")
            logging.info("LOGIK-PROJEKT structure created successfully.")

            # Update summary text
            summary = (
                f"LOGIK-PROJEKT Name: {projekt_name}\n"
                f"Client Name: {client_name}\n"
                f"Campaign Name: {campaign_name}\n"
                f"Projekt Resolution: {projekt_resolution}\n"
                f"Projekt Bit Depth: {projekt_bit_depth}\n"
                f"Projekt Frame Rate: {projekt_frame_rate}\n"
                f"Projekt Color Science: {projekt_color_science}\n"
                f"Projekt Start Frame: {projekt_start_frame}\n"
            )
            self.summary_text.setText(summary)
        except ValueError as ve:
            logging.error(f"Validation error: {ve}")
            self.env_info_text.append(f"\nValidation error: {ve}")
        except Exception as e:
            logging.error(f"An error occurred: {e}")
            self.env_info_text.append(f"\nAn error occurred: {e}")

# ========================================================================== #
# Main execution
# ========================================================================== #

if __name__ == "__main__":
    app = QApplication([])

    window = LogikProjektCreatorApp()
    window.show()

    app.exec()
