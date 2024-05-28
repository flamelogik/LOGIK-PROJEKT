import os

# -------------------------------------------------------------------------- #

# File Name:        function_26-add_color_policy.sh
# Version:          2.1.5
# Language:         bash script
# Flame Version:    2025.x
# Author:           Phil MAN - phil_man@mac.com
# Toolset:          MAN_MADE_MATERIAL: LOGIK-PROJEKT
# Modified:         2024-05-18
# Modifier:         Phil MAN - phil_man@mac.com

# Description:      This program contains function(s) that are used to
#                   create new logik projekts.

# Installation:     Copy the 'LOGIK-PROJEKT' repo to your GitHub directory,
#                   e.g. '/home/$USER/workspace/GitHub'

# Changelist:       The full changelist is at the end of this document.

# -------------------------------------------------------------------------- #

# ========================================================================== #
# This section adds a color management policy to the new logik projekt.
# ========================================================================== #

# Function to add the logik projekt synColor policy
def add_syncolor_policy():

    # ---------------------------------------------------------------------- #

    # Set the umask to 0
    os.umask(0)

    # ---------------------------------------------------------------------- #

    # Add the logik projekt synColor policy with wiretap_duplicate_node

    # Add Autodesk colorsync policy to the project node using wiretap
    # /opt/Autodesk/wiretap/tools/current/wiretap_duplicate_node \
    # -s "/syncolor/policies/Autodesk/$proj_color_science" \
    # -n "/projects/$name/syncolor" | sed 's/^/  /'
    # print("\n$separator\n")

    # ---------------------------------------------------------------------- #

    # Add Shared colorsync policy to the project node using wiretap
    print("/opt/Autodesk/wiretap/tools/current/wiretap_duplicate_node "
          "-s \"/syncolor/policies/Shared/$proj_color_science\" "
          "-n \"/projects/$name/syncolor\" | sed 's/^/  /'")
    print("\n$separator\n")

    # ---------------------------------------------------------------------- #

# ========================================================================== #
# This section defines how to handle the main script function.
# ========================================================================== #

# Check if the script is being sourced or executed
if __name__ == "__main__":
    add_syncolor_policy()
