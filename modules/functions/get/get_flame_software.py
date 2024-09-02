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

# File Name:        get_flame_software.py
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

# Ensure the root of the project is in the system path
sys.path.append(
    os.path.abspath(
        os.path.join(
            os.path.dirname(__file__), '../../../../../')))

def get_flame_family_apps_list():
    """
    Retrieves a list of flame family application directories from the hardcoded directory.
    
    Returns:
        list: Sorted list of flame family application directories.
    """
    directory = '/opt/Autodesk'  # PRODUCTION
    # directory = '/home/pman/testing'  # TESTING
    flame_family_prefixes = ['flame', 'project_server', 'flare', 'flame_assist', 'smoke']

    try:
        # List all entries in the directory
        entries = os.listdir(directory)
        
        # Filter for directories that match any of the flame family prefixes
        flame_dirs = [entry for entry in entries if any(entry.startswith(prefix) for prefix in flame_family_prefixes) and os.path.isdir(os.path.join(directory, entry))]
        
        # Sort the list in descending order using custom sorting logic
        flame_dirs = sorted(flame_dirs, key=sort_key, reverse=True)

        return flame_dirs
    
    except Exception as e:
        print(f"An error occurred: {e}")
        return []

def sort_key(directory_name):
    """
    Sorting key function that composes a numeric value for sorting based on major, minor, patch,
    app_key, and prerelease.
    """
    pattern = r'(\w+)_(\d+)(?:\.(\d+))?(?:\.(\d+))?(?:\.(pr\d+))?'
    match = re.match(pattern, directory_name)
    
    if not match:
        return (0, 0, 0, 0, 0)  # Return a default tuple for non-matching names
    
    name = match.group(1)
    major = int(match.group(2)) if match.group(2) else 0
    minor = int(match.group(3)) if match.group(3) else 0
    patch = int(match.group(4)) if match.group(4) else 0
    prerelease = match.group(5) or ''
    
    # Determine app_key value
    app_importance = {
        'flame': 5,
        'project_server': 4,
        'flare': 3,
        'flame_assist': 2,
        'smoke': 1
    }
    app_value = app_importance.get(name, 0)
    
    # Set prerelease_value based on whether it's a release or prerelease version
    prerelease_value = 999 if not prerelease else int(prerelease[2:])
    
    # Create a tuple for sorting
    return (app_value, major, minor, patch, prerelease_value)

def sanitize_app_name(app_name):
    """
    Extract the prefix and version from the application name.
    
    Args:
        app_name (str): Application name to sanitize.
        
    Returns:
        str: The sanitized application name without periods and with underscores.
    """
    # Define the flame family prefixes
    flame_family_prefixes = ['flame', 'project_server', 'flare', 'flame_assist', 'smoke']

    # Check if the app name starts with any of the flame family prefixes
    prefix = next((prefix for prefix in flame_family_prefixes if app_name.startswith(prefix)), None)
    
    if not prefix:
        return app_name

    # Remove the preceding prerelease version if present
    app_name = re.sub(r'(pr\d+)', '', app_name)
    
    # Replace periods with underscores
    app_name = app_name.replace('.', '_')
    
    # Remove any trailing underscores
    app_name = app_name.rstrip('_')
    
    return app_name

def sanitize_app_version(app_name):
    """
    Extract the numeric component of the sanitized application name.
    
    Args:
        app_name (str): Application name to sanitize.
        
    Returns:
        str: Sanitized application version without leading underscores.
    """
    # Define the flame family prefixes
    flame_family_prefixes = ['flame', 'project_server', 'flare', 'flame_assist', 'smoke']

    # Extract the prefix
    prefix = next((prefix for prefix in flame_family_prefixes if app_name.startswith(prefix)), None)
    
    if not prefix:
        return "0"

    # Sanitize the app name
    sanitized_name = sanitize_app_name(app_name)
    
    # Extract the numeric component
    pattern = r'(\d+(?:_\d+)*)'
    match = re.search(pattern, sanitized_name)
    
    if match:
        return match.group(0)
    
    return "0"

# ========================================================================== #
# This section defines how to handle the main script function.
# ========================================================================== #

if __name__ == "__main__":
    test_app_names = [
        "flame_2022.3",
        "project_server_2021.1",
        "flare_2020.2",
        "flame_assist_2019.1",
        "smoke_2018.0",
        "flame_2022.3pr1"
    ]
    
    for app_name in test_app_names:
        sanitized_name = sanitize_app_name(app_name)
        sanitized_version = sanitize_app_version(app_name)
        print(f"\n  Original: {app_name},\n  Sanitized Name: {sanitized_name},\n  Sanitized Version: {sanitized_version}\n")

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
