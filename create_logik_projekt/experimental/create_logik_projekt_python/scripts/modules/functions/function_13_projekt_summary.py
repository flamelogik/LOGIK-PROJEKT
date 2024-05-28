import os

# -------------------------------------------------------------------------- #

# File Name:        function_13-projekt_summary.py
# Version:          2.1.5
# Language:         Python script
# Flame Version:    2025.x
# Author:           Phil MAN - phil_man@mac.com
# Toolset:          MAN_MADE_MATERIAL: LOGIK-PROJEKT
# Modified:         2024-05-18
# Modifier:         Phil MAN - phil_man@mac.com

# Description:      This program contains function(s) that are used to
#                   create new logik projekts.

# Installation:     Copy the 'LOGIK-PROJEKT' repo to your GitHub directory,
#                   e.g. '/home/$USER/workspace/GitHub'

# Changelist:       The full changelist is at the end of this document.

# -------------------------------------------------------------------------- #

# ========================================================================== #
# This section defines global variables.
# ========================================================================== #

# Declare global variables
name = ""
nickname = ""
description = ""
shotgun_name = ""
setup_dir = ""
partition = ""
version = ""
frame_width = ""
frame_height = ""
frame_depth = ""
aspect_ratio = ""
field_dominance = ""
frame_rate = ""
default_start_frame = ""
proj_color_science = ""

# ========================================================================== #
# This section creates the logik projekt metadata directories.
# ========================================================================== #

# Function to create directories for logik projekt setup
def create_metadata_directories():
    projekt_log_dir = os.path.join(script_path, "xml", YYYY, MM, DD)
    os.makedirs(projekt_log_dir, exist_ok=True)

# -------------------------------------------------------------------------- #

# ========================================================================== #
# This section sets the logik projekt metadata.
# ========================================================================== #

# Function to set logik projekt metadata
def set_projekt_metadata():
    global name, nickname, description, shotgun_name, setup_dir, partition, version, frame_width, frame_height, frame_depth, aspect_ratio, field_dominance, frame_rate, default_start_frame
    name = f"{client}_{campaign}_{max_sanitized_sw_ver}_{workstation_name}"
    nickname = f"{client}_{campaign}"
    description = f"flame {max_sanitized_sw_ver} projekt for {client} {campaign}"
    shotgun_name = nickname
    setup_dir = name
    partition = "stonefs"  # This could be turned into a variable!
    version = max_dir_ver
    frame_width = proj_res_h
    frame_height = proj_res_v
    frame_depth = proj_color_depth
    aspect_ratio = proj_aspect_ratio
    field_dominance = "PROGRESSIVE"
    frame_rate = proj_fcm
    default_start_frame = default_start_frame

# -------------------------------------------------------------------------- #

# ========================================================================== #
# This section summarizes the logik projekt metadata.
# ========================================================================== #

# Function to summarize logik projekt metadata
def summarize_projekt_metadata():
    print("  logik projekt summary\n")
    print(f"  projekt name:        {name}")
    print(f"  projekt nickname:    {nickname}")
    print(f"  projekt description: {description}")
    print(f"  shotgrid name:       {shotgun_name}")
    print(f"  setup directory:     {setup_dir}")
    print(f"  flame framestore:    {partition}")
    print(f"  software version:    {version}")
    print(f"  frame width:         {frame_width}")
    print(f"  frame height:        {frame_height}")
    print(f"  color depth:         {frame_depth}")
    print(f"  aspect ratio:        {aspect_ratio}")
    print(f"  field dominance:     {field_dominance}")
    print(f"  frame rate:          {frame_rate}")
    print(f"  start frame:         {default_start_frame}")
    print(f"  color policy:        {proj_color_science}")
    print("\n$separator\n")

# -------------------------------------------------------------------------- #

# ========================================================================== #
# This section creates the logik projekt metadata directories.
# ========================================================================== #

# Function to write metadata to file
def write_projekt_metadata():
    create_metadata_directories()
    projekt_metadata_xml_file = os.path.join(projekt_log_dir, f"projekt_metadata_{name}.xml")
    with open(projekt_metadata_xml_file, 'w') as f:
        f.write("<Project>")
        ProjektParameters = [
            f"Name:{name}",
            f"Nickname:{nickname}",
            # "Description:$description",
            f"ShotgunProjectName:{shotgun_name}",
            f"SetupDir:{setup_dir}",
            f"Partition:{partition}",
            # "Version:$version",
            f"FrameWidth:{frame_width}",
            f"FrameHeight:{frame_height}",
            f"FrameDepth:{frame_depth}",
            f"AspectRatio:{aspect_ratio}",
            f"FieldDominance:{field_dominance}",
            f"FrameRate:{frame_rate}",
            f"DefaultStartFrame:{default_start_frame}",
        ]
        for ProjektParameter in ProjektParameters:
            key, value = ProjektParameter.split(':')
            f.write(f"<{key}>{value}</{key}>")
        f.write("</Project>")
    print(f"  projekt XML:         {os.path.basename(projekt_metadata_xml_file)}")

# ========================================================================== #
# This section defines how to handle the main script function.
# ========================================================================== #

# Check if the script is being sourced or executed
if __name__ == "__main__":

    # Create directories
    create_metadata_directories()

    # Set metadata
    set_projekt_metadata()

    # Summarize metadata
    summarize_projekt_metadata()

    # Write metadata to file
    write_projekt_metadata()
