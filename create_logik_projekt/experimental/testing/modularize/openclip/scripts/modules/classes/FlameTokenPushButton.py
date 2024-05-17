# filename: FlameTokenPushButton.py

# -------------------------------------------------------------------------- #

# File Name:        FlameTokenPushButton.py
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

from PySide6 import (
    QtWidgets,
    QtCore,
    QtGui
)
import xml.etree.ElementTree as ET
from typing import (
    Union,
    List,
    Dict,
    Optional,
    Callable
)
import os
import re
import datetime
import shutil
import ast

class FlameTokenPushButton(QtWidgets.QPushButton):
    '''
    Custom Qt Flame Token Push Button Widget

    FlameTokenPushButton(button_name, token_dict, token_dest[, button_width=150, button_max_width=300])

    button_name: Text displayed on button [str]
    token_dict: Dictionary defining tokens. {'Token Name': '<Token>'} [dict]
    token_dest: QLineEdit that token will be applied to [QtWidgets.QLineEdit]
    button_width: (optional) default is 150 [int]
    button_max_width: (optional) default is 300 [int]

    Example:

        token_dict = {'Token 1': '<Token1>', 'Token2': '<Token2>'}
        token_push_button = FlameTokenPushButton('Add Token', token_dict, token_dest)
    '''

    def __init__(self, button_name: str, token_dict: Dict[str, str], token_dest, button_width: Optional[int]=150, button_max_width:Optional[int]=300):
        super(FlameTokenPushButton, self).__init__()
        from functools import partial

        # Check argument types

        if not isinstance(button_name, str):
            raise TypeError('FlameTokenPushButton: button_name must be a string.')
        if not isinstance(token_dict, dict):
            raise TypeError('FlameTokenPushButton: token_dict must be a dictionary.')
        if not isinstance(token_dest, QtWidgets.QLineEdit):
            raise TypeError('FlameTokenPushButton: token_dest must be a QLineEdit.')
        if not isinstance(button_width, int):
            raise TypeError('FlameTokenPushButton: button_width must be an integer.')
        if not isinstance(button_max_width, int):
            raise TypeError('FlameTokenPushButton: button_max_width must be an integer.')

        # Build token push button

        self.setText(button_name)
        self.setMinimumHeight(28)
        self.setMinimumWidth(button_width)
        self.setMaximumWidth(button_max_width)
        self.setFocusPolicy(QtCore.Qt.NoFocus)
        self.setStyleSheet('QPushButton {color: rgb(154, 154, 154); background-color: rgb(45, 55, 68); border: none; font: 14px "Discreet"}'
                           'QPushButton:hover {border: 1px solid rgb(90, 90, 90)}'
                           'QPushButton:disabled {color: rgb(106, 106, 106); background-color: rgb(45, 55, 68); border: none}'
                           'QPushButton::menu-indicator {subcontrol-origin: padding; subcontrol-position: center right}'
                           'QToolTip {color: rgb(170, 170, 170); background-color: rgb(71, 71, 71); border: 10px solid rgb(71, 71, 71)}')

        def token_action_menu():

            def insert_token(token):
                for key, value in token_dict.items():
                    if key == token:
                        token_name = value
                        token_dest.insert(token_name)

            for key, value in token_dict.items():
                token_menu.addAction(key, partial(insert_token, key))

        token_menu = QtWidgets.QMenu(self)
        token_menu.setFocusPolicy(QtCore.Qt.NoFocus)
        token_menu.setStyleSheet('QMenu {color: rgb(154, 154, 154); background-color: rgb(45, 55, 68); border: none; font: 14px "Discreet"}'
                                 'QMenu::item:selected {color: rgb(217, 217, 217); background-color: rgb(58, 69, 81)}')

        self.setMenu(token_menu)

        token_action_menu()

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
