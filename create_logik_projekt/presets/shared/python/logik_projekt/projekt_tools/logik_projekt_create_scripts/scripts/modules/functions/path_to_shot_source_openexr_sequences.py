# filename: path_to_shot_source_openexr_sequences.py

'''
# -------------------------------------------------------------------------- #

# File Name:        path_to_shot_source_openexr_sequences.py
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

# import flame
import os
# import pdb; pdb.set_trace()
# import re
# import fileinput
# import logging
# from datetime import datetime

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
