
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

# File Name:        print_nuke_environment.py
# Version:          0.0.1
# Created:          2024-11-08
# Modified:

# -------------------------------------------------------------------------- #

import nuke

def main():
    """
    Main function to print all key-value pairs from the nuke.env dictionary.

    This function retrieves all the keys from the nuke.env dictionary and prints
    each key along with its corresponding value in a formatted string.

    Returns:
        None
    """
    # Get all keys in nuke.env
    env_keys = nuke.env.keys()

    # Print key-value pairs
    for key in env_keys:
        value = nuke.env[key]
        print(f"{key}: {value}")


# -------------------------------------------------------------------------- #

# ========================================================================== #
# 53 54 52 45 4E 47 54 48 2D 49 4E 2D 4E 55 4D 42 45 52 53 C2 A9 32 30 32 35 #
# ========================================================================== #

