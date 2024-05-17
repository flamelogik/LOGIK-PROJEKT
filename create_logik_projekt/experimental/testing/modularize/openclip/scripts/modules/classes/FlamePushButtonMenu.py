# filename: FlamePushButtonMenu.py

# -------------------------------------------------------------------------- #

# File Name:        FlamePushButtonMenu.py
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

class FlamePushButtonMenu(QtWidgets.QPushButton):
    '''
    Custom Qt Flame Menu Push Button Widget

    FlamePushButtonMenu(button_name, menu_options[, menu_width=150, max_menu_width=2000, menu_action=None])

    button_name: text displayed on button [str]
    menu_options: list of options show when button is pressed [list]
    menu_width: (optional) width of widget. default is 150. [int]
    max_menu_width: (optional) set maximum width of widget. default is 2000. [int]
    menu_action: (optional) execute when button is changed. [function]

    To update an existing button menu:

    FlamePushButtonMenu.update_menu(button_name, menu_options[, menu_action=None])

    button_name: text displayed on button [str]
    menu_options: list of options show when button is pressed [list]
    menu_action: (optional) execute when button is changed. [function]

    Examples:

        push_button_menu_options = ['Item 1', 'Item 2', 'Item 3', 'Item 4']
        menu_push_button = FlamePushButtonMenu('push_button_name', push_button_menu_options)

        or

        push_button_menu_options = ['Item 1', 'Item 2', 'Item 3', 'Item 4']
        menu_push_button = FlamePushButtonMenu(push_button_menu_options[0], push_button_menu_options)
    '''

    def __init__(self, button_name: str, menu_options: List[str], menu_width: Optional[int]=150, max_menu_width: Optional[int]=2000, menu_action: Optional[Callable[..., None]]=None):
        super(FlamePushButtonMenu, self).__init__()
        from functools import partial

        # Check argument types

        if not isinstance(button_name, str):
            raise TypeError('FlamePushButtonMenu: button_name must be string.')
        if not isinstance(menu_options, list):
            raise TypeError('FlamePushButtonMenu: menu_options must be list.')
        if not isinstance(menu_width, int):
            raise TypeError('FlamePushButtonMenu: menu_width must be integer.')
        if not isinstance(max_menu_width, int):
            raise TypeError('FlamePushButtonMenu: max_menu_width must be integer.')

        # Build push button menu

        self.setText(button_name)
        self.setMinimumHeight(28)
        self.setMinimumWidth(menu_width)
        self.setMaximumWidth(max_menu_width)
        self.setFocusPolicy(QtCore.Qt.NoFocus)
        self.setStyleSheet('QPushButton {color: rgb(154, 154, 154); background-color: rgb(45, 55, 68); border: none; font: 14px "Discreet"}'
                           'QPushButton:disabled {color: rgb(116, 116, 116); background-color: rgb(45, 55, 68); border: none}'
                           'QPushButton:hover {border: 1px solid rgb(90, 90, 90)}'
                           'QPushButton::menu-indicator {image: none}'
                           'QToolTip {color: rgb(170, 170, 170); background-color: rgb(71, 71, 71); border: 10px solid rgb(71, 71, 71)}')

        self.pushbutton_menu = QtWidgets.QMenu(self)
        self.pushbutton_menu.setFocusPolicy(QtCore.Qt.NoFocus)
        self.pushbutton_menu.setMinimumWidth(menu_width)
        self.pushbutton_menu.setStyleSheet('QMenu {color: rgb(154, 154, 154); background-color: rgb(45, 55, 68); border: none; font: 14px "Discreet"}'
                                           'QMenu::item:selected {color: rgb(217, 217, 217); background-color: rgb(58, 69, 81)}')
        for menu in menu_options:
            self.pushbutton_menu.addAction(menu, partial(self.create_menu, menu, menu_action))

        self.setMenu(self.pushbutton_menu)

    def create_menu(self, menu, menu_action):
        self.setText(menu)
        if menu_action:
            menu_action()

    def update_menu(self, button_name: str, menu_options: List[str], menu_action=None):
        from functools import partial

        self.setText(button_name)

        self.pushbutton_menu.clear()

        for menu in menu_options:
            self.pushbutton_menu.addAction(menu, partial(self.create_menu, menu, menu_action))

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
