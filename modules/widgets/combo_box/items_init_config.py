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

# File Name:        items_init_config.py
# Version:          1.9.9
# Created:          2024-01-19
# Modified:         2024-12-25

# ========================================================================== #
# This section defines the import statements and directory paths.
# ========================================================================== #

# Standard library imports
import os
import platform
import sys

# -------------------------------------------------------------------------- #

def get_base_path():
    if getattr(sys, 'frozen', False):
        return sys._MEIPASS
    else:
        return os.path.abspath(
            os.path.join(
                os.path.dirname(__file__), '..', '..', '..'
            )
        )
    
# -------------------------------------------------------------------------- #

def get_resource_path(relative_path):
    base_path = get_base_path()
    return os.path.join(
        base_path,
        relative_path
    )

# -------------------------------------------------------------------------- #

# Set the path to the 'modules' directory
modules_dir = get_resource_path('modules')
# Set the path to the 'resources' directory
resources_dir = get_resource_path('resources')
# Append the modules path to the system path
if modules_dir not in sys.path:
    sys.path.append(modules_dir)

# ========================================================================== #
# This section defines the primary functions for the script.
# ========================================================================== #

# Define the fixed template directory path
template_directory_path = get_resource_path('resources/flame/presets/cfg/init.cfg/template')
print(f"  Looking for templates in: {template_directory_path}\n")

# Initialize combo_box_items_init_config
combo_box_items_init_config = []

# Check if template directory exists
if os.path.exists(template_directory_path) and os.path.isdir(template_directory_path):
    # List contents of the template directory and sort them alphabetically
    template_contents = sorted(os.listdir(template_directory_path))
    print(f"  Template directory found. Contents:\n")
    for item in template_contents:
        print(f"  {item}")
    
    # Filter for .cfg files if needed
    combo_box_items_init_config = [item for item in template_contents if item.endswith('.cfg')]
    print(f"\n  Found {len(combo_box_items_init_config)} template files")
else:
    print(f"  Template directory not found: {template_directory_path}")
    print(f"  combo_box_items_init_config set to empty list\n")

# If no templates were found, provide a default template
if not combo_box_items_init_config:
    combo_box_items_init_config = ["1920x1080@23976p.cfg"]
    print(f"  Using default template: {combo_box_items_init_config[0]}\n")

# Export variables for use in other scripts
__all__ = ['template_directory_path', 'combo_box_items_init_config']

# ========================================================================== #
# C2 A9 32 30 32 34 2D 4D 41 4E 2D 4D 41 44 45 2D 4D 45 4B 41 4E 59 5A 4D 53 #
# ========================================================================== #

# Changelist:       

# -------------------------------------------------------------------------- #
# version:          0.0.1
# created:          2024-01-19 - 12:34:56
# comments:         scripts to create flame projekts, presets & templates.
# -------------------------------------------------------------------------- #
# version:          0.1.0
# modified:         2024-04-20 - 16:20:00
# comments:         refactored monolithic program into separate functions.
# -------------------------------------------------------------------------- #
# version:          0.5.0
# modified:         2024-05-24 - 20:24:00
# comments:         merged flame_colortoolkit with projekt.
# -------------------------------------------------------------------------- #
# version:          0.6.0
# modified:         2024-05-25 - 15:00:03
# comments:         started conversion to python3.
# -------------------------------------------------------------------------- #
# version:          0.7.0
# modified:         2024-06-21 - 18:21:03
# comments:         started gui design with pyside6.
# -------------------------------------------------------------------------- #
# version:          0.9.9
# modified:         2024-08-31 - 16:51:09
# comments:         prep for release - code appears to be functional
# -------------------------------------------------------------------------- #
# Version:          1.9.9
# modified:         2024-12-25 - 09:50:17
# comments:         Preparation for future features
# -------------------------------------------------------------------------- #
