# filename: FlameTextEdit

# -------------------------------------------------------------------------- #

# File Name:        FlameTextEdit.py
# Version:          0.0.4
# Language:         python script
# Flame Version:    2025.x
# Author:           Phil MAN - phil_man@mac.com
# Toolset:          MAN_MADE_MATERIAL: LOGIK-PROJEKT
# Created:          2024-04-20
# Modified:         2024-05-09
# Modifier:         Phil MAN - phil_man@mac.com

# Description:      This program is part of a library of custom functions
#                   and modules for autodesk flame.

# Installation:     Copy the 'LOGIK-PROJEKT' repo to your GitHub directory,
#                   e.g. '/home/$USER/workspace/GitHub'

# Attribution:      This script is derived from work originally authored by
#                   Michael Vaglienty: 'pyflame_lib_script_template.py'

# Changelist:       The full changelist is at the end of this document.

# -------------------------------------------------------------------------- #

# ========================================================================== #
# This section imports the necessary modules.
# ========================================================================== #

from PySide6 import QtWidgets, QtCore, QtGui
import xml.etree.ElementTree as ET
from typing import Union, List, Dict, Optional, Callable
import os, re, datetime, shutil, ast

class FlameTextEdit(QtWidgets.QPlainTextEdit): # Fix for flame 2025
    '''
    Custom Qt Flame Text Edit Widget

    FlameTextEdit(text[, read_only=False])

    text: text to be displayed [str]
    read_only: (optional) make text in window read only [bool] - default is False

    Example:

        text_edit = FlameTextEdit('Some important text here', read_only=True)
    '''

    def __init__(self, text: str, read_only: Optional[bool]=False):
        super(FlameTextEdit, self).__init__()

        # Check argument types

        if not isinstance(text, str):
            raise TypeError('FlameTextEdit: text must be a string.')
        if not isinstance(read_only, bool):
            raise TypeError('FlameTextEdit: read_only must be a boolean.')

        # Build text edit

        self.setMinimumHeight(50)
        self.setMinimumWidth(150)
        self.setText(text)
        self.setReadOnly(read_only)
        self.setFocusPolicy(QtCore.Qt.ClickFocus)

        if read_only:
            self.setStyleSheet('QTextEdit {color: rgb(154, 154, 154); background-color: #37414b; selection-color: #262626; selection-background-color: #b8b1a7; border: none; padding-left: 5px; font: 14px "Discreet"}'
                               'QScrollBar {color: 111111; background: rgb(49, 49, 49)}'
                               'QScrollBar::handle {color: 111111; background : 111111;}'
                               'QScrollBar::add-line:vertical {border: none; background: none; width: 0px; height: 0px}'
                               'QScrollBar::sub-line:vertical {border: none; background: none; width: 0px; height: 0px}'
                               'QScrollBar {color: 111111; background: rgb(49, 49, 49)}'
                               'QScrollBar::handle {color: 111111; background : 111111;}'
                               'QScrollBar::add-line:horizontal {border: none; background: none; width: 0px; height: 0px}'
                               'QScrollBar::sub-line:horizontal {border: none; background: none; width: 0px; height: 0px}')
        else:
            self.setStyleSheet('QTextEdit {color: rgb(154, 154, 154); background-color: #37414b; selection-color: #262626; selection-background-color: #b8b1a7; border: none; padding-left: 5px; font: 14px "Discreet"}'
                               'QTextEdit:focus {background-color: #495663}'
                               'QScrollBar {color: 111111; background: rgb(49, 49, 49)}'
                               'QScrollBar::handle {color: 111111; background : 111111;}'
                               'QScrollBar::add-line:vertical {border: none; background: none; width: 0px; height: 0px}'
                               'QScrollBar::sub-line:vertical {border: none; background: none; width: 0px; height: 0px}'
                               'QScrollBar {color: 111111; background: rgb(49, 49, 49)}'
                               'QScrollBar::handle {color: 111111; background : 111111;}'
                               'QScrollBar::add-line:horizontal {border: none; background: none; width: 0px; height: 0px}'
                               'QScrollBar::sub-line:horizontal {border: none; background: none; width: 0px; height: 0px}')

# ========================================================================== #
# This section defines how to handle the main script function.
# ========================================================================== #

# # If this script is executed as main:
# # Call functions for immediate execution
# if __name__ == "__main__":

# ========================================================================== #
# C2 A9 2D 32 30 32 34 2D 4D 41 4E 5F 4D 41 44 45 5F 4D 41 54 45 52 49 61 4C #
# ========================================================================== #

# Changelist:
# -------------------------------------------------------------------------- #
# version:               0.0.1
# modified:              2024-05-07 - 21:48:20
# comments:              Refactored monolithic code to discreet modules
# -------------------------------------------------------------------------- #
# version:               0.0.2
# modified:              2024-05-07 - 21:49:31
# comments:              Added docstrings
# -------------------------------------------------------------------------- #
# version:               0.0.3
# modified:              2024-05-07 - 21:50:00
# comments:              Prep for initial production test
# -------------------------------------------------------------------------- #
# version:               0.0.4
# modified:              2024-05-09 - 13:18:47
# comments:              Refactored code works in flame 2025. Time to tidy up.
