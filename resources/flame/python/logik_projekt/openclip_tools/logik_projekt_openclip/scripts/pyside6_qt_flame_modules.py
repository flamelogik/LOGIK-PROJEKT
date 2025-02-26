#

# -------------------------------------------------------------------------- #

# DISCLAIMER:       This file is part of LOGIK-PROJEKT.
#                   Copyright © 2024 man-made-mekanyzms
                
#                   LOGIK-PROJEKT creates directories, files, scripts & tools
#                   for use with Autodesk Flame and other software.

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
                
#                   Contact: phil_man@mac.com

# -------------------------------------------------------------------------- #

# File Name:        pyside6_qt_flame_modules.py
# Version:          1.0.3
# Created:          2024-01-19
# Modified:         2025-02-25

# ========================================================================== #
# This section imports the necessary modules and adds the modules directory
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
import sys
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

# Get the directory path of the currently executing script
current_script_dir = os.path.dirname(os.path.abspath(__file__))

# Print the current_script_dir
print(f"current_script_dir: {current_script_dir}")

# The current_script_dir should be 'resources/flame/python/logik_projekt/openclip_tools/logik_projekt_openclip/scripts'
# The modules directory should be 'resources/flame/python/logik_projekt/openclip_tools/logik_projekt_openclip/scripts/modules'
# Check if this is true
modules_dir = os.path.join(current_script_dir, 'modules')
print(f"modules_dir: {modules_dir}")

# Append the 'modules' directory to sys.path to access modules
modules_dir = os.path.join(current_script_dir, 'modules')
sys.path.append(modules_dir)

# from pyside6_qt_flame_classes import (
from modules.pyside6_qt_flame_classes import (
# from modules.classes import (
    pyside6_qt_button,
    pyside6_qt_clickable_line_edit,
    pyside6_qt_label,
    pyside6_qt_line_edit,
    pyside6_qt_list_widget,
    pyside6_qt_message_window,
    pyside6_qt_password_window,
    pyside6_qt_preset_window,
    pyside6_qt_progress_window,
    pyside6_qt_push_button,
    pyside6_qt_push_button_menu,
    pyside6_qt_qdialog,
    pyside6_qt_slider,
    pyside6_qt_text_edit,
    pyside6_qt_token_push_button,
    pyside6_qt_tree_widget,
    pyside6_qt_window,
)

# from pyside6_qt_flame_functions import (
from modules.pyside6_qt_flame_functions import (
# from modules.functions import (
    pyside6_qt_get_shot_name,
    pyside6_qt_print,
    pyside6_qt_get_flame_version,
    pyside6_qt_file_browser,
    pyside6_qt_resolve_shot_name,
    pyside6_qt_resolve_path_tokens,
    pyside6_qt_refresh_hooks,
    pyside6_qt_open_in_finder,
    pyside6_qt_load_config,
    pyside6_qt_save_config,
)

# from modules.functions.pyside6_qt_output_config_ui import (
from modules.pyside6_qt_output_config_ui import (
    pyside6_qt_output_config_ui as pyside6_qt_output_config_ui
)

# ============================== TEST ====================================== #

# # Append the 'modules' directory to sys.path to access modules
# if modules_dir not in sys.path:
#     sys.path.append(modules_dir)

# # Verify if the modules directory exists
# if not os.path.exists(modules_dir):
#     print(f"Error: modules_dir does not exist: {modules_dir}")
# else:
#     print(f"modules_dir exists: {modules_dir}")

# # Import modules from the 'modules' directory
# try:
#     from modules.pyside6_qt_flame_classes import (
#         pyside6_qt_button,
#         pyside6_qt_clickable_line_edit,
#         pyside6_qt_label,
#         pyside6_qt_line_edit,
#         pyside6_qt_list_widget,
#         pyside6_qt_message_window,
#         pyside6_qt_password_window,
#         pyside6_qt_preset_window,
#         pyside6_qt_progress_window,
#         pyside6_qt_push_button,
#         pyside6_qt_push_button_menu,
#         pyside6_qt_qdialog,
#         pyside6_qt_slider,
#         pyside6_qt_text_edit,
#         pyside6_qt_token_push_button,
#         pyside6_qt_tree_widget,
#         pyside6_qt_window,
#     )

