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

# File Name:        pyside6_qt_output_config_ui.py
# Version:          1.0.0
# Created:          2024-01-19
# Modified:         2024-10-30

# ========================================================================== #
# This section imports the necessary modules.
# ========================================================================== #

import os
import re
import datetime
import shutil
import ast
import sys
import xml.etree.ElementTree as ET

from functools import partial

from pathlib import Path

from PySide6 import (
    QtWidgets,
    QtCore,
    QtGui
)

from typing import (
    Union,
    List,
    Dict,
    Optional,
    Callable
)

# Get the directory path of the currently executing script
current_script_dir = os.path.dirname(os.path.abspath(__file__))

# Append parent_dir to sys.path to access modules relative to the script
parent_dir = os.path.abspath(os.path.join(current_script_dir, ".."))
sys.path.append(parent_dir)

# ========================================================================== #
# This section imports the Qt UI classes.
# ========================================================================== #

from pyside6_qt_flame_classes import (
    pyside6_qt_button,
    pyside6_qt_clickable_line_edit,
    pyside6_qt_label,
    pyside6_qt_line_edit,
    pyside6_qt_list_widget,
    pyside6_qt_message_window,
    pyside6_qt_password_window,
    pyside6_qt_preset_window,
    pyside6_qt_progress_window,
    pyside6_qt_push_button,
    pyside6_qt_push_button_menu,
    pyside6_qt_qdialog,
    pyside6_qt_slider,
    pyside6_qt_text_edit,
    pyside6_qt_token_push_button,
    pyside6_qt_tree_widget,
    pyside6_qt_window
)

# ========================================================================== #
# This section imports the pyflame functions.
# ========================================================================== #

from pyside6_qt_flame_functions import (
    pyside6_qt_get_flame_version,
    pyside6_qt_get_shot_name,
    pyside6_qt_file_browser,
    pyside6_qt_load_config,
    pyside6_qt_open_in_finder,
    pyside6_qt_print,
    pyside6_qt_resolve_shot_name,
    pyside6_qt_resolve_path_tokens,
    pyside6_qt_refresh_hooks,
    pyside6_qt_save_config
)

# ========================================================================== #
# This section defines the pyside6_qt_output_config_ui class.
# ========================================================================== #

