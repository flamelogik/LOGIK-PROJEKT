# filename: FlameQDialog.py

# -------------------------------------------------------------------------- #

# File Name:        FlameQDialog.py
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

class FlameQDialog(QtWidgets.QDialog):
    '''
    Custom Qt Flame QDialog Widget

    FlameQDialog(window_title, window_layout, window_width, window_height[, window_bar_color]

    window_title: Text shown top left of window [str]
    window_layout: Layout of window [QtWidgets.QLayout]
    window_width: Width of window [int]
    window_height: Height of window [int]
    window_bar_color: (optional) Color of left window bar (Default is blue) [str]

    Example:

        setup_window = FlameQDialog(f'{SCRIPT_NAME}: Setup <small>{VERSION}', gridbox, 1000, 360)
    '''

    def __init__(self, window_title: str, window_layout, window_width: int, window_height: int, window_bar_color: Optional[str]='blue'):
        super(FlameQDialog, self).__init__()

        # Check argument types

        if not isinstance(window_title, str):
            raise TypeError('FlameQDialog: window_title must be a string.')
        elif not isinstance(window_layout, QtWidgets.QLayout):
            raise TypeError('FlameQDialog: window_layout must be a QtWidgets.QLayout.')
        elif not isinstance(window_width, int):
            raise TypeError('FlameQDialog: window_width must be an integer.')
        elif not isinstance(window_height, int):
            raise TypeError('FlameQDialog: window_height must be an integer.')
        elif not isinstance(window_bar_color, str):
            raise TypeError('FlameQDialog: window_bar_color must be a string.')

        # Build window

        self.window_bar_color = window_bar_color
        self.window_width = window_width
        self.window_height = window_height

        self.setWindowFlags(QtCore.Qt.FramelessWindowHint | QtCore.Qt.WindowStaysOnTopHint)
        self.setMinimumSize(QtCore.QSize(window_width, window_height))
        self.setMaximumSize(QtCore.QSize(window_width, window_height))
        self.setStyleSheet('QWidget {background-color: rgb(36, 36, 36)}'
                           'QTabWidget {background-color: rgb(36, 36, 36); border: none; font: 14px "Discreet"}'
                           'QTabWidget::tab-bar {alignment: center}'
                           'QTabBar::tab {color: rgb(154, 154, 154); background-color: rgb(36, 36, 36); min-width: 20ex; padding: 5px;}'
                           'QTabBar::tab:selected {color: rgb(186, 186, 186); background-color: rgb(31, 31, 31); border: 1px solid rgb(31, 31, 31); border-bottom: 1px solid rgb(51, 102, 173)}'
                           'QTabBar::tab:!selected {color: rgb(186, 186, 186); background-color: rgb(36, 36, 36); border: none}'
                           'QTabWidget::pane {border-top: 1px solid rgb(49, 49, 49)}')

        primaryScreen = QtWidgets.QApplication.primaryScreen() # resolution = QtWidgets.QDesktopWidget().screenGeometry()
        resolution = primaryScreen.geometry() # Fix for flame 2025
        self.move((resolution.width() / 2) - (self.frameSize().width() / 2),
                  (resolution.height() / 2) - (self.frameSize().height() / 2))

        self.window_title_label = FlameLabel(window_title, label_width=window_width)
        self.window_title_label.setStyleSheet('color: rgb(154, 154, 154); font: 18px "Discreet"')

        # Layout

        self.grid = QtWidgets.QGridLayout()
        self.grid.addWidget(self.window_title_label, 0, 0)
        self.grid.addLayout(window_layout, 2, 0, 3, 3)
        self.grid.setRowMinimumHeight(3, 100)

        self.setLayout(self.grid)

    def paintEvent(self, event):
        '''
        Add title bar line and side color lines to window
        '''

        # Line colors

        painter = QtGui.QPainter(self)
        if self.window_bar_color == 'blue':
            bar_color = QtGui.QColor(0, 110, 176)
        elif self.window_bar_color == 'red':
            bar_color = QtGui.QColor(200, 29, 29)
        elif self.window_bar_color == 'green':
            bar_color = QtGui.QColor(0, 180, 13)
        elif self.window_bar_color == 'yellow':
            bar_color = QtGui.QColor(251, 181, 73)
        elif self.window_bar_color == 'gray':
            bar_color = QtGui.QColor(71, 71, 71)

        # Draw lines

        painter.setPen(QtGui.QPen(QtGui.QColor(71, 71, 71), .5, QtCore.Qt.SolidLine))
        painter.drawLine(0, 40, self.window_width, 40)
        painter.setPen(QtGui.QPen(bar_color, 6, QtCore.Qt.SolidLine))
        painter.drawLine(0, 0, 0, self.window_height)

    # For moving frameless window

    def mousePressEvent(self, event):
        self.oldPosition = event.globalPos()

    def mouseMoveEvent(self, event):

        try:
            delta = QtCore.QPoint(event.globalPos() - self.oldPosition)
            self.move(self.x() + delta.x(), self.y() + delta.y())
            self.oldPosition = event.globalPos()
        except:
            pass

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
