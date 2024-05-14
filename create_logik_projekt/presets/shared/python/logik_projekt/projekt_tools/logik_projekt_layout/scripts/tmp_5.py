# filename: create_projekt_layout.py

# -------------------------------------------------------------------------- #

# Program Name:     create_projekt_layout.py
# Version:          1.0.6
# Language:         python script
# Flame Version:    2025.x
# Author:           Phil MAN - phil_man@mac.com
# Toolset:          MAN_MADE_MATERIAL: LOGIK-PROJEKT
# Created:          2024-04-20
# Modified:         2024-05-14
# Modifier:         Phil MAN - phil_man@mac.com

# Description:      This script creates logik projekt flame layouts.

# Installation:     Copy the 'LOGIK-PROJEKT' directory to:
#                   '/opt/Autodesk/shared/python/'

# Changelist:       The full changelist is at the end of this document.

# -------------------------------------------------------------------------- #

# ========================================================================== #
# This section imports the necessary modules.
# ========================================================================== #

import flame
import datetime
import json
import os

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
    abs_classes_and_functions_dir = abs_info.abs_classes_and_functions_dir
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
        abs_classes_and_functions_dir,
        abs_classes_dir, 
        abs_functions_dir, 
        abs_version_dir
    )

# ========================================================================== #
# This section defines color variables.
# ========================================================================== #

# Define object colors
object_colors = {

    # Autodesk Colors
    "Red": (0.376, 0.047, 0.047),             # Red
    "Green": (0.114, 0.263, 0.176),           # Green
    "Bright Green": (0.102, 0.502, 0.208),    # Bright Green
    "Blue": (0.188, 0.263, 0.400),            # Blue
    "Light Blue": (0.263, 0.408, 0.502),      # Light Blue
    "Purple": (0.388, 0.318, 0.541),          # Purple
    "Orange": (0.600, 0.345, 0.165),          # Orange
    "Gold": (0.478, 0.478, 0.271),            # Gold
    "Yellow": (0.784, 0.784, 0.196),          # Yellow
    "Light Grey": (0.706, 0.706, 0.706),      # Light Grey
    "Black": (0.000, 0.000, 0.000),           # Black

    # Custom Colors
    "Dark Red": (0.188, 0.023, 0.023),        # Dark Red
    "Dark Green": (0.057, 0.131, 0.088),      # Dark Green
    "Dark Blue": (0.094, 0.131, 0.200),       # Dark Blue
    "Dark Purple": (0.194, 0.159, 0.270),     # Dark Purple
    "Dark Orange": (0.300, 0.172, 0.082),     # Dark Orange
    "Dark Gold": (0.239, 0.239, 0.135),       # Dark Gold

    # Grey Scale
    "Grey02": (0.928, 0.928, 0.928),          # Grey02
    "Grey03": (0.857, 0.857, 0.857),          # Grey03
    "Grey04": (0.786, 0.786, 0.786),          # Grey04
    "Grey05": (0.714, 0.714, 0.714),          # Grey05
    "Grey06": (0.643, 0.643, 0.643),          # Grey06
    "Grey07": (0.571, 0.571, 0.571),          # Grey07
    "Grey08": (0.500, 0.500, 0.500),          # Grey08
    "Grey09": (0.417, 0.417, 0.417),          # Grey09
    "Grey10": (0.333, 0.333, 0.333),          # Grey10
    "Grey11": (0.250, 0.250, 0.250),          # Grey11
    "Grey12": (0.167, 0.167, 0.167),          # Grey12
    "Grey13": (0.083, 0.083, 0.083)           # Grey13
}

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
                f"New batch group '{object_name}' created successfully in library "
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
            f"New reel group '{object_name}' created successfully in library "
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

    # # If the object doesn't exist, create it
    # new_object = getattr(
    #     library,
    #     f"create_{object_type}"
    #     )(name=object_name)

    # if object_color:

    #     new_object.colour = object_color

    # print(
    #     f"New {object_type} '{object_name}' created successfully in library "
    #     f"'{library.name}'."
    #     )

    # return new_object

    # ---------------------------------------------------------------------- #

    # # If the object doesn't exist, create it
    # if object_type == 'folder':

    #     new_object = library.create_folder(
    #         name=object_name
    #         )

    # elif object_type == 'reel':

    #     new_object = library.create_reel(
    #         name=object_name
    #         )

    # elif object_type == 'schematic':

    #     new_object = library.create_schematic_reel(
    #         name=object_name
    #         )

    # elif object_type == 'sequences':

    #     new_object = library.create_sequences_reel(
    #         name=object_name
    #         )

    # elif object_type == 'shelf':

    #     new_object = library.create_shelf_reel(
    #         name=object_name
    #         )

    # else:

    #     new_object = getattr(
    #         library,
    #         f"create_{object_type}"
    #         )(name=object_name)

    # if object_color:

    #     new_object.colour = object_color

    # print(
    #     f"New {object_type} '{object_name}' created successfully in library "
    #     f"'{library.name}'."
    #     )

    # # Add the new object to the library list
    # getattr(library, f"{object_type}s").append(new_object)

    # # Check the type of the created object
    # if new_object.type != object_type.capitalize():
    #     # Delete the incorrect type
    #     getattr(library, f"{object_type}s").remove(new_object)
    #     # Raise an exception
    #     raise ValueError(f"Created object '{object_name}' is not of type '{object_type.capitalize()}'")

    # return new_object

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
            print(f"New reel '{object_name}' created successfully in library "
                f"'{library.name}' with Type '{object_reel_type}'.")
        else:
            print(f"New reel '{object_name}' created successfully in library "
                f"'{library.name}'.")
    else:
        print(
            f"New {object_type} '{object_name}' created successfully in library "
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
        f"New library '{library_name}' created successfully in workspace "
        f"'{workspace.name}'."
        )

    return new_library

