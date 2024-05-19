'''
Script Name: pyflame_lib_mmm_comp.py
Script Version: 1.1
Script Family: MAN_MADE_MATERIAL
Modified by: Phil MAN phil_man@mac.com
Modification Date: 2023-12-05
Based on original python by: Michael Vaglienty
Creation Date: 02.15.22
Flame Version: 2025

This file contains a library various custom UI widgets that can be used to build QT windows similar to the look of Flame along with some other useful functions.

This file should be placed in same folder as main script.

To avoid conflicts with having multiple copies within /opt/Autodesk/shared/python, file should be renamed to: pyflame_lib_<script name>.py

Usage:

    import as module in script:

    from pyflame_lib_<script name> import FlameButton, FlameLabel, FlameSlider...

Updates:

    v1.1 2023-12-05

        Updated script to use PySide6 for compatibility with flame 2025.

    01.18.23

        Added pyflame_load_config and pyflame_save_config functions for saving and loading config files.

    01.02.23

        pyflame_print / FlameMessageWindow: Error print messages now print in yellow, warning messages now print in red.

    12.04.22

        Updated class descriptions

    11.21.22

        Added Teal color for FlameWindow color bar

        Added text argument to FlameProgerssBar Class

        Added enable done button argument to FlameProgressBar Class

        Added color bars to FlameProgressBar Class

    07.14.22

        Added pyflame_open_in_finder function. Opens supplied path in System Finder.

        Shot name resolver: If camera source name is passed, first eight characters will be used as shot name.
'''

# -------------------------------------------------------------------------- #

# File Name:        experimental_comp.py
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

# ========================================================================== #
# This section imports the necessary modules.
# ========================================================================== #

try:
    from PySide6 import QtWidgets, QtCore, QtGui
except ImportError:
    from PySide2 import QtWidgets, QtCore, QtGui
import xml.etree.ElementTree as ET
from typing import Union, List, Dict, Optional, Callable
import os, re, datetime, shutil, ast

def pyflame_get_shot_name(shot_name_source) -> str:
        '''
        Extract shot name from PyClipNode object or string.

        shot_name_source: PyClipNode object, or string.

        If a PyClipNode object is passed that has a shot name is assigned to the clip, that will be returned. If no shot name is assigned,
        the shot name will be extracted from the clip name.
        '''
        import flame

        # Check argument type

        if not isinstance(shot_name_source, (flame.PyClipNode, str)):
            raise TypeError('shot_name_source must be a PyClipNode object or string.')

        # Extract shot name from PyClipNode object. If no shot name is assigned, extract shot name from clip name.

        if isinstance(shot_name_source, flame.PyClipNode):
            shot_name = str(shot_name_source.clip.versions[0].tracks[0].segments[0].shot_name)[1:-1]
            if shot_name != '':
                return shot_name
            else:
                shot_name = str(shot_name_source.name)[1:-1]

        # Try to parse shot name from clip name

        try:
            # Split clip name into list by numbers in clip name

            shot_name_split = re.split(r'(\d+)', shot_name)
            shot_name_split = [s for s in shot_name_split if s != '']
            #print('shot_name_split:', shot_name_split)

            # Recombine shot name split list into new batch group name
            # Else statement is used if clip name starts with number

            if shot_name_split[1].isalnum():
                shot_name = shot_name_split[0] + shot_name_split[1]
            else:
                shot_name = shot_name_split[0] + shot_name_split[1] + shot_name_split[2]
        except:
            # If shot name can't be split, pass clip name as shot name
            pass

        return shot_name

#

def pyflame_print(script_name: str, message: str, message_type: Optional[str]='message', time: Optional[int]=3) -> None:
    '''
    Print message to terminal. If using Flame 2023.1 or later also prints to the Flame message window

    script_name: Name of script [str]
    message: Message to print. Warning message will print red, Error message will print yellow. [str]
    message_type: Type of message (message, error, warning) [str]
    time: Amount of time to display message for [int]

    Example:

        pyflame_print('Script Name', 'Config not found.', message_type='error')
    '''

    import flame

    # Check argument values

    if not isinstance(script_name, str):
        raise TypeError('Pyflame Print: script_name must be a string')
    if not isinstance(message, str):
        raise TypeError('Pyflame Print: message must be a string')
    if message_type not in ['message', 'error', 'warning']:
        raise ValueError('Pyflame Print: message Type must be one of: message, error, warning')
    if not isinstance(time, int):
        raise TypeError('Pyflame Print: time must be an integer')

    # Print to terminal/shell

    if message_type == 'warning':
        # print message text in red
        print(f'\033[91m--> {message}\033[0m\n')
    elif message_type == 'error':
        # print message text in yellow
        print(f'\033[93m--> {message}\033[0m\n')
    else:
        print(f'--> {message}\n')

    # Print to Flame Message Window - Flame 2023.1 and later
    # Warning and error intentionally swapped to match color of message window

    script_name =script_name.upper()

    try:
        if message_type == 'message' or message_type == 'confirm':
            flame.messages.show_in_console(f'{script_name}: {message}', 'info', time)
        elif message_type == 'error':
            flame.messages.show_in_console(f'{script_name}: {message}', 'warning', time)
        elif message_type == 'warning':
            flame.messages.show_in_console(f'{script_name}: {message}', 'error', time)
    except:
        pass

#

def pyflame_get_flame_version() -> float:
    import flame
    '''
    Get version of flame and return float value

    2022 returns as 2022.0
    2022.1.1 returns as 2022.1
    2022.1.pr145 returns as 2022.1

    Example:

        flame_version = pyflame_get_flame_version()
    '''

    flame_version = flame.get_version()

    if 'pr' in flame_version:
        flame_version = flame_version.rsplit('.pr', 1)[0]
    if len(flame_version) > 6:
        flame_version = flame_version[:6]
    flame_version = float(flame_version)

    print('Flame Version:', flame_version, '\n')

    return flame_version

#

def pyflame_file_browser(title: str, extension: List[str], default_path: str='/opt/Autodesk', select_directory: Optional[bool]=False, multi_selection: Optional[bool]=False, include_resolution: Optional[bool]=False, use_flame_browser: Optional[bool]=True, window_to_hide=[]) -> Union[str, list]:
    '''
    Opens QT file browser window(Flame 2022 - Flame 2023). Flame's file browser is used 2023.1 and later.

    title: File browser window title. [str]
    extension: File extension filter. [''] for directories. [list]
    default_path: Open file browser to this path. [str]
    select_directory: (optional) Ability to select directories. Default False.[bool]
    multi_selection: (optional) Ability to select multiple files/folders. Default False. [bool]
    include_resolution: (optional) Enable resolution controls in flame browser. Default False. [bool]
    use_flame_browser: (optional) - Use Flame's file browser if using Flame 2023.1 or later. Default True [bool]
    window_to_hide: (optional) - Hide Qt window while file browser window is open. window is restored when browser is closed. [QWidget]

    When Multi Selection is enabled, the file browser will return a list. Otherwise it will return a string.

    Example:

        path = pyflame_file_browser('Load Undistort ST Map(EXR)', 'exr', self.undistort_map_path)
    '''

    import flame

    # Check argument values

    if not isinstance(extension, list):
        raise TypeError('Pyflame File Browser: extension must be a list.')
    if not isinstance(default_path, str):
        raise TypeError('Pyflame File Browser: default_path must be a string.')
    if not isinstance(select_directory, bool):
        raise TypeError('Pyflame File Browser: select_directory must be a boolean.')
    if not isinstance(multi_selection, bool):
        raise TypeError('Pyflame File Browser: multi_selection must be a boolean.')
    if not isinstance(include_resolution, bool):
        raise TypeError('Pyflame File Browser: include_resolution must be a boolean.')
    if not isinstance(window_to_hide, list):
        raise TypeError('Pyflame File Browser: window_to_hide must be a list.')

    # Clean up path

    while os.path.isdir(default_path) is not True:
        default_path = default_path.rsplit('/', 1)[0]
        if '/' not in default_path and not os.path.isdir(default_path):
            default_path = '/opt/Autodesk'
        print('Browser path:', default_path, '\n')

    # Open file browser

    if pyflame_get_flame_version() >= 2023.1 and use_flame_browser:

        # Hide Qt window while browser is open

        if window_to_hide:
            for window in window_to_hide:
                window.hide()

        # Open Flame file browser

        flame.browser.show(title=title, extension=extension, default_path=default_path, select_directory=select_directory, multi_selection=multi_selection, include_resolution=include_resolution)

        # Restore Qt windows

        if window_to_hide:
            for window in window_to_hide:
                window.show()

        # Return file path(s) from Flame file browser

        if flame.browser.selection:
            if multi_selection:
                return flame.browser.selection
            return flame.browser.selection[0]
    else:
        browser = QtWidgets.QFileDialog()
        browser.setDirectory(default_path)

        if select_directory:
            browser.setFileMode(QtWidgets.QFileDialog.FileMode.Directory) # Fix for flame 2025
        else:
            browser.setFileMode(QtWidgets.QFileDialog.FileMode.ExistingFile) # Fix for flame 2025
            browser.setNameFilter(f'*.{extension[0]}')

        if browser.exec_():
            return str(browser.selectedFiles()[0])

        return print('\n--> Import cancelled \n')

#

def pyflame_resolve_shot_name(name: str) -> str:
    '''
    Resolve shot name from provided string.

    name: name of shot(shot_0010) [str]

    Example:

        shot_name = pyflame_resolve_shot_name('shot_name')
    '''

    if not isinstance(name, str):
        raise TypeError('Pyflame Resolve Shot Name: name must be a string.')

    # Check if name is a camera source(such as: A010C0012). If so, use first 8 characters for shot name. If not, split name to find shot name.

    if re.match(r'^A\d{3}C\d{3}', name):
        shot_name = name[:8]
    else:
        shot_name_split = re.split(r'(\d+)', name)

        if len(shot_name_split) > 1:
            if shot_name_split[1].isalnum():
                shot_name = shot_name_split[0] + shot_name_split[1]
            else:
                shot_name = shot_name_split[0] + shot_name_split[1] + shot_name_split[2]
        else:
            shot_name = name

    return shot_name

#

def pyflame_resolve_path_tokens(path_to_resolve: str, PyObject=None, date=None) -> str:
    '''
    Use when resolving paths with tokens.

    pyflame_translate_path_tokens(path_to_resolve[, clip=flame_clip, date=datetime])

    path_to_resolve: Path with tokens to be translated. [str]
    PyObject: (optional) Flame PyObject. [flame.PyClip]
    date: (optional) Date/time to use for token translation. Default is None. If None is passed datetime value will be gotten each time function is run. [datetime]

    Supported tokens are:

    <ProjectName>, <ProjectNickName>, <UserName>, <UserNickName>, <YYYY>, <YY>, <MM>, <DD>, <Hour>, <Minute>, <AMPM>, <ampm>

    If a clip is passed, the following tokens will be translated:

    <ShotName>, <SeqName>, <SEQNAME>, <ClipName>, <Resolution>, <ClipHeight>, <ClipWidth>, <TapeName>

    Example:

        export_path = pyflame_translate_path_tokens(self.custom_export_path, clip, self.date)
    '''

    import flame

    if not isinstance(path_to_resolve, str):
        raise TypeError('Pyflame Translate Path Tokens: path_to_resolve must be a string')

    def get_seq_name(name):

        # Get sequence name abreviation from shot name

        seq_name = re.split('[^a-zA-Z]', name)[0]

        return seq_name

    print('Tokenized path to resolve:', path_to_resolve)

    # Get time values for token conversion

    if not date:
        date = datetime.datetime.now()

    yyyy = date.strftime('%Y')
    yy = date.strftime('%y')
    mm = date.strftime('%m')
    dd = date.strftime('%d')
    hour = date.strftime('%I')
    if hour.startswith('0'):
        hour = hour[1:]
    minute = date.strftime('%M')
    ampm_caps = date.strftime('%p')
    ampm = str(date.strftime('%p')).lower()

    # Replace tokens in path

    resolved_path = re.sub('<ProjectName>', flame.project.current_project.name, path_to_resolve)
    resolved_path = re.sub('<ProjectNickName>', flame.project.current_project.nickname, resolved_path)
    resolved_path = re.sub('<UserName>', flame.users.current_user.name, resolved_path)
    resolved_path = re.sub('<UserNickName>', flame.users.current_user.nickname, resolved_path)
    resolved_path = re.sub('<YYYY>', yyyy, resolved_path)
    resolved_path = re.sub('<YY>', yy, resolved_path)
    resolved_path = re.sub('<MM>', mm, resolved_path)
    resolved_path = re.sub('<DD>', dd, resolved_path)
    resolved_path = re.sub('<Hour>', hour, resolved_path)
    resolved_path = re.sub('<Minute>', minute, resolved_path)
    resolved_path = re.sub('<AMPM>', ampm_caps, resolved_path)
    resolved_path = re.sub('<ampm>', ampm, resolved_path)

    if PyObject:

        if isinstance(PyObject, flame.PyClip):

            clip = PyObject

            clip_name = str(clip.name)[1:-1]

            # Get shot name from clip

            try:
                if clip.versions[0].tracks[0].segments[0].shot_name != '':
                    shot_name = str(clip.versions[0].tracks[0].segments[0].shot_name)[1:-1]
                else:
                    shot_name = pyflame_resolve_shot_name(clip_name)
            except:
                shot_name = ''

            # Get tape name from clip

            try:
                tape_name = str(clip.versions[0].tracks[0].segments[0].tape_name)
            except:
                tape_name = ''

            # Get Seq Name from shot name

            seq_name = get_seq_name(shot_name)

            # Replace clip tokens in path

            resolved_path = re.sub('<ShotName>', shot_name, resolved_path)
            resolved_path = re.sub('<SeqName>', seq_name, resolved_path)
            resolved_path = re.sub('<SEQNAME>', seq_name.upper(), resolved_path)
            resolved_path = re.sub('<ClipName>', str(clip.name)[1:-1], resolved_path)
            resolved_path = re.sub('<Resolution>', str(clip.width) + 'x' + str(clip.height), resolved_path)
            resolved_path = re.sub('<ClipHeight>', str(clip.height), resolved_path)
            resolved_path = re.sub('<ClipWidth>', str(clip.width), resolved_path)
            resolved_path = re.sub('<TapeName>', tape_name, resolved_path)

        elif isinstance(PyObject, flame.PySegment):

            segment = PyObject

            segment_name = str(segment.name)[1:-1]

            # Get shot name from clip

            try:
                if segment.shot_name != '':
                    shot_name = str(segment.shot_name)[1:-1]
                else:
                    shot_name = pyflame_resolve_shot_name(segment_name)
            except:
                shot_name = ''

            # Get tape name from segment

            try:
                tape_name = str(segment.tape_name)
            except:
                tape_name = ''

            # Get Seq Name from shot name

            seq_name = get_seq_name(shot_name)

            # Replace segment tokens in path

            resolved_path = re.sub('<ShotName>', shot_name, resolved_path)
            resolved_path = re.sub('<SeqName>', seq_name, resolved_path)
            resolved_path = re.sub('<SEQNAME>', seq_name.upper(), resolved_path)
            resolved_path = re.sub('<ClipName>', segment_name, resolved_path)
            resolved_path = re.sub('<Resolution>', 'Unable to Resolve', resolved_path)
            resolved_path = re.sub('<ClipHeight>', 'Unable to Resolve', resolved_path)
            resolved_path = re.sub('<ClipWidth>', 'Unable to Resolve', resolved_path)
            resolved_path = re.sub('<TapeName>', tape_name, resolved_path)

        elif isinstance(PyObject, flame.PyBatch):

            batch = PyObject

            shot_name = ''

            for node in batch.nodes:
                if node.type in ('Render', 'Write File'):
                    if node.shot_name:
                        shot_name = str(node.shot_name)[1:-1]
                        break

            if not shot_name:
                shot_name = pyflame_resolve_shot_name(str(batch.name)[1:-1])

            # Get Seq Name from shot name

            seq_name = get_seq_name(shot_name)

            resolved_path = re.sub('<ShotName>', shot_name, resolved_path)
            resolved_path = re.sub('<SeqName>', seq_name, resolved_path)
            resolved_path = re.sub('<SEQNAME>', seq_name.upper(), resolved_path)

    print('Resolved path:', resolved_path, '\n')

    return resolved_path

