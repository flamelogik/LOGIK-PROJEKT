# filename: create_nuke_scripts.py

# -------------------------------------------------------------------------- #

# File Name:        create_nuke_scripts.py
# Version:          1.0.5
# Language:         python script
# Flame Version:    2025.x
# Author:           Phil MAN - phil_man@mac.com
# Toolset:          MAN_MADE_MATERIAL: LOGIK-PROJEKT
# Created:          2024-04-20
# Modified:         2024-05-06
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
import os
# import pdb; pdb.set_trace()
# import re
import fileinput
# import logging
from datetime import datetime

# ========================================================================== #
# This section enables debugging.
# ========================================================================== #

# # Initiate script logging for debugging
# def setup_logging(*args, **kwargs):
#     script_path = os.path.abspath(__file__)
#     script_name = os.path.basename(script_path)
#     script_name_without_extension = os.path.splitext(script_name)[0]
#     script_directory = os.path.dirname(script_path)
#     log_directory = os.path.join(script_directory, 'log')

#     if not os.path.exists(log_directory):
#         os.makedirs(log_directory)

#     log_filename = f"{datetime.now().strftime('%Y-%m-%d-%H-%M')}_{script_name}.debug.log"
#     log_filepath = os.path.join(log_directory, log_filename)
#     print("Log filepath:", log_filepath)  # Add this line for debugging
#     logging.basicConfig(filename=log_filepath, level=logging.DEBUG, *args, **kwargs)

# ========================================================================== #
# This section defines the logik projekt job structure.
# ========================================================================== #

