#

# -------------------------------------------------------------------------- #

# File Name:        create_nuke_source_script.py
# Version:          2.2.9
# Created:          2024-01-19
# Modified:         2024-11-09

# ========================================================================== #
# This section imports the necessary modules.
# ========================================================================== #

import os
import fileinput
from pathlib import Path
# import logging

# ========================================================================== #
# This section defines functions to create nuke scripts.
# ========================================================================== #

def create_nuke_source_script(shot_name,
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
    Modifies a Nuke shot script to set its frame range and append a Read node
    for a specific source.

    Parameters:
        shot_name (str): The name of the shot.
        shots_dir (str): The directory where shots are stored.
        shot_sources_dir (str): The directory for shot sources.
        shot_source_dir (str): The directory for the specific shot source.
        app_name (str): The name of the application ('nuke').
        task_type (str): The type of task (e.g., 'comp').
        version_name (str): The name of the version (e.g., 'v0000').
        shot_scripts_dir (str): The directory for shot scripts.
        shot_source_version_openexr_sequences_info (list): Info about OpenEXR sequences.
        shot_source_version_start_frame (int): Start frame of the source.
        shot_source_version_end_frame (int): End frame of the source.
    """

    # Define the path to the main shot script
    shot_scripts_app_task_dir = os.path.join(shots_dir,
                                             shot_scripts_dir,
                                             app_name,
                                             'shot',
                                             task_type)
    shot_scripts_app_task_file = f"{shot_name}_{app_name}_{task_type}_{version_name}.nk"
    shot_scripts_app_task_path = os.path.join(shot_scripts_app_task_dir,
                                              shot_scripts_app_task_file)

    # Set the frame range in the main shot script
    with fileinput.FileInput(shot_scripts_app_task_path, inplace=True) as file:
        for line in file:
            line = line.replace('NUKE_START_FRAME', str(shot_source_version_start_frame))
            line = line.replace('NUKE_END_FRAME', str(shot_source_version_end_frame))
            print(line, end='')

    # Define the path to the Read node template
    template_path = os.path.abspath(os.path.join(
        os.path.dirname(__file__),
        '..', '..', '..', '..', 'cfg', 'templates', 'foundry', 'nuke', 'nuke_read_node.nk.template'
    ))

    with open(template_path, 'r') as f:
        template_content = f.read()

    # Get the sequence directory from the info list. Assuming the first entry is desired.
    sequence_dir = ""
    if shot_source_version_openexr_sequences_info:
        sequence_dir = shot_source_version_openexr_sequences_info[0].get('shot_source_version_sequence_dir', '')


    # Replace placeholders in the Read node template
    content = template_content.replace('@@SHOT_SOURCE_VERSION_SEQUENCE_DIR@@', sequence_dir)
    content = content.replace('@@SHOT_SOURCE_VERSION_START_FRAME@@', str(shot_source_version_start_frame))
    content = content.replace('@@SHOT_SOURCE_VERSION_END_FRAME@@', str(shot_source_version_end_frame))
    content = content.replace('@@SHOT_SOURCE_DIR@@', shot_source_dir)
    content = content.replace('@@TASK_TYPE@@', task_type)
    content = content.replace('@@VERSION_NAME@@', version_name)

    # Append the configured Read node to the main shot script
    with open(shot_scripts_app_task_path, 'a') as nuke_shot_script_file:
        nuke_shot_script_file.write(content)

    # # This section is for logging purposes
    # logging.debug(f"Nuke script appended for:  {shot_name}_{app_name}_{task_type}_{version_name}")

    print(f"Read node appended to: {shot_scripts_app_task_file}\n")


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
