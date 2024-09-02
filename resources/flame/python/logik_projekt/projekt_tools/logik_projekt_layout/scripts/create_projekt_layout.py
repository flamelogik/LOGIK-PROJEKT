#

# -------------------------------------------------------------------------- #

# DISCLAIMER:       This file is part of LOGIK-PROJEKT.
#                   Copyright © 2024 man-made-mekanyzms
                
#                   LOGIK-PROJEKT creates directories, files, scripts & tools
#                   for use with Autodesk Flame and other software.

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
                
#                   Contact: phil_man@mac.com

# -------------------------------------------------------------------------- #

# File Name:        create_projekt_layout.py
# Version:          0.4.5
# Created:          2024-01-19
# Modified:         2024-08-31

# ========================================================================== #
# This section imports the necessary modules.
# ========================================================================== #

import flame
import datetime
import json
import os
import sys

# ========================================================================== #
# This section defines some variables based on the date.
# ========================================================================== #

# Get today's date and time
today_date = datetime.date.today().strftime("%Y-%m-%d")
today_time = datetime.datetime.now().strftime("%H-%M-%S")

from modules.classes.pathfinder_abs import abs_path_info

def get_absolute_info():
    abs_info = abs_path_info(__file__)

    abs_script_name = abs_info.script_name
    abs_path_to_this_script = abs_info.abs_path_to_this_script
    abs_script_dir = abs_info.abs_script_dir
    abs_parent_dir = abs_info.abs_parent_dir
    abs_config_dir = abs_info.abs_config_dir
    abs_scripts_dir = abs_info.abs_scripts_dir
    abs_modules_dir = abs_info.abs_modules_dir
    abs_classes_dir = abs_info.abs_classes_dir
    abs_functions_dir = abs_info.abs_functions_dir
    abs_version_dir = abs_info.abs_version_dir

    # abs_info.print_absolute_paths()

    return (
        abs_script_name,
        abs_path_to_this_script,
        abs_script_dir,
        abs_parent_dir,
        abs_config_dir,
        abs_scripts_dir,
        abs_modules_dir,
        abs_classes_dir,
        abs_functions_dir,
        abs_version_dir
    )

# Get absolute path information
(
    abs_script_name,
    abs_path_to_this_script,
    abs_script_dir,
    abs_parent_dir,
    abs_config_dir,
    abs_scripts_dir,
    abs_modules_dir,
    abs_classes_dir,
    abs_functions_dir,
    abs_version_dir
) = get_absolute_info()

# ========================================================================== #
# This section creates a decorative separator for blocks of text.
# ========================================================================== #

# Define a variable called 'separator'
separator = (
    f"+ {'-' * 75} +"
)

# ========================================================================== #
# This section creates a decorative separator for blocks of code.
# ========================================================================== #

# Define a variable called 'separator_hash'
separator_hash = (
    f"# {'#' * 75} #"
)

# ========================================================================== #
# This section defines color variables.
# ========================================================================== #

# Define object colors (from python function)
from modules.functions.object_colors import (
    object_colors
)

# ========================================================================== #
# This section defines a function to create or validate flame objects.
# ========================================================================== #

# Function to create or validate folders, reel groups, or reel objects.
def create_or_validate_object(
        library,
        object_name,
        object_type,
        object_color=None,
        object_reel_type=None,
        batch_group=False,
        reel_type='reel'  # Default to standard reel type
        ):

    # ---------------------------------------------------------------------- #

    # import flame

    # ---------------------------------------------------------------------- #

    # Check if the object exists in the library

    # For batch groups, continue with the existing logic
    if object_type == 'batch group':

        if batch_group:

            for group in library.batch_groups:

                if group.name == object_name:

                    print(
                        f"Batch group '{object_name}' already exists in library "
                        f"'{library.name}'."
                    )

                    return group

            # If the batch group doesn't exist, create it
            new_group = library.create_batch_group(
                name=object_name
                )

            if object_color:

                new_group.colour = object_color

            print(
                f"  New batch group '{object_name}' created successfully in library "
                f"'{library.name}'."
            )
            return new_group

    # ---------------------------------------------------------------------- #

    # Reel groups need to be handled separately
    if object_type == 'reel group':

        for group in library.reel_groups:

            if group.name == object_name:

                print(
                    f"Reel group '{object_name}' already exists in library "
                    f"'{library.name}'."
                    )

                return group

        # If the reel group doesn't exist, create it
        new_group = library.create_reel_group(
            name=object_name
            )

        if object_color:

            new_group.colour = object_color

        print(
            f"  New reel group '{object_name}' created successfully in library "
            f"'{library.name}'.")
        return new_group

    # ---------------------------------------------------------------------- #

    # For folders and reels, continue with the existing logic
    for obj in getattr(
        library,
        f"{object_type}s"
        ):

        if obj.name == object_name:

            print(
                f"{object_type.capitalize()} '{object_name}' already "
                f"exists in library '{library.name}'."
                )

            return obj

    # ---------------------------------------------------------------------- #

    # If the object doesn't exist, create it
    new_object = getattr(
        library,
        f"create_{object_type}"
        )(name=object_name)

    if object_color:

        new_object.colour = object_color

    if object_type == 'reel':
        if object_reel_type:
            new_object.attributes['Type'] = object_reel_type
            print(f"  New reel '{object_name}' created successfully in library "
                f"'{library.name}' with Type '{object_reel_type}'.")
        else:
            print(f"  New reel '{object_name}' created successfully in library "
                f"'{library.name}'.")
    else:
        print(
            f"  New {object_type} '{object_name}' created successfully in library "
            f"'{library.name}'."
            )

    return new_object

# ========================================================================== #
# This section defines a function to create or validate flame libraries.
# ========================================================================== #

# Function to create or validate library objects.
def create_or_validate_library(
        workspace,
        library_name,
        object_color=None
        ):

    # ---------------------------------------------------------------------- #

    # import flame

    # ---------------------------------------------------------------------- #

    # Check if the library exists in the workspace
    for library in workspace.libraries:

        if library.name == library_name:

            print(
                f"Library '{library_name}' already exists in workspace "
                f"'{workspace.name}'."
                )

            return library

    # ---------------------------------------------------------------------- #

    # If the library doesn't exist, create it.
    new_library = workspace.create_library(
        name=library_name
        )

    if object_color:
        new_library.colour = object_color
    print(
        f"  New library '{library_name}' created successfully in workspace "
        f"'{workspace.name}'."
        )

    return new_library

# ========================================================================== #
# This section defines a function to create or validate from templates.
# ========================================================================== #

# Function to create or validate objects from template JSON files.
def create_and_validate_from_template(json_file, the_current_workspace):

    # ---------------------------------------------------------------------- #

    # import flame

    # ---------------------------------------------------------------------- #

    # print(f"Processing file: {json_file}")
    print(f"\n{separator}\n")
    print(f"  Processing file: {os.path.basename(json_file)}")

    # Load the JSON file
    with open(json_file) as file:
        data = json.load(file)

    for item_key, item_data in data.items():
        object_name = item_data["object_name"]
        process_type = item_data["process_type"]
        parent_object = item_data["parent_object"]
        display_name = item_data["display_name"]
        object_type = item_data["object_type"]
        object_color = item_data.get("object_color", "")  # Get object_color or default to empty string

        # Include object_color if it's not empty
        if object_color:
            # Construct the command
            command_parts = [
                f"{object_name} = \\",
                f"\t{process_type}(",
                f"\t\t{parent_object},",  # Ensure proper string quotation
                f"\t\t{display_name},",   # Ensure proper string quotation
                # f"\t\t{object_type},",    # Not sure if object_type should be included
                f"\t\t{object_color}"     # Ensure proper string quotation
            ]
        else:
            # Construct the command without object_color
            command_parts = [
                f"{object_name} = \\",
                f"\t{process_type}(",
                f"\t\t{parent_object},",  # Ensure proper string quotation
                f"\t\t{display_name}"     # Ensure proper string quotation
                # f"\t\t{object_type}"      # Not sure if object_type should be included
            ]

        print(f"\n{separator}\n")
        print(f"  Creating: {object_type}: {display_name}\n")
        parent_command = "\n".join(command_parts) + "\n\t)"
        print(parent_command)
        try:
            exec(parent_command)
        except Exception as e:
            print(f"  An error occurred while executing the command: {e}\n")

        # Check if there are children objects
        if "children" in item_data:
            children = item_data["children"]
            for child_key, child_data in children.items():
                child_object_name = child_data["object_name"]
                child_process_type = child_data["process_type"]
                child_parent_object = child_data["parent_object"]
                child_display_name = child_data["display_name"]
                child_object_type = child_data["object_type"]
                child_object_color = child_data.get("object_color", "")  # Get object_color or default to empty string

                # Include child_object_color if it's not empty
                if child_object_color:
                    # Construct the command
                    child_command_parts = [
                        f"{child_object_name} = \\",
                        f"\t{child_process_type}(",
                        f"\t\t{child_parent_object},",  # Ensure proper string quotation
                        f"\t\t{child_display_name},",  # Ensure proper string quotation
                        f"\t\t'{child_object_type}',",  # Ensure proper string quotation
                        f"\t\t{child_object_color}"  # Ensure proper string quotation
                    ]
                else:
                    # Construct the command without child_object_color
                    child_command_parts = [
                        f"{child_object_name} = \\",
                        f"\t{child_process_type}(",
                        f"\t\t{child_parent_object},",  # Ensure proper string quotation
                        f"\t\t{child_display_name},",  # Ensure proper string quotation
                        f"\t\t'{child_object_type}'"  # Ensure proper string quotation
                    ]

                print(f"\n{separator}\n")
                print(f"  Creating: {child_object_type}: {child_display_name}\n")
                child_command = "\n".join(child_command_parts) + "\n\t)\n"
                print(child_command)
                try:
                    exec(child_command)
                except Exception as e:
                    print(f"  An error occurred while executing the command: {e}\n")

        print(f"\n{separator}\n")

# -------------------------------------------------------------------------- #

# ========================================================================== #
# This section defines functions to modify the Default Library.
# ========================================================================== #

# Function to change the color of the 'Default Library' to 'Dark Red'.
def change_default_library_color(workspace):

    # ---------------------------------------------------------------------- #

    # import flame

    # ---------------------------------------------------------------------- #

    # Find the 'Default Library' in the workspace
    for library in workspace.libraries:
        if library.name == 'Default Library':

            # Change the color of the 'Default Library'
            library.colour = object_colors.get("Dark Red")

            print(f"Color of 'Default Library' changed to Dark Red.")
            return True

    # 'Default Library' not found
    print("Library 'Default Library' not found.")
    return False

# -------------------------------------------------------------------------- #

# Function to change the name of the 'Default Library' to 'desktops'.
def change_default_library_name(workspace, new_name):

    # ---------------------------------------------------------------------- #

    # import flame

    # ---------------------------------------------------------------------- #

    # Find the 'Default Library' in the workspace
    for library in workspace.libraries:
        if library.name == 'Default Library':

            # Change the name of the 'Default Library'
            library.name = new_name

            print(f"Name of 'Default Library' changed to '{new_name}'.")
            return True

    # 'Default Library' not found
    print("Library 'Default Library' not found.")
    return False

# ========================================================================== #
# This section defines a function to create a logik projekt layout.
# ========================================================================== #