# Define function to define job structure
def define_job_structure(projekt_dir):
    """
    Define the directory structure for a job.

    Args:
        projekt_dir (str): The root directory for the job.

    Returns:
        dict: A dictionary containing the defined directory structure.
    """

    # # This section is for logging purposes
    # logging.info("Defining job structure...")

    # Define directories
    jobs_dir = /JOBS

    # # Get the current Flame project
    # the_current_projekt = flame.projects.current_project

    # # Get the project job_name
    # the_projekt_job_name = the_current_projekt.nickname

    # Define the job root directory
    # job_root = os.path.join(jobs_dir, the_projekt_job_name)

    # Testing
    tgt_job_dir = projekt_dir

    tgt_assets_dir = f"{tgt_job_dir}/assets"
    tgt_audio_dir = f"{tgt_assets_dir}/audio"
    tgt_CGI_dir = f"{tgt_assets_dir}/CGI"
    tgt_footage_graded_dir = f"{tgt_assets_dir}/footage_graded"
    tgt_footage_raw_dir = f"{tgt_assets_dir}/footage_raw"

    tgt_geometry_dir = f"{tgt_assets_dir}/geometry"
    tgt_geometry_3ds_dir = f"{tgt_geometry_dir}/3ds"
    tgt_geometry_alembic_dir = f"{tgt_geometry_dir}/alembic"
    tgt_geometry_cache_dir = f"{tgt_geometry_dir}/cache"
    tgt_geometry_dxf_dir = f"{tgt_geometry_dir}/dxf"
    tgt_geometry_fbx_dir = f"{tgt_geometry_dir}/fbx"
    tgt_geometry_obj_dir = f"{tgt_geometry_dir}/obj"
    tgt_geometry_usd_dir = f"{tgt_geometry_dir}/usd"

    tgt_graphics_dir = f"{tgt_assets_dir}/graphics"
    tgt_matchmoving_dir = f"{tgt_assets_dir}/matchmoving"
    tgt_miscellaneous_dir = f"{tgt_assets_dir}/miscellaneous"
    tgt_roto_dir = f"{tgt_assets_dir}/roto"
    tgt_slates_dir = f"{tgt_assets_dir}/slates"
    tgt_subtitles_dir = f"{tgt_assets_dir}/subtitles"
    tgt_tracking_dir = f"{tgt_assets_dir}/tracking"
    tgt_video_dir = f"{tgt_assets_dir}/video"

    tgt_rsync_dir = f"{tgt_job_dir}/rsync"

    tgt_configs_dir = f"{tgt_job_dir}/configs"
    tgt_configs_workstation_dir = f"{tgt_configs_dir}/configs_workstation"

    tgt_deliverables_dir = f"{tgt_job_dir}/deliverables"
    tgt_finals_dir = f"{tgt_deliverables_dir}/finals"

    tgt_editorial_dir = f"{tgt_job_dir}/editorial"
    tgt_editorial_aaf_dir = f"{tgt_editorial_dir}/editorial_aaf"
    tgt_editorial_edl_dir = f"{tgt_editorial_dir}/editorial_edl"
    tgt_editorial_xml_dir = f"{tgt_editorial_dir}/editorial_xml"

    tgt_shots_dir = f"{tgt_job_dir}/shots"

    # # This section is for logging purposes
    # logging.info("Job structure defined.")

    return {
        "projekt_dir": projekt_dir,
        "tgt_job_dir": tgt_job_dir,
        "tgt_assets_dir": tgt_assets_dir,
        "tgt_audio_dir": tgt_audio_dir,
        "tgt_CGI_dir": tgt_CGI_dir,
        "tgt_footage_graded_dir": tgt_footage_graded_dir,
        "tgt_footage_raw_dir": tgt_footage_raw_dir,
        "tgt_geometry_dir": tgt_geometry_dir,
        "tgt_geometry_3ds_dir": tgt_geometry_3ds_dir,
        "tgt_geometry_alembic_dir": tgt_geometry_alembic_dir,
        "tgt_geometry_cache_dir": tgt_geometry_cache_dir,
        "tgt_geometry_dxf_dir": tgt_geometry_dxf_dir,
        "tgt_geometry_fbx_dir": tgt_geometry_fbx_dir,
        "tgt_geometry_obj_dir": tgt_geometry_obj_dir,
        "tgt_geometry_usd_dir": tgt_geometry_usd_dir,
        "tgt_graphics_dir": tgt_graphics_dir,
        "tgt_matchmoving_dir": tgt_matchmoving_dir,
        "tgt_miscellaneous_dir": tgt_miscellaneous_dir,
        "tgt_roto_dir": tgt_roto_dir,
        "tgt_slates_dir": tgt_slates_dir,
        "tgt_subtitles_dir": tgt_subtitles_dir,
        "tgt_tracking_dir": tgt_tracking_dir,
        "tgt_video_dir": tgt_video_dir,
        "tgt_rsync_dir": tgt_rsync_dir,
        "tgt_configs_dir": tgt_configs_dir,
        "tgt_configs_workstation_dir": tgt_configs_workstation_dir,
        "tgt_deliverables_dir": tgt_deliverables_dir,
        "tgt_finals_dir": tgt_finals_dir,
        "tgt_editorial_dir": tgt_editorial_dir,
        "tgt_editorial_aaf_dir": tgt_editorial_aaf_dir,
        "tgt_editorial_edl_dir": tgt_editorial_edl_dir,
        "tgt_editorial_xml_dir": tgt_editorial_xml_dir,
        "tgt_shots_dir": tgt_shots_dir
    }

# ========================================================================== #
# This section gathers information about logik projekt shots.
# ========================================================================== #

# Define function to list shot directories
def list_shots_dir(tgt_shots_dir):
    """List directories in tgt_shots_dir path and sort alphabetically.

    Args:
        tgt_shots_dir (str): The directory to list.

    Returns:
        shots_dir_list: A sorted list of directories in tgt_shots_dir.
    """

    # # This section is for logging purposes
    # logging.info(f"Listing shot directories in {tgt_shots_dir}:")

    shots_dir_list = [
        shots_dir_item for shots_dir_item in os.listdir(tgt_shots_dir) 
        if os.path.isdir(os.path.join(tgt_shots_dir, shots_dir_item))
    ]

    # Sort the list alphabetically
    shots_dir_list.sort()

    # # This section is for logging purposes
    # for shot_dir in shots_dir_list:
    #     logging.info(f" - {shot_dir}")

    return shots_dir_list

