# filename: create_projekt_layout.py

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
def create_and_validate_from_template(json_file):

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
                f"\t\t{parent_object},",
                f"\t\t'{display_name}',",
                f"\t\t'{object_type}',",
                f"\t\t'{object_color}'",
            ]
        else:
            # Construct the command without object_color
            command_parts = [
                f"{object_name} = \\",
                f"\t{process_type}(",
                f"\t\t{parent_object},",
                f"\t\t'{display_name}',",
                f"\t\t'{object_type}'"
            ]

        print(f"Creating: {object_type}: {display_name}")
        parent_command = "\n".join(command_parts) + "\n\t\n)"
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
                        f"\t\t{child_parent_object},",
                        f"\t\t'{child_display_name}',",
                        f"\t\t'{child_object_type}',",
                        f"\t\t'{child_object_color}'"
                    ]
                else:
                    # Construct the command without child_object_color
                    child_command_parts = [
                        f"{child_object_name} = \\",
                        f"\t{child_process_type}(",
                        f"\t\t{child_parent_object},",
                        f"\t\t'{child_display_name}',",
                        f"\t\t'{child_object_type}'"
                    ]
                
                print(f"Creating: {object_type}: {display_name}")
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
    for file_name in os.listdir(
        abs_config_dir
    ):
        if file_name.startswith("library_template") and file_name.endswith(".json"):
            # Define the path to the JSON file
            json_file_path = os.path.join(abs_config_dir, file_name)

            # Call create_and_validate_from_template function with the path to the JSON file
            create_and_validate_from_template(json_file_path)

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
# -------------------------------------------------------------------------- #
# version:               0.0.5
# modified:              2024-05-12 - 15:37:50
# comments:              Added function to read directories from JSON files.
# -------------------------------------------------------------------------- #
# version:               0.0.6
# modified:              2024-05-12 - 18:16:05
# comments:              Added a 'separators' function and tested in flame 2025.
