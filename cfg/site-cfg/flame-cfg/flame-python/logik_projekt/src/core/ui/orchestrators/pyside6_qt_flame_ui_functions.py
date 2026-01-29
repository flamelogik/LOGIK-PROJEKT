#

# -------------------------------------------------------------------------- #

# File Name:        pyside6_qt_flame_functions.py
# Version:          1.1.0
# Created:          2024-01-19
# Modified:         2025-11-15

# -------------------------------------------------------------------------- #
# Setup sys.path
# -------------------------------------------------------------------------- #

import os
import sys

# Ensure the parent directory of 'src' is in sys.path for canonical imports
current_file = os.path.abspath(__file__)
src_parent = os.path.dirname(os.path.dirname(os.path.dirname(current_file)))
if src_parent not in sys.path:
    sys.path.insert(0, src_parent)

# -------------------------------------------------------------------------- #
# Imports - Widget Functions
# -------------------------------------------------------------------------- #

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
