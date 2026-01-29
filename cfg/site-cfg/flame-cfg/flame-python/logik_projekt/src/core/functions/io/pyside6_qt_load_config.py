#

# -------------------------------------------------------------------------- #

# File Name:        pyside6_qt_load_config.py
# Version:          1.0.4
# Created:          2024-01-19
# Modified:         2025-11-15

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
try:
    from PySide6 import (
        QtWidgets,
        QtCore,
        QtGui,
    )
except ImportError:
    from PySide2 import (
        QtWidgets,
        QtCore,
        QtGui,
    )

# ========================================================================== #
# Import required widget functions
# ========================================================================== #

from src.core.functions.print.pyside6_qt_print import pyside6_qt_print
from src.core.functions.io.pyside6_qt_save_config import pyside6_qt_save_config

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
# Changelist
# ========================================================================== #

# version:               1.0.4
# modified:              2025-11-15
# comments:              Fixed imports to use full package paths
# -------------------------------------------------------------------------- #
# version:               1.0.3
# modified:              2025-02-25 - 07:01:21
# comments:              Added legacy support for PySide2 imports
# -------------------------------------------------------------------------- #