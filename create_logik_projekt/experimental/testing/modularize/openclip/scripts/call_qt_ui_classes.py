# filename: call_qt_ui_classes.py

# -------------------------------------------------------------------------- #

# File Name:        call_qt_ui_classes.py
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
# This section imports the Qt UI classes.
# ========================================================================== #

# # EXAMPLE
# from modules.classes.example import (
#     example_function as new_function_name
# )

from modules.classes.FlameButton import (
    FlameButton as FlameButton
)
from modules.classes.FlameClickableLineEdit import (
    FlameClickableLineEdit as FlameClickableLineEdit
)
from modules.classes.FlameLabel import (
    FlameLabel as FlameLabel
)
from modules.classes.FlameLineEdit import (
    FlameLineEdit as FlameLineEdit
)
from modules.classes.FlameListWidget import (
    FlameListWidget as FlameListWidget
)
from modules.classes.FlameMessageWindow import (
    FlameMessageWindow as FlameMessageWindow
)
from modules.classes.FlamePasswordWindow import (
    FlamePasswordWindow as FlamePasswordWindow
)
from modules.classes.FlamePresetWindow import (
    FlamePresetWindow as FlamePresetWindow
)
from modules.classes.FlameProgressWindow import (
    FlameProgressWindow as FlameProgressWindow
)
from modules.classes.FlamePushButton import (
    FlamePushButton as FlamePushButton
)
from modules.classes.FlamePushButtonMenu import (
    FlamePushButtonMenu as FlamePushButtonMenu
)
from modules.classes.FlameQDialog import (
    FlameQDialog as FlameQDialog
)
from modules.classes.FlameSlider import (
    FlameSlider as FlameSlider
)
from modules.classes.FlameTextEdit import (
    FlameTextEdit as FlameTextEdit
)
from modules.classes.FlameTokenPushButton import (
    FlameTokenPushButton as FlameTokenPushButton
)
from modules.classes.FlameTreeWidget import (
    FlameTreeWidget as FlameTreeWidget
)
from modules.classes.FlameWindow import (
    FlameWindow as FlameWindow
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
