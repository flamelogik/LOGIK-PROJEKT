#!/bin/bash

# -------------------------------------------------------------------------- #

# File Name:        function_17-job_dirs.sh
# Version:          2.0.2
# Language:         bash script
# Flame Version:    2025.x
# Author:           Phil MAN - phil_man@mac.com
# Toolset:          MAN_MADE_MATERIAL: LOGIK-PROJEKT
# Modified:         2024-04-30
# Modifier:         Phil MAN - phil_man@mac.com

# Description:      This program contains function(s) that are used to
#                   create new logik projekts.

# Installation:     Copy the 'LOGIK-PROJEKT' repo to your GitHub directory,
#                   e.g. '/home/$USER/workspace/GitHub'

# Changelist:       The full changelist is at the end of this document.

# -------------------------------------------------------------------------- #

# ========================================================================== #
# This section defines the primary functions for the script.
# ========================================================================== #

# Function to create job directories
create_projekt_job_directories() {
    # Set the umask to 0
    umask 0

    # Declare variables
    # local jobs_dir="/JOBS"
    local jobs_dir="/Volumes/logik/salt/JOBS"
    local tgt_job_dir="$jobs_dir/$nickname"

    # Create directories
    echo -e "  creating logik projekt job directories:"
    echo -e "\n$separator\n"

    # ---------------------------------------------------------------------- #

    tgt_assets_dir="$tgt_job_dir/assets"
    tgt_audio_dir="$tgt_assets_dir/audio"
    tgt_audio_dated_dir="$tgt_audio_dir/$today"
    tgt_CGI_dir="$tgt_assets_dir/CGI"
    tgt_footage_graded_dir="$tgt_assets_dir/footage_graded"
    tgt_footage_graded_dated_dir="$tgt_footage_graded_dir/$today"
    tgt_footage_raw_dir="$tgt_assets_dir/footage_raw"
    tgt_footage_raw_dated_dir="$tgt_footage_raw_dir/$today"
    tgt_geometry_dir="$tgt_assets_dir/geometry"
    tgt_geometry_3ds_dir="$tgt_geometry_dir/3ds"
    tgt_geometry_alembic_dir="$tgt_geometry_dir/alembic"
    tgt_geometry_cache_dir="$tgt_geometry_dir/cache"
    tgt_geometry_dxf_dir="$tgt_geometry_dir/dxf"
    tgt_geometry_fbx_dir="$tgt_geometry_dir/fbx"
    tgt_geometry_obj_dir="$tgt_geometry_dir/obj"
    tgt_geometry_usd_dir="$tgt_geometry_dir/usd"
    tgt_graphics_dir="$tgt_assets_dir/graphics"
    tgt_matchmoving_dir="$tgt_assets_dir/matchmoving"
    tgt_miscellaneous_dir="$tgt_assets_dir/miscellaneous"
    tgt_roto_dir="$tgt_assets_dir/roto"
    tgt_slates_dir="$tgt_assets_dir/slates"
    tgt_subtitles_dir="$tgt_assets_dir/subtitles"
    tgt_tracking_dir="$tgt_assets_dir/tracking"
    tgt_video_dir="$tgt_assets_dir/video"

    tgt_rsync_dir="$tgt_job_dir/backup_scripts"

    tgt_configs_dir="$tgt_job_dir/configs"
    tgt_configs_workstation_dir="$tgt_configs_dir/$workstation_name"

    tgt_deliverables_dir="$tgt_job_dir/deliverables"
    tgt_finals_dir="$tgt_deliverables_dir/finals"

    tgt_editorial_dir="$tgt_job_dir/editorial"
    tgt_editorial_aaf_dir="$tgt_editorial_dir/aaf"
    tgt_editorial_edl_dir="$tgt_editorial_dir/edl"
    tgt_editorial_xml_dir="$tgt_editorial_dir/xml"
    tgt_editorial_today_dir="$tgt_editorial_dir/$today-editorial"

    tgt_flame_dir="$tgt_job_dir/flame"
    tgt_flame_archives_dir="$tgt_flame_dir/archives"
    tgt_setups_dir="$tgt_flame_dir/setups"
    tgt_version_dir="$tgt_setups_dir/$version"
    tgt_workstation_dir="$tgt_version_dir/$workstation_name"

    tgt_reference_dir="$tgt_job_dir/reference"
    tgt_reference_today_dir="$tgt_reference_dir/$today-reference"

    tgt_shots_dir="$tgt_job_dir/shots"

    tgt_wip_dir="$tgt_job_dir/work_in_progress"
    tgt_postings_dir="$tgt_wip_dir/postings"

    # ---------------------------------------------------------------------- #

    # Define the directories
    declare -a flame_job_dirs=(
        "$tgt_job_dir"
        "$tgt_assets_dir"
        "$tgt_audio_dir"
        "$tgt_audio_dated_dir"
        "$tgt_CGI_dir"
        "$tgt_footage_graded_dir"
        "$tgt_footage_graded_dated_dir"
        "$tgt_footage_raw_dir"
        "$tgt_footage_raw_dated_dir"
        "$tgt_geometry_dir"
        "$tgt_geometry_3ds_dir"
        "$tgt_geometry_alembic_dir"
        "$tgt_geometry_cache_dir"
        "$tgt_geometry_dxf_dir"
        "$tgt_geometry_fbx_dir"
        "$tgt_geometry_obj_dir"
        "$tgt_geometry_usd_dir"
        "$tgt_graphics_dir"
        "$tgt_miscellaneous_dir"
        "$tgt_matchmoving_dir"
        "$tgt_roto_dir"
        "$tgt_slates_dir"
        "$tgt_subtitles_dir"
        "$tgt_tracking_dir"
        "$tgt_video_dir"
        "$tgt_rsync_dir"
        "$tgt_configs_dir"
        "$tgt_configs_workstation_dir"
        "$tgt_deliverables_dir"
        "$tgt_finals_dir"
        "$tgt_editorial_dir"
        "$tgt_editorial_edl_dir"
        "$tgt_editorial_aaf_dir"
        "$tgt_editorial_xml_dir"
        "$tgt_editorial_today_dir"
        "$tgt_flame_dir"
        "$tgt_flame_archives_dir"
        "$tgt_setups_dir"
        "$tgt_version_dir"
        "$tgt_workstation_dir"
        "$tgt_reference_dir"
        "$tgt_reference_today_dir"
        "$tgt_shots_dir"
        "$tgt_wip_dir"
        "$tgt_postings_dir"
    )

    # Create the directories
    for dir in "${flame_job_dirs[@]}"; do
        mkdir -p -m 2777 "$dir" | sed 's/^ *mkdir: created directory //' | sed 's/^/  /'
    done

    echo -e "\n$separator\n"

    echo -e "  logik projekt job directories created."
    echo -e "\n$separator\n"
}

# ========================================================================== #
# This section defines how to handle the main script function.
# ========================================================================== #

# # Call the function to create the flame projekt directories
# create_flame_projekt_directories

# Check if the script is being sourced or executed
if [[ "${BASH_SOURCE[0]}" == "${0}" ]]; then

    create_projekt_job_directories
fi

# -------------------------------------------------------------------------- #

# ========================================================================== #
# C2 A9 2D 32 30 32 34 2D 4D 41 4E 5F 4D 41 44 45 5F 4D 41 54 45 52 49 61 4C #
# ========================================================================== #

# Changelist:       
# -------------------------------------------------------------------------- #
# version:               1.0.0
# modified:              2024-04-20 - 16:20:00
# comments:              refactored monolithic program into separate functions
# -------------------------------------------------------------------------- #
# version:               2.0.0
# modified:              2024-04-29 - 11:29:27
# comments:              testing production readiness
# -------------------------------------------------------------------------- #
# version:               2.0.1
# modified:              2024-04-30 - 07:06:00
# comments:              Removed 'declare -g' statements for macOS compatibility
# -------------------------------------------------------------------------- #
# version:               2.0.2
# modified:              2024-04-30 - 12:29:07
# comments:              added 'umask 0' statements for rsync commands
