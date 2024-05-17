# filename: pyflame_load_config.py

'''
# -------------------------------------------------------------------------- #

# File Name:        pyflame_load_config.py
# Version:          0.0.4
# Language:         python script
# Flame Version:    2025.x
# Author:           Phil MAN - phil_man@mac.com
# Toolset:          MAN_MADE_MATERIAL: LOGIK-PROJEKT
# Created:          2024-04-20
# Modified:         2024-05-09
# Modifier:         Phil MAN - phil_man@mac.com

# Description:      This program is part of a library of custom functions
#                   and modules for autodesk flame.

# Installation:     Copy the 'LOGIK-PROJEKT' repo to your GitHub directory,
#                   e.g. '/home/$USER/workspace/GitHub'

# Attribution:      This script is derived from work originally authored by
#                   Michael Vaglienty: 'pyflame_lib_script_template.py'

# Changelist:       The full changelist is at the end of this document.

# -------------------------------------------------------------------------- #
'''

# ========================================================================== #
# This section imports the necessary modules.
# ========================================================================== #

from PySide6 import (
    QtWidgets,
    QtCore,
    QtGui
)
import xml.etree.ElementTree as ET
from typing import (
    Union,
    List,
    Dict,
    Optional,
    Callable
)
import os
import re
import datetime
import shutil
import ast

# ========================================================================== #
# This section imports the pyflame functions.

# from classes_and_functions.functions.example import (
#     example_function as new_function_name
# )

# ========================================================================== #

# from pyflame_get_flame_version import (
#     pyflame_get_flame_version as pyflame_get_flame_version
# )

# from pyflame_get_shot_name import (
#     pyflame_get_shot_name as pyflame_get_shot_name
# )

# from pyflame_file_browser import (
#     pyflame_file_browser as pyflame_file_browser
# )

# from pyflame_load_config import (
#     pyflame_load_config as pyflame_load_config
# )

# from pyflame_open_in_finder import (
#     pyflame_open_in_finder as pyflame_open_in_finder
# )

from pyflame_print import (
    pyflame_print as pyflame_print
)

# from pyflame_refresh_hooks import (
#     pyflame_refresh_hooks as pyflame_refresh_hooks
# )

# from pyflame_resolve_path_tokens import (
#     pyflame_resolve_path_tokens as pyflame_resolve_path_tokens
# )

# from pyflame_resolve_shot_name import (
#     pyflame_resolve_shot_name as pyflame_resolve_shot_name
# )

from pyflame_save_config import (
    pyflame_save_config as pyflame_save_config
)

# ========================================================================== #
# This section defines the main function.
# ========================================================================== #

def pyflame_load_config(script_name: str, script_path: str, config_values: Dict[str, str]):
    '''
    Use to create and load XML config files for scripts.

    Default config values are passed in as a dict.

    Attributes will be created based on the key names.

    If a config file doesn't exist, a default config file will be 
    created/saved from the provied config_values dict.

    New config values can be added to the config_values dict that may not 
    exist in the config file. 

    These will be added to the config file when it is saved using 
    pyflame_save_config()

    Config file will be loaded/saved to: 
    
    /opt/Autodesk/shared/python/man_made_material/openclip_workflow/SCRIPT_NAME/config/config.xml

    pyflame_load_config(script_name, script_path, config_values)

    script_name: [str] Name of script.

    script_path: [str] Path to script.

    config_values: [Dict] Default config values. 
                    Keys and values must be strings. 
                    Attributes will be added based on key names.

    Example:

    self.settings = pyflame_load_config(SCRIPT_NAME, SCRIPT_PATH, {
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

        pyflame_print(script_name, f'Config file not found. Creating default config file: {config_xml}')

        # Create config folder if it doesn't exist

        if not os.path.isdir(config_path):
            try:
                os.makedirs(config_path)
            except:
                FlameMessageWindow('error', f'{script_name}: Error', f'Unable to create folder: {config_path}<br>Check folder permissions')

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
    config_xml = os.path.join(config_path, 'config.xml')
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
        setattr(pyflame_load_config, key, value)

    print('\n')

    pyflame_print(script_name, 'Config loaded.')

    return pyflame_load_config

# ========================================================================== #
# This section defines how to handle the main script function.
# ========================================================================== #

# # If this script is executed as main:
# # Call functions for immediate execution
# if __name__ == "__main__":

# ========================================================================== #
# C2 A9 2D 32 30 32 34 2D 4D 41 4E 5F 4D 41 44 45 5F 4D 41 54 45 52 49 61 4C #
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
