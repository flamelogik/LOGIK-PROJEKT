# filename: pathfinder_abs.py

'''
# -------------------------------------------------------------------------- #

# Program Name:     pathfinder_abs.py
# Version:          0.2.0
# Language:         python script
# Flame Version:    2025.x
# Author:           Phil MAN - phil_man@mac.com
# Toolset:          MAN_MADE_MATERIAL: LOGIK-PROJEKT
# Created:          2024-04-20
# Modified:         2024-05-14
# Modifier:         Phil MAN - phil_man@mac.com

# Description:      This python script gathers information about the current
#                   running script and related directories.
#                   
#                   This script defines 2 classes which locate the running 
#                   script and related directories, using absolute paths.
#                   
#                   It provides methods to create necessary directories
#                   and print out the paths.

# Installation:     Copy the 'LOGIK-PROJEKT' directory to:
#                   '/opt/Autodesk/shared/python/'

# Changelist:       The full changelist is at the end of this document.

# -------------------------------------------------------------------------- #
'''

# ========================================================================== #
# This section imports required modules.
# ========================================================================== #

import os
import sys

# ========================================================================== #
# This section locates the running script and absolute paths.
# ========================================================================== #

class abs_path_info:
    def __init__(self, script_name):
        """
        Initializes the abs_path_info object with the path to 
        the running script which defines related directories.

        Args:
            script_name (str): The name of the running script.

        Attributes:
            script_name (str): The name of the running script.

            abs_path_to_this_script (str): The absolute path to the directory of the running script.

            abs_script_dir (str): The absolute directory of the running script.

            abs_parent_dir (str): The absolute parent directory of the running script.

            abs_config_dir (str): The absolute directory where configuration files are stored.

            abs_scripts_dir (str): The absolute directory where other scripts are stored.

            abs_classes_and_functions_dir (str): The absolute directory where classes and functions are stored.

            abs_classes_dir (str): The absolute directory where classes are stored.

            abs_functions_dir (str): The absolute directory where functions are stored.

            abs_version_dir (str): The absolute directory where version information is stored.

        """

        # Get the directory of the calling script
        caller_dir = os.path.dirname(
            os.path.abspath(
                script_name
            )
        )
        
        self.script_name = script_name

        self.abs_path_to_this_script = caller_dir

        self.abs_script_dir = os.path.dirname(
            script_name
        )

        self.abs_parent_dir = os.path.dirname(
            self.abs_script_dir
        )

        self.abs_config_dir = os.path.join(
            self.abs_parent_dir, 
            "config"
        )

        self.abs_scripts_dir = os.path.join(
            self.abs_parent_dir, 
            "scripts"
        )

        self.abs_classes_and_functions_dir = os.path.join(
            self.abs_scripts_dir, 
            "classes_and_functions"
        )

        self.abs_classes_dir = os.path.join(
            self.abs_classes_and_functions_dir, 
            "classes"
        )

        self.abs_functions_dir = os.path.join(
            self.abs_classes_and_functions_dir, 
            "functions"
        )

        self.abs_version_dir = os.path.join(
            self.abs_parent_dir, 
            "version"
        )

    # ---------------------------------------------------------------------- #

    def create_directories(self):
        """
        Creates necessary directories if they do not exist.
        """
                
        print("Creating necessary directories...")
        os.makedirs(
            self.abs_classes_and_functions_dir, 
            exist_ok=True
        )

        os.makedirs(
            self.abs_classes_dir, 
            exist_ok=True
        )

        os.makedirs(
            self.abs_functions_dir, 
            exist_ok=True
        )

    # ---------------------------------------------------------------------- #

    def print_absolute_paths(self):
        """
        Prints out the paths of the running script and related directories.
        """

        print("This script:        ", 
              os.path.basename(self.script_name)
        )
        
        print("Path to this script:", 
              os.path.basename(self.abs_path_to_this_script)
        )
        print("Script directory:   ", 
              os.path.basename(self.abs_script_dir)
        )
        print("Parent directory:   ", 
              os.path.basename(self.abs_parent_dir)
        )
        print("Config directory:   ", 
              os.path.basename(self.abs_config_dir)
        )
        print("Scripts directory:  ", 
              os.path.basename(self.abs_scripts_dir)
        )
        print("Classes directory:  ", 
              os.path.basename(self.abs_classes_dir)
        )
        print("Functions directory:", 
              os.path.basename(self.abs_functions_dir)
        )
        print("Version directory:  ", 
              os.path.basename(self.abs_version_dir)
        )

# ========================================================================== #
# This section defines how to handle the main script function.
# ========================================================================== #

# Example usage:
if __name__ == "__main__":
    # Pass the calling script's __file__ attribute
    abs_script_directories = abs_path_info(sys.argv[0])
    abs_script_directories.create_directories()
    abs_script_directories.print_paths()

# ========================================================================== #
# C2 A9 2D 32 30 32 34 2D 4D 41 4E 5F 4D 41 44 45 5F 4D 41 54 45 52 49 61 4C #
# ========================================================================== #

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
