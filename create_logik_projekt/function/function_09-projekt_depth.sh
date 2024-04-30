#!/bin/bash

# -------------------------------------------------------------------------- #

# File Name:        function_09-projekt_depth.sh
# Version:          2.0.1
# Language:         bash script
# Flame Version:    2025.x
# Author:           Phil MAN - phil_man@mac.com
# Toolset:          MAN_MADE_MATERIAL: LOGIK-PROJEKT
# Modified:         2024-04-30
# Modifier:         Phil MAN - phil_man@mac.com

# Description:      This program contains function(s) that are used to
#                   create new logik projekts.

# Installation:     Copy the 'LOGIK-PROJEKT' repo to your GitHub directory,
#                   e.g. '/home/$USER/workspace/GitHub'

# Changelist:       The full changelist is at the end of this document.

# -------------------------------------------------------------------------- #

# ========================================================================== #
# This section defines global variables.
# ========================================================================== #

# Declare global variables
# declare -g proj_color_depth=""
proj_color_depth=""

# -------------------------------------------------------------------------- #

# Function to validate user input for bit depth
validate_depth_choice() {
    local choice=$1
    if [[ $choice =~ ^[1-5]$ ]]; then
        return 0  # Valid choice
    else
        echo -e "  invalid input. enter a number between 1 and 5."
        echo -e "\n$separator\n"
        return 1  # Invalid choice
    fi
}

# ========================================================================== #
# This section defines the primary functions for the script.
# ========================================================================== #

# Function to gather projekt bit depth information
gather_projekt_depth() {
    # local proj_color_depth

    # Check if $has_projekt_setup_template is true
    if [ "$has_projekt_setup_template" = "True" ]; then
        # Read $projekt_setup_template
        if [ -f "$projekt_setup_template" ]; then
            # Read the value from projekt_setup_template
            proj_color_depth=$(sed -n '4s/^.*: //p' "$projekt_setup_template")
        else
            echo "Error: $projekt_setup_template not found."
            exit 1
        fi
    else
        while true; do
            # Prompt user for projekt bit depth
            echo -e "  select projekt bit depth:\n"
            echo -e "  1. 16-bit fp"
            echo -e "  2. 32-bit fp"
            echo -e "  3. 12-bit"
            echo -e "  4. 10-bit"
            echo -e "  5. 8-bit\n"
            echo -e "$separator\n"

            # Read user's depth_choice
            read -p "  enter your choice (1 - 5): " depth_choice
            echo -e "\n$separator\n"

            # Validate user's depth_choice
            if validate_depth_choice "$depth_choice"; then
                break  # Break out of the loop if the choice is valid
            fi
        done

        # Handle user's depth_choice
        case $depth_choice in
            1)
                proj_color_depth="16-bit fp"
                ;;
            2)
                proj_color_depth="32-bit fp"
                ;;
            3)
                proj_color_depth="12-bit"
                ;;
            4)
                proj_color_depth="10-bit"
                ;;
            5)
                proj_color_depth="8-bit"
                ;;
        esac
    fi

    # ---------------------------------------------------------------------- #

    # Display the projekt bit depth
    echo -e "  projekt depth:       $proj_color_depth"
    echo -e "\n$separator\n"

    # ---------------------------------------------------------------------- #

    # Write the projekt information into the projekt_setup_file
    echo "projekt bit-depth: $proj_color_depth" >> "$projekt_setup_file"

    # ---------------------------------------------------------------------- #

    # Write the information into the projekt_setup_template
    echo "projekt bit-depth: $proj_color_depth" >> "$projekt_setup_template"

}

# ========================================================================== #
# This section defines how to handle the main script function.
# ========================================================================== #

# # Call the function to gather projekt depth information
# gather_projekt_depth

# Check if the script is being sourced or executed
if [[ "${BASH_SOURCE[0]}" == "${0}" ]]; then
    gather_projekt_depth
fi

# Now the global variables can be accessed wherever needed
# echo -e "  projekt depth:    $proj_color_depth"

# -------------------------------------------------------------------------- #

# ========================================================================== #
# C2 A9 2D 32 30 32 34 2D 4D 41 4E 5F 4D 41 44 45 5F 4D 41 54 45 52 49 61 4C #
# ========================================================================== #

# Changelist:       
# -------------------------------------------------------------------------- #
# version:               1.0.0
# modified:              2024-04-20 - 16:20:00
# comments:              refactored monolithic program into separate functions
# -------------------------------------------------------------------------- #
# version:               2.0.0
# modified:              2024-04-29 - 11:29:27
# comments:              testing production readiness
# -------------------------------------------------------------------------- #
# version:               2.0.1
# modified:              2024-04-30 - 07:06:00
# comments:              Removed 'declare -g' statements for macOS compatibility
