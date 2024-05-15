# filename: pyflame_save_config.py

'''
# -------------------------------------------------------------------------- #

# File Name:        pyflame_save_config.py
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

# from pyflame_save_config import (
#     pyflame_save_config as pyflame_save_config
# )

# ========================================================================== #
# This section defines the main function.
# ========================================================================== #

def pyflame_save_config(
    script_name: str, 
    script_path: str, 
    config_values: Dict[str, str]
):
    '''
    Use to save settings to XML config file.

    Config file will be saved to: /opt/Autodesk/shared/python/man_made_material/openclip_workflow/SCRIPT_NAME/config/config.xml

    pyflame_save_config(script_name, script_path, config_values_dict)

    script_name: [str] Name of script.
    script_path: [str] Path to script.
    config_values: [Dict] Settings/values to be saved. Settings must already exist in config file to be saved.
                    Key is setting name, value is setting value. Setting values will be saved as strings.

    Example:

    pyflame_save_config(SCRIPT_NAME, SCRIPT_PATH, {
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
    config_xml = os.path.join(config_path, 'config.xml')
    print(f'    Config path: {config_xml}\n')

    # Save config

    save_xml(config_values)

    pyflame_print(script_name, 'Config saved.')

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
