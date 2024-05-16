# filename: path_to_shot_source_openexr_sequences.py

# -------------------------------------------------------------------------- #

# File Name:        path_to_shot_source_openexr_sequences.py
# Version:          2.1.2
# Language:         python script
# Flame Version:    2025.x
# Author:           Phil MAN - phil_man@mac.com
# Toolset:          MAN_MADE_MATERIAL: LOGIK-PROJEKT
# Created:          2024-04-20
# Modified:         2024-05-15
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
# from datetime import datetime

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
# from create_nuke_shot_script import (
#     create_nuke_shot_script as create_nuke_shot_script 
# )
# from create_nuke_source_script import (
#     create_nuke_source_script as create_nuke_source_script 
# )
# from process_shot_info import (
#     process_shot_info as process_shot_info
# )

# ========================================================================== #
# This section gathers information about logik projekt shots.
# ========================================================================== #

# Define function to recursively search for OpenEXR image sequences
def path_to_shot_source_openexr_sequences(directory, 
                                          start_frame_min, 
                                          end_frame_max):
    """
    Recursively search for OpenEXR image sequences.

    Parameters:
    directory (str): The directory to search in.
    start_frame_min (int): Minimum frame number of the sequence.
    end_frame_max (int): Maximum frame number of the sequence.

    Returns:
    tuple: A tuple containing information about OpenEXR sequences found,
           start frame number, and end frame number.
    """

    # # This section is for logging purposes
    # logging.info(f"Searching for OpenEXR image sequences in {directory}...")

    shot_source_version_openexr_sequences_info = []
    shot_source_version_start_frame = None
    shot_source_version_end_frame = None
    shot_source_openexr_files_list = []

    # Recursively search for OpenEXR files
    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.lower().endswith('.exr'):
                shot_source_openexr_files_list.append(os.path.join(root, file))

    shot_source_openexr_files_list.sort()

    # Process each OpenEXR file
    for shot_source_version_openexr_file in shot_source_openexr_files_list:
        shot_source_version_openexr_path = shot_source_version_openexr_file
        shot_source_version_openexr_filename = os.path.basename(shot_source_version_openexr_file)
        shot_source_version_openexr_frame_number = int(shot_source_version_openexr_filename.split('.')[1])

        # Extract prefix from the filename
        shot_source_version_openexr_filename_parts = shot_source_version_openexr_filename.split('.')
        shot_source_version_filename_prefix = '.'.join(shot_source_version_openexr_filename_parts[:-2])
        shot_source_version_openexr_filename_suffix = shot_source_version_openexr_filename_parts[-1]

        shot_source_version_sequence_dir = os.path.dirname(shot_source_version_openexr_file)

        # Update start and end frame numbers
        if shot_source_version_start_frame is None:
            shot_source_version_start_frame = shot_source_version_openexr_frame_number
            shot_source_version_end_frame = shot_source_version_openexr_frame_number
        else:
            shot_source_version_start_frame = min(shot_source_version_openexr_frame_number, shot_source_version_start_frame)
            shot_source_version_end_frame = max(shot_source_version_openexr_frame_number, shot_source_version_end_frame)

        start_frame_min = min(start_frame_min, shot_source_version_start_frame)
        end_frame_max = max(end_frame_max, shot_source_version_end_frame)

        # Append information to the list
        shot_source_version_openexr_sequences_info.append({
            'shot_source_version_openexr_path': shot_source_version_openexr_path,
            'shot_source_version_sequence_dir': shot_source_version_sequence_dir,
            'shot_source_version_filename_prefix': shot_source_version_filename_prefix,
            'shot_source_version_openexr_frame_number': shot_source_version_openexr_frame_number,
            'shot_source_version_openexr_filename_suffix': shot_source_version_openexr_filename_suffix,
        })

    return shot_source_version_openexr_sequences_info, shot_source_version_start_frame, shot_source_version_end_frame

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
# -------------------------------------------------------------------------- #
# version:               2.1.2
# modified:              2024-05-15 - 12:35:57
# comments:              Renamed nuke script functions and started blender tools.
