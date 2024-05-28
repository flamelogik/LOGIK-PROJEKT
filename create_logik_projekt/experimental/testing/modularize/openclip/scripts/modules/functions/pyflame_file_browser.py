# filename: pyflame_file_browser.py

'''
# -------------------------------------------------------------------------- #

# File Name:        pyflame_file_browser.py
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

from pyflame_get_flame_version import (
    pyflame_get_flame_version as pyflame_get_flame_version
)

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

# from pyflame_print import (
#     pyflame_print as pyflame_print
# )

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

# ============================================================================ #
# This section defines the main function.
# ============================================================================ #

def pyflame_file_browser(
    title: str,
    extension: List[str],
    default_path: str = '/opt/Autodesk',
    select_directory: Optional[bool] = False,
    multi_selection: Optional[bool] = False,
    include_resolution: Optional[bool] = False,
    use_flame_browser: Optional[bool] = True,
    window_to_hide=[]
) -> Union[str, list]:
    '''
    Opens QT file browser window(Flame 2022 - Flame 2023). 
    Flame's file browser is used 2023.1 and later.

    title: File browser window title. [str]

    extension: File extension filter. [''] for directories. [list]

    default_path: Open file browser to this path. [str]

    select_directory: (optional) Ability to select directories. 
        Default False. [bool]

    multi_selection: (optional) Ability to select multiple files/folders.
        Default False. [bool]

    include_resolution: (optional) Enable resolution controls in flame browser.
        Default False. [bool]

    use_flame_browser: (optional) - Use Flame's file browser if using Flame
        2023.1 or later. Default True [bool]

    window_to_hide: (optional) - Hide Qt window while file browser 
    window is open. window is restored when browser is closed. [QWidget]

    When Multi Selection is enabled, the file browser will return a list.
    Otherwise it will return a string.

    Example:

        path = pyflame_file_browser('Load Undistort ST Map(EXR)', 'exr',
        self.undistort_map_path)
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

        flame.browser.show(
            title=title,
            extension=extension,
            default_path=default_path,
            select_directory=select_directory,
            multi_selection=multi_selection,
            include_resolution=include_resolution
        )

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
            browser.setFileMode(
                QtWidgets.QFileDialog.FileMode.Directory
            )  # Fix for flame 2025
        else:
            browser.setFileMode(
                QtWidgets.QFileDialog.FileMode.ExistingFile
            )  # Fix for flame 2025
            browser.setNameFilter(f'*.{extension[0]}')

        if browser.exec_():
            return str(browser.selectedFiles()[0])

        return print('\n--> Import cancelled \n')

# def pyflame_file_browser(title: str, extension: List[str], default_path: str='/opt/Autodesk', select_directory: Optional[bool]=False, multi_selection: Optional[bool]=False, include_resolution: Optional[bool]=False, use_flame_browser: Optional[bool]=True, window_to_hide=[]) -> Union[str, list]:
#     '''
#     Opens QT file browser window(Flame 2022 - Flame 2023). Flame's file browser is used 2023.1 and later.

#     title: File browser window title. [str]
#     extension: File extension filter. [''] for directories. [list]
#     default_path: Open file browser to this path. [str]
#     select_directory: (optional) Ability to select directories. Default False.[bool]
#     multi_selection: (optional) Ability to select multiple files/folders. Default False. [bool]
#     include_resolution: (optional) Enable resolution controls in flame browser. Default False. [bool]
#     use_flame_browser: (optional) - Use Flame's file browser if using Flame 2023.1 or later. Default True [bool]
#     window_to_hide: (optional) - Hide Qt window while file browser window is open. window is restored when browser is closed. [QWidget]

#     When Multi Selection is enabled, the file browser will return a list. Otherwise it will return a string.

#     Example:

#         path = pyflame_file_browser('Load Undistort ST Map(EXR)', 'exr', self.undistort_map_path)
#     '''

#     import flame

#     # Check argument values

#     if not isinstance(extension, list):
#         raise TypeError('Pyflame File Browser: extension must be a list.')
#     if not isinstance(default_path, str):
#         raise TypeError('Pyflame File Browser: default_path must be a string.')
#     if not isinstance(select_directory, bool):
#         raise TypeError('Pyflame File Browser: select_directory must be a boolean.')
#     if not isinstance(multi_selection, bool):
#         raise TypeError('Pyflame File Browser: multi_selection must be a boolean.')
#     if not isinstance(include_resolution, bool):
#         raise TypeError('Pyflame File Browser: include_resolution must be a boolean.')
#     if not isinstance(window_to_hide, list):
#         raise TypeError('Pyflame File Browser: window_to_hide must be a list.')

#     # Clean up path

#     while os.path.isdir(default_path) is not True:
#         default_path = default_path.rsplit('/', 1)[0]
#         if '/' not in default_path and not os.path.isdir(default_path):
#             default_path = '/opt/Autodesk'
#         print('Browser path:', default_path, '\n')

#     # Open file browser

#     if pyflame_get_flame_version() >= 2023.1 and use_flame_browser:

#         # Hide Qt window while browser is open

#         if window_to_hide:
#             for window in window_to_hide:
#                 window.hide()

#         # Open Flame file browser

#         flame.browser.show(title=title, extension=extension, default_path=default_path, select_directory=select_directory, multi_selection=multi_selection, include_resolution=include_resolution)

#         # Restore Qt windows

#         if window_to_hide:
#             for window in window_to_hide:
#                 window.show()

#         # Return file path(s) from Flame file browser

#         if flame.browser.selection:
#             if multi_selection:
#                 return flame.browser.selection
#             return flame.browser.selection[0]
#     else:
#         browser = QtWidgets.QFileDialog()
#         browser.setDirectory(default_path)

#         if select_directory:
#             browser.setFileMode(QtWidgets.QFileDialog.FileMode.Directory) # Fix for flame 2025
#         else:
#             browser.setFileMode(QtWidgets.QFileDialog.FileMode.ExistingFile) # Fix for flame 2025
#             browser.setNameFilter(f'*.{extension[0]}')

#         if browser.exec_():
#             return str(browser.selectedFiles()[0])

#         return print('\n--> Import cancelled \n')

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
