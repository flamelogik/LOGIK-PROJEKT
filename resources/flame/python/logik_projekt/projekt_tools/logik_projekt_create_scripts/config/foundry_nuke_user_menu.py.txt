# Installation:
# Windows: C:\Users\YourUsername\.nuke\menu.py
# macOS: /Users/YourUsername/.nuke/menu.py
# Linux: /home/YourUsername/.nuke/menu.py

import os.path
import nuke
import nukescripts
import re
from PySide2 import QtWidgets, QtGui, QtCore

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
