# filename: FlameButton.py

# -------------------------------------------------------------------------- #

# File Name:        FlameButton.py
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

class FlameButton(QtWidgets.QPushButton):
    '''
    Custom Qt Flame Button Widget

    FlameButton(button_name, connect[, button_color='normal', button_width=150, button_max_width=150])

    button_name: button text [str]
    connect: execute when clicked [function]
    button_color: (optional) normal, blue, red [str]
    button_width: (optional) default is 150 [int]
    button_max_width: (optional) default is 150 [int]

    Example:

        button = FlameButton('Button Name', do_something_magical_when_pressed, button_color='blue')
    '''

    def __init__(self, button_name: str, connect: Callable[..., None], button_color: Optional[str]='normal', button_width: Optional[int]=150, button_max_width: Optional[int]=150) -> None:
        super(FlameButton, self).__init__()

        # Check argument types

        if not isinstance(button_name, str):
            raise TypeError('FlameButton: button_name must be a string')
        elif button_color not in ['normal', 'blue', 'red']:
            raise ValueError('FlameButton: button_color must be one of: normal(grey), blue, or red')
        elif not isinstance(button_width, int):
            raise TypeError('FlameButton: button_width must be an integer')
        elif not isinstance(button_max_width, int):
            raise TypeError('FlameButton: button_max_width must be an integer')

        # Build button

        self.setText(button_name)
        self.setMinimumSize(QtCore.QSize(button_width, 28))
        self.setMaximumSize(QtCore.QSize(button_max_width, 28))
        self.setFocusPolicy(QtCore.Qt.NoFocus)
        self.clicked.connect(connect)
        if button_color == 'normal':
            self.setStyleSheet('QPushButton {color: rgb(154, 154, 154); background-color: rgb(58, 58, 58); border: none; font: 14px "Discreet"}'
                               'QPushButton:hover {border: 1px solid rgb(90, 90, 90)}'
                               'QPushButton:pressed {color: rgb(159, 159, 159); background-color: rgb(66, 66, 66); border: 1px solid rgb(90, 90, 90)}'
                               'QPushButton:disabled {color: rgb(116, 116, 116); background-color: rgb(58, 58, 58); border: none}'
                               'QPushButton::menu-indicator {subcontrol-origin: padding; subcontrol-position: center right}'
                               'QToolTip {color: rgb(170, 170, 170); background-color: rgb(71, 71, 71); border: 10px solid rgb(71, 71, 71)}')
        elif button_color == 'blue':
            self.setStyleSheet('QPushButton {color: rgb(190, 190, 190); background-color: rgb(0, 110, 175); border: none; font: 14px "Discreet"}'
                               'QPushButton:hover {border: 1px solid rgb(90, 90, 90)}'
                               'QPushButton:pressed {color: rgb(159, 159, 159); border: 1px solid rgb(90, 90, 90)'
                               'QPushButton:disabled {color: rgb(116, 116, 116); background-color: rgb(58, 58, 58); border: none}'
                               'QToolTip {color: rgb(170, 170, 170); background-color: rgb(71, 71, 71); border: 10px solid rgb(71, 71, 71)}')
        elif button_color == 'red':
            self.setStyleSheet('QPushButton {color: rgb(190, 190, 190); background-color: rgb(200, 29, 29); border: none; font: 14px "Discreet"}'
                               'QPushButton:hover {border: 1px solid rgb(90, 90, 90)}'
                               'QPushButton:pressed {color: rgb(159, 159, 159); border: 1px solid rgb(90, 90, 90)'
                               'QPushButton:disabled {color: rgb(116, 116, 116); background-color: rgb(58, 58, 58); border: none}'
                               'QToolTip {color: rgb(170, 170, 170); background-color: rgb(71, 71, 71); border: 10px solid rgb(71, 71, 71)}')

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