# -------------------------------------------------------------------------- #

# Define function to define shot structure
def define_shot_structure(tgt_shots_dir, 
                          shot_dir, 
                          app_name, 
                          task_type):
    """
    Define directory structure for a shot.

    Parameters:
    tgt_shots_dir (str): Directory path where shots are stored.
    shot_dir (str): Name of the shot directory.
    app_name (str): Name of the application.
    task_type (str): Type of task.

    Returns:
    dict: Dictionary containing directory paths for the shot structure.
    """

    # # This section is for logging purposes
    # logging.info(f"Defining shot structure for {shot_dir}...")

    # Define directories
    shot_batch_setups_dir = f"{tgt_shots_dir}/{shot_dir}/batch_setups"

    shot_media_dir = f"{tgt_shots_dir}/{shot_dir}/media"
    shot_renders_dir = f"{shot_media_dir}/renders"
    shot_sources_dir = f"{shot_media_dir}/sources"

    shot_openclip_dir = f"{tgt_shots_dir}/{shot_dir}/openclip"
    shot_output_clips_dir = f"{shot_openclip_dir}/output_clips"
    shot_output_clips_app_dir = f"{shot_output_clips_dir}/{app_name}"
    shot_output_clips_app_task_dir = f"{shot_output_clips_app_dir}/shot/{task_type}"

    shot_segment_clips_dir = f"{shot_openclip_dir}/segment_clips"
    shot_segment_clips_app_dir = f"{shot_segment_clips_dir}/{app_name}"
    shot_segment_clips_app_task_dir = f"{shot_segment_clips_app_dir}/source/{task_type}"

    shot_scripts_dir = f"{tgt_shots_dir}/{shot_dir}/scripts"
    shot_scripts_app_dir = f"{shot_scripts_dir}/{app_name}"
    shot_scripts_app_task_dir = f"{shot_scripts_app_dir}/{task_type}"

    # Create directories if they don't exist
    for directory in [
        shot_batch_setups_dir, 
        shot_renders_dir, 
        shot_sources_dir,
        shot_output_clips_dir, 
        shot_output_clips_app_dir,
        # shot_output_clips_app_task_dir,
        shot_segment_clips_dir, 
        shot_segment_clips_app_dir,
        # shot_segment_clips_app_task_dir,
        shot_scripts_dir,
        # shot_scripts_app_dir,
        shot_scripts_app_dir
        # shot_scripts_app_task_dir
    ]:

        os.makedirs(directory, exist_ok=True)

    # # This section is for logging purposes
    # logging.info(f"Shot structure defined for {shot_dir}.")

    return {
        "shot_batch_setups_dir": shot_batch_setups_dir,
        "shot_media_dir": shot_media_dir,
        "shot_renders_dir": shot_renders_dir,
        "shot_sources_dir": shot_sources_dir,
        "shot_openclip_dir": shot_openclip_dir,
        "shot_output_clips_dir": shot_output_clips_dir,
        "shot_output_clips_app_dir": shot_output_clips_app_dir,
        "shot_output_clips_app_task_dir": shot_output_clips_app_task_dir,
        "shot_segment_clips_dir": shot_segment_clips_dir,
        "shot_segment_clips_app_dir": shot_segment_clips_app_dir,
        "shot_segment_clips_app_task_dir": shot_segment_clips_app_task_dir,
        "shot_scripts_dir": shot_scripts_dir,
        "shot_scripts_app_dir": shot_scripts_app_dir,
        "shot_scripts_app_task_dir": shot_scripts_app_task_dir
    }

# -------------------------------------------------------------------------- #

def list_shot_sources_dir(shot_sources_dir):
    """List directories directly inside the given directory path.

    Args:
        shot_sources_dir (str): The directory to list.

    Returns:
        list:   A sorted list of subdirectories directly inside the
                given directory path.
    """

    # # This section is for logging purposes
    # logging.info(f"Listing directories of {shot_sources_dir}:")

    shot_sources_dir_list = os.listdir(shot_sources_dir)
    shot_sources_dir_list.sort()  # Sort the directory list
    
    # # This section is for logging purposes
    # for shot_source_dir in shot_sources_dir_list:
    #     logging.info(f" - {shot_source_dir}")
    
    return shot_sources_dir_list

