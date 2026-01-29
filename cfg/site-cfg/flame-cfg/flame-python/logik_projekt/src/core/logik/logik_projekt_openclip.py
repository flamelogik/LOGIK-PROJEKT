#!/usr/bin/env python3
# -------------------------------------------------------------------------- #
# Filename:     logik_projekt_openclip.py
# Purpose:      Create OpenClip for LOGIK-PROJEKT clips.
# Description:  LOGIK-PROJEKT OpenClip core module to create OpenClips
# Author:       phil_man@mac.com
# Copyright:    Copyright (c) 2025
# Disclaimer:   Disclaimer at bottom of script.
# License:      GNU General Public License v3.0 (GPL-3.0).
#               https://www.gnu.org/licenses/gpl-3.0.en.html

# Version:      2027.0.0
# Status:       Development
# Type:         Application
# Created:      2025-07-01
# Modified:     2025-11-15

# Changelog:    Changelog at bottom of script.
# -------------------------------------------------------------------------- #

# -------------------------------------------------------------------------- #
# Imports
# -------------------------------------------------------------------------- #

# Standard library imports
import os
import sys
import logging
from pathlib import Path
from typing import List



# Third-party imports (from Flame's PySide6 Qt modules)
from src.core.ui.orchestrators.pyside6_qt_flame_ui import (
    pyside6_qt_load_config,
    pyside6_qt_output_config_ui,
    pyside6_qt_print,
    pyside6_qt_get_shot_name,
)

# ========================================================================== #
# Logging Setup
# ========================================================================== #

def setup_logging(tool_name):
    """Sets up logging to file and console."""
    
    # Determine the logs directory relative to the 'logik_projekt' directory
    current_script_path = Path(__file__).resolve()
    # Navigate up from 'scripts' -> 'logik_projekt_openclip' -> 'openclip_tools' -> 'logik_projekt'
    logik_projekt_base_path = current_script_path.parent.parent.parent.parent
    log_dir = logik_projekt_base_path / 'logs'
    os.makedirs(log_dir, exist_ok=True)
    
    log_file = log_dir / f"{tool_name}.log"

    # Get the root logger
    logger = logging.getLogger(tool_name)
    
    # Prevent adding handlers multiple times if the script is reloaded
    if logger.hasHandlers():
        logger.handlers.clear()

    logger.setLevel(logging.DEBUG)
    logger.propagate = False # Prevent passing logs to the root logger in Flame

    # Create formatter
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

    # Create file handler
    file_handler = logging.FileHandler(log_file)
    file_handler.setLevel(logging.DEBUG)
    file_handler.setFormatter(formatter)
    logger.addHandler(file_handler)

    # Create stream handler for console output
    stream_handler = logging.StreamHandler()
    stream_handler.setLevel(logging.DEBUG) # User wants to see debug statements
    stream_handler.setFormatter(formatter)
    logger.addHandler(stream_handler)

    return logger

# ========================================================================== #
# Base Class for OpenClip Operations
# ========================================================================== #

