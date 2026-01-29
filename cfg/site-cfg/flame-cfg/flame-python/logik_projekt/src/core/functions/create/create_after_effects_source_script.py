#

# -------------------------------------------------------------------------- #

# File Name:        create_after_effects_source_script.py
# Version:          2.2.7
# Created:          2024-01-19
# Modified:         2024-08-31

# ========================================================================== #
# This section imports the necessary modules.
# ========================================================================== #

# import flame
import os
# import pdb; pdb.set_trace()
import re
import fileinput
# import logging
# from datetime import datetime

# ========================================================================== #
# This section defines functions to create after effects scripts.
# ========================================================================== #

# Define function to create a source script
def create_after_effects_source_script(shot_name,
                         shots_dir,
                         shot_sources_dir,
                         shot_source_dir,
                         app_name,
                         task_type,
                         version_name,
                         shot_scripts_dir,
                         shot_source_version_openexr_sequences_info,
                         shot_source_version_start_frame,
                         shot_source_version_end_frame):

    """
    Create a source script for after effects  based on layer and task.

    Parameters:
        shot_name (str): The name of the shot.
        shots_dir (str): The directory where shots are stored.
        shot_sources_dir (str): The directory for shot sources.
        shot_source_dir (str): The directory for shot source.
        app_name (str): The name of the application.
        task_type (str): The type of task.
        version_name (str): The name of the version.
        shot_scripts_dir (str): The directory for shot scripts.
        shot_source_version_openexr_sequences_info (list): Information about OpenEXR sequences.
        shot_source_version_start_frame (int): Start frame number of the source version.
        shot_source_version_end_frame (int): End frame number of the source version.

    Returns:
    None
    """

    # Define the directory for the specific app and task type
    source_scripts_app_task_dir = os.path.join(shots_dir,
                                               shot_scripts_dir,
                                               app_name,
                                               'sources',
                                               task_type)

    # Create the directory if it doesn't exist
    os.makedirs(source_scripts_app_task_dir, exist_ok=True)

    # Define the file path for the script
    source_scripts_app_task_file = f"{shot_source_dir}_{app_name}_{task_type}_{version_name}.aep"
    source_scripts_app_task_file_path = os.path.join(source_scripts_app_task_dir,
                                                source_scripts_app_task_file)
  
    # Define the script path for the script
    source_scripts_app_task_script = f"{shot_source_dir}_{app_name}_{task_type}_{version_name}.jsx"
    source_scripts_app_task_script_path = os.path.join(source_scripts_app_task_dir,
                                                source_scripts_app_task_script)

    # Define the path to the template file.
    # It's constructed relative to this script's location.
    template_path = os.path.abspath(os.path.join(
        os.path.dirname(__file__),
        '..', '..', '..', '..', 'cfg', 'templates', 'adobe', 'after-effects', 'after_effects_source_script.jsx.template'
    ))

    with open(template_path, 'r') as f:
        template_content = f.read()

    # Replace placeholders
    content = template_content.replace('@@SOURCE_SCRIPTS_APP_TASK_SCRIPT@@', source_scripts_app_task_script)
    content = content.replace('@@SHOT_SOURCES_DIR@@', shot_sources_dir)
    content = content.replace('@@SHOT_SOURCE_DIR@@', shot_source_dir)
    content = content.replace('@@APP_NAME@@', app_name)
    content = content.replace('@@TASK_TYPE@@', task_type)
    content = content.replace('@@VERSION_NAME@@', version_name)
    content = content.replace('@@SHOT_SOURCE_VERSION_START_FRAME@@', str(shot_source_version_start_frame))
    content = content.replace('@@SOURCE_SCRIPTS_APP_TASK_FILE_PATH@@', source_scripts_app_task_file_path)

    # Write the After Effects script content to the file
    with open(source_scripts_app_task_script_path, 'w') as f:
        f.write(content)

    # # This section is for logging purposes
    # logging.debug(f"After Effects script created for:  {shot_source_dir}_{version_name}")

    print(f"After Effects Source script created:  {source_scripts_app_task_script}\n")

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