# -------------------------------------------------------------------------- #

# Define function to list the contents of each shot_source_dir
def list_shot_source_dir(shot_source_dir):
    """List directories directly inside the given directory path.

    Args:
        shot_source_dir (str): The directory to list.

    Returns:
        list:   A sorted list of subdirectories directly inside the
                given directory path.
    """

    # # This section is for logging purposes
    # logging.info(f"Listing contents of source directory {shot_source_dir}:")

    shot_source_dir_list = os.listdir(shot_source_dir)
    shot_source_dir_list.sort()  # Sort the directory list

    # # This section is for logging purposes
    # for shot_source_version_dir in shot_source_dir_list:
    #     logging.info(f" - {shot_source_version_dir}")

    return shot_source_dir_list

# -------------------------------------------------------------------------- #

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
# This section defines functions to create pattern-based openclip files.
# ========================================================================== #

# Define function to create an openclip output clip for a nuke shot script
def create_openclip_output_clip(shot_name, 
                                app_name, 
                                task_type, 
                                tgt_shots_dir,
                                shot_output_clips_app_dir):
    """
    Create an openclip output clip for a nuke shot script.

    Parameters:
    shot_name (str): The name of the shot.
    app_name (str): The name of the application.
    task_type (str): The type of task.
    tgt_shots_dir (str): The directory where shots are stored.
    shot_output_clips_app_dir (str): The directory for output clips.

    Returns:
    None
    """

    shot_output_clips_app_task_dir = os.path.join(tgt_shots_dir,
                                                  shot_output_clips_app_dir,
                                                  task_type) # May be unnecessary.

    # Create the directory if it doesn't exist
    os.makedirs(shot_output_clips_app_task_dir, exist_ok=True) # May be unnecessary.

    shot_output_clips_app_task_file = f"{shot_name}_{app_name}_{task_type}.clip"
    shot_output_clips_app_task_path = os.path.join(tgt_shots_dir,
                                                   shot_output_clips_app_dir,
                                                   task_type,
                                                   shot_output_clips_app_task_file)

    with open(shot_output_clips_app_task_path, 'w') as output_clip_file:
        output_clip_file.write(f"""<?xml version="1.0" encoding="UTF-8"?>
<clip type="clip" version="5">
    <name>{shot_name}_{app_name}_{task_type}</name>
    <handler>
        <name>MIO Clip</name>
        <options>
            <ScanPattern type="string">{tgt_shots_dir}/{shot_name}/media/renders/{shot_name}_{app_name}_{task_type}_v{{version}}/{shot_name}_{app_name}_{task_type}_v{{version}}.{{frame}}.exr</ScanPattern>
        </options>
    </handler>
</clip>""")

    # # This section is for logging purposes
    # logging.debug(f"output clip created for:     {shot_name}_{app_name}_{task_type}")

    print(f"Output clip created:         {shot_name}_{app_name}_{task_type}.clip\n")
 
# -------------------------------------------------------------------------- #