# Create Project Layout by creating or validate folders, reels, & reel groups
def create_layout(*args):

    # ---------------------------------------------------------------------- #

    # import flame

    # ---------------------------------------------------------------------- #

    # If Flame passes any arguments, you can handle them here
    if args:
        print("Received arguments from Flame:", args)

    (
        abs_script_name,
        abs_path_to_this_script,
        abs_script_dir,
        abs_parent_dir,
        abs_config_dir,
        abs_scripts_dir,
        abs_modules_dir,
        abs_classes_dir,
        abs_functions_dir,
        abs_version_dir
    ) = get_absolute_info()

    # ---------------------------------------------------------------------- #

    the_current_projekt = flame.projects.current_project
    the_current_workspace = the_current_projekt.current_workspace
    the_current_desktop = the_current_workspace.desktop

    # ---------------------------------------------------------------------- #

    user_nickname = flame.users.current_user.nickname

    # ---------------------------------------------------------------------- #

    # Validate or create 'Default Library' library
    default_library = \
        create_or_validate_library(
            the_current_workspace,
            'Default Library'
            )

    # Change the color of 'Default Library' to Dark Red
    change_default_library_color(the_current_workspace)

    # Change the name of 'Default Library' to 'desktops'
    change_default_library_name(the_current_workspace, 'desktops')

    # Change the variable name to 'desktops_library'
    desktops_library = default_library

    # Validate or create 'work' folder in 'desktops'
    user_folder = \
        create_or_validate_object(
            desktops_library,
            user_nickname,
            'folder'
            )

    # ---------------------------------------------------------------------- #

    # Search abs_config_dir for Python files that begin with 'library_template'
    for file_name in sorted(os.listdir(abs_config_dir)):
        if file_name.startswith("library_template") and file_name.endswith(".json"):
            # Define the path to the JSON file
            object_colors_json_path = os.path.join(abs_config_dir, file_name)

            # Call create_and_validate_from_template function with the path to the JSON file
            create_and_validate_from_template(object_colors_json_path, the_current_workspace)

    # ---------------------------------------------------------------------- #

    # Change the current desktop name
    # new_desktop_name = today_date + '-work'
    # user_name = flame.users.current_user.name
    # new_desktop_name = today_date + user_name
    # the_current_desktop.name = new_desktop_name
    new_desktop_name = today_date + '-' + user_nickname
    the_current_desktop.name = new_desktop_name

    # Print the name of the current desktop
    print(f"Current desktop: {the_current_desktop.name}")

    # Change the name and color of the reel group in the current desktop
    for desktop_reel_group in the_current_desktop.reel_groups:
        if desktop_reel_group.name == 'Reels':
            desktop_reel_group.name = today_date + '-conform'
            desktop_reel_group.colour = object_colors.get("Dark Purple")
            for reel in desktop_reel_group.reels:
                    if reel.name == 'Reel 1':
                        reel.name = 'ref'
                        reel.colour = object_colors.get("Dark Blue")
                    if reel.name == 'Reel 2':
                        reel.name = 'Sources'
                        reel.colour = object_colors.get("Dark Green")
                    if reel.name == 'Sequences':
                        reel.colour = object_colors.get("Dark Red")

    # Validate or create dated postings reel in 'pattern_browsed_clips'
    published_sequences_reel = \
        create_or_validate_object(
            desktop_reel_group,
            'Published-Sequences',
            'reel',
            # object_reel_type='Sequences',
            object_colors.get("Red")
            )

    # Validate or create dated postings reel in 'pattern_browsed_clips'
    published_versions_reel = \
        create_or_validate_object(
            desktop_reel_group,
            'Published-Versions',
            'reel',
            object_colors.get("Green")
            )

    # Validate or create dated postings reel in 'pattern_browsed_clips'
    todays_postings_reel = \
        create_or_validate_object(
            desktop_reel_group,
            today_date + '-postings',
            'reel',
            object_colors.get("Blue")
            )

    # ---------------------------------------------------------------------- #

    print("Project layout setup completed.")

# ========================================================================== #
# This section defines custom flame menus.
# ========================================================================== #

# Add custom UI actions
def get_main_menu_custom_ui_actions():

    # ---------------------------------------------------------------------- #

    # import flame

    # ---------------------------------------------------------------------- #

    return [
        {
            'name': 'logik-projekt',
            'hierarchy': [],
            'actions': []
        },
        {
            'name': 'create',
            'hierarchy': ['logik-projekt'],
            'order': 1,
            'actions': [
                {
                    'name': 'create layout',
                    'execute': create_layout,
                    'minimumVersion': '2025'
                }
            ]
        }
    ]

# -------------------------------------------------------------------------- #

'''
# def get_mediahub_files_custom_ui_actions():

    # ---------------------------------------------------------------------- #

    # import flame

    # ---------------------------------------------------------------------- #

    return [
        {
            'name': 'create',
            'hierarchy': ['logik-projekt'],
            'order': 1,
            'actions': [
                {
                    'name': 'create layout',
                    'execute': create_layout,
                    'minimumVersion': '2025'
                }
            ]
        }
    ]
'''

