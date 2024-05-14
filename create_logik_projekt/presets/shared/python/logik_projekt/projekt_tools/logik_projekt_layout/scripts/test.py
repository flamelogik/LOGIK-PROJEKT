# Import the os module to work with file paths
import os

# Import the json module to work with JSON files
import json

import sys

# Import the pathfinder_abs class from the module
from modules.classes.pathfinder_abs import abs_path_info

# -------------------------------------------------------------------------- #

# Get the abs_path_info
def get_absolute_info():
    # Create an instance of the abs_path_info class
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

    # Call the method to print script information
    abs_info.print_absolute_paths()

    # Return the abs_info values
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

# -------------------------------------------------------------------------- #

def get_object_colors(abs_config_dir):
    # Construct the path to the object_colors.json file
    library_template_json = os.path.join(
        abs_config_dir, 
        "object_colors.json")

    # Read object colors from JSON file
    try:
        with open(library_template_json, 'r') as f:
            object_colors = json.load(f)
        return object_colors
    except FileNotFoundError:
        print("Object colors JSON file not found!")
        return {}

def create_and_validate_from_template(json_file):
    # Construct the path to the object_colors.json file
    abs_config_dir = os.path.dirname(os.path.abspath(__file__))
    library_template_json = os.path.join(abs_config_dir, "library_template_03.json")

    # # Read object colors from JSON file
    # try:
    #     with open(library_template_json, 'r') as f:
    #         object_colors = json.load(f)
    # except FileNotFoundError:
    #     print("Object colors JSON file not found!")
    #     object_colors = {}

    # Load the JSON file
    with open(library_template_json) as json_file:
        data = json.load(library_template_json)

    # Iterate over each item
    for item_key, item_data in data["library_template_03"]["children"].items():
        # Extract relevant data
        object_name = item_data["object_name"]
        process_type = item_data["process_type"]
        parent_object = item_data["parent_object"]
        display_name = item_data["display_name"]
        object_type = item_data["object_type"]
        
        # Generate the command string
        command = f"{object_name} = \\\n\t{process_type}(\n\t\t{parent_object},\n\t\t'{display_name}',\n\t\t'{object_type}'\n\t)"

        # # Execute the command
        # exec(command)

        # Print the command (optional)
        print(command)

def main():
    # Get the absolute information
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

    # # Call the function to get object colors
    # object_colors = get_object_colors(abs_config_dir)

    # # Print the Object Colors
    # print("Object Colors:", object_colors)

    # # Access the RGB values of "Dark Red"
    # dark_red_rgb = object_colors.get("Dark Red")

    # # Print the RGB values of "Dark Red"
    # if dark_red_rgb:
    #     print("RGB values of Dark Red:", dark_red_rgb)
    # else:
    #     print("Dark Red not found in object colors!")

    # Example usage
    create_and_validate_from_template('data.json')

# Execute the main function
if __name__ == "__main__":
    main()
# -------------------------------------------------------------------------- #
# version:               0.0.5
# modified:              2024-05-12 - 15:37:50
# comments:              Added function to read directories from JSON files.
# -------------------------------------------------------------------------- #
# version:               0.0.6
# modified:              2024-05-12 - 18:16:05
# comments:              Added a 'separators' function and tested in flame 2025.
