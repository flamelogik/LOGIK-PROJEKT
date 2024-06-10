# filename: create_nuke_scripts.py

'''
# -------------------------------------------------------------------------- #

# File Name:        create_nuke_script.py
# Version:          2.2.6
# Language:         python script
# Flame Version:    2025.x
# Author:           Phil MAN - phil_man@mac.com
# Toolset:          MAN_MADE_MATERIAL: LOGIK-PROJEKT
# Created:          2024-04-20
# Modified:         2024-06-10
# Modifier:         Phil MAN - phil_man@mac.com

# Description:      This program scans the logik projekt shots directory
#                   and creates nuke scripts and pattern based openclips.

# Installation:     Copy the 'LOGIK-PROJEKT' repo to your GitHub directory,
#                   e.g. '/home/$USER/workspace/GitHub'

# Changelist:       The full changelist is at the end of this document.

# -------------------------------------------------------------------------- #
'''

# ========================================================================== #
# This section imports the necessary modules.
# ========================================================================== #

import flame
import os
# import pdb; pdb.set_trace() 
# import re
import fileinput
# import logging
from datetime import datetime

# ========================================================================== #
# This section imports the external classes.
# ========================================================================== #

# # EXAMPLE:
# from modules.classes.example import (
#     example_function as new_function_name
# )

# ========================================================================== #
# This EXAMPLE demonstrates how to imports the external functions.
# ========================================================================== #

# # EXAMPLE:
# from modules.functions.example import (
#     example_function as new_function_name
# )

# ========================================================================== #
# This section enables debugging.
# ========================================================================== #

# # Initiate script logging for debugging
# from modules.functions.debugging_and_logging import (
#     debugging_and_logging as debugging_and_logging 
# )

'''def setup_logging(*args, **kwargs):
    script_path = os.path.abspath(__file__)
    script_name = os.path.basename(script_path)
    script_name_without_extension = os.path.splitext(script_name)[0]
    script_directory = os.path.dirname(script_path)
    log_directory = os.path.join(script_directory, 'log')

    if not os.path.exists(log_directory):
        os.makedirs(log_directory)

    log_filename = f"{datetime.now().strftime('%Y-%m-%d-%H-%M')}_{script_name}.debug.log"
    log_filepath = os.path.join(log_directory, log_filename)
    print("Log filepath:", log_filepath)  # Add this line for debugging
    logging.basicConfig(filename=log_filepath, level=logging.DEBUG, *args, **kwargs)
'''

# ========================================================================== #
# This section defines the logik projekt job structure.
# ========================================================================== #

# Define function to define job structure
from modules.functions.define_job_structure import (
    define_job_structure as define_job_structure 
)

# ========================================================================== #
# This section gathers information about logik projekt shots.
# ========================================================================== #

# Define function to list shot directories
from modules.functions.list_shots_dir import (
    list_shots_dir as list_shots_dir 
)

# -------------------------------------------------------------------------- #

# Define function to define shot structure
from modules.functions.define_shot_structure import (
    define_shot_structure as define_shot_structure 
)

# -------------------------------------------------------------------------- #

# Define function to list shot sources directory
from modules.functions.list_shot_sources_dir import (
    list_shot_sources_dir as list_shot_sources_dir 
)

# -------------------------------------------------------------------------- #

# Define function to list the contents of each shot_source_dir
from modules.functions.list_shot_source_dir import (
    list_shot_source_dir as list_shot_source_dir 
)

# -------------------------------------------------------------------------- #

# Define function to recursively search for OpenEXR image sequences
from modules.functions.path_to_shot_source_openexr_sequences import (
    path_to_shot_source_openexr_sequences as path_to_shot_source_openexr_sequences 
)

# ========================================================================== #
# This section defines functions to create pattern-based openclip files.
# ========================================================================== #

# Define function to create an openclip output clip for a nuke shot script
from modules.functions.create_openclip_output_clip import (
    create_openclip_output_clip as create_openclip_output_clip 
)

# -------------------------------------------------------------------------- #

# Define function to create an openclip segment clip for a nuke source script
from modules.functions.create_openclip_segment_clip import (
    create_openclip_segment_clip as create_openclip_segment_clip 
)

