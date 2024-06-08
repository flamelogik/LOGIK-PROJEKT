'''
# -------------------------------------------------------------------------- #

# File Name:        debug_and_log.py
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
# This section defines the import staements.
# ========================================================================== #

# pyside6_summary.py
from PySide6.QtWidgets import QTextEdit

# ========================================================================== #
# This section defines the main functions.
# ========================================================================== #

local_stylesheet = """
/* Summary box (QTextEdit) */
QTextEdit {
    background-color: #37414b;  /* Replace with your desired color */
    color: #ffffff;  /* Text color */
    font: 14px "Discreet";  /* Font */
    border: 1px solid #007acc;  /* Border */
    border-radius: 0px;  /* No rounded corners */
}
"""

def create_summary_textbox():
    textbox = QTextEdit()
    textbox.setReadOnly(True)  # Make it read-only
    textbox.setStyleSheet(local_stylesheet)  # Apply the local stylesheet
    return textbox

# def update_summary_textbox(textbox, dropdowns):
#     summary_text = ""
#     for label, dropdown in dropdowns.items():
#         summary_text += f"{label}: {dropdown.currentText()}\n"
#     textbox.setPlainText(summary_text)

def update_summary_textbox(textbox, lineedits, dropdowns):
    summary_text = ""
    for label, lineedit in lineedits.items():
        summary_text += f"{label}: {lineedit.text()}\n"
    for label, dropdown in dropdowns.items():
        summary_text += f"{label}: {dropdown.currentText()}\n"
    textbox.setPlainText(summary_text)

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
