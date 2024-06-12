'''
# -------------------------------------------------------------------------- #

# File Name:        debug_and_log.py
# Version:          1.0.1
# Language:         python script
# Flame Version:    2025.x
# Author:           Phil MAN - phil_man@mac.com
# Toolset:          MAN_MADE_MATERIAL: LOGIK-PROJEKT
# Created:          2024-04-20
# Modified:         2024-06-11
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

import os
from PySide6.QtWidgets import QPushButton, QMessageBox
from modules.functions.openclip_prefs_saver import openclip_prefs_saver

# ========================================================================== #
# This section defines the main functions.
# ========================================================================== #

def create_button(summary_textbox):
    button = QPushButton("Update LOGIK-PROJEKT openclip preferences")
    button.clicked.connect(lambda: save_preferences(summary_textbox))
    return button

def save_preferences(summary_textbox):
    if not summary_textbox:
        # Handle if the summary textbox is not provided
        return

    try:
        openclip_prefs_saver(summary_textbox)
    except Exception as e:
        show_error_message(str(e))

def show_error_message(error_message):
    msg_box = QMessageBox()
    msg_box.setWindowTitle("Error")
    msg_box.setText(f"An error occurred: {error_message}")
    msg_box.setIcon(QMessageBox.Critical)
    msg_box.exec_()

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

#                   This program is distributed in the hope that it will
#                   be useful, but WITHOUT ANY WARRANTY; without even the
#                   implied warranty of MERCHANTABILITY or 
#                   FITNESS FOR A PARTICULAR PURPOSE.

#                   See the GNU General Public License for more details.
#                   You should have received a copy of the 
#                   GNU General Public License along with this program. 

#                   If not, see <https://www.gnu.org/licenses/>.

#                   In no event shall the authors or copyright holders be 
#                   liable for any claim, damages, or other liability, 
#                   whether in an action of contract, tort, or otherwise, 
#                   arising from, out of, or in connection with the software 
#                   or the use or other dealings in the software.

# -------------------------------------------------------------------------- #
'''

# -------------------------------------------------------------------------- #
# Changelist:       
# -------------------------------------------------------------------------- #
# version:               1.0.0
# modified:              2024-06-07 - 16:22:45
# comments:              Working program
# -------------------------------------------------------------------------- #
# version:               1.0.1
# modified:              2024-06-11 - 07:36:09
# comments:              Unique renaming of scripts and disclaimer update.
