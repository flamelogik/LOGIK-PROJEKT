# filename: FlameWindow.py

# -------------------------------------------------------------------------- #

# File Name:        FlameWindow.py
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

class FlameWindow(QtWidgets.QWidget):
    '''
    Custom Qt Flame Window Widget

    FlameWindow(window_title, window_layout, window_width, window_height[, window_bar_color='blue'])

    window_title: text displayed in top left corner of window [str]
    window_layout: QLayout object. QLayout should be defined before adding FlameWindow [object]
    window_width: width of window [int]
    window_height: height of window [int]
    window_bar_color: (optional) color of bar on left side of window. options are red, blue, green, yellow, gray, teal. [str] - default is blue

    Usage:

        grid_layout = QtWidgets.QGridLayout()
        self.window = FlameWindow(f'Import Camera <small>{VERSION}', grid_layout, 400, 200)
    '''

    def __init__(self, window_title: str, window_layout, window_width: int, window_height: int, window_bar_color: Optional[str]='blue'):
        super(FlameWindow, self).__init__()

        # Check argument types

        if not isinstance(window_title, str):
            raise TypeError('FlameWindow: Window Title must be a string.')
        if not isinstance(window_width, int):
            raise TypeError('FlameWindow: Window Width must be a string.')
        if not isinstance(window_height, int):
            raise TypeError('FlameWindow: Window Width must be a string.')
        if window_bar_color not in ['blue', 'red', 'green', 'yellow', 'gray', 'teal']:
           raise ValueError('FlameWindow: Window Bar Color must be one of: blue, red, green, yellow, gray, teal.')

        # Build window

        self.window_bar_color = window_bar_color

        self.window_width = window_width
        self.window_height = window_height
        self.setMinimumSize(QtCore.QSize(window_width, window_height))
        self.setMaximumSize(QtCore.QSize(window_width, window_height))
        self.setWindowFlags(QtCore.Qt.FramelessWindowHint | QtCore.Qt.WindowStaysOnTopHint)
        self.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.setAttribute(QtCore.Qt.WA_DeleteOnClose)
        self.setStyleSheet('QWidget {background-color: rgb(36, 36, 36)}'
                           'QTabWidget {background-color: rgb(36, 36, 36); border: none; font: 14px "Discreet"}'
                           'QTabWidget::tab-bar {alignment: center}'
                           'QTabBar::tab {color: rgb(154, 154, 154); background-color: rgb(36, 36, 36); min-width: 20ex; padding: 5px;}'
                           'QTabBar::tab:selected {color: rgb(186, 186, 186); background-color: rgb(31, 31, 31); border: 1px solid rgb(31, 31, 31); border-bottom: 1px solid rgb(51, 102, 173)}'
                           'QTabBar::tab:!selected {color: rgb(186, 186, 186); background-color: rgb(36, 36, 36); border: none}'
                           'QTabWidget::pane {border-top: 1px solid rgb(49, 49, 49)}')

        # Center window in linux

        primaryScreen = QtWidgets.QApplication.primaryScreen() # resolution = QtWidgets.QDesktopWidget().screenGeometry()
        resolution = primaryScreen.geometry() # Fix for flame 2025
        self.move((resolution.width() / 2) - (self.frameSize().width() / 2),
                  (resolution.height() / 2) - (self.frameSize().height() / 2))

        self.title_label = FlameLabel(window_title, label_width=window_width)
        self.title_label.setStyleSheet('color: rgb(154, 154, 154); font: 18px "Discreet"')

        # Layout

        self.grid = QtWidgets.QGridLayout()
        self.grid.addWidget(self.title_label, 0, 0)
        self.grid.addLayout(window_layout, 2, 0, 3, 3)
        self.grid.setRowMinimumHeight(3, 100)

        self.setLayout(self.grid)

    def paintEvent(self, event):

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
        elif self.window_bar_color == 'teal':
            bar_color = QtGui.QColor(14, 110, 106)

        painter.setPen(QtGui.QPen(QtGui.QColor(71, 71, 71), .5, QtCore.Qt.SolidLine))
        painter.drawLine(0, 40, self.window_width, 40)
        painter.setPen(QtGui.QPen(bar_color, 6, QtCore.Qt.SolidLine))
        painter.drawLine(0, 0, 0, self.window_height)

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
