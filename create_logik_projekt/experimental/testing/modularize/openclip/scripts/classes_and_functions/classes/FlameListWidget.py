# filename: FlameListWidget.py

# -------------------------------------------------------------------------- #

# File Name:        FlameListWidget.py
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

class FlameListWidget(QtWidgets.QListWidget):
    '''
    Custom Qt Flame List Widget

    FlameListWidget([min_width=200, max_width=2000, min_height=250, max_height=2000])

    Example:

        list_widget = FlameListWidget()
    '''

    def __init__(self, min_width: Optional[int]=200, max_width: Optional[int]=2000, min_height: Optional[int]=250, max_height: Optional[int]=2000):
        super(FlameListWidget, self).__init__()

        # Check argument types

        if not isinstance(min_width, int):
            raise TypeError('FlameListWidget: min_width must be integer.')
        if not isinstance(max_width, int):
            raise TypeError('FlameListWidget: max_width must be integer.')
        if not isinstance(min_height, int):
            raise TypeError('FlameListWidget: min_height must be integer.')
        if not isinstance(max_height, int):
            raise TypeError('FlameListWidget: max_height must be integer.')

        # Build list widget

        self.setMinimumWidth(min_width)
        self.setMaximumWidth(max_width)
        self.setMinimumHeight(min_height)
        self.setMaximumHeight(max_height)
        self.spacing()
        self.setUniformItemSizes(True)
        self.setFocusPolicy(QtCore.Qt.NoFocus)
        self.setSelectionMode(QtWidgets.QAbstractItemView.SelectionMode.ExtendedSelection) # Fix for flame 2025
        self.setAlternatingRowColors(True)
        self.setStyleSheet('QListWidget {color: rgb(154, 154, 154); background-color: rgb(30, 30, 30); alternate-background-color: rgb(36, 36, 36); outline: 3px rgb(0, 0, 0); font: 14px "Discreet"}'
                           'QListWidget::item:selected {color: rgb(217, 217, 217); background-color: rgb(102, 102, 102); border: 1px solid rgb(102, 102, 102)}'
                           'QScrollBar {background: rgb(61, 61, 61)}'
                           'QScrollBar::handle {background: rgb(31, 31, 31)}'
                           'QScrollBar::add-line:vertical {border: none; background: none; width: 0px; height: 0px}'
                           'QScrollBar::sub-line:vertical {border: none; background: none; width: 0px; height: 0px}'
                           'QScrollBar {background: rgb(61, 61, 61)}'
                           'QScrollBar::handle {background: rgb(31, 31, 31)}'
                           'QScrollBar::add-line:horizontal {border: none; background: none; width: 0px; height: 0px}'
                           'QScrollBar::sub-line:horizontal {border: none; background: none; width: 0px; height: 0px}'
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
