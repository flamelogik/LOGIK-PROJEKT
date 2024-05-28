#!/usr/bin/env python3

# -------------------------------------------------------------------------- #
# File Name:        function_06-adsk_info.py
# Version:          2.1.5
# Language:         Python 3
# Flame Version:    2025.x
# Author:           Phil MAN - phil_man@mac.com
# Toolset:          MAN_MADE_MATERIAL: LOGIK-PROJEKT
# Modified:         2024-05-18
# Modifier:         Phil MAN - phil_man@mac.com
#
# Description:      This program contains function(s) that are used to
#                   create new logik projekts.
#
# Installation:     Copy the 'LOGIK-PROJEKT' repo to your GitHub directory,
#                   e.g. '/home/$USER/workspace/GitHub'
#
# Changelist:       The full changelist is at the end of this document.
# -------------------------------------------------------------------------- #

# ========================================================================== #
# This section defines global variables.
# ========================================================================== #

# Define dir_names as a global list
dir_names = []

# Define adsk_dir
adsk_dir = "/opt/Autodesk"

# ========================================================================== #
# This section initializes miscellaneous variables.
# ========================================================================== #

# Define function to initialize variables
def initialize_adsk_variables():
    '''
    Initialize miscellaneous variables related to Autodesk.
    '''
    global sorted_dir_names, max_dir_val, max_dir_name, max_dir_ver
    global max_sw_val, max_sw_ver, max_sanitized_sw_ver, beta_sw
    
    sorted_dir_names = []
    max_dir_val = "0000000000000000"
    max_dir_name = ""
    max_dir_ver = ""
    max_sw_val = ""
    max_sw_ver = ""
    max_sanitized_sw_ver = ""
    beta_sw = False

# ========================================================================== #
# This section defines how to handle release or beta sw installations.
# ========================================================================== #

# Define function for processing beta_sw condition
def process_beta_sw():
    '''
    Process beta software installations.
    '''
    global max_sw_val

    if beta_sw:
        app_maj = app_ver_long_parts[0]
        app_min = "00"
        app_dot = "00"
        app_dot_dot = "00"
        app_pr_ver = ""
        app_pr_dot_ver = ""

        for i, part in enumerate(app_ver_long_parts[1:4]):
            if "pr" in part:
                if i == 0:
                    app_min = "00"
                elif i == 1:
                    app_dot = "00"
                elif i == 2:
                    app_dot_dot = "00"
                app_pr_ver = part
                break
            else:
                if i == 0:
                    app_min = "{:02d}".format(int(part))
                elif i == 1:
                    app_dot = "{:02d}".format(int(part))
                elif i == 2:
                    app_dot_dot = "{:02d}".format(int(part))

        if "pr" in app_ver_long_parts[-1]:
            app_pr_dot_ver = "00"
        else:
            app_pr_dot_ver = "{:02d}".format(int(app_ver_long_parts[-1]))

        app_pr_val = app_pr_ver.replace("pr", "")

        calc_app_ver = "{}.{}.{}.{}".format(app_maj, app_min, app_dot, app_dot_dot)
        calc_app_ver_pr = "{}.{}".format(calc_app_ver, app_pr_ver)
        calc_app_val_1 = "{}{}{}{}{}".format(app_maj, app_min, app_dot, app_dot_dot, app_val)
        calc_app_val_2 = "{}{}".format(app_pr_val, app_pr_dot_ver)
        calc_app_val = "{}{}".format(calc_app_val_1, calc_app_val_2)

        if not max_sw_val or int(calc_app_val) > int(max_sw_val):
            max_sw_val = calc_app_val