class LogikProjektOpenClipBase:
    """Base class for creating and managing OpenClips in Flame."""
    tool_name = None
    version = None

    def __init__(self, selection: List):
        self.selection = selection
        self.script_name = str(self.tool_name)
        
        self.logger = setup_logging(self.script_name)
        
        self.logger.info(f"--- Starting {self.script_name} {self.version} ---")

        # Define paths relative to the script location
        current_script_path = Path(__file__).resolve()
        # The config directory is a sibling to the 'scripts' directory where this file lives
        tool_family_path = current_script_path.parent.parent
        self.config_path = str(tool_family_path / 'config' / self.tool_name)
        self.logger.debug(f"Config path set to: {self.config_path}")

        # Ensure the configuration directory exists to prevent FileNotFoundError
        os.makedirs(self.config_path, exist_ok=True)

        # Load config file
        self.logger.debug("Loading settings...")
        loaded_settings = pyside6_qt_load_config(self.script_name, self.config_path, self._get_default_settings())

        # Workaround for pyside6_qt_load_config returning a function
        if callable(loaded_settings):
            self.logger.warning("pyside6_qt_load_config returned a function. Falling back to default settings.")
            self.settings = self._get_default_settings()
        else:
            self.settings = loaded_settings
            self.logger.debug("Settings loaded successfully.")
        
        # Sanitize settings by converting string booleans to actual booleans
        self.logger.debug("Sanitizing boolean settings.")
        def to_bool(value):
            return str(value).lower() in ('true', '1', 't', 'y', 'yes')
        
        boolean_keys = ['write_file_create_open_clip', 'write_file_include_setup']
        for key in boolean_keys:
            if key in self.settings:
                original_value = self.settings[key]
                self.settings[key] = to_bool(original_value)
                self.logger.debug(f"Sanitized '{key}': '{original_value}' -> {self.settings[key]}")

        # Init Variables
        self.y_position = 0
        self.x_position = 0
        self.batch_duration = 1
        self.batch_group = None
        self.clip_name = ""
        self.clip_duration = 0
        self.clip_frame_rate = 0.0
        self.clip_timecode = ""
        self.clip_shot_name = ""
        self.render_node = None
        self.logger.debug("Base class initialized.")

    def _get_default_settings(self):
        # Default settings must use strings for boolean values to satisfy the config loader.
        return {
            'render_node_type': 'Write File Node',
            'write_file_media_path': '/PROJEKTS/',
            'write_file_pattern': '<project nickname>/shots/<shot name>/media/renders/<name>_<version name>/<name>_<version name><frame><ext>',
            'write_file_create_open_clip': 'True',
            'write_file_include_setup': 'True',
            'write_file_create_open_clip_value': '<project nickname>/shots/<shot name>/openclip/output_clips/flame/<name><ext>',
            'write_file_include_setup_value': '<project nickname>/shots/<shot name>/batch_setups/<name>_<version name>_<workstation>_<user nickname><ext>',
            'write_file_image_format': 'OpenEXR 16-bit fp',
            'write_file_compression': 'DWAA',
            'write_file_padding': '8',
            'write_file_frame_index': 'Use Start Frame',
            'write_file_version_name': 'v<version>'
        }

    def get_clip_info(self, clip):
        """Extracts necessary information from the clip."""
        self.clip_name = str(clip.name)[1:-1]
        self.clip_duration = clip.duration
        self.clip_frame_rate = clip.clip.frame_rate
        self.clip_timecode = clip.clip.start_time
        self.clip_shot_name = pyside6_qt_get_shot_name(clip)
        self.logger.debug(f"Extracted info for clip: {self.clip_name}")

    def batch_projekt_clips(self):
        """Processes clips that are already in a batch."""
        import flame
        self.logger.info("Processing clips in current batch...")
        self.batch_group = flame.batch
        self._setup_reels()

        for clip in self.selection:
            self.x_position = clip.pos_x
            self.y_position = clip.pos_y
            self.get_clip_info(clip)
            self.create_batch_nodes(clip)

        self.batch_group.frame_all()
        self.logger.info("Batch processing complete.")

    def media_panel_projekt_clips(self):
        """Processes clips from the media panel by creating a new batch."""
        import flame
        self.logger.info("Processing clips from media panel...")
        flame.go_to('Batch')

        batch_group_name = f'projekt_{self.tool_name.split("_")[-1]}'
        self.logger.debug(f"Creating new batch group: {batch_group_name}")
        batch_group = flame.batch.create_batch_group(batch_group_name, reels=self._get_reel_names())
        sources_reel = batch_group.reels[0]
        batch_group.expanded = False

        for clip in self.selection:
            flame.media_panel.copy(clip, sources_reel)
        self.logger.debug(f"Copied {len(self.selection)} clips to new batch.")

        self.selection = flame.batch.nodes
        self.selection.reverse()

        clip_pos_y = 192
        for clip in self.selection:
            clip_pos_y += 192
            clip.pos_y = clip_pos_y
            if int(str(clip.duration)) > int(str(batch_group.duration)):
                batch_group.duration = int(str(clip.duration))

        self.batch_projekt_clips()
        batch_group.frame_all()

    def _setup_reels(self):
        import flame
        reel_names = self._get_reel_names()
        self.logger.debug(f"Setting up schematic reels: {reel_names}")
        
        reel_map = {
            'Schematic Reel': 'sources', 'Schematic Reel 1': 'sources',
            'Schematic Reel 2': 'reference', 'Schematic Reel 3': 'CGI',
            'Schematic Reel 4': 'depth'
        }
        for reel in flame.batch.reels:
            if reel.name in reel_map:
                new_name = reel_map[reel.name]
                reel.name = new_name
                self.logger.info(f"Renamed schematic reel '{reel.name}' to '{new_name}'.")

        existing_reels = [r.name for r in flame.batch.reels]
        for reel_name in reel_names:
            if reel_name not in existing_reels:
                flame.batch.create_reel(reel_name)
                self.logger.info(f"Created new schematic reel named '{reel_name}'.")

    def _get_reel_names(self):
        return ["sources", "reference", "CGI", "depth", "graphics", "mattes", "motion", "multichannel", "neat_video", "nuke", "paint", "precomp", "roto", "comp"]

    def create_batch_nodes(self, clip):
        """Creates the nodes for a given clip."""
        import flame
        self.logger.debug(f"Creating batch nodes for clip: {self.clip_name}")

        processing_node = self._add_processing_node(clip)

        if self.settings['render_node_type'] == 'Render Node':
            self._add_render_node()
        else:
            self._add_write_node()

        self.render_node.pos_x = processing_node.pos_x + 288
        self.render_node.pos_y = processing_node.pos_y

        self._connect_nodes(clip, processing_node, self.render_node)

        self.y_position -= 192
        message = f'Added nodes for: {self.clip_name}'
        pyside6_qt_print(self.script_name, message)
        self.logger.info(message)

    def _add_processing_node(self, clip):
        """Adds the primary processing node (e.g., MUX). Can be overridden."""
        import flame
        self.logger.debug("Adding MUX node.")
        mux_node = self.batch_group.create_node('MUX')
        mux_node.pos_x = self.x_position + 288
        mux_node.pos_y = self.y_position - 24
        return mux_node

    def _connect_nodes(self, clip, processing_node, render_node):
        """Connects the nodes. Can be overridden."""
        import flame
        self.logger.debug(f"Connecting {clip.name} -> {processing_node.name} -> {render_node.name}")
        flame.batch.connect_nodes(clip, 'Default', processing_node, 'Default')
        flame.batch.connect_nodes(processing_node, 'Default', render_node, 'Default')

    def _add_render_node(self):
        import flame
        self.logger.debug("Adding Render node.")
        self.render_node = self.batch_group.create_node('Render')
        self._configure_common_node_settings()
        
        self.render_node.destination = ('Libraries', 'Batch Renders')
        self.render_node.add_to_workspace = True
        self.render_node.note = f"This node was configured by {self.tool_name}."
        
        self._configure_specialized_render_node()

    def _add_write_node(self):
        import flame
        self.logger.debug("Adding Write File node.")
        self.render_node = self.batch_group.create_node('Write File')
        self._configure_common_node_settings()

        self.render_node.add_to_workspace = True
        self.render_node.media_path = self.settings['write_file_media_path']
        self.render_node.media_path_pattern = self.settings['write_file_pattern']
        self.render_node.create_clip = self.settings['write_file_create_open_clip']
        self.render_node.include_setup = self.settings['write_file_include_setup']
        self.render_node.create_clip_path = self.settings['write_file_create_open_clip_value']
        self.render_node.include_setup_path = self.settings['write_file_include_setup_value']
        self.render_node.frame_index_mode = self.settings['write_file_frame_index']
        self.render_node.frame_padding = int(self.settings['write_file_padding'])
        self.render_node.note = f"{self.tool_name.split('_')[-1]} openclip for: {self.clip_shot_name} configured by logik-projekt."

        if self.settings['write_file_compression']:
            self.render_node.compress = True
            self.render_node.compress_mode = self.settings['write_file_compression']
        
        image_format = self.settings['write_file_image_format'].split(' ', 1)[0]
        if image_format == 'Jpeg':
            self.render_node.quality = 100

        self._configure_specialized_write_node()

    def _configure_common_node_settings(self):
        self.logger.debug("Configuring common node settings.")
        self.render_node.range_start = self.batch_group.start_frame
        self.render_node.range_end = int(str(self.batch_group.start_frame)) + int(str(self.clip_duration)) - 1
        self.render_node.frame_rate = self.clip_frame_rate
        self.render_node.source_timecode = self.clip_timecode
        self.render_node.record_timecode = self.clip_timecode
        self.render_node.note_collapsed = True
        if self.clip_shot_name:
            self.render_node.shot_name = self.clip_shot_name

    def output_node_setup(self):
        """Opens the configuration UI."""
        self.logger.info("Opening configuration UI.")
        output_node_setup = pyside6_qt_output_config_ui(
            settings=self.settings,
            script_name=self.script_name,
            config_path=self.config_path,
            version=self.version
        )
        output_node_setup.output_node_setup()

    # --- Abstract methods for specialization ---
    def _configure_specialized_render_node(self):
        raise NotImplementedError("This method should be implemented by a subclass.")

    def _configure_specialized_write_node(self):
        raise NotImplementedError("This method should be implemented by a subclass.")