#

def pyflame_refresh_hooks(script_name: Optional[str]='') -> None:
    '''
    Refresh python hooks and print message to terminal and Flame message window

    script_name: (optional) Name of script. This is displayed in the Flame message window. If none is passed 'PYTHON HOOKS' will be used [str]

    Example:

        pyflame_refresh_hooks('Script Name')
    '''

    import flame

    if not isinstance(script_name, str):
        raise TypeError('Pyflame Refresh Hooks: script_name must be a string')

    flame.execute_shortcut('Rescan Python Hooks')

    if not script_name:
        script_name = 'PYTHON HOOKS:'

    pyflame_print(script_name, 'Python hooks refreshed.')

#

def pyflame_open_in_finder(path: str) -> None:
    '''
    Open path in System Finder

    path: Path to open in Finder [str]
    '''

    import subprocess, platform

    # Check arguments

    if not isinstance(path, str):
        raise TypeError('Pyflame Open In Finder: Path must be a string')
    if not os.path.exists(path):
        raise FileNotFoundError('Pyflame Open In Finder: Path does not exist')

    # Open path in Finder

    if platform.system() == 'Darwin':
        subprocess.Popen(['open', path])
    else:
        subprocess.Popen(['xdg-open', path])

#

def pyflame_load_config(script_name: str, script_path: str, config_values: Dict[str, str]):
    '''
    Use to create and load XML config files for scripts.
    Default config values are passed in as a dict.
    Attributes will be created based on the key names.

    If a config file doesn't exist, a default config file will be created/saved from the provied config_values dict.
    New config values can be added to the config_values dict that may not exist in the config file. These will be added to the config file when it is saved using pyflame_save_config()

    Config file will be loaded/saved to: /opt/Autodesk/shared/python/man_made_material/openclip_workflow/SCRIPT_NAME/config/config.xml

    pyflame_load_config(script_name, script_path, config_values)

    script_name: [str] Name of script.
    script_path: [str] Path to script.
    config_values: [Dict] Default config values. Keys and values must be strings. Attributes will be added based on key names.

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

#

def pyflame_save_config(script_name: str, script_path: str, config_values: Dict[str, str]):
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

#

### Custom Flame QT UI Elements ###

#

class FlameButton(QtWidgets.QPushButton):
    '''
    Custom Qt Flame Button Widget

    FlameButton(button_name, connect[, button_color='normal', button_width=150, button_max_width=150])

    button_name: button text [str]
    connect: execute when clicked [function]
    button_color: (optional) normal, blue, red [str]
    button_width: (optional) default is 150 [int]
    button_max_width: (optional) default is 150 [int]

    Example:

        button = FlameButton('Button Name', do_something_magical_when_pressed, button_color='blue')
    '''

    def __init__(self, button_name: str, connect: Callable[..., None], button_color: Optional[str]='normal', button_width: Optional[int]=150, button_max_width: Optional[int]=150) -> None:
        super(FlameButton, self).__init__()

        # Check argument types

        if not isinstance(button_name, str):
            raise TypeError('FlameButton: button_name must be a string')
        elif button_color not in ['normal', 'blue', 'red']:
            raise ValueError('FlameButton: button_color must be one of: normal(grey), blue, or red')
        elif not isinstance(button_width, int):
            raise TypeError('FlameButton: button_width must be an integer')
        elif not isinstance(button_max_width, int):
            raise TypeError('FlameButton: button_max_width must be an integer')

        # Build button

        self.setText(button_name)
        self.setMinimumSize(QtCore.QSize(button_width, 28))
        self.setMaximumSize(QtCore.QSize(button_max_width, 28))
        self.setFocusPolicy(QtCore.Qt.NoFocus)
        self.clicked.connect(connect)
        if button_color == 'normal':
            self.setStyleSheet('QPushButton {color: rgb(154, 154, 154); background-color: rgb(58, 58, 58); border: none; font: 14px "Discreet"}'
                               'QPushButton:hover {border: 1px solid rgb(90, 90, 90)}'
                               'QPushButton:pressed {color: rgb(159, 159, 159); background-color: rgb(66, 66, 66); border: 1px solid rgb(90, 90, 90)}'
                               'QPushButton:disabled {color: rgb(116, 116, 116); background-color: rgb(58, 58, 58); border: none}'
                               'QPushButton::menu-indicator {subcontrol-origin: padding; subcontrol-position: center right}'
                               'QToolTip {color: rgb(170, 170, 170); background-color: rgb(71, 71, 71); border: 10px solid rgb(71, 71, 71)}')
        elif button_color == 'blue':
            self.setStyleSheet('QPushButton {color: rgb(190, 190, 190); background-color: rgb(0, 110, 175); border: none; font: 14px "Discreet"}'
                               'QPushButton:hover {border: 1px solid rgb(90, 90, 90)}'
                               'QPushButton:pressed {color: rgb(159, 159, 159); border: 1px solid rgb(90, 90, 90)'
                               'QPushButton:disabled {color: rgb(116, 116, 116); background-color: rgb(58, 58, 58); border: none}'
                               'QToolTip {color: rgb(170, 170, 170); background-color: rgb(71, 71, 71); border: 10px solid rgb(71, 71, 71)}')
        elif button_color == 'red':
            self.setStyleSheet('QPushButton {color: rgb(190, 190, 190); background-color: rgb(200, 29, 29); border: none; font: 14px "Discreet"}'
                               'QPushButton:hover {border: 1px solid rgb(90, 90, 90)}'
                               'QPushButton:pressed {color: rgb(159, 159, 159); border: 1px solid rgb(90, 90, 90)'
                               'QPushButton:disabled {color: rgb(116, 116, 116); background-color: rgb(58, 58, 58); border: none}'
                               'QToolTip {color: rgb(170, 170, 170); background-color: rgb(71, 71, 71); border: 10px solid rgb(71, 71, 71)}')

#

class FlameClickableLineEdit(QtWidgets.QLineEdit):
    '''
    Custom Qt Flame Clickable Line Edit Widget

    FlameClickableLineEdit(text, connect[, width=150, max_width=2000])

    text: text displayed in line edit [str]
    connect: execute when line edit is clicked on [function]
    width: (optional) width of widget. default is 150. [int]
    max_width: (optional) maximum width of widget. default is 2000 [int]

    Example:

        clickable_lineedit =  FlameClickableLineEdit('Some Text', some_function)
    '''

    clicked = QtCore.Signal()

    def __init__(self, text: str, connect: Callable[..., None], width: Optional[int]=150, max_width: Optional[int]=2000):
        super(FlameClickableLineEdit, self).__init__()

        # Check argument types

        if not isinstance(text, str):
            raise TypeError('FlameClickableLineEdit: text must be a string')
        elif not isinstance(width, int):
            raise TypeError('FlameClickableLineEdit: width must be an integer')
        elif not isinstance(max_width, int):
            raise TypeError('FlameClickableLineEdit: max_width must be an integer')

        # Build line edit

        self.setText(text)
        self.setMinimumHeight(28)
        self.setMinimumWidth(width)
        self.setMaximumWidth(max_width)
        self.setReadOnly(True)
        self.clicked.connect(connect)
        self.setFocusPolicy(QtCore.Qt.NoFocus)
        self.setStyleSheet('QLineEdit {color: rgb(154, 154, 154); background-color: rgb(55, 65, 75); selection-color: rgb(38, 38, 38); selection-background-color: rgb(184, 177, 167); border: 1px solid rgb(55, 65, 75); padding-left: 5px; font: 14px "Discreet"}'
                           'QLineEdit:focus {background-color: rgb(73, 86, 99)}'
                           'QLineEdit:hover {border: 1px solid rgb(90, 90, 90)}'
                           'QLineEdit:disabled {color: rgb(106, 106, 106); background-color: rgb(55, 55, 55); border: 1px solid rgb(55, 55, 55)}'
                           'QToolTip {color: rgb(170, 170, 170); background-color: rgb(71, 71, 71); border: 10px solid rgb(71, 71, 71)}')

    def mousePressEvent(self, event):
        if event.button() == QtCore.Qt.LeftButton:
            self.clicked.emit()
        else:
            super().mousePressEvent(event)

#

class FlameLabel(QtWidgets.QLabel):
    '''
    Custom Qt Flame Label Widget

    FlameLabel(label_name[, label_type='normal', label_width=150])

    label_name: text displayed [str]
    label_type: (optional) select from different styles: normal, underline, background. default is normal [str]
    label_width: (optional) default is 150 [int]

    Example:

        label = FlameLabel('Label Name', label_type='underline', label_width=300)
    '''

    def __init__(self, label_name: str, label_type: Optional[str]='normal', label_width: Optional[int]=150):
        super(FlameLabel, self).__init__()

        # Check argument types

        if not isinstance(label_name, str):
            raise TypeError('FlameLabel: label_name must be a string')
        elif not isinstance(label_type, str):
            raise TypeError('FlameLabel: label_type must be a string')
        elif label_type not in ['normal', 'underline', 'background']:
            raise ValueError('FlameLabel: label_type must be one of: normal, underline, background')
        elif not isinstance(label_width, int):
            raise TypeError('FlameLabel: label_width must be an integer')

        # Build label

        self.setText(label_name)
        self.setMinimumSize(label_width, 28)
        self.setMaximumHeight(28)
        self.setFixedHeight(28)
        self.setFocusPolicy(QtCore.Qt.NoFocus)

        # Set label stylesheet based on label_type

        if label_type == 'normal':
            self.setStyleSheet('QLabel {color: rgb(154, 154, 154); font: 14px "Discreet"}'
                               'QLabel:disabled {color: rgb(106, 106, 106)}')
        elif label_type == 'underline':
            self.setAlignment(QtCore.Qt.AlignCenter)
            self.setStyleSheet('QLabel {color: rgb(154, 154, 154); border-bottom: 1px inset rgb(40, 40, 40); font: 14px "Discreet"}'
                               'QLabel:disabled {color: rgb(106, 106, 106)}')
        elif label_type == 'background':
            self.setStyleSheet('QLabel {color: rgb(154, 154, 154); background-color: rgb(30, 30, 30); padding-left: 5px; font: 14px "Discreet"}'
                               'QLabel:disabled {color: rgb(106, 106, 106)}')

#

class FlameLineEdit(QtWidgets.QLineEdit):
    '''
    Custom Qt Flame Line Edit Widget

    FlameLineEdit(text[, width=150, max_width=2000])

    text: text show [str]
    width: (optional) width of widget. default is 150. [int]
    max_width: (optional) maximum width of widget. default is 2000. [int]

    Example:

        line_edit = FlameLineEdit('Some text here')
    '''

    def __init__(self, text: str, width: Optional[int]=150, max_width: Optional[int]=2000):
        super(FlameLineEdit, self).__init__()

        # Check argument types

        if not isinstance(text, str):
            raise TypeError('FlameLineEdit: text must be string.')
        if not isinstance(width, int):
            raise TypeError('FlameLineEdit: width must be integer.')
        if not isinstance(max_width, int):
            raise TypeError('FlameLineEdit: max_width must be integer.')

        # Build line edit

        self.setText(text)
        self.setMinimumHeight(28)
        self.setMinimumWidth(width)
        self.setMaximumWidth(max_width)
        self.setFocusPolicy(QtCore.Qt.ClickFocus)
        self.setStyleSheet('QLineEdit {color: rgb(154, 154, 154); background-color: rgb(55, 65, 75); selection-color: rgb(38, 38, 38); selection-background-color: rgb(184, 177, 167); border: 1px solid rgb(55, 65, 75); padding-left: 5px; font: 14px "Discreet"}'
                           'QLineEdit:focus {background-color: rgb(73, 86, 99)}'
                           'QLineEdit:hover {border: 1px solid rgb(90, 90, 90)}'
                           'QLineEdit:disabled {color: rgb(106, 106, 106); background-color: rgb(55, 55, 55); border: 1px solid rgb(55, 55, 55)}'
                           'QToolTip {color: rgb(170, 170, 170); background-color: rgb(71, 71, 71); border: none}')

#

class FlameListWidget(QtWidgets.QListWidget):
    '''
    Custom Qt Flame List Widget

    FlameListWidget([min_width=200, max_width=2000, min_height=250, max_height=2000])

    Example:

        list_widget = FlameListWidget()
    '''

    def __init__(self, min_width: Optional[int]=200, max_width: Optional[int]=2000, min_height: Optional[int]=250, max_height: Optional[int]=2000):
        super(FlameListWidget, self).__init__()

        # Check argument types

        if not isinstance(min_width, int):
            raise TypeError('FlameListWidget: min_width must be integer.')
        if not isinstance(max_width, int):
            raise TypeError('FlameListWidget: max_width must be integer.')
        if not isinstance(min_height, int):
            raise TypeError('FlameListWidget: min_height must be integer.')
        if not isinstance(max_height, int):
            raise TypeError('FlameListWidget: max_height must be integer.')

        # Build list widget

        self.setMinimumWidth(min_width)
        self.setMaximumWidth(max_width)
        self.setMinimumHeight(min_height)
        self.setMaximumHeight(max_height)
        self.spacing()
        self.setUniformItemSizes(True)
        self.setFocusPolicy(QtCore.Qt.NoFocus)
        self.setSelectionMode(QtWidgets.QAbstractItemView.SelectionMode.ExtendedSelection) # Fix for flame 2025
        self.setAlternatingRowColors(True)
        self.setStyleSheet('QListWidget {color: rgb(154, 154, 154); background-color: rgb(30, 30, 30); alternate-background-color: rgb(36, 36, 36); outline: 3px rgb(0, 0, 0); font: 14px "Discreet"}'
                           'QListWidget::item:selected {color: rgb(217, 217, 217); background-color: rgb(102, 102, 102); border: 1px solid rgb(102, 102, 102)}'
                           'QScrollBar {background: rgb(61, 61, 61)}'
                           'QScrollBar::handle {background: rgb(31, 31, 31)}'
                           'QScrollBar::add-line:vertical {border: none; background: none; width: 0px; height: 0px}'
                           'QScrollBar::sub-line:vertical {border: none; background: none; width: 0px; height: 0px}'
                           'QScrollBar {background: rgb(61, 61, 61)}'
                           'QScrollBar::handle {background: rgb(31, 31, 31)}'
                           'QScrollBar::add-line:horizontal {border: none; background: none; width: 0px; height: 0px}'
                           'QScrollBar::sub-line:horizontal {border: none; background: none; width: 0px; height: 0px}'
                           'QToolTip {color: rgb(170, 170, 170); background-color: rgb(71, 71, 71); border: 10px solid rgb(71, 71, 71)}')

#

class FlameMessageWindow(QtWidgets.QDialog):
    '''
    Custom Qt Flame Message Window

    FlameMessageWindow(message_type, message_title, message[, time=3, parent=None])

    message_type: Type of message window to be shown. Options are: confirm, message, error, warning [str] Confirm and warning return True or False values
    message_title: Text shown in top left of window ie. Confirm Operation [str]
    message: Text displayed in body of window [str]
    time: (optional) Time in seconds to display message in flame message area. Default is 3. [int]
    parent: (optional) - Parent window [QtWidget]

    Message Window Types:

        confirm: confirm and cancel button / grey left bar - returns True or False
        message: ok button / blue left bar
        error: ok button / yellow left bar
        warning: confirm and cancel button / red left bar - returns True of False

    Examples:

        FlameMessageWindow('error', f'{SCRIPT_NAME}: Error', f'Unable to create folder.<br>Check folder permissions')

        or

        if FlameMessageWindow('confirm', 'Confirm Operation', 'Some important message'):
            do something
    '''

    def __init__(self, message_type: str, message_title: str, message: str, time: int=3, parent=None):
        super(FlameMessageWindow, self).__init__()
        import flame

        # Check argument types

        if message_type not in ['confirm', 'message', 'error', 'warning']:
            raise ValueError('FlameMessageWindow: message_type must be one of: confirm, message, error, warning.')
        if not isinstance(message_title, str):
            raise TypeError('FlameMessageWindow: message_title must be a string.')
        if not isinstance(message, str):
            raise TypeError('FlameMessageWindow: message must be a string.')
        if not isinstance(time, int):
            raise TypeError('FlameMessageWindow: time must be an integer.')

        # Create message window

        self.message_type = message_type

        self.setWindowFlags(QtCore.Qt.FramelessWindowHint | QtCore.Qt.WindowStaysOnTopHint)
        self.setMinimumSize(QtCore.QSize(500, 330))
        self.setMaximumSize(QtCore.QSize(500, 330))
        self.setStyleSheet('background-color: rgb(36, 36, 36)')

        primaryScreen = QtWidgets.QApplication.primaryScreen() # resolution = QtWidgets.QDesktopWidget().screenGeometry()
        resolution = primaryScreen.geometry() # Fix for flame 2025
        self.move((resolution.width() / 2) - (self.frameSize().width() / 2),
                  (resolution.height() / 2) - (self.frameSize().height() / 2))

        self.setParent(parent)

        self.grid = QtWidgets.QGridLayout()

        self.main_label = FlameLabel(message_title, label_width=500)
        self.main_label.setStyleSheet('color: rgb(154, 154, 154); font: 18px "Discreet"')

        self.message_text_edit = QtWidgets.QPlainTextEdit(message) # Fix for flame 2025
        self.message_text_edit.setDisabled(True)
        self.message_text_edit.setStyleSheet('QPlainTextEdit {color: rgb(154, 154, 154); background-color: rgb(36, 36, 36); selection-color: rgb(190, 190, 190); selection-background-color: rgb(36, 36, 36); border: none; padding-left: 20px; padding-right: 20px; font: 12px "Discreet"}')  # Fix for flame 2025

        # Set confirm/ok button color

        if message_type == 'confirm':
            self.confirm_button = FlameButton('Confirm', self.confirm, button_color='blue', button_width=110)
        elif message_type == 'warning':
            self.confirm_button = FlameButton('Confirm', self.confirm, button_color='red', button_width=110)
        else:
            self.ok_button = FlameButton('Ok', self.confirm, button_color='blue', button_width=110)

        # Set layout for message window

        if message_type == 'confirm' or message_type == 'warning':
            self.cancel_button = FlameButton('Cancel', self.cancel, button_width=110)
            self.grid.addWidget(self.main_label, 0, 0)
            self.grid.setRowMinimumHeight(1, 30)
            self.grid.addWidget(self.message_text_edit, 2, 0, 4, 8)
            self.grid.setRowMinimumHeight(9, 30)
            self.grid.addWidget(self.cancel_button, 10, 5)
            self.grid.addWidget(self.confirm_button, 10, 6)
            self.grid.setRowMinimumHeight(11, 30)
        else:
            self.grid.addWidget(self.main_label, 0, 0)
            self.grid.setRowMinimumHeight(1, 30)
            self.grid.addWidget(self.message_text_edit, 2, 0, 4, 8)
            self.grid.setRowMinimumHeight(9, 30)
            self.grid.addWidget(self.ok_button, 10, 6)
            self.grid.setRowMinimumHeight(11, 30)

        message = message.replace('<br>', ' ')
        message = message.replace('<center>', '')
        message = message.replace('</center>', '')
        message = message.replace('<dd>', '')
        message = message.replace('<b>', '')
        message = message.replace('</b>', '')

        # Print to terminal/shell

        if message_type == 'warning':
            # print message text in red
            print(f'\033[91m\n--> {message_title}: {message}\033[0m\n')
        elif message_type == 'error':
            # print message text in yellow
            print(f'\033[93m\n--> {message_title}: {message}\033[0m\n')
        else:
            print(f'\n--> {message_title}: {message}\n')

        # Print message to Flame message window - only works in Flame 2023.1 and later
        # Warning and error intentionally swapped to match color of message window

        message_title = message_title.upper()

        try:
            if message_type == 'confirm' or message_type == 'message':
                flame.messages.show_in_console(f'{message_title}: {message}', 'info', time)
            elif message_type == 'error':
                flame.messages.show_in_console(f'{message_title}: {message}', 'warning', time)
            elif message_type == 'warning':
                flame.messages.show_in_console(f'{message_title}: {message}', 'error', time)
        except:
            pass

        self.setLayout(self.grid)
        self.exec()

    def __bool__(self):

        return self.confirmed

    def cancel(self):

        self.close()
        self.confirmed = False
        print('--> Cancelled\n')

    def confirm(self):

        self.close()
        self.confirmed = True
        if self.message_type == 'confirm':
            print('--> Confirmed\n')

    def paintEvent(self, event):
        painter = QtGui.QPainter(self)

        if self.message_type == 'confirm':
            line_color = QtGui.QColor(71, 71, 71)
        elif self.message_type == 'message':
            line_color = QtGui.QColor(0, 110, 176)
        elif self.message_type == 'error':
            line_color = QtGui.QColor(251, 181, 73)
        elif self.message_type == 'warning':
            line_color = QtGui.QColor(200, 29, 29)

        painter.setPen(QtGui.QPen(line_color, 6, QtGui.Qt.SolidLine)) # Fix for flame 2025
        painter.drawLine(0, 0, 0, 330)

        painter.setPen(QtGui.QPen(QtGui.QColor(71, 71, 71), .5, QtGui.Qt.SolidLine)) # Fix for flame 2025
        painter.drawLine(0, 40, 500, 40)

    def mousePressEvent(self, event):
        self.oldPosition = event.globalPos()

    def mouseMoveEvent(self, event):

        try:
            delta = QtCore.QPoint(event.globalPos() - self.oldPosition)
            self.move(self.x() + delta.x(), self.y() + delta.y())
            self.oldPosition = event.globalPos()
        except:
            pass

#

class FlamePasswordWindow(QtWidgets.QDialog):
    '''
    Custom Qt Flame Password Window

    FlamePasswordWindow(window_title, message[, user_name=False, parent=None])

    window_title: text shown in top left of window ie. Confirm Operation [str]
    message: text shown in window [str]
    user_name: if set to true a prompt for a user name will be included [bool]
    parent: (optional) parent window [object]

    Returns password as string

    Examples:

        for system password:

            password = str(FlamePasswordWindow('Enter System Password', 'System password needed to do something.'))

        username and password prompt:

            username, password = iter(FlamePasswordWindow('Login', 'Enter username and password.', user_name=True))
    '''

    def __init__(self, window_title: str, message: str, user_name: Optional[bool]=False, parent=None):
        super(FlamePasswordWindow, self).__init__()

        # Check argument types

        if not isinstance(window_title, str):
            raise TypeError('FlamePasswordWindow: window_title must be a string')
        if not isinstance(message, str):
            raise TypeError('FlamePasswordWindow: message must be a string')
        if not isinstance(user_name, bool):
            raise TypeError('FlamePasswordWindow: user_name must be a boolean')

        self.username = ''
        self.password = ''

        self.setWindowFlags(QtCore.Qt.FramelessWindowHint | QtCore.Qt.WindowStaysOnTopHint)
        self.setMinimumSize(QtCore.QSize(500, 300))
        self.setMaximumSize(QtCore.QSize(500, 230))
        self.setStyleSheet('background-color: rgb(36, 36, 36)')

        primaryScreen = QtWidgets.QApplication.primaryScreen() # resolution = QtWidgets.QDesktopWidget().screenGeometry()
        resolution = primaryScreen.geometry() # Fix for flame 2025
        self.move((resolution.width() / 2) - (self.frameSize().width() / 2),
                  (resolution.height() / 2) - (self.frameSize().height() / 2))

        self.setParent(parent)

        self.main_label = FlameLabel(window_title, label_width=500)
        self.main_label.setStyleSheet('color: rgb(154, 154, 154); font: 18px "Discreet"')

        self.message_label = FlameLabel(message, label_width=480)
        self.message_label.setStyleSheet('QLabel {color: rgb(154, 154, 154); background-color: rgb(36, 36, 36); padding-left: 20px; padding-right: 20px; font: 12px "Discreet"}')

        self.password_label = FlameLabel('Password', label_width=80)

        self.password_entry = FlameLineEdit('', width=300)
        self.password_entry.setEchoMode(QtWidgets.QLineEdit.EchoMode.Password) # Fix for flame 2025

        if user_name:
            self.username_label = FlameLabel('Username', label_width=80)
            self.username_entry = FlameLineEdit('', width=300)
            self.confirm_button = FlameButton('Confirm', self.username_password, button_color='blue', button_width=110)
        else:
            self.confirm_button = FlameButton('Confirm', self.system_password, button_color='blue', button_width=110)

        self.cancel_button = FlameButton('Cancel', self.cancel, button_width=110)

        # UI Widget Layout

        self.grid = QtWidgets.QGridLayout()
        self.grid.addWidget(self.main_label, 0, 0)
        self.grid.setRowMinimumHeight(1, 30)
        self.grid.addWidget(self.message_label, 2, 0)
        self.grid.setRowMinimumHeight(3, 30)

        if user_name:
            self.grid.addWidget(self.username_label, 4, 0)
            self.grid.addWidget(self.username_entry, 4, 1)

        self.grid.addWidget(self.password_label, 5, 0)
        self.grid.addWidget(self.password_entry, 5, 1)
        self.grid.setRowMinimumHeight(9, 60)
        self.grid.addWidget(self.cancel_button, 10, 5)
        self.grid.addWidget(self.confirm_button, 10, 6)
        self.grid.setRowMinimumHeight(11, 30)

        message = message.replace('<br>', '')
        message = message.replace('<center>', '')
        message = message.replace('<dd>', '')

        print(f'\n--> {window_title}: {message}\n')

        self.setLayout(self.grid)
        self.show()
        self.exec_()

    def __str__(self):

        return self.password

    def __iter__(self):

        yield from (self.username, self.password)

    def cancel(self):

        self.login = ''
        self.close()
        print('--> Cancelled.\n')
        return

    def username_password(self):

        if self.password_entry.text() and self.username_entry.text():
            self.close()

            self.username = self.username_entry.text()
            self.password = self.password_entry.text()

            return

    def system_password(self):

        password = self.password_entry.text()

        # Test password - return password if correct

        if password:
            import subprocess

            args = "sudo -S echo OK".split()
            kwargs = dict(stdout=subprocess.PIPE, encoding="ascii")

            kwargs.update(input=password)
            cmd = subprocess.run(args, **kwargs)

            if cmd.stdout:
                print('--> Password Correct\n')
                self.password = password
                self.close()
                return
            else:
                self.message_label.setText('Password incorrect, try again.')
                print('--> Password Incorrect\n')

    def paintEvent(self, event):
        painter = QtGui.QPainter(self)

        painter.setPen(QtGui.QPen(QtGui.QColor(200, 29, 29), 6, QtCore.Qt.SolidLine))
        painter.drawLine(0, 0, 0, 330)

        painter.setPen(QtGui.QPen(QtGui.QColor(71, 71, 71), .5, QtCore.Qt.SolidLine))
        painter.drawLine(0, 40, 500, 40)

    def mousePressEvent(self, event):
        self.oldPosition = event.globalPos()

    def mouseMoveEvent(self, event):

        try:
            delta = QtCore.QPoint(event.globalPos() - self.oldPosition)
            self.move(self.x() + delta.x(), self.y() + delta.y())
            self.oldPosition = event.globalPos()
        except:
            pass

#

class FlamePresetWindow():
    '''
    Custom Qt Flame Preset Window

    FlamePresetWindow(script_name, script_path, setup_window)

    window_title: Text shown in top left of window [str]
    script_name: Name of script [str]
    script_path: Path to script [str]
    setup_window: Setup window to open

    When creating a new preset, 'new_preset' is sent to the setup_window.
    When editing a preset, the path of the selected preset is sent to the setup window.

    The Save button in the setup window should return the name of the preset as a string.
    The Cancel button in the setup window should return the string 'cancel'

    Preset set as default will show an asterisk (*) next to the preset name.

    Example:

    return FlamePresetWindow(f'{SCRIPT_NAME}: Presets <small>{VERSION}', SCRIPT_NAME, SCRIPT_PATH, UberSaveSetup)
    '''

    def __init__(self, window_title: str, script_name: str, script_path: str, setup_window):
        import flame

        # Check argument types

        if not isinstance(window_title, str):
            raise TypeError('FlamePresetWindow: window_title must be a string')
        if not isinstance(script_name, str):
            raise TypeError('FlamePresetWindow: script_name must be a string')
        elif not isinstance(script_path, str):
            raise TypeError('FlamePresetWindow: script_path must be a string')

        # Set misc variables

        self.default_preset = ''
        self.script_name = script_name
        self.script_path = script_path
        self.setup_window = setup_window

        self.flame_prj_name = flame.project.current_project.project_name
        #print('flame_prj_name:', self.flame_prj_name)

        self.preset_settings_name = self.script_name.lower().replace(' ', '_') + '_preset_settings'
        #print('preset_settings_name:', self.preset_settings_name, '\n')

        # Set paths

        self.preset_config_xml = os.path.join(self.script_path, 'config', 'preset_config.xml')
        self.preset_path = os.path.join(self.script_path, 'config', 'preset')
        self.project_config_path = os.path.join(self.script_path, 'config', 'project')

        # Build window

        grid_layout = QtWidgets.QGridLayout()
        self.preset_window = FlameWindow(window_title, grid_layout, 670, 300)

        # Labels

        self.preset_label = FlameLabel('Current Project Preset', label_type='underline')

        # Shot Name Type Push Button Menu

        preset_list = self.build_preset_list()
        self.current_preset_push_btn = FlamePushButtonMenu('', preset_list)

        #  Buttons

        self.new_btn = FlameButton('New', self.new_preset, button_width=100)
        self.make_default_btn = FlameButton('Make Default', self.make_default, button_width=100)
        self.edit_btn = FlameButton('Edit', self.edit_preset, button_width=100)
        self.rename_btn = FlameButton('Rename', self.edit_preset, button_width=100)
        self.delete_btn = FlameButton('Delete', self.delete_preset, button_width=100)
        self.duplicate_btn = FlameButton('Duplicate', self.duplicate_preset, button_width=100)
        self.set_btn = FlameButton('Set', self.set, button_width=100)
        self.done_btn = FlameButton('Done', self.done, button_width=100)

        self.load_current_preset()

        # Preset Window layout

        grid_layout.setContentsMargins(10, 10, 10, 10) # grid_layout.setMargin(10) # Fix for flame 2025

        grid_layout.setRowMinimumHeight(1, 30)

        grid_layout.addWidget(self.preset_label, 4, 0, 1, 4)
        grid_layout.addWidget(self.current_preset_push_btn, 5, 0, 1, 4)

        grid_layout.addWidget(self.new_btn, 5, 5)
        grid_layout.addWidget(self.edit_btn, 6, 5)
        grid_layout.addWidget(self.set_btn, 7, 5)
        grid_layout.addWidget(self.make_default_btn, 5, 6)
        grid_layout.addWidget(self.duplicate_btn, 6, 6)
        grid_layout.addWidget(self.delete_btn, 7, 6)

        grid_layout.setRowMinimumHeight(8, 28)

        grid_layout.addWidget(self.done_btn, 9, 6)

        self.preset_window.setLayout(grid_layout)
        self.preset_window.show()

    def paintEvent(self, event):
        '''
        Add title bar line and side color lines to window
        '''

        painter = QtGui.QPainter(self)

        # Vertical line

        painter.setPen(QtGui.QPen(QtGui.QColor(0, 110, 176), 6, QtCore.Qt.SolidLine))
        painter.drawLine(0, 0, 0, 330)

        # Horizontal line

        painter.setPen(QtGui.QPen(QtGui.QColor(71, 71, 71), .5, QtCore.Qt.SolidLine))
        painter.drawLine(0, 40, 650, 40)

    # For moving frameless window

    def mousePressEvent(self, event):
        self.oldPosition = event.globalPos()

    def mouseMoveEvent(self, event):

        try:
            delta = QtCore.QPoint(event.globalPos() - self.oldPosition)
            self.move(self.x() + delta.x(), self.y() + delta.y())
            self.oldPosition = event.globalPos()
        except:
            pass

    # ----------------------------------------------------------------------------------------------------------------------

    def preset_config(self):
        '''
        Check for default config file and create if it doesn't exist
        '''

        def get_config_values():

            xml_tree = ET.parse(self.preset_config_xml)
            root = xml_tree.getroot()

            # Get Settings

            for setting in root.iter(self.preset_settings_name):
                self.default_preset = setting.find('default_preset').text

            print('default_preset:', self.default_preset, '\n')

            pyflame_print(self.script_name, 'Preset config loaded.')

        def create_config_file():

            if not os.path.exists(self.preset_path):
                try:
                    os.makedirs(self.preset_path)
                    os.makedirs(self.project_config_path)
                except:
                    FlameMessageWindow('error', f'{self.script_name}: Error', f'Unable to create folder: {self.preset_path}<br>Check folder permissions')

            if not os.path.isfile(self.preset_config_xml):
                pyflame_print(self.script_name, 'Preset config file not found. Creating new preset config file.')

                config = f"""
<settings>
    <{self.preset_settings_name}>
        <default_preset></default_preset>
    </{self.preset_settings_name}>
</settings>"""

                with open(self.preset_config_xml, 'a') as config_file:
                    config_file.write(config)
                    config_file.close()

        if os.path.isfile(self.preset_config_xml):
            get_config_values()
        else:
            create_config_file()
            if os.path.isfile(self.preset_config_xml):
                get_config_values()

    def load_current_preset(self):
        '''
        Set current preset push button text to default preset unless a project preset is set
        '''

        xml_tree = ET.parse(self.preset_config_xml)
        root = xml_tree.getroot()

        # Get Settings

        for setting in root.iter(self.preset_settings_name):
            self.default_preset = setting.find('default_preset').text

        # If default preset is None and no presets exist in preset folder, set current preset to ''

        if not self.default_preset and len(os.listdir(self.preset_path)) == 0:
            return self.current_preset_push_btn.setText('')

        # If default preset is None and one or more presets exists in preset folder, set current preset to first preset and make that preset the default preset

        if not self.default_preset and len(os.listdir(self.preset_path)) > 0:
            preset_file = os.listdir(self.preset_path)[0]
            preset_file_name = self.get_project_preset_name_xml(os.path.join(self.preset_path, preset_file))
            self.update_default_preset_xml(preset_file_name)
            self.default_preset = preset_file_name

        # Check for existing project preset

        try:
            project_preset = [f[:-4] for f in os.listdir(self.project_config_path) if f[:-4] == self.flame_prj_name][0]
        except:
            project_preset = False

        if project_preset:

            # Get current project preset name from project file

            preset_name = self.get_project_preset_name_xml(os.path.join(self.project_config_path, project_preset + '.xml'))

            if preset_name == self.default_preset:
                preset_name = preset_name + '*'

            self.current_preset_push_btn.setText(preset_name)
        else:
            if os.listdir(self.preset_path):
                self.current_preset_push_btn.setText(self.default_preset + '*')
            else:
                self.current_preset_push_btn.setText('')

        if not os.listdir(self.preset_path):
            return print('No saved presets found.')

        # If preset current project is set to is not found, switch to the default preset and delete the project preset

        if not os.path.isfile(os.path.join(self.preset_path, self.get_current_preset_button() + '.xml')):
            FlameMessageWindow('error', f'{self.script_name}: Error', f'Preset file not found: {self.current_preset_push_btn.text()}<br><br>Switching to default preset.')
            self.current_preset_push_btn.setText(self.default_preset + '*')
            os.remove(os.path.join(self.project_config_path, project_preset + '.xml'))

    def build_preset_list(self) -> List[str]:
        '''
        Builds list of presets from preset folder
        '''

        self.preset_config()

        preset_list = []

        for preset in os.listdir(self.preset_path):
            preset = preset[:-4]
            if preset == self.default_preset or len(os.listdir(self.preset_path)) == 1:
                preset = preset + '*'
            preset_list.append(preset)

        preset_list.sort()

        print('preset_list:', preset_list, '\n')

        return preset_list

    def get_current_preset_button(self) -> str:
        '''
        Get current preset button text. Remove '*' if it exists in name.
        '''

        current_preset = self.current_preset_push_btn.text()
        if current_preset.endswith('*'):
            current_preset = current_preset[:-1]

        return current_preset

    def update_current_preset_button(self, preset_name: str=None, preset_is_default: bool=False):
        '''
        Update current preset button text and menu

        preset_name: Preset name that will be shown on Curren Project Preset button. If none is given, first preset in list will be shown.
        preset_is_default: Preset being passed is the default preset. If true, preset will be shown as default preset with an asterisk.
        '''

        preset_list = self.build_preset_list()

        # If preset list is empty, set current preset to empty string and return

        if not preset_list:
            return self.current_preset_push_btn.update_menu('', [])

        # Update Current Project Preset button and menu

        # If preset name is not given, set to first preset in list - for deleting presets
        if not preset_name:
            return self.current_preset_push_btn.update_menu(preset_list[0], preset_list)
        # If preset name returned is cancel, don't update the Current Preset push button
        elif preset_name == 'cancel':
            return
        # If the returned preset name is the same as the default preset add asterisk to the preset name
        elif preset_name == self.default_preset:
            return self.current_preset_push_btn.update_menu(preset_name + '*', preset_list)
        # If only one preset exists in the preset list, that preset is the default. Add asterisk the the name.
        elif preset_name and len(preset_list) == 1:
            return self.current_preset_push_btn.update_menu(preset_name + '*', preset_list)
        elif preset_is_default and not preset_name.endswith('*'):
            return self.current_preset_push_btn.update_menu(preset_name + '*', preset_list)
        return self.current_preset_push_btn.update_menu(preset_name, preset_list)

    def update_default_preset_xml(self, new_default_preset: str):
        '''
        Write new default preset to config file
        '''

        if new_default_preset.endswith('*'):
            new_default_preset = new_default_preset[:-1]

        #print('new_default_preset:', new_default_preset, '\n')

        xml_tree = ET.parse(self.preset_config_xml)
        root = xml_tree.getroot()

        for setting in root.iter(self.preset_settings_name):
            setting.find('default_preset').text = new_default_preset

        xml_tree.write(self.preset_config_xml)

    def save_project_preset_xml(self, preset_path: str, preset_name: str):
        '''
        Update and save project preset xml file with passed preset name
        '''

        # Bypass saving if preset name is 'cancel'. 'cancel' gets passed when the user clicks the cancel button in the setup window.

        if preset_name != 'cancel':

            xml_tree = ET.parse(preset_path)
            root = xml_tree.getroot()

            preset = root.find('.//preset_name')
            preset.text = preset_name

            xml_tree.write(preset_path)

    def create_project_preset_xml(self, preset_name: str, preset_path: str):
            '''
            Create and write new default preset xml file
            '''

            # Create project preset

            preset = f"""
<settings>
    <{self.preset_settings_name}>
        <preset_name></preset_name>
    </{self.preset_settings_name}>
</settings>"""

            with open(preset_path, 'a') as xml_file:
                xml_file.write(preset)
                xml_file.close()

            # Update and save new preset file with current preset name

            self.save_project_preset_xml(preset_path, preset_name)

    def get_project_preset_name_xml(self, project_preset_path: str) -> str:
        '''
        Get name of preset from preset xml
        '''

        script_name = self.script_name.lower().replace(' ', '_')

        # Load settings from project file

        xml_tree = ET.parse(project_preset_path)
        root = xml_tree.getroot()

        # Assign values from config file to variables

        for setting in root.iter(f'{script_name}_preset_settings'):
            preset_name = setting.find('preset_name').text

        return preset_name

    def update_project_presets(self, old_preset_name: str, new_preset_name: str):
        '''
        When changing the name of an existing preset, check all project presets for old preset name. If found, update to new preset name.
        '''

        for project_preset_xml in os.listdir(self.project_config_path):
            project_preset_xml_path = os.path.join(self.project_config_path, project_preset_xml)
            project_preset_name = self.get_project_preset_name_xml(project_preset_xml_path)
            if project_preset_name == old_preset_name:
                self.save_project_preset_xml(project_preset_xml_path, new_preset_name)

        pyflame_print(self.script_name, f'Updated project presets to new preset name: {new_preset_name}')

    # Button actions

    def new_preset(self):
        '''
        Open Setup window with default values.
        Sends string 'new preset' to Setup window.
        Setup window should return preset name as string.
        Setup window cancel button should return 'cancel'.
        Current Project Preset button will be updated with new preset name.
        '''

        pyflame_print(self.script_name, 'Creating new preset.')

        # Hide preset window while creating new preset

        self.preset_window.hide()
        print('preset_window hidden')
        # Load Setup window passing 'new preset' as string

        preset_name = str(self.setup_window('new_preset'))

        # Restore preset window after creating new preset

        self.preset_window.show()
        print('preset_window shown')
        # Refresh current preset button and menu

        self.update_current_preset_button(preset_name)

    def edit_preset(self):
        '''
        Open Setup window with selected preset loaded.
        Sends selected preset xml path to Setup window.
        Setup window should return preset name as string.
        Setup window cancel button should return 'cancel'.
        '''

        # Edit preset returns preset path

        if self.current_preset_push_btn.text():

            preset = self.get_current_preset_button()

            full_preset_path = os.path.join(self.preset_path, preset + '.xml')

            pyflame_print(self.script_name, f'Editing preset: {preset}')

            # Hide preset window while creating new preset

            self.preset_window.hide()

            preset_name = str(self.setup_window(full_preset_path))

            # Restore preset window after creating new preset

            self.preset_window.show()

            # If preset name is changed during edit, update all project presets using preset with new preset name

            if preset != preset_name:
                self.update_project_presets(preset, preset_name)

            self.update_current_preset_button(preset_name)

    def make_default(self):
        '''
        Set current preset as default preset.
        Default preset is shown with an asterisk.
        '''

        if self.current_preset_push_btn.text():

            # Set default preset in preset config xml

            self.update_default_preset_xml(self.current_preset_push_btn.text())

            # Update push button text and list

            self.update_current_preset_button(self.current_preset_push_btn.text(), preset_is_default=True)

            pyflame_print(self.script_name, f'Default preset set to: {self.current_preset_push_btn.text()}')

    def duplicate_preset(self):
        '''
        Create duplicate of currently selected preset. Add copy to end of preset name.
        '''

        if self.current_preset_push_btn.text():

            current_preset = self.get_current_preset_button()

            # Add 'copy' to the end of the new file being created.

            existing_presets = [f[:-4] for f in os.listdir(self.preset_path)]

            new_preset_name = current_preset

            while new_preset_name in existing_presets:
                new_preset_name = new_preset_name  + ' copy'

            # Duplicate preset

            source_file = os.path.join(self.preset_path, current_preset + '.xml')
            dest_file = os.path.join(self.preset_path, new_preset_name + '.xml')
            shutil.copyfile(source_file, dest_file)

            # Save new preset name to duplicate preset xml file

            xml_tree = ET.parse(dest_file)
            root = xml_tree.getroot()

            preset_name = root.find('.//preset_name')
            preset_name.text = new_preset_name

            xml_tree.write(dest_file)

            # Update current preset push button

            self.update_current_preset_button(new_preset_name)

            pyflame_print(self.script_name, f'Preset duplicate created: {new_preset_name}')

    def delete_preset(self):
        '''
        Delete curretly selected preset
        '''

        if self.current_preset_push_btn.text():

            preset_name = self.current_preset_push_btn.text()
            preset_path = os.path.join(self.preset_path, preset_name + '.xml')

            # If selected preset it the default preset, confirm that the user wants to delete it.
            # If confirmed, the default preset is set to the first preset in the list.

            if preset_name.endswith('*'):
                if FlameMessageWindow('warning', f'{self.script_name}: Confirm Operation', 'Selected preset is currently the default preset.<br><br>Deleting this preset will set the default preset to the next preset in the list.<br><br>Are you sure you want to delete this preset?'):

                    # If confirmed, delete preset

                    os.remove(os.path.join(self.preset_path, self.get_current_preset_button() + '.xml'))

                    # Update preset config xml with new default preset

                    if os.listdir(self.preset_path):
                        new_preset = str(os.listdir(self.preset_path)[0])[:-4]
                    else:
                        new_preset = ''
                    print(f'new_preset: {new_preset}')
                    self.update_default_preset_xml(new_preset)

                    # Update current preset push button

                    return self.update_current_preset_button(preset_is_default=True)
                else:
                    return

            # Check all project config files for current preset before deleting.
            # If the preset exists in other project files, delete project files. Confirm first.

            def check_for_project_files():

                preset_names = []

                if os.listdir(self.project_config_path):
                    for n in os.listdir(self.project_config_path):
                        saved_preset_name = self.get_project_preset_name_xml(os.path.join(self.project_config_path, n))
                        preset_names.append(saved_preset_name)

                return preset_names

            # Check for project preset files, if they exitst, get names of presets in project files.

            preset_names = check_for_project_files()

            # If project presets exist, check preset names for preset being deleted.

            if preset_names:

                # If preset exists in other project configs, confirm deletion

                if preset_name in preset_names:
                    if FlameMessageWindow('warning', f'{self.script_name}: Confirm Operation', 'Selected preset is used by other projects. Deleting this preset will delete it for the other projects and set those projects to the Default preset. Continue?'):
                        os.remove(preset_path)
                    else:
                        return
                else:
                    # If preset is not found in any projects, delete. Confirm first.

                    if FlameMessageWindow('warning', f'{self.script_name}: Confirm Operation', f'Delete Preset: <b>{preset_name}'):
                        os.remove(preset_path)
                    else:
                        return

            else:
                # If no project configs exist, delete preset. Confirm first.

                if FlameMessageWindow('warning', f'{self.script_name}: Confirm Operation', f'Delete Preset: <b>{preset_name}'):
                    os.remove(preset_path)
                else:
                    return

            # Update push button text and list
            print('lfkdflkl666')
            self.update_current_preset_button()

            pyflame_print(self.script_name, f'Preset deleted: {preset_name}')

    def set(self):
        '''
        Set current preset as current project preset.
        Creates a new project preset file.
        '''

        if self.current_preset_push_btn.text():

            # Get current preset button name

            preset_name_text = self.get_current_preset_button()

            # Create new preset xml path

            preset_path = os.path.join(self.project_config_path, self.flame_prj_name + '.xml')

            if preset_name_text != self.default_preset:

                # If project preset already exists, delete it before creating new one.

                if os.path.isfile(preset_path):
                    os.remove(preset_path)

                # Create project preset

                self.create_project_preset_xml(preset_name_text, preset_path)

            else:
                try:
                    os.remove(preset_path)
                except:
                    pass

            FlameMessageWindow('message', f'{self.script_name}: Preset Set', f'Uber Save preset set for this project: {preset_name_text}')

    def done(self):
        '''
        Close preset window
        '''

        # Save default preset to default preset xml file

        preset_list = self.build_preset_list()
        for preset in preset_list:
            if preset.endswith('*'):
                self.update_default_preset_xml(preset)

        # Close preset window

        self.preset_window.close()

        pyflame_print(self.script_name, 'Done.')

#

class FlameProgressWindow(QtWidgets.QDialog):
    '''
    Custom Qt Flame Progress Window

    FlameProgressWindow(window_title, num_to_do[, text=None, enable_done_button=False, parent=None])

    window_title: text shown in top left of window ie. Rendering... [str]
    num_to_do: total number of operations to do [int]
    text: message to show in window [str]
    enable_done_button: enable done button, default is False [bool]

    Examples:

        To create window:

            self.progress_window = FlameProgressWindow('Rendering...', 10, text='Rendering: Batch 1 of 5', enable_done_button=True)

        To update progress bar:

            self.progress_window.set_progress_value(number_of_things_done)

        To enable or disable done button - True or False:

            self.progress_window.enable_done_button(True)
    '''

    def __init__(self, window_title: str, num_to_do: int, text: str='', window_bar_color='teal', enable_done_button=False, parent=None):
        super(FlameProgressWindow, self).__init__()

        # Check argument types

        if not isinstance(window_title, str):
            raise TypeError('FlameProgressWindow: window_title must be a string')
        if not isinstance(num_to_do, int):
            raise TypeError('FlameProgressWindow: num_to_do must be an integer')
        if not isinstance(text, str):
            raise TypeError('FlameProgressWindow: text must be a string')
        if not isinstance(enable_done_button, bool):
            raise TypeError('FlameProgressWindow: enable_done_button must be a boolean')
        if window_bar_color not in ['blue', 'red', 'green', 'yellow', 'gray', 'teal']:
           raise ValueError('FlameWindow: Window Bar Color must be one of: blue, red, green, yellow, gray, teal.')

        self.window_bar_color = window_bar_color

        # Build window

        self.setWindowFlags(QtCore.Qt.FramelessWindowHint | QtCore.Qt.WindowStaysOnTopHint)
        self.setMinimumSize(QtCore.QSize(500, 330))
        self.setMaximumSize(QtCore.QSize(500, 330))
        self.setStyleSheet('background-color: rgb(36, 36, 36)')

        primaryScreen = QtWidgets.QApplication.primaryScreen() # resolution = QtWidgets.QDesktopWidget().screenGeometry()
        resolution = primaryScreen.geometry() # Fix for flame 2025
        self.move((resolution.width() / 2) - (self.frameSize().width() / 2),
                  (resolution.height() / 2) - (self.frameSize().height() / 2))

        self.setParent(parent)

        self.grid = QtWidgets.QGridLayout()

        self.main_label = FlameLabel(window_title, label_width=500)
        self.main_label.setStyleSheet('color: rgb(154, 154, 154); font: 18px "Discreet"')

        self.message_text_edit = QtWidgets.QPlainTextEdit('') # Fix for flame 2025
        self.message_text_edit.setDisabled(True)
        self.message_text_edit.setStyleSheet('QPlainTextEdit {color: rgb(154, 154, 154); background-color: rgb(36, 36, 36); selection-color: rgb(190, 190, 190); selection-background-color: rgb(36, 36, 36); border: none; padding-left: 20px; padding-right: 20px; font: 12px "Discreet"}') # Fix for flame 2025
        self.message_text_edit.setText(text)

        # Progress bar

        self.progress_bar = QtWidgets.QProgressBar()
        self.progress_bar.setMaximum(num_to_do)
        self.progress_bar.setMaximumHeight(5)
        self.progress_bar.setTextVisible(False)
        self.progress_bar.setStyleSheet('QProgressBar {color: rgb(154, 154, 154); background-color: rgb(45, 45, 45); font: 14px "Discreet"; border: none}'
                                        'QProgressBar:chunk {background-color: rgb(0, 110, 176)}')

        self.done_button = FlameButton('Done', self.close, button_color='blue', button_width=110)
        self.done_button.setEnabled(enable_done_button)

        # Layout

        self.grid.addWidget(self.main_label, 0, 0)
        self.grid.setRowMinimumHeight(1, 30)
        self.grid.addWidget(self.message_text_edit, 2, 0, 1, 4)
        self.grid.addWidget(self.progress_bar, 8, 0, 1, 7)
        self.grid.setRowMinimumHeight(9, 30)
        self.grid.addWidget(self.done_button, 10, 6)
        self.grid.setRowMinimumHeight(11, 30)

        print(f'\n--> {window_title}\n')

        self.setLayout(self.grid)
        self.show()

    def set_text(self, text):

        self.message_text_edit.setText(text)

    def set_progress_value(self, value):

        self.progress_bar.setValue(value)

    def enable_done_button(self, value):

        if value:
            self.done_button.setEnabled(True)
        else:
            self.done_button.setEnabled(False)

    def paintEvent(self, event):

        painter = QtGui.QPainter(self)
        if self.window_bar_color == 'blue':
            bar_color = QtGui.QColor(0, 110, 176)
        elif self.window_bar_color == 'red':
            bar_color = QtGui.QColor(200, 29, 29)
        elif self.window_bar_color == 'green':
            bar_color = QtGui.QColor(0, 180, 13)
        elif self.window_bar_color == 'yellow':
            bar_color = QtGui.QColor(251, 181, 73)
        elif self.window_bar_color == 'gray':
            bar_color = QtGui.QColor(71, 71, 71)
        elif self.window_bar_color == 'teal':
            bar_color = QtGui.QColor(14, 110, 106)

        painter.setPen(QtGui.QPen(QtGui.QColor(71, 71, 71), .5, QtCore.Qt.SolidLine))
        painter.drawLine(0, 40, 500, 40)
        painter.setPen(QtGui.QPen(bar_color, 6, QtCore.Qt.SolidLine))
        painter.drawLine(0, 0, 0, 330)

    def mousePressEvent(self, event):

        self.oldPosition = event.globalPos()

    def mouseMoveEvent(self, event):

        try:
            delta = QtCore.QPoint(event.globalPos() - self.oldPosition)
            self.move(self.x() + delta.x(), self.y() + delta.y())
            self.oldPosition = event.globalPos()
        except:
            pass

#

class FlamePushButton(QtWidgets.QPushButton):
    '''
    Custom Qt Flame Push Button Widget

    FlamePushButton(button_name, button_checked[, connect=None, button_width=150])

    button_name: text displayed on button [str]
    button_checked: True or False [bool]
    connect: (optional) execute when button is pressed [function]
    button_width: (optional) default is 150. [int]

    Example:

        pushbutton = FlamePushButton('Button Name', False)
    '''

    def __init__(self, button_name: str, button_checked: bool, connect: Optional[Callable[..., None]]=None, button_width: Optional[int]=150):
        super(FlamePushButton, self).__init__()

        # Check argument types

        if not isinstance(button_name, str):
            raise TypeError('FlamePushButton: button_name must be string.')
        if not isinstance(button_checked, bool):
            raise TypeError('FlamePushButton: button_checked must be bool.')
        if not isinstance(button_width, int):
            raise TypeError('FlamePushButton: button_width must be integer.')

        # Build push button

        self.setText(button_name)
        self.setCheckable(True)
        self.setChecked(button_checked)
        self.setMinimumSize(button_width, 28)
        self.setMaximumSize(button_width, 28)
        self.setFocusPolicy(QtCore.Qt.NoFocus)
        self.clicked.connect(connect)
        self.setStyleSheet('QPushButton {color: rgb(154, 154, 154); background-color: qlineargradient(x1: 0, y1: 0, x2: 1, y2: 0, stop: .93 rgb(58, 58, 58), stop: .94 rgb(44, 54, 68)); text-align: left; '
                                        'border-top: qlineargradient(x1: 0, y1: 0, x2: 1, y2: 0, stop: .93 rgb(58, 58, 58), stop: .94 rgb(44, 54, 68)); '
                                        'border-bottom: qlineargradient(x1: 0, y1: 0, x2: 1, y2: 0, stop: .93 rgb(58, 58, 58), stop: .94 rgb(44, 54, 68)); '
                                        'border-left: 1px solid rgb(58, 58, 58); '
                                        'border-right: 1px solid rgb(44, 54, 68); '
                                        'padding-left: 5px; font: 14px "Discreet"}'
                           'QPushButton:checked {color: rgb(217, 217, 217); background-color: qlineargradient(x1: 0, y1: 0, x2: 1, y2: 0, stop: .93 rgb(71, 71, 71), stop: .94 rgb(50, 101, 173)); text-align: left; '
                                        'border-top: qlineargradient(x1: 0, y1: 0, x2: 1, y2: 0, stop: .93 rgb(71, 71, 71), stop: .94 rgb(50, 101, 173)); '
                                        'border-bottom: qlineargradient(x1: 0, y1: 0, x2: 1, y2: 0, stop: .93 rgb(71, 71, 71), stop: .94 rgb(50, 101, 173)); '
                                        'border-left: 1px solid rgb(71, 71, 71); '
                                        'border-right: 1px solid rgb(50, 101, 173); '
                                        'padding-left: 5px; font: italic}'
                           'QPushButton:hover {border: 1px solid rgb(90, 90, 90)}'
                           'QPushButton:disabled {color: #6a6a6a; background-color: qlineargradient(x1: 0, y1: 0, x2: 1, y2: 0, stop: .93 rgb(58, 58, 58), stop: .94 rgb(50, 50, 50)); font: light; border: none}'
                           'QToolTip {color: rgb(170, 170, 170); background-color: rgb(71, 71, 71); border: 10px solid rgb(71, 71, 71)}')

#

class FlamePushButtonMenu(QtWidgets.QPushButton):
    '''
    Custom Qt Flame Menu Push Button Widget

    FlamePushButtonMenu(button_name, menu_options[, menu_width=150, max_menu_width=2000, menu_action=None])

    button_name: text displayed on button [str]
    menu_options: list of options show when button is pressed [list]
    menu_width: (optional) width of widget. default is 150. [int]
    max_menu_width: (optional) set maximum width of widget. default is 2000. [int]
    menu_action: (optional) execute when button is changed. [function]

    To update an existing button menu:

    FlamePushButtonMenu.update_menu(button_name, menu_options[, menu_action=None])

    button_name: text displayed on button [str]
    menu_options: list of options show when button is pressed [list]
    menu_action: (optional) execute when button is changed. [function]

    Examples:

        push_button_menu_options = ['Item 1', 'Item 2', 'Item 3', 'Item 4']
        menu_push_button = FlamePushButtonMenu('push_button_name', push_button_menu_options)

        or

        push_button_menu_options = ['Item 1', 'Item 2', 'Item 3', 'Item 4']
        menu_push_button = FlamePushButtonMenu(push_button_menu_options[0], push_button_menu_options)
    '''

    def __init__(self, button_name: str, menu_options: List[str], menu_width: Optional[int]=150, max_menu_width: Optional[int]=2000, menu_action: Optional[Callable[..., None]]=None):
        super(FlamePushButtonMenu, self).__init__()
        from functools import partial

        # Check argument types

        if not isinstance(button_name, str):
            raise TypeError('FlamePushButtonMenu: button_name must be string.')
        if not isinstance(menu_options, list):
            raise TypeError('FlamePushButtonMenu: menu_options must be list.')
        if not isinstance(menu_width, int):
            raise TypeError('FlamePushButtonMenu: menu_width must be integer.')
        if not isinstance(max_menu_width, int):
            raise TypeError('FlamePushButtonMenu: max_menu_width must be integer.')

        # Build push button menu

        self.setText(button_name)
        self.setMinimumHeight(28)
        self.setMinimumWidth(menu_width)
        self.setMaximumWidth(max_menu_width)
        self.setFocusPolicy(QtCore.Qt.NoFocus)
        self.setStyleSheet('QPushButton {color: rgb(154, 154, 154); background-color: rgb(45, 55, 68); border: none; font: 14px "Discreet"}'
                           'QPushButton:disabled {color: rgb(116, 116, 116); background-color: rgb(45, 55, 68); border: none}'
                           'QPushButton:hover {border: 1px solid rgb(90, 90, 90)}'
                           'QPushButton::menu-indicator {image: none}'
                           'QToolTip {color: rgb(170, 170, 170); background-color: rgb(71, 71, 71); border: 10px solid rgb(71, 71, 71)}')

        self.pushbutton_menu = QtWidgets.QMenu(self)
        self.pushbutton_menu.setFocusPolicy(QtCore.Qt.NoFocus)
        self.pushbutton_menu.setMinimumWidth(menu_width)
        self.pushbutton_menu.setStyleSheet('QMenu {color: rgb(154, 154, 154); background-color: rgb(45, 55, 68); border: none; font: 14px "Discreet"}'
                                           'QMenu::item:selected {color: rgb(217, 217, 217); background-color: rgb(58, 69, 81)}')
        for menu in menu_options:
            self.pushbutton_menu.addAction(menu, partial(self.create_menu, menu, menu_action))

        self.setMenu(self.pushbutton_menu)

    def create_menu(self, menu, menu_action):
        self.setText(menu)
        if menu_action:
            menu_action()

    def update_menu(self, button_name: str, menu_options: List[str], menu_action=None):
        from functools import partial

        self.setText(button_name)

        self.pushbutton_menu.clear()

        for menu in menu_options:
            self.pushbutton_menu.addAction(menu, partial(self.create_menu, menu, menu_action))

#

class FlameQDialog(QtWidgets.QDialog):
    '''
    Custom Qt Flame QDialog Widget

    FlameQDialog(window_title, window_layout, window_width, window_height[, window_bar_color]

    window_title: Text shown top left of window [str]
    window_layout: Layout of window [QtWidgets.QLayout]
    window_width: Width of window [int]
    window_height: Height of window [int]
    window_bar_color: (optional) Color of left window bar (Default is blue) [str]

    Example:

        setup_window = FlameQDialog(f'{SCRIPT_NAME}: Setup <small>{VERSION}', gridbox, 1000, 360)
    '''

    def __init__(self, window_title: str, window_layout, window_width: int, window_height: int, window_bar_color: Optional[str]='blue'):
        super(FlameQDialog, self).__init__()

        # Check argument types

        if not isinstance(window_title, str):
            raise TypeError('FlameQDialog: window_title must be a string.')
        elif not isinstance(window_layout, QtWidgets.QLayout):
            raise TypeError('FlameQDialog: window_layout must be a QtWidgets.QLayout.')
        elif not isinstance(window_width, int):
            raise TypeError('FlameQDialog: window_width must be an integer.')
        elif not isinstance(window_height, int):
            raise TypeError('FlameQDialog: window_height must be an integer.')
        elif not isinstance(window_bar_color, str):
            raise TypeError('FlameQDialog: window_bar_color must be a string.')

        # Build window

        self.window_bar_color = window_bar_color
        self.window_width = window_width
        self.window_height = window_height

        self.setWindowFlags(QtCore.Qt.FramelessWindowHint | QtCore.Qt.WindowStaysOnTopHint)
        self.setMinimumSize(QtCore.QSize(window_width, window_height))
        self.setMaximumSize(QtCore.QSize(window_width, window_height))
        self.setStyleSheet('QWidget {background-color: rgb(36, 36, 36)}'
                           'QTabWidget {background-color: rgb(36, 36, 36); border: none; font: 14px "Discreet"}'
                           'QTabWidget::tab-bar {alignment: center}'
                           'QTabBar::tab {color: rgb(154, 154, 154); background-color: rgb(36, 36, 36); min-width: 20ex; padding: 5px;}'
                           'QTabBar::tab:selected {color: rgb(186, 186, 186); background-color: rgb(31, 31, 31); border: 1px solid rgb(31, 31, 31); border-bottom: 1px solid rgb(51, 102, 173)}'
                           'QTabBar::tab:!selected {color: rgb(186, 186, 186); background-color: rgb(36, 36, 36); border: none}'
                           'QTabWidget::pane {border-top: 1px solid rgb(49, 49, 49)}')

        primaryScreen = QtWidgets.QApplication.primaryScreen() # resolution = QtWidgets.QDesktopWidget().screenGeometry()
        resolution = primaryScreen.geometry() # Fix for flame 2025
        self.move((resolution.width() / 2) - (self.frameSize().width() / 2),
                  (resolution.height() / 2) - (self.frameSize().height() / 2))

        self.window_title_label = FlameLabel(window_title, label_width=window_width)
        self.window_title_label.setStyleSheet('color: rgb(154, 154, 154); font: 18px "Discreet"')

        # Layout

        self.grid = QtWidgets.QGridLayout()
        self.grid.addWidget(self.window_title_label, 0, 0)
        self.grid.addLayout(window_layout, 2, 0, 3, 3)
        self.grid.setRowMinimumHeight(3, 100)

        self.setLayout(self.grid)

    def paintEvent(self, event):
        '''
        Add title bar line and side color lines to window
        '''

        # Line colors

        painter = QtGui.QPainter(self)
        if self.window_bar_color == 'blue':
            bar_color = QtGui.QColor(0, 110, 176)
        elif self.window_bar_color == 'red':
            bar_color = QtGui.QColor(200, 29, 29)
        elif self.window_bar_color == 'green':
            bar_color = QtGui.QColor(0, 180, 13)
        elif self.window_bar_color == 'yellow':
            bar_color = QtGui.QColor(251, 181, 73)
        elif self.window_bar_color == 'gray':
            bar_color = QtGui.QColor(71, 71, 71)

        # Draw lines

        painter.setPen(QtGui.QPen(QtGui.QColor(71, 71, 71), .5, QtCore.Qt.SolidLine))
        painter.drawLine(0, 40, self.window_width, 40)
        painter.setPen(QtGui.QPen(bar_color, 6, QtCore.Qt.SolidLine))
        painter.drawLine(0, 0, 0, self.window_height)

    # For moving frameless window

    def mousePressEvent(self, event):
        self.oldPosition = event.globalPos()

    def mouseMoveEvent(self, event):

        try:
            delta = QtCore.QPoint(event.globalPos() - self.oldPosition)
            self.move(self.x() + delta.x(), self.y() + delta.y())
            self.oldPosition = event.globalPos()
        except:
            pass

#

class FlameSlider(QtWidgets.QLineEdit):
    '''
    Custom Qt Flame Slider Widget

    FlameSlider(start_value, min_value, max_value[, value_is_float=False, slider_width=110])

    start_value: int or float value
    min_value: int or float value
    max_value: int or float value
    value_is_float: (optional) bool value
    slider_width: (optional) default value is 110. [int]

    Usage:

        slider = FlameSlider(0, -20, 20, False)
    '''

    def __init__(self, start_value: int, min_value: int, max_value: int, value_is_float: Optional[bool]=False, slider_width: Optional[int]=110):
        super(FlameSlider, self).__init__()

        # Check argument types

        if not isinstance(start_value, int):
            raise TypeError('FlameSlider: start_value must be integer.')
        if not isinstance(min_value, int):
            raise TypeError('FlameSlider: min_value must be integer.')
        if not isinstance(max_value, int):
            raise TypeError('FlameSlider: max_value must be integer.')
        if not isinstance(value_is_float, bool):
            raise TypeError('FlameSlider: value_is_float must be a boolean.')
        if not isinstance(max_value, int):
            raise TypeError('FlameSlider: slider_width must be integer.')

        # Build slider

        self.setAlignment(QtCore.Qt.AlignCenter)
        self.setMinimumHeight(28)
        self.setMinimumWidth(slider_width)
        self.setMaximumWidth(slider_width)

        if value_is_float:
            self.spinbox_type = 'Float'
        else:
            self.spinbox_type = 'Integer'

        self.min = min_value
        self.max = max_value
        self.steps = 1
        self.value_at_press = None
        self.pos_at_press = None
        self.setValue(start_value)
        self.setReadOnly(True)
        self.textChanged.connect(self.value_changed)
        self.setFocusPolicy(QtCore.Qt.NoFocus)
        self.setStyleSheet('QLineEdit {color: rgb(154, 154, 154); background-color: rgb(55, 65, 75); selection-color: rgb(38, 38, 38); selection-background-color: rgb(184, 177, 167); border: none; padding-left: 5px; font: 14px "Discreet"}'
                           'QLineEdit:hover {border: 1px solid rgb(90, 90, 90)}'
                           'QLineEdit:disabled {color: rgb(106, 106, 106); background-color: rgb(55, 65, 75)}'
                           'QToolTip {color: rgb(170, 170, 170); background-color: rgb(71, 71, 71); border: 10px solid rgb(71, 71, 71)}')
        self.clearFocus()

        class Slider(QtWidgets.QSlider):

            def __init__(self, start_value, min_value, max_value, slider_width):
                super(Slider, self).__init__()

                self.setMaximumHeight(4)
                self.setMinimumWidth(slider_width)
                self.setMaximumWidth(slider_width)
                self.setMinimum(min_value)
                self.setMaximum(max_value)
                self.setValue(start_value)
                self.setOrientation(QtCore.Qt.Horizontal)
                self.setStyleSheet('QSlider {color: rgb(55, 65, 75); background-color: rgb(39, 45, 53)}'
                                   'QSlider::groove {color: rgb(39, 45, 53); background-color: rgb(39, 45, 53)}'
                                   'QSlider::handle:horizontal {background-color: rgb(102, 102, 102); width: 3px}'
                                   'QSlider::disabled {color: rgb(106, 106, 106); background-color: rgb(55, 65, 75)}')
                self.setDisabled(True)
                self.raise_()

        def set_slider():
            slider666.setValue(float(self.text()))

        slider666 = Slider(start_value, min_value, max_value, slider_width)
        self.textChanged.connect(set_slider)

        self.vbox = QtWidgets.QVBoxLayout(self)
        self.vbox.addWidget(slider666)
        self.vbox.setContentsMargins(0, 24, 0, 0)

    def calculator(self):
        from functools import partial

        def clear():
            calc_lineedit.setText('')

        def button_press(key):

            if self.clean_line == True:
                calc_lineedit.setText('')

            calc_lineedit.insert(key)

            self.clean_line = False

        def plus_minus():

            if calc_lineedit.text():
                calc_lineedit.setText(str(float(calc_lineedit.text()) * -1))

        def add_sub(key):

            if calc_lineedit.text() == '':
                calc_lineedit.setText('0')

            if '**' not in calc_lineedit.text():
                try:
                    calc_num = eval(calc_lineedit.text().lstrip('0'))

                    calc_lineedit.setText(str(calc_num))

                    calc_num = float(calc_lineedit.text())

                    if calc_num == 0:
                        calc_num = 1
                    if key == 'add':
                        self.setValue(float(self.text()) + float(calc_num))
                    else:
                        self.setValue(float(self.text()) - float(calc_num))

                    self.clean_line = True
                except:
                    pass

        def enter():

            if self.clean_line == True:
                return calc_window.close()

            if calc_lineedit.text():
                try:

                    # If only single number set slider value to that number

                    self.setValue(float(calc_lineedit.text()))
                except:

                    # Do math

                    new_value = calculate_entry()
                    self.setValue(float(new_value))

            close_calc()

        def equals():

            if calc_lineedit.text() == '':
                calc_lineedit.setText('0')

            if calc_lineedit.text() != '0':

                calc_line = calc_lineedit.text().lstrip('0')
            else:
                calc_line = calc_lineedit.text()

            if '**' not in calc_lineedit.text():
                try:
                    calc = eval(calc_line)
                except:
                    calc = 0

                calc_lineedit.setText(str(calc))
            else:
                calc_lineedit.setText('1')

        def calculate_entry():

            calc_line = calc_lineedit.text().lstrip('0')

            if '**' not in calc_lineedit.text():
                try:
                    if calc_line.startswith('+'):
                        calc = float(self.text()) + eval(calc_line[-1:])
                    elif calc_line.startswith('-'):
                        calc = float(self.text()) - eval(calc_line[-1:])
                    elif calc_line.startswith('*'):
                        calc = float(self.text()) * eval(calc_line[-1:])
                    elif calc_line.startswith('/'):
                        calc = float(self.text()) / eval(calc_line[-1:])
                    else:
                        calc = eval(calc_line)
                except:
                    calc = 0
            else:
                calc = 1

            calc_lineedit.setText(str(float(calc)))

            return calc

        def close_calc():
            calc_window.close()
            self.setStyleSheet('QLineEdit {color: rgb(154, 154, 154); background-color: rgb(55, 65, 75); selection-color: rgb(154, 154, 154); selection-background-color: rgb(55, 65, 75); border: none; padding-left: 5px; font: 14pt "Discreet"}'
                               'QLineEdit:hover {border: 1px solid rgb(90, 90, 90)}')
        def revert_color():
            self.setStyleSheet('QLineEdit {color: rgb(154, 154, 154); background-color: rgb(55, 65, 75); selection-color: rgb(154, 154, 154); selection-background-color: rgb(55, 65, 75); border: none; padding-left: 5px; font: 14pt "Discreet"}'
                               'QLineEdit:hover {border: 1px solid rgb(90, 90, 90)}')
        calc_version = '1.2'
        self.clean_line = False

        calc_window = QtWidgets.QWidget()
        calc_window.setMinimumSize(QtCore.QSize(210, 280))
        calc_window.setMaximumSize(QtCore.QSize(210, 280))
        calc_window.setWindowTitle(f'pyFlame Calc {calc_version}')
        calc_window.setWindowFlags(QtCore.Qt.WindowStaysOnTopHint | QtCore.Qt.Popup)
        calc_window.setAttribute(QtCore.Qt.WA_DeleteOnClose)
        calc_window.destroyed.connect(revert_color)
        calc_window.move(QtGui.QCursor.pos().x() - 110, QtGui.QCursor.pos().y() - 290)
        calc_window.setStyleSheet('background-color: rgb(36, 36, 36)')

        # Labels

        calc_label = QtWidgets.QLabel('Calculator', calc_window)
        calc_label.setAlignment(QtCore.Qt.AlignCenter)
        calc_label.setMinimumHeight(28)
        calc_label.setStyleSheet('color: rgb(154, 154, 154); background-color: rgb(57, 57, 57); font: 14px "Discreet"')

        #  LineEdit

        calc_lineedit = QtWidgets.QLineEdit('', calc_window)
        calc_lineedit.setMinimumHeight(28)
        calc_lineedit.setFocus()
        calc_lineedit.returnPressed.connect(enter)
        calc_lineedit.setStyleSheet('QLineEdit {color: rgb(154, 154, 154); background-color: rgb(55, 65, 75); selection-color: rgb(38, 38, 38); selection-background-color: rgb(184, 177, 167); border: none; padding-left: 5px; font: 14px "Discreet"}')

        # Limit characters that can be entered into lineedit

        regex = QtCore.QRegularExpression('[0-9_,=,/,*,+,\-,.]+') # Fix for flame 2025
        validator = QtGui.QRegularExpressionValidator(regex) # Fix for flame 2025
        calc_lineedit.setValidator(validator)

        # Buttons

        def calc_null():
            # For blank button - this does nothing
            pass

        class FlameButton(QtWidgets.QPushButton):

            def __init__(self, button_name, size_x, size_y, connect, parent, *args, **kwargs):
                super(FlameButton, self).__init__(*args, **kwargs)

                self.setText(button_name)
                self.setParent(parent)
                self.setMinimumSize(size_x, size_y)
                self.setMaximumSize(size_x, size_y)
                self.setFocusPolicy(QtCore.Qt.NoFocus)
                self.clicked.connect(connect)
                self.setStyleSheet('QPushButton {color: rgb(154, 154, 154); background-color: rgb(58, 58, 58); border: none; font: 14px "Discreet"}'
                                   'QPushButton:hover {border: 1px solid rgb(90, 90, 90)}'
                                   'QPushButton:pressed {color: rgb(159, 159, 159); background-color: rgb(66, 66, 66); border: none}'
                                   'QPushButton:disabled {color: rgb(116, 116, 116); background-color: rgb(58, 58, 58); border: none}')

        blank_btn = FlameButton('', 40, 28, calc_null, calc_window)
        blank_btn.setDisabled(True)
        plus_minus_btn = FlameButton('+/-', 40, 28, plus_minus, calc_window)
        plus_minus_btn.setStyleSheet('color: rgb(154, 154, 154); background-color: rgb(45, 55, 68); font: 14px "Discreet"')
        add_btn = FlameButton('Add', 40, 28, (partial(add_sub, 'add')), calc_window)
        sub_btn = FlameButton('Sub', 40, 28, (partial(add_sub, 'sub')), calc_window)

        #  --------------------------------------- #

        clear_btn = FlameButton('C', 40, 28, clear, calc_window)
        equal_btn = FlameButton('=', 40, 28, equals, calc_window)
        div_btn = FlameButton('/', 40, 28, (partial(button_press, '/')), calc_window)
        mult_btn = FlameButton('/', 40, 28, (partial(button_press, '*')), calc_window)

        #  --------------------------------------- #

        _7_btn = FlameButton('7', 40, 28, (partial(button_press, '7')), calc_window)
        _8_btn = FlameButton('8', 40, 28, (partial(button_press, '8')), calc_window)
        _9_btn = FlameButton('9', 40, 28, (partial(button_press, '9')), calc_window)
        minus_btn = FlameButton('-', 40, 28, (partial(button_press, '-')), calc_window)

        #  --------------------------------------- #

        _4_btn = FlameButton('4', 40, 28, (partial(button_press, '4')), calc_window)
        _5_btn = FlameButton('5', 40, 28, (partial(button_press, '5')), calc_window)
        _6_btn = FlameButton('6', 40, 28, (partial(button_press, '6')), calc_window)
        plus_btn = FlameButton('+', 40, 28, (partial(button_press, '+')), calc_window)

        #  --------------------------------------- #

        _1_btn = FlameButton('1', 40, 28, (partial(button_press, '1')), calc_window)
        _2_btn = FlameButton('2', 40, 28, (partial(button_press, '2')), calc_window)
        _3_btn = FlameButton('3', 40, 28, (partial(button_press, '3')), calc_window)
        enter_btn = FlameButton('Enter', 40, 61, enter, calc_window)

        #  --------------------------------------- #

        _0_btn = FlameButton('0', 89, 28, (partial(button_press, '0')), calc_window)
        point_btn = FlameButton('.', 40, 28, (partial(button_press, '.')), calc_window)

        gridbox = QtWidgets.QGridLayout()
        gridbox.setVerticalSpacing(5)
        gridbox.setHorizontalSpacing(5)

        gridbox.addWidget(calc_label, 0, 0, 1, 4)

        gridbox.addWidget(calc_lineedit, 1, 0, 1, 4)

        gridbox.addWidget(blank_btn, 2, 0)
        gridbox.addWidget(plus_minus_btn, 2, 1)
        gridbox.addWidget(add_btn, 2, 2)
        gridbox.addWidget(sub_btn, 2, 3)

        gridbox.addWidget(clear_btn, 3, 0)
        gridbox.addWidget(equal_btn, 3, 1)
        gridbox.addWidget(div_btn, 3, 2)
        gridbox.addWidget(mult_btn, 3, 3)

        gridbox.addWidget(_7_btn, 4, 0)
        gridbox.addWidget(_8_btn, 4, 1)
        gridbox.addWidget(_9_btn, 4, 2)
        gridbox.addWidget(minus_btn, 4, 3)

        gridbox.addWidget(_4_btn, 5, 0)
        gridbox.addWidget(_5_btn, 5, 1)
        gridbox.addWidget(_6_btn, 5, 2)
        gridbox.addWidget(plus_btn, 5, 3)

        gridbox.addWidget(_1_btn, 6, 0)
        gridbox.addWidget(_2_btn, 6, 1)
        gridbox.addWidget(_3_btn, 6, 2)
        gridbox.addWidget(enter_btn, 6, 3, 2, 1)

        gridbox.addWidget(_0_btn, 7, 0, 1, 2)
        gridbox.addWidget(point_btn, 7, 2)

        calc_window.setLayout(gridbox)

        calc_window.show()

    def value_changed(self):

        # If value is greater or less than min/max values set values to min/max

        if int(self.value()) < self.min:
            self.setText(str(self.min))
        if int(self.value()) > self.max:
            self.setText(str(self.max))

    def mousePressEvent(self, event):

        if event.buttons() == QtCore.Qt.LeftButton:
            self.value_at_press = self.value()
            self.pos_at_press = event.pos()
            self.setCursor(QtGui.QCursor(QtCore.Qt.Horizontal)) # Fix for flame 2025
            self.setStyleSheet('QLineEdit {color: rgb(217, 217, 217); background-color: rgb(73, 86, 99); selection-color: rgb(154, 154, 154); selection-background-color: rgb(73, 86, 99); border: none; padding-left: 5px; font: 14pt "Discreet"}'
                               'QLineEdit:hover {border: 1px solid rgb(90, 90, 90)}')

    def mouseReleaseEvent(self, event):

        if event.button() == QtCore.Qt.LeftButton:

            # Open calculator if button is released within 10 pixels of button click

            if event.pos().x() in range((self.pos_at_press.x() - 10), (self.pos_at_press.x() + 10)) and event.pos().y() in range((self.pos_at_press.y() - 10), (self.pos_at_press.y() + 10)):
                self.calculator()
            else:
                self.setStyleSheet('QLineEdit {color: rgb(154, 154, 154); background-color: rgb(55, 65, 75); selection-color: rgb(154, 154, 154); selection-background-color: rgb(55, 65, 75); border: none; padding-left: 5px; font: 14pt "Discreet"}'
                                   'QLineEdit:hover {border: 1px solid rgb(90, 90, 90)}')

            self.value_at_press = None
            self.pos_at_press = None
            self.setCursor(QtGui.QCursor(QtCore.Qt.IBeamCursor))
            return

        super(FlameSlider, self).mouseReleaseEvent(event)

    def mouseMoveEvent(self, event):

        if event.buttons() != QtCore.Qt.LeftButton:
            return

        if self.pos_at_press is None:
            return

        steps_mult = self.getStepsMultiplier(event)
        delta = event.pos().x() - self.pos_at_press.x()

        if self.spinbox_type == 'Integer':
            delta /= 10  # Make movement less sensiteve.
        else:
            delta /= 100
        delta *= self.steps * steps_mult

        value = self.value_at_press + delta
        self.setValue(value)

        super(FlameSlider, self).mouseMoveEvent(event)

    def getStepsMultiplier(self, event):

        steps_mult = 1

        if event.modifiers() == QtCore.Qt.ControlModifier: # Fix for flame 2025
            steps_mult = 10
        elif event.modifiers() == QtCore.Qt.ShiftModifier: # Fix for flame 2025
            steps_mult = 0.10

        return steps_mult

    def setMinimum(self, value):

        self.min = value

    def setMaximum(self, value):

        self.max = value

    def setSteps(self, steps):

        if self.spinbox_type == 'Integer':
            self.steps = max(steps, 1)
        else:
            self.steps = steps

    def value(self):

        if self.spinbox_type == 'Integer':
            return int(self.text())
        else:
            return float(self.text())

    def setValue(self, value):

        if self.min is not None:
            value = max(value, self.min)

        if self.max is not None:
            value = min(value, self.max)

        if self.spinbox_type == 'Integer':
            self.setText(str(int(value)))
        else:
            # Keep float values to two decimal places

            self.setText('%.2f' % float(value))

#

class FlameTextEdit(QtWidgets.QPlainTextEdit): # Fix for flame 2025
    '''
    Custom Qt Flame Text Edit Widget

    FlameTextEdit(text[, read_only=False])

    text: text to be displayed [str]
    read_only: (optional) make text in window read only [bool] - default is False

    Example:

        text_edit = FlameTextEdit('Some important text here', read_only=True)
    '''

    def __init__(self, text: str, read_only: Optional[bool]=False):
        super(FlameTextEdit, self).__init__()

        # Check argument types

        if not isinstance(text, str):
            raise TypeError('FlameTextEdit: text must be a string.')
        if not isinstance(read_only, bool):
            raise TypeError('FlameTextEdit: read_only must be a boolean.')

        # Build text edit

        self.setMinimumHeight(50)
        self.setMinimumWidth(150)
        self.setText(text)
        self.setReadOnly(read_only)
        self.setFocusPolicy(QtCore.Qt.ClickFocus)

        if read_only:
            self.setStyleSheet('QTextEdit {color: rgb(154, 154, 154); background-color: #37414b; selection-color: #262626; selection-background-color: #b8b1a7; border: none; padding-left: 5px; font: 14px "Discreet"}'
                               'QScrollBar {color: 111111; background: rgb(49, 49, 49)}'
                               'QScrollBar::handle {color: 111111; background : 111111;}'
                               'QScrollBar::add-line:vertical {border: none; background: none; width: 0px; height: 0px}'
                               'QScrollBar::sub-line:vertical {border: none; background: none; width: 0px; height: 0px}'
                               'QScrollBar {color: 111111; background: rgb(49, 49, 49)}'
                               'QScrollBar::handle {color: 111111; background : 111111;}'
                               'QScrollBar::add-line:horizontal {border: none; background: none; width: 0px; height: 0px}'
                               'QScrollBar::sub-line:horizontal {border: none; background: none; width: 0px; height: 0px}')
        else:
            self.setStyleSheet('QTextEdit {color: rgb(154, 154, 154); background-color: #37414b; selection-color: #262626; selection-background-color: #b8b1a7; border: none; padding-left: 5px; font: 14px "Discreet"}'
                               'QTextEdit:focus {background-color: #495663}'
                               'QScrollBar {color: 111111; background: rgb(49, 49, 49)}'
                               'QScrollBar::handle {color: 111111; background : 111111;}'
                               'QScrollBar::add-line:vertical {border: none; background: none; width: 0px; height: 0px}'
                               'QScrollBar::sub-line:vertical {border: none; background: none; width: 0px; height: 0px}'
                               'QScrollBar {color: 111111; background: rgb(49, 49, 49)}'
                               'QScrollBar::handle {color: 111111; background : 111111;}'
                               'QScrollBar::add-line:horizontal {border: none; background: none; width: 0px; height: 0px}'
                               'QScrollBar::sub-line:horizontal {border: none; background: none; width: 0px; height: 0px}')

#

class FlameTokenPushButton(QtWidgets.QPushButton):
    '''
    Custom Qt Flame Token Push Button Widget

    FlameTokenPushButton(button_name, token_dict, token_dest[, button_width=150, button_max_width=300])

    button_name: Text displayed on button [str]
    token_dict: Dictionary defining tokens. {'Token Name': '<Token>'} [dict]
    token_dest: QLineEdit that token will be applied to [QtWidgets.QLineEdit]
    button_width: (optional) default is 150 [int]
    button_max_width: (optional) default is 300 [int]

    Example:

        token_dict = {'Token 1': '<Token1>', 'Token2': '<Token2>'}
        token_push_button = FlameTokenPushButton('Add Token', token_dict, token_dest)
    '''

    def __init__(self, button_name: str, token_dict: Dict[str, str], token_dest, button_width: Optional[int]=150, button_max_width:Optional[int]=300):
        super(FlameTokenPushButton, self).__init__()
        from functools import partial

        # Check argument types

        if not isinstance(button_name, str):
            raise TypeError('FlameTokenPushButton: button_name must be a string.')
        if not isinstance(token_dict, dict):
            raise TypeError('FlameTokenPushButton: token_dict must be a dictionary.')
        if not isinstance(token_dest, QtWidgets.QLineEdit):
            raise TypeError('FlameTokenPushButton: token_dest must be a QLineEdit.')
        if not isinstance(button_width, int):
            raise TypeError('FlameTokenPushButton: button_width must be an integer.')
        if not isinstance(button_max_width, int):
            raise TypeError('FlameTokenPushButton: button_max_width must be an integer.')

        # Build token push button

        self.setText(button_name)
        self.setMinimumHeight(28)
        self.setMinimumWidth(button_width)
        self.setMaximumWidth(button_max_width)
        self.setFocusPolicy(QtCore.Qt.NoFocus)
        self.setStyleSheet('QPushButton {color: rgb(154, 154, 154); background-color: rgb(45, 55, 68); border: none; font: 14px "Discreet"}'
                           'QPushButton:hover {border: 1px solid rgb(90, 90, 90)}'
                           'QPushButton:disabled {color: rgb(106, 106, 106); background-color: rgb(45, 55, 68); border: none}'
                           'QPushButton::menu-indicator {subcontrol-origin: padding; subcontrol-position: center right}'
                           'QToolTip {color: rgb(170, 170, 170); background-color: rgb(71, 71, 71); border: 10px solid rgb(71, 71, 71)}')

        def token_action_menu():

            def insert_token(token):
                for key, value in token_dict.items():
                    if key == token:
                        token_name = value
                        token_dest.insert(token_name)

            for key, value in token_dict.items():
                token_menu.addAction(key, partial(insert_token, key))

        token_menu = QtWidgets.QMenu(self)
        token_menu.setFocusPolicy(QtCore.Qt.NoFocus)
        token_menu.setStyleSheet('QMenu {color: rgb(154, 154, 154); background-color: rgb(45, 55, 68); border: none; font: 14px "Discreet"}'
                                 'QMenu::item:selected {color: rgb(217, 217, 217); background-color: rgb(58, 69, 81)}')

        self.setMenu(token_menu)

        token_action_menu()

#

class FlameTreeWidget(QtWidgets.QTreeWidget):
    '''
    Custom Qt Flame Tree Widget

    FlameTreeWidget(tree_headers[, connect=None, tree_min_width=100, tree_min_height=100])

    tree_headers: list of names to be used for column names in tree [list]
    connect: execute when item in tree is clicked on [function]
    tree_min_width = set tree width [int]
    tree_min_height = set tree height [int]

    Exmaple:

        tree_headers = ['Header1', 'Header2', 'Header3', 'Header4']
        tree = FlameTreeWidget(tree_headers)
    '''

    def __init__(self, tree_headers: List[str], connect: Optional[Callable[..., None]]=None, tree_min_width: Optional[int]=100, tree_min_height: Optional[int]=100):
        super(FlameTreeWidget, self).__init__()

        # Check argument types

        if not isinstance(tree_headers, list):
            raise TypeError('FlameTreeWidget: tree_headers must be a list')
        if not isinstance(tree_min_width, int):
            raise TypeError('FlameTreeWidget: tree_min_width must be an integer')
        if not isinstance(tree_min_height, int):
            raise TypeError('FlameTreeWidget: tree_min_height must be an integer')

        # Build tree widget

        self.setMinimumWidth(tree_min_width)
        self.setMinimumHeight(tree_min_height)
        self.setSortingEnabled(True)
        self.sortByColumn(0, QtCore.Qt.SortOrder.AscendingOrder) # Fix for flame 2025
        self.setAlternatingRowColors(True)
        self.setFocusPolicy(QtCore.Qt.NoFocus)
        self.clicked.connect(connect)
        self.setStyleSheet('QTreeWidget {color: rgb(154, 154, 154); background-color: rgb(30, 30, 30); alternate-background-color: rgb(36, 36, 36); border: none; font: 14pt "Discreet"}'
                           'QHeaderView::section {color: rgb(154, 154, 154); background-color: rgb(57, 57, 57); border: none; padding-left: 10px; font: 14pt "Discreet"}'
                           'QTreeWidget:item:selected {color: rgb(217, 217, 217); background-color: rgb(71, 71, 71); selection-background-color: rgb(153, 153, 153); border: 1px solid rgb(17, 17, 17)}'
                           'QTreeWidget:item:selected:active {color: rgb(153, 153, 153); border: none}'
                           'QTreeWidget:disabled {color: rgb(101, 101, 101); background-color: rgb(34, 34, 34)}'
                           'QMenu {color: rgb(154, 154, 154); background-color: rgb(36, 48, 61); font: 14pt "Discreet"}'
                           'QMenu::item:selected {color: rgb(217, 217, 217); background-color: rgb(58, 69, 81)}'
                           'QScrollBar {color: rgb(17, 17, 17); background: rgb(49, 49, 49)}'
                           'QScrollBar::handle {color: rgb(17, 17, 17)}'
                           'QScrollBar::add-line:vertical {border: none; background: none; width: 0px; height: 0px}'
                           'QScrollBar::sub-line:vertical {border: none; background: none; width: 0px; height: 0px}'
                           'QScrollBar {color: rgb(17, 17, 17); background: rgb(49, 49, 49)}'
                           'QScrollBar::handle {color: rgb(17, 17, 17)}'
                           'QScrollBar::add-line:horizontal {border: none; background: none; width: 0px; height: 0px}'
                           'QScrollBar::sub-line:horizontal {border: none; background: none; width: 0px; height: 0px}')

        self.setHeaderLabels(tree_headers)

#

class FlameWindow(QtWidgets.QWidget):
    '''
    Custom Qt Flame Window Widget

    FlameWindow(window_title, window_layout, window_width, window_height[, window_bar_color='blue'])

    window_title: text displayed in top left corner of window [str]
    window_layout: QLayout object. QLayout should be defined before adding FlameWindow [object]
    window_width: width of window [int]
    window_height: height of window [int]
    window_bar_color: (optional) color of bar on left side of window. options are red, blue, green, yellow, gray, teal. [str] - default is blue

    Usage:

        grid_layout = QtWidgets.QGridLayout()
        self.window = FlameWindow(f'Import Camera <small>{VERSION}', grid_layout, 400, 200)
    '''

    def __init__(self, window_title: str, window_layout, window_width: int, window_height: int, window_bar_color: Optional[str]='blue'):
        super(FlameWindow, self).__init__()

        # Check argument types

        if not isinstance(window_title, str):
            raise TypeError('FlameWindow: Window Title must be a string.')
        if not isinstance(window_width, int):
            raise TypeError('FlameWindow: Window Width must be a string.')
        if not isinstance(window_height, int):
            raise TypeError('FlameWindow: Window Width must be a string.')
        if window_bar_color not in ['blue', 'red', 'green', 'yellow', 'gray', 'teal']:
           raise ValueError('FlameWindow: Window Bar Color must be one of: blue, red, green, yellow, gray, teal.')

        # Build window

        self.window_bar_color = window_bar_color

        self.window_width = window_width
        self.window_height = window_height
        self.setMinimumSize(QtCore.QSize(window_width, window_height))
        self.setMaximumSize(QtCore.QSize(window_width, window_height))
        self.setWindowFlags(QtCore.Qt.FramelessWindowHint | QtCore.Qt.WindowStaysOnTopHint)
        self.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.setAttribute(QtCore.Qt.WA_DeleteOnClose)
        self.setStyleSheet('QWidget {background-color: rgb(36, 36, 36)}'
                           'QTabWidget {background-color: rgb(36, 36, 36); border: none; font: 14px "Discreet"}'
                           'QTabWidget::tab-bar {alignment: center}'
                           'QTabBar::tab {color: rgb(154, 154, 154); background-color: rgb(36, 36, 36); min-width: 20ex; padding: 5px;}'
                           'QTabBar::tab:selected {color: rgb(186, 186, 186); background-color: rgb(31, 31, 31); border: 1px solid rgb(31, 31, 31); border-bottom: 1px solid rgb(51, 102, 173)}'
                           'QTabBar::tab:!selected {color: rgb(186, 186, 186); background-color: rgb(36, 36, 36); border: none}'
                           'QTabWidget::pane {border-top: 1px solid rgb(49, 49, 49)}')

        # Center window in linux

        primaryScreen = QtWidgets.QApplication.primaryScreen() # resolution = QtWidgets.QDesktopWidget().screenGeometry()
        resolution = primaryScreen.geometry() # Fix for flame 2025
        self.move((resolution.width() / 2) - (self.frameSize().width() / 2),
                  (resolution.height() / 2) - (self.frameSize().height() / 2))

        self.title_label = FlameLabel(window_title, label_width=window_width)
        self.title_label.setStyleSheet('color: rgb(154, 154, 154); font: 18px "Discreet"')

        # Layout

        self.grid = QtWidgets.QGridLayout()
        self.grid.addWidget(self.title_label, 0, 0)
        self.grid.addLayout(window_layout, 2, 0, 3, 3)
        self.grid.setRowMinimumHeight(3, 100)

        self.setLayout(self.grid)

    def paintEvent(self, event):

        painter = QtGui.QPainter(self)
        if self.window_bar_color == 'blue':
            bar_color = QtGui.QColor(0, 110, 176)
        elif self.window_bar_color == 'red':
            bar_color = QtGui.QColor(200, 29, 29)
        elif self.window_bar_color == 'green':
            bar_color = QtGui.QColor(0, 180, 13)
        elif self.window_bar_color == 'yellow':
            bar_color = QtGui.QColor(251, 181, 73)
        elif self.window_bar_color == 'gray':
            bar_color = QtGui.QColor(71, 71, 71)
        elif self.window_bar_color == 'teal':
            bar_color = QtGui.QColor(14, 110, 106)

        painter.setPen(QtGui.QPen(QtGui.QColor(71, 71, 71), .5, QtCore.Qt.SolidLine))
        painter.drawLine(0, 40, self.window_width, 40)
        painter.setPen(QtGui.QPen(bar_color, 6, QtCore.Qt.SolidLine))
        painter.drawLine(0, 0, 0, self.window_height)

    def mousePressEvent(self, event):

        self.oldPosition = event.globalPos()

    def mouseMoveEvent(self, event):

        try:
            delta = QtCore.QPoint(event.globalPos() - self.oldPosition)
            self.move(self.x() + delta.x(), self.y() + delta.y())
            self.oldPosition = event.globalPos()
        except:
            pass

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
