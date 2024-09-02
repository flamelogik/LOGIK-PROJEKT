#

# -------------------------------------------------------------------------- #

# DISCLAIMER:       This file is part of LOGIK-PROJEKT.
#                   Copyright © 2024 man-made-mekanyzms
                
#                   LOGIK-PROJEKT creates directories, files, scripts & tools
#                   for use with Autodesk Flame and other software.

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
                
#                   Contact: phil_man@mac.com

# -------------------------------------------------------------------------- #

# File Name:        projekt_style_sheet.py
# Version:          0.9.9
# Created:          2024-01-19
# Modified:         2024-08-31

# ========================================================================== #
# This section defines the stylesheet for the main application.
# ========================================================================== #

# Default stylesheet
ProjektStyleSheet = """
/* Set the background color */
QWidget {
    background-color: #242424; /* Replace with your desired color */
}

/* Text color (white) */
QPushButton, QLineEdit, QComboBox {
    color: #ffffff; /* White color */
    font: 14px "Discreet Bold"; /* Replace with the actual font name */
}

/* Label text color */
QLabel {
    color: #9F9F9F; /* Label color */
}

/* Font (Discreet 14 px) */
QLabel, QPushButton, QLineEdit, QComboBox {
    font: 14px "Discreet"; /* Replace with the actual font name */
}

/* Summary box (QTextEdit) */
QTextEdit {
    background-color: #37414b;  /* Replace with your desired color */
    color: #ffffff;  /* Text color */
    font: 14px "Discreet";  /* Font */
    border: 1px solid #007acc;  /* Border */
    border-radius: 0px;  /* No rounded corners */
}

/* Disabled Button color */
QPushButton:disabled {
    background-color: #4D0000; /* Red: #4D0000, Amber: #7F3F00, Green: #2F5F00 */
}

/* Enabled Button Color */
QPushButton {
    background-color: #2F5F00; /* Replace with your desired color */
}

/* Lineedit Text Entry Background */
QLineEdit {
    background-color: #37414b; /* Replace with your desired color */
    padding: 4px;
}

/* Dropdown menu */
QComboBox {
    background-color: #2c3644; /* Replace with your desired color */
    border: none; /* Remove border */
    border-radius: 0; /* Remove rounded corners */
    padding: 5px;
}

/* Dropdown menu selection */
QComboBox QAbstractItemView::item:selected {
    background-color: #2c3644; /* Replace with your desired color */
}

/* QComboBox Popup styling */
QComboBox QAbstractItemView {
    border: none; /* Remove border */
    background-color: #2a3341; /* Background color of dropdown items */
}

/* Reset QFileDialog to default values */
QFileDialog {
    background-color: #2E2E2E; /* Dark grey background */
    color: #CCCCCC; /* Light grey text */
}

QFileDialog QFrame {
    background-color: #2E2E2E;
    border: 1px solid #444444; /* Slightly lighter grey border */
}

QFileDialog QLabel {
    color: #CCCCCC;
}

QFileDialog QPushButton {
    background-color: #3A3A3A; /* Slightly lighter grey for buttons */
    color: #CCCCCC;
    border: 1px solid #444444;
    padding: 5px;
}

QFileDialog QPushButton:hover {
    background-color: #4A4A4A; /* Slightly lighter on hover */
}

QFileDialog QLineEdit {
    background-color: #3A3A3A;
    color: #CCCCCC;
    border: 1px solid #444444;
}

QFileDialog QListView, QFileDialog QTreeView {
    background-color: #2E2E2E;
    color: #CCCCCC;
    border: 1px solid #444444;
}

QFileDialog QComboBox {
    background-color: #3A3A3A;
    color: #CCCCCC;
    border: 1px solid #444444;
}

QFileDialog QToolButton {
    background-color: #3A3A3A;
    color: #CCCCCC;
    border: 1px solid #444444;
}
"""

# Stylesheet for Button Color 1
ButtonColor1StyleSheet = """
QPushButton {
    background-color: #4D0000; /* Red */
}
"""

# Stylesheet for Button Color 2
ButtonColor2StyleSheet = """
QPushButton {
    background-color: #6F2F00; /* Amber #7F3F00 */
}
"""

# Stylesheet for Button Color 3
ButtonColor3StyleSheet = """
QPushButton {
    background-color: #1F4F00; /* Green #2F5F00 */
}
"""

def apply_stylesheet(app, stylesheet):
    app.setStyleSheet(stylesheet)

# ========================================================================== #
# C2 A9 32 30 32 34 2D 4D 41 4E 2D 4D 41 44 45 2D 4D 45 4B 41 4E 59 5A 4D 53 #
# ========================================================================== #

# Changelist:       

# -------------------------------------------------------------------------- #
# version:          0.0.1
# created:          2024-01-19 - 12:34:56
# comments:         scripts to create flame projekts, presets & templates.
# -------------------------------------------------------------------------- #
# version:          0.1.0
# modified:         2024-04-20 - 16:20:00
# comments:         refactored monolithic program into separate functions.
# -------------------------------------------------------------------------- #
# version:          0.5.0
# modified:         2024-05-24 - 20:24:00
# comments:         merged flame_colortoolkit with projekt.
# -------------------------------------------------------------------------- #
# version:          0.6.0
# modified:         2024-05-25 - 15:00:03
# comments:         started conversion to python3.
# -------------------------------------------------------------------------- #
# version:          0.7.0
# modified:         2024-06-21 - 18:21:03
# comments:         started gui design with pyside6.
# -------------------------------------------------------------------------- #
# version:          0.9.9
# modified:         2024-08-31 - 16:51:10
# comments:         prep for release - code appears to be functional
# -------------------------------------------------------------------------- #
