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

# File Name:        logik_projekt_openclip_comp.py
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
    pyside6_qt_save_config,
    pyside6_qt_output_config_ui
)

# ========================================================================== #
# This section defines paths.
# ========================================================================== #

# Define base path
base_python_path = Path('/opt/Autodesk/shared/python')

# Define other paths relative to base_python_path
tool_family_path = base_python_path / 'logik_projekt/openclip_tools/logik_projekt_openclip'
tool_name = 'logik_projekt_openclip_comp'
tool_path = tool_family_path / 'scripts' / tool_name
tool_config_path = tool_family_path / 'config' / tool_name

SCRIPT_NAME = str(tool_name)

# Convert paths to str():
# CONFIG_PATH = str(tool_family_path)
CONFIG_PATH = str(tool_config_path)
SCRIPT_PATH = str(tool_path)

# Define the script version
VERSION = 'v1.0'

# ========================================================================== #
# This section defines the openclip class.
# ========================================================================== #

class class_projekt_openclip_comp():

    def __init__(self, selection):

        print('\n')
        print('>' * 10, f'{SCRIPT_NAME} {VERSION}', '<' * 10, '\n')

        self.selection = selection

        # Load config file

        self.settings = pyside6_qt_load_config(SCRIPT_NAME, CONFIG_PATH, {
            'render_node_type': 'Write File Node',
            'write_file_media_path': '/PROJEKTS/',
            'write_file_pattern': '<project nickname>/shots/<shot name>/media/renders/<name>_<version name>/<name>_<version name><frame><ext>',
            'write_file_create_open_clip': 'True',
            'write_file_include_setup': 'True',
            'write_file_create_open_clip_value': '<project nickname>/shots/<shot name>/openclip/output_clips/flame/<name><ext>',
            'write_file_include_setup_value': '<project nickname>/shots/<shot name>/batch_setups/<name>_<version name>_<workstation>_<user nickname><ext>',
            'write_file_image_format': 'OpenEXR 16-bit fp',
            'write_file_compression': 'PIZ',
            'write_file_padding': '8',
            'write_file_frame_index': 'Use Start Frame',
            'write_file_version_name': 'v<version>'
        })

        # Init Variables

        self.y_position = 0
        self.x_position = 0
        self.batch_duration = 1

    # ---------------------------------------------------------------------- #

    def batch_projekt_comp_clips(self):
        import flame

        # Get current batch
        self.batch_group = flame.batch

        # Define reel names
        reel_names = [
            "sources",
            "reference",
            "CGI",
            "depth",
            "graphics",
            "mattes",
            "motion",
            "multichannel",
            "neat_video",
            "nuke",
            "paint",
            "precomp",
            "roto",
            "comp",  # trailing comma is legitimate on last list item in python
        ]

        # Rename 'Schematic Reel' or 'Schematic Reel 1' to 'sources' if it exists
        for reel in flame.batch.reels:
            if reel.name == 'Schematic Reel' or reel.name == 'Schematic Reel 1':
                reel.name = 'sources'
                print(f"Renamed '{reel.name}' to 'sources'.")

        # Rename 'Schematic Reel' or 'Schematic Reel 2' to 'reference' if it exists
        for reel in flame.batch.reels:
            if reel.name == 'Schematic Reel' or reel.name == 'Schematic Reel 2':
                reel.name = 'reference'
                print(f"Renamed '{reel.name}' to 'reference'.")

        # Rename 'Schematic Reel' or 'Schematic Reel 3' to 'CGI' if it exists
        for reel in flame.batch.reels:
            if reel.name == 'Schematic Reel' or reel.name == 'Schematic Reel 3':
                reel.name = 'CGI'
                print(f"Renamed '{reel.name}' to 'CGI'.")

        # Rename 'Schematic Reel' or 'Schematic Reel 4' to 'depth' if it exists
        for reel in flame.batch.reels:
            if reel.name == 'Schematic Reel' or reel.name == 'Schematic Reel 4':
                reel.name = 'depth'
                print(f"Renamed '{reel.name}' to 'depth'.")

        # Create reels that don't exist
        for reel_name in reel_names:
            if not any(reel.name == reel_name for reel in flame.batch.reels):
                flame.batch.create_reel(reel_name)
                print(f"Created new schematic reel named '{reel_name}'.")
            else:
                print(f"Schematic reel named '{reel_name}' already exists.")

        for clip in self.selection:
            self.x_position = clip.pos_x
            self.y_position = clip.pos_y

            self.get_clip_info(clip)

            self.create_batch_nodes(clip)

        self.batch_group.frame_all()

        print('Done.\n')

    # ---------------------------------------------------------------------- #

    def media_panel_projekt_comp_clips(self):
        import flame

        flame.go_to('Batch')

        # Create batch group
        batch_group = flame.batch.create_batch_group(
            'projekt_comp',
            reels=[
                'sources',
                'reference',
                'CGI',
                'depth',
                'graphics',
                'mattes',
                'motion',
                'multichannel',
                'neat_video',
                'nuke',
                'paint',
                'precomp',
                'roto',
                'comp'
            ]
        )

        # Add source clip(s) to 'sources_reel'
        sources_reel = batch_group.reels[0]

        batch_group.expanded = False

        # Copy all clips in selection to batch
        for clip in self.selection:
            flame.media_panel.copy(clip, sources_reel)

        # Create new selection of all clips in batch
        self.selection = flame.batch.nodes
        self.selection.reverse()

        # Repo clips in batch to spread them out

        # clip_pos_y = 200
        clip_pos_y = 192

        for clip in self.selection:
                clip_pos_y += 192
                clip.pos_y = clip_pos_y

        # Set batch duration if duration of current clip is longer than last or Default
        for clip in flame.batch.nodes:
            if int(str(clip.duration)) > int(str(batch_group.duration)):
                batch_group.duration = int(str(clip.duration))

        # Run batch comp clips on all clips in batch
        self.batch_projekt_comp_clips()

        batch_group.frame_all()

    # ---------------------------------------------------------------------- #

    def get_clip_info(self, clip):
        import flame

        # Get clip values

        self.clip_name = str(clip.name)[1:-1]
        #print('clip_name: ', self.clip_name)

        self.clip_duration = clip.duration
        #print('clip_duration:', self.clip_duration)

        self.clip_frame_rate = clip.clip.frame_rate
        #print('clip_frame_rate:', self.clip_frame_rate)

        self.clip_timecode = clip.clip.start_time
        #print('clip_timecode:', self.clip_timecode)

        self.clip_shot_name = pyside6_qt_get_shot_name(clip)

    # ---------------------------------------------------------------------- #

    def create_batch_nodes(self, clip):
        import flame

        def add_render_node():

            # Create render node

            self.render_node = self.batch_group.create_node('Render')

            self.render_node.range_start = self.batch_group.start_frame
            self.render_node.range_end = int(str(self.batch_group.start_frame)) + int(str(self.clip_duration)) - 1

            self.render_node.frame_rate = self.clip_frame_rate

            self.render_node.source_timecode = self.clip_timecode
            self.render_node.record_timecode = self.clip_timecode

            self.render_node.name = self.clip_shot_name + '_comp'
            # self.render_node.name = self.clip_name + '_mattes'
            # self.render_node.name = self.clip_name + '_multichannel'
            # self.render_node.name = self.clip_name + '_neat_video'
            # self.render_node.name = self.clip_name + '_precomp'

            # self.render_node.destination = ('Batch Reels', 'comp')
            # self.render_node.destination = ('Batch Reels', 'mattes')
            # self.render_node.destination = ('Batch Reels', 'multichannel')
            # self.render_node.destination = ('Batch Reels', 'neat_video')
            # self.render_node.destination = ('Batch Reels', 'precomp')
            self.render_node.destination = ('Libraries', 'Batch Renders')

            # Enable the 'Add to Workspace' option
            self.render_node.add_to_workspace = True

            # Enable the 'Smart Replace' option
            self.render_node.smart_replace = True

            # self.render_node.bit_depth = '10-bit'
            self.render_node.bit_depth = '16-bit fp'
            # self.render_node.bit_depth = '32-bit fp'

            if self.clip_shot_name:
                self.render_node.shot_name = self.clip_shot_name

            # self.render_node.format = "Multi-Channel"
            # self.render_node.format = "RGB-A"

            # add version note
            self.render_node.note = "This node was configured by projekt_comp."
            # add version note collapsed state
            self.render_node.note_collapsed = True

        # ------------------------------------------------------------------ #

        def add_write_node():

            # Create write node

            self.render_node = flame.batch.create_node('Write File')

            self.render_node.range_start = int(str(flame.batch.start_frame))
            self.render_node.range_end = int(str(self.batch_group.start_frame)) + int(str(self.clip_duration)) - 1

            self.render_node.frame_rate = self.clip_frame_rate

            self.render_node.source_timecode = self.clip_timecode
            self.render_node.record_timecode = self.clip_timecode

            self.render_node.name = self.clip_shot_name + '_comp'
            # self.render_node.name = self.clip_name + '_mattes'
            # self.render_node.name = self.clip_name + '_multichannel'
            # self.render_node.name = self.clip_name + '_neat_video'
            # self.render_node.name = self.clip_name + '_precomp'

            self.render_node.destination = ('Batch Reels', 'comp')
            # self.render_node.destination = ('Batch Reels', 'mattes')
            # self.render_node.destination = ('Batch Reels', 'multichannel')
            # self.render_node.destination = ('Batch Reels', 'neat_video')
            # self.render_node.destination = ('Batch Reels', 'precomp')

            # self.render_node.destination = ('Libraries', 'Batch Renders')

            # Enable the 'Add to Workspace' option
            self.render_node.add_to_workspace = True

            # Enable the 'Smart Replace' option
            self.render_node.smart_replace = True

            image_format = self.settings.write_file_image_format.split(' ', 1)[0]
            bit_depth = self.settings.write_file_image_format.split(' ', 1)[1]
            # bit_depth = '32-bit fp'

            self.render_node.file_type = image_format
            self.render_node.bit_depth = bit_depth

            self.render_node.media_path = self.settings.write_file_media_path
            self.render_node.media_path_pattern = self.settings.write_file_pattern
            self.render_node.create_clip = self.settings.write_file_create_open_clip
            self.render_node.include_setup = self.settings.write_file_include_setup
            self.render_node.create_clip_path = self.settings.write_file_create_open_clip_value
            self.render_node.include_setup_path = self.settings.write_file_include_setup_value

            if self.settings.write_file_compression:
                self.render_node.compress = True
                self.render_node.compress_mode = self.settings.write_file_compression
            if image_format == 'Jpeg':
                self.render_node.quality = 100

            self.render_node.frame_index_mode = self.settings.write_file_frame_index
            self.render_node.frame_padding = int(self.settings.write_file_padding)

            self.render_node.shot_name = self.clip_shot_name

            # self.render_node.format = "Multi-Channel"
            # self.render_node.format = "RGB-A"

            # add version note
            self.render_node.note = "comp openclip for: " + str(self.render_node.shot_name) + " configured by logik-projekt."

            # add version note collapsed state
            self.render_node.note_collapsed = True

            if self.settings.write_file_create_open_clip:
                self.render_node.version_mode = 'Follow Iteration' # Enable for final comps.
                # self.render_node.version_mode = 'Custom Version' # Enable for intermediate renders.
                self.render_node.version_name = self.settings.write_file_version_name

                # add version number
                # self.render_node.version_number = 1 # Enable if using 'Custom Version'
                # add version padding
                # self.render_node.version_padding = 4 # Enable if using 'Custom Version'

        # ------------------------------------------------------------------ #

        # Add MUX node

        mux_node = self.batch_group.create_node('MUX')
        mux_node.pos_x = self.x_position + 288
        mux_node.pos_y = self.y_position - 24

        # ------------------------------------------------------------------ #

        # Add Neat Video node

        # neat_video_node = self.batch_group.create_node('OpenFX')
        # neat_video_node.change_plugin('Reduce Noise v5')
        # neat_video_node.pos_x = self.x_position + 288
        # neat_video_node.pos_y = self.y_position - 24

        # ------------------------------------------------------------------ #

        # Add Render Node or Write File Node

        if self.settings.render_node_type == 'Render Node':
            add_render_node()
        else:
            add_write_node()

        self.render_node.pos_x = mux_node.pos_x + 288
        self.render_node.pos_y = mux_node.pos_y - 0

        # ------------------------------------------------------------------ #

        # Connect nodes

        flame.batch.connect_nodes(clip, 'Default', mux_node, 'Default')
        flame.batch.connect_nodes(mux_node, 'Default', self.render_node, 'Default')
        # flame.batch.connect_nodes(clip, 'Default', neat_video_node, 'Default')
        # flame.batch.connect_nodes(neat_video_node, 'Default', self.render_node, 'Default')

        self.y_position = self.y_position - 192

        pyside6_qt_print(SCRIPT_NAME, f'Added MUX nodes added for: {self.clip_name}')

    # ---------------------------------------------------------------------- #

    def output_node_setup(self):
        output_node_setup = pyside6_qt_output_config_ui(
            settings=self.settings,
            script_name=SCRIPT_NAME,
            config_path=CONFIG_PATH,
            version=VERSION
        )
        output_node_setup.output_node_setup()

