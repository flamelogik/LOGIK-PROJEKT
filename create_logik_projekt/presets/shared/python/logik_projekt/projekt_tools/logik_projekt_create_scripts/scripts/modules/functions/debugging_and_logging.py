# filename: debugging_and_logging.py

# -------------------------------------------------------------------------- #

# File Name:        debugging_and_logging.py
# Version:          2.0.2
# Language:         python script
# Flame Version:    2025.x
# Author:           Phil MAN - phil_man@mac.com
# Toolset:          MAN_MADE_MATERIAL: LOGIK-PROJEKT
# Created:          2024-04-20
# Modified:         2024-05-14
# Modifier:         Phil MAN - phil_man@mac.com

# Description:      This program scans the logik projekt shots directory
#                   and creates nuke scripts and pattern based openclips.

# Installation:     Copy the 'LOGIK-PROJEKT' repo to your GitHub directory,
#                   e.g. '/home/$USER/workspace/GitHub'

# Changelist:       The full changelist is at the end of this document.

# -------------------------------------------------------------------------- #

# ========================================================================== #
# This section imports the necessary modules.
# ========================================================================== #

# import flame
import os
# import pdb; pdb.set_trace()
# import re
# import fileinput
# import logging
from datetime import datetime

# ========================================================================== #
# This section imports the external functions.
# ========================================================================== #

# # EXAMPLE:
# from modules.functions.example import (
#     example_function as new_function_name
# )

# from debugging_and_logging import (
#     debugging_and_logging as debugging_and_logging 
# )
# from define_job_structure import (
#     define_job_structure as define_job_structure 
# )
# from list_shots_dir import (
#     list_shots_dir as list_shots_dir 
# )
# from define_shot_structure import (
#     define_shot_structure as define_shot_structure 
# )
# from list_shot_sources_dir import (
#     list_shot_sources_dir as list_shot_sources_dir 
# )
# from list_shot_source_dir import (
#     list_shot_source_dir as list_shot_source_dir 
# )
# from path_to_shot_source_openexr_sequences import (
#     path_to_shot_source_openexr_sequences as path_to_shot_source_openexr_sequences 
# )
# from create_openclip_output_clip import (
#     create_openclip_output_clip as create_openclip_output_clip 
# )
# from create_openclip_segment_clip import (
#     create_openclip_segment_clip as create_openclip_segment_clip 
# )
# from create_shot_script import (
#     create_shot_script as create_shot_script 
# )
# from create_source_script import (
#     create_source_script as create_source_script 
# )
# from process_shot_info import (
#     process_shot_info as process_shot_info
# )

# ========================================================================== #
# This section enables debugging.
# ========================================================================== #

# Initiate script logging for debugging
def setup_logging(*args, **kwargs):
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

# ========================================================================== #
# C2 A9 2D 32 30 32 34 2D 4D 41 4E 5F 4D 41 44 45 5F 4D 41 54 45 52 49 61 4C #
# ========================================================================== #

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
