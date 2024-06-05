'''
File Name:        projekt_utilities_strukture.py
Version:          1.0.0
Language:         python script
Author:           Phil MAN - phil_man@mac.com
Created:          2024-05-23
Modified:         2024-06-02

Description:      This program defines projekt directory strukture
'''

# ========================================================================== #
# This section defines the import statements
# ========================================================================== #

import os
import logging

# ========================================================================== #
# This function defines the directory strukture for a logik projekt
# ========================================================================== #

def create_directory(path):
    """Create a directory if it does not exist."""
    if not os.path.exists(path):
        os.makedirs(path)
        logging.info(f"Created directory: {path}")
    else:
        logging.warning(f"Directory already exists: {path}")

def create_logik_projekt_structure(base_path, projekt_name):
    """Create the directory structure for a new LOGIK-PROJEKT."""
    projekt_path = os.path.join(base_path, projekt_name)

    # Create main LOGIK-PROJEKT directory
    create_directory(projekt_path)

    # Define subdirectories
    subdirectories = [
        'build',
        'config',
        'doc',
        'experimental',
        'log',
        'pref',
        'script',
        'temp',
        'www',
        'version'
    ]

    for subdirectory in subdirectories:
        create_directory(os.path.join(projekt_path, subdirectory))

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
