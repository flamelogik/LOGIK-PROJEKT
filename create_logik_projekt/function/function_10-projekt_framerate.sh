#!/bin/bash

# -------------------------------------------------------------------------- #

# File Name:        function_10-projekt_framerate.sh
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
# declare -g proj_fcm=""
proj_fcm=""

# -------------------------------------------------------------------------- #

# Function to validate user input
validate_framerate_choice() {
    local choice=$1
    if [[ $choice =~ ^[1-8]$ ]]; then
        return 0  # Valid choice
    else
        echo -e "Invalid input. Please enter a number between 1 and 7."
        echo -e "\n$separator\n"
        return 1  # Invalid choice
    fi
}

# ========================================================================== #
# This section defines the primary functions for the script.
# ========================================================================== #

# Function to gather projekt frame rate information
gather_projekt_framerate() {
    # local proj_fcm

    # Check if $has_projekt_setup_template is true
    if [ "$has_projekt_setup_template" = "True" ]; then
        # Read $projekt_setup_template
        if [ -f "$projekt_setup_template" ]; then
            # Read the value from projekt_setup_template
            proj_fcm=$(sed -n '5s/^.*: //p' "$projekt_setup_template")
        else
            echo "Error: $projekt_setup_template not found."
            exit 1
        fi
    else
        while true; do
            # Display menu for projekt frame rate options
            echo -e "  select projekt frame rate:\n"
            echo -e "  1. 23.976 fps"
            echo -e "  2. 24 fps"
            echo -e "  3. 25 fps"
            echo -e "  4. 29.97 fps"
            echo -e "  5. 30 fps"
            echo -e "  6. 50 fps"
            echo -e "  7. 59.94 fps"
            echo -e "  8. 60 fps\n"
            echo -e "$separator\n"

            # Read user's choice
            read -p "  enter your choice (1 to 8): " choice
            echo -e "\n$separator\n"

            # Validate user's choice
            if validate_framerate_choice "$choice"; then
                break  # Break out of the loop if the choice is valid
            fi
        done

        # ------------------------------------------------------------------ #

        # Handle user's choice
        case $choice in
            1)
                proj_fcm="23.976 fps"
                ;;
            2)
                proj_fcm="24 fps"
                ;;
            3)
                proj_fcm="25 fps"
                ;;
            4)
                proj_fcm="29.97 fps"
                ;;
            5)
                proj_fcm="30 fps"
                ;;
            6)
                proj_fcm="50 fps"
                ;;
            7)
                proj_fcm="59.94 fps"
                ;;
            8)
                proj_fcm="60 fps"
                ;;
        esac
    fi

    # ---------------------------------------------------------------------- #

    # Display the projekt framerate
    echo -e "  frame rate:          $proj_fcm"
    echo -e "\n$separator\n"

    # ---------------------------------------------------------------------- #

    # Write the projekt information into the projekt_setup_file
    echo "projekt framerate: $proj_fcm" >> "$projekt_setup_file"

    # ---------------------------------------------------------------------- #

    # Write the information into the projekt_setup_template
    echo "projekt framerate: $proj_fcm" >> "$projekt_setup_template"

}

# ========================================================================== #
# This section defines how to handle the main script function.
# ========================================================================== #

# Call the function to gather projekt frame rate information
# gather_projekt_framerate

# Check if the script is being sourced or executed
if [[ "${BASH_SOURCE[0]}" == "${0}" ]]; then
    gather_projekt_framerate
fi

# Now the global variables can be accessed wherever needed
# echo -e "  frame rate:       $proj_fcm"

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