# ========================================================================== #
# This section defines a function to create or validate from templates.
# ========================================================================== #

# Function to create or validate objects from template JSON files.
def create_and_validate_from_template(json_file, the_current_workspace):

    # import flame

    # the_current_projekt = flame.projects.current_project
    # the_current_workspace = the_current_projekt.current_workspace
    # the_current_desktop = the_current_workspace.desktop

    # print(f"Processing file: {json_file}")
    print(f"Processing file: {os.path.basename(json_file)}\n")

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
                f"\t\t'{display_name}',",   # Ensure proper string quotation
                # f"\t\t{object_type},",    # Not sure if object_type should be included
                f"\t\t{object_color}"     # Ensure proper string quotation
            ]
        else:
            # Construct the command without object_color
            command_parts = [
                f"{object_name} = \\",
                f"\t{process_type}(",
                f"\t\t{parent_object},",  # Ensure proper string quotation
                f"\t\t'{display_name}'"     # Ensure proper string quotation
                # f"\t\t{object_type}"      # Not sure if object_type should be included
            ]

        print(f"Creating: {object_type}: {display_name}")
        parent_command = "\n".join(command_parts) + "\n\t)"
        print(parent_command)
        try:
            exec(parent_command)
        except Exception as e:
            print(f"An error occurred while executing the command: {e}")

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
                        f"\t\t'{child_display_name}',",   # Ensure proper string quotation
                        f"\t\t'{child_object_type}',",    # Ensure proper string quotation
                        f"\t\t{child_object_color}"     # Ensure proper string quotation
                    ]
                else:
                    # Construct the command without child_object_color
                    child_command_parts = [
                        f"{child_object_name} = \\",
                        f"\t{child_process_type}(",
                        f"\t\t{child_parent_object},",  # Ensure proper string quotation
                        f"\t\t'{child_display_name}',",   # Ensure proper string quotation
                        f"\t\t'{child_object_type}'"       # Ensure proper string quotation
                    ]
                
                print(f"Creating: {child_object_type}: {child_display_name}")
                child_command = "\n".join(child_command_parts) + "\n\t)\n"
                print(child_command)
                try:
                    exec(child_command)
                except Exception as e:
                    print(f"An error occurred while executing the command: {e}")

        print("\n# ================= #\n")


# -------------------------------------------------------------------------- #

# ========================================================================== #
# This section defines functions to modify the Default Library.
# ========================================================================== #

