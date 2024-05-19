# filename: FlameClickableLineEdit.py

# -------------------------------------------------------------------------- #

# File Name:        FlameClickableLineEdit.py
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

class FlameClickableLineEdit(QtWidgets.QLineEdit):
    '''
    Custom Qt Flame Clickable Line Edit Widget

    FlameClickableLineEdit(text, connect[, width=150, max_width=2000])

    text: text displayed in line edit [str]
    connect: execute when line edit is clicked on [function]
    width: (optional) width of widget. default is 150. [int]
    max_width: (optional) maximum width of widget. default is 2000 [int]

    Example:

        clickable_lineedit =  FlameClickableLineEdit('Some Text', some_function)
    '''

    clicked = QtCore.Signal()

    def __init__(self, text: str, connect: Callable[..., None], width: Optional[int]=150, max_width: Optional[int]=2000):
        super(FlameClickableLineEdit, self).__init__()

        # Check argument types

        if not isinstance(text, str):
            raise TypeError('FlameClickableLineEdit: text must be a string')
        elif not isinstance(width, int):
            raise TypeError('FlameClickableLineEdit: width must be an integer')
        elif not isinstance(max_width, int):
            raise TypeError('FlameClickableLineEdit: max_width must be an integer')

        # Build line edit

        self.setText(text)
        self.setMinimumHeight(28)
        self.setMinimumWidth(width)
        self.setMaximumWidth(max_width)
        self.setReadOnly(True)
        self.clicked.connect(connect)
        self.setFocusPolicy(QtCore.Qt.NoFocus)
        self.setStyleSheet('QLineEdit {color: rgb(154, 154, 154); background-color: rgb(55, 65, 75); selection-color: rgb(38, 38, 38); selection-background-color: rgb(184, 177, 167); border: 1px solid rgb(55, 65, 75); padding-left: 5px; font: 14px "Discreet"}'
                           'QLineEdit:focus {background-color: rgb(73, 86, 99)}'
                           'QLineEdit:hover {border: 1px solid rgb(90, 90, 90)}'
                           'QLineEdit:disabled {color: rgb(106, 106, 106); background-color: rgb(55, 55, 55); border: 1px solid rgb(55, 55, 55)}'
                           'QToolTip {color: rgb(170, 170, 170); background-color: rgb(71, 71, 71); border: 10px solid rgb(71, 71, 71)}')

    def mousePressEvent(self, event):
        if event.button() == QtCore.Qt.LeftButton:
            self.clicked.emit()
        else:
            super().mousePressEvent(event)

# ========================================================================== #
# This section defines how to handle the main script function.
# ========================================================================== #

# # If this script is executed as main:
# # Call functions for immediate execution
# if __name__ == "__main__":

# ========================================================================== #
# C2 A9 32 30 32 34 2D 4D 41 4E 5F 4D 41 44 45 2D 4D 45 4B 41 4E 49 53 4D 5A #
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
