
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

# File Name:        print_environment_variables.py
# Version:          0.0.1
# Created:          2024-11-08
# Modified:         

# -------------------------------------------------------------------------- #

import os

def print_environment_variables():
    """
    Prints all environment variables and their values.

    This function retrieves all environment variable names (keys) from the
    os.environ dictionary and prints each key-value pair.

    Returns:
        None
    """
    # Get all keys (environment variable names) in os.environ
    env_keys = os.environ.keys()

    # Print key-value pairs
    for key in env_keys:
        value = os.environ[key]
        print(f"{key}: {value}")


def main():
    print_environment_variables()

# -------------------------------------------------------------------------- #

# ========================================================================== #
# C2 A9 32 30 32 34 20 7C 20 62 72 69 61 6E 40 73 69 6C 6F 38 34 2E 63 6F 6D #
# ========================================================================== #

