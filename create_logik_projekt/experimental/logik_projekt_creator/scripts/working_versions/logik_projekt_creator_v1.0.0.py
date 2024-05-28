# -------------------------------------------------------------------------- #

# File Name:        logik_projekt_creator.py
# Version:          1.0.0
# Language:         python script
# Author:           Phil MAN - phil_man@mac.com
# Created:          2024-05-23
# Modified:         2024-05-26s

# Description:      This program creates a LOGIK-PROJEKT directory structure
#                   based on user input.

# -------------------------------------------------------------------------- #

import sys

import os

import logging

from datetime import datetime

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

log_filepath = setup_logging(script_dir)
