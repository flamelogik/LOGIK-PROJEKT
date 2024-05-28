# filename: pyflame_print.py

'''
# -------------------------------------------------------------------------- #

# File Name:        pyflame_print.py
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

def pyflame_print(
        script_name: str, 
        message: str, 
        message_type: Optional[str]='message', 
        time: Optional[int]=3
    ) -> None:
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
