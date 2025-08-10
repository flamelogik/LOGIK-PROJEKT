
# -------------------------------------------------------------------------- #

# DISCLAIMER:       This file is part of LOGIK-PROJEKT.
#                   Copyright © 2024 Silo 84
   
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
   
#                   Contact: brian@silo84.com
# -------------------------------------------------------------------------- #

# File Name:        init.py
# Version:          0.0.1
# Created:          2024-10-25
# Modified:         2021-11-06

# -------------------------------------------------------------------------- #


import nuke
import os



print("# -------------------------------------------------------------------------- #")


# ========================================================================== #
# This section imports projekt_core
# ========================================================================== #

nuke.pluginAddPath('./repo/projekt_core_v0.0.1',addToSysPath=True)

# -------------------------------------------------------------------------- #
try:
    import projekt_core
    print("projekt_core imported successfully.")
except ImportError as e:
    print(f"Error importing core: {e}")

from projekt_core import settings


# ========================================================================== #
# This section loads the gizmoUtilities module
# ========================================================================== #
#  loading in init.py allows gizmos to be available in render/terminal mode.

try:
    import projekt_core.gizmoUtilities
    print("projekt_core.gizmoUtilities imported successfully.")
except ImportError as e:
    print(f"Error importing gizmoUtilities: {e}")

projekt_core.gizmoUtilities.main()



# ========================================================================== #
# This section adds the repo folder to the plugin path.
# ========================================================================== #
# - to download 3rd party tools run - python ./software/nuke/repo/download_tools.py

# -------------------------------------------------------------------------- #

# read the init.py file in repo folder to load additinoal tools:
nuke.pluginAddPath('./repo')


# ========================================================================== #
# This section defines third party imports.
# ========================================================================== #

# -------------------------------------------------------------------------- #


# ========================================================================== #
# This section defines ofx and plugin imports.
# ========================================================================== #

# -------------------------------------------------------------------------- #


# ========================================================================== #
# This section defines environment variable checking and printing.
# ========================================================================== #

# Function to check and print environment variables
def check_and_print_env_vars(var_names):
    print("# -------------------------------------------------------------------------- #")
    for var_name in var_names:
        var_value = os.environ.get(var_name)

        print(f"{var_name}: {var_value}")
    print("# -------------------------------------------------------------------------- #")

# List of environment variable names
env_vars = [
    "PROJEKT_ROOT",
    "PROJEKT_NAME",
    "PROJEKT_PATH",
    "PROJEKT_OS",
    "PROJEKT_PIPELINE_ROOT",
    "PROJEKT_PIPE_TEMPLATES",

]

# Call the function to check and print environment variables
check_and_print_env_vars(env_vars)

# ========================================================================== #
# 53 54 52 45 4E 47 54 48 2D 49 4E 2D 4E 55 4D 42 45 52 53 C2 A9 32 30 32 35 #
# ========================================================================== #