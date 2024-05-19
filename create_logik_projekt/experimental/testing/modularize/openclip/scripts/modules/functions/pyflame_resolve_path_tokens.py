# filename: pyflame_resolve_path_tokens.py

'''
# -------------------------------------------------------------------------- #

# File Name:        pyflame_resolve_path_tokens.py
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

from pyflame_resolve_shot_name import (
    pyflame_resolve_shot_name as pyflame_resolve_shot_name
)

# from pyflame_save_config import (
#     pyflame_save_config as pyflame_save_config
# )

# ========================================================================== #
# This section defines the main function.
# ========================================================================== #

def pyflame_resolve_path_tokens(
    path_to_resolve: str, 
    PyObject=None, 
    date=None
) -> str:
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
