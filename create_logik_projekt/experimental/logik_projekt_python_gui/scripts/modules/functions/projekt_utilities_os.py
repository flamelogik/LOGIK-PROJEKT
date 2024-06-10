'''
File Name:        projekt_utilities_os.py
Version:          1.0.0
Language:         python script
Author:           Phil MAN - phil_man@mac.com
Created:          2024-05-23
Modified:         2024-06-02

Description:      This program gathers operating system information
'''

# ========================================================================== #
# This section defines the import statements
# ========================================================================== #

import platform
import logging

# ========================================================================== #
# This function examines the operating system environment
# ========================================================================== #

def check_operating_system():
    '''
    Check if the operating system is Linux or macOS.
    '''
    os_name = platform.system()

    if os_name == 'Linux':
        logging.info("Operating system is Linux.")
        return 'Linux'

    elif os_name == 'Darwin':
        logging.info("Operating system is macOS.")
        return 'macOS'

    else:
        logging.error(f"Unsupported operating system: {os_name}")
        raise EnvironmentError(f"Unsupported operating system: {os_name}")

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
