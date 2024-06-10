'''
File Name:        projekt_utilities_templator.py
Version:          1.0.0
Language:         python script
Author:           Phil MAN - phil_man@mac.com
Created:          2024-05-23
Modified:         2024-06-02

Description:      This program creates logik projekt templates
'''

# ========================================================================== #
# This section defines the import statements
# ========================================================================== #

import sys
import os
import logging
from datetime import datetime

# -------------------------------------------------------------------------- #

# Try to import PySide6 modules first;
try:
    from PySide6.QtWidgets import (
        QApplication,
        QFileDialog,
        QMainWindow,
        QWidget,
        QVBoxLayout,
        QLabel,
        QLineEdit,
        QTextEdit,
        QComboBox,
        QPushButton
    )
    from PySide6.QtGui import (
        QPalette,
        QColor
    )
    from PySide6.QtCore import (
        Qt
    )
    print("Using PySide6")

except ImportError:

    # fall back to PySide2 if PySide 6 is not available
    from PySide2.QtWidgets import (
        QApplication,
        QMainWindow,
        QWidget,
        QVBoxLayout,
        QLabel,
        QLineEdit,
        QTextEdit,
        QComboBox,
        QPushButton
    )
    from PySide2.QtGui import (
        QPalette,
        QColor
    )
    from PySide2.QtCore import (
        Qt
    )
    print("Using PySide2")

# -------------------------------------------------------------------------- #

# Add the modules/functions directory to the system path
script_path = os.path.abspath(__file__)
script_directory = os.path.dirname(script_path)
modules_dir = os.path.join(script_directory, 'modules', 'functions')
sys.path.append(modules_dir)

# -------------------------------------------------------------------------- #

from modules.functions.debug_and_log import setup_logging
from modules.functions.projekt_utilities_os import check_operating_system
from modules.functions.projekt_utilities_strings import string_clean
from modules.functions.define_dropdown_menus import dropdown_menu_definitions

# ========================================================================== #
# This section defines the import statements
# ========================================================================== #

def create_projekt_template(client_name, campaign_name, summary_text):
    # Validate that client_name and campaign_name are not empty
    if not client_name:
        raise ValueError("Client name cannot be empty")
    if not campaign_name:
        raise ValueError("Campaign name cannot be empty")

    # Prompt the user to choose where to save the Logik Projekt Template
    app = QApplication.instance()  # Get the existing QApplication instance
    if app is None:
        app = QApplication([])  # Create a new QApplication if none exists

    options = QFileDialog.Options()
    options |= QFileDialog.ShowDirsOnly
    directory = QFileDialog.getExistingDirectory(None, "Select Directory", options=options)

    if not directory:
        raise ValueError("No directory selected")

    # Create the projekt_template_file name
    now = datetime.now()
    date_time_str = now.strftime("%Y_%m_%d_%H_%M")
    filename = f"projekt_template_{date_time_str}_{client_name}_{campaign_name}"
    file_path = os.path.join(directory, filename)

    # Write the summary text to the projekt_template_file
    with open(file_path, 'w') as file:
        file.write(summary_text)

    return file_path

# ========================================================================== #
# C2 A9 32 30 32 34 2D 4D 41 4E 5F 4D 41 44 45 2D 4D 45 4B 41 4E 49 53 4D 5A #
# ========================================================================== #

'''
Disclaimer:       This program is part of LOGIK-PROJEKT.
                  LOGIK-PROJEKT is free software.

                  You can redistribute it and/or modify it under the terms
                  of the GNU General Public License as published by the
                  Free Software Foundation, either version 3 of the License,
                  or any later version.

                  This program is distributed in the hope that it will be
                  useful, but WITHOUT ANY WARRANTY; without even the
                  implied warranty of MERCHANTABILITY or FITNESS FOR A
                  PARTICULAR PURPOSE.

                  See the GNU General Public License for more details.

                  You should have received a copy of the GNU General
                  Public License along with this program.

                  If not, see <https://www.gnu.org/licenses/>.
'''

# -------------------------------------------------------------------------- #
# Changelist:
# -------------------------------------------------------------------------- #
