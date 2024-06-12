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

from PySide6.QtWidgets import QLineEdit

# ========================================================================== #
# This section defines the main functions.
# ========================================================================== #

'''
def create_lineedit():
    lineedit = QLineEdit()
    # Set placeholder text if needed
    # lineedit.setPlaceholderText("Enter text here")
    # Set text if needed
    # lineedit.setText("Enter text here")
    return lineedit
'''

def create_render_node_type_lineedit():
    lineedit = QLineEdit()
    # lineedit.setPlaceholderText("Write File Node")
    lineedit.setText("Write File Node")
    return lineedit

def create_write_node_projekt_root_path_lineedit():
    lineedit = QLineEdit()
    # lineedit.setPlaceholderText("/JOBS/")
    lineedit.setText("/JOBS/")
    return lineedit

def create_write_node_file_path_lineedit():
    lineedit = QLineEdit()
    # lineedit.setPlaceholderText("<project nickname>/shots/<shot name>/media/renders/<name>_<version name>/<name>_<version name><frame><ext>")
    lineedit.setText("<project nickname>/shots/<shot name>/media/renders/<name>_<version name>/<name>_<version name><frame><ext>")
    return lineedit

def create_write_node_openclip_path_lineedit():
    lineedit = QLineEdit()
    # lineedit.setPlaceholderText("<project nickname>/shots/<shot name>/openclip/output_clips/flame/<name><ext>")
    lineedit.setText("<project nickname>/shots/<shot name>/openclip/output_clips/flame/<name><ext>")
    return lineedit

def create_write_node_setup_path_lineedit():
    lineedit = QLineEdit()
    # lineedit.setPlaceholderText("<project nickname>/shots/<shot name>/batch_setups/<name>_<version name>_<workstation>_<user nickname><ext>")
    lineedit.setText("<project nickname>/shots/<shot name>/batch_setups/<name>_<version name>_<workstation>_<user nickname><ext>")
    return lineedit

def create_write_node_create_openclip_lineedit():
    lineedit = QLineEdit()
    # lineedit.setPlaceholderText("True")
    lineedit.setText("True")
    return lineedit

def create_write_node_include_setup_lineedit():
    lineedit = QLineEdit()
    # lineedit.setPlaceholderText("True")
    lineedit.setText("True")
    return lineedit

def create_write_node_image_format_lineedit():
    lineedit = QLineEdit()
    # lineedit.setPlaceholderText("OpenEXR 16-bit fp")
    lineedit.setText("OpenEXR 16-bit fp")
    return lineedit

def create_write_node_compression_lineedit():
    lineedit = QLineEdit()
    # lineedit.setPlaceholderText("PIZ")
    lineedit.setText("PIZ")
    return lineedit

def create_write_node_padding_lineedit():
    lineedit = QLineEdit()
    # lineedit.setPlaceholderText("8")
    lineedit.setText("8")
    return lineedit

def create_write_node_frame_index_lineedit():
    lineedit = QLineEdit()
    # lineedit.setPlaceholderText("Use Start Frame")
    lineedit.setText("Use Start Frame")
    return lineedit

def create_write_node_version_name_lineedit():
    lineedit = QLineEdit()
    # lineedit.setPlaceholderText("v<version>")
    lineedit.setText("v<version>")
    return lineedit

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
