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

# File Name:        create_logik_projekt.py
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

# # Import all third-party imports from third_party_imports.py
# from functions.import_statements.logik_projekt_imports import (
#     create_separator,
#     banner_head,
#     banner_tail,
#     TimestampUtility,
#     ShellLogger,
#     create_xml_file,
#     run_wiretap_create_node,
#     create_the_projekt_directories,
#     create_the_projekt_flame_directories,
#     symlink_iterations_dir,
#     symlink_subdirectories,
#     template_directory_path,
#     sync_archive_prefs,
#     sync_batch_project_bins,
#     update_flame_colortoolkit_bookmarks,
#     sync_bookmarks,
#     sync_overlays,
#     sync_io_presets,
#     sync_media_import_rules,
#     sync_mediahub_rules,
#     sync_mediaimport_rules,
#     sync_python_scripts,
#     sync_color_policies,
#     sync_color_transforms,
#     add_syncolor_policy,
#     create_projekt_flame_launcher_script,
#     create_projekt_flame_archive_script,
#     create_projekt_backup_script,
#     backup_projekt_template,
#     backup_projekt_parameters_xml,
#     backup_projekt_creation_log
# )

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

# # Import the sync_nuke_dirs function
# from functions.synchronize.sync_nuke_dirs import (
#     sync_nuke_dirs
# )

# # Import the sync_overlays function  # DIFFERENT TO BURNIN METADATA OVERLAYS
# from functions.synchronize.sync_overlays import (
#     sync_overlays
# )

# # Import the sync_editorial_tree_premiere function
# from functions.synchronize.sync_editorial_tree_premiere import (
#     sync_editorial_tree_premiere
# )

# -------------------------------------------------------------------------- #

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
# This section defines environment specific variables.
# ========================================================================== #

# These paths should be passed from the main app.
the_hostname = "delta"
the_projekt_os = "Linux"
the_software_version = "flame_2025.1.pr199"
the_sanitized_version = "2025_1"
the_framestore = "stonefs"

'''
Print the variables for debugging
print(f"  Debug: the_hostname:              {the_hostname}")
print(f"  Debug: the_projekt_os:            {the_projekt_os}")
print(f"  Debug: the_software_version:      {the_software_version}")
print(f"  Debug: the_sanitized_version:     {the_sanitized_version}")
'''

# ========================================================================== #
# This section defines common paths.
# ========================================================================== #

projekt_roots_config_path = os.path.join(
    resources_dir,
    'cfg',
    'projekt_configuration',
    'roots',
    'projekt_roots.json'
)

# Read the JSON configuration file
try:
    with open(projekt_roots_config_path, 'r') as config_file:
        config = json.load(config_file)
except Exception as e:
    print(f"  Error reading JSON configuration file: {e}")
    config = {}

# Define common directory paths
the_projekts_dir = config.get(
    'the_projekts_dir',
    "/PROJEKTS"
)

the_projekt_flame_dirs = config.get(
    'the_projekt_flame_dirs',
    "/opt/Autodesk/project"
)

the_adsk_dir = config.get(
    'the_adsk_dir',
    "/opt/Autodesk"
)

the_adsk_dir_linux = config.get(
    'the_adsk_dir_linux',
    "/opt/Autodesk"
)

the_adsk_dir_macos = config.get(
    'the_adsk_dir_macos',
    "/Applications/Autodesk"
)

'''
Print the variables for debugging
print(f"  Debug: projekt_roots_config_path: {projekt_roots_config_path}")
print(f"  Debug: the_projekts_dir:          {the_projekts_dir}")
print(f"  Debug: the_projekt_flame_dirs:    {the_projekt_flame_dirs}")
print(f"  Debug: the_adsk_dir:              {the_adsk_dir}")
print(f"  Debug: the_adsk_dir_linux:        {the_adsk_dir_linux}")
print(f"  Debug: the_adsk_dir_macos:        {the_adsk_dir_macos}")
'''

# ========================================================================== #
# This section defines projekt specific paths.
# ========================================================================== #

# These paths should be passed from the main app.
the_projekt_name = "8888_new_job"
the_projekt_flame_name = f"{the_projekt_name}_{the_sanitized_version}_{the_hostname}"

separator = '# ' + '-' * 75 + ' #'

# ========================================================================== #
# This section defines the primary functions for the script.
# ========================================================================== #

