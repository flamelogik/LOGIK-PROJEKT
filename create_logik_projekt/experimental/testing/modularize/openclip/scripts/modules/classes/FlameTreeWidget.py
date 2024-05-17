# filename: FlameTreeWidget.py

# -------------------------------------------------------------------------- #

# File Name:        FlameTreeWidget.py
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

class FlameTreeWidget(QtWidgets.QTreeWidget):
    '''
    Custom Qt Flame Tree Widget

    FlameTreeWidget(tree_headers[, connect=None, tree_min_width=100, tree_min_height=100])

    tree_headers: list of names to be used for column names in tree [list]
    connect: execute when item in tree is clicked on [function]
    tree_min_width = set tree width [int]
    tree_min_height = set tree height [int]

    Exmaple:

        tree_headers = ['Header1', 'Header2', 'Header3', 'Header4']
        tree = FlameTreeWidget(tree_headers)
    '''

    def __init__(self, tree_headers: List[str], connect: Optional[Callable[..., None]]=None, tree_min_width: Optional[int]=100, tree_min_height: Optional[int]=100):
        super(FlameTreeWidget, self).__init__()

        # Check argument types

        if not isinstance(tree_headers, list):
            raise TypeError('FlameTreeWidget: tree_headers must be a list')
        if not isinstance(tree_min_width, int):
            raise TypeError('FlameTreeWidget: tree_min_width must be an integer')
        if not isinstance(tree_min_height, int):
            raise TypeError('FlameTreeWidget: tree_min_height must be an integer')

        # Build tree widget

        self.setMinimumWidth(tree_min_width)
        self.setMinimumHeight(tree_min_height)
        self.setSortingEnabled(True)
        self.sortByColumn(0, QtCore.Qt.SortOrder.AscendingOrder) # Fix for flame 2025
        self.setAlternatingRowColors(True)
        self.setFocusPolicy(QtCore.Qt.NoFocus)
        self.clicked.connect(connect)
        self.setStyleSheet('QTreeWidget {color: rgb(154, 154, 154); background-color: rgb(30, 30, 30); alternate-background-color: rgb(36, 36, 36); border: none; font: 14pt "Discreet"}'
                           'QHeaderView::section {color: rgb(154, 154, 154); background-color: rgb(57, 57, 57); border: none; padding-left: 10px; font: 14pt "Discreet"}'
                           'QTreeWidget:item:selected {color: rgb(217, 217, 217); background-color: rgb(71, 71, 71); selection-background-color: rgb(153, 153, 153); border: 1px solid rgb(17, 17, 17)}'
                           'QTreeWidget:item:selected:active {color: rgb(153, 153, 153); border: none}'
                           'QTreeWidget:disabled {color: rgb(101, 101, 101); background-color: rgb(34, 34, 34)}'
                           'QMenu {color: rgb(154, 154, 154); background-color: rgb(36, 48, 61); font: 14pt "Discreet"}'
                           'QMenu::item:selected {color: rgb(217, 217, 217); background-color: rgb(58, 69, 81)}'
                           'QScrollBar {color: rgb(17, 17, 17); background: rgb(49, 49, 49)}'
                           'QScrollBar::handle {color: rgb(17, 17, 17)}'
                           'QScrollBar::add-line:vertical {border: none; background: none; width: 0px; height: 0px}'
                           'QScrollBar::sub-line:vertical {border: none; background: none; width: 0px; height: 0px}'
                           'QScrollBar {color: rgb(17, 17, 17); background: rgb(49, 49, 49)}'
                           'QScrollBar::handle {color: rgb(17, 17, 17)}'
                           'QScrollBar::add-line:horizontal {border: none; background: none; width: 0px; height: 0px}'
                           'QScrollBar::sub-line:horizontal {border: none; background: none; width: 0px; height: 0px}')

        self.setHeaderLabels(tree_headers)

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
