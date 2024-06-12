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

from PySide6.QtWidgets import QComboBox

# ========================================================================== #
# This section defines the main functions.
# ========================================================================== #

def create_openclip_dropdown():
    dropdown = QComboBox()
    dropdown.addItems(["True", "False"])
    return dropdown

def create_setup_dropdown():
    dropdown = QComboBox()
    dropdown.addItems(["True", "False"])
    return dropdown

def create_node_type_dropdown():
    dropdown = QComboBox()
    dropdown.addItems(["Render", "Write File"])
    return dropdown

def create_node_format_dropdown():
    dropdown = QComboBox()
    dropdown.addItems(["RGB-A", "Multi-Channel"])
    return dropdown

def create_render_resolution_dropdown():
    dropdown = QComboBox()
    dropdown.addItems(["Working", "Full"])
    return dropdown

def create_frame_rate_dropdown():
    dropdown = QComboBox()
    dropdown.addItems(["23.976 fps", "24 fps", "25 fps", "29.97 fps DF", "29.97 fps NDF", "30 fps", "50 fps", "59.94 fps DF", "59.94 fps NDF", "60 fps"])
    return dropdown

def create_file_format_dropdown():
    dropdown = QComboBox()
    dropdown.addItems(["Alias", "Cineon", "Dpx", "Jpeg", "Maya", "OpenEXR", "Pict", "Pixar", "Png", "Sgi", "SoftImage", "Targa", "Tiff", "Tx", "Wavefront"])
    return dropdown

def create_bit_depth_dropdown():
    dropdown = QComboBox()
    dropdown.addItems(["32-bit fp", "16-bit fp", "16-bit", "12-bit", "10-bit", "8-bit"])
    return dropdown

def create_compression_dropdown():
    dropdown = QComboBox()
    dropdown.addItems(["Scanline", "Multi_Scanline", "RLE", "PXR24", "PIZ", "Pixspan", "Packed", "LZW", "DWAB", "DWAA", "B44A", "B44", "Uncompressed"])
    return dropdown

def create_media_path_tokens_dropdown():
    dropdown = QComboBox()
    dropdown.addItems(["Date", "Time", "Year (YYYY)", "Year (YY)", "Month", "Day", "Hour", "Minute", "Second", "Workstation", "User Nickname", "User", "Project Nickname", "Project", "Batch Iteration", "Batch Name", "Iteration", "Tape/Reel/Source", "Shot Name", "Colour Space", "Clip Resolution", "Clip Height", "Clip Width", "Version", "Version Name", "Extension", "Polarity", "Frame Index", "Clip Name"])
    return dropdown

def create_workspace_tokens_dropdown():
    dropdown = QComboBox()
    dropdown.addItems(["Batch Reels", "Reel Groups", "Libraries"])
    return dropdown

def create_version_dropdown():
    dropdown = QComboBox()
    dropdown.addItems(["Follow Iteration", "Custom Version", "No Versioning"])
    return dropdown

def create_zero_padding_dropdown():
    dropdown = QComboBox()
    dropdown.addItems(["4", "5", "6", "7", "8"])
    return dropdown

def create_start_frame_dropdown():
    dropdown = QComboBox()
    dropdown.addItems(["Follow Iteration", "Custom Version", "No Versioning"])
    return dropdown

def create_version_prefix_dropdown():
    dropdown = QComboBox()
    dropdown.addItems(["v", "V"])
    return dropdown

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
