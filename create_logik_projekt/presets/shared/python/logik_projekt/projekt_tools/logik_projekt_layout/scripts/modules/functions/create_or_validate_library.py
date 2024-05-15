# File Name:        create_or_validate_library.py

# -------------------------------------------------------------------------- #

# File Name:        create_or_validate_library.py
# Version:          0.2.0
# Language:         python script
# Flame Version:    2025.x
# Author:           Phil MAN - phil_man@mac.com
# Toolset:          MAN_MADE_MATERIAL: LOGIK-PROJEKT
# Created:          2024-04-20
# Modified:         2024-05-14
# Modifier:         Phil MAN - phil_man@mac.com

# Description:      This python script is part of a program that creates 
#                   logik projekt flame layouts.

# Installation:     Copy the 'LOGIK-PROJEKT' directory to:
#                   '/opt/Autodesk/shared/python/'

# Changelist:       The full changelist is at the end of this document.

# -------------------------------------------------------------------------- #

# ========================================================================== #
# This section imports the necessary modules.
# ========================================================================== #

import flame
import datetime

# ========================================================================== #
# This section defines some variables based on the date.
# ========================================================================== #

# Get today's date and time
today_date = datetime.date.today().strftime("%Y-%m-%d")
today_time = datetime.datetime.now().strftime("%H-%M-%S")

# ========================================================================== #
# This section defines a function to create or validate flame libraries.
# ========================================================================== #

# Function to create or validate library objects.
def create_or_validate_library(
        workspace,
        library_name,
        object_color=None
        ):

    # ---------------------------------------------------------------------- #

    # Check if the library exists in the workspace
    for library in workspace.libraries:

        if library.name == library_name:

            print(
                f"Library '{library_name}' already exists in workspace "
                f"'{workspace.name}'."
                )

            return library

    # ---------------------------------------------------------------------- #

    # If the library doesn't exist, create it.
    new_library = workspace.create_library(
        name=library_name
        )

    if object_color:
        new_library.colour = object_color
    print(
        f"New library '{library_name}' created successfully in workspace "
        f"'{workspace.name}'."
        )

    return new_library

# ========================================================================== #
# C2 A9 2D 32 30 32 34 2D 4D 41 4E 5F 4D 41 44 45 5F 4D 41 54 45 52 49 61 4C #
# ========================================================================== #

# Changelist:  
# -------------------------------------------------------------------------- #
# version:               0.0.1
# modified:              2024-05-03 - 01:53:36
# comments:              Basic functionality defined and tested
# -------------------------------------------------------------------------- #
# version:               0.0.2
# modified:              2024-05-03 - 02:13:01
# comments:              Fixed some formatting and flame menus
# -------------------------------------------------------------------------- #
# version:               0.0.3
# modified:              2024-05-03 - 11:26:02
# comments:              Changed 'the_current_project' to 'the_current_projekt'
# -------------------------------------------------------------------------- #
# version:               0.0.4
# modified:              2024-05-03 - 11:38:53
# comments:              Standardized 'logik-projekt' menu entries
# -------------------------------------------------------------------------- #
# version:               0.0.5
# modified:              2024-05-12 - 15:37:50
# comments:              Added function to read directories from JSON files.
# -------------------------------------------------------------------------- #
# version:               0.0.6
# modified:              2024-05-12 - 18:16:05
# comments:              Added a 'separators' function and tested in flame 2025.
# -------------------------------------------------------------------------- #
# version:               0.0.7
# modified:              2024-05-14 - 16:30:58
# comments:              Minor reformatting.
# -------------------------------------------------------------------------- #
# version:               0.0.8
# modified:              2024-05-14 - 16:31:23
# comments:              Changed object_colors from python to JSON.
# -------------------------------------------------------------------------- #
# version:               0.0.9
# modified:              2024-05-14 - 16:31:47
# comments:              Tested in flame 2025.
# -------------------------------------------------------------------------- #
# version:               0.1.0
# modified:              2024-05-14 - 16:46:55
# comments:              Production tested in flame 2025.
# -------------------------------------------------------------------------- #
# version:               0.2.0
# modified:              2024-05-14 - 18:05:26
# comments:              Prepped for obsolete code removal. Tested in flame 2025
