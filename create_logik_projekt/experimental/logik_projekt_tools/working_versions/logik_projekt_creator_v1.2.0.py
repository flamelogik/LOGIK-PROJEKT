'''
# -------------------------------------------------------------------------- #

# File Name:        logik_projekt_creator.py
# Version:          1.2.0
# Language:         python script
# Author:           [Your Name] - [Your Email]
# Created:          2024-05-23
# Modified:         2024-05-24

# Description:      This program creates a LOGIK-PROJEKT directory structure
#                   based on user input.

# -------------------------------------------------------------------------- #
'''

import os
import platform
import logging
from datetime import datetime
from PySide6.QtWidgets import (QApplication, QWidget, QVBoxLayout, QLabel, QLineEdit, QPushButton, QTextEdit)

# ========================================================================== #
# Import logging setup from debug_and_log.py
# ========================================================================== #

from modules.functions.debug_and_log import setup_logging

# ========================================================================== #
# Set up logging
# ========================================================================== #

script_path = os.path.abspath(__file__)
script_directory = os.path.dirname(script_path)
log_directory = os.path.join(script_directory, 'log')

if not os.path.exists(log_directory):
    os.makedirs(log_directory)

log_filename = f"{datetime.now():%Y-%m-%d-%H-%M}_logik_projekt_creator.debug.log"
log_filepath = os.path.join(log_directory, log_filename)

setup_logging(filename=log_filepath)

# ========================================================================== #
# Define functions for checking the operating system
# ========================================================================== #

def check_operating_system():
    """Check if the operating system is Linux or macOS."""
    os_name = platform.system()
    if os_name == 'Linux':
        logging.info("Operating system is Linux.")
        return 'Linux'
    elif os_name == 'Darwin':
        logging.info("Operating system is macOS.")
        return 'macOS'
    else:
        logging.error(f"Unsupported operating system: {os_name}")
        raise EnvironmentError(f"Unsupported operating system: {os_name}")

# ========================================================================== #
# Define functions to create the LOGIK-PROJEKT structure
# ========================================================================== #

def create_directory(path):
    """Create a directory if it does not exist."""
    if not os.path.exists(path):
        os.makedirs(path)
        logging.info(f"Created directory: {path}")
    else:
        logging.warning(f"Directory already exists: {path}")

def create_logik_projekt_structure(base_path, projekt_name):
    """Create the directory structure for a new LOGIK-PROJEKT."""
    projekt_path = os.path.join(base_path, projekt_name)
    
    # Create main LOGIK-PROJEKT directory
    create_directory(projekt_path)
    
    # Define subdirectories
    subdirectories = [
        'build',
        'config',
        'doc',
        'experimental',
        'log',
        'pref',
        'script',
        'temp',
        'www',
        'version'
    ]
    
    for subdirectory in subdirectories:
        create_directory(os.path.join(projekt_path, subdirectory))

# ========================================================================== #
# Define the GUI application
# ========================================================================== #

class LogikProjektCreatorApp(QWidget):
    def __init__(self):
        super().__init__()

        self.initUI()
        self.update_environment_info()

    def initUI(self):
        self.setWindowTitle('LOGIK-PROJEKT Creator')
        self.setGeometry(100, 100, 600, 400)

        layout = QVBoxLayout()

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

        self.setLayout(layout)

    def update_environment_info(self):
        """Update the environment information text box."""
        try:
            os_type = check_operating_system()
            env_info = (
                f"Script Path: {script_path}\n"
                f"Script Directory: {script_directory}\n"
                f"Log Directory: {log_directory}\n"
                f"Log Filename: {log_filename}\n"
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
            projekt_name = self.projekt_name_input.text().strip()

            if not base_path or not projekt_name:
                raise ValueError("Both base path and LOGIK-PROJEKT name must be provided.")

            create_logik_projekt_structure(base_path, projekt_name)

            self.env_info_text.append("\nLOGIK-PROJEKT structure created successfully.")
            logging.info("LOGIK-PROJEKT structure created successfully.")
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
