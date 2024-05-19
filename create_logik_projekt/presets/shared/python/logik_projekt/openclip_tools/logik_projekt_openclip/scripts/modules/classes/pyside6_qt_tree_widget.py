# filename: pyside6_qt_tree_widget.py

# -------------------------------------------------------------------------- #

# File Name:        pyside6_qt_tree_widget.py
# Version:          0.4.3
# Language:         python script
# Flame Version:    2025.x
# Author:           Phil MAN - phil_man@mac.com
# Toolset:          MAN_MADE_MATERIAL: LOGIK-PROJEKT
# Created:          2024-04-20
# Modified:         2024-05-18
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

class pyside6_qt_tree_widget(QtWidgets.QTreeWidget):
    '''
    Custom Qt Flame Tree Widget

    pyside6_qt_tree_widget(tree_headers[, connect=None, tree_min_width=100, tree_min_height=100])

    tree_headers: list of names to be used for column names in tree [list]
    connect: execute when item in tree is clicked on [function]
    tree_min_width = set tree width [int]
    tree_min_height = set tree height [int]

    Exmaple:

        tree_headers = ['Header1', 'Header2', 'Header3', 'Header4']
        tree = pyside6_qt_tree_widget(tree_headers)
    '''

    def __init__(self, tree_headers: List[str], connect: Optional[Callable[..., None]]=None, tree_min_width: Optional[int]=100, tree_min_height: Optional[int]=100):
        super(pyside6_qt_tree_widget, self).__init__()

        # Check argument types

        if not isinstance(tree_headers, list):
            raise TypeError('pyside6_qt_tree_widget: tree_headers must be a list')
        if not isinstance(tree_min_width, int):
            raise TypeError('pyside6_qt_tree_widget: tree_min_width must be an integer')
        if not isinstance(tree_min_height, int):
            raise TypeError('pyside6_qt_tree_widget: tree_min_height must be an integer')

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
# modified:              2024-05-17 - 13:36:43
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
# modified:              2024-05-17 - 13:44:31
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
# modified:              2024-05-17 - 13:50:11
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
# modified:              2024-05-17 - 15:16:42
# comments:              Replaced pyside6_qt_textedit with pyside6_qt_text_edit
# -------------------------------------------------------------------------- #
# version:               0.3.3
# modified:              2024-05-17 - 15:48:01
# comments:              Replaced pyside6_qt_push_buttonMenu with pyside6_qt_push_button_menu
# -------------------------------------------------------------------------- #
# version:               0.4.3
# modified:              2024-05-18 - 18:00:39
# comments:              Added GNU GPLv3 Disclaimer.
