#

# -------------------------------------------------------------------------- #

# File Name:        create_nuke_scripts.py
# Version:          2.2.7
# Created:          2024-01-19
# Modified:         2024-08-31

# ========================================================================== #
# This section imports the necessary modules.
# ========================================================================== #

import os
import sys
import fileinput
import datetime
from typing import (
    Union,
    List,
    Dict,
    Optional,
    Callable
)
import xml.etree.ElementTree as ET

from PySide6 import (
    QtWidgets,
    QtCore,
    QtGui
)

import flame

# Get the project root directory (which is two levels up from this script)
project_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Add the project root to sys.path to allow for absolute imports
if project_root not in sys.path:
    sys.path.insert(0, project_root)

# ========================================================================== #
# This section enables debugging.
# ========================================================================== #

# Initiate script logging for debugging
from src.core.functions.log.debugging_and_logging import (
    setup_logging as setup_logging
)

# ========================================================================== #
# This section defines the logik projekt job structure.
# ========================================================================== #

# Define function to define job structure
from src.core.functions.define.define_job_structure import (
    define_job_structure as define_job_structure
)

# ========================================================================== #
# This section gathers information about logik projekt shots.
# ========================================================================== #

# Define function to list shot directories
from src.core.functions.list.list_shots_dir import (
    list_shots_dir as list_shots_dir
)

# -------------------------------------------------------------------------- #

# Define function to define shot structure
from src.core.functions.define.define_shot_structure import (
    define_shot_structure as define_shot_structure
)

# -------------------------------------------------------------------------- #

# Define function to list shot sources directory
from src.core.functions.list.list_shot_sources_dir import (
    list_shot_sources_dir as list_shot_sources_dir
)

# -------------------------------------------------------------------------- #

# Define function to list the contents of each shot_source_dir
from src.core.functions.list.list_shot_source_dir import (
    list_shot_source_dir as list_shot_source_dir
)

# -------------------------------------------------------------------------- #

# Define function to recursively search for OpenEXR image sequences
from src.core.functions.path.path_to_shot_source_openexr_sequences import (
    path_to_shot_source_openexr_sequences as path_to_shot_source_openexr_sequences
)

# ========================================================================== #
# This section defines functions to create pattern-based openclip files.
# ========================================================================== #

# Define function to create an openclip output clip for a nuke shot script
from src.core.functions.create.create_openclip_output_clip import (
    create_openclip_output_clip as create_openclip_output_clip
)

# -------------------------------------------------------------------------- #

# Define function to create an openclip segment clip for a nuke source script
from src.core.functions.create.create_openclip_segment_clip import (
    create_openclip_segment_clip as create_openclip_segment_clip
)

# ========================================================================== #
# This section defines functions to create nuke scripts.
# ========================================================================== #

# Define function to create a shot script for nuke based on task
from src.core.functions.create.create_nuke_shot_script import (
    create_nuke_shot_script as create_nuke_shot_script
)

# -------------------------------------------------------------------------- #

# Define function to create a source script
from src.core.functions.create.create_nuke_source_script import (
    create_nuke_source_script as create_nuke_source_script
)

# ========================================================================== #
# This section processes shot information to create files.
# ========================================================================== #

# Define function to process shot information
from src.core.functions.process.process_shot_info_nuke import (
    process_shot_info as process_shot_info
)

# ========================================================================== #
# This section defines the main create_openclips_and_scripts function.
# ========================================================================== #

def create_openclips_and_scripts(*args, **kwargs):

    # Set up debugging
    # pdb.set_trace()

    # Set umask
    os.umask(0)

    # Define paths
    jobs_dir = '/PROJEKTS'

    # Get the current Flame project
    the_current_projekt = flame.projects.current_project

    # Get the project job_name
    the_projekt_job_name = the_current_projekt.nickname

    # Define the job root directory
    job_root = os.path.join(jobs_dir, the_projekt_job_name)

    # # Testing
    # job_root = "/PROJEKTS/dry_run_01"

    # Setup logging
    logger = setup_logging()

    # Define job structure using the function
    job_structure = define_job_structure(job_root)
    logger.info("Job structure defined.")

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

    # Process shot information
    process_shot_info(job_structure,
                      app_name,
                      task_types_list,
                      start_frame_min,
                      end_frame_max)

# ========================================================================== #
# This section defines the flame menu entries.
# ========================================================================== #


def get_main_menu_custom_ui_actions():
    print("\n" + "="*80)
    print("DEBUG: get_main_menu_custom_ui_actions() called")
    print("="*80)
    
    menu_structure = [
        {
            'name': 'logik-projekt',
            'hierarchy': [],
            'actions': []
        },
        {
            'name': 'configure',
            'hierarchy': ['logik-projekt'],
            'order': 0,
            'actions': []
        },
        {
            'name': 'foundry',
            'hierarchy': ['logik-projekt', 'configure'],
            'order': 0,
            'separator': 'below',
            'actions': [
                {
                    'name': 'nuke scripts',
                    'order': 0,
                    'isVisible': lambda sel: True,
                    'execute': create_openclips_and_scripts,
                    'minimumVersion': '2025'
                }
            ]
        }
    ]
    
    print("DEBUG: Menu structure with hierarchy approach")
    for i, item in enumerate(menu_structure):
        print(
            f"  [{i}] name='{item.get('name')}', "
            f"hierarchy={item.get('hierarchy', 'N/A')}"
        )
    print("="*80 + "\n")
    
    return menu_structure


# -------------------------------------------------------------------------- #


def get_media_panel_custom_ui_actions():
    print("\n" + "="*80)
    print("DEBUG: get_media_panel_custom_ui_actions() called")
    print("="*80)
    
    menu_structure = [
        {
            'name': 'logik-projekt',
            'hierarchy': [],
            'actions': []
        },
        {
            'name': 'export',
            'hierarchy': ['logik-projekt'],
            'order': 0,
            'actions': []
        },
        {
            'name': 'foundry',
            'hierarchy': ['logik-projekt', 'export'],
            'order': 0,
            'separator': 'below',
            'actions': [
                {
                    'name': 'nuke scripts',
                    'order': 0,
                    'separator': 'below',
                    # 'isVisible': scope_clip,
                    'execute': create_openclips_and_scripts,
                    'minimumVersion': '2025'
                }
            ]
        }
    ]
    
    print("DEBUG: Menu structure with hierarchy approach")
    for i, item in enumerate(menu_structure):
        print(
            f"  [{i}] name='{item.get('name')}', "
            f"hierarchy={item.get('hierarchy', 'N/A')}"
        )
    print("="*80 + "\n")
    
    return menu_structure


# ========================================================================== #
# This section defines how to handle the main script function.
# ========================================================================== #

# If this script is executed as main:
# Call functions for immediate execution
if __name__ == "__main__":
    create_openclips_and_scripts()

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