# ========================================================================== #
# This section defines functions to create nuke scripts.
# ========================================================================== #

# Define function to create a shot script for nuke based on task
from modules.functions.create_nuke_shot_script import (
    create_nuke_shot_script as create_nuke_shot_script 
)

# -------------------------------------------------------------------------- #

# Define function to create a source script
from modules.functions.create_nuke_source_script import (
    create_nuke_source_script as create_nuke_source_script 
)

# ========================================================================== #
# This section processes shot information to create files.
# ========================================================================== #

# Define function to process shot information
from modules.functions.process_shot_info_nuke import (
    process_shot_info as process_shot_info
)

# ========================================================================== #
# This section defines the main create_openclips_and_scripts function.
# ========================================================================== #

def create_openclips_and_scripts(*args, **kwargs):

    # Set up debugging
    # pdb.set_trace()

    # Here are some common debugger commands:

    # n or next: Execute the current line and move to the next line.
    # s or step: Execute the current line and step into any function calls on that line.
    # c or continue: Continue execution until the next breakpoint or until the end of the script.
    # p or print: Print the value of a variable.
    # l or list: Show the current line and a few lines of code around it.

    # You can find more information about using pdb in the
    # Python documentation:
    # https://docs.python.org/3/library/pdb.html

    # Set umask
    os.umask(0)

    # Define paths
    jobs_dir = '/JOBS'

    import flame

    # Get the current Flame project
    the_current_projekt = flame.projects.current_project

    # Get the project job_name
    the_projekt_job_name = the_current_projekt.nickname

    # Define the job root directory
    job_root = os.path.join(jobs_dir, the_projekt_job_name)

    # # Testing
    # job_root = "/JOBS/dry_run_01"

    # # Setup logging
    # setup_logging()

    # Define job structure using the function
    job_structure = define_job_structure(job_root)
    # logging.info("Job structure defined.")

    # Define app_name and task_types_list
    app_name = "nuke"
    task_types_list = (
        "color",
        "comp",
        "paint",
        "precomp",
        "roto"
    )

    # Initialize start_frame_min with positive infinity
    # and end_frame_max with negative infinity
    start_frame_min = float('inf')
    end_frame_max = float('-inf')

    # Define a function to print variables
    # def print_variables():
        # logging.info("Printing variables:")
        # for key, value in job_structure.items():
        #     logging.info(f"{key}: {value}")

    # Call the function to print variables
    # print_variables()

    # Process shot information
    process_shot_info(job_structure, 
                      app_name, 
                      task_types_list, 
                      start_frame_min, 
                      end_frame_max)

# ========================================================================== #
# This section defines the flame menu entries.
# ========================================================================== #

# Add custom UI actions
def get_main_menu_custom_ui_actions():

    return [
        {
            'name': 'logik-projekt',
            'hierarchy': [],
            'actions': []
        },
        {
            'name': 'create',
            'hierarchy': ['logik-projekt'],
            'order': 6,
            'actions': [
                {
                    'name': 'nuke scripts',
                    'execute': create_openclips_and_scripts,
                    'minimumVersion': '2025'
                }
            ]
        }
    ]

# -------------------------------------------------------------------------- #

# def get_mediahub_files_custom_ui_actions():

#     return [
#         {
#             'name': 'create',
#             'hierarchy': ['logik-projekt'],
#             'order': 5,
#             'actions': [
#                 {
#                     'name': 'nuke scripts',
#                     'execute': create_openclips_and_scripts,
#                     'minimumVersion': '2025'
#                 }
#             ]
#         }
#     ]

# -------------------------------------------------------------------------- #

def get_media_panel_custom_ui_actions():

    return [
        {
            'name': 'create',
            'hierarchy': ['logik-projekt'],
            'order': 6,
            'actions': [
                {
                    'name': 'nuke scripts',
                    'order': 6,
                    'separator': 'below',
                    'execute': create_openclips_and_scripts,
                    'minimumVersion': '2025'
                }
            ]
        }
    ]

