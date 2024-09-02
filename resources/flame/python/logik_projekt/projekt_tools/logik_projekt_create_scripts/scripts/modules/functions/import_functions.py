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

# File Name:        import_functions.py
# Version:          2.2.7
# Created:          2024-01-19
# Modified:         2024-08-31

# ========================================================================== #
# This section imports the necessary modules.
# ========================================================================== #

# import flame
import os
# import pdb; pdb.set_trace()
# import re
import fileinput
# import logging
# from datetime import datetime

# ========================================================================== #
# This section imports the external functions.
# ========================================================================== #

# # EXAMPLE:
# from modules.functions.example import (
#     example_function as new_function_name
# )

# from debugging_and_logging import (
#     debugging_and_logging as debugging_and_logging 
# )
# from define_job_structure import (
#     define_job_structure as define_job_structure 
# )
# from list_shots_dir import (
#     list_shots_dir as list_shots_dir 
# )
# from define_shot_structure import (
#     define_shot_structure as define_shot_structure 
# )
# from list_shot_sources_dir import (
#     list_shot_sources_dir as list_shot_sources_dir 
# )
# from list_shot_source_dir import (
#     list_shot_source_dir as list_shot_source_dir 
# )
# from path_to_shot_source_openexr_sequences import (
#     path_to_shot_source_openexr_sequences as path_to_shot_source_openexr_sequences 
# )
# from create_openclip_output_clip import (
#     create_openclip_output_clip as create_openclip_output_clip 
# )
# from create_openclip_segment_clip import (
#     create_openclip_segment_clip as create_openclip_segment_clip 
# )
# from create_blender_shot_script import (
#     create_blender_shot_script as create_blender_shot_script 
# )
# from create_blender_source_script import (
#     create_blender_source_script as create_blender_source_script 
# )
# from create_nuke_shot_script import (
#     create_nuke_shot_script as create_nuke_shot_script 
# )
# from create_nuke_source_script import (
#     create_nuke_source_script as create_nuke_source_script 
# )
# from process_shot_info import (
#     process_shot_info as process_shot_info
# )

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
