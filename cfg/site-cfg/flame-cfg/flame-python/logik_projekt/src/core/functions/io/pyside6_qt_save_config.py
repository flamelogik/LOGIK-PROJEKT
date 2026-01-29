#

# -------------------------------------------------------------------------- #

# File Name:        pyside6_qt_save_config.py
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

# ========================================================================== #
# This section defines the main function.
# ========================================================================== #

def pyside6_qt_save_config(
    script_name: str,
    script_path: str,
    config_values: Dict[str, str]
):
    '''
    Use to save settings to XML config file.

    Config file will be saved to: /opt/Autodesk/shared/python/man_made_material/openclip_workflow/SCRIPT_NAME/config/config.xml

    pyside6_qt_save_config(script_name, script_path, config_values_dict)

    script_name: [str] Name of script.
    script_path: [str] Path to script.
    config_values: [Dict] Settings/values to be saved. Settings must already exist in config file to be saved.
                    Key is setting name, value is setting value. Setting values will be saved as strings.

    Example:

    pyside6_qt_save_config(SCRIPT_NAME, SCRIPT_PATH, {
        'camera_path': camera_file_path,
        'scene_scale': settings.scene_scale,
        'import_type': settings.import_type,
        'st_map_setup': st_map_setup_button.isChecked(),
        'patch_setup': patch_setup_button.isChecked()
    })
    '''

    # Check argument types

    if not isinstance(script_name, str):
        raise TypeError('script_name: script_name must be a string.')
    if not isinstance(script_path, str):
        raise TypeError('script_path: script_path must be a string.')
    elif not isinstance(config_values, dict):
        raise TypeError('config_values: config_values must be a dict.')

    # ------------------------------

    def save_xml(config_values):

        def indent_new_element(element, level=1):
            '''
            Add new element indentation to XML file.
            '''

            i = "\n"
            if len(element):
                if not element.text or not element.text.strip():
                    element.text = i + "    "
                if not element.tail or not element.tail.strip():
                    element.tail = i
                for elem in element:
                    indent_new_element(elem, level+1)
                if not element.tail or not element.tail.strip():
                    element.tail = i
            else:
                if level and (not element.tail or not element.tail.strip()):
                    element.tail = i

        def fix_indentation(file_path, spaces="    "):
            '''
            Fixes indentation of XML file. All lines except first and last line will be indented by 4 spaces.
            '''

            with open(file_path, "r") as f:
                lines = f.readlines()
            for i in range(1, len(lines)-1):
                if not lines[i].startswith(spaces):
                    lines[i] = spaces + lines[i]
            with open(file_path, "w") as f:
                f.writelines(lines)

        print('    Config Values:\n')

        # Save settings to config file

        xml_tree = ET.parse(config_xml)
        root = xml_tree.getroot()

        # loop through config_values dict and update XML file

        for key, value in config_values.items():
            xml_value = root.find(f'.//{key}')
            value = str(value)

            # Remove quotes from string values

            if value.startswith("'") and value.endswith("'"):
                value = value[1:-1]

            # If setting doesn't exist in config file, add it, if it does, update it

            if xml_value is None:
                xml_value = ET.Element(key)
                indent_new_element(xml_value)
                root.append(xml_value)
                xml_value.text = value
                print(f'        added: {key}: {value}')
            else:
                xml_value.text = value
                print(f'        updated: {key}: {value}')

        print('\n')

        xml_tree.write(config_xml)

        # Fix xml indentation

        fix_indentation(config_xml)

    print(f'Saving config...\n')

    script_name = script_name.replace(' ', '_')

    # Set config paths

    config_path = os.path.join(script_path, 'config')
    # config_xml = os.path.join(config_path, 'config.xml')
    config_xml = os.path.join(script_path, 'config.xml')
    print(f'    Config path: {config_xml}\n')

    # Save config

    save_xml(config_values)

    pyside6_qt_print(script_name, 'Config saved.')

# ========================================================================== #
# Changelist
# ========================================================================== #

# version:               1.0.4
# modified:              2025-11-15
# comments:              Fixed import to use full package path
# -------------------------------------------------------------------------- #
# version:               1.0.3
# modified:              2025-02-25 - 07:01:22
# comments:              Added legacy support for PySide2 imports
# -------------------------------------------------------------------------- #