# Define function to create an openclip segment clip for a nuke source script
def create_openclip_segment_clip(shot_source_dir, 
                                 app_name, 
                                 task_type, 
                                 tgt_shots_dir, 
                                 shot_segment_clips_app_dir):
    """
    Create an openclip segment clip for a nuke segment script.

    Parameters:
    shot_name (str): The name of the shot.
    app_name (str): The name of the application.
    task_type (str): The type of task.
    tgt_shots_dir (str): The directory where shots are stored.
    shot_output_clips_app_dir (str): The directory for output clips.

    Returns:
    None
    """

    shot_segment_clips_app_task_dir = os.path.join(tgt_shots_dir, 
                                                   shot_segment_clips_app_dir, 
                                                   task_type) # May be unnecessary.

    # Create the directory if it doesn't exist
    os.makedirs(shot_segment_clips_app_task_dir, exist_ok=True) # May be unnecessary.

    shot_segment_clips_app_task_file = f"{shot_source_dir}_{app_name}_{task_type}.clip"
    shot_segment_clips_app_task_path = os.path.join(tgt_shots_dir, 
                                                    shot_segment_clips_app_dir, 
                                                    task_type, 
                                                    shot_segment_clips_app_task_file)

    with open(shot_segment_clips_app_task_path, 'w') as segment_clip_file:
        segment_clip_file.write(f"""<?xml version="1.0" encoding="UTF-8"?>
<clip type="clip" version="5">
    <name>{shot_source_dir}_{app_name}_{task_type}</name>
    <handler>
        <name>MIO Clip</name>
        <options>
            <ScanPattern type="string">{tgt_shots_dir}/media/sources/{shot_source_dir}_{app_name}_{task_type}_v{{version}}/{shot_source_dir}_{app_name}_{task_type}_v{{version}}.{{frame}}.exr</ScanPattern>
        </options>
    </handler>
</clip>""")
        
    # # This section is for logging purposes
    # logging.debug(f"segment clip created for:    {shot_source_dir}_{app_name}_{task_type}")

    print(f"Segment clip created:        {shot_source_dir}_{app_name}_{task_type}.clip\n")

# ========================================================================== #
# This section defines functions to create nuke scripts.
# ========================================================================== #

# Define function to create a shot script for nuke based on task
def create_shot_script(shot_name, 
                       app_name, 
                       task_type, 
                       version_name,
                       tgt_shots_dir, 
                       shot_renders_dir, 
                       shot_scripts_dir):
    """
    Create a shot script for nuke based on task.

    Parameters:
        shot_name        (str): The name of the shot.
        app_name         (str): The name of the application.
        task_type        (str): The type of task.
        version_name     (str): The name of the version.
        tgt_shots_dir        (str): The directory where shots are stored.
        shot_renders_dir (str): The directory for shot renders.
        shot_scripts_dir (str): The directory for shot scripts.

    Returns:
    None
    """

    # Define the directory for the specific app and task type
    shot_scripts_app_task_dir = os.path.join(tgt_shots_dir,
                                             shot_scripts_dir,
                                             app_name,
                                             'shot',
                                             task_type)

    # Create the directory if it doesn't exist
    os.makedirs(shot_scripts_app_task_dir, exist_ok=True)

    # Define the file path for the script
    shot_scripts_app_task_file = f"{shot_name}_{app_name}_{task_type}_{version_name}.nk"
    shot_scripts_app_task_path = os.path.join(shot_scripts_app_task_dir,
                                              shot_scripts_app_task_file)

    # Write the Nuke script content to the file
    with open(shot_scripts_app_task_path, 'w') as nuke_shot_script_file:
        nuke_shot_script_file.write(f"""# LOGIK-PROJEKT Nuke Shot Script
# Task Name: {shot_name}_{app_name}_{task_type}
Root {{
 inputs 0
 name "{shot_name}_{app_name}_{task_type}_{version_name}.nk"
 frame NUKE_START_FRAME
 first_frame NUKE_START_FRAME
 last_frame NUKE_END_FRAME
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
Write {{
 file "{shot_renders_dir}/{shot_name}_{app_name}_{task_type}_{version_name}/{shot_name}_{app_name}_{task_type}_{version_name}.%08d.exr"
 file_type exr
 write_ACES_compliant_EXR true
 metadata "all metadata"
 first_part rgba
 create_directories true
 first "NUKE_START_FRAME"
 last "NUKE_END_FRAME"
 use_limit true
 version 0
 ocioColorspace "ACES - ACEScg"
 display ACES
 view sRGB
 name Write1
 label "{shot_name}_{app_name}_{task_type}"
 xpos 0
 ypos 240
 postage_stamp true
}}""")

        # # This section is for logging purposes
        # logging.debug(f"Nuke script created for:  {shot_name}_{app_name}_{task_type}_{version_name}")

        print(f"Nuke Shot script created:    {shot_name}_{app_name}_{task_type}.nk\n")

