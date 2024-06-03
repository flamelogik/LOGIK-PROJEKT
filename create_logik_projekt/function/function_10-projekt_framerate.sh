#!/bin/bash

# -------------------------------------------------------------------------- #

# File Name:        function_10-projekt_framerate.sh
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
# This section defines global variables.
# ========================================================================== #

# Declare global variables
# declare -g proj_fcm=""
proj_fcm=""

# -------------------------------------------------------------------------- #

# Function to validate user input
validate_framerate_choice() {
    local choice=$1
    if [[ $choice =~ ^[1-9]$|^10$ ]]; then
        return 0  # Valid choice
    else
        echo -e "Invalid input. Please enter a number between 1 and 10."
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
            echo -e "  4. 29.97 fps DF"
            echo -e "  5. 29.97 fps NDF"
            echo -e "  6. 30 fps"
            echo -e "  7. 50 fps"
            echo -e "  8. 59.94 fps DF"
            echo -e "  9. 59.94 fps NDF"
            echo -e " 10. 60 fps\n"
            echo -e "$separator\n"

            # Read user's choice
            read -p "  enter your choice (1 to 10): " choice
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
                proj_fcm="29.97 fps DF"
                ;;
            5)
                proj_fcm="29.97 fps NDF"
                ;;
            6)
                proj_fcm="30 fps"
                ;;
            7)
                proj_fcm="50 fps"
                ;;
            8)
                proj_fcm="59.94 fps DF"
                ;;
            9)
                proj_fcm="59.94 fps NDF"
                ;;
            10)
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
# C2 A9 32 30 32 34 2D 4D 41 4E 5F 4D 41 44 45 2D 4D 45 4B 41 4E 49 53 4D 5A #
# ========================================================================== #

# -------------------------------------------------------------------------- #

# Disclaimer:       This program is part of LOGIK-PROJEKT.
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

# -------------------------------------------------------------------------- #
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
# -------------------------------------------------------------------------- #
# version:               2.0.2
# modified:              2024-04-30 - 12:29:07
# comments:              added 'umask 0' statements for rsync commands
# -------------------------------------------------------------------------- #
# version:               2.0.3
# modified:              2024-05-03 - 10:16:09
# comments:              Restored CamelCase keys for projekt_metadata_xml_file
# -------------------------------------------------------------------------- #
# version:               2.0.4
# modified:              2024-05-03 - 10:56:34
# comments:              Restore 'jobs_dir' to /JOBS
# -------------------------------------------------------------------------- #
# version:               2.1.4
# modified:              2024-05-18 - 18:00:11
# comments:              Added GNU GPLv3 Disclaimer.
# -------------------------------------------------------------------------- #
# version:               2.1.5
# modified:              2024-05-18 - 18:45:00
# comments:              Minor modification to Disclaimer.
