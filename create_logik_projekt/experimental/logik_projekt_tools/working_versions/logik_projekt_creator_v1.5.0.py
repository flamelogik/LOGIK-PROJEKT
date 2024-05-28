'''
# -------------------------------------------------------------------------- #

# File Name:        logik_projekt_creator.py
# Version:          1.5.0
# Language:         python script
# Author:           Phil MAN - phil_man@mac.com
# Created:          2024-05-23
# Modified:         2024-05-24

# Description:      This program creates a LOGIK-PROJEKT directory structure
#                   based on user input.

# -------------------------------------------------------------------------- #
'''

import sys
import os
import logging
from datetime import datetime
from PySide6.QtWidgets import (QApplication, QWidget, QVBoxLayout, QLabel, QLineEdit, QPushButton, QTextEdit)

# Add the modules/functions directory to the system path
script_dir = os.path.dirname(os.path.abspath(__file__))
modules_dir = os.path.join(script_dir, 'modules', 'functions')
sys.path.append(modules_dir)

from debug_and_log import setup_logging
from os_check import check_operating_system
from string_utils import string_clean
from projekt_structure import create_logik_projekt_structure

# ========================================================================== #
# Set up logging
# ========================================================================== #

script_path = os.path.abspath(__file__)
script_directory = os.path.dirname(script_path)

log_filepath = setup_logging(script_dir)

# ========================================================================== #
# Define the GUI application
# ========================================================================== #

class LogikProjektCreatorApp(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
        self.update_environment_info()

    def initUI(self):
        """Initialize the user interface."""
        self.setWindowTitle('LOGIK-PROJEKT Creator')
        self.setGeometry(100, 100, 600, 400)

        layout = QVBoxLayout()

        self.env_info_text = QTextEdit()
        self.env_info_text.setReadOnly(True)
        layout.addWidget(QLabel('Environment Information:'))
        layout.addWidget(self.env_info_text)

        self.base_path_input = QLineEdit(self)
        layout.addWidget(QLabel('Enter the base path for the LOGIK-PROJEKT:'))
        layout.addWidget(self.base_path_input)

        self.projekt_name_input = QLineEdit(self)
        layout.addWidget(QLabel('Enter the LOGIK-PROJEKT name:'))
        layout.addWidget(self.projekt_name_input)

        self.client_name_input = QLineEdit(self)
        layout.addWidget(QLabel('Enter the Client Name:'))
        layout.addWidget(self.client_name_input)

        self.campaign_name_input = QLineEdit(self)
        layout.addWidget(QLabel('Enter the Campaign Name:'))
        layout.addWidget(self.campaign_name_input)

        self.create_button = QPushButton('Create LOGIK-PROJEKT Structure', self)
        self.create_button.clicked.connect(self.on_create_button_click)
        layout.addWidget(self.create_button)

        self.create_template_button = QPushButton('Create LOGIK-PROJEKT Template', self)
        # Connect the button to a function when implemented
        layout.addWidget(self.create_template_button)

        self.cancel_button = QPushButton('Cancel', self)
        self.cancel_button.clicked.connect(self.close)
        layout.addWidget(self.cancel_button)

        self.setLayout(layout)

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

            if not base_path or not projekt_name:
                raise ValueError("Both base path and LOGIK-PROJEKT name must be provided.")

            create_logik_projekt_structure(base_path, projekt_name)

            self.env_info_text.append("\nLOGIK-PROJEKT structure created successfully.")
            self.env_info_text.append(f"Client Name: {client_name}")
            self.env_info_text.append(f"Campaign Name: {campaign_name}")
            logging.info("LOGIK-PROJEKT structure created successfully.")
        except ValueError as ve:
            logging.warning(f"Validation error: {ve}")
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