# ========================================================================== #
# This section defines how to handle the main script function.
# ========================================================================== #

# If this script is executed as main:
# Call functions for immediate execution
if __name__ == "__main__":
    create_openclips_and_scripts()

# ========================================================================== #
# C2 A9 32 30 32 34 2D 4D 41 4E 5F 4D 41 44 45 2D 4D 45 4B 41 4E 49 53 4D 5A #
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
# version:               0.0.1
# modified:              2024-05-03 - 01:50:36
# comments:              Basic functionality defined and tested
# -------------------------------------------------------------------------- #
# version:               0.0.2
# modified:              2024-05-03 - 02:12:19
# comments:              Fixed some formatting and flame menus
# -------------------------------------------------------------------------- #
# version:               0.0.3
# modified:              2024-05-03 - 11:25:42
# comments:              Changed 'the_current_project' to 'the_current_projekt'
# -------------------------------------------------------------------------- #
# version:               0.0.4
# modified:              2024-05-03 - 11:38:31
# comments:              Standardizd 'logik-projekt' menu entries
# -------------------------------------------------------------------------- #
# version:               0.0.5
# modified:              2024-05-03 - 12:29:29
# comments:              Restored '_{version_name}' in script construction
# -------------------------------------------------------------------------- #
# version:               0.0.6
# modified:              2024-05-03 - 13:37:01
# comments:              Added validation for file existence
# -------------------------------------------------------------------------- #
# version:               1.0.0
# modified:              2024-05-06 - 14:35:57
# comments:              Complete re-write - tested on Lucid Link
# -------------------------------------------------------------------------- #
# version:               1.0.1
# modified:              2024-05-06 - 16:12:00
# comments:              Minor reformatting
# -------------------------------------------------------------------------- #
# version:               1.0.2
# modified:              2024-05-06 - 16:24:36
# comments:              added printf statements at logging.debug points
# -------------------------------------------------------------------------- #
# version:               1.0.3
# modified:              2024-05-06 - 17:02:53
# comments:              Added (*args, **kwargs) to main function
# -------------------------------------------------------------------------- #
# version:               1.0.4
# modified:              2024-05-06 - 21:50:39
# comments:              Updated docstrings, comments and formatting
# -------------------------------------------------------------------------- #
# version:               1.0.5
# modified:              2024-05-06 - 22:14:47
# comments:              Corrected Write node file path for Nuke Shot script.
# -------------------------------------------------------------------------- #
# version:               1.0.6
# modified:              2024-05-10 - 09:39:33
# comments:              Enabled production job_dir and disabled test job_dir
# -------------------------------------------------------------------------- #
# version:               2.0.0
# modified:              2024-05-10 - 21:14:44
# comments:              Refactored monolithic code and tested in flame 2025
# -------------------------------------------------------------------------- #
# version:               2.0.1
# modified:              2024-05-10 - 21:45:10
# comments:              Modified docstrings and formatting.
# -------------------------------------------------------------------------- #
# version:               2.0.2
# modified:              2024-05-14 - 12:53:36
# comments:              Renamed 'classes_and_functions' directory to 'modules'.
# -------------------------------------------------------------------------- #
# version:               2.1.2
# modified:              2024-05-15 - 12:35:57
# comments:              Renamed nuke script functions and started blender tools.
# -------------------------------------------------------------------------- #
# version:               2.2.2
# modified:              2024-05-18 - 18:00:56
# comments:              Added GNU GPLv3 Disclaimer.
# -------------------------------------------------------------------------- #
# version:               2.2.3
# modified:              2024-05-18 - 18:46:27
# comments:              Minor modification to Disclaimer.
# -------------------------------------------------------------------------- #
# version:               2.2.4
# modified:              2024-06-08 - 08:47:53
# comments:              Removed unused code and prep for after effects scripts.
# -------------------------------------------------------------------------- #
# version:               2.2.5
# modified:              2024-06-09 - 11:27:00
# comments:              Added After Effects script/openclip generators
# -------------------------------------------------------------------------- #
# version:               2.2.6
# modified:              2024-06-10 - 06:59:38
# comments:              Removed some double quotes from After Effects templates
