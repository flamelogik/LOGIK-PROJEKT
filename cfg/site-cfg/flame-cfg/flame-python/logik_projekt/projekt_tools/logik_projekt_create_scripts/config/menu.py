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

# filename: menu.py

# Installation:
# Windows: C:\Users\YourUsername\.nuke\menu.py
# macOS: /Users/YourUsername/.nuke/menu.py
# Linux: /home/YourUsername/.nuke/menu.py

# ========================================================================== #
# This section defines the import statements and directory paths.
# ========================================================================== #

import os.path
import nuke
import nukescripts
import re

try:
    from PySide6 import QtWidgets, QtCore, QtGui
except ImportError:
    from PySide2 import QtWidgets, QtCore, QtGui

# Function to update the versioning in the file paths of all write nodes
def update_write_node_version():
  
    """Increments the versioning in the file paths of all write nodes"""
    root_name = nuke.toNode("root").name()

    # Get the version number from the script name
    (script_prefix, script_version) = nukescripts.version_get(root_name, "v")

    for node in nuke.allNodes("Write"):
      
        file_knob = node["file"]

        if file_knob is not None:
          
            current_path = file_knob.value()

            if current_path:
              
                # Split directory and filename
                dirname, basename = os.path.split(current_path)

                # Split basename and extension
                basename, ext = os.path.splitext(basename)

                # Extract version from basename
                (path_prefix, path_version) = nukescripts.version_get(basename, "v")

                # Check if script version is greater than file path version
                if script_version > path_version:
                  
                    # Version up basename
                    new_basename = nukescripts.version_set(
                        basename, path_prefix, int(path_version), int(script_version)
                    )
                    # Update directory name
                    new_dirname = dirname.replace(
                        path_prefix + str(path_version).zfill(4), path_prefix + str(int(script_version)).zfill(4)
                    )
                    # Reconstruct full path
                    new_path = os.path.join(new_dirname, new_basename + ext)
                    file_knob.setValue(new_path)


# Add a callback to the script_save event
nuke.addOnScriptSave(update_write_node_version)

# ========================================================================== #
# C2 A9 32 30 32 34 2D 4D 41 4E 2D 4D 41 44 45 2D 4D 45 4B 41 4E 59 5A 4D 53 #
# ========================================================================== #

# Changelist:     

# -------------------------------------------------------------------------- #
