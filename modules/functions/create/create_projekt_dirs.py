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

# File Name:        create_projekt_dirs.py
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

__all__ = ['create_the_projekt_directories']

# ========================================================================== #
# This section defines the primary functions for the script.
# ========================================================================== #

def create_the_projekt_directories(
        the_projekts_dir,
        the_projekt_name,
        the_projekts_flame_dir,
        the_sanitized_version,
        bookmarks_file,
        tmp_bookmarks_file,
        the_projekt_dirs_json_dir,
        the_projekt_dirs_json_files,
    ):

    def _write_bookmarks(file_path, bookmarks):
        with open(file_path, 'w') as f:
            json.dump(bookmarks, f, indent=4)
        print(f"  Bookmarks written to: {file_path}\n")

    def _read_json_files(files):
        data = []
        for file in files:
            print(f"  Reading JSON config file: {file}\n")
            try:
                with open(file, 'r') as f:
                    file_data = json.load(f)
                    data.append(file_data)
            except Exception as e:
                print(f"* Error reading {file}: {e}")
        return data

    def _find_bookmark_folder(bookmarks_list, folder_name):
        for bookmark in bookmarks_list:
            if bookmark.get('Folder') == folder_name:
                return bookmark.get('Bookmarks', [])
        return None

    def _format_path(path, the_projekts_dir, the_projekt_name, the_projekts_flame_dir):
        formatted = path.format(
            projekts_dir=the_projekts_dir,
            projekt_dir=the_projekt_name,
            projekt_flame_dir=the_projekts_flame_dir,
        )
        return formatted.replace('//', '/')

    def _collect_keys_values(item, bookmarks_list, the_projekts_dir, the_projekt_name, the_projekts_flame_dir, current_folder_bookmarks=None):
        if isinstance(item, dict):
            path = _format_path(item.get('path', ''), the_projekts_dir, the_projekt_name, the_projekts_flame_dir)
            if path:
                full_path = '/' + path.lstrip('/')
                if not os.path.exists(full_path):
                    os.makedirs(full_path)
                    print(f"  Successfully created directory: {full_path}")

                bookmark_name = item.get('bookmark_name', '')
                if bookmark_name:
                    bookmark_entry = {
                        'Bookmark': bookmark_name,
                        'Path': full_path,
                        'Visibility': item.get('bookmark_visibility', 'Global')
                    }

                    if item.get('bookmark_type') == 'folder':
                        folder_name = bookmark_name
                        print(f"\n\n  Processing bookmarks: {folder_name}\n")
                        folder_bookmarks = _find_bookmark_folder(current_folder_bookmarks or bookmarks_list, folder_name)
                        if folder_bookmarks is None:
                            folder_entry = {
                                'Folder': folder_name,
                                'Bookmarks': [bookmark_entry]
                            }
                            if current_folder_bookmarks is not None:
                                current_folder_bookmarks.append(folder_entry)
                            else:
                                bookmarks_list.append(folder_entry)
                            current_folder_bookmarks = folder_entry['Bookmarks']
                        else:
                            folder_bookmarks.append(bookmark_entry)
                            current_folder_bookmarks = folder_bookmarks
                    else:
                        if current_folder_bookmarks is not None:
                            current_folder_bookmarks.append(bookmark_entry)
                        else:
                            bookmarks_list.append(bookmark_entry)

            children = item.get('children', {})
            if children:
                for key, value in children.items():
                    _collect_keys_values(
                        value,
                        bookmarks_list,
                        the_projekts_dir,
                        the_projekt_name,
                        the_projekts_flame_dir,
                        current_folder_bookmarks
                    )

    bookmarks_file_header = {
        "DlBookmark": {
            "Version": 1,
            "Sections": [
                {
                    "Section": "Project",
                    "Bookmarks": [
                        {
                            "Bookmark": "flame setups",
                            "Path": "<project home>",
                            "Visibility": "Global"
                        },
                        {
                            "Bookmark": "PROJEKTS",
                            "Path": f"{the_projekts_dir}/",
                            "Visibility": "Global"
                        },
                        {
                            "Bookmark": "projekt home",
                            "Path": f"{the_projekts_dir}/{the_projekt_name}/",
                            "Visibility": "Global"
                        },
                        {
                            "Folder": "projekt directories",
                            "Bookmarks": []
                        }
                    ]
                }
            ]
        }
    }

    # Write bookmarks file header to bookmarks file
    _write_bookmarks(bookmarks_file, bookmarks_file_header)

    # Read the JSON files
    json_data = _read_json_files(the_projekt_dirs_json_files)

    # Initialize bookmarks data
    additional_bookmarks = []

    # Collect keys and values, create directories, and update bookmarks
    for file_data in json_data:
        for item in file_data.values():
            # _collect_keys_values(item, additional_bookmarks, projekts_dir, projekt_dir, projekt_flame_dir)
            _collect_keys_values(item, additional_bookmarks, the_projekts_dir, the_projekt_name, the_projekts_flame_dir)



    # Initialize data variable outside the if block
    data = None

    # Write additional bookmarks to tmp_bookmarks_file
    if additional_bookmarks:
        with open(tmp_bookmarks_file, 'w') as tmp_file:
            json.dump({ 'Bookmarks': additional_bookmarks }, tmp_file, indent=4)
        print(f"\n  Additional bookmarks written to {tmp_bookmarks_file}\n")

        # Load the existing bookmarks file to append new bookmarks
        with open(bookmarks_file, 'r+') as f:
            data = json.load(f)
            
            # Read tmp_bookmarks_file
            if os.path.getsize(tmp_bookmarks_file) > 0:
                try:
                    with open(tmp_bookmarks_file, 'r') as tmp_file:
                        tmp_bookmarks_data = json.load(tmp_file)
                        
                        # Insert tmp_bookmarks_file content into the bookmarks list
                        projekt_dirs_folder = _find_bookmark_folder(data['DlBookmark']['Sections'][0]['Bookmarks'], "projekt directories")
                        if projekt_dirs_folder is not None:
                            projekt_dirs_folder.extend(tmp_bookmarks_data.get('Bookmarks', []))
                except json.JSONDecodeError as e:
                    print(f"* Error decoding JSON from {tmp_bookmarks_file}: {e}")
            else:
                print(f"  {tmp_bookmarks_file} is empty or does not exist.")
            
            # Write updated data back to the file
            f.seek(0)
            json.dump(data, f, indent=4)
            f.truncate()

        # Clear tmp_bookmarks_file after processing
        with open(tmp_bookmarks_file, 'w') as tmp_file:
            tmp_file.write('{}')  # Write an empty dictionary to clear the file

        print(f"  Bookmarks file updated successfully.")
    else:
        # If there are no additional bookmarks, read the existing bookmarks file
        try:
            with open(bookmarks_file, 'r') as f:
                data = json.load(f)
        except (FileNotFoundError, json.JSONDecodeError) as e:
            print(f"* Error reading bookmarks file: {e}")
            data = bookmarks_file_header  # Use the header as fallback

    return data  # Return the final bookmarks data

# ========================================================================== #
# This section defines how to handle the main script function.
# ========================================================================== #

if __name__ == "__main__":
    import argparse
    
    parser = argparse.ArgumentParser(description="Create project directories and bookmarks.")
    parser.add_argument("the_projekts_dir", help="Path to the projects directory")
    parser.add_argument("the_projekt_name", help="Name of the specific project")
    parser.add_argument("the_projekts_flame_dir", help="Path to the Flame project directory")
    parser.add_argument("bookmarks_file", help="Path to the bookmarks file")
    parser.add_argument("tmp_bookmarks_file", help="Path to the temporary bookmarks file")
    parser.add_argument("the_projekt_dirs_json_dir", help="Directory containing JSON configuration files")
    parser.add_argument("the_projekt_dirs_json_files", nargs="+", help="JSON configuration files")

    args = parser.parse_args()

    create_the_projekt_directories(args.the_projekts_dir, args.the_projekt_name, args.the_projekts_flame_dir, 
                        args.bookmarks_file, args.tmp_bookmarks_file, 
                        args.the_projekt_dirs_json_dir, args.the_projekt_dirs_json_files)

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
# modified:         2024-12-31 - 11:17:16
# comments:         Improved legibility and minor modifications
# -------------------------------------------------------------------------- #
