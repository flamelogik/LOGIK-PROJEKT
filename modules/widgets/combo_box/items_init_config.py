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
# This section defines the primary functions for the script.
# ========================================================================== #

import os
import platform

# Define the initial presets directory path
presets_directory_path = '/opt/Autodesk/presets'

# Print the list of directories in presets_directory_path
print(f"  Directories in {presets_directory_path}:\n")
for entry in os.listdir(presets_directory_path):
    if os.path.isdir(os.path.join(presets_directory_path, entry)):
        print(f"  - {entry}")

# Function to get the latest version directory based on the versioning scheme
def get_latest_version(path):
    print(f"\n  Searching for the latest version in: {path}\n")
    latest_version = None
    max_version = (-1, -1, -1, -1)  # Initialize with smallest values

    for entry in os.listdir(path):
        if os.path.isdir(os.path.join(path, entry)):
            print(f"  Found directory: {entry}")
            parts = entry.split('.')

            try:
                # Parse major version
                major_version = int(parts[0])

                # Initialize minor, patch, pre_release versions
                minor_version = 0
                patch_version = 0
                pre_release_version = 0

                # Check if there are enough parts for minor version
                if len(parts) >= 2:
                    minor_part = parts[1].split('pr')
                    minor_version = int(minor_part[0]) if minor_part[0] else 0
                    if len(minor_part) > 1:
                        pre_release_version = int(minor_part[1])

                # Check if there are enough parts for patch version
                if len(parts) >= 3:
                    patch_part = parts[2].split('pr')
                    patch_version = int(patch_part[0]) if patch_part[0] else 0
                    if len(patch_part) > 1:
                        pre_release_version = int(patch_part[1])

                version_tuple = (major_version, minor_version, patch_version, pre_release_version)
                print(f"  Parsed version tuple: {version_tuple}\n")

                if version_tuple > max_version:
                    max_version = version_tuple
                    latest_version = entry
                    print(f"  Updated latest version: {latest_version}\n")

            except ValueError:
                continue  # Skip if version parsing fails

    if latest_version:
        print(f"  Latest version found: {latest_version}\n")
    else:
        print("  No valid version directories found.")

    return latest_version

# Get the latest version directory in presets directory
latest_version_directory = get_latest_version(presets_directory_path)

if latest_version_directory:
    print(f"  Latest version directory: {latest_version_directory}\n")

    # Form the path to cfg directory
    cfg_directory_path = os.path.join(presets_directory_path, latest_version_directory, 'cfg')
    print(f"  Path to cfg directory: {cfg_directory_path}\n")

    # Select macos or linux based on the platform
    system_type = platform.system().lower()
    if system_type == 'darwin':  # MacOS
        system_subdirectory = 'macos'
    elif system_type == 'linux':
        system_subdirectory = 'linux'
    else:
        raise RuntimeError(f"Unsupported system: {system_type}\n")

    print(f"  Detected system type: {system_type}\n")
    print(f"  Selected system subdirectory: {system_subdirectory}\n")

    # Form the path to template directory
    template_directory_path = os.path.join(cfg_directory_path, system_subdirectory, 'template')
    print(f"  Path to template directory: {template_directory_path}\n")

    # Check if template directory exists
    if os.path.exists(template_directory_path) and os.path.isdir(template_directory_path):
        # List contents of the template directory and sort them alphabetically
        template_contents = sorted(os.listdir(template_directory_path))
        print(f"  Template directory found. Sorted contents:\n")
        for item in template_contents:
            print(f"  {item}")

        # Set combo_box_items_init_config to template_contents
        combo_box_items_init_config = template_contents
        # print(f"  combo_box_items_init_config set to: {combo_box_items_init_config}")  # hide this from the shell

    else:
        combo_box_items_init_config = []
        print(f"  Template directory not found: {template_directory_path}\n")
        print(f"  combo_box_items_init_config set to empty list\n")
else:
    combo_box_items_init_config = []
    print(f"  No directories found in presets directory.\n")
    print(f"  combo_box_items_init_config set to empty list\n")

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
