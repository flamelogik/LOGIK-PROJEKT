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

import os
import json
from datetime import datetime
from PySide6.QtWidgets import QFileDialog, QMessageBox

# ========================================================================== #
# This section defines the main functions.
# ========================================================================== #

def parse_summary_text(summary_text_content):
    """
    Parse the summary text content and convert it to a dictionary.
    """
    summary_dict = {}
    lines = summary_text_content.split('\n')
    for line in lines:
        if ': ' in line:
            key, value = line.split(': ', 1)
            summary_dict[key.strip()] = value.strip()
    return summary_dict

def openclip_prefs_saver(summary_text):
    # Get the directory of the config folder
    config_dir = os.path.join(os.path.dirname(__file__), '..', '..', '..', 'config')

    # Create the config directory if it doesn't exist
    if not os.path.exists(config_dir):
        os.makedirs(config_dir)

    # Define the file paths
    prefs_file_path = os.path.join(config_dir, 'openclip_prefs.json')
    backup_file_path = None

    # Check if the prefs file already exists
    if os.path.exists(prefs_file_path):
        # Create a backup file with timestamp
        timestamp = datetime.now().strftime('%Y_%m_%d-%H_%M')
        backup_file_path = os.path.join(config_dir, f'openclip_prefs-{timestamp}.bak')
        os.rename(prefs_file_path, backup_file_path)

    # Get the contents of the summary text box
    summary_text_content = summary_text.toPlainText()

    # Parse the summary text content
    summary_dict = parse_summary_text(summary_text_content)

    # Save the contents to the prefs file as JSON
    with open(prefs_file_path, 'w') as prefs_file:
        json.dump(summary_dict, prefs_file, indent=4)

    # Show message box
    msg_box = QMessageBox()
    msg_box.setWindowTitle("Preferences Saved")
    msg_box.setText("Your preferences have been successfully saved.")
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