# ========================================================================== #
# Specialized Subclasses
# ========================================================================== #

class LogikProjektOpenClipComp(LogikProjektOpenClipBase):
    tool_name = 'logik_projekt_openclip_comp'
    version = 'v2.0'

    def _configure_specialized_render_node(self):
        self.logger.debug("Configuring specialized Render node for Comp.")
        self.render_node.name = f"{self.clip_shot_name}_comp"
        self.render_node.smart_replace = True
        self.render_node.bit_depth = '16-bit fp'

    def _configure_specialized_write_node(self):
        self.logger.debug("Configuring specialized Write File node for Comp.")
        self.render_node.name = f"{self.clip_shot_name}_comp"
        self.render_node.destination = ('Batch Reels', 'comp')
        self.render_node.smart_replace = True
        image_format, bit_depth = self.settings['write_file_image_format'].split(' ', 1)
        self.render_node.file_type = image_format
        self.render_node.bit_depth = bit_depth
        if self.settings['write_file_create_open_clip']:
            self.render_node.version_mode = 'Follow Iteration'
            self.render_node.version_name = self.settings['write_file_version_name']

class LogikProjektOpenClipMattes(LogikProjektOpenClipBase):
    tool_name = 'logik_projekt_openclip_mattes'
    version = 'v2.0'

    def _configure_specialized_render_node(self):
        self.logger.debug("Configuring specialized Render node for Mattes.")
        self.render_node.name = f"{self.clip_name}_mattes"
        self.render_node.smart_replace = False
        self.render_node.bit_depth = '16-bit fp'

    def _configure_specialized_write_node(self):
        self.logger.debug("Configuring specialized Write File node for Mattes.")
        self.render_node.name = f"{self.clip_name}_mattes"
        self.render_node.destination = ('Batch Reels', 'mattes')
        self.render_node.smart_replace = False
        image_format, bit_depth = self.settings['write_file_image_format'].split(' ', 1)
        self.render_node.file_type = image_format
        self.render_node.bit_depth = bit_depth
        if self.settings['write_file_create_open_clip']:
            self.render_node.version_mode = 'Custom Version'
            self.render_node.version_name = self.settings['write_file_version_name']
            self.render_node.version_number = 1
            self.render_node.version_padding = 4

