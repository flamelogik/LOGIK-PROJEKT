#

# -------------------------------------------------------------------------- #

# File Name:        process_shot_info_after_effects.py
# Version:          2.2.7
# Created:          2024-01-19
# Modified:         2024-08-31

# ========================================================================== #
# This section imports the necessary modules.
# ========================================================================== #

import os
import sys

# Get the project root directory (which is four levels up from this script)
project_root = os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))

# Add the project root to sys.path to allow for absolute imports
if project_root not in sys.path:
    sys.path.insert(0, project_root)

# ========================================================================== #
# This section imports the external functions.
# ========================================================================== #

from src.core.functions.define.define_job_structure import (
    define_job_structure as define_job_structure
)
from src.core.functions.list.list_shots_dir import (
    list_shots_dir as list_shots_dir
)
from src.core.functions.define.define_shot_structure import (
    define_shot_structure as define_shot_structure
)
from src.core.functions.list.list_shot_sources_dir import (
    list_shot_sources_dir as list_shot_sources_dir
)
from src.core.functions.list.list_shot_source_dir import (
    list_shot_source_dir as list_shot_source_dir
)
from src.core.functions.path.path_to_shot_source_openexr_sequences import (
    path_to_shot_source_openexr_sequences as path_to_shot_source_openexr_sequences
)
from src.core.functions.create.create_openclip_output_clip import (
    create_openclip_output_clip as create_openclip_output_clip
)
from src.core.functions.create.create_openclip_segment_clip import (
    create_openclip_segment_clip as create_openclip_segment_clip
)
from src.core.functions.create.create_after_effects_shot_script import (
    create_after_effects_shot_script as create_after_effects_shot_script
)
from src.core.functions.create.create_after_effects_source_script import (
    create_after_effects_source_script as create_after_effects_source_script
)

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
          
            # Create After Effects shot script
            create_after_effects_shot_script(
                shot_name,
                app_name,
                task_type,
                version_name,
                shots_dir,
                shot_structure["shot_renders_dir"],
                shot_structure["shot_scripts_dir"],
                shot_structure["shot_sources_dir"],
                shot_dir, # shot_source_dir
                1001, # shot_source_version_start_frame
                [], # shot_source_version_openexr_sequences_info
                1100, # shot_source_version_end_frame
            )

            # Construct the correct path for listing source directories
            shot_sources_dir = os.path.join(shots_dir,
                                            shot_structure["shot_sources_dir"])

            # List source directories
            shot_sources_dir_list = list_shot_sources_dir(shot_sources_dir)

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
                    # Create openclip segment clip
                    create_openclip_segment_clip(shot_source_dir,
                                                 app_name,
                                                 task_type,
                                                 shots_dir,
                                                 shot_dir,
                                                 shot_structure["shot_segment_clips_app_dir"])

                    # Create After Effects source script for the shot
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

# ========================================================================== #
# C2 A9 32 30 32 34 2D 4D 41 4E 2D 4D 41 44 45 2D 4D 45 4B 41 4E 59 5A 4D 53 #
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
# -------------------------------------------------------------------------- #
# version:               2.2.7
# modified:              2024-08-31 - 19:04:02
# comments:              prep for release.
# -------------------------------------------------------------------------- #