'''
# -------------------------------------------------------------------------- #

# File Name:        projekt_qt_stylesheet.py
# Version:          1.0.0
# Language:         python script
# Flame Version:    2025.x
# Author:           Phil MAN - phil_man@mac.com
# Toolset:          MAN_MADE_MATERIAL: LOGIK-PROJEKT
# Created:          2024-04-20
# Modified:         2024-06-07
# Modifier:         Phil MAN - phil_man@mac.com

# Description:      This program is part of LOGIK-PROJEKT.
#                   LOGIK-PROJEKT is a library of custom functions and
#                   modules for autodesk flame.

# Installation:     Copy the 'LOGIK-PROJEKT' repo to your GitHub directory,
#                   e.g. '/home/$USER/workspace/GitHub'

# Changelist:       The full changelist is at the end of this document.

# -------------------------------------------------------------------------- #
'''

# ========================================================================== #
# This section defines the main functions.
# ========================================================================== #

stylesheet = """
/* Set the background color */
QWidget {
    background-color: #242424; /* Replace with your desired color */
}

/* Text color (white) */
QPushButton, QLineEdit, QComboBox {
    color: #ffffff; /* White color */
}

/* Label text color */
QLabel {
    color: #9F9F9F; /* Label color */
}

/* Font (Discreet 14 px) */
QLabel, QPushButton, QLineEdit, QComboBox {
    font: 14px "Discreet"; /* Replace with the actual font name */
}

/* Disabled Button color */
QPushButton:disabled {
    background-color: #4D0000; /* Replace with your desired color */
}

/* Enabled Button Color */
QPushButton {
    background-color: #4D0000; /* Replace with your desired color */
}

/* Lineedit Text Entry Background */
QLineEdit {
    background-color: #37414b; /* Replace with your desired color */
}

/* Dropdown menu */
QComboBox {
    background-color: #2c3644; /* Replace with your desired color */
    border: none; /* Remove border */
    border-radius: 0; /* Remove rounded corners */
    padding: 5px;
}

# /* Remove 3D relief from dropdown arrow */
# QComboBox::drop-down {
#     border: none; /* Remove border */
#     background: none; /* Remove background */
# }

# QComboBox::down-arrow {
#     image: url(your_icon_path/down-arrow.png); /* Replace with your desired icon path */
#     width: 12px; /* Adjust width if necessary */
#     height: 12px; /* Adjust height if necessary */
# }

/* Dropdown menu selection */
QComboBox QAbstractItemView::item:selected {
    background-color: #2c3644; /* Replace with your desired color */
}

/* QComboBox Popup styling */
QComboBox QAbstractItemView {
    border: none; /* Remove border */
    background-color: #2a3341; /* Background color of dropdown items */
}

/* Summary box (QTextEdit) */
QTextEdit {
    background-color: #37414b;  /* Replace with your desired color */
    color: #ffffff;  /* Text color */
    font: 14px "Discreet";  /* Font */
    border: 1px solid #007acc;  /* Border */
    border-radius: 0px;  /* No rounded corners */
}
"""

# ========================================================================== #
# C2 A9 32 30 32 34 2D 4D 41 4E 5F 4D 41 44 45 2D 4D 45 4B 41 4E 49 53 4D 5A #
# ========================================================================== #
'''
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
'''
# -------------------------------------------------------------------------- #
# Changelist:       
# -------------------------------------------------------------------------- #
# version:               1.0.0
# modified:              2024-06-07 - 16:22:45
# comments:              Working program
