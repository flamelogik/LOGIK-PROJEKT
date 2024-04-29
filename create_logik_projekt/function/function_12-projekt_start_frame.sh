#!/bin/bash

# -------------------------------------------------------------------------- #

# File Name:        function_12-projekt_start_frame.sh
# Version:          2.0.0
# Language:         bash script
# Flame Version:    2025.x
# Author:           Phil MAN - phil_man@mac.com
# Toolset:          MAN_MADE_MATERIAL: LOGIK-PROJEKT
# Modified:         2024-04-29
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
declare -g default_start_frame=""

# -------------------------------------------------------------------------- #

# Function to validate user input for framerate
validate_start_frame_choice() {
    local choice=$1
    if [[ $choice =~ ^[1-8]$ ]]; then
        return 0  # Valid choice
    else
        echo -e "Invalid input. Please enter a number between 1 and 8."
        echo -e "\n$separator\n"
        return 1  # Invalid choice
    fi
}

# ========================================================================== #
# This section defines the primary functions for the script.
# ========================================================================== #

# Function to gather projekt framerate information
gather_projekt_start_frame() {
    # local default_start_frame

    # Check if $has_projekt_setup_template is true
    if [ "$has_projekt_setup_template" = "True" ]; then
        # Read $projekt_setup_template
        if [ -f "$projekt_setup_template" ]; then
            # Read the value from projekt_setup_template
            default_start_frame=$(sed -n '7s/^.*: //p' "$projekt_setup_template")
        else
            echo "Error: $projekt_setup_template not found."
            exit 1
        fi
    else
        # Set the default_start_frame
        default_start_frame="1001"

    # ---------------------------------------------------------------------- #

        # Display the projekt start frame
        echo -e "  start frame:         $default_start_frame"
        echo -e "\n$separator\n"

    # ---------------------------------------------------------------------- #

        # Write the projekt information into the projekt_setup_file
        echo "start frame: $default_start_frame" >> "$projekt_setup_file"

    # ---------------------------------------------------------------------- #

        # Write the information into the projekt_setup_template
        echo "start frame: $default_start_frame" >> "$projekt_setup_template"

    fi

    # ---------------------------------------------------------------------- #

    # # Display the projekt start frame
    # echo -e "projekt Start Frame: $default_start_frame"
    # echo -e "\n$separator\n"

}

# ========================================================================== #
# This section defines how to handle the main script function.
# ========================================================================== #

# Call the function to gather projekt framerate information
# gather_projekt_start_frame

# Check if the script is being sourced or executed
if [[ "${BASH_SOURCE[0]}" == "${0}" ]]; then
    gather_projekt_start_frame
fi

# Now the global variables can be accessed wherever needed
# echo -e "  start frame:      $default_start_frame"

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