# Define function for processing release_sw condition
def process_release_sw():
    '''
    Process release software installations.
    '''
    global max_sw_val

    if release_sw:
        app_maj = app_ver_long_parts[0]
        app_min = "{:02d}".format(int(app_ver_long_parts[1])) if app_ver_long_parts[1] else "00"
        app_dot = "{:02d}".format(int(app_ver_long_parts[2])) if app_ver_long_parts[2] else "00"
        app_dot_dot = "{:02d}".format(int(app_ver_long_parts[3])) if app_ver_long_parts[3] else "00"
        app_pr_ver = "pr999"
        app_pr_dot_ver = "99"

        app_pr_val = app_pr_ver.replace("pr", "")

        calc_app_ver = "{}.{}.{}.{}".format(app_maj, app_min, app_dot, app_dot_dot)
        calc_app_ver_pr = "{}.{}".format(calc_app_ver, app_pr_ver)
        calc_app_val_1 = "{}{}{}{}{}".format(app_maj, app_min, app_dot, app_dot_dot, app_val)
        calc_app_val_2 = "{}{}".format(app_pr_val, app_pr_dot_ver)
        calc_app_val = "{}{}".format(calc_app_val_1, calc_app_val_2)

        if not max_sw_val or int(calc_app_val) > int(max_sw_val):
            max_sw_val = calc_app_val

# ========================================================================== #
# This section defines the primary functions for the script.
# ========================================================================== #

# Define function to check '/opt/Autodesk' for flame family software.
def check_adsk_installations():
    '''
    Check '/opt/Autodesk' for flame family software installations.
    '''
    global dir_names

    # Check if the directory exists
    if not os.path.isdir(adsk_dir):
        print(f"\n{'+' * 78}\n")
        print(f"  '{adsk_dir}' does not exist.\n")
        print(f"{'+' * 78}\n")
        return False

    # Get directory names matching multiple patterns
    dir_names = [dir_entry for dir_entry in os.listdir(adsk_dir) if any(pattern in dir_entry for pattern in ["fla", "lustre", "projectserver", "smoke"])]

    # Validate if dir_names is not empty
    if not dir_names:
        print(f"\n{'+' * 78}\n")
        print(f"  No directories found in {adsk_dir} starting with 'fla'.\n")
        print(f"{'+' * 78}\n")
        return False

    # Output the directory names
    print("  The following installations have been found on this system:\n")
    for dir_name in dir_names:
        print(f"                    {dir_name}")
    print(f"\n{'+' * 78}\n")
    return True

# Define function to display information derived from flame family software
def display_software_information(dir_name, dir_basename, app_name, app_val, beta_sw, release_sw, app_ver_long, count_app_ver_long_parts, app_maj, app_min, app_dot, app_dot_dot, app_pr_ver, app_pr_dot_ver, app_pr_val, calc_app_ver, sanitized_app_ver, calc_app_ver_pr, sanitized_app_ver_pr, calc_app_val_1, calc_app_val_2, calc_app_val, max_sw_val):
    '''
    Display information derived from flame family software.
    '''
    print(f"  Directory:           {dir_name}\n")
    print(f"  Base name:           {dir_basename}\n")
    print(f"  App name:            {app_name}")
    print(f"  App val:             {app_val}")
    print(f"  Beta:                {beta_sw}")
    print(f"  Release:             {release_sw}\n")
    print(f"  App ver long:        {app_ver_long}")
    print(f"  Count parts:         {count_app_ver_long_parts}\n")
    print(f"  App maj:             {app_maj}")
    print(f"  App min:             {app_min}")
    print(f"  App dot:             {app_dot}")
    print(f"  App dot dot:         {app_dot_dot}\n")
    print(f"  App pr ver:          {app_pr_ver}")
    print(f"  App pr dot ver:      {app_pr_dot_ver}")
    print(f"  App pr val:          {app_pr_val}\n")
    print(f"  Calc app ver:        {calc_app_ver}")
    print(f"  Sanitized ver:       {sanitized_app_ver}\n")
    print(f"  Calc app ver pr:     {calc_app_ver_pr}")
    print(f"  Sanitized ver pr:    {sanitized_app_ver_pr}")
    print(f"  Calc app 1:          {calc_app_val_1}")
    print(f"  Calc app 2:          {calc_app_val_2}")
    print(f"  Calc app val:        {calc_app_val}\n")
    print(f"  Max sw val:          {max_sw_val}")
    print(f"\n{'+' * 78}\n")

