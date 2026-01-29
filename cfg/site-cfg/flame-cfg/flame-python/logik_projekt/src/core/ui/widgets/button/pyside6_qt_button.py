#

# -------------------------------------------------------------------------- #

# File Name:        pyside6_qt_button.py
# Version:          1.1.1
# Created:          2024-01-19
# Modified:         2025-11-15

# ========================================================================== #
# Setup sys.path
# ========================================================================== #

import os
import sys

# Ensure the parent directory of 'src' is in sys.path
current_file = os.path.abspath(__file__)
# Go up: pyside6_qt_button.py -> classes -> widgets -> ui -> src -> logik_projekt
src_parent = os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(current_file)))))
if src_parent not in sys.path:
    sys.path.insert(0, src_parent)

# ========================================================================== #
# Imports
# ========================================================================== #

from typing import Optional, Callable

try:
    from PySide6 import QtWidgets, QtCore, QtGui
except ImportError:
    from PySide2 import QtWidgets, QtCore, QtGui

# ========================================================================== #
# Class Definition
# ========================================================================== #

class pyside6_qt_button(QtWidgets.QPushButton):
    '''
    Custom Qt Flame Button Widget

    pyside6_qt_button(button_name, connect[, button_color='normal', button_width=150, button_max_width=150])

    button_name: button text [str]
    connect: execute when clicked [function]
    button_color: (optional) normal, blue, red [str]
    button_width: (optional) default is 150 [int]
    button_max_width: (optional) default is 150 [int]

    Example:

        button = pyside6_qt_button('Button Name', do_something_magical_when_pressed, button_color='blue')
    '''

    def __init__(self, button_name: str, connect: Callable[..., None], button_color: Optional[str]='normal', button_width: Optional[int]=150, button_max_width: Optional[int]=150) -> None:
        super(pyside6_qt_button, self).__init__()

        # Check argument types

        if not isinstance(button_name, str):
            raise TypeError('pyside6_qt_button: button_name must be a string')
        elif button_color not in ['normal', 'blue', 'red']:
            raise ValueError('pyside6_qt_button: button_color must be one of: normal(grey), blue, or red')
        elif not isinstance(button_width, int):
            raise TypeError('pyside6_qt_button: button_width must be an integer')
        elif not isinstance(button_max_width, int):
            raise TypeError('pyside6_qt_button: button_max_width must be an integer')

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

# -------------------------------------------------------------------------- #
# Changelist
# -------------------------------------------------------------------------- #

# version:               1.1.1
# modified:              2025-11-15
# comments:              Added sys.path setup for Flame compatibility
# -------------------------------------------------------------------------- #