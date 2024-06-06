# filename: pyside6_qt_password_window.py

'''
# -------------------------------------------------------------------------- #

# File Name:        pyside6_qt_password_window.py
# Version:          0.4.6
# Language:         python script
# Flame Version:    2025.x
# Author:           Phil MAN - phil_man@mac.com
# Toolset:          MAN_MADE_MATERIAL: LOGIK-PROJEKT
# Created:          2024-04-20
# Modified:         2024-06-05
# Modifier:         Phil MAN - phil_man@mac.com

# Description:      This program is part of a library of custom functions
#                   and modules for autodesk flame.

# Installation:     Copy the 'LOGIK-PROJEKT' repo to your GitHub directory,
#                   e.g. '/home/$USER/workspace/GitHub'

# Attribution:      This script is derived from work originally authored by
#                   Michael Vaglienty: 'pyflame_lib_script_template.py'

# Changelist:       The full changelist is at the end of this document.

# -------------------------------------------------------------------------- #
'''

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

class pyside6_qt_password_window(QtWidgets.QDialog):
    '''
    Custom Qt Flame Password Window

    pyside6_qt_password_window(window_title, message[, user_name=False, parent=None])

    window_title: text shown in top left of window ie. Confirm Operation [str]
    message: text shown in window [str]
    user_name: if set to true a prompt for a user name will be included [bool]
    parent: (optional) parent window [object]

    Returns password as string

    Examples:

        for system password:

            password = str(pyside6_qt_password_window('Enter System Password', 'System password needed to do something.'))

        username and password prompt:

            username, password = iter(pyside6_qt_password_window('Login', 'Enter username and password.', user_name=True))
    '''

    def __init__(self, window_title: str, message: str, user_name: Optional[bool]=False, parent=None):
        super(pyside6_qt_password_window, self).__init__()

        # Check argument types

        if not isinstance(window_title, str):
            raise TypeError('pyside6_qt_password_window: window_title must be a string')
        if not isinstance(message, str):
            raise TypeError('pyside6_qt_password_window: message must be a string')
        if not isinstance(user_name, bool):
            raise TypeError('pyside6_qt_password_window: user_name must be a boolean')

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

        self.main_label = pyside6_qt_label(window_title, label_width=500)
        self.main_label.setStyleSheet('color: rgb(154, 154, 154); font: 18px "Discreet"')

        self.message_label = pyside6_qt_label(message, label_width=480)
        self.message_label.setStyleSheet('QLabel {color: rgb(154, 154, 154); background-color: rgb(36, 36, 36); padding-left: 20px; padding-right: 20px; font: 12px "Discreet"}')

        self.password_label = pyside6_qt_label('Password', label_width=80)

        self.password_entry = pyside6_qt_line_edit('', width=300)
        self.password_entry.setEchoMode(QtWidgets.QLineEdit.EchoMode.Password) # Fix for flame 2025

        if user_name:
            self.username_label = pyside6_qt_label('Username', label_width=80)
            self.username_entry = pyside6_qt_line_edit('', width=300)
            self.confirm_button = pyside6_qt_button('Confirm', self.username_password, button_color='blue', button_width=110)
        else:
            self.confirm_button = pyside6_qt_button('Confirm', self.system_password, button_color='blue', button_width=110)

        self.cancel_button = pyside6_qt_button('Cancel', self.cancel, button_width=110)

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
# C2 A9 32 30 32 34 2D 4D 41 4E 5F 4D 41 44 45 2D 4D 45 4B 41 4E 49 53 4D 5A #
# ========================================================================== #

# -------------------------------------------------------------------------- #

# Disclaimer:       This program is part of LOGIK-PROJEKT.
#                   LOGIK-PROJEKT is free software.

#                   You can redistribute it and/or modify it under the terms
#                   of the GNU General Public License as published by the
#                   Free Software Foundation, either version 3 of the License,
#                   or any later version.

#                   This program is distributed in the hope that it will be
#                   useful, but WITHOUT ANY WARRANTY; without even the
#                   implied warranty of MERCHANTABILITY or FITNESS FOR A
#                   PARTICULAR PURPOSE.

#                   See the GNU General Public License for more details.

#                   You should have received a copy of the GNU General
#                   Public License along with this program.

#                   If not, see <https://www.gnu.org/licenses/>.

# -------------------------------------------------------------------------- #
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
# -------------------------------------------------------------------------- #
# version:               0.0.5
# modified:              2024-05-17 - 13:36:42
# comments:              Replaced FlameButton with pyside6_qt_button
# -------------------------------------------------------------------------- #
# version:               0.0.6
# modified:              2024-05-17 - 13:37:49
# comments:              Replaced FlameClickableLineEdit with pyside6_qt_clickable_line_edit
# -------------------------------------------------------------------------- #
# version:               0.0.7
# modified:              2024-05-17 - 13:38:19
# comments:              Replaced FlameLabel with pyside6_qt_label
# -------------------------------------------------------------------------- #
# version:               0.0.8
# modified:              2024-05-17 - 13:38:29
# comments:              Replaced FlameLineEdit with pyside6_qt_line_edit
# -------------------------------------------------------------------------- #
# version:               0.0.9
# modified:              2024-05-17 - 13:39:27
# comments:              Replaced FlameListWidget with pyside6_qt_list_widget
# -------------------------------------------------------------------------- #
# version:               0.1.0
# modified:              2024-05-17 - 13:39:47
# comments:              Replaced FlameMessageWindow with pyside6_qt_message_window
# -------------------------------------------------------------------------- #
# version:               0.1.1
# modified:              2024-05-17 - 13:40:01
# comments:              Replaced FlamePasswordWindow with pyside6_qt_password_window
# -------------------------------------------------------------------------- #
# version:               0.1.2
# modified:              2024-05-17 - 13:40:28
# comments:              Replaced FlamePresetWindow with pyside6_qt_preset_window
# -------------------------------------------------------------------------- #
# version:               0.1.3
# modified:              2024-05-17 - 13:40:37
# comments:              Replaced FlameProgressWindow with pyside6_qt_progress_window
# -------------------------------------------------------------------------- #
# version:               0.1.4
# modified:              2024-05-17 - 13:41:39
# comments:              Replaced FlamePushButton with pyside6_qt_push_button
# -------------------------------------------------------------------------- #
# version:               0.1.5
# modified:              2024-05-17 - 13:41:49
# comments:              Replaced FlamePushButtonMenu with pyside6_qt_push_button_menu
# -------------------------------------------------------------------------- #
# version:               0.1.6
# modified:              2024-05-17 - 13:42:30
# comments:              Replaced FlameQDialog with pyside6_qt_qdialog
# -------------------------------------------------------------------------- #
# version:               0.1.7
# modified:              2024-05-17 - 13:44:20
# comments:              Replaced FlameSlider with pyside6_qt_slider
# -------------------------------------------------------------------------- #
# version:               0.1.8
# modified:              2024-05-17 - 13:44:30
# comments:              Replaced FlameTextEdit with pyside6_qt_text_edit
# -------------------------------------------------------------------------- #
# version:               0.1.9
# modified:              2024-05-17 - 13:44:39
# comments:              Replaced FlameTokenPushButton with pyside6_qt_token_push_button
# -------------------------------------------------------------------------- #
# version:               0.2.0
# modified:              2024-05-17 - 13:45:12
# comments:              Replaced FlameTreeWidget with pyside6_qt_tree_widget
# -------------------------------------------------------------------------- #
# version:               0.2.1
# modified:              2024-05-17 - 13:45:29
# comments:              Replaced FlameWindow with pyside6_qt_window
# -------------------------------------------------------------------------- #
# version:               0.2.2
# modified:              2024-05-17 - 13:45:43
# comments:              Replaced pyflame_file_browser with pyside6_qt_file_browser
# -------------------------------------------------------------------------- #
# version:               0.2.3
# modified:              2024-05-17 - 13:47:07
# comments:              Replaced pyflame_get_flame_version with pyside6_qt_get_flame_version
# -------------------------------------------------------------------------- #
# version:               0.2.4
# modified:              2024-05-17 - 13:47:43
# comments:              Replaced pyflame_get_shot_name with pyside6_qt_get_shot_name
# -------------------------------------------------------------------------- #
# version:               0.2.5
# modified:              2024-05-17 - 13:47:56
# comments:              Replaced pyflame_load_config with pyside6_qt_load_config
# -------------------------------------------------------------------------- #
# version:               0.2.6
# modified:              2024-05-17 - 13:49:42
# comments:              Replaced pyflame_open_in_finder with pyside6_qt_open_in_finder
# -------------------------------------------------------------------------- #
# version:               0.2.7
# modified:              2024-05-17 - 13:49:51
# comments:              Replaced pyflame_print with pyside6_qt_print
# -------------------------------------------------------------------------- #
# version:               0.2.8
# modified:              2024-05-17 - 13:50:00
# comments:              Replaced pyflame_refresh_hooks with pyside6_qt_refresh_hooks
# -------------------------------------------------------------------------- #
# version:               0.2.9
# modified:              2024-05-17 - 13:50:10
# comments:              Replaced pyflame_resolve_path_tokens with pyside6_qt_resolve_path_tokens
# -------------------------------------------------------------------------- #
# version:               0.3.0
# modified:              2024-05-17 - 13:50:21
# comments:              Replaced pyflame_resolve_shot_name with pyside6_qt_resolve_shot_name
# -------------------------------------------------------------------------- #
# version:               0.3.1
# modified:              2024-05-17 - 13:50:32
# comments:              Replaced pyflame_save_config with pyside6_qt_save_config
# -------------------------------------------------------------------------- #
# version:               0.3.2
# modified:              2024-05-17 - 15:16:41
# comments:              Replaced pyside6_qt_textedit with pyside6_qt_text_edit
# -------------------------------------------------------------------------- #
# version:               0.3.3
# modified:              2024-05-17 - 15:48:01
# comments:              Replaced pyside6_qt_push_buttonMenu with pyside6_qt_push_button_menu
# -------------------------------------------------------------------------- #
# version:               0.4.3
# modified:              2024-05-18 - 18:00:39
# comments:              Added GNU GPLv3 Disclaimer.
# -------------------------------------------------------------------------- #
# version:               0.4.4
# modified:              2024-05-18 - 18:46:09
# comments:              Minor modification to Disclaimer.
# -------------------------------------------------------------------------- #
# version:               0.4.5
# modified:              2024-06-04 - 17:38:52
# comments:              Added 'Smart Replace' option for render and write nodes
# -------------------------------------------------------------------------- #
# version:               0.4.6
# modified:              2024-06-05 - 19:30:33
# comments:              Added a new script to create openclip multichannel
