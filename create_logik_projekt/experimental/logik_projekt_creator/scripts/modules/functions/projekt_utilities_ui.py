'''
File Name:        projekt_utilities_ui.py
Version:          1.0.0
Language:         python script
Author:           Phil MAN - phil_man@mac.com
Created:          2024-05-23
Modified:         2024-06-02

Description:      This program defines functions for creating UI widgets
'''

# ========================================================================== #
# This section defines the import statements
# ========================================================================== #

from PySide6.QtWidgets import QLabel, QLineEdit, QComboBox, QPushButton

# ========================================================================== #
# This function defines functions for creating UI widgets
# ========================================================================== #

def create_labeled_entry(layout, label_text):
    label = QLabel(label_text)
    label.setStyleSheet("color: white; font-family: 'Courier New', monospace; font-weight: bold;")
    layout.addWidget(label)

    entry = QLineEdit()
    entry.setStyleSheet("""
        background-color: #111111;
        color: white;
        font-family: 'Courier New', monospace;
        font-weight: bold;
    """)
    layout.addWidget(entry)
    return entry

# -------------------------------------------------------------------------- #

def create_dropdown_menu(layout, label_text):
    label = QLabel(label_text)
    label.setStyleSheet("color: white; font-family: 'Courier New', monospace; font-weight: bold;")
    layout.addWidget(label)

    combo_box = QComboBox()
    combo_box.setStyleSheet("""
        background-color: #111111;
        color: white;
        font-family: 'Courier New', monospace;
        font-weight: bold;
    """)
    layout.addWidget(combo_box)
    return combo_box

# -------------------------------------------------------------------------- #

def create_button(layout, text, color, function):
    button = QPushButton(text)
    button.setStyleSheet(f"""
        background-color: {color};
        color: white;
        font-family: 'Courier New', monospace;
        font-weight: bold;
    """)
    button.clicked.connect(function)
    layout.addWidget(button)
    return button

# ========================================================================== #
# C2 A9 32 30 32 34 2D 4D 41 4E 5F 4D 41 44 45 2D 4D 45 4B 41 4E 49 53 4D 5A #
# ========================================================================== #

'''
Disclaimer:       This program is part of LOGIK-PROJEKT.
                  LOGIK-PROJEKT is free software.

                  You can redistribute it and/or modify it under the terms
                  of the GNU General Public License as published by the
                  Free Software Foundation, either version 3 of the License,
                  or any later version.

                  This program is distributed in the hope that it will be
                  useful, but WITHOUT ANY WARRANTY; without even the
                  implied warranty of MERCHANTABILITY or FITNESS FOR A
                  PARTICULAR PURPOSE.

                  See the GNU General Public License for more details.

                  You should have received a copy of the GNU General
                  Public License along with this program.

                  If not, see <https://www.gnu.org/licenses/>.
'''

# -------------------------------------------------------------------------- #
# Changelist:
# -------------------------------------------------------------------------- #
