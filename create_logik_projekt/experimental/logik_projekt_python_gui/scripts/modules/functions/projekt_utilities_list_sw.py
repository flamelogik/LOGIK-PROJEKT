'''
File Name:        projekt_utilities_list_sw.py
Version:          1.0.0
Language:         python script
Author:           Phil MAN - phil_man@mac.com
Created:          2024-05-23
Modified:         2024-06-02

Description:      This program processes flame family software installations
'''

# ========================================================================== #
# This section defines the import statements
# ========================================================================== #

import os
import re

# ========================================================================== #
# This function defines lists and sorts flame family software installations
# ========================================================================== #

def list_flame_family_software(directory):
    try:
        # List all entries in the directory
        entries = os.listdir(directory)
        
        # Filter for directories that begin with 'flame_'
        flame_dirs = [entry for entry in entries if entry.startswith('flame_') and os.path.isdir(os.path.join(directory, entry))]
        
        # Sort the list alphanumerically using custom sorting logic
        flame_dirs = sorted(flame_dirs, key=flame_version_key, reverse=True)
        
        return flame_dirs
    
    except Exception as e:
        print(f"An error occurred: {e}")
        return []

# -------------------------------------------------------------------------- #

def flame_version_key(directory_name):
    """
    Extracts the version information from a directory name and converts it into a tuple
    that can be used for sorting. Handles prerelease versions by considering them lower value
    than release versions.
    """
    pattern = r'flame_(\d+)(?:\.(\d+))?(?:\.(\d+))?(?:\.pr(\d+)(?:\.(\d+))?)?'
    match = re.match(pattern, directory_name)
    
    if not match:
        return (0, 0, 0, 0, 0)  # Return a default tuple for non-matching names
    
    major_version = int(match.group(1)) if match.group(1) else 0
    minor_version = int(match.group(2)) if match.group(2) else 0
    patch_version = int(match.group(3)) if match.group(3) else 0
    pr_version = int(match.group(4)) if match.group(4) else 0
    sub_pr_version = int(match.group(5)) if match.group(5) else 0
    
    return (major_version, minor_version, patch_version, pr_version, sub_pr_version)

# -------------------------------------------------------------------------- #

def latest_flame_version(directory):
    flame_dirs = list_flame_family_software(directory)
    if flame_dirs:
        return flame_dirs[0]  # The first element in the reversed sorted list
    else:
        return None

# -------------------------------------------------------------------------- #

def sanitize_latest_flame_version_name(version):
    # Remove the 'pr' suffix and everything after it
    version = re.sub(r'\.pr\d+(\.\d+)?', '', version)
    
    # Replace periods with underscores
    version = version.replace('.', '_')
    
    return version

# -------------------------------------------------------------------------- #

# Example usage
if __name__ == "__main__":
    directory = '/opt/Autodesk'
    
    flame_dirs = list_flame_family_software(directory)
    # print("Sorted flame directories:")
    for flame_dir in flame_dirs:
        print(flame_dir)
    
    latest_version = latest_flame_version(directory)
    print("\nThe latest flame version is:")
    print(latest_version)
    
    sanitized_version = sanitize_latest_flame_version_name(latest_version)
    print("\nThe sanitized latest flame version is:")
    print(sanitized_version)

# ========================================================================== #
# C2 A9 32 30 32 34 2D 4D 41 4E 5F 4D 41 44 45 2D 4D 45 4B 41 4E 49 53 4D 5A #
# ========================================================================== #

'''
Disclaimer:       This program is part of LOGIK-PROJEKT.
                  LOGIK-PROJEKT is free software.

                  You can redistribute it and/or modify it under the terms
                  of the GNU General Public License as published by the
                  Free Software Foundation, either version 3 of the License,
                  or any later version.

                  This program is distributed in the hope that it will be
                  useful, but WITHOUT ANY WARRANTY; without even the
                  implied warranty of MERCHANTABILITY or FITNESS FOR A
                  PARTICULAR PURPOSE.

                  See the GNU General Public License for more details.

                  You should have received a copy of the GNU General
                  Public License along with this program.

                  If not, see <https://www.gnu.org/licenses/>.
'''

# -------------------------------------------------------------------------- #
# Changelist:
# -------------------------------------------------------------------------- #
