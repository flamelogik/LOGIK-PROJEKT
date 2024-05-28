# -------------------------------------------------------------------------- #
# File Name:        logik_projekt_creator.py
# Version:          1.0.1
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

log_filepath = setup_logging(script_directory)
