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

# File Name:        pyside6_qt_load_config.py
# Version:          1.0.1
# Created:          2024-01-19
# Modified:         2024-11-16

# ========================================================================== #
# This section imports the necessary modules.
# ========================================================================== #

# Standard library imports
import ast
import datetime
import functools
import importlib.util
import os
import re
import shutil
import subprocess
import typing
from typing import (
    Union,
    List,
    Dict,
    Optional,
    Callable
)
import xml
import xml.etree.ElementTree as ET

# Third Party library imports
from PySide6 import (
    QtWidgets,
    QtCore,
    QtGui
)

# from ..classes.pyside6_qt_message_window import pyside6_qt_message_window

# ========================================================================== #
# This section imports the pyflame functions.

# from classes_and_functions.functions.example import (
#     example_function as new_function_name
# )

# ========================================================================== #

# from pyside6_qt_get_flame_version import (
#     pyside6_qt_get_flame_version as pyside6_qt_get_flame_version
# )

# from pyside6_qt_get_shot_name import (
#     pyside6_qt_get_shot_name as pyside6_qt_get_shot_name
# )

# from pyside6_qt_file_browser import (
#     pyside6_qt_file_browser as pyside6_qt_file_browser
# )

# from pyside6_qt_load_config import (
#     pyside6_qt_load_config as pyside6_qt_load_config
# )

# from pyside6_qt_open_in_finder import (
#     pyside6_qt_open_in_finder as pyside6_qt_open_in_finder
# )

from pyside6_qt_print import (
    pyside6_qt_print as pyside6_qt_print
)

# from pyside6_qt_refresh_hooks import (
#     pyside6_qt_refresh_hooks as pyside6_qt_refresh_hooks
# )

# from pyside6_qt_resolve_path_tokens import (
#     pyside6_qt_resolve_path_tokens as pyside6_qt_resolve_path_tokens
# )

# from pyside6_qt_resolve_shot_name import (
#     pyside6_qt_resolve_shot_name as pyside6_qt_resolve_shot_name
# )

from pyside6_qt_save_config import (
    pyside6_qt_save_config as pyside6_qt_save_config
)

# ========================================================================== #
# This section defines the main function.
# ========================================================================== #