# -------------------------------------------------------------------------- #

def projekt_comp_media_panel_clips(selection):

    script = class_projekt_openclip_comp(selection)
    script.media_panel_projekt_comp_clips()

# -------------------------------------------------------------------------- #

def projekt_comp_batch_clips(selection):

    script = class_projekt_openclip_comp(selection)
    script.batch_projekt_comp_clips()

# -------------------------------------------------------------------------- #

def setup(selection):

    script = class_projekt_openclip_comp(selection)
    script.output_node_setup()

# -------------------------------------------------------------------------- #

# Scopes

def scope_clip(selection):
    import flame

    for item in selection:
        if isinstance(item, (flame.PyClip, flame.PyClipNode)):
            return True
    return False

# -------------------------------------------------------------------------- #

def scope_folder(selection):
    import flame

    for item in selection:
        if isinstance(item, (flame.PyFolder)):
            return True
    return False

# -------------------------------------------------------------------------- #

def scope_library(selection):
    import flame

    for item in selection:
        if isinstance(item, (flame.PyLibrary)):
            return True
    return False

# -------------------------------------------------------------------------- #

def scope_segment(selection):
    import flame

    for item in selection:
        if isinstance(item, flame.PySegment):
            return True
    return False

# -------------------------------------------------------------------------- #