# -------------------------------------------------------------------------- #

# Define function to display sorted directories
def display_sorted_dir_names():
    '''
    Display sorted directories.
    '''
    global sorted_dir_names

    # Sort sorted_dir_names in descending order by calc_app_val
    sorted_dir_names.sort(key=lambda x: x.split(":")[1], reverse=True)

    # Echo the sorted list
    print("  Sorted Directory Names (Descending Order):\n")

    # Iterate through the sorted directory names
    for i, sorted_dir in enumerate(sorted_dir_names, start=1):
        print(f"            {i}.    {sorted_dir.split(':')[0]}")

        # Limit the output to a maximum of 99 entries
        if i == 99:
            break

    # Display a separator
    print(f"\n{'+' * 78}\n")

# -------------------------------------------------------------------------- #

# Define function to display calculated information
def display_calculated_flame_info():
    '''
    Display calculated information.
    '''
    global max_dir_name, max_sw_ver, max_sanitized_sw_ver

    # Print the highest directory name outside the loop
    print(f"  max flame ver:       {max_dir_name}")

    # Print the highest software app_ver outside the loop
    print(f"  max sw ver:          {max_sw_ver}")

    # Print the highest software app_ver outside the loop
    print(f"  sanitized sw ver:    {max_sanitized_sw_ver}")

    # Display a separator
    print(f"\n{'+' * 78}\n")

# -------------------------------------------------------------------------- #

def process_adsk_installations():
    '''
    Process Autodesk installations.
    '''
    global sorted_dir_names, max_dir_val, max_dir_name, max_sw_val, max_sw_ver, max_sanitized_sw_ver

    # Loop through directory names
    for dir_name in dir_names:
        # Get basename of directory
        dir_basename = os.path.basename(dir_name)

        # Check if basename contains 'pr'
        if "pr" in dir_basename:
            beta_sw = True
            release_sw = False
        else:
            beta_sw = False
            release_sw = True

        # Split basename into parts
        dir_basename_parts = dir_basename.split("_")

        # Set app_name to the first part
        app_name = dir_basename_parts[0]

        # Set app_ver_long to the second part
        app_ver_long = dir_basename_parts[1]

        # Split app_ver_long into parts by period
        app_ver_long_parts = app_ver_long.split(".")

        # Count the number of parts
        count_app_ver_long_parts = len(app_ver_long_parts)

        # Initialize variables
        app_maj = ""
        app_min = ""
        app_dot = ""
        app_dot_dot = ""
        app_pr_ver = ""
        app_pr_dot_ver = ""
        app_pr_val = ""
        calc_app_ver = ""
        calc_app_val_1 = ""
        calc_app_val_2 = ""
        calc_app_val = ""

        # Set app_val based on the app_name
        app_val = {
            "projectserver": "6",
            "flame": "5",
            "flare": "4",
            "flameassist": "3",
            "lustre": "2",
            "smoke": "1",
        }.get(app_name, "0")

        # ------------------------------------------------------------------ #

        # Process beta_sw condition
        process_beta_sw()

        # ------------------------------------------------------------------ #

        # Process release_sw condition
        process_release_sw()

        # ------------------------------------------------------------------ #

        # Append current dir_basename & calc_app_val to sorted_dir_names
        sorted_dir_names.append(f"{dir_basename}:{calc_app_val}")

        # ------------------------------------------------------------------ #

        # Update max_dir_val if the current calc_app_val is higher
        if calc_app_val > max_dir_val:
            max_dir_val = calc_app_val
            max_dir_ver = calc_app_ver
            max_dir_name = dir_basename
            max_sw_ver = calc_app_ver
            max_sanitized_sw_ver = sanitized_app_ver

        # ------------------------------------------------------------------ #

if __name__ == "__main__":
    initialize_adsk_variables()
    if check_adsk_installations():
        process_adsk_installations()
        display_sorted_dir_names()
        display_calculated_flame_info()

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