# Function to change the color of the 'Default Library' to 'Dark Red'.
def change_default_library_color(workspace):

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
        abs_classes_and_functions_dir,
        abs_classes_dir, 
        abs_functions_dir, 
        abs_version_dir
    ) = get_absolute_info()

    # object_colors = get_object_colors(abs_config_dir)

    # print("Object Colors:")
    # for color, value in object_colors.items():
    #     print(f"{color}: {value}\n")

    # ---------------------------------------------------------------------- #

    the_current_projekt = flame.projects.current_project
    the_current_workspace = the_current_projekt.current_workspace
    the_current_desktop = the_current_workspace.desktop

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

    # ---------------------------------------------------------------------- #

    # Search abs_config_dir for Python files that begin with 'library_template'
    for file_name in sorted(os.listdir(abs_config_dir)):
        if file_name.startswith("library_template") and file_name.endswith(".json"):
            # Define the path to the JSON file
            json_file_path = os.path.join(abs_config_dir, file_name)

            # Call create_and_validate_from_template function with the path to the JSON file
            create_and_validate_from_template(json_file_path, the_current_workspace)

    # # Validate or create 'desktops' library
    # desktops_library = \
    #     create_or_validate_library(
    #         the_current_workspace,
    #         'desktops'
    #         )

    # # Validate or create 'work' folder in 'desktops'
    # work_folder = \
    #     create_or_validate_object(
    #         desktops_library,
    #         'work',
    #         'folder'
    #         )

    # ---------------------------------------------------------------------- #

    # # Validate or create 'reference' library
    # reference_library = \
    #     create_or_validate_library(
    #         the_current_workspace,
    #         'reference',
    #         object_colors.get("Dark Orange")
    #         )

    # # Validate or create dated reference folder in 'reference'
    # todays_reference_folder = \
    #     create_or_validate_object(
    #         reference_library,
    #         today_date + '-reference',
    #         'folder'
    #         )

    # ---------------------------------------------------------------------- #

    # # Validate or create 'editorial' library
    # editorial_library = \
    #     create_or_validate_library(
    #         the_current_workspace,
    #         'editorial',
    #         object_colors.get("Dark Gold")
    #         )

    # # Validate or create folder 'conforms' in 'editorial'
    # conforms_folder = \
    #     create_or_validate_object(
    #         editorial_library,
    #         'conforms',
    #         'folder'
    #         )

    # # Validate or create dated conforms template reel group in 'conforms'
    # dated_conforms_template_reel_group = \
    #     create_or_validate_object(
    #         conforms_folder,
    #         'YYYY-MM-DD-conform',
    #         'reel group'
    #         )

    # # Rename reels in 'dated conforms template reel group'
    # for reel in dated_conforms_template_reel_group.reels:
    #     if reel.name == 'Reel 1':
    #         reel.name = 'ref'
    #         reel.colour = object_colors.get("Dark Blue")
    #     if reel.name == 'Reel 2':
    #         reel.name = 'Sources'
    #         reel.colour = object_colors.get("Dark Green")
    #     if reel.name == 'Sequences':
    #         reel.colour = object_colors.get("Dark Red")

    # # # Validate or create dated conforms reel group in 'conforms'
    # # dated_conforms_reel_group = \
    # #     create_or_validate_object(
    # #         conforms_folder,
    # #         today_date + '-conform',
    # #         'reel group'
    # #         )

    # # # Rename reels in 'dated conforms reel group'
    # # for reel in dated_conforms_reel_group.reels:
    # #     if reel.name == 'Reel 1':
    # #         reel.name = 'ref'
    # #         reel.colour = object_colors.get("Dark Blue")
    # #     if reel.name == 'Reel 2':
    # #         reel.name = 'Sources'
    # #         reel.colour = object_colors.get("Dark Green")
    # #     if reel.name == 'Sequences':
    # #         reel.colour = object_colors.get("Dark Red")

    # # Validate or create folder 'work_in_progress' in 'editorial'
    # work_in_progress_folder = \
    #     create_or_validate_object(
    #         editorial_library,
    #         'work_in_progress',
    #         'folder'
    #         )

    # # Validate or create folder 'postings' in 'work_in_progress'
    # postings_folder = \
    #     create_or_validate_object(
    #         work_in_progress_folder,
    #         'postings',
    #         'folder',
    #         object_colors.get("Blue")
    #         )

    # # Validate or create dated postings reel in 'postings'
    # todays_postings_reel = \
    #     create_or_validate_object(
    #         postings_folder,
    #         today_date + '-postings',
    #         'reel'
    #         )

    # ---------------------------------------------------------------------- #

    # # Validate or create 'assets' library
    # assets_library = \
    #     create_or_validate_library(
    #         the_current_workspace,
    #         'assets',
    #         object_colors.get("Dark Green")
    #         )

    # # Validate or create asset folders in 'assets'
    # audio_folder = \
    #     create_or_validate_object(
    #         assets_library,
    #         'audio',
    #         'folder'
    #         )

    # cgi_folder = \
    #     create_or_validate_object(
    #         assets_library,
    #         'CGI',
    #         'folder'
    #         )

    # footage_graded_folder = \
    #     create_or_validate_object(
    #         assets_library,
    #         'footage_graded',
    #         'folder'
    #         )

    # footage_raw_folder = \
    #     create_or_validate_object(
    #         assets_library,
    #         'footage_raw',
    #         'folder'
    #         )

    # graphics_folder = \
    #     create_or_validate_object(
    #         assets_library,
    #         'graphics',
    #         'folder'
    #         )

    # matchmoving_folder = \
    #     create_or_validate_object(
    #         assets_library,
    #         'matchmoving',
    #         'folder'
    #         )

    # miscellaneous_folder = \
    #     create_or_validate_object(
    #         assets_library,
    #         'miscellaneous',
    #         'folder'
    #         )

    # roto_folder = \
    #     create_or_validate_object(
    #         assets_library,
    #         'roto',
    #         'folder'
    #         )

    # slates_folder = \
    #     create_or_validate_object(
    #         assets_library,
    #         'slates',
    #         'folder'
    #         )

    # subtitles_folder = \
    #     create_or_validate_object(
    #         assets_library,
    #         'subtitles',
    #         'folder'
    #         )

    # tracking_folder = \
    #     create_or_validate_object(
    #         assets_library,
    #         'tracking',
    #         'folder'
    #         )

    # video_folder = \
    #     create_or_validate_object(
    #         assets_library,
    #         'video',
    #         'folder'
    #         )

    # ---------------------------------------------------------------------- #

    # # Validate or create 'masters' library
    # masters_library = \
    #     create_or_validate_library(
    #         the_current_workspace,
    #         'masters',
    #         object_colors.get("Dark Blue")
    #         )

    # # Validate or create folder 'final_masters' in 'masters'
    # final_masters_folder = \
    #     create_or_validate_object(
    #         masters_library,
    #         'final_masters',
    #         'folder'
    #         )

    # # # Validate or create 'master_edits' reel group in 'final_masters'
    # # master_edits_reel_group = \
    # #     create_or_validate_object(
    # #         final_masters_folder,
    # #         'master_edits',
    # #         'reel group'
    # #         )

    # # # Rename reels in 'master edits reel group'
    # # for reel in master_edits_reel_group.reels:
    # #     if reel.name == 'Reel 1':
    # #         reel.name = 'final_masters'
    # #     elif reel.name == 'Reel 2':
    # #         reel.name = 'versions'
    # #     elif reel.name == 'Sequences':
    # #         reel.name = 'slated_masters'

    # # Validate or create 'final masters' reel in 'final_masters'
    # final_masters_reel = \
    #     create_or_validate_object(
    #         final_masters_folder,
    #         'final_masters',
    #         'reel',
    #         # object_reel_type='Sequences',
    #         object_colors.get("Dark Gold")
    #         )

    # # Validate or create 'slated masters' reel in 'final_masters'
    # slated_masters_reel = \
    #     create_or_validate_object(
    #         final_masters_folder,
    #         'slated_masters',
    #         'reel',
    #         # object_reel_type='Sequences',
    #         object_colors.get("Dark Red")
    #         )

    # # Validate or create 'versions' reel in 'final_masters'
    # versions_reel = \
    #     create_or_validate_object(
    #         final_masters_folder,
    #         'versions',
    #         'reel',
    #         # object_reel_type='Sequences',
    #         object_colors.get("Dark Blue")
    #         )

    # ---------------------------------------------------------------------- #

    # # Validate or create 'shots' library
    # shots_library = \
    #     create_or_validate_library(
    #         the_current_workspace,
    #         'shots',
    #         object_colors.get("Dark Purple")
    #         )

    # # Validate or create folder 'batch_groups' in 'shots'
    # batch_groups_folder = \
    #     create_or_validate_object(
    #         shots_library,
    #         'batch_groups',
    #         'folder'
    #         )

    # ---------------------------------------------------------------------- #

    # Change the current desktop name
    new_desktop_name = today_date + '-work'
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

    # # Validate or create batch group in 'default_Desktop'
    # default_Desktop_batch_group = \
    #     create_or_validate_object(
    #         the_current_desktop,
    #         'My New Batch',
    #         'batch group',
    #         object_colors.get("Red"),
    #         batch_group=True
    #         )

    # ---------------------------------------------------------------------- #

    print("Project layout setup completed.")

# ========================================================================== #
# This section defines custom flame menus.
# ========================================================================== #

# Add custom UI actions
def get_main_menu_custom_ui_actions():

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

# def get_mediahub_files_custom_ui_actions():

#     return [
#         {
#             'name': 'create',
#             'hierarchy': ['logik-projekt'],
#             'order': 1,
#             'actions': [
#                 {
#                     'name': 'create layout',
#                     'execute': create_layout,
#                     'minimumVersion': '2025'
#                 }
#             ]
#         }
#     ]

# -------------------------------------------------------------------------- #

def get_media_panel_custom_ui_actions():

    return [
        {
            'name': 'create',
            'hierarchy': ['logik-projekt'],
            'order': 1,
            'actions': [
                {
                    'name': 'create layout',
                    'order': 4,
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
# C2 A9 2D 32 30 32 34 2D 4D 41 4E 5F 4D 41 44 45 5F 4D 41 54 45 52 49 61 4C #
# ========================================================================== #

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
# version:               1.0.6
# modified:              2024-05-14 - 15:30:58
# comments:              Defined 'object_colors' in a separate function.
