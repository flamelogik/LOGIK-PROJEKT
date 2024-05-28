import os

# -------------------------------------------------------------------------- #
'''
# File Name:        function_07-projekt_name.py
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
client = ""
campaign = ""

# ========================================================================== #
# This section defines functions to coerce data.
# ========================================================================== #

# Function to convert uppercase characters to lowercase
def to_lowercase(input_str):
    '''
    Convert uppercase characters to lowercase.
    '''
    return input_str.lower()

# -------------------------------------------------------------------------- #

# Function to sanitize input (letters, numbers, and underscores only)
def sanitize_input(input_str):
    '''
    Sanitize input (letters, numbers, and underscores only).
    '''
    input_str = input_str.lower()
    input_str = ''.join(char if char.isalnum() else '_' for char in input_str)
    input_str = '_'.join(input_str.split('_'))
    input_str = input_str.strip('_')
    if input_str.isalnum() or '_' in input_str:
        return input_str
    else:
        return "error: format must be letters, numbers, or underscores."

# ========================================================================== #
# This section defines the primary functions for the script.
# ========================================================================== #

# Function to gather the client name
def gather_client_name():
    '''
    Gather the client name.
    '''
    global client

    print("  enter the client name for this logik projekt.\n")
    print("  Use letters, numbers, spaces or underscores:\n")
    print("  e.g. Apple, BMW, Chevron, Delta, 23 and Me")
    print("\n$separator\n")
    raw_client = input("  enter client name:   ")
    print("\n$separator\n")
    client = sanitize_input(raw_client)

    # Display client
    print("  client name:         ", client)
    print("\n$separator\n")

    # Write the information into the projekt_setup_file
    with open(projekt_setup_file, 'w') as f:
        f.write(f"client name: {client}\n")

    # Write the information into the projekt_setup_template
    with open(projekt_setup_template, 'w') as f:
        f.write(f"client name: {client}\n")

# -------------------------------------------------------------------------- #

# Function to gather the campaign name
def gather_campaign_name():
    '''
    Gather the campaign name.
    '''
    global campaign

    print("  enter the campaign name for this logik projekt.\n")
    print("  Use letters, numbers, or underscores:\n")
    print("  e.g. iPhone 25, M7, Carwash, Business Class, DNA test 2025")
    print("\n$separator\n")
    raw_campaign = input("  enter campaign name: ")
    print("\n$separator\n")
    campaign = sanitize_input(raw_campaign)

    # Display campaign
    print("  campaign name:       ", campaign)
    print("\n$separator\n")

    # Write the information into the projekt_setup_file
    with open(projekt_setup_file, 'a') as f:
        f.write(f"campaign name: {campaign}\n")

    # Write the information into the projekt_setup_template
    with open(projekt_setup_template, 'a') as f:
        f.write(f"campaign name: {campaign}\n")

# Function to gather projekt name information
def gather_projekt_name():
    '''
    Gather project name information.
    '''
    global client, campaign

    # Check if $has_projekt_setup_template is true
    if has_projekt_setup_template:
        if os.path.isfile(projekt_setup_template):
            with open(projekt_setup_template, 'r') as f:
                lines = f.readlines()
                client = lines[0].split(' ', 2)[2].strip()
                campaign = lines[1].split(' ', 2)[2].strip()
        else:
            print(f"Error: {projekt_setup_template} not found.")
            return 1
    else:
        gather_client_name()
        gather_campaign_name()

# ========================================================================== #
# This section defines how to handle the main script function.
# ========================================================================== #

# # Call the function to gather projekt name information
# gather_projekt_name()

# Check if the script is being sourced or executed
if __name__ == "__main__":
    gather_projekt_name()

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
