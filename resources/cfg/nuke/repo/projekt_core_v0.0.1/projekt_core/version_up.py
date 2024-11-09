
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

# File Name:        version_up.py
# Version:          0.0.1
# Created:          2024-11-07
# Modified:         

# -------------------------------------------------------------------------- #

import nuke
import os
import re

def version_up_write_nodes():
    """
    Version up 'Write' nodes (EXR, QT, JPG) on save.
    
    This function looks for Write nodes named 'Write_exr', 'Write_QT', and 'Write_jpg',
    regardless of case. It updates their file path version to match the version from the 
    root script's name.
    """
    # List of write nodes to match (case-insensitive)
    write_nodes = ['Write_exr', 'Write_QT', 'Write_jpg']

    # Get the version from the root file name
    root_version_match = re.search(r'[vV]\d+', os.path.split(nuke.root().name())[1])
    
    if root_version_match:
        root_version = root_version_match.group()
        
        for node_name in write_nodes:
            # Match nodes case-insensitively
            for node in nuke.allNodes():
                if re.match(node_name, node.name(), re.IGNORECASE):
                    n = nuke.toNode(node.name())
                    # Update the file path with the version from the root script
                    n['file'].setValue(re.sub(r'[vV]\d+', root_version, n['file'].value()))
    else:
        return

# -------------------------------------------------------------------------- #
# Register callback
# -------------------------------------------------------------------------- #
nuke.addOnScriptSave(version_up_write_nodes)

# -------------------------------------------------------------------------- #

# ========================================================================== #
# C2 A9 32 30 32 34 20 7C 20 62 72 69 61 6E 40 73 69 6C 6F 38 34 2E 63 6F 6D #
# ========================================================================== #