# -------------------------------------------------------------------------- #

def get_media_panel_custom_ui_actions():

    # ---------------------------------------------------------------------- #

    # import flame

    # ---------------------------------------------------------------------- #

    return [
        {
            'name': 'create',
            'hierarchy': ['logik-projekt'],
            'order': 1,
            'actions': [
                {
                    'name': 'create layout',
                    'order': 1,
                    'separator': 'below',
                    'execute': create_layout,
                    'minimumVersion': '2025'
                }
            ]
        }
    ]

# ========================================================================== #
# This section defines how to handle the main script function.
# ========================================================================== #

# If this script is executed as main
if __name__ == "__main__":
    create_layout()  # Call setup function for immediate execution

# ========================================================================== #
# C2 A9 32 30 32 34 2D 4D 41 4E 2D 4D 41 44 45 2D 4D 45 4B 41 4E 59 5A 4D 53 #
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
# version:               0.0.1
# modified:              2024-05-03 - 01:53:36
# comments:              Basic functionality defined and tested
# -------------------------------------------------------------------------- #
# version:               0.0.2
# modified:              2024-05-03 - 02:13:01
# comments:              Fixed some formatting and flame menus
# -------------------------------------------------------------------------- #
# version:               0.0.3
# modified:              2024-05-03 - 11:26:02
# comments:              Changed 'the_current_project' to 'the_current_projekt'
# -------------------------------------------------------------------------- #
# version:               0.0.4
# modified:              2024-05-03 - 11:38:53
# comments:              Standardized 'logik-projekt' menu entries
# -------------------------------------------------------------------------- #
# version:               0.0.5
# modified:              2024-05-12 - 15:37:50
# comments:              Added function to read directories from JSON files.
# -------------------------------------------------------------------------- #
# version:               0.0.6
# modified:              2024-05-12 - 18:16:05
# comments:              Added a 'separators' function and tested in flame 2025.
# -------------------------------------------------------------------------- #
# version:               0.0.7
# modified:              2024-05-14 - 16:30:58
# comments:              Minor reformatting.
# -------------------------------------------------------------------------- #
# version:               0.0.8
# modified:              2024-05-14 - 16:31:23
# comments:              Changed object_colors from python to JSON.
# -------------------------------------------------------------------------- #
# version:               0.0.9
# modified:              2024-05-14 - 16:31:47
# comments:              Tested in flame 2025.
# -------------------------------------------------------------------------- #
# version:               0.1.0
# modified:              2024-05-14 - 16:46:55
# comments:              Production tested in flame 2025.
# -------------------------------------------------------------------------- #
# version:               0.2.0
# modified:              2024-05-14 - 18:05:26
# comments:              Prepped for obsolete code removal. Tested in flame 2025
# -------------------------------------------------------------------------- #
# version:               0.3.0
# modified:              2024-05-14 - 19:27:33
# comments:              Restored 'object_colors' from python function.
# -------------------------------------------------------------------------- #
# version:               0.3.1
# modified:              2024-05-15 - 07:55:47
# comments:              Renamed 'classes_and_functions' dir to 'modules'.
# -------------------------------------------------------------------------- #
# version:               0.4.1
# modified:              2024-05-18 - 18:01:29
# comments:              Added GNU GPLv3 Disclaimer.
# -------------------------------------------------------------------------- #
# version:               0.4.2
# modified:              2024-05-18 - 18:46:51
# comments:              Minor modification to Disclaimer.
# -------------------------------------------------------------------------- #
# version:               0.4.3
# modified:              2024-06-03 - 10:32:22
# comments:              Moved import flame statement to each function
# -------------------------------------------------------------------------- #
# version:               0.4.4
# modified:              2024-06-12 - 12:21:22
# comments:              Restored import flame statement to top of script.
# -------------------------------------------------------------------------- #
# version:               0.4.5
# modified:              2024-08-31 - 18:40:12
# comments:              prep for release.
# -------------------------------------------------------------------------- #
