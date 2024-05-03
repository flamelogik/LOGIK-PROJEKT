# filename: create_nuke_scripts.py

# -------------------------------------------------------------------------- #

# File Name:        create_nuke_script.py
# Version:          0.0.2
# Language:         python script
# Flame Version:    2025.x
# Author:           Phil MAN - phil_man@mac.com
# Toolset:          MAN_MADE_MATERIAL: LOGIK-PROJEKT
# Created:          2024-04-20
# Modified:         2024-05-03
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

import flame
import logging
import os
import re

# ========================================================================== #
# This section enables debugging.
# ========================================================================== #

# Set up logging
logging.basicConfig(level=logging.DEBUG, format='%(levelname)s: %(message)s')

# ========================================================================== #
# This section defines the logik projekt, directories and path variables.
# ========================================================================== #

# Get the current Flame project
the_current_projekt = flame.projects.current_project()

# Get the project nickname
the_current_nickname = the_current_projekt.nickname()
# the_current_nickname = "eric_parliament"

# Define paths
jobs_root = '/JOBS'
job_dir = os.path.join(jobs_root, the_current_nickname)
shots_dir = os.path.join(job_dir, 'shots')

# List shot directories
shots_list = os.listdir(shots_dir)

# Count the number of shots
shots_count = len(shots_list)

# Dictionary to store 'renders' and 'sources' directories for each shot
shot_directories = {}

# Iterate over shot directories
for shot_name in shots_list:

    # Define paths for 'renders' and 'sources' directories
    # openclips_dir = os.path.join(shots_dir, shot_name, 'openclip')
    # scripts_dir = os.path.join(shots_dir, shot_name, 'scripts')
    renders_dir = os.path.join(shots_dir, shot_name, 'media', 'renders')
    sources_dir = os.path.join(shots_dir, shot_name, 'media', 'sources')
    
    # Store paths in the dictionary
    shot_directories[shot_name] = {
        # 'openclips': openclips_dir,
        # 'scripts': scripts_dir,
        'renders': renders_dir,
        'sources': sources_dir
    }

# Define Application Names and Tasks directories
app_name = "nuke"

# task_type_array = (
#     "anim", "color", "comp", "fx", "light",
#     "model", "paint", "precomp", "roto", "texture"
# )

task_type_array = (
    "color", "comp", "paint", "precomp", "roto"
)

# Dictionary to store 'renders' and 'sources' directories for each shot
shot_directories = {}

# Iterate over shot directories
for shot_name in os.listdir(shots_dir):
    # Define paths for 'renders' and 'sources' directories
    renders_dir = os.path.join(shots_dir, shot_name, 'media', 'renders')
    sources_dir = os.path.join(shots_dir, shot_name, 'media', 'sources')
    
    # Store paths in the dictionary
    shot_directories[shot_name] = {'renders': renders_dir, 'sources': sources_dir}

# ========================================================================== #
# This section collects metadata.
# ========================================================================== #

# Function to extract source information
def extract_source_info():
    extracted_info = []  # List to store extracted information

    # Iterate over shot directories
    for shot_name, directories in shot_directories.items():
        sources_dir = directories['sources']
        
        # List all directories in sources_dir and sort them
        sources_list = sorted([d for d in os.listdir(sources_dir) if os.path.isdir(os.path.join(sources_dir, d))])
        
        # Iterate over source items
        for source_item in sources_list:
            source_item_path = os.path.join(sources_dir, source_item)
            source_item_recursive_dir = None
            
            # Find openEXR image sequences recursively
            for root, dirs, files in os.walk(source_item_path):
                for file in files:
                    if file.lower().endswith('.exr'):
                        source_item_recursive_dir = root
                        break
                if source_item_recursive_dir:
                    break
            
            # Extract filename, filename prefix, and filename version number from openEXR files
            if source_item_recursive_dir:
                exr_files = [f for f in os.listdir(source_item_recursive_dir) if f.lower().endswith('.exr')]
                exr_files.sort()  # Sort the list of filenames
                
                start_frame, end_frame = float('inf'), float('-inf')  # Initialize with extreme values
                for exr_file in exr_files:
                    frame_number = int(re.search(r'\d{8}', exr_file).group())  # Extract 8-digit frame number from filename
                    start_frame = min(start_frame, frame_number)
                    end_frame = max(end_frame, frame_number)
                    
                    # Extract version number and file prefix
                    filename_prefix_full = exr_file.split('.')[0]
                    version_number = filename_prefix_full.split('_v')[-1]
                    version_name = f"v{version_number}"
                    filename_prefix = filename_prefix_full.rsplit('_', 1)[0]
                    
                    # Append extracted information to the list
                    extracted_info.append((shot_name, source_item_recursive_dir, filename_prefix_full, filename_prefix, version_name, start_frame, end_frame))
    
    return extracted_info

# Call the function to extract source information
extracted_info = extract_source_info()

# ========================================================================== #
# This section defines the logik projekt, directories and path variables.
# ========================================================================== #

