#

# -------------------------------------------------------------------------- #

# DISCLAIMER:       This file is part of LOGIK-PROJEKT.
#                   Copyright © 2024 man-made-mekanyzms
                
#                   LOGIK-PROJEKT creates directories, files, scripts & tools
#                   for use with Autodesk Flame and other software.

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
                
#                   Contact: phil_man@mac.com

# -------------------------------------------------------------------------- #

# File Name:        define_job_structure.py
# Version:          2.2.7
# Created:          2024-01-19
# Modified:         2024-08-31

# ========================================================================== #
# This section imports the necessary modules.
# ========================================================================== #

# import flame
# import os
# import pdb; pdb.set_trace()
# import re
# import fileinput
# import logging
# from datetime import datetime

# ========================================================================== #
# This section defines the logik projekt job structure.
# ========================================================================== #

# Define function to define job structure
def define_job_structure(job_root):
    """
    Define the directory structure for a job.

    Args:
        job_root (str): The root directory for the job.

    Returns:
        dict: A dictionary containing the defined directory structure.
    """

    # # This section is for logging purposes
    # logging.info("Defining job structure...")

    # Define directories
    job_dir = job_root

    assets_dir = f"{job_dir}/assets"
    audio_dir = f"{assets_dir}/audio"
    CGI_dir = f"{assets_dir}/CGI"
    footage_graded_dir = f"{assets_dir}/footage_graded"
    footage_raw_dir = f"{assets_dir}/footage_raw"

    geometry_dir = f"{assets_dir}/geometry"
    geometry_3ds_dir = f"{geometry_dir}/3ds"
    geometry_alembic_dir = f"{geometry_dir}/alembic"
    geometry_cache_dir = f"{geometry_dir}/cache"
    geometry_dxf_dir = f"{geometry_dir}/dxf"
    geometry_fbx_dir = f"{geometry_dir}/fbx"
    geometry_obj_dir = f"{geometry_dir}/obj"
    geometry_usd_dir = f"{geometry_dir}/usd"

    graphics_dir = f"{assets_dir}/graphics"
    matchmoving_dir = f"{assets_dir}/matchmoving"
    miscellaneous_dir = f"{assets_dir}/miscellaneous"
    roto_dir = f"{assets_dir}/roto"
    slates_dir = f"{assets_dir}/slates"
    subtitles_dir = f"{assets_dir}/subtitles"
    tracking_dir = f"{assets_dir}/tracking"
    video_dir = f"{assets_dir}/video"

    rsync_dir = f"{job_dir}/rsync"

    configs_dir = f"{job_dir}/configs"
    configs_workstation_dir = f"{configs_dir}/configs_workstation"

    deliverables_dir = f"{job_dir}/deliverables"
    finals_dir = f"{deliverables_dir}/finals"

    editorial_dir = f"{job_dir}/editorial"
    editorial_aaf_dir = f"{editorial_dir}/editorial_aaf"
    editorial_edl_dir = f"{editorial_dir}/editorial_edl"
    editorial_xml_dir = f"{editorial_dir}/editorial_xml"

    shots_dir = f"{job_dir}/shots"

    # # This section is for logging purposes
    # logging.info("Job structure defined.")

    return {
        "job_root": job_root,
        "job_dir": job_dir,
        "assets_dir": assets_dir,
        "audio_dir": audio_dir,
        "CGI_dir": CGI_dir,
        "footage_graded_dir": footage_graded_dir,
        "footage_raw_dir": footage_raw_dir,
        "geometry_dir": geometry_dir,
        "geometry_3ds_dir": geometry_3ds_dir,
        "geometry_alembic_dir": geometry_alembic_dir,
        "geometry_cache_dir": geometry_cache_dir,
        "geometry_dxf_dir": geometry_dxf_dir,
        "geometry_fbx_dir": geometry_fbx_dir,
        "geometry_obj_dir": geometry_obj_dir,
        "geometry_usd_dir": geometry_usd_dir,
        "graphics_dir": graphics_dir,
        "matchmoving_dir": matchmoving_dir,
        "miscellaneous_dir": miscellaneous_dir,
        "roto_dir": roto_dir,
        "slates_dir": slates_dir,
        "subtitles_dir": subtitles_dir,
        "tracking_dir": tracking_dir,
        "video_dir": video_dir,
        "rsync_dir": rsync_dir,
        "configs_dir": configs_dir,
        "configs_workstation_dir": configs_workstation_dir,
        "deliverables_dir": deliverables_dir,
        "finals_dir": finals_dir,
        "editorial_dir": editorial_dir,
        "editorial_aaf_dir": editorial_aaf_dir,
        "editorial_edl_dir": editorial_edl_dir,
        "editorial_xml_dir": editorial_xml_dir,
        "shots_dir": shots_dir
    }

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