def scope_seq(selection):
    import flame

    for item in selection:
        if isinstance(item, flame.PySequence):
            return True
    return False

# -------------------------------------------------------------------------- #

# Flame Menus

def get_batch_custom_ui_actions():

    return [
        {
            'name': 'logik-projekt',
            'hierarchy': [],
            'actions': []
        },
        {
            'name': 'create-openclip',
            'hierarchy': ['logik-projekt'],
            'order': 0,
            'actions': [
                {
                    'name': 'projekt_comp selected clips',
                    'order': 0,
                    'separator': 'below',
                    'isVisible': scope_clip,
                    'execute': projekt_comp_batch_clips,
                    'minimumVersion': '2025'
                }
            ]
        }
    ]

# -------------------------------------------------------------------------- #

def get_main_menu_custom_ui_actions():

    return [
        {
            'name': 'logik-projekt',
            'hierarchy': [],
            'actions': []
        },
        {
            'name': 'create-openclip',
            'hierarchy': ['logik-projekt'],
            'order': 0,
            'actions': [
                {
                    'name': 'configure projekt_comp',
                    'execute': setup,
                    'minimumVersion': '2025'
                }
           ]
        }
    ]

# -------------------------------------------------------------------------- #

def get_media_panel_custom_ui_actions():

    return [
        {
            'name': 'logik-projekt',
            'hierarchy': [],
            'actions': []
        },
        {
            'name': 'create-openclip',
            'hierarchy': ['logik-projekt'],
            'order': 0,
            'actions': [
                {
                    'name': 'projekt_comp selected clips',
                    'order': 0,
                    'separator': 'below',
                    'isVisible': scope_clip,
                    'execute': projekt_comp_media_panel_clips,
                    'minimumVersion': '2025'
                }
            ]
        }
    ]

