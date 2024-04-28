#!/bin/bash

# -------------------------------------------------------------------------- #

# filename: "function_26-add_color_policy.sh"

# -------------------------------------------------------------------------- #

# ========================================================================== #
# This section adds a color management policy to the new logik projekt.
# ========================================================================== #

# Function to add the logik projekt synColor policy
add_syncolor_policy() {

    # ---------------------------------------------------------------------- #

    # Set the umask to 0
    umask 0

    # ---------------------------------------------------------------------- #

    # Add the logik projekt synColor policy with wiretap_duplicate_node

    # Add Autodesk colorsync policy to the project node using wiretap
    # /opt/Autodesk/wiretap/tools/current/wiretap_duplicate_node \
    # -s "/syncolor/policies/Autodesk/$proj_color_science" \
    # -n "/projects/$name/syncolor" | sed 's/^/  /'
    # echo -e "\n$separator\n"

    # ---------------------------------------------------------------------- #

    # Add Shared colorsync policy to the project node using wiretap
    /opt/Autodesk/wiretap/tools/current/wiretap_duplicate_node \
    -s "/syncolor/policies/Shared/$proj_color_science" \
    -n "/projects/$name/syncolor" \
    | sed 's/^/  /'
    echo -e "\n$separator\n"

    # ---------------------------------------------------------------------- #

}

# ========================================================================== #
# This section defines how to handle the main script function.
# ========================================================================== #

# # Call the function
# add_syncolor_policy

# Check if the script is being sourced or executed
if [[ "${BASH_SOURCE[0]}" == "${0}" ]]; then
    add_syncolor_policy
fi

# -------------------------------------------------------------------------- #

# ========================================================================== #
# C2 A9 2D 32 30 32 34 2D 4D 41 4E 5F 4D 41 44 45 5F 4D 41 54 45 52 49 61 4C #
# ========================================================================== #
