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

# File Name:        pathfinder_rel.py
# Version:          0.4.5
# Created:          2024-01-19
# Modified:         2024-08-31

# ========================================================================== #
# This section imports the necessary modules.
# ========================================================================== #

import os
import sys

# ========================================================================== #
# This section locates the running script and relative paths.
# ========================================================================== #

class rel_path_info:

    def __init__(self, script_name):
        """
        Initializes the rel_path_info object with the path to
        the running script which defines related directories.

        Args:
            script_name (str): The name of the running script.

        Attributes:
            script_name (str): The name of the running script.

            rel_path_to_this_script (str): The relative path to the directory of the running script.

            rel_script_dir (str): The relative directory of the running script.

            rel_parent_dir (str): The relative parent directory of the running script.

            rel_config_dir (str): The relative directory where configuration files are stored.

            rel_scripts_dir (str): The relative directory where other scripts are stored.

            rel_modules_dir (str): The relative directory where classes and functions are stored.

            rel_classes_dir (str): The relative directory where classes are stored.

            rel_functions_dir (str): The relative directory where functions are stored.

            rel_version_dir (str): The relative directory where version information is stored.

        """

        # Get the directory of the calling script
        caller_dir = os.path.dirname(
            os.path.abspath(
                script_name
            )
        )

        self.script_name = script_name

        self.rel_path_to_this_script = caller_dir

        self.rel_script_dir = os.path.relpath(
            os.path.dirname(script_name), os.getcwd()
        )

        self.rel_parent_dir = os.path.relpath(
            os.path.dirname(self.rel_script_dir), os.getcwd()
        )

        self.rel_config_dir = os.path.relpath(
            os.path.join(self.rel_parent_dir,
                         "config"),
                         os.getcwd()
        )

        self.rel_scripts_dir = os.path.relpath(
            os.path.join(self.rel_parent_dir,
                         "scripts"),
                         os.getcwd()
        )

        self.rel_modules_dir = os.path.relpath(
            os.path.join(self.rel_scripts_dir,
                         "modules"),
                         os.getcwd()
        )

        self.rel_classes_dir = os.path.relpath(
            os.path.join(self.rel_modules_dir,
                         "classes"),
                         os.getcwd()
        )

        self.rel_functions_dir = os.path.relpath(
            os.path.join(self.rel_modules_dir,
                         "functions"),
                         os.getcwd()
        )

        self.rel_version_dir = os.path.relpath(
            os.path.join(self.rel_parent_dir,
                         "version"),
                         os.getcwd()
        )

    # ---------------------------------------------------------------------- #

    def print_relative_paths(self):
        """
        Prints out the relative paths of the running script and related directories.
        """

        print("Relative path to this script:",
              os.path.basename(self.rel_path_to_this_script)
        )
        print("Relative script directory:   ",
              os.path.basename(self.rel_script_dir)
        )
        print("Relative parent directory:   ",
              os.path.basename(self.rel_parent_dir)
        )
        print("Relative config directory:   ",
              os.path.basename(self.rel_config_dir)
        )
        print("Relative scripts directory:  ",
              os.path.basename(self.rel_scripts_dir)
        )
        print("Relative classes directory:  ",
              os.path.basename(self.rel_classes_dir)
        )
        print("Relative functions directory:",
              os.path.basename(self.rel_functions_dir)
        )
        print("Relative version directory:  ",
              os.path.basename(self.rel_version_dir)
        )

# ========================================================================== #
# This section defines how to handle the main script function.
# ========================================================================== #

# Example usage:
if __name__ == "__main__":
    # Pass the calling script's __file__ attribute
    rel_script_directories = rel_path_info(sys.argv[0])
    rel_script_directories.print_relative_paths()

# ========================================================================== #
# C2 A9 32 30 32 34 2D 4D 41 4E 2D 4D 41 44 45 2D 4D 45 4B 41 4E 59 5A 4D 53 #
# ========================================================================== #

# -------------------------------------------------------------------------- #

# Disclaimer:       This program is part of LOGIK-PROJEKT.
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

# -------------------------------------------------------------------------- #
# Changelist:

# -------------------------------------------------------------------------- #
# version:               0.0.5
# modified:              2024-05-12 - 15:37:50
# comments:              Added function to read directories from JSON files.
# -------------------------------------------------------------------------- #
# version:               0.0.6
# modified:              2024-05-12 - 18:16:05
# comments:              Added a 'separators' function and tested in flame 2025.
# -------------------------------------------------------------------------- #
# version:               0.0.7
# modified:              2024-05-14 - 16:30:58
# comments:              Minor reformatting.
# -------------------------------------------------------------------------- #
# version:               0.0.8
# modified:              2024-05-14 - 16:31:23
# comments:              Changed object_colors from python to JSON.
# -------------------------------------------------------------------------- #
# version:               0.0.9
# modified:              2024-05-14 - 16:31:47
# comments:              Tested in flame 2025.
# -------------------------------------------------------------------------- #
# version:               0.1.0
# modified:              2024-05-14 - 16:46:55
# comments:              Production tested in flame 2025.
# -------------------------------------------------------------------------- #
# version:               0.2.0
# modified:              2024-05-14 - 18:05:26
# comments:              Prepped for obsolete code removal. Tested in flame 2025
# -------------------------------------------------------------------------- #
# version:               0.3.0
# modified:              2024-05-14 - 19:27:33
# comments:              Restored 'object_colors' from python function.
# -------------------------------------------------------------------------- #
# version:               0.3.1
# modified:              2024-05-15 - 07:55:47
# comments:              Renamed 'classes_and_functions' dir to 'modules'.
# -------------------------------------------------------------------------- #
# version:               0.4.1
# modified:              2024-05-18 - 18:01:29
# comments:              Added GNU GPLv3 Disclaimer.
# -------------------------------------------------------------------------- #
# version:               0.4.2
# modified:              2024-05-18 - 18:46:51
# comments:              Minor modification to Disclaimer.
# -------------------------------------------------------------------------- #
# version:               0.4.3
# modified:              2024-06-03 - 10:32:22
# comments:              Moved import flame statement to each function
# -------------------------------------------------------------------------- #
# version:               0.4.4
# modified:              2024-06-12 - 12:21:22
# comments:              Restored import flame statement to top of script.
# -------------------------------------------------------------------------- #
# version:               0.4.5
# modified:              2024-08-31 - 18:40:12
# comments:              prep for release.
# -------------------------------------------------------------------------- #
