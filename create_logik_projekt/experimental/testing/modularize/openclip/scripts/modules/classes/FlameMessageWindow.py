# filename: FlameMessageWindow.py

# -------------------------------------------------------------------------- #

# File Name:        FlameMessageWindow.py
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

class FlameMessageWindow(QtWidgets.QDialog):
    '''
    Custom Qt Flame Message Window

    FlameMessageWindow(message_type, message_title, message[, time=3, parent=None])

    message_type: Type of message window to be shown. Options are: confirm, message, error, warning [str] Confirm and warning return True or False values
    message_title: Text shown in top left of window ie. Confirm Operation [str]
    message: Text displayed in body of window [str]
    time: (optional) Time in seconds to display message in flame message area. Default is 3. [int]
    parent: (optional) - Parent window [QtWidget]

    Message Window Types:

        confirm: confirm and cancel button / grey left bar - returns True or False
        message: ok button / blue left bar
        error: ok button / yellow left bar
        warning: confirm and cancel button / red left bar - returns True of False

    Examples:

        FlameMessageWindow('error', f'{SCRIPT_NAME}: Error', f'Unable to create folder.<br>Check folder permissions')

        or

        if FlameMessageWindow('confirm', 'Confirm Operation', 'Some important message'):
            do something
    '''

    def __init__(self, message_type: str, message_title: str, message: str, time: int=3, parent=None):
        super(FlameMessageWindow, self).__init__()
        import flame

        # Check argument types

        if message_type not in ['confirm', 'message', 'error', 'warning']:
            raise ValueError('FlameMessageWindow: message_type must be one of: confirm, message, error, warning.')
        if not isinstance(message_title, str):
            raise TypeError('FlameMessageWindow: message_title must be a string.')
        if not isinstance(message, str):
            raise TypeError('FlameMessageWindow: message must be a string.')
        if not isinstance(time, int):
            raise TypeError('FlameMessageWindow: time must be an integer.')

        # Create message window

        self.message_type = message_type

        self.setWindowFlags(QtCore.Qt.FramelessWindowHint | QtCore.Qt.WindowStaysOnTopHint)
        self.setMinimumSize(QtCore.QSize(500, 330))
        self.setMaximumSize(QtCore.QSize(500, 330))
        self.setStyleSheet('background-color: rgb(36, 36, 36)')

        primaryScreen = QtWidgets.QApplication.primaryScreen() # resolution = QtWidgets.QDesktopWidget().screenGeometry()
        resolution = primaryScreen.geometry() # Fix for flame 2025
        self.move((resolution.width() / 2) - (self.frameSize().width() / 2),
                  (resolution.height() / 2) - (self.frameSize().height() / 2))

        self.setParent(parent)

        self.grid = QtWidgets.QGridLayout()

        self.main_label = FlameLabel(message_title, label_width=500)
        self.main_label.setStyleSheet('color: rgb(154, 154, 154); font: 18px "Discreet"')

        self.message_text_edit = QtWidgets.QPlainTextEdit(message) # Fix for flame 2025
        self.message_text_edit.setDisabled(True)
        self.message_text_edit.setStyleSheet('QPlainTextEdit {color: rgb(154, 154, 154); background-color: rgb(36, 36, 36); selection-color: rgb(190, 190, 190); selection-background-color: rgb(36, 36, 36); border: none; padding-left: 20px; padding-right: 20px; font: 12px "Discreet"}')  # Fix for flame 2025

        # Set confirm/ok button color

        if message_type == 'confirm':
            self.confirm_button = FlameButton('Confirm', self.confirm, button_color='blue', button_width=110)
        elif message_type == 'warning':
            self.confirm_button = FlameButton('Confirm', self.confirm, button_color='red', button_width=110)
        else:
            self.ok_button = FlameButton('Ok', self.confirm, button_color='blue', button_width=110)

        # Set layout for message window

        if message_type == 'confirm' or message_type == 'warning':
            self.cancel_button = FlameButton('Cancel', self.cancel, button_width=110)
            self.grid.addWidget(self.main_label, 0, 0)
            self.grid.setRowMinimumHeight(1, 30)
            self.grid.addWidget(self.message_text_edit, 2, 0, 4, 8)
            self.grid.setRowMinimumHeight(9, 30)
            self.grid.addWidget(self.cancel_button, 10, 5)
            self.grid.addWidget(self.confirm_button, 10, 6)
            self.grid.setRowMinimumHeight(11, 30)
        else:
            self.grid.addWidget(self.main_label, 0, 0)
            self.grid.setRowMinimumHeight(1, 30)
            self.grid.addWidget(self.message_text_edit, 2, 0, 4, 8)
            self.grid.setRowMinimumHeight(9, 30)
            self.grid.addWidget(self.ok_button, 10, 6)
            self.grid.setRowMinimumHeight(11, 30)

        message = message.replace('<br>', ' ')
        message = message.replace('<center>', '')
        message = message.replace('</center>', '')
        message = message.replace('<dd>', '')
        message = message.replace('<b>', '')
        message = message.replace('</b>', '')

        # Print to terminal/shell

        if message_type == 'warning':
            # print message text in red
            print(f'\033[91m\n--> {message_title}: {message}\033[0m\n')
        elif message_type == 'error':
            # print message text in yellow
            print(f'\033[93m\n--> {message_title}: {message}\033[0m\n')
        else:
            print(f'\n--> {message_title}: {message}\n')

        # Print message to Flame message window - only works in Flame 2023.1 and later
        # Warning and error intentionally swapped to match color of message window

        message_title = message_title.upper()

        try:
            if message_type == 'confirm' or message_type == 'message':
                flame.messages.show_in_console(f'{message_title}: {message}', 'info', time)
            elif message_type == 'error':
                flame.messages.show_in_console(f'{message_title}: {message}', 'warning', time)
            elif message_type == 'warning':
                flame.messages.show_in_console(f'{message_title}: {message}', 'error', time)
        except:
            pass

        self.setLayout(self.grid)
        self.exec()

    def __bool__(self):

        return self.confirmed

    def cancel(self):

        self.close()
        self.confirmed = False
        print('--> Cancelled\n')

    def confirm(self):

        self.close()
        self.confirmed = True
        if self.message_type == 'confirm':
            print('--> Confirmed\n')

    def paintEvent(self, event):
        painter = QtGui.QPainter(self)

        if self.message_type == 'confirm':
            line_color = QtGui.QColor(71, 71, 71)
        elif self.message_type == 'message':
            line_color = QtGui.QColor(0, 110, 176)
        elif self.message_type == 'error':
            line_color = QtGui.QColor(251, 181, 73)
        elif self.message_type == 'warning':
            line_color = QtGui.QColor(200, 29, 29)

        painter.setPen(QtGui.QPen(line_color, 6, QtGui.Qt.SolidLine)) # Fix for flame 2025
        painter.drawLine(0, 0, 0, 330)

        painter.setPen(QtGui.QPen(QtGui.QColor(71, 71, 71), .5, QtGui.Qt.SolidLine)) # Fix for flame 2025
        painter.drawLine(0, 40, 500, 40)

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
