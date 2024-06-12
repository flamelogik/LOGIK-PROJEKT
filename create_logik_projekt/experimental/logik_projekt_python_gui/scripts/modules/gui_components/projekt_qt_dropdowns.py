'''
# -------------------------------------------------------------------------- #

# File Name:        projekt_qt_dropdowns.py
# Version:          1.0.0
# Language:         python script
# Flame Version:    2025.x
# Author:           Phil MAN - phil_man@mac.com
# Toolset:          MAN_MADE_MATERIAL: LOGIK-PROJEKT
# Created:          2024-04-20
# Modified:         2024-06-07
# Modifier:         Phil MAN - phil_man@mac.com

# Description:      This program is part of LOGIK-PROJEKT.
#                   LOGIK-PROJEKT is a library of custom functions and
#                   modules for autodesk flame.

# Installation:     Copy the "LOGIK-PROJEKT" repo to your GitHub directory,
#                   e.g. "/home/$USER/workspace/GitHub"

# Changelist:       The full changelist is at the end of this document.

# -------------------------------------------------------------------------- #
'''

# # ========================================================================== #
# # This section defines the import staements.
# # ========================================================================== #

# from PySide6.QtWidgets import QComboBox

# # ========================================================================== #
# # This section defines the main functions.
# # ========================================================================== #

# def create_projekt_resolution_dropdown():
#     dropdown = QComboBox()
#     dropdown.addItems(
#         ["1920 x 1080 | HD 1080 16:9", "Full"])
#     return dropdown

# def create_projekt_frame_rate_dropdown():
#     dropdown = QComboBox()
#     dropdown.addItems(["23.976 fps", "24 fps", "25 fps", "29.97 fps DF", "29.97 fps NDF", "30 fps", "50 fps", "59.94 fps DF", "59.94 fps NDF", "60 fps"])
#     return dropdown

# def create_projekt_scan_mode_dropdown():
#     dropdown = QComboBox()
#     dropdown.addItems(["FIELD_1", "FIELD_2", "PROGRESSIVE"])
#     return dropdown

# def create_projekt_bit_depth_dropdown():
#     dropdown = QComboBox()
#     dropdown.addItems(["32-bit fp", "16-bit fp", "16-bit", "12-bit", "10-bit", "8-bit"])
#     return dropdown

# def create_projekt_colour_science_dropdown():
#     dropdown = QComboBox()
#     dropdown.addItems(["ARRI Alexa LogC V3 (K1S1)", "ARRI Alexa LogC v4", "Autodesk ACES 1.1", "Autodesk ACES 1.0", "Autodesk Simple Linear Workflow", "Autodesk Legacy Workflow", "R3D Log3g10 Red Wide Gamut RGB (Do Not Use)", "Sony Cine+ 709", "Sony Low Contrast 709", "Sony Low Contrast 709 Type A (Alexa Emulation)", "Sony SLog2 709", "Apple Log (ADSK ACES 1.1)"])
#     return dropdown

# def create_projekt_start_frame_dropdown():
#     dropdown = QComboBox()
#     dropdown.addItems(["1001", "1"])
#     return dropdown


import os

import json

from PySide6.QtWidgets import (
    QComboBox, 
    QStyledItemDelegate, 
    QStyleOptionComboBox
)

from PySide6.QtCore import Qt

# Define the base directory relative to the main script
BASE_DIR = os.path.dirname(
    os.path.dirname(
        os.path.dirname(
            os.path.abspath(__file__)
        )
    )
)

from ..functions.projekt_json_loader import (
    load_projekt_json_resolutions,
    load_projekt_json_frame_rates,
    load_projekt_json_scan_modes,
    load_projekt_json_bit_depths,
    load_projekt_json_color_science,
    load_projekt_json_start_frames
)

print(BASE_DIR)

class SeparatorItemDelegate(QStyledItemDelegate):
    def paint(self, painter, option, index):
        if index.data(Qt.UserRole) == "separator":
            options = QStyleOptionComboBox()
            options.rect = option.rect
            self.initStyleOption(options, index)
            style = option.widget.style()
            style.drawControl(
                QStyle.CE_ComboBoxItem,
                options, 
                painter
            )
        else:
            super().paint(painter, option, index)


def create_separator_item(name):
    item = QComboBox()
    item.setItemDelegate(SeparatorItemDelegate())
    item.addItem(name, userData="separator")
    item.setEnabled(False)
    return item


def create_projekt_resolution_dropdown():
    dropdown = QComboBox()
    dropdown.setItemDelegate(SeparatorItemDelegate())
    dropdown.addItem("Projekt Resolutions")
    resolutions = load_projekt_json_resolutions()
    for group_name, resolution_group in resolutions.items():
        dropdown.addItem(create_separator_item(group_name))
        for resolution_item in resolution_group:
            dropdown.addItem(
                f"{resolution_item['width']} x {resolution_item['height']} | {resolution_item['name']}"
            )
    return dropdown


def create_projekt_frame_rate_dropdown():
    dropdown = QComboBox()
    dropdown.setItemDelegate(SeparatorItemDelegate())
    dropdown.addItem("Frame Rates")
    frame_rates = load_projekt_json_frame_rates()
    for frame_rate in frame_rates:
        dropdown.addItem(frame_rate['name'])
    return dropdown


def create_projekt_scan_mode_dropdown():
    dropdown = QComboBox()
    dropdown.setItemDelegate(SeparatorItemDelegate())
    dropdown.addItem("Scan Modes")
    scan_modes = load_projekt_json_scan_modes()
    for scan_mode in scan_modes:
        dropdown.addItem(scan_mode['name'])
    return dropdown


def create_projekt_bit_depth_dropdown():
    dropdown = QComboBox()
    dropdown.setItemDelegate(SeparatorItemDelegate())
    dropdown.addItem("Bit Depths")
    bit_depths = load_projekt_json_bit_depths()
    for bit_depth in bit_depths:
        dropdown.addItem(bit_depth['name'])
    return dropdown


def create_projekt_colour_science_dropdown():
    dropdown = QComboBox()
    dropdown.setItemDelegate(SeparatorItemDelegate())
    dropdown.addItem("Color Science")
    color_science = load_projekt_json_color_science()
    for science in color_science:
        dropdown.addItem(science['name'])
    return dropdown


def create_projekt_start_frame_dropdown():
    dropdown = QComboBox()
    dropdown.setItemDelegate(SeparatorItemDelegate())
    dropdown.addItem("Start Frames")
    start_frames = load_projekt_json_start_frames()
    for start_frame in start_frames:
        dropdown.addItem(start_frame['name'])
    return dropdown

# ========================================================================== #
# C2 A9 32 30 32 34 2D 4D 41 4E 5F 4D 41 44 45 2D 4D 45 4B 41 4E 49 53 4D 5A #
# ========================================================================== #
'''
# -------------------------------------------------------------------------- #

# Disclaimer:       This program is part of LOGIK-PROJEKT.
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
# -------------------------------------------------------------------------- #
'''
# -------------------------------------------------------------------------- #
# Changelist:       
# -------------------------------------------------------------------------- #
# version:               1.0.0
# modified:              2024-06-07 - 16:22:45
# comments:              Working program
