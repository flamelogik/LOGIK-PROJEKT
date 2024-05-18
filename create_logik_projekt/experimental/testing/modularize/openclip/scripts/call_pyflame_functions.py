# filename: call_pyflame_functions.py

# -------------------------------------------------------------------------- #

# File Name:        call_pyflame_functions.py
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

# Changelist:       The full changelist is at the end of this document.

# -------------------------------------------------------------------------- #

# ========================================================================== #
# This section imports the pyflame functions.
# ========================================================================== #

# # EXAMPLE
# from modules.functions.example import (
#     example_function as new_function_name
# )

from modules.functions.pyflame_get_shot_name import (
    pyflame_get_shot_name as pyflame_get_shot_name
)
from modules.functions.pyflame_print import (
    pyflame_print as pyflame_print
)
from modules.functions.pyflame_get_flame_version import (
    pyflame_get_flame_version as pyflame_get_flame_version
)
from modules.functions.pyflame_file_browser import (
    pyflame_file_browser as pyflame_file_browser
)
from modules.functions.pyflame_resolve_shot_name import (
    pyflame_resolve_shot_name as pyflame_resolve_shot_name
)
from modules.functions.pyflame_resolve_path_tokens import (
    pyflame_resolve_path_tokens as pyflame_resolve_path_tokens
)
from modules.functions.pyflame_refresh_hooks import (
    pyflame_refresh_hooks as pyflame_refresh_hooks
)
from modules.functions.pyflame_open_in_finder import (
    pyflame_open_in_finder as pyflame_open_in_finder
)
from modules.functions.pyflame_load_config import (
    pyflame_load_config as pyflame_load_config
)
from modules.functions.pyflame_save_config import (
    pyflame_save_config as pyflame_save_config
)

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
# modified:              2024-05-07 - 21:48:19
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
