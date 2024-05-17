# filename: FlamePasswordWindow.py

# -------------------------------------------------------------------------- #

# File Name:        FlamePasswordWindow.py
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

class FlamePasswordWindow(QtWidgets.QDialog):
    '''
    Custom Qt Flame Password Window

    FlamePasswordWindow(window_title, message[, user_name=False, parent=None])

    window_title: text shown in top left of window ie. Confirm Operation [str]
    message: text shown in window [str]
    user_name: if set to true a prompt for a user name will be included [bool]
    parent: (optional) parent window [object]

    Returns password as string

    Examples:

        for system password:

            password = str(FlamePasswordWindow('Enter System Password', 'System password needed to do something.'))

        username and password prompt:

            username, password = iter(FlamePasswordWindow('Login', 'Enter username and password.', user_name=True))
    '''

    def __init__(self, window_title: str, message: str, user_name: Optional[bool]=False, parent=None):
        super(FlamePasswordWindow, self).__init__()

        # Check argument types

        if not isinstance(window_title, str):
            raise TypeError('FlamePasswordWindow: window_title must be a string')
        if not isinstance(message, str):
            raise TypeError('FlamePasswordWindow: message must be a string')
        if not isinstance(user_name, bool):
            raise TypeError('FlamePasswordWindow: user_name must be a boolean')

        self.username = ''
        self.password = ''

        self.setWindowFlags(QtCore.Qt.FramelessWindowHint | QtCore.Qt.WindowStaysOnTopHint)
        self.setMinimumSize(QtCore.QSize(500, 300))
        self.setMaximumSize(QtCore.QSize(500, 230))
        self.setStyleSheet('background-color: rgb(36, 36, 36)')

        primaryScreen = QtWidgets.QApplication.primaryScreen() # resolution = QtWidgets.QDesktopWidget().screenGeometry()
        resolution = primaryScreen.geometry() # Fix for flame 2025
        self.move((resolution.width() / 2) - (self.frameSize().width() / 2),
                  (resolution.height() / 2) - (self.frameSize().height() / 2))

        self.setParent(parent)

        self.main_label = FlameLabel(window_title, label_width=500)
        self.main_label.setStyleSheet('color: rgb(154, 154, 154); font: 18px "Discreet"')

        self.message_label = FlameLabel(message, label_width=480)
        self.message_label.setStyleSheet('QLabel {color: rgb(154, 154, 154); background-color: rgb(36, 36, 36); padding-left: 20px; padding-right: 20px; font: 12px "Discreet"}')

        self.password_label = FlameLabel('Password', label_width=80)

        self.password_entry = FlameLineEdit('', width=300)
        self.password_entry.setEchoMode(QtWidgets.QLineEdit.EchoMode.Password) # Fix for flame 2025

        if user_name:
            self.username_label = FlameLabel('Username', label_width=80)
            self.username_entry = FlameLineEdit('', width=300)
            self.confirm_button = FlameButton('Confirm', self.username_password, button_color='blue', button_width=110)
        else:
            self.confirm_button = FlameButton('Confirm', self.system_password, button_color='blue', button_width=110)

        self.cancel_button = FlameButton('Cancel', self.cancel, button_width=110)

        # UI Widget Layout

        self.grid = QtWidgets.QGridLayout()
        self.grid.addWidget(self.main_label, 0, 0)
        self.grid.setRowMinimumHeight(1, 30)
        self.grid.addWidget(self.message_label, 2, 0)
        self.grid.setRowMinimumHeight(3, 30)

        if user_name:
            self.grid.addWidget(self.username_label, 4, 0)
            self.grid.addWidget(self.username_entry, 4, 1)

        self.grid.addWidget(self.password_label, 5, 0)
        self.grid.addWidget(self.password_entry, 5, 1)
        self.grid.setRowMinimumHeight(9, 60)
        self.grid.addWidget(self.cancel_button, 10, 5)
        self.grid.addWidget(self.confirm_button, 10, 6)
        self.grid.setRowMinimumHeight(11, 30)

        message = message.replace('<br>', '')
        message = message.replace('<center>', '')
        message = message.replace('<dd>', '')

        print(f'\n--> {window_title}: {message}\n')

        self.setLayout(self.grid)
        self.show()
        self.exec_()

    def __str__(self):

        return self.password

    def __iter__(self):

        yield from (self.username, self.password)

    def cancel(self):

        self.login = ''
        self.close()
        print('--> Cancelled.\n')
        return

    def username_password(self):

        if self.password_entry.text() and self.username_entry.text():
            self.close()

            self.username = self.username_entry.text()
            self.password = self.password_entry.text()

            return

    def system_password(self):

        password = self.password_entry.text()

        # Test password - return password if correct

        if password:
            import subprocess

            args = "sudo -S echo OK".split()
            kwargs = dict(stdout=subprocess.PIPE, encoding="ascii")

            kwargs.update(input=password)
            cmd = subprocess.run(args, **kwargs)

            if cmd.stdout:
                print('--> Password Correct\n')
                self.password = password
                self.close()
                return
            else:
                self.message_label.setText('Password incorrect, try again.')
                print('--> Password Incorrect\n')

    def paintEvent(self, event):
        painter = QtGui.QPainter(self)

        painter.setPen(QtGui.QPen(QtGui.QColor(200, 29, 29), 6, QtCore.Qt.SolidLine))
        painter.drawLine(0, 0, 0, 330)

        painter.setPen(QtGui.QPen(QtGui.QColor(71, 71, 71), .5, QtCore.Qt.SolidLine))
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