class LogikProjektOpenClipMultichannel(LogikProjektOpenClipBase):
    tool_name = 'logik_projekt_openclip_multichannel'
    version = 'v2.0'

    def _configure_specialized_render_node(self):
        self.logger.debug("Configuring specialized Render node for Multichannel.")
        self.render_node.name = f"{self.clip_name}_multichannel"
        self.render_node.smart_replace = False
        self.render_node.bit_depth = '32-bit fp'
        self.render_node.format = "Multi-Channel"

    def _configure_specialized_write_node(self):
        self.logger.debug("Configuring specialized Write File node for Multichannel.")
        self.render_node.name = f"{self.clip_name}_multichannel"
        self.render_node.destination = ('Batch Reels', 'multichannel')
        self.render_node.smart_replace = False
        self.render_node.file_type = self.settings['write_file_image_format'].split(' ', 1)[0]
        self.render_node.bit_depth = '32-bit fp'
        self.render_node.format = "Multi-Channel"
        if self.settings['write_file_create_open_clip']:
            self.render_node.version_mode = 'Custom Version'
            self.render_node.version_name = self.settings['write_file_version_name']
            self.render_node.version_number = 1
            self.render_node.version_padding = 4

class LogikProjektOpenClipNeatVideo(LogikProjektOpenClipBase):
    tool_name = 'logik_projekt_openclip_neat_video'
    version = 'v2.0'

    def _add_processing_node(self, clip):
        import flame
        self.logger.debug("Adding OpenFX Reduce Noise node.")
        neat_video_node = self.batch_group.create_node('OpenFX')
        neat_video_node.change_plugin('Reduce Noise v5')
        neat_video_node.pos_x = self.x_position + 288
        neat_video_node.pos_y = self.y_position - 24
        return neat_video_node

    def _connect_nodes(self, clip, processing_node, render_node):
        import flame
        self.logger.debug(f"Connecting {clip.name} -> {processing_node.name} -> {render_node.name}")
        flame.batch.connect_nodes(clip, 'Default', processing_node, 'Default')
        flame.batch.connect_nodes(processing_node, 'Default', render_node, 'Default')

    def _configure_specialized_render_node(self):
        self.logger.debug("Configuring specialized Render node for Neat Video.")
        self.render_node.name = f"{self.clip_name}_neat_video"
        self.render_node.smart_replace = False
        self.render_node.bit_depth = '16-bit fp'

    def _configure_specialized_write_node(self):
        self.logger.debug("Configuring specialized Write File node for Neat Video.")
        self.render_node.name = f"{self.clip_name}_neat_video"
        self.render_node.destination = ('Batch Reels', 'neat_video')
        self.render_node.smart_replace = False
        image_format, bit_depth = self.settings['write_file_image_format'].split(' ', 1)
        self.render_node.file_type = image_format
        self.render_node.bit_depth = bit_depth
        if self.settings['write_file_create_open_clip']:
            self.render_node.version_mode = 'Custom Version'
            self.render_node.version_name = self.settings['write_file_version_name']
            self.render_node.version_number = 1
            self.render_node.version_padding = 4

