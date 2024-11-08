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

# File Name:        logik_projekt_imports.py
# Version:          0.9.9
# Created:          2024-01-19
# Modified:         2024-08-31

# ========================================================================== #
# This section defines the import statements and directory paths.
# ========================================================================== #

# Standard library imports
import argparse
import ast
import base64
import collections
import datetime
import getpass
import grp
import importlib
import io
import json
import os
import platform
import re
import shutil
import socket
import subprocess
import sys
import unittest
import xml

# -------------------------------------------------------------------------- #

def get_base_path():
    if getattr(sys, 'frozen', False):
        return sys._MEIPASS
    else:
        return os.path.abspath(
            os.path.join(
                os.path.dirname(__file__), '..', '..', '..'
            )
        )
    
# -------------------------------------------------------------------------- #

def get_resource_path(relative_path):
    base_path = get_base_path()
    return os.path.join(
        base_path,
        relative_path
    )

# -------------------------------------------------------------------------- #

# Set the path to the 'modules' directory
modules_dir = get_resource_path('modules')
# Set the path to the 'resources' directory
resources_dir = get_resource_path('resources')
# Append the modules path to the system path
if modules_dir not in sys.path:
    sys.path.append(modules_dir)

# ========================================================================== #
# This section defines third party imports.
# ========================================================================== #

# Local Application/Library Specific Imports

# Import the shell decoration functions
from functions.shell.shell_decorators import (
    create_separator,
    banner_head,
    banner_tail,
)

# Import the shell utility functions
from functions.shell.shell_utilities import (
    TimestampUtility
)

# Import the shell logging functions
from functions.shell.shell_logging import (
    ShellLogger
)

# -------------------------------------------------------------------------- #

# Import the create_xml_file function
from functions.create.create_parameters_xml import (
    create_xml_file
)

# Import the run_wiretap_create_node function
from functions.wiretap.wiretap_create_node import (
    run_wiretap_create_node
)

# -------------------------------------------------------------------------- #

# Import the create_projekt_dirs function
from functions.create.create_projekt_dirs import (
    create_the_projekt_directories
)

# Import the create_the_projekt_flame_directories function
from functions.create.create_projekt_flame_dirs import (
    create_the_projekt_flame_directories
)

# Import the symlink_iterations_dir function
from functions.link.link_iterations_dir import (
    symlink_iterations_dir
)

# Import the symlink_subdirectories function
from functions.link.link_subdirectories import (
    symlink_subdirectories
)

# Import the template_directory_path for init_configs
from widgets.combo_box.items_init_config import (
    template_directory_path
)

# -------------------------------------------------------------------------- #

# Import the sync_archive_prefs function
from functions.synchronize.sync_archive_prefs import (
    sync_archive_prefs
)

# Import the sync_batch_project_bins function
from functions.synchronize.sync_batch import (
    sync_batch_project_bins
)

# Import the update_flame_colortoolkit_bookmarks function
from functions.update.update_flame_colortoolkit_bookmarks import (
    update_flame_colortoolkit_bookmarks
)

# Import the sync_bookmarks function
from functions.synchronize.sync_bookmarks import (
    sync_bookmarks
)

# Import the sync_overlays function
from functions.synchronize.sync_burnmetadata import (
    sync_overlays
)

# Import the sync_io_presets function
from functions.synchronize.sync_io import (
    sync_io_presets
)

# Import the sync_media_import_rules function
from functions.synchronize.sync_media_import import (
    sync_media_import_rules
)

# Import the sync_mediahub_rules function
from functions.synchronize.sync_mediahub import (
    sync_mediahub_rules
)

# Import the sync_mediaimport_rules function
from functions.synchronize.sync_mediaImport import (
    sync_mediaimport_rules
)

# # Import the sync_overlays function  # DIFFERENT TO BURNIN METADATA OVERLAYS
# from functions.synchronize.sync_overlays import (
#     sync_overlays
# )

# Import the sync_python_scripts function
from functions.synchronize.sync_python import (
    sync_python_scripts
)

# Import the sync_color_policies function
from functions.synchronize.sync_syncolor_policies import (
    sync_color_policies
)

# Import the sync_color_transforms function
from functions.synchronize.sync_syncolor_transforms import (
    sync_color_transforms
)

# Import the add_syncolor_policy function
from functions.wiretap.wiretap_add_color_policy import (
    add_syncolor_policy
)

# Import the add_syncolor_policy function
from functions.create.create_launcher_script import (
    create_projekt_flame_launcher_script
)

# -------------------------------------------------------------------------- #

# Import the create_projekt_flame_archive_script function
from functions.create.create_archive_script import (
    create_projekt_flame_archive_script
)

# Import the create_projekt_backup_script function
from functions.create.create_backup_script import (
    create_projekt_backup_script
)

# Import the backup_projekt_template function
from functions.backup.backup_projekt_template import (
    backup_projekt_template
)

# Import the backup_projekt_parameters_xml function
from functions.backup.backup_projekt_parameters import (
    backup_projekt_parameters_xml
)

# Import the backup_projekt_creation_log function
from functions.backup.backup_creation_log import (
    backup_projekt_creation_log
)

# ========================================================================== #
# This section defines how to handle the main script function.
# ========================================================================== #

if __name__ == "__main__":
    main()

# ========================================================================== #
# C2 A9 32 30 32 34 2D 4D 41 4E 2D 4D 41 44 45 2D 4D 45 4B 41 4E 59 5A 4D 53 #
# ========================================================================== #

# Changelist:       

# -------------------------------------------------------------------------- #
# version:          0.0.1
# created:          2024-01-19 - 12:34:56
# comments:         scripts to create flame projekts, presets & templates.
# -------------------------------------------------------------------------- #
# version:          0.1.0
# modified:         2024-04-20 - 16:20:00
# comments:         refactored monolithic program into separate functions.
# -------------------------------------------------------------------------- #
# version:          0.5.0
# modified:         2024-05-24 - 20:24:00
# comments:         merged flame_colortoolkit with projekt.
# -------------------------------------------------------------------------- #
# version:          0.6.0
# modified:         2024-05-25 - 15:00:03
# comments:         started conversion to python3.
# -------------------------------------------------------------------------- #
# version:          0.7.0
# modified:         2024-06-21 - 18:21:03
# comments:         started gui design with pyside6.
# -------------------------------------------------------------------------- #
# version:          0.9.9
# modified:         2024-08-31 - 16:51:09
# comments:         prep for release - code appears to be functional
# -------------------------------------------------------------------------- #