def main():
    # Create a separator
    separator = create_separator()

    # Read JSON data from stdin
    input_data = sys.stdin.read()
    the_projekt_information = json.loads(input_data)

    # Define the log file path
    log_file_path = 'resources/tmp/current_projekt_creation_log'

    # Ensure the directory exists
    os.makedirs(os.path.dirname(log_file_path), exist_ok=True)

    # Use the ShellLogger in a with statement to ensure proper closure
    with ShellLogger(log_file_path) as logger:

        # # Redirect sys.stdout and sys.stderr to the logger
        # sys.stdout = logger
        # sys.stderr = logger

        # Set the timestamps
        datestamp = TimestampUtility.timestamp_date()
        timestamp = TimestampUtility.timestamp_time()

        #Gather all of the projekt information variables and values
        the_projekt_serial_number = the_projekt_information.get('the_projekt_serial_number')
        the_projekt_client_name = the_projekt_information.get('the_projekt_client_name')
        the_projekt_campaign_name = the_projekt_information.get('the_projekt_campaign_name')
        the_projekt_name = the_projekt_information.get('the_projekt_name')
        the_projekt_resolution = the_projekt_information.get('the_projekt_resolution')
        the_projekt_width = the_projekt_information.get('the_projekt_width')
        the_projekt_height = the_projekt_information.get('the_projekt_height')
        the_projekt_storage_aspect_ratio = the_projekt_information.get('the_projekt_storage_aspect_ratio')
        the_projekt_display_aspect_ratio = the_projekt_information.get('the_projekt_display_aspect_ratio')
        the_projekt_pixel_aspect_ratio = the_projekt_information.get('the_projekt_pixel_aspect_ratio')
        the_projekt_aspect_ratio = the_projekt_information.get('the_projekt_aspect_ratio')
        the_projekt_bit_depth = the_projekt_information.get('the_projekt_bit_depth')
        the_projekt_frame_rate = the_projekt_information.get('the_projekt_frame_rate')
        the_projekt_scan_mode = the_projekt_information.get('the_projekt_scan_mode')
        the_projekt_start_frame = the_projekt_information.get('the_projekt_start_frame')
        the_projekt_init_config = the_projekt_information.get('the_projekt_init_config')
        the_projekt_color_science = the_projekt_information.get('the_projekt_color_science')
        the_projekt_user_name = the_projekt_information.get('the_projekt_user_name')
        the_projekt_primary_group = the_projekt_information.get('the_projekt_primary_group')
        the_projekt_os = the_projekt_information.get('the_projekt_os')
        the_hostname = the_projekt_information.get('the_hostname')
        the_projekt_localhostname = the_projekt_information.get('the_projekt_localhostname')
        the_projekt_computername = the_projekt_information.get('the_projekt_computername')
        the_software_version = the_projekt_information.get('the_software_version')
        the_framestore = the_projekt_information.get('the_framestore')
        the_sanitized_sw_ver = the_projekt_information.get('the_sanitized_sw_ver')
        the_sanitized_version = the_projekt_information.get('the_sanitized_version')
        the_projekt_flame_name = the_projekt_information.get('the_projekt_flame_name')

        # ------------------------------------------------------------------ #

        # Define the XML file path
        projekt_xml_path = 'resources/tmp/current_projekt_parameters.xml'

        the_projekt_dir = the_projekt_information.get('the_projekt_name')
        the_projekt_flame_dir = the_projekt_information.get('the_projekt_flame_name')

        bookmarks_file = 'resources/tmp/current_projekt_bookmarks.json'
        tmp_bookmarks_file = 'resources/tmp/tmp_bookmarks.json'

        the_projekt_dirs_json_dir = 'resources/cfg/projekt_configuration/tree/projekt'
        # the_projekt_dirs_json_files = [os.path.join(the_projekt_dirs_json_dir, file) for file in os.listdir(the_projekt_dirs_json_dir) if file.endswith('.json')]
        the_projekt_dirs_json_files = sorted(
            [os.path.join(the_projekt_dirs_json_dir, file) for file in os.listdir(the_projekt_dirs_json_dir) if file.endswith('.json')]
        )

        # Call the create_the_projekt_flame_directories function
        the_flame_dirs_json_file = 'resources/cfg/projekt_configuration/tree/flame/flame_setup_dirs.json'

        # ------------------------------------------------------------------ #

        # Print a banner head
        logger.log_and_print(f"{banner_head('Creating Projekt')}")

        # Replace all instances of log_and_print with print
        logger.log_and_print(f"{separator}")
        logger.log_and_print(f"  projekt: {the_projekt_name}")
        logger.log_and_print(f"\n{separator}")
        logger.log_and_print(f"  hostname: {the_hostname}")
        logger.log_and_print(f"  host OS: {the_projekt_os}")
        logger.log_and_print(f"  username: {the_projekt_user_name}")
        logger.log_and_print(f"  groupname: {the_projekt_primary_group}")
        logger.log_and_print(f"  flame ver: {the_software_version}")
        logger.log_and_print(f"  framestore: {the_framestore}")
        logger.log_and_print(f"  datestamp: {datestamp}")
        logger.log_and_print(f"  timestamp: {timestamp}")
        # logger.log_and_print(f"\n\n{separator}\n")

        # ------------------------------------------------------------------ #

        # Print a banner head
        logger.log_and_print(f"{banner_head('The Projekt Information')}")

        # Print each variable from the_projekt_information
        for key, value in the_projekt_information.items():
            logger.log_and_print(f"  {key}: {value}")

        # Print a separator
        logger.log_and_print(f"\n{separator}")

        # ------------------------------------------------------------------ #

        # Print a banner head
        logger.log_and_print(f"{banner_head('Creating Projekt XML File')}")

        # Call the create_xml_file function
        create_xml_file(the_projekt_information, projekt_xml_path, logger)

        # Print a separator
        logger.log_and_print(f"\n{separator}")

        # ------------------------------------------------------------------ #

        # Print a banner head
        logger.log_and_print(f"{banner_head('Creating Flame Projekt')}")

        # Call the run_wiretap_create_node function
        run_wiretap_create_node(the_projekt_flame_name, projekt_xml_path, separator)

        # Print a separator
        logger.log_and_print(f"\n{separator}")

        # ------------------------------------------------------------------ #

        # Print a banner head
        logger.log_and_print(f"{banner_head('Creating Projekt Directories')}")

        # Call the create_projekt_dirs function
        create_the_projekt_directories(
            the_projekts_dir,
            the_projekt_name,
            the_projekt_flame_dir,
            bookmarks_file,
            tmp_bookmarks_file,
            the_projekt_dirs_json_dir,
            the_projekt_dirs_json_files,
        )

        # Print a separator
        logger.log_and_print(f"\n{separator}")

        # ------------------------------------------------------------------ #

        # Print a banner head
        logger.log_and_print(f"{banner_head('Creating Flame Directories')}")

        # Call the create_the_projekt_flame_directories function
        create_the_projekt_flame_directories(
            the_flame_dirs_json_file,
            the_projekt_flame_dirs,
            the_projekt_flame_dir,
            # logger
        )

        # Print a separator
        logger.log_and_print(f"\n{separator}")

        # ------------------------------------------------------------------ #

        # Print a banner head
        logger.log_and_print(f"\n{banner_head('Linking Batch Iterations Directory')}")

        # Link the batch iterations directory
        symlink_iterations_dir(
            the_projekts_dir,
            the_projekt_dir,
            the_projekt_flame_dirs,
            the_projekt_flame_dir
        )

        # Print a separator
        logger.log_and_print(f"\n{separator}")

        # ------------------------------------------------------------------ #

        # Print a banner head
        logger.log_and_print(f"{banner_head('Linking Flame Setup Directories')}")

        # Linking Flame Setup Directories
        symlink_subdirectories(
            the_projekts_dir,
            the_projekt_dir,
            the_projekt_flame_dirs,
            the_projekt_flame_dir,
            the_sanitized_version,
            the_hostname
        )

        # Print a separator
        logger.log_and_print(f"\n{separator}")

        # ------------------------------------------------------------------ #

        # Print a banner head
        logger.log_and_print(f"{banner_head('Copying Init Config to flame projekt')}")

        # Copy the init config to the flame projekt
        the_src_projekt_init_config = f"{template_directory_path}/{the_projekt_init_config}"
        the_tgt_projekt_init_config = f"{the_projekt_flame_dirs}/{the_projekt_flame_dir}/cfg/{the_projekt_flame_name}.cfg"
        logger.log_and_print(f"Copying file from {the_src_projekt_init_config} to {the_tgt_projekt_init_config}")

        shutil.copyfile(the_src_projekt_init_config, the_tgt_projekt_init_config)

        # Print a separator
        logger.log_and_print(f"\n{separator}")

        # ------------------------------------------------------------------ #

        # Print a banner head
        logger.log_and_print(f"{banner_head('Copying Archive Prefs')}")

        # Function to create archive defaults for 'Convert to Local Path'
        sync_archive_prefs(
            the_projekts_dir,
            the_projekt_flame_dirs,
            the_adsk_dir,
            the_adsk_dir_linux,
            the_adsk_dir_macos,
            the_projekt_name,
            the_projekt_flame_name,
            separator
        )

        # Print a separator
        logger.log_and_print(f"\n{separator}")

        # ------------------------------------------------------------------ #

        # Print a banner head
        logger.log_and_print(f"{banner_head('Copying Batch Project Bins')}")

        # Function to copy batch project bins
        sync_batch_project_bins(
            the_projekts_dir,
            the_projekt_flame_dirs,
            the_adsk_dir,
            the_adsk_dir_linux,
            the_adsk_dir_macos,
            the_projekt_name,
            the_projekt_flame_name,
            separator
        )

        # Print a separator
        logger.log_and_print(f"\n{separator}")


        # ------------------------------------------------------------------ #

        # Print a banner head
        logger.log_and_print(f"{banner_head('Updating Flame ColorToolkit Bookmarks')}")

        tgt_projekt_policies_dir = os.path.join(the_projekts_dir, the_projekt_dir, "utilities", "Synergy", "SynColor", "Shared", "policies")
        tgt_projekt_transforms_dir = os.path.join(the_projekts_dir, the_projekt_dir, "utilities", "Synergy", "SynColor", "Shared", "transforms")

        # Define the new bookmarks to be added
        flame_colortoolkit_bookmarks = [
            {
                "Bookmark": "flame_colortoolkit (linux)",
                "Path": "/opt/Autodesk/Synergy/SynColor/Shared/transforms/flame_colortoolkit",
                "Visibility": "Global"
            },
            {
                "Bookmark": "flame_colortoolkit (macos)",
                "Path": "/Applications/Autodesk/Synergy/SynColor/Shared/transforms/flame_colortoolkit",
                "Visibility": "Global"
            }
        ]

        # # Define the new bookmarks to be added
        # flame_colortoolkit_bookmarks = [
        #     {
        #         "Bookmark": "flame_colortoolkit",
        #         "Path": f"{tgt_projekt_transforms_dir}/flame_colortoolkit",
        #         "Visibility": "Global"
        #     }
        # ]

        # Function to copy batch project bins
        update_flame_colortoolkit_bookmarks(
            bookmarks_file,
            flame_colortoolkit_bookmarks,
            tgt_projekt_transforms_dir,
        )

        # Print a separator
        logger.log_and_print(f"\n{separator}")

        # ------------------------------------------------------------------ #

        # Print a banner head
        logger.log_and_print(f"{banner_head('Copying Projekt Bookmarks')}")

        # Function to copy projekt bookmarks
        sync_bookmarks(
            the_projekts_dir,
            the_projekt_flame_dirs,
            the_adsk_dir,
            the_adsk_dir_linux,
            the_adsk_dir_macos,
            the_projekt_name,
            the_projekt_flame_name,
            separator
        )

        # Print a separator
        logger.log_and_print(f"\n{separator}")

        # ------------------------------------------------------------------ #

        # Print a banner head
        logger.log_and_print(f"{banner_head('Copying Burnin MetaData Presets')}")

        # Function to copy burnin metadata presets
        sync_overlays(
            the_projekts_dir,
            the_projekt_flame_dirs,
            the_adsk_dir,
            the_adsk_dir_linux,
            the_adsk_dir_macos,
            the_projekt_name,
            the_projekt_flame_name,
            separator
        )

        # Print a separator
        logger.log_and_print(f"\n{separator}")

        # ------------------------------------------------------------------ #

        # Print a banner head
        logger.log_and_print(f"{banner_head('Copying Export / Import Presets')}")

        # Function to copy io presets
        sync_io_presets(
            the_projekts_dir,
            the_projekt_flame_dirs,
            the_adsk_dir,
            the_adsk_dir_linux,
            the_adsk_dir_macos,
            the_projekt_name,
            the_projekt_flame_name,
            separator
        )

        # Print a separator
        logger.log_and_print(f"\n{separator}")

        # ------------------------------------------------------------------ #

        # Print a banner head
        logger.log_and_print(f"{banner_head('Copying Media Import Rules')}")

        # Function to copy media import rules
        sync_media_import_rules(
            the_projekts_dir,
            the_projekt_flame_dirs,
            the_adsk_dir,
            the_adsk_dir_linux,
            the_adsk_dir_macos,
            the_projekt_name,
            the_projekt_flame_name,
            separator
        )

        # Print a separator
        logger.log_and_print(f"\n{separator}")

        # ------------------------------------------------------------------ #

        # Print a banner head
        logger.log_and_print(f"{banner_head('Copying MediaHub Rules')}")

        # Function to copy mediahub rules
        sync_mediahub_rules(
            the_projekts_dir,
            the_projekt_flame_dirs,
            the_adsk_dir,
            the_adsk_dir_linux,
            the_adsk_dir_macos,
            the_projekt_name,
            the_projekt_flame_name,
            separator
        )

        # Print a separator
        logger.log_and_print(f"\n{separator}")

        # ------------------------------------------------------------------ #

        # Print a banner head
        logger.log_and_print(f"{banner_head('Copying MediaImport Rules')}")

        # Function to copy mediaimport rules
        sync_mediaimport_rules(
            the_projekts_dir,
            the_projekt_flame_dirs,
            the_adsk_dir,
            the_adsk_dir_linux,
            the_adsk_dir_macos,
            the_projekt_name,
            the_projekt_flame_name,
            separator
        )

        # Print a separator
        logger.log_and_print(f"\n{separator}")

        # ------------------------------------------------------------------ #

        # # Print a banner head
        # logger.log_and_print(f"{banner_head('Copying Nuke Directories')}")

        # # Function to copy nuke directories
        # sync_nuke_dirs(
        #     the_projekts_dir,
        #     the_projekt_flame_dirs,
        #     the_adsk_dir,
        #     the_adsk_dir_linux,
        #     the_adsk_dir_macos,
        #     the_projekt_name,
        #     the_projekt_flame_name,
        #     separator
        # )

        # # Print a separator
        # logger.log_and_print(f"\n{separator}")

        # ------------------------------------------------------------------ #

        # # Print a banner head
        # logger.log_and_print(f"{banner_head('Creating Editorial Structure - Premiere')}")

        # # # Function to create editorial directory structure - premiere
        # # sync_editorial_tree_premiere(
        # #     the_projekts_dir,
        # #     the_projekt_flame_dirs,
        # #     the_adsk_dir,
        # #     the_adsk_dir_linux,
        # #     the_adsk_dir_macos,
        # #     the_projekt_name,
        # #     the_projekt_flame_name,
        # #     separator
        # # )

        # # Function to create editorial directory structure - premiere
        # sync_editorial_tree_premiere(
        #     the_projekts_dir,
        #     the_projekt_name,
        #     the_projekt_flame_name,
        #     separator
        # )

        # # Print a separator
        # logger.log_and_print(f"\n{separator}")

        # # # ------------------------------------------------------------------ #

        # Print a banner head
        logger.log_and_print(f"{banner_head('Copying Python Scripts')}")

        # Function to copy python scripts
        sync_python_scripts(
            the_projekts_dir,
            the_projekt_flame_dirs,
            the_adsk_dir,
            the_adsk_dir_linux,
            the_adsk_dir_macos,
            the_projekt_name,
            the_projekt_flame_name,
            separator
        )

        # Print a separator
        logger.log_and_print(f"\n{separator}")

        # ------------------------------------------------------------------ #

        # Set the_projekt_os
        the_projekt_os = the_projekt_information.get('the_projekt_os')

        # Print a banner head
        logger.log_and_print(f"{banner_head('Copying Syncolor Policies')}")

        # Function to copy syncolor policies
        sync_color_policies(
            the_projekts_dir,
            the_projekt_flame_dirs,
            the_adsk_dir,
            the_adsk_dir_linux,
            the_adsk_dir_macos,
            the_projekt_name,
            the_projekt_flame_name,
            separator,
            the_projekt_os
        )

        # Print a separator
        logger.log_and_print(f"\n{separator}")

        # ------------------------------------------------------------------ #

        # Print a banner head
        logger.log_and_print(f"{banner_head('Copying Syncolor Transforms')}")

        # Function to copy syncolor transforms
        sync_color_transforms(
            the_projekts_dir,
            the_projekt_flame_dirs,
            the_adsk_dir,
            the_adsk_dir_linux,
            the_adsk_dir_macos,
            the_projekt_name,
            the_projekt_flame_name,
            separator,
            the_projekt_os
        )

        # Print a separator
        logger.log_and_print(f"\n{separator}")

        # ------------------------------------------------------------------ #

        # Print a banner head
        logger.log_and_print(f"{banner_head('Add Syncolor Policy')}")

        # Function to add_syncolor_policy
        add_syncolor_policy(
            the_projekt_color_science,
            the_projekt_flame_name,
            separator,
        )

        # ------------------------------------------------------------------ #

        # Print a banner head
        logger.log_and_print(f"{banner_head('Creating a flame archiving script')}")

        # Function to create_projekt_flame_archive_script
        create_projekt_flame_archive_script(
            the_projekts_dir,
            the_projekt_flame_dirs,
            the_adsk_dir,
            the_adsk_dir_linux,
            the_adsk_dir_macos,
            the_projekt_name,
            the_projekt_flame_name,
            the_hostname,
            separator,
        )

        # Print a separator
        logger.log_and_print(f"\n{separator}")

        # ------------------------------------------------------------------ #

        # Print a banner head
        logger.log_and_print(f"{banner_head('Creating an rsync backup script')}")

        # Function to create_projekt_backup_script
        create_projekt_backup_script(
            the_projekts_dir,
            the_projekt_flame_dirs,
            the_adsk_dir,
            the_adsk_dir_linux,
            the_adsk_dir_macos,
            the_projekt_name,
            the_projekt_flame_name,
            the_hostname,
            separator,
        )

        # Print a separator
        logger.log_and_print(f"\n{separator}")

        # ------------------------------------------------------------------ #

        # Print a banner head
        logger.log_and_print(f"{banner_head('Creating a flame launcher script')}")

        # Function to create_projekt_flame_launcher_script
        create_projekt_flame_launcher_script(
                the_projekts_dir,
                the_projekt_flame_dirs,
                the_adsk_dir,
                the_adsk_dir_linux,
                the_adsk_dir_macos,
                the_projekt_name,
                the_projekt_flame_name,
                the_hostname,
                separator,
                the_software_version
            )

        # Print a separator
        logger.log_and_print(f"\n{separator}")

        # ------------------------------------------------------------------ #

        # Print a banner head
        logger.log_and_print(f"{banner_head('Backing up Projekt Flame XML')}")

        # Function to backup flame project parameters xml
        backup_projekt_parameters_xml(
            the_projekts_dir,
            the_projekt_flame_dirs,
            the_adsk_dir,
            the_adsk_dir_linux,
            the_adsk_dir_macos,
            the_projekt_name,
            the_projekt_flame_name,
            the_hostname,
            separator,
        )

        # Print a separator
        logger.log_and_print(f"\n{separator}")

        # ------------------------------------------------------------------ #

        # Print a banner head
        logger.log_and_print(f"{banner_head('Backing up Projekt Template')}")

        # Function to back up the projekt template
        backup_projekt_template(
            the_projekts_dir,
            the_projekt_flame_dirs,
            the_adsk_dir,
            the_adsk_dir_linux,
            the_adsk_dir_macos,
            the_projekt_name,
            the_projekt_flame_name,
            the_hostname,
            separator,
        )

        # Print a separator
        logger.log_and_print(f"\n{separator}")

        # ------------------------------------------------------------------ #

        # Print a banner head
        logger.log_and_print(f"{banner_head('Backing up Projekt Creation Log')}")

        # Function to back up the projekt creation log
        backup_projekt_creation_log(
            the_projekts_dir,
            the_projekt_flame_dirs,
            the_adsk_dir,
            the_adsk_dir_linux,
            the_adsk_dir_macos,
            the_projekt_name,
            the_projekt_flame_name,
            the_hostname,
            separator,
        )

        # Print a separator
        logger.log_and_print(f"\n{separator}")

        # ------------------------------------------------------------------ #

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