class LogikProjektOpenClipPrecomp(LogikProjektOpenClipBase):
    tool_name = 'logik_projekt_openclip_precomp'
    version = 'v2.0'

    def _configure_specialized_render_node(self):
        self.logger.debug("Configuring specialized Render node for Precomp.")
        self.render_node.name = f"{self.clip_name}_precomp"
        self.render_node.smart_replace = False
        self.render_node.bit_depth = '16-bit fp'

    def _configure_specialized_write_node(self):
        self.logger.debug("Configuring specialized Write File node for Precomp.")
        self.render_node.name = f"{self.clip_name}_precomp"
        self.render_node.destination = ('Batch Reels', 'precomp')
        self.render_node.smart_replace = False
        image_format, bit_depth = self.settings['write_file_image_format'].split(' ', 1)
        self.render_node.file_type = image_format
        self.render_node.bit_depth = bit_depth
        if self.settings['write_file_create_open_clip']:
            self.render_node.version_mode = 'Custom Version'
            self.render_node.version_name = self.settings['write_file_version_name']
            self.render_node.version_number = 1
            self.render_node.version_padding = 4


# -------------------------------------------------------------------------- #

# DISCLAIMER:   This file is part of LOGIK-PROJEKT.

#               Copyright © 2025 STRENGTH IN NUMBERS

#               LOGIK-PROJEKT creates directories, files, scripts & tools
#               for use with Autodesk Flame and other software.

#               LOGIK-PROJEKT is free software.

#               You can redistribute it and/or modify it under the terms
#               of the GNU General Public License as published by the
#               Free Software Foundation, either version 3 of the License,
#               or any later version.

#               This program is distributed in the hope that it will be
#               useful, but WITHOUT ANY WARRANTY; without even the

#               implied warranty of MERCHANTABILITY or
#               FITNESS FOR A PARTICULAR PURPOSE.

#               See the GNU General Public License for more details.
#               You should have received a copy of the GNU General
#               Public License along with this program.

#               If not, see <https://www.gnu.org/licenses/gpl-3.0.en.html>.

#               Contact: phil_man@mac.com

# -------------------------------------------------------------------------- #
# C2 A9 32 30 32 35 53 54 52 45 4E 47 54 48 2D 49 4E 2D 4E 55 4D 42 45 52 53 #
# -------------------------------------------------------------------------- #
# Changelog:
# -------------------------------------------------------------------------- #
