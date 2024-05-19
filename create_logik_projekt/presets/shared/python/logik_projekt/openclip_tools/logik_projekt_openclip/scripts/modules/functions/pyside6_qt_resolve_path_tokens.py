# filename: pyside6_qt_resolve_path_tokens.py

'''
# -------------------------------------------------------------------------- #

# File Name:        pyside6_qt_resolve_path_tokens.py
# Version:          0.4.3
# Language:         python script
# Flame Version:    2025.x
# Author:           Phil MAN - phil_man@mac.com
# Toolset:          MAN_MADE_MATERIAL: LOGIK-PROJEKT
# Created:          2024-04-20
# Modified:         2024-05-18
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

# from pyside6_qt_print import (
#     pyside6_qt_print as pyside6_qt_print
# )

# from pyside6_qt_refresh_hooks import (
#     pyside6_qt_refresh_hooks as pyside6_qt_refresh_hooks
# )

# from pyside6_qt_resolve_path_tokens import (
#     pyside6_qt_resolve_path_tokens as pyside6_qt_resolve_path_tokens
# )

from pyside6_qt_resolve_shot_name import (
    pyside6_qt_resolve_shot_name as pyside6_qt_resolve_shot_name
)

# from pyside6_qt_save_config import (
#     pyside6_qt_save_config as pyside6_qt_save_config
# )

# ========================================================================== #
# This section defines the main function.
# ========================================================================== #

def pyside6_qt_resolve_path_tokens(
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
                    shot_name = pyside6_qt_resolve_shot_name(clip_name)
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
                    shot_name = pyside6_qt_resolve_shot_name(segment_name)
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
                shot_name = pyside6_qt_resolve_shot_name(str(batch.name)[1:-1])

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
# C2 A9 32 30 32 34 2D 4D 41 4E 5F 4D 41 44 45 2D 4D 45 4B 41 4E 49 53 4D 5A #
# ========================================================================== #

# -------------------------------------------------------------------------- #

# Disclaimer:       This program is part of LOGIK-PROJEKT.
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

# -------------------------------------------------------------------------- #
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
# modified:              2024-05-17 - 13:36:43
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
# modified:              2024-05-17 - 13:38:30
# comments:              Replaced FlameLineEdit with pyside6_qt_line_edit
# -------------------------------------------------------------------------- #
# version:               0.0.9
# modified:              2024-05-17 - 13:39:28
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
# modified:              2024-05-17 - 13:41:50
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
# modified:              2024-05-17 - 13:44:31
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
# modified:              2024-05-17 - 13:50:11
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
# modified:              2024-05-17 - 15:16:42
# comments:              Replaced pyside6_qt_textedit with pyside6_qt_text_edit
# -------------------------------------------------------------------------- #
# version:               0.3.3
# modified:              2024-05-17 - 15:48:01
# comments:              Replaced pyside6_qt_push_buttonMenu with pyside6_qt_push_button_menu
# -------------------------------------------------------------------------- #
# version:               0.4.3
# modified:              2024-05-18 - 18:00:39
# comments:              Added GNU GPLv3 Disclaimer.
