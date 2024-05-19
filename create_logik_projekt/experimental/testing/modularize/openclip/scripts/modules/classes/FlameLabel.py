# filename: FlameLabel.py

# -------------------------------------------------------------------------- #

# File Name:        FlameLabel.py
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

class FlameLabel(QtWidgets.QLabel):
    '''
    Custom Qt Flame Label Widget

    FlameLabel(label_name[, label_type='normal', label_width=150])

    label_name: text displayed [str]
    label_type: (optional) select from different styles: normal, underline, background. default is normal [str]
    label_width: (optional) default is 150 [int]

    Example:

        label = FlameLabel('Label Name', label_type='underline', label_width=300)
    '''

    def __init__(self, label_name: str, label_type: Optional[str]='normal', label_width: Optional[int]=150):
        super(FlameLabel, self).__init__()

        # Check argument types

        if not isinstance(label_name, str):
            raise TypeError('FlameLabel: label_name must be a string')
        elif not isinstance(label_type, str):
            raise TypeError('FlameLabel: label_type must be a string')
        elif label_type not in ['normal', 'underline', 'background']:
            raise ValueError('FlameLabel: label_type must be one of: normal, underline, background')
        elif not isinstance(label_width, int):
            raise TypeError('FlameLabel: label_width must be an integer')

        # Build label

        self.setText(label_name)
        self.setMinimumSize(label_width, 28)
        self.setMaximumHeight(28)
        self.setFixedHeight(28)
        self.setFocusPolicy(QtCore.Qt.NoFocus)

        # Set label stylesheet based on label_type

        if label_type == 'normal':
            self.setStyleSheet('QLabel {color: rgb(154, 154, 154); font: 14px "Discreet"}'
                               'QLabel:disabled {color: rgb(106, 106, 106)}')
        elif label_type == 'underline':
            self.setAlignment(QtCore.Qt.AlignCenter)
            self.setStyleSheet('QLabel {color: rgb(154, 154, 154); border-bottom: 1px inset rgb(40, 40, 40); font: 14px "Discreet"}'
                               'QLabel:disabled {color: rgb(106, 106, 106)}')
        elif label_type == 'background':
            self.setStyleSheet('QLabel {color: rgb(154, 154, 154); background-color: rgb(30, 30, 30); padding-left: 5px; font: 14px "Discreet"}'
                               'QLabel:disabled {color: rgb(106, 106, 106)}')

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
