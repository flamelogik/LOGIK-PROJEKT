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

# File Name:        sync_python.py
# Version:          1.9.9
# Created:          2024-01-19
# Modified:         2024-12-25

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

# -------------------------------------------------------------------------- #

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

# Function to synchronize python scripts
def sync_python_scripts(
        the_hostname,
        the_projekt_os,
        the_projekts_dir,
        the_projekt_flame_dirs,
        the_adsk_dir,
        the_adsk_dir_linux,
        the_adsk_dir_macos,
        the_projekt_name,
        the_projekt_flame_name,
        the_sanitized_version,
        separator,
    ):
    
    # Nested function to generate backup filename with current date
    def generate_backup_filename(filepath):
        # Get the current date
        date_str = datetime.datetime.now().strftime("%Y_%m_%d")
        # Split the file path into name and extension
        base, ext = os.path.splitext(filepath)
        # Create the backup filename with the date suffix
        return f"{base}.{date_str}.bak"

    # Set the projekt_dir
    the_projekt_dir =f"{the_projekts_dir}/{the_projekt_name}"

    # Set the projekt_flame_dir
    the_projekt_flame_dir =f"{the_projekt_flame_dirs}/{the_projekt_flame_name}"

    # Define the projekt flame setups directory based on the flame version
    if the_sanitized_version.startswith("2025"):
        the_projekt_flame_setups_dir = the_projekt_flame_dir
    else:
        the_projekt_flame_setups_dir = os.path.join(the_projekt_flame_dir, 'setups')

    # # Set the projekt_flame_setups_dir
    # the_projekt_flame_setups_dir = os.path.join(the_projekt_flame_dir, "setups")  # Fix for flame 2026

    # Set the source and target python directories
    src_shared_python_dir = "resources/flame/python"
    tgt_shared_python_dir = "/opt/Autodesk/shared/python"

    print("  synchronizing python directories.\n")

    # Set the umask to 0
    os.umask(0)

    # Set the rsync options
    sync_opts = ["-av"]

    # Use rsync to copy the python scripts
    result = subprocess.run(
        ["rsync"] + sync_opts + [f"{src_shared_python_dir}/", f"{tgt_shared_python_dir}/"],
        text=True,
        capture_output=True
    )

    # Print rsync output
    print(result.stdout.replace('\n', '\n  '))

    print("\n  Logik PROJEKT Python scripts synchronized.")
    # print("\n" + separator + "\n")

    # # Remove older man_made_material python directories if they exist
    # man_made_material_dir = os.path.join(tgt_shared_python_dir, "man_made_material")
    # if os.path.isdir(man_made_material_dir):
    #     print("  removing older python directories.\n")
    #     shutil.rmtree(man_made_material_dir)

# ========================================================================== #
# This section defines how to handle the main script function.
# ========================================================================== #

def main():
    # Example values for the function arguments
    sync_opts = ["-av"]  # Update with actual rsync options
    separator = "-" * 80

    # Call the function to synchronize Python scripts
    sync_python_scripts(
        the_hostname,
        the_projekt_os,
        the_projekts_dir,
        the_projekt_flame_dirs,
        the_adsk_dir,
        the_adsk_dir_linux,
        the_adsk_dir_macos,
        the_projekt_name,
        the_projekt_flame_name,
        the_sanitized_version,
        separator,
    )

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
# Version:          1.9.9
# modified:         2024-12-25 - 09:50:15
# comments:         Preparation for future features
# -------------------------------------------------------------------------- #
