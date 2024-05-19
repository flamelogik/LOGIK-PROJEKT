#!/bin/bash

# -------------------------------------------------------------------------- #

# File Name:        function_08-projekt_resolution.sh
# Version:          2.1.4
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
# declare -g proj_res=""
# declare -g proj_res_h=""
# declare -g proj_res_v=""
# declare -g proj_aspect_ratio=""
proj_res=""
proj_res_h=""
proj_res_v=""
proj_aspect_ratio=""

# ========================================================================== #
# This section defines the primary functions for the script.
# ========================================================================== #

# Function to gather projekt resolution information
gather_projekt_resolution() {
    # local proj_res_h
    # local proj_res_v
    # local proj_res
    # local proj_aspect_ratio

    # ---------------------------------------------------------------------- #

    # Check if $has_projekt_setup_template is true
    if [ "$has_projekt_setup_template" = "True" ]; then

        # Read $projekt_setup_template
        if [ -f "$projekt_setup_template" ]; then

            # Read the value from projekt_setup_template
            proj_res=$(sed -n '3p' "$projekt_setup_template" | cut -d ' ' -f3-)

            # Extract proj_res_h and proj_res_v from proj_res
            proj_res_h=$(awk '{print $1}' <<< "$proj_res")
            proj_res_v=$(awk '{print $3}' <<< "$proj_res")

        else

            echo "Error: $projekt_setup_template not found."
            return 1

        fi

    else

        # Set variable defaults
        proj_res_h=1920
        proj_res_v=1080
        proj_res=""
        proj_aspect_ratio=1.77778

        # Display menu for projekt resolution options
        echo -e "  select projekt resolution:\n"
        echo -e "  1. 1920 x 1080 HD"
        echo -e "  2. 3840 x 2160 UHD"
        echo -e "  3. other\n"
        echo -e "\n$separator\n"

        # Read user's resolution_choice
        read -p "  enter your resolution_choice (1, 2, or 3): " resolution_choice
        echo -e "\n$separator\n"

        # Handle user's resolution_choice
        case $resolution_choice in
            1)
                # Option 1: Set resolution to 1920x1080
                proj_res_h=1920
                proj_res_v=1080
                ;;
            2)
                # Option 2: Set resolution to 3840x2160
                proj_res_h=3840
                proj_res_v=2160
                ;;
            3)
                # Option 3: Prompt user for custom resolution with validation
                while true; do
                    read -p "  enter horizontal resolution: " proj_res_h

                    if is_number "$proj_res_h"; then

                        read -p "  enter vertical resolution:   " proj_res_v

                        if is_number "$proj_res_v"; then

                            break

                        else

                            echo "  invalid input. enter a valid resolution."

                        fi

                    else

                        echo "  invalid input. enter a valid resolution."

                    fi

                done
                ;;
            *)

                # invalid resolution_choice, exit with an error
                echo "  invalid resolution_choice. exiting."
                return 1
                ;;

        esac

    fi

    # ---------------------------------------------------------------------- #

    # Calculate proj_aspect_ratio rounded to a maximum of 5 decimal points
    proj_aspect_ratio=$(awk "BEGIN {printf \"%.5f\", $proj_res_h / $proj_res_v}")

    proj_res="$proj_res_h x $proj_res_v"

    # ---------------------------------------------------------------------- #

    # Display the projekt resolution
    echo -e "  resolution:       $proj_res"
    echo -e "  horizontal res:   $proj_res_h"
    echo -e "  vertical res:     $proj_res_v"
    echo -e "  aspect ratio:     $proj_aspect_ratio\n"
    echo -e "\n$separator\n"

    # ---------------------------------------------------------------------- #

    # Write the projekt information into the projekt_setup_file
    echo "projekt resolution: $proj_res" >> "$projekt_setup_file"

    # ---------------------------------------------------------------------- #

    # Write the information into the projekt_setup_template
    echo "projekt resolution: $proj_res" >> "$projekt_setup_template"

}

# ========================================================================== #
# This section defines how to handle the main script function.
# ========================================================================== #

# # Call the function to gather projekt resolution information
# gather_projekt_resolution

# Check if the script is being sourced or executed
if [[ "${BASH_SOURCE[0]}" == "${0}" ]]; then
    gather_projekt_resolution
fi

# Now the global variables can be accessed wherever needed
# echo -e "  resolution:       $proj_res"
# echo -e "  horizontal res:   $proj_res_h"
# echo -e "  vertical res:     $proj_res_v"
# echo -e "  aspect ratio:     $proj_aspect_ratio\n"
# echo -e "\n$separator\n"

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