# -------------------------------------------------------------------------- #

# Define function to create a source script
def create_source_script(shot_name, 
                         tgt_shots_dir, 
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
    Create a source script for nuke based on layer and task.

    Parameters:
        shot_name (str): The name of the shot.
        tgt_shots_dir (str): The directory where shots are stored.
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
    source_scripts_app_task_dir = os.path.join(tgt_shots_dir, 
                                               shot_scripts_dir, 
                                               app_name, 
                                               'sources', 
                                               task_type)

    # Create the directory if it doesn't exist
    os.makedirs(source_scripts_app_task_dir, exist_ok=True)

    # Define the file path for the script
    source_scripts_app_task_file = f"{shot_source_dir}_{app_name}_{task_type}_{version_name}.nk"
    source_scripts_app_task_path = os.path.join(source_scripts_app_task_dir, 
                                                source_scripts_app_task_file)

    # Append the Nuke script content to the file
    with open(source_scripts_app_task_path, 'a') as nuke_source_script_file:
        nuke_source_script_file.write(f"""# LOGIK-PROJEKT Nuke Source Script
# Task Name: {shot_source_dir}_{app_name}_{task_type}
Root {{
 inputs 0
 name "{shot_source_dir}_{version_name}.nk"
 frame "{shot_source_version_start_frame}"
 first_frame "{shot_source_version_start_frame}"
 last_frame "{shot_source_version_end_frame}"
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
}}""")

        # Write the Read node
        nuke_source_script_file.write(f"""
Read {{
 inputs 0
 file_type exr
 file "{shot_source_version_openexr_sequences_info[1]['shot_source_version_sequence_dir']}/{shot_source_dir}_{version_name}.########.exr"
 first {shot_source_version_start_frame}
 last {shot_source_version_end_frame}
 origfirst {shot_source_version_start_frame}
 origlast {shot_source_version_end_frame}
 origset true
 name Read1
 label "{shot_source_dir}"
 xpos 0
 ypos 0
}}
set Ndbbb980 [stack 0]
Write {{
 file "{shot_sources_dir}/{shot_source_dir}_{app_name}_{task_type}_{version_name}/{shot_source_dir}_{app_name}_{task_type}_{version_name}.%08d.exr"
 file_type exr
 write_ACES_compliant_EXR true
 metadata "all metadata"
 first_part rgba
 create_directories true
 first "{shot_source_version_start_frame}"
 last "{shot_source_version_end_frame}"
 use_limit true
 version 0
 ocioColorspace "ACES - ACEScg"
 display ACES
 view sRGB
 name Write1
 label "{shot_source_dir}_{app_name}_{task_type}"
 xpos 0
 ypos 192
 postage_stamp true
}}""")

        # # This section is for logging purposes
        # logging.debug(f"Nuke script created for:  {shot_source_dir}_{version_name}")

        print(f"Nuke Source script created:  {shot_source_dir}_{version_name}.nk\n")

    # Define the directory for the specific app and task type
    shot_scripts_app_task_dir = os.path.join(tgt_shots_dir, 
                                             shot_scripts_dir, 
                                             app_name, 
                                             'shot', 
                                             task_type)

    # Create the directory if it doesn't exist
    os.makedirs(shot_scripts_app_task_dir, exist_ok=True)

    # Define the file path for the script
    shot_scripts_app_task_file = f"{shot_name}_{app_name}_{task_type}_{version_name}.nk"
    shot_scripts_app_task_path = os.path.join(shot_scripts_app_task_dir, 
                                              shot_scripts_app_task_file)

    # Open the file for in-place editing
    with fileinput.FileInput(shot_scripts_app_task_path, inplace=True) as file:
        for line in file:
            # Replace 'NUKE_START_FRAME' with the value of 'shot_source_version_start_frame'
            line = line.replace('NUKE_START_FRAME', str(shot_source_version_start_frame))
            # Replace 'NUKE_END_FRAME' with the value of 'shot_source_version_end_frame'
            line = line.replace('NUKE_END_FRAME', str(shot_source_version_end_frame))
            print(line, end='')

    # Write the Nuke script content to the file
    with open(shot_scripts_app_task_path, 'a') as nuke_shot_script_file:

        # Write the Read node
        nuke_shot_script_file.write(f"""
# Source Nodes
Read {{
 inputs 0
 file_type exr
 file "{shot_source_version_openexr_sequences_info[1]['shot_source_version_sequence_dir']}/{shot_source_dir}_{version_name}.########.exr"
 first {shot_source_version_start_frame}
 last {shot_source_version_end_frame}
 origfirst {shot_source_version_start_frame}
 origlast {shot_source_version_end_frame}
 origset true
 name Read1
 label "{shot_source_dir}"
 xpos 0
 ypos 0
}}
set Ndbbb980 [stack 0]
Write {{
 file "{shot_sources_dir}/{shot_source_dir}_{app_name}_{task_type}_{version_name}/{shot_source_dir}_{app_name}_{task_type}_{version_name}.%08d.exr"
 file_type exr
 write_ACES_compliant_EXR true
 metadata "all metadata"
 first_part rgba
 create_directories true
 first "{shot_source_version_start_frame}"
 last "{shot_source_version_end_frame}"
 use_limit true
 version 0
 ocioColorspace "ACES - ACEScg"
 display ACES
 view sRGB
 name Write1
 label "{shot_source_dir}_{app_name}_{task_type}"
 xpos 0
 ypos 192
 postage_stamp true
}}""")

        # # This section is for logging purposes
        # logging.debug(f"Nuke script appended for:  {shot_name}_{app_name}_{task_type}_{version_name}")

        print(f"Read/Write nodes appended:   {shot_source_dir}_{app_name}_{task_type}\n")

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
    # Access tgt_shots_dir from job_structure dictionary
    tgt_shots_dir = job_structure["tgt_shots_dir"]

    # List shot directories and store them in a variable
    shots_dir_list = list_shots_dir(tgt_shots_dir)

    # Define shot structures and list sources directories for each shot
    for shot_dir in shots_dir_list:

        # Define shot_name
        shot_name = shot_dir

        # Define version_name
        version_name = "v0000"

        # Iterate over task types list
        for task_type in task_types_list:
            shot_structure = define_shot_structure(tgt_shots_dir, 
                                                   shot_dir, 
                                                   app_name, 
                                                   task_type)
            
            # Log shot structure
            # logging.info(f"Shot structure for {shot_dir} ({task_type}): {shot_structure}")

            # Create openclip output clip
            create_openclip_output_clip(shot_name, 
                                        app_name, 
                                        task_type, 
                                        tgt_shots_dir, 
                                        shot_structure["shot_output_clips_app_dir"])

            # Create Nuke script for the shot
            create_shot_script(shot_name, 
                               app_name, 
                               task_type, 
                               version_name, 
                               tgt_shots_dir, 
                               shot_structure["shot_renders_dir"], 
                               shot_structure["shot_scripts_dir"])

            # Construct the correct path for listing source directories
            shot_sources_dir = os.path.join(tgt_shots_dir, 
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
                                                 tgt_shots_dir, 
                                                 shot_structure["shot_segment_clips_app_dir"])

                    # Create Nuke script for the shot
                    create_source_script(shot_name, 
                                         tgt_shots_dir, 
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

    # # Define paths
    # jobs_dir = '/JOBS'

    # # Get the current Flame project
    # the_current_projekt = flame.projects.current_project

    # # Get the project job_name
    # the_projekt_job_name = the_current_projekt.nickname

    # Define the job root directory
    # projekt_dir = os.path.join(jobs_dir, the_projekt_job_name)

    # Testing
    projekt_dir = "/JOBS/dry_run_01"

    # # Setup logging
    # setup_logging()

    # Define job structure using the function
    job_structure = define_job_structure(projekt_dir)
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
            'order': 5,
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
            'order': 5,
            'actions': [
                {
                    'name': 'nuke scripts',
                    'order': 5,
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