# -------------------------------------------------------------------------- #

# def get_timeline_custom_ui_actions():

#     return [
#         {
#             'name': 'logik-projekt',
#             'hierarchy': [],
#             'actions': []
#         },
#         {
#             'name': 'create-openclip',
#             'hierarchy': ['logik-projekt'],
#             'order': 0,
#             'actions': [
#                 {
#                     'name': 'projekt_comp selected clips',
#                     'order': 0,
#                     'separator': 'below',
#                     "isVisible": scope_segment,
#                     'execute': projekt_comp_media_panel_clips,
#                     'minimumVersion': '2025'
#                 }
#             ]
#         }

#      ]

# ========================================================================== #
# This section defines how to handle the main script function.
# ========================================================================== #

# # If this script is executed as main:
# # Call functions for immediate execution
# if __name__ == "__main__":

# ========================================================================== #
# C2 A9 32 30 32 34 2D 4D 41 4E 2D 4D 41 44 45 2D 4D 45 4B 41 4E 59 5A 4D 53 #
# ========================================================================== #

# Changelist:

# -------------------------------------------------------------------------- #
# version:               0.0.1
# modified:              2024-05-07 - 21:48:20
# comments:              Refactored monolithic code to discreet modules
# -------------------------------------------------------------------------- #
# version:               0.0.2
# modified:              2024-05-07 - 21:49:31
# comments:              Added docstrings
# -------------------------------------------------------------------------- #
# version:               0.0.3
# modified:              2024-05-07 - 21:50:00
# comments:              Prep for initial production test
# -------------------------------------------------------------------------- #
# version:               0.0.4
# modified:              2024-05-09 - 13:18:47
# comments:              Refactored code works in flame 2025. Time to tidy up.
# -------------------------------------------------------------------------- #
# version:               0.0.5
# modified:              2024-05-17 - 13:36:42
# comments:              Replaced FlameButton with pyside6_qt_button
# -------------------------------------------------------------------------- #
# version:               0.0.6
# modified:              2024-05-17 - 13:37:49
# comments:              Replaced FlameClickableLineEdit with pyside6_qt_clickable_line_edit
# -------------------------------------------------------------------------- #
# version:               0.0.7
# modified:              2024-05-17 - 13:38:19
# comments:              Replaced FlameLabel with pyside6_qt_label
# -------------------------------------------------------------------------- #
# version:               0.0.8
# modified:              2024-05-17 - 13:38:29
# comments:              Replaced FlameLineEdit with pyside6_qt_line_edit
# -------------------------------------------------------------------------- #
# version:               0.0.9
# modified:              2024-05-17 - 13:39:27
# comments:              Replaced FlameListWidget with pyside6_qt_list_widget
# -------------------------------------------------------------------------- #
# version:               0.1.0
# modified:              2024-05-17 - 13:39:47
# comments:              Replaced FlameMessageWindow with pyside6_qt_message_window
# -------------------------------------------------------------------------- #
# version:               0.1.1
# modified:              2024-05-17 - 13:40:01
# comments:              Replaced FlamePasswordWindow with pyside6_qt_password_window
# -------------------------------------------------------------------------- #
# version:               0.1.2
# modified:              2024-05-17 - 13:40:28
# comments:              Replaced FlamePresetWindow with pyside6_qt_preset_window
# -------------------------------------------------------------------------- #
# version:               0.1.3
# modified:              2024-05-17 - 13:40:37
# comments:              Replaced FlameProgressWindow with pyside6_qt_progress_window
# -------------------------------------------------------------------------- #
# version:               0.1.4
# modified:              2024-05-17 - 13:41:39
# comments:              Replaced FlamePushButton with pyside6_qt_push_button
# -------------------------------------------------------------------------- #
# version:               0.1.5
# modified:              2024-05-17 - 13:41:49
# comments:              Replaced FlamePushButtonMenu with pyside6_qt_push_button_menu
# -------------------------------------------------------------------------- #
# version:               0.1.6
# modified:              2024-05-17 - 13:42:30
# comments:              Replaced FlameQDialog with pyside6_qt_qdialog
# -------------------------------------------------------------------------- #
# version:               0.1.7
# modified:              2024-05-17 - 13:44:20
# comments:              Replaced FlameSlider with pyside6_qt_slider
# -------------------------------------------------------------------------- #
# version:               0.1.8
# modified:              2024-05-17 - 13:44:30
# comments:              Replaced FlameTextEdit with pyside6_qt_text_edit
# -------------------------------------------------------------------------- #
# version:               0.1.9
# modified:              2024-05-17 - 13:44:39
# comments:              Replaced FlameTokenPushButton with pyside6_qt_token_push_button
# -------------------------------------------------------------------------- #
# version:               0.2.0
# modified:              2024-05-17 - 13:45:12
# comments:              Replaced FlameTreeWidget with pyside6_qt_tree_widget
# -------------------------------------------------------------------------- #
# version:               0.2.1
# modified:              2024-05-17 - 13:45:29
# comments:              Replaced FlameWindow with pyside6_qt_window
# -------------------------------------------------------------------------- #
# version:               0.2.2
# modified:              2024-05-17 - 13:45:43
# comments:              Replaced pyflame_file_browser with pyside6_qt_file_browser
# -------------------------------------------------------------------------- #
# version:               0.2.3
# modified:              2024-05-17 - 13:47:07
# comments:              Replaced pyflame_get_flame_version with pyside6_qt_get_flame_version
# -------------------------------------------------------------------------- #
# version:               0.2.4
# modified:              2024-05-17 - 13:47:43
# comments:              Replaced pyflame_get_shot_name with pyside6_qt_get_shot_name
# -------------------------------------------------------------------------- #
# version:               0.2.5
# modified:              2024-05-17 - 13:47:56
# comments:              Replaced pyflame_load_config with pyside6_qt_load_config
# -------------------------------------------------------------------------- #
# version:               0.2.6
# modified:              2024-05-17 - 13:49:42
# comments:              Replaced pyflame_open_in_finder with pyside6_qt_open_in_finder
# -------------------------------------------------------------------------- #
# version:               0.2.7
# modified:              2024-05-17 - 13:49:51
# comments:              Replaced pyflame_print with pyside6_qt_print
# -------------------------------------------------------------------------- #
# version:               0.2.8
# modified:              2024-05-17 - 13:50:00
# comments:              Replaced pyflame_refresh_hooks with pyside6_qt_refresh_hooks
# -------------------------------------------------------------------------- #
# version:               0.2.9
# modified:              2024-05-17 - 13:50:10
# comments:              Replaced pyflame_resolve_path_tokens with pyside6_qt_resolve_path_tokens
# -------------------------------------------------------------------------- #
# version:               0.3.0
# modified:              2024-05-17 - 13:50:21
# comments:              Replaced pyflame_resolve_shot_name with pyside6_qt_resolve_shot_name
# -------------------------------------------------------------------------- #
# version:               0.3.1
# modified:              2024-05-17 - 13:50:32
# comments:              Replaced pyflame_save_config with pyside6_qt_save_config
# -------------------------------------------------------------------------- #
# version:               0.3.2
# modified:              2024-05-17 - 15:16:41
# comments:              Replaced pyside6_qt_textedit with pyside6_qt_text_edit
# -------------------------------------------------------------------------- #
# version:               0.3.3
# modified:              2024-05-17 - 15:48:00
# comments:              Replaced pyside6_qt_push_buttonMenu with pyside6_qt_push_button_menu
# -------------------------------------------------------------------------- #
# version:               0.4.3
# modified:              2024-05-18 - 18:00:39
# comments:              Added GNU GPLv3 Disclaimer.
# -------------------------------------------------------------------------- #
# version:               0.4.4
# modified:              2024-05-18 - 18:46:09
# comments:              Minor modification to Disclaimer.
# -------------------------------------------------------------------------- #
# version:               0.4.5
# modified:              2024-06-04 - 17:38:52
# comments:              Added 'Smart Replace' option for render and write nodes
# -------------------------------------------------------------------------- #
# version:               0.4.6
# modified:              2024-06-05 - 19:30:33
# comments:              Added a new script to create openclip multichannel
# -------------------------------------------------------------------------- #
# version:               0.4.7
# modified:              2024-06-05 - 21:08:34
# comments:              Modified note strings
# -------------------------------------------------------------------------- #
# version:               0.4.8
# modified:              2024-06-26 - 22:31:48
# comments:              Fixed missing import statements for pyside6_qt_label
# -------------------------------------------------------------------------- #
# version:               0.4.8
# modified:              2024-07-11 - 08:39:06
# comments:              Added new schematic reels for batch groups
# -------------------------------------------------------------------------- #
# version:               0.4.9
# modified:              2024-07-11 - 08:41:36
# comments:              Fixed a version bug for the changelist updater script
# -------------------------------------------------------------------------- #
# version:               0.5.0
# modified:              2024-08-31 - 18:26:05
# comments:              prep for release.
# -------------------------------------------------------------------------- #
# version:               1.0.0
# modified:              2024-10-30 - 07:35:26
# comments:              Refactored PySide6 Output Node Config UI.
# -------------------------------------------------------------------------- #
