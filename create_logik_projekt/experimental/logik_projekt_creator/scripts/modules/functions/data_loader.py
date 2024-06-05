'''
File Name:        projekt_data_loader.py
Version:          1.0.0
Language:         python script
Author:           Phil MAN - phil_man@mac.com
Created:          2024-05-23
Modified:         2024-06-02

Description:      This program aggregates projekt setup options data
'''

# ========================================================================== #
# This section defines the import statements
# ========================================================================== #

import os
import json

# ========================================================================== #
# This section defines the options for projekt resolution
# ========================================================================== #

def load_resolutions(projekt_resolution):
    script_dir = os.path.dirname(os.path.abspath(__file__))

    json_files = [
        'resolutions-broadcast.json',
        'resolutions-film.json',
        'resolutions-dcp.json',
        'resolutions-aja.json',
        'resolutions-arri.json',
        'resolutions-bmd.json',
        'resolutions-canon.json',
        'resolutions-panasonic.json',
        'resolutions-red.json',
        'resolutions-sony.json',
        'resolutions-zcam.json',
        'resolutions-miscellaneous.json'
    ]

    combined_data = {"items": []}

    for file_name in json_files:
        resolutions_path = os.path.join(script_dir, '../../../config', file_name)
        with open(resolutions_path, 'r') as file:
            data = json.load(file)
            combined_data["items"].extend(data["items"])

    separator_names = set()

    for category in combined_data["items"]:
        separator_name = category.get("separator_name")
        if separator_name and separator_name not in separator_names:
            projekt_resolution.addItem(separator_name, userData=None)
            separator_names.add(separator_name)

        for item in category["items"]:
            projekt_resolution.addItem(item["name"], userData=item)

# ========================================================================== #
# This section defines the options for projekt bit depth
# ========================================================================== #

def load_bit_depths(projekt_bit_depth):
    script_dir = os.path.dirname(os.path.abspath(__file__))

    json_files = [
        'bit_depths.json'
    ]

    combined_data = {"items": []}

    for file_name in json_files:
        bit_depths_path = os.path.join(script_dir, '../../../config', file_name)
        with open(bit_depths_path, 'r') as file:
            data = json.load(file)
            combined_data["items"].extend(data["items"])

    separator_names = set()

    for category in combined_data["items"]:
        separator_name = category.get("separator_name")
        if separator_name and separator_name not in separator_names:
            projekt_bit_depth.addItem(separator_name, userData=None)
            separator_names.add(separator_name)

        for item in category["items"]:
            projekt_bit_depth.addItem(item["name"], userData=item)

# ========================================================================== #
# This section defines the options for projekt frame rate
# ========================================================================== #

def load_frame_rates(projekt_frame_rate):
    script_dir = os.path.dirname(os.path.abspath(__file__))

    json_files = [
        'frame_rates.json'
    ]

    combined_data = {"items": []}

    for file_name in json_files:
        frame_rates_path = os.path.join(script_dir, '../../../config', file_name)
        with open(frame_rates_path, 'r') as file:
            data = json.load(file)
            combined_data["items"].extend(data["items"])

    separator_names = set()

    for category in combined_data["items"]:
        separator_name = category.get("separator_name")
        if separator_name and separator_name not in separator_names:
            projekt_frame_rate.addItem(separator_name, userData=None)
            separator_names.add(separator_name)

        for item in category["items"]:
            projekt_frame_rate.addItem(item["name"], userData=item)

# ========================================================================== #
# This section defines the options for projekt color science
# ========================================================================== #

def load_color_sciences(projekt_color_science):
    script_dir = os.path.dirname(os.path.abspath(__file__))

    json_files = [
        'color_science.json'
    ]

    combined_data = {"items": []}

    for file_name in json_files:
        color_sciences_path = os.path.join(script_dir, '../../../config', file_name)
        with open(color_sciences_path, 'r') as file:
            data = json.load(file)
            combined_data["items"].extend(data["items"])

    separator_names = set()

    for category in combined_data["items"]:
        separator_name = category.get("separator_name")
        if separator_name and separator_name not in separator_names:
            projekt_color_science.addItem(separator_name, userData=None)
            separator_names.add(separator_name)

        for item in category["items"]:
            projekt_color_science.addItem(item["name"], userData=item)

# ========================================================================== #
# This section defines the options for projekt start frame
# ========================================================================== #

def load_start_frames(projekt_start_frame):
    script_dir = os.path.dirname(os.path.abspath(__file__))

    json_files = [
        'start_frames.json'
    ]

    combined_data = {"items": []}

    for file_name in json_files:
        start_frames_path = os.path.join(script_dir, '../../../config', file_name)
        with open(start_frames_path, 'r') as file:
            data = json.load(file)
            combined_data["items"].extend(data["items"])

    separator_names = set()

    for category in combined_data["items"]:
        separator_name = category.get("separator_name")
        if separator_name and separator_name not in separator_names:
            projekt_start_frame.addItem(separator_name, userData=None)
            separator_names.add(separator_name)

        for item in category["items"]:
            projekt_start_frame.addItem(item["name"], userData=item)

# ========================================================================== #
# C2 A9 32 30 32 34 2D 4D 41 4E 5F 4D 41 44 45 2D 4D 45 4B 41 4E 49 53 4D 5A #
# ========================================================================== #

'''
Disclaimer:       This program is part of LOGIK-PROJEKT.
                  LOGIK-PROJEKT is free software.

                  You can redistribute it and/or modify it under the terms
                  of the GNU General Public License as published by the
                  Free Software Foundation, either version 3 of the License,
                  or any later version.

                  This program is distributed in the hope that it will be
                  useful, but WITHOUT ANY WARRANTY; without even the
                  implied warranty of MERCHANTABILITY or FITNESS FOR A
                  PARTICULAR PURPOSE.

                  See the GNU General Public License for more details.

                  You should have received a copy of the GNU General
                  Public License along with this program.

                  If not, see <https://www.gnu.org/licenses/>.
'''

# -------------------------------------------------------------------------- #
# Changelist:
# -------------------------------------------------------------------------- #
