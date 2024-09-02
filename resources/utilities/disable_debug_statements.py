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

# resources/utilities/disable_debug_statements.py

# ========================================================================== #
# This section defines the import statements and diresctory paths.
# ========================================================================== #

import os

def search_and_replace(root_dir, replacements, log_file):
    log_entries = []

    for subdir, _, files in os.walk(root_dir):
        for file in files:
            if file.endswith('.py'):
                file_path = os.path.join(subdir, file)
                with open(file_path, 'r') as f:
                    lines = f.readlines()

                modified = False
                new_lines = []
                for line in lines:
                    original_line = line
                    for search_str, replace_str in replacements.items():
                        if search_str in line:
                            line = line.replace(search_str, replace_str)
                            modified = True
                    if modified:
                        new_lines.append(line)
                        log_entries.append(f"Modified: {file_path}\nOriginal: {original_line.strip()}\nNew: {line.strip()}\n")
                    else:
                        new_lines.append(line)

                if modified:
                    with open(file_path, 'w') as f:
                        f.writelines(new_lines)

    with open(log_file, 'w') as log:
        log.writelines(log_entries)

if __name__ == "__main__":
    root_directory = '/home/pman/workspace/GitHub/projekt_app/modules/widgets'
    replacements = {
        'print(f"  Debug: ': '# print(f"  Debug: ',
        '# # print(f"  Debug: ': '# print(f"  Debug: '
    }
    log_filename = '/home/pman/workspace/GitHub/projekt_app/modules/utilities/disable_debug_statements-log.txt'

    search_and_replace(root_directory, replacements, log_filename)

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