#     from modules.pyside6_qt_flame_functions import (
#         pyside6_qt_get_shot_name,
#         pyside6_qt_print,
#         pyside6_qt_get_flame_version,
#         pyside6_qt_file_browser,
#         pyside6_qt_resolve_shot_name,
#         pyside6_qt_resolve_path_tokens,
#         pyside6_qt_refresh_hooks,
#         pyside6_qt_open_in_finder,
#         pyside6_qt_load_config,
#         pyside6_qt_save_config,
#     )

#     from modules.pyside6_qt_output_config_ui import (
#         pyside6_qt_output_config_ui as pyside6_qt_output_config_ui
#     )
    
# except ImportError as e:
#     print(f"Error importing modules: {e}")

# ============================== TEST ====================================== #

# ========================================================================== #
# This section defines how to handle the main script function.
# ========================================================================== #

# # If this script is executed as main:
# # Call scripts for immediate execution
# if __name__ == "__main__":

# ========================================================================== #
# C2 A9 32 30 32 34 2D 4D 41 4E 2D 4D 41 44 45 2D 4D 45 4B 41 4E 59 5A 4D 53 #
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
# -------------------------------------------------------------------------- #
# version:               0.0.5
# modified:              2024-05-17 - 13:36:42
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
# modified:              2024-05-17 - 13:38:29
# comments:              Replaced FlameLineEdit with pyside6_qt_line_edit
# -------------------------------------------------------------------------- #
# version:               0.0.9
# modified:              2024-05-17 - 13:39:27
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
# modified:              2024-05-17 - 13:41:49
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
# modified:              2024-05-17 - 13:44:30
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
# modified:              2024-05-17 - 13:49:59
# comments:              Replaced pyflame_refresh_hooks with pyside6_qt_refresh_hooks
# -------------------------------------------------------------------------- #
# version:               0.2.9
# modified:              2024-05-17 - 13:50:10
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
# modified:              2024-05-17 - 15:16:41
# comments:              Replaced pyside6_qt_textedit with pyside6_qt_text_edit
# -------------------------------------------------------------------------- #
# version:               0.3.3
# modified:              2024-05-17 - 15:48:00
# comments:              Replaced pyside6_qt_push_buttonMenu with pyside6_qt_push_button_menu
# -------------------------------------------------------------------------- #
# version:               0.4.3
# modified:              2024-05-18 - 18:00:39
# comments:              Added GNU GPLv3 Disclaimer.
# -------------------------------------------------------------------------- #
# version:               0.4.4
# modified:              2024-05-18 - 18:46:09
# comments:              Minor modification to Disclaimer.
# -------------------------------------------------------------------------- #
# version:               0.4.5
# modified:              2024-06-04 - 17:38:53
# comments:              Added 'Smart Replace' option for render and write nodes
# -------------------------------------------------------------------------- #
# version:               0.4.6
# modified:              2024-06-05 - 19:30:33
# comments:              Added a new script to create openclip multichannel
# -------------------------------------------------------------------------- #
# version:               0.4.7
# modified:              2024-06-05 - 21:08:34
# comments:              Modified note strings
# -------------------------------------------------------------------------- #
# version:               0.4.8
# modified:              2024-06-26 - 22:31:48
# comments:              Fixed missing import statements for pyside6_qt_label
# -------------------------------------------------------------------------- #
# version:               0.4.8
# modified:              2024-07-11 - 08:39:06
# comments:              Added new schematic reels for batch groups
# -------------------------------------------------------------------------- #
# version:               0.4.9
# modified:              2024-07-11 - 08:41:36
# comments:              Fixed a version bug for the changelist updater script
# -------------------------------------------------------------------------- #
# version:               0.5.0
# modified:              2024-08-31 - 18:26:06
# comments:              prep for release.
# -------------------------------------------------------------------------- #
# version:               1.0.0
# modified:              2024-10-30 - 07:35:27
# comments:              Refactored PySide6 Output Node Config UI.
# -------------------------------------------------------------------------- #
# version:               1.0.1
# modified:              2024-11-16 - 16:52:07
# comments:              Fixed circular import statements
# -------------------------------------------------------------------------- #
# version:               1.0.2
# modified:              2025-01-19 - 17:47:49
# comments:              Changed import statements to fix shell errors.
# -------------------------------------------------------------------------- #
# version:               1.0.3
# modified:              2025-02-25 - 07:01:22
# comments:              Added legacy support for PySide2 imports
# -------------------------------------------------------------------------- #
