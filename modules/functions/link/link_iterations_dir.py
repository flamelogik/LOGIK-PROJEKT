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

# File Name:        link_iterations_dir.py
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

def symlink_iterations_dir(
        the_projekts_dir,
        the_projekt_dir,
        the_projekt_flame_dirs,
        the_projekt_flame_dir,
        the_sanitized_version,
    ):

# --------------- ENABLE THIS FUNCTION FOR FLAME 2025 ---------------------- #

    # # Define the projekt flame setups directory for flame 2025
    # the_projekt_flame_setups_dir = the_projekt_flame_dir

# --------------- ENABLE THIS FUNCTION FOR FLAME 2026 ---------------------- #

    # Define the projekt flame setups directory based on the flame version
    the_projekt_flame_setups_dir = os.path.join(
        the_projekt_flame_dir,
        'setups'
    )

    # # Experimental shit that keeps changing
    # if the_sanitized_version.startswith("2025"):
    #     the_projekt_flame_setups_dir = the_projekt_flame_dir
    # else:
    #     the_projekt_flame_setups_dir = os.path.join(
    #         the_projekt_flame_dir,
    #         'setups'
    #     )

# -------------------------------------------------------------------------- #

    """
    Create a symbolic link from the flame iterations directory
    to the projekt flame batch directory.
    """
    source_path = os.path.abspath(
        os.path.join(
            the_projekts_dir,
            the_projekt_dir,
            "flame",
            "iterations"
        )
    )

    target_path = os.path.abspath(
        os.path.join(
            the_projekt_flame_dirs,
            the_projekt_flame_setups_dir,
            "batch",
            "flame",
            "iterations"
        )
    )
   
    print(f"  Linking batch iterations directory\n")
    print(f"  from: {source_path}")
    print(f"  to:   {target_path}\n")
   
    if not os.path.exists(source_path):
        print(f"  Source path does not exist: {os.path.basename(source_path)}")
        return
   
    os.makedirs(os.path.dirname(target_path), exist_ok=True)
   
    try:
        if os.path.lexists(target_path):
            print(f"  Removing existing link: {os.path.basename(target_path)}")
            os.remove(target_path)
       
        os.symlink(source_path, target_path)
        print(f"  Successfully linked: {os.path.basename(source_path)} -> {os.path.basename(target_path)}\n")
    except Exception as e:
        print(f"  Error creating symbolic link for iterations: {e}")

# ========================================================================== #
# This section defines how to handle the main script function.
# ========================================================================== #

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Create symbolic link for iterations directory.")
    parser.add_argument("--the_projekts_dir", required=True, help="Path to the projects directory")
    parser.add_argument("--the_projekt_dir", required=True, help="Name of the project directory")
    parser.add_argument("--the_projekt_flame_dirs", required=True, help="Path to the project flame directories")
    parser.add_argument("--the_projekt_flame_dir", required=True, help="Name of the project flame directory")
    args = parser.parse_args()

    symlink_iterations_dir(
        args.the_projekts_dir,
        args.the_projekt_dir,
        args.the_projekt_flame_dirs,
        args.the_projekt_flame_dir
    )

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
# modified:         2024-12-25 - 09:50:13
# comments:         Preparation for future features
# -------------------------------------------------------------------------- #
# version:          2.0.0
# modified:         2024-12-31 - 11:17:18
# comments:         Improved legibility and minor modifications
# -------------------------------------------------------------------------- #