class pyside6_qt_output_config_ui:
    def __init__(self, settings, script_name, config_path, version):
        self.settings = settings
        self.SCRIPT_NAME = script_name
        self.CONFIG_PATH = config_path
        self.VERSION = version
        
    def output_node_setup(self):
        def save_config():
            if not self.write_file_media_path_lineedit.text():
                pyside6_qt_message_window('error', f'{self.SCRIPT_NAME}: Error', 'Write Node Setup: Enter Media Path.')
            elif not self.write_file_pattern_lineedit.text():
                pyside6_qt_message_window('error', f'{self.SCRIPT_NAME}: Error', 'Write Node Setup: Enter Pattern for image files.')
            elif not self.write_file_create_open_clip_lineedit.text():
                pyside6_qt_message_window('error', f'{self.SCRIPT_NAME}: Error', 'Write Node Setup: Enter Create Open Clip Naming.')
            elif not self.write_file_include_setup_lineedit.text():
                pyside6_qt_message_window('error', f'{self.SCRIPT_NAME}: Error', 'Write Node Setup: Enter Include Setup Naming.')
            elif not self.write_file_version_name_lineedit.text():
                pyside6_qt_message_window('error', f'{self.SCRIPT_NAME}: Error', 'Write Node Setup: Enter Version Naming.')
            else:
                pyside6_qt_save_config(self.SCRIPT_NAME, self.CONFIG_PATH, {
                    'render_node_type': self.write_file_render_node_type_push_btn.text(),
                    'write_file_media_path': self.write_file_media_path_lineedit.text(),
                    'write_file_pattern': self.write_file_pattern_lineedit.text(),
                    'write_file_create_open_clip': str(self.write_file_create_open_clip_btn.isChecked()),
                    'write_file_include_setup': str(self.write_file_include_setup_btn.isChecked()),
                    'write_file_create_open_clip_value': self.write_file_create_open_clip_lineedit.text(),
                    'write_file_include_setup_value': self.write_file_include_setup_lineedit.text(),
                    'write_file_image_format': self.write_file_image_format_push_btn.text(),
                    'write_file_compression': self.write_file_compression_push_btn.text(),
                    'write_file_padding': self.write_file_padding_slider.text(),
                    'write_file_frame_index': self.write_file_frame_index_push_btn.text(),
                    'write_file_version_name': self.write_file_version_name_lineedit.text(),
                })
                self.setup_window.close()

        def write_file_create_open_clip_btn_check():
            if self.write_file_create_open_clip_btn.isChecked():
                self.write_file_create_open_clip_lineedit.setDisabled(False)
                self.write_file_open_clip_token_btn.setDisabled(False)
            else:
                self.write_file_create_open_clip_lineedit.setDisabled(True)
                self.write_file_open_clip_token_btn.setDisabled(True)

        def write_file_include_setup_btn_check():
            if self.write_file_include_setup_btn.isChecked():
                self.write_file_include_setup_lineedit.setDisabled(False)
                self.write_file_include_setup_token_btn.setDisabled(False)
            else:
                self.write_file_include_setup_lineedit.setDisabled(True)
                self.write_file_include_setup_token_btn.setDisabled(True)

        def render_node_type_toggle():
            controls = [
                self.write_file_setup_label,
                self.write_file_media_path_label,
                self.write_file_pattern_label,
                self.write_file_type_label,
                self.write_file_frame_index_label,
                self.write_file_padding_label,
                self.write_file_compression_label,
                self.write_file_settings_label,
                self.write_file_version_name_label,
                self.write_file_media_path_lineedit,
                self.write_file_pattern_lineedit,
                self.write_file_create_open_clip_lineedit,
                self.write_file_include_setup_lineedit,
                self.write_file_version_name_lineedit,
                self.write_file_padding_slider,
                self.write_file_image_format_push_btn,
                self.write_file_compression_push_btn,
                self.write_file_frame_index_push_btn,
                self.write_file_pattern_token_btn,
                self.write_file_browse_btn,
                self.write_file_include_setup_btn,
                self.write_file_create_open_clip_btn,
                self.write_file_open_clip_token_btn,
                self.write_file_include_setup_token_btn
            ]
            
            disabled = self.write_file_render_node_type_push_btn.text() == 'Render Node'
            for control in controls:
                control.setDisabled(disabled)

            if not disabled:
                write_file_create_open_clip_btn_check()
                write_file_include_setup_btn_check()

        def media_path_browse():
            file_path = pyside6_qt_file_browser('Select Directory', [''], 
                                              self.write_file_media_path_lineedit.text(), 
                                              select_directory=True, 
                                              window_to_hide=[self.setup_window])
            if file_path:
                self.write_file_media_path_lineedit.setText(file_path)

        def compression(file_format):
            def create_menu(option):
                self.write_file_compression_push_btn.setText(option)

            compression_menu.clear()
            self.write_file_image_format_push_btn.setText(file_format)

            compression_settings = {
                'Dpx': ['Uncompressed', 'Pixspan', 'Packed'],
                'Jpeg': [],
                'OpenEXR': ['Uncompressed', 'Scanline', 'Multi_Scanline', 'RLE', 'PXR24', 'PIZ', 'DWAB', 'DWAA', 'B44A', 'B44'],
                'Png': [],
                'Sgi': ['Uncompressed', 'RLE'],
                'Targa': [],
                'Tiff': ['Uncompressed', 'RLE', 'LZW']
            }

            format_type = next((k for k in compression_settings.keys() if k in file_format), None)
            compression_list = compression_settings.get(format_type, [])
            
            self.write_file_compression_push_btn.setEnabled(bool(compression_list))
            if compression_list:
                default_compression = 'PIZ' if format_type == 'OpenEXR' else 'Uncompressed'
                self.write_file_compression_push_btn.setText(default_compression)
            else:
                self.write_file_compression_push_btn.setText('')

            for option in compression_list:
                compression_menu.addAction(option, partial(create_menu, option))

        # Setup UI
        gridbox = QtWidgets.QGridLayout()
        self.setup_window = pyside6_qt_window(f'{self.SCRIPT_NAME}: Output Node Configuration <small>{self.VERSION}</small>', 
                                            gridbox, 1000, 570)

        # Create Labels
        self.write_file_render_node_type_label = pyside6_qt_label('Output Node Type')
        self.write_file_setup_label = pyside6_qt_label('Write File Node Setup', label_type='underline')
        self.write_file_media_path_label = pyside6_qt_label('Media Path')
        self.write_file_pattern_label = pyside6_qt_label('Pattern')
        self.write_file_type_label = pyside6_qt_label('File Type')
        self.write_file_frame_index_label = pyside6_qt_label('Frame Index')
        self.write_file_padding_label = pyside6_qt_label('Padding')
        self.write_file_compression_label = pyside6_qt_label('Compression')
        self.write_file_settings_label = pyside6_qt_label('Settings', label_type='underline')
        self.write_file_version_name_label = pyside6_qt_label('Version Name')

        # Create Line Edits
        self.write_file_media_path_lineedit = pyside6_qt_line_edit(self.settings.write_file_media_path)
        self.write_file_pattern_lineedit = pyside6_qt_line_edit(self.settings.write_file_pattern)
        self.write_file_create_open_clip_lineedit = pyside6_qt_line_edit(self.settings.write_file_create_open_clip_value)
        self.write_file_include_setup_lineedit = pyside6_qt_line_edit(self.settings.write_file_include_setup_value)
        self.write_file_version_name_lineedit = pyside6_qt_line_edit(self.settings.write_file_version_name, max_width=150)

        # Create Slider
        self.write_file_padding_slider = pyside6_qt_slider(int(self.settings.write_file_padding), 1, 20, 
                                                         value_is_float=False, slider_width=150)

        # Setup Image Format Menu
        image_format_menu = QtWidgets.QMenu(self.setup_window)
        image_format_menu.setStyleSheet('QMenu {color: #9a9a9a; background-color:#2d3744; border: none; font: 14px "Discreet"}'
                                      'QMenu::item:selected {color: #d9d9d9; background-color: #3a4551}')

        self.write_file_image_format_push_btn = QtWidgets.QPushButton(self.settings.write_file_image_format)
        self.write_file_image_format_push_btn.setMenu(image_format_menu)
        self.write_file_image_format_push_btn.setMinimumSize(QtCore.QSize(150, 28))
        self.write_file_image_format_push_btn.setMaximumSize(QtCore.QSize(150, 28))
        self.write_file_image_format_push_btn.setFocusPolicy(QtCore.Qt.NoFocus)
        self.write_file_image_format_push_btn.setStyleSheet('QPushButton {color: #9a9a9a; background-color: #2d3744; border: none; font: 14px "Discreet"}'
                                                          'QPushButton:hover {border: 1px solid #5a5a5a}'
                                                          'QPushButton:disabled {color: #747474; background-color: #2d3744; border: none}'
                                                          'QPushButton::menu-indicator { image: none; }')

        # Setup Compression Menu
        compression_menu = QtWidgets.QMenu(self.setup_window)
        compression_menu.setStyleSheet('QMenu {color: #9a9a9a; background-color:#2d3744; border: none; font: 14px "Discreet"}'
                                     'QMenu::item:selected {color: #d9d9d9; background-color: #3a4551}')

        self.write_file_compression_push_btn = QtWidgets.QPushButton(self.settings.write_file_compression)
        self.write_file_compression_push_btn.setMenu(compression_menu)
        self.write_file_compression_push_btn.setMinimumSize(QtCore.QSize(150, 28))
        self.write_file_compression_push_btn.setMaximumSize(QtCore.QSize(150, 28))
        self.write_file_compression_push_btn.setFocusPolicy(QtCore.Qt.NoFocus)
        self.write_file_compression_push_btn.setStyleSheet('QPushButton {color: #9a9a9a; background-color: #2d3744; border: none; font: 14px "Discreet"}'
                                                         'QPushButton:hover {border: 1px solid #5a5a5a}'
                                                         'QPushButton:disabled {color: #747474; background-color: #2d3744; border: none}'
                                                         'QPushButton::menu-indicator { image: none; }')

        # Add Image Format Options
        formats = [
            'Dpx 8-bit', 'Dpx 10-bit', 'Dpx 12-bit', 'Dpx 16-bit',
            'Jpeg 8-bit',
            'OpenEXR 16-bit fp', 'OpenEXR 32-bit fp',
            'Png 8-bit', 'Png 16-bit',
            'Sgi 8-bit', 'Sgi 16-bit',
            'Targa 8-bit',
            'Tiff 8-bit', 'Tiff 16-bit'
        ]
        for format_option in formats:
            image_format_menu.addAction(format_option, partial(compression, format_option))

        # Setup Render Type Menu
        render_node_options = ['Render Node', 'Write File Node']
        self.write_file_render_node_type_push_btn = pyside6_qt_push_button_menu(
            self.settings.render_node_type, 
            render_node_options, 
            menu_action=render_node_type_toggle
        )

        # Setup Frame Index Menu
        frame_index = ['Use Start Frame', 'Use Timecode']
        self.write_file_frame_index_push_btn = pyside6_qt_push_button_menu(
            self.settings.write_file_frame_index, 
            frame_index
        )

        # # Setup Token Buttons
        # write_file_token_dict = {
        #     'Batch Name': '<batch name>', 
        #     'Batch Iteration': '<batch iteration>', 
        #     'Iteration': '<iteration>',
        #     'Project': '<project>', 
        #     'Project Nickname': '<project nickname>', 
        #     'Shot Name': '<shot name>', 
        #     'Clip Height


        # Setup Token Buttons
        write_file_token_dict = {
            'Batch Name': '<batch name>',
            'Batch Iteration': '<batch iteration>',
            'Iteration': '<iteration>',
            'Project': '<project>',
            'Project Nickname': '<project nickname>',
            'Shot Name': '<shot name>',
            'Clip Height': '<height>',
            'Clip Width': '<width>',
            'Clip Name': '<name>',
        }

        self.write_file_pattern_token_btn = pyside6_qt_token_push_button('Add Token', write_file_token_dict, self.write_file_pattern_lineedit)
        self.write_file_open_clip_token_btn = pyside6_qt_token_push_button('Add Token', write_file_token_dict, self.write_file_create_open_clip_lineedit)
        self.write_file_include_setup_token_btn = pyside6_qt_token_push_button('Add Token', write_file_token_dict, self.write_file_include_setup_lineedit)

        # Setup Push Buttons
        self.write_file_create_open_clip_btn = pyside6_qt_push_button('Create Open Clip', self.settings.write_file_create_open_clip)
        self.write_file_create_open_clip_btn.clicked.connect(write_file_create_open_clip_btn_check)
        write_file_create_open_clip_btn_check()

        self.write_file_include_setup_btn = pyside6_qt_push_button('Include Setup', self.settings.write_file_include_setup)
        self.write_file_include_setup_btn.clicked.connect(write_file_include_setup_btn_check)
        write_file_include_setup_btn_check()

        # Setup Regular Buttons
        self.write_file_browse_btn = pyside6_qt_button('Browse', media_path_browse)
        self.write_file_save_btn = pyside6_qt_button('Save', save_config)
        self.write_file_cancel_btn = pyside6_qt_button('Cancel', self.setup_window.close)

        # Initialize Compression and Render Node Type
        compression(self.write_file_image_format_push_btn.text())
        self.write_file_compression_push_btn.setText(self.settings.write_file_compression)
        render_node_type_toggle()

        # Layout Setup
        gridbox.setContentsMargins(20, 20, 20, 20)
        gridbox.setVerticalSpacing(5)
        gridbox.setHorizontalSpacing(5)
        gridbox.setRowStretch(3, 2)
        gridbox.setRowStretch(6, 2)
        gridbox.setRowStretch(9, 2)

        # Add widgets to grid
        gridbox.addWidget(self.write_file_render_node_type_label, 0, 0)
        gridbox.addWidget(self.write_file_render_node_type_push_btn, 0, 1)

        gridbox.addWidget(self.write_file_setup_label, 1, 0, 1, 6)

        gridbox.addWidget(self.write_file_media_path_label, 2, 0)
        gridbox.addWidget(self.write_file_media_path_lineedit, 2, 1, 1, 4)
        gridbox.addWidget(self.write_file_browse_btn, 2, 5)

        gridbox.addWidget(self.write_file_pattern_label, 3, 0)
        gridbox.addWidget(self.write_file_pattern_lineedit, 3, 1, 1, 4)
        gridbox.addWidget(self.write_file_pattern_token_btn, 3, 5)

        gridbox.setRowMinimumHeight(4, 28)

        gridbox.addWidget(self.write_file_create_open_clip_btn, 5, 0)
        gridbox.addWidget(self.write_file_create_open_clip_lineedit, 5, 1, 1, 4)
        gridbox.addWidget(self.write_file_open_clip_token_btn, 5, 5)

        gridbox.addWidget(self.write_file_include_setup_btn, 6, 0)
        gridbox.addWidget(self.write_file_include_setup_lineedit, 6, 1, 1, 4)
        gridbox.addWidget(self.write_file_include_setup_token_btn, 6, 5)

        gridbox.setRowMinimumHeight(7, 28)

        gridbox.addWidget(self.write_file_settings_label, 8, 0, 1, 5)
        gridbox.addWidget(self.write_file_frame_index_label, 9, 0)
        gridbox.addWidget(self.write_file_frame_index_push_btn, 9, 1)
        gridbox.addWidget(self.write_file_type_label, 10, 0)
        gridbox.addWidget(self.write_file_image_format_push_btn, 10, 1)
        gridbox.addWidget(self.write_file_compression_label, 11, 0)
        gridbox.addWidget(self.write_file_compression_push_btn, 11, 1)

        gridbox.addWidget(self.write_file_padding_label, 9, 2)
        gridbox.addWidget(self.write_file_padding_slider, 9, 3)
        gridbox.addWidget(self.write_file_version_name_label, 11, 2)
        gridbox.addWidget(self.write_file_version_name_lineedit, 11, 3)

        gridbox.addWidget(self.write_file_save_btn, 13, 5)
        gridbox.addWidget(self.write_file_cancel_btn, 14, 5)

        self.setup_window.show()
# version:               1.0.0
# modified:              2024-10-30 - 07:35:27
# comments:              Refactored PySide6 Output Node Config UI.
# -------------------------------------------------------------------------- #
