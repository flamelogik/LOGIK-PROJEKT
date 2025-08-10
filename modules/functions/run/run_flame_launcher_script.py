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

# File Name:        run_flame_launcher_script.py
# Version:          2.0.0
# Created:          2024-01-19
# Modified:         2024-12-31

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

        # Define the paths and files for create_projekt_dirs
        # the_projekt_name = the_projekt_information.get('the_projekt_name')  # Already defined above

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
        logger.log_and_print(f"{banner_head('Creating a custom flame launcher')}")

        # Path to the launcher script directory
        the_projekt_flame_launcher_dir = f"{the_projekts_dir}/{the_projekt_name}/cfg/workstation/{the_hostname}"

        # Path to the Bash script
        the_flame_launcher_script = f"{the_projekt_flame_launcher_dir}/{the_projekt_name}-flame_launcher-{the_hostname}.sh"

        # Execute the Bash script
        subprocess.run([the_flame_launcher_script])

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
# version:          1.9.9
# modified:         2024-12-25 - 09:50:14
# comments:         Preparation for future features
# -------------------------------------------------------------------------- #
# version:          2.0.0
# modified:         2024-12-31 - 11:17:18
# comments:         Improved legibility and minor modifications
# -------------------------------------------------------------------------- #