def pyside6_qt_load_config(script_name: str, script_path: str, config_values: Dict[str, str]):
    '''
    Use to create and load XML config files for scripts.

    Default config values are passed in as a dict.

    Attributes will be created based on the key names.

    If a config file doesn't exist, a default config file will be 
    created/saved from the provied config_values dict.

    New config values can be added to the config_values dict that may not 
    exist in the config file. 

    These will be added to the config file when it is saved using 
    pyside6_qt_save_config()

    Config file will be loaded/saved to: 
    
    /opt/Autodesk/shared/python/man_made_material/openclip_workflow/SCRIPT_NAME/config/config.xml

    pyside6_qt_load_config(script_name, script_path, config_values)

    script_name: [str] Name of script.

    script_path: [str] Path to script.

    config_values: [Dict] Default config values. 
                    Keys and values must be strings. 
                    Attributes will be added based on key names.

    Example:

    self.settings = pyside6_qt_load_config(SCRIPT_NAME, SCRIPT_PATH, {
        'camera_path': '/opt/Autodesk',
        'scene_scale': '100',
        'import_type': 'Action Objects',
        'st_map_setup': 'False',
    })

    This will create the following attributes:

    self.settings.camera_path
    self.settings.scene_scale
    self.settings.import_type
    self.settings.st_map_setup

    The following conversions will be done to strings in the config dict:
        'True' or 'False' will be converted to bools.
        Numbers will be converted to ints or floats.
        Strings that begin and end with brackets will be converted to lists.
        Strings that begin and end with curly brackets will be converted to dicts.
    '''

    # Check argument types

    if not isinstance(script_name, str):
        raise TypeError('script_name: script_name must be a string.')
    
    if not isinstance(script_path, str):
        raise TypeError('script_path: script_path must be a string.')
    
    elif not isinstance(config_values, dict):
        raise TypeError('config_values: config_values must be a dict.')
    
    for key, value in config_values.items():

        if not isinstance(key, str):
            raise TypeError('config_values: config_values keys must be strings.')
        
        if not isinstance(value, str):
            raise TypeError('config_values: config_values values must be strings.')

    # ------------------------------

    def create_default_config(script_name: str, config_values: Dict):
        '''
        Save out default config file from config_values dict.
        '''

        def dict_to_xml(tag, d):
            '''
            Turn dict of key/value pairs into XML
            '''

            elem = ET.Element(tag)
            for key, val in d.items():
                child = ET.Element(key)
                child.text = str(val)
                elem.append(child)
            return elem

        def indent(elem, level=0):
            '''
            Add indentation to XML file
            '''

            i = '\n' + level*'    '
            if len(elem):
                if not elem.text or not elem.text.strip():
                    elem.text = i + '    '
                if not elem.tail or not elem.tail.strip():
                    elem.tail = i
                for elem in elem:
                    indent(elem, level+1)
                if not elem.tail or not elem.tail.strip():
                    elem.tail = i
            else:
                if level and (not elem.tail or not elem.tail.strip()):
                    elem.tail = i

        pyside6_qt_print(script_name, f'Config file not found. Creating default config file: {config_xml}')

        # # Create config folder if it doesn't exist

        # if not os.path.isdir(config_path):
        #     try:
        #         os.makedirs(config_path)
        #     except:
        #         pyside6_qt_message_window('error', f'{script_name}: Error', f'Unable to create folder: {config_path}<br>Check folder permissions')

        # Create and save XML config file

        root = dict_to_xml(f'{script_name.lower()}_settings', config_values)
        indent(root)
        xml_tree = ET.ElementTree(root)
        xml_tree.write(config_xml)

    def load_xml(config_values):
        '''
        Load config file and return dict of values.
        '''

        # Load XML config file

        xml_tree = ET.parse(config_xml)
        root = xml_tree.getroot()

        for child in root:
                xml_value = child.text
                for key, value in config_values.items():
                    if child.tag == key:
                        config_values[key] = xml_value
        return config_values

    def convert_value_type(value):
        '''
        Convert string to bool, list, dict, int, or float if needed
        '''

        if value == 'True' or value == 'False':
            value = ast.literal_eval(value) # convert string to bool
        elif value == None:
            value = ''
        else:
            try:
                value = int(value) # convert string to int
            except ValueError:
                try:
                    value = float(value) # convert string to float
                except ValueError:
                    if value.startswith('[') and value.endswith(']'):
                        value = ast.literal_eval(value) # convert string to list
                    elif value.startswith('{') and value.endswith('}'):
                        value = ast.literal_eval(value) # convert string to dict
        return value

    print(f'Loading config...\n')

    script_name = script_name.replace(' ', '_')

    # Set config paths

    config_path = os.path.join(script_path, 'config')
    # config_xml = os.path.join(config_path, 'config.xml')
    config_xml = os.path.join(script_path, 'config.xml')
    print(f'    Config path: {config_xml}\n')

    # Create default config file if it doesn't exist

    if not os.path.exists(config_xml):
        create_default_config(script_name, config_values)

    # Load XML config file

    config_value_dict = load_xml(config_values)

    # Convert config to attributes

    print('    Config values:\n')

    for key, value in config_value_dict.items():
        value = convert_value_type(value) # Convert value to correct type
        print(f'        {key}: {value}')
        setattr(pyside6_qt_load_config, key, value)

    print('\n')

    pyside6_qt_print(script_name, 'Config loaded.')

    return pyside6_qt_load_config

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
# modified:              2024-10-30 - 07:35:27
# comments:              Refactored PySide6 Output Node Config UI.
# -------------------------------------------------------------------------- #
# version:               1.0.1
# modified:              2024-11-16 - 16:52:07
# comments:              Fixed circular import statements
# -------------------------------------------------------------------------- #