# Function to create Nuke composition scripts
def create_nuke_scripts(extracted_info):
    """
    Creates Nuke scripts for each shot and task type.
    """
    # Iterate over extracted information
    for shot_name, source_item_recursive_dir, filename_prefix_full, filename_prefix, version_name, start_frame, end_frame in extracted_info:
        for task_type in task_type_array:

            # Check if the directories exist
            openclips_dir = os.path.join(shots_dir, shot_name, 'openclip')
            openclips_app_dir = os.path.join(shots_dir, shot_name, 'openclip', app_name)
            scripts_dir = os.path.join(shots_dir, shot_name, 'scripts')
            app_scripts_dir = os.path.join(scripts_dir, app_name)
            app_tasks_dir = os.path.join(app_scripts_dir, "tasks")

            if not os.path.exists(openclips_dir):
                os.makedirs(openclips_dir)

            if not os.path.exists(openclips_app_dir):
                os.makedirs(openclips_app_dir)

            if not os.path.exists(scripts_dir):
                os.makedirs(scripts_dir)

            if not os.path.exists(app_scripts_dir):
                os.makedirs(app_scripts_dir)
 
            if not os.path.exists(app_tasks_dir):
                os.makedirs(app_tasks_dir)
            
            # Create task directory if it doesn't exist
            app_task_dir = os.path.join(app_tasks_dir, task_type)
            if not os.path.exists(app_task_dir):
                os.makedirs(app_task_dir)

            
            # Create shot task name
            shot_task_name = f"{shot_name}_{app_name}_{task_type}"

            # Define openclip variables
            shot_task_openclip_name = f"{shot_task_name}.clip"
            shot_task_openclip_path = os.path.join(openclips_app_dir, shot_task_openclip_name)

            # Create openclip file
            with open(shot_task_openclip_path, 'w') as shot_task_openclip_file:

                # Write openclip content
                print(f"Creating {task_type} openclip for {shot_name}")
                shot_task_openclip_file.write(f"""<?xml version="1.0" encoding="UTF-8"?>
<clip type="clip" version="5">
	<name>{shot_name}_{app_name}_{task_type}</name>
	<handler>
		<name>MIO Clip</name>
		<options>
			<ScanPattern type="string">{shots_dir}/{shot_name}/media/renders/{shot_name}_{app_name}_{task_type}_v{{version}}/{shot_name}_{app_name}_{task_type}_v{{version}}.{{frame}}.exr</ScanPattern>
		</options>
	</handler>
</clip>
""")

            # Define script variables
            shot_task_script_name = f"{shot_task_name}_{version_name}.nk"
            shot_task_script_path = os.path.join(app_task_dir, shot_task_script_name)

            # Create script file
            with open(shot_task_script_path, 'w') as nuke_script_file:

                # Write Nuke script content
                print(f"Created {task_type} script for {shot_name}")
                nuke_script_file.write(f"""Root {{
 inputs 0
 name "{shot_task_script_path}"
 frame "{start_frame}"
 first_frame "{start_frame}"
 last_frame "{end_frame}"
 lock_range true
 format "2048 1556 0 0 2048 1556 1 2K_Super_35(full-ap)"
 proxy_type scale
 proxy_format "1024 778 0 0 1024 778 1 1K_Super_35(full-ap)"
 colorManagement OCIO
 OCIO_config aces_1.2
 defaultViewerLUT "OCIO LUTs"
 workingSpaceLUT "ACES - ACEScg"
 monitorLut "Rec.709 (ACES)"
 monitorOutLUT "Rec.709 (ACES)"
 int8Lut matte_paint
 int16Lut "ACES - ACEScct"
 logLut "ACES - ACEScct"
 floatLut "ACES - ACEScg"
}}
Read {{
 inputs 0
 file_type exr
 file "{source_item_recursive_dir}/{filename_prefix_full}.########.exr"
 first {start_frame}
 last {end_frame}
 origfirst {start_frame}
 origlast {end_frame}
 origset true
 name Read1
 xpos 0
 ypos 0
}}
set Ndbbb980 [stack 0]
Write {{
 file "{renders_dir}/{shot_task_name}/{shot_task_name}.%08d.exr"
 file_type exr
 write_ACES_compliant_EXR true
 metadata "all metadata"
 first_part rgba
 create_directories true
 first "{start_frame}"
 last "{end_frame}"
 use_limit true
 version 0
 ocioColorspace "ACES - ACEScg"
 display ACES
 view sRGB
 name Write1
 xpos 0
 ypos 192
 postage_stamp true
}}""")
            
# Call the function to create Nuke composition scripts with the extracted information
# create_nuke_scripts(extracted_info)

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
            'order': 5,
            'actions': [
                {
                    'name': 'nuke scripts',
                    'execute': create_nuke_scripts,
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
#                     'execute': create_nuke_scripts,
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
            'order': 5,
            'actions': [
                {
                    'name': 'nuke scripts',
                    'order': 5,
                    'separator': 'below',
                    'execute': create_nuke_scripts,
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
    create_nuke_scripts(extracted_info)

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
