# -------------------------------------------------------------------------- #
# File Name:        logik_projekt_creator.py
# Version:          1.0.3
# Language:         python script
# Author:           Phil MAN - phil_man@mac.com
# Created:          2024-05-23
# Modified:         2024-05-27
# Description:      This program is part of LOGIK-PROJEKT.
# -------------------------------------------------------------------------- #

import sys
import os
import logging
from datetime import datetime

# Try to import PySide6 modules first; fall back to PySide2 if not available
try:
    from PySide6.QtWidgets import (
        QApplication, 
        QMainWindow, 
        QWidget, 
        QVBoxLayout, 
        QLabel, 
        QLineEdit, 
        QPushButton, 
        QTextEdit, 
        QMenuBar, 
        QMenu, 
        QComboBox
    )
    from PySide6.QtGui import (
        QAction, 
        QPalette, 
        QColor
    )
    from PySide6.QtCore import (
        Qt
    )
    print("Using PySide6")
except ImportError:
    from PySide2.QtWidgets import (
        QApplication, 
        QMainWindow, 
        QWidget, 
        QVBoxLayout, 
        QLabel, 
        QLineEdit, 
        QPushButton, 
        QTextEdit, 
        QMenuBar, 
        QMenu, 
        QComboBox
    )
    from PySide2.QtGui import (
        QAction, 
        QPalette, 
        QColor
    )
    from PySide2.QtCore import (
        Qt
    )
    print("Using PySide2")

# Add the modules/functions directory to the system path
script_path = os.path.abspath(__file__)
script_directory = os.path.dirname(script_path)
modules_dir = os.path.join(script_directory, 'modules', 'functions')
sys.path.append(modules_dir)

from debug_and_log import setup_logging
from os_check import check_operating_system
from string_utils import string_clean
from projekt_structure import create_logik_projekt_structure
from define_dropdown_menus import dropdown_menu_definitions

# ========================================================================== #
# Set up logging
# ========================================================================== #

log_filepath = setup_logging()

# ========================================================================== #
# New Functionality: Log Directory Creation
# ========================================================================== #

def create_and_log_directory(path):
    """Create a directory and log its creation."""
    try:
        os.makedirs(path, exist_ok=True)
        logging.info(f"Created directory: {path}")
    except Exception as e:
        logging.error(f"Failed to create directory {path}: {e}")

def create_logik_projekt_structure_with_logging(base_path):
    """Create LOGIK-PROJEKT directory structure and log each step."""
    directories = [
        os.path.join(base_path, "dir1"),
        os.path.join(base_path, "dir2"),
        os.path.join(base_path, "dir1", "subdir1"),
        os.path.join(base_path, "dir1", "subdir2"),
        os.path.join(base_path, "dir2", "subdir1"),
    ]
    
    for directory in directories:
        create_and_log_directory(directory)

# ========================================================================== #
# GUI Setup
# ========================================================================== #

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        
        # Set window properties
        self.setWindowTitle("LOGIK-PROJEKT Creator")
        self.setGeometry(0, 0, 1024, 960)
        self.center()
        
        # Set the background color
        self.setStyleSheet("background-color: #333333;")
        
        # Create central widget and layout
        central_widget = QWidget()
        layout = QVBoxLayout()
        central_widget.setLayout(layout)
        self.setCentralWidget(central_widget)
        
        # Add widgets
        self.projekt_serial_number = self.create_labeled_entry(layout, "Projekt Serial Number")
        self.projekt_client_name = self.create_labeled_entry(layout, "Projekt Client Name")
        self.projekt_campaign_name = self.create_labeled_entry(layout, "Projekt Campaign Name")
        
    def center(self):
        frame_geometry = self.frameGeometry()
        screen_center = QApplication.primaryScreen().availableGeometry().center()
        frame_geometry.moveCenter(screen_center)
        self.move(frame_geometry.topLeft())
    
    def create_labeled_entry(self, layout, label_text):
        """Create a labeled text entry box."""
        label = QLabel(label_text)
        label.setStyleSheet("color: white; font-family: 'Courier New', monospace;")
        layout.addWidget(label)
        
        entry = QLineEdit()
        entry.setStyleSheet("""
            background-color: #111111;
            color: white;
            font-family: 'Courier New', monospace;
            font-weight: bold;
        """)
        layout.addWidget(entry)
        return entry

# ========================================================================== #
# Application Entry Point
# ========================================================================== #

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())

# ========================================================================== #
# Changelist
# ========================================================================== #
# Version 1.0.1
# - Added failover to PySide2 if PySide6 is not installed.
# - Updated the description in the header.
#
# Version 1.0.2
# - Added functionality to log the creation of each directory in the 
#   LOGIK-PROJEKT structure.
#
# Version 1.0.3
# - Added a GUI with the following features:
#   - Centered on launch.
#   - 1024 pixels wide and 960 pixels tall.
#   - Dark grey background (#333333).
#   - Monospaced and white text.
#   - Styled text entry boxes with a dark background (#111111), bold, 
#     monospaced, and white font.
#   - Text entry boxes for Projekt Serial Number, Projekt Client Name, 
#     and Projekt Campaign Name.
