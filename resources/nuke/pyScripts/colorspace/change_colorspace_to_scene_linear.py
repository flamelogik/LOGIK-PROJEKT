
# -------------------------------------------------------------------------- #

# DISCLAIMER:       This file is part of LOGIK-PROJEKT.
#                   Copyright © 2024 Silo 84
               
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
               
#                   Contact: brian@silo84.com

# -------------------------------------------------------------------------- #

# File Name:        change_colorspace_to_scene_linear.py
# Version:          0.0.1
# Created:          2024-11-08
# Modified:         

# -------------------------------------------------------------------------- #


import nuke
 
def change_colorspace_to_scene_linear(): 
    """
    Change the colorspace of selected 'Read' nodes in Nuke to 'scene_linear'.
    This function iterates through all currently selected nodes in Nuke,
    checks if they are of the class 'Read', and sets their colorspace to 'scene_linear'.
    It also optionally refreshes the Nuke GUI to reflect the changes.
    Usage:
        Select the 'Read' nodes in Nuke that you want to change the colorspace for,
        then run this function.
    Note:
        This script is intended to be used within the Nuke environment.
    """
    # Get the selected nodes
    selected_nodes = nuke.selectedNodes()
     
    # Iterate through the selected nodes and set the colorspace
    for node in selected_nodes:
        if node.Class() == 'Read':
            node['colorspace'].setValue('scene_linear')
     
    # Optional: Refresh the GUI to reflect the changes
    nuke.updateUI()

def main():
    change_colorspace_to_scene_linear()

# -------------------------------------------------------------------------- #

# ========================================================================== #
# C2 A9 32 30 32 34 20 7C 20 62 72 69 61 6E 40 73 69 6C 6F 38 34 2E 63 6F 6D #
# ========================================================================== #

