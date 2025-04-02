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
# Version:          2.0.0
# Created:          2024-01-19
# Modified:         2024-12-31

# ========================================================================== #
# This section defines the stylesheet for the main application.
# ========================================================================== #

def adjust_color_brightness(color, factor):
    """
    Adjust the brightness of a hex color.
   
    Args:
        color (str): The hex color string (e.g., '#4D0000').
        factor (float): The factor by which to adjust the brightness (e.g., 1.1 for 10% brighter, 0.8 for 20% darker).
   
    Returns:
        str: The adjusted hex color string.
    """
    color = color.lstrip('#')
    rgb = tuple(int(color[i:i+2], 16) for i in (0, 2, 4))
    adjusted_rgb = tuple(min(255, max(0, int(c * factor))) for c in rgb)
    return '#{:02x}{:02x}{:02x}'.format(*adjusted_rgb)

# Define the base colors
button_color_1 = "#4D0000"  # Red
button_color_2 = "#7F3F00"  # Amber
button_color_3 = "#2F5F00"  # Green

# Calculate hover and pressed colors
button_color_1_hover = adjust_color_brightness(button_color_1, 1.25)  # 25% brighter
button_color_1_pressed = adjust_color_brightness(button_color_1, 0.6)  # 40% darker

button_color_2_hover = adjust_color_brightness(button_color_2, 1.25)  # 25% brighter
button_color_2_pressed = adjust_color_brightness(button_color_2, 0.6)  # 40% darker

button_color_3_hover = adjust_color_brightness(button_color_3, 1.25)  # 25% brighter
button_color_3_pressed = adjust_color_brightness(button_color_3, 0.6)  # 40% darker

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

# Stylesheet for Button Color 1 (Red)
ButtonColor1StyleSheet = f"""
QPushButton {{
    background-color: {button_color_1}; /* Normal state */
    color: #ffffff; /* Text color */
    border: 1px solid #444444; /* Border */
    padding: 5px; /* Padding */
}}

QPushButton:hover {{
    background-color: {button_color_1_hover}; /* Hover state */
}}

QPushButton:pressed {{
    background-color: {button_color_1_pressed}; /* Pressed state */
}}
"""

# Stylesheet for Button Color 2 (Amber)
ButtonColor2StyleSheet = f"""
QPushButton {{
    background-color: {button_color_2}; /* Normal state */
    color: #ffffff; /* Text color */
    border: 1px solid #444444; /* Border */
    padding: 5px; /* Padding */
}}

QPushButton:hover {{
    background-color: {button_color_2_hover}; /* Hover state */
}}

QPushButton:pressed {{
    background-color: {button_color_2_pressed}; /* Pressed state */
}}
"""

# Stylesheet for Button Color 3 (Green)
ButtonColor3StyleSheet = f"""
QPushButton {{
    background-color: {button_color_3}; /* Normal state */
    color: #ffffff; /* Text color */
    border: 1px solid #444444; /* Border */
    padding: 5px; /* Padding */
}}

QPushButton:hover {{
    background-color: {button_color_3_hover}; /* Hover state */
}}

QPushButton:pressed {{
    background-color: {button_color_3_pressed}; /* Pressed state */
}}
"""

def apply_stylesheet(app, stylesheet):
    app.setStyleSheet(stylesheet)
   
# ========================================================================== #
# 53 54 52 45 4E 47 54 48 2D 49 4E 2D 4E 55 4D 42 45 52 53 C2 A9 32 30 32 35 #
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
# version:          1.9.9
# modified:         2024-12-25 - 09:50:19
# comments:         Preparation for future features
# -------------------------------------------------------------------------- #
# version:          2.0.0
# modified:         2024-12-31 - 11:17:29
# comments:         Improved legibility and minor modifications
# -------------------------------------------------------------------------- #
