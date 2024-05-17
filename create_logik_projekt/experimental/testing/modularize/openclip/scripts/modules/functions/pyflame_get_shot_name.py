# filename: pyflame_get_shot_name.py

'''
# -------------------------------------------------------------------------- #

# File Name:        pyflame_get_shot_name.py
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

def pyflame_get_shot_name(shot_name_source) -> str:
        '''
        Extract shot name from PyClipNode object or string.

        shot_name_source: PyClipNode object, or string.

        If a PyClipNode object is passed that has a shot name is assigned 
        to the clip, that will be returned. 
        If no shot name is assigned, the shot name will be extracted from the clip name.
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
