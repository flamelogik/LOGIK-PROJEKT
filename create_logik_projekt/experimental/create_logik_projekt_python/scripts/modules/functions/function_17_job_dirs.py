import os
import sys

# -------------------------------------------------------------------------- #

# File Name:        function_17-job_dirs.sh
# Version:          2.1.5
# Language:         bash script
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
# This section defines the primary functions for the script.
# ========================================================================== #

# Function to create job directories
def create_projekt_job_directories():
    # Set the umask to 0
    os.umask(0)

    # Declare variables
    jobs_dir = "/JOBS"
    # jobs_dir = "/Volumes/logik/salt/JOBS" # Experimental
    tgt_job_dir = f"{jobs_dir}/{nickname}"

    # Create directories
    print("  creating logik projekt job directories:")
    print("\n$separator\n")

    # ---------------------------------------------------------------------- #

    tgt_assets_dir = f"{tgt_job_dir}/assets"
    tgt_audio_dir = f"{tgt_assets_dir}/audio"
    tgt_audio_dated_dir = f"{tgt_audio_dir}/{today}"
    tgt_CGI_dir = f"{tgt_assets_dir}/CGI"
    tgt_footage_graded_dir = f"{tgt_assets_dir}/footage_graded"
    tgt_footage_graded_dated_dir = f"{tgt_footage_graded_dir}/{today}"
    tgt_footage_raw_dir = f"{tgt_assets_dir}/footage_raw"
    tgt_footage_raw_dated_dir = f"{tgt_footage_raw_dir}/{today}"
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

    tgt_rsync_dir = f"{tgt_job_dir}/backup_scripts"

    tgt_configs_dir = f"{tgt_job_dir}/configs"
    tgt_configs_workstation_dir = f"{tgt_configs_dir}/{workstation_name}"

    tgt_deliverables_dir = f"{tgt_job_dir}/deliverables"
    tgt_finals_dir = f"{tgt_deliverables_dir}/finals"

    tgt_editorial_dir = f"{tgt_job_dir}/editorial"
    tgt_editorial_aaf_dir = f"{tgt_editorial_dir}/aaf"
    tgt_editorial_edl_dir = f"{tgt_editorial_dir}/edl"
    tgt_editorial_xml_dir = f"{tgt_editorial_dir}/xml"
    tgt_editorial_today_dir = f"{tgt_editorial_dir}/{today}-editorial"

    tgt_flame_dir = f"{tgt_job_dir}/flame"
    tgt_flame_archives_dir = f"{tgt_flame_dir}/archives"
    tgt_setups_dir = f"{tgt_flame_dir}/setups"
    tgt_version_dir = f"{tgt_setups_dir}/{version}"
    tgt_workstation_dir = f"{tgt_version_dir}/{workstation_name}"

    tgt_reference_dir = f"{tgt_job_dir}/reference"
    tgt_reference_today_dir = f"{tgt_reference_dir}/{today}-reference"

    tgt_shots_dir = f"{tgt_job_dir}/shots"

    tgt_wip_dir = f"{tgt_job_dir}/work_in_progress"
    tgt_postings_dir = f"{tgt_wip_dir}/postings"

    # ---------------------------------------------------------------------- #

    # Define the directories
    flame_job_dirs = [
        tgt_job_dir,
        tgt_assets_dir,
        tgt_audio_dir,
        tgt_audio_dated_dir,
        tgt_CGI_dir,
        tgt_footage_graded_dir,
        tgt_footage_graded_dated_dir,
        tgt_footage_raw_dir,
        tgt_footage_raw_dated_dir,
        tgt_geometry_dir,
        tgt_geometry_3ds_dir,
        tgt_geometry_alembic_dir,
        tgt_geometry_cache_dir,
        tgt_geometry_dxf_dir,
        tgt_geometry_fbx_dir,
        tgt_geometry_obj_dir,
        tgt_geometry_usd_dir,
        tgt_graphics_dir,
        tgt_miscellaneous_dir,
        tgt_matchmoving_dir,
        tgt_roto_dir,
        tgt_slates_dir,
        tgt_subtitles_dir,
        tgt_tracking_dir,
        tgt_video_dir,
        tgt_rsync_dir,
        tgt_configs_dir,
        tgt_configs_workstation_dir,
        tgt_deliverables_dir,
        tgt_finals_dir,
        tgt_editorial_dir,
        tgt_editorial_edl_dir,
        tgt_editorial_aaf_dir,
        tgt_editorial_xml_dir,
        tgt_editorial_today_dir,
        tgt_flame_dir,
        tgt_flame_archives_dir,
        tgt_setups_dir,
        tgt_version_dir,
        tgt_workstation_dir,
        tgt_reference_dir,
        tgt_reference_today_dir,
        tgt_shots_dir,
        tgt_wip_dir,
        tgt_postings_dir
    ]

    # Create the directories
    for dir in flame_job_dirs:
        os.makedirs(dir, mode=0o2777, exist_ok=True)
        print(f"  created directory: {dir}")

    print("\n$separator\n")
    print("  logik projekt job directories created.")
    print("\n$separator\n")

# ========================================================================== #
# This section defines how to handle the main script function.
# ========================================================================== #

# Check if the script is being sourced or executed
if __name__ == "__main__":
    # Mocking the missing variables to prevent errors
    nickname = "mocked_nickname"
    today = "mocked_today"
    workstation_name = "mocked_workstation_name"
    version = "mocked_version"

    create_projekt_job_directories()
