#

# -------------------------------------------------------------------------- #

# File Name:        pyside6_qt_flame_modules.py
# Version:          1.1.1
# Created:          2024-01-19
# Modified:         2025-11-15

# ========================================================================== #
# Imports - Standard Library
# ========================================================================== #

import ast
import os
import sys

# Ensure the parent directory of 'src' is in sys.path for canonical imports
current_file = os.path.abspath(__file__)
src_parent = os.path.dirname(os.path.dirname(os.path.dirname(current_file)))
if src_parent not in sys.path:
    sys.path.insert(0, src_parent)

# ========================================================================== #
# Imports - Third Party
# ========================================================================== #

try:
    from PySide6 import QtWidgets, QtCore, QtGui
except ImportError:
    from PySide2 import QtWidgets, QtCore, QtGui

# ========================================================================== #
# Imports - LOGIK-PROJEKT UI Classes (Direct from widgets)
# ========================================================================== #

from src.core.ui.widgets.button.pyside6_qt_button import pyside6_qt_button
from src.core.ui.widgets.line_edit.pyside6_qt_clickable_line_edit import pyside6_qt_clickable_line_edit
from src.core.ui.widgets.label.pyside6_qt_label import pyside6_qt_label
from src.core.ui.widgets.line_edit.pyside6_qt_line_edit import pyside6_qt_line_edit
from src.core.ui.widgets.list.pyside6_qt_list_widget import pyside6_qt_list_widget
from src.core.ui.dialog.pyside6_qt_message_window import pyside6_qt_message_window
from src.core.ui.dialog.pyside6_qt_password_window import pyside6_qt_password_window
from src.core.ui.dialog.pyside6_qt_preset_window import pyside6_qt_preset_window
from src.core.ui.dialog.pyside6_qt_progress_window import pyside6_qt_progress_window
from src.core.ui.widgets.button.pyside6_qt_push_button import pyside6_qt_push_button
from src.core.ui.widgets.button.pyside6_qt_push_button_menu import pyside6_qt_push_button_menu
from src.core.ui.dialog.pyside6_qt_qdialog import pyside6_qt_qdialog
from src.core.ui.widgets.slider.pyside6_qt_slider import pyside6_qt_slider
from src.core.ui.widgets.text_edit.pyside6_qt_text_edit import pyside6_qt_text_edit
from src.core.ui.widgets.button.pyside6_qt_token_push_button import pyside6_qt_token_push_button
from src.core.ui.widgets.tree.pyside6_qt_tree_widget import pyside6_qt_tree_widget
from src.core.ui.widgets.window.pyside6_qt_window import pyside6_qt_window

# ========================================================================== #
# Imports - LOGIK-PROJEKT UI Functions (Direct from widgets)
# ========================================================================== #

from src.core.functions.browse.pyside6_qt_file_browser import pyside6_qt_file_browser
from src.core.functions.get.pyside6_qt_get_flame_version import pyside6_qt_get_flame_version
from src.core.functions.get.pyside6_qt_get_shot_name import pyside6_qt_get_shot_name
from src.core.functions.io.pyside6_qt_load_config import pyside6_qt_load_config
from src.core.functions.open.pyside6_qt_open_in_finder import pyside6_qt_open_in_finder
from src.core.functions.print.pyside6_qt_print import pyside6_qt_print
from src.core.functions.refresh.pyside6_qt_refresh_hooks import pyside6_qt_refresh_hooks
from src.core.functions.resolve.pyside6_qt_resolve_path_tokens import pyside6_qt_resolve_path_tokens
from src.core.functions.resolve.pyside6_qt_resolve_shot_name import pyside6_qt_resolve_shot_name
from src.core.functions.io.pyside6_qt_save_config import pyside6_qt_save_config

# ========================================================================== #
# Imports - LOGIK-PROJEKT UI Components
# ========================================================================== #

from src.core.ui.layouts.pyside6_qt_output_config_ui import (
    pyside6_qt_output_config_ui
)


# -------------------------------------------------------------------------- #

# DISCLAIMER:   This file is part of LOGIK-PROJEKT.

#               Copyright © 2025 STRENGTH IN NUMBERS

#               LOGIK-PROJEKT creates directories, files, scripts & tools
#               for use with Autodesk Flame and other software.

#               LOGIK-PROJEKT is free software.

#               You can redistribute it and/or modify it under the terms
#               of the GNU General Public License as published by the
#               Free Software Foundation, either version 3 of the License,
#               or any later version.

#               This program is distributed in the hope that it will be
#               useful, but WITHOUT ANY WARRANTY; without even the

#               implied warranty of MERCHANTABILITY or
#               FITNESS FOR A PARTICULAR PURPOSE.

#               See the GNU General Public License for more details.
#               You should have received a copy of the GNU General
#               Public License along with this program.

#               If not, see <https://www.gnu.org/licenses/gpl-3.0.en.html>.

#               Contact: phil_man@mac.com

# -------------------------------------------------------------------------- #
# C2 A9 32 30 32 35 53 54 52 45 4E 47 54 48 2D 49 4E 2D 4E 55 4D 42 45 52 53 #
# -------------------------------------------------------------------------- #
# Changelog:
# -------------------------------------------------------------------------- #
