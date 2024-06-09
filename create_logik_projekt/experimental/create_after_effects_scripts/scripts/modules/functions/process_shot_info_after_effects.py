# filename: process_shot_info_after_effects.py

'''
# -------------------------------------------------------------------------- #

# File Name:        process_shot_info_after_effects.py
# Version:          2.2.4
# Language:         python script
# Flame Version:    2025.x
# Author:           Phil MAN - phil_man@mac.com
# Toolset:          MAN_MADE_MATERIAL: LOGIK-PROJEKT
# Created:          2024-04-20
# Modified:         2024-06-08
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
# This section imports the external classes.
# ========================================================================== #

# # EXAMPLE:
# from modules.classes.example import (
#     example_function as new_function_name
# )

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
from modules.functions.define_job_structure import (
    define_job_structure as define_job_structure 
)
from list_shots_dir import (
    list_shots_dir as list_shots_dir 
)
from define_shot_structure import (
    define_shot_structure as define_shot_structure 
)
from list_shot_sources_dir import (
    list_shot_sources_dir as list_shot_sources_dir 
)
from list_shot_source_dir import (
    list_shot_source_dir as list_shot_source_dir 
)
from path_to_shot_source_openexr_sequences import (
    path_to_shot_source_openexr_sequences as path_to_shot_source_openexr_sequences 
)
from create_openclip_output_clip import (
    create_openclip_output_clip as create_openclip_output_clip 
)
from create_openclip_segment_clip import (
    create_openclip_segment_clip as create_openclip_segment_clip 
)
from create_after_effects_shot_script import (
    create_after_effects_shot_script as create_after_effects_shot_script 
)
from create_after_effects_source_script import (
    create_after_effects_source_script as create_after_effects_source_script 
)
# from process_shot_info import (
#     process_shot_info as process_shot_info
# )

# ========================================================================== #
# This section processes shot information to create files.
# ========================================================================== #

# Define function to process shot information
def process_shot_info(job_structure, 
                      app_name, 
                      task_types_list, 
                      start_frame_min, 
                      end_frame_max):
    """
    Process shot information.

    Parameters:
    job_structure (dict): The structure of the job.
    app_name (str): The name of the application.
    task_types_list (list): List of task types.
    start_frame_min (int): Minimum frame number.
    end_frame_max (int): Maximum frame number.

    Returns:
    None
    """
    # Access shots_dir from job_structure dictionary
    shots_dir = job_structure["shots_dir"]

    # List shot directories and store them in a variable
    shots_dir_list = list_shots_dir(shots_dir)

    # Define shot structures and list sources directories for each shot
    for shot_dir in shots_dir_list:

        # Define shot_name
        shot_name = shot_dir

        # Define version_name
        version_name = "v0000"

        # Iterate over task types list
        for task_type in task_types_list:
            shot_structure = define_shot_structure(shots_dir, 
                                                   shot_dir, 
                                                   app_name, 
                                                   task_type)
            
            # Log shot structure
            # logging.info(f"Shot structure for {shot_dir} ({task_type}): {shot_structure}")

            # # Create openclip output clip
            # create_openclip_output_clip(shot_name, 
            #                             app_name, 
            #                             task_type, 
            #                             shots_dir, 
            #                             shot_structure["shot_output_clips_app_dir"])

            # # Create Nuke script for the shot
            # create_after_effects_shot_script(shot_name, 
            #                    app_name, 
            #                    task_type, 
            #                    version_name, 
            #                    shots_dir, 
            #                    shot_structure["shot_renders_dir"], 
            #                    shot_structure["shot_scripts_dir"])

            # Construct the correct path for listing source directories
            shot_sources_dir = os.path.join(shots_dir, 
                                            shot_structure["shot_sources_dir"])

            # List source directories
            shot_sources_dir_list = list_shot_sources_dir(shot_sources_dir)

            # Log source directories
            # logging.info(f"Source directories for {shot_dir} ({task_type}): {shot_sources_dir_list}")

            # Call path_to_shot_source_openexr_sequences for each source directory
            for shot_source_dir in shot_sources_dir_list:
                shot_source_dir_path = os.path.join(shot_sources_dir, 
                                                    shot_source_dir)
                shot_source_version_openexr_sequences_info, \
                    shot_source_version_start_frame, \
                        shot_source_version_end_frame = path_to_shot_source_openexr_sequences(
                            shot_source_dir_path, 
                            start_frame_min, 
                            end_frame_max)
                
                if shot_source_version_openexr_sequences_info:

                    # logging.info(f"OpenEXR files found in {shot_source_dir_path} ({task_type}):")
                    # for exr_info in shot_source_version_openexr_sequences_info:
                        # logging.info(f" - {exr_info['shot_source_version_openexr_path']} | Prefix: {exr_info['shot_source_version_filename_prefix']}, Frame: {exr_info['shot_source_version_openexr_frame_number']}, Suffix: {exr_info['shot_source_version_openexr_filename_suffix']}, Sequence Dir: {exr_info['shot_source_version_sequence_dir']}")
                    # logging.info(f"Start Frame: {shot_source_version_start_frame}, End Frame: {shot_source_version_end_frame}")

                    # Create openclip segment clip
                    create_openclip_segment_clip(shot_source_dir, 
                                                 app_name, 
                                                 task_type, 
                                                 shots_dir, 
                                                 shot_dir,
                                                 shot_structure["shot_segment_clips_app_dir"])

                    # Create Nuke script for the shot
                    create_after_effects_source_script(shot_name, 
                                         shots_dir, 
                                         shot_sources_dir, 
                                         shot_source_dir, 
                                         app_name, 
                                         task_type, 
                                         version_name, 
                                         shot_structure["shot_scripts_dir"], 
                                         shot_source_version_openexr_sequences_info, 
                                         shot_source_version_start_frame, 
                                         shot_source_version_end_frame)

                # else:

                    # # This section is for logging purposes
                    # logging.info(f"No OpenEXR files found in {shot_source_dir_path} ({task_type})")

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
