#!/usr/bin/env python3
# -------------------------------------------------------------------------- #
# Filename:     modify_flame_workspace_colors.py
# Purpose:      Modifies the colors of a Flame workspace JSON file.
# Description:  This script reads a Flame workspace JSON file, and for each
#               library, it makes the children of that library a slightly
#               brighter color than the parent.
# Author:       Gemini
# -------------------------------------------------------------------------- #

import json
import os

def brighten_color(color, factor=1.05):
    """Increases the brightness of a color by a given factor and rounds to 3 decimal places."""
    return [round(min(1.0, c * factor), 3) for c in color]

def process_children(children, parent_color):
    """Recursively processes children to brighten their colors."""
    for child in children:
        child_color = brighten_color(parent_color)
        child["colour"] = child_color
        if "children" in child:
            process_children(child["children"], child_color)

def modify_workspace_colors(file_path):
    """Loads, modifies, and saves the workspace JSON file."""
    try:
        with open(file_path, 'r') as f:
            workspace_data = json.load(f)

        for item in workspace_data:
            if item.get("type") == "library" and "children" in item:
                parent_color = item.get("colour", [0.5, 0.5, 0.5])
                process_children(item["children"], parent_color)

        with open(file_path, 'w') as f:
            json.dump(workspace_data, f, indent=4)
        
        print(f"Successfully modified colors in {file_path}")

    except FileNotFoundError:
        print(f"Error: Workspace file not found at {file_path}")
    except json.JSONDecodeError:
        print(f"Error: Could not decode JSON from {file_path}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == '__main__':
    # Assumes the script is run from the project root
    # You might need to adjust the path depending on your execution context
    workspace_file_path = os.path.join(
        os.path.dirname(__file__),
        '../../../../pref/site-prefs/default-prefs/logik-projekt-prefs/flame-workspace.json'
    )
    modify_workspace_colors(os.path.normpath(workspace_file_path))


# -------------------------------------------------------------------------- #

# DISCLAIMER:   This file is part of LOGIK-PROJEKT.

#               Copyright © 2025 STRENGTH IN NUMBERS

#               LOGIK-PROJEKT creates directories, files, scripts & tools
#               for use with Autodesk Flame and other software.

#               LOGIK-PROJEKT is free software.

#               You can redistribute it and/or modify it under the terms
#               of the GNU General Public License as published by the
#               Free Software Foundation, either version 3 of the License,
#               or any later version.

#               This program is distributed in the hope that it will be
#               useful, but WITHOUT ANY WARRANTY; without even the
#               implied warranty of MERCHANTABILITY or
#               FITNESS FOR A PARTICULAR PURPOSE.

#               See the GNU General Public License for more details.
#               You should have received a copy of the GNU General
#               Public License along with this program.

#               If not, see <https://www.gnu.org/licenses/gpl-3.0.en.html>.

#               Contact: phil_man@mac.com

# -------------------------------------------------------------------------- #
# C2 A9 32 30 32 35 53 54 52 45 4E 47 54 48 2D 49 4E 2D 4E 55 4D 42 45 52 53 #
# -------------------------------------------------------------------------- #
# Changelog:
# -------------------------------------------------------------------------- #
