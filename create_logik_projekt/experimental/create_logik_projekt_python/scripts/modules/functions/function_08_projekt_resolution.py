import os

# -------------------------------------------------------------------------- #
'''
# File Name:        function_08-projekt_resolution.py
# Version:          2.1.5
# Language:         Python script
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
'''
# -------------------------------------------------------------------------- #

# ========================================================================== #
# This section defines global variables.
# ========================================================================== #

# Declare global variables
proj_res = ""
proj_res_h = ""
proj_res_v = ""
proj_aspect_ratio = ""

# ========================================================================== #
# This section defines the primary functions for the script.
# ========================================================================== #

# Function to gather projekt resolution information
def gather_projekt_resolution():
    '''
    Gather project resolution information.
    '''
    global proj_res, proj_res_h, proj_res_v, proj_aspect_ratio

    # Check if $has_projekt_setup_template is true
    if has_projekt_setup_template:

        # Read $projekt_setup_template
        if os.path.isfile(projekt_setup_template):

            # Read the value from projekt_setup_template
            with open(projekt_setup_template, 'r') as f:
                lines = f.readlines()
                proj_res = lines[2].split(' ', 2)[2].strip()

            # Extract proj_res_h and proj_res_v from proj_res
            proj_res_h, _, proj_res_v = proj_res.partition('x')

        else:
            print(f"Error: {projekt_setup_template} not found.")
            return 1

    else:

        # Set variable defaults
        proj_res_h = 1920
        proj_res_v = 1080
        proj_res = ""
        proj_aspect_ratio = 1.77778

        # Display menu for project resolution options
        print("  select project resolution:\n")
        print("  1. 1920 x 1080 HD")
        print("  2. 3840 x 2160 UHD")
        print("  3. other\n")
        print("\n$separator\n")

        # Read user's resolution_choice
        resolution_choice = input("  enter your resolution_choice (1, 2, or 3): ")
        print("\n$separator\n")

        # Handle user's resolution_choice
        if resolution_choice == "1":
            # Option 1: Set resolution to 1920x1080
            proj_res_h = 1920
            proj_res_v = 1080
        elif resolution_choice == "2":
            # Option 2: Set resolution to 3840x2160
            proj_res_h = 3840
            proj_res_v = 2160
        elif resolution_choice == "3":
            # Option 3: Prompt user for custom resolution with validation
            while True:
                proj_res_h = input("  enter horizontal resolution: ")
                if proj_res_h.isdigit():
                    proj_res_v = input("  enter vertical resolution: ")
                    if proj_res_v.isdigit():
                        break
                    else:
                        print("  invalid input. enter a valid resolution.")
                else:
                    print("  invalid input. enter a valid resolution.")
        else:
            # invalid resolution_choice, exit with an error
            print("  invalid resolution_choice. exiting.")
            return 1

    # Calculate proj_aspect_ratio rounded to a maximum of 5 decimal points
    proj_aspect_ratio = round(float(proj_res_h) / float(proj_res_v), 5)

    proj_res = f"{proj_res_h} x {proj_res_v}"

    # Display the project resolution
    print("  resolution:       ", proj_res)
    print("  horizontal res:   ", proj_res_h)
    print("  vertical res:     ", proj_res_v)
    print("  aspect ratio:     ", proj_aspect_ratio)
    print("\n$separator\n")

    # Write the project information into the projekt_setup_file
    with open(projekt_setup_file, 'a') as f:
        f.write(f"projekt resolution: {proj_res}\n")

    # Write the information into the projekt_setup_template
    with open(projekt_setup_template, 'a') as f:
        f.write(f"projekt resolution: {proj_res}\n")

# ========================================================================== #
# This section defines how to handle the main script function.
# ========================================================================== #

# Check if the script is being sourced or executed
if __name__ == "__main__":
    gather_projekt_resolution()

# -------------------------------------------------------------------------- #

# ========================================================================== #
# C2 A9 32 30 32 34 2D 4D 41 4E 5F 4D 41 44 45 2D 4D 45 4B 41 4E 49 53 4D 5A #
# ========================================================================== #

# -------------------------------------------------------------------------- #
'''
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
'''
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
