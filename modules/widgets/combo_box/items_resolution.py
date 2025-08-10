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

# File Name:        items_resolution.py
# Version:          2.0.0
# Created:          2024-01-19
# Modified:         2024-12-31

# ========================================================================== #
# This section defines the import statements and path setup.
# ========================================================================== #

# Standard library imports

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

    """
    Get the base path for the application.
    This works both for development and compiled mode (PyInstaller).
    """

    if getattr(sys, 'frozen', False):

        # If the application is run as a bundle, use the sys._MEIPASS
        return sys._MEIPASS
    
    else:

        # If the application is run from a script, use the script's directory
        return os.path.abspath(
            os.path.join(
                os.path.dirname(__file__), '..', '..', '..'
            )
        )

def get_resource_path(relative_path):

    """
    Get absolute path to resource.
    This works both for development and compiled mode (PyInstaller).
    """

    base_path = get_base_path()
    return os.path.join(
        base_path,
        relative_path
    )

# -------------------------------------------------------------------------- #

# Set up the path to the 'modules' directory
modules_dir = get_resource_path('modules')

# Set up the path to the 'resources' directory
resources_dir = get_resource_path('resources')

# Append the modules path to the system path
if modules_dir not in sys.path:
    sys.path.append(modules_dir)

# Print the modules directory path for debugging (optional)
# print(f"  Debug: modules_dir is set to:    {modules_dir}")
# print(f"  Debug: resources_dir is set to:  {resources_dir}")

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
    print(f"  Error reading JSON configuration file: {e}\n")
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

# Print the variables for debugging
# print(f"  Debug: projekt_roots_config_path: {projekt_roots_config_path}")
# print(f"  Debug: the_projekts_dir:         {the_projekts_dir}")
# print(f"  Debug: the_projekt_flame_dirs:   {the_projekt_flame_dirs}")
# print(f"  Debug: the_adsk_dir:             {the_adsk_dir}")
# print(f"  Debug: the_adsk_dir_linux:       {the_adsk_dir_linux}")
# print(f"  Debug: the_adsk_dir_macos:       {the_adsk_dir_macos}")

# ========================================================================== #
# This section defines projekt specific paths.
# ========================================================================== #

# These paths should be passed from the main app.
the_projekt_name = "8888_new_job"
the_projekt_flame_name = f"{the_projekt_name}_2025_1_delta"

# ========================================================================== #
# This section defines environment specific variables.
# ========================================================================== #

# These paths should be passed from the main app.
the_hostname = "delta"

# ========================================================================== #
# This section defines extra specific variables.
# ========================================================================== #

def combine_resolution_file(directory, order_file):
    combined_resolutions = []
    
    try:
        with open(order_file, 'r') as file:
            order = json.load(file)
            if not isinstance(order, list):
                raise ValueError("  Order file must be a list of filenames.")
    except (FileNotFoundError, json.JSONDecodeError, ValueError) as e:
        print(f"  Error loading order file: {e}\n")
        return combined_resolutions
    
    for filename in order:
        filepath = os.path.join(directory, filename)
        try:
            with open(filepath, 'r') as file:
                data = json.load(file)
                combined_resolutions.append(data)
        except (FileNotFoundError, json.JSONDecodeError) as e:
            print(f"  Skipping invalid resolution file {filepath}: {e}\n")
    
    return combined_resolutions

def combine_resolutions(directory, order_file):
    combined_resolutions = combine_resolution_file(directory, order_file)
    
    combobox_items = []
    resolution_details = []
    
    for data in combined_resolutions:
        if 'items' in data:
            for item_group in data['items']:
                if 'separator_name' in item_group:
                    combobox_items.append({'type': 'separator', 'name': item_group['separator_name']})
                for resolution in item_group.get('items', []):
                    if 'resolution_name' in resolution:
                        combobox_items.append({'type': 'item', 'name': resolution['resolution_name']})
                        resolution_details.append({
                            'resolution_name': resolution['resolution_name'],
                            'width': resolution.get('width', 'N/A'),
                            'height': resolution.get('height', 'N/A'),
                            'storage_aspect_ratio': resolution.get('storage_aspect_ratio', 'N/A'),
                            'display_aspect_ratio': resolution.get('display_aspect_ratio', 'N/A'),
                            'pixel_aspect_ratio': resolution.get('pixel_aspect_ratio', 'N/A'),
                            'aspect_ratio': resolution.get('aspect_ratio', 'N/A')
                        })
    
    return combobox_items, resolution_details

if __name__ == '__main__':
    directory = 'resources/cfg/projekt_configuration/parameters/resolution_json_files'
    order_file = 'resources/cfg/projekt_configuration/parameters/load_order/load_order_resolutions.json'
    combobox_items, resolution_details = combine_resolutions(directory, order_file)
    
    print("Combobox Items:")
    print(combobox_items)
    
    print("\nResolution Details:")
    for detail in resolution_details:
        print(detail)

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
# modified:         2024-12-25 - 09:50:17
# comments:         Preparation for future features
# -------------------------------------------------------------------------- #
# version:          2.0.0
# modified:         2024-12-31 - 11:17:25
# comments:         Improved legibility and minor modifications
# -------------------------------------------------------------------------- #
