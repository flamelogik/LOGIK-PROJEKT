import os
import json
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

def get_object_colors(abs_config_dir):
    object_colors_json = os.path.join(abs_config_dir, "object_colors.json")
    try:
        with open(object_colors_json, 'r') as f:
            object_colors = json.load(f)
        return object_colors
    except FileNotFoundError:
        print("Object colors JSON file not found!")
        return {}

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

        parent_command = "\n".join(command_parts) + "\n\t\n)"
        print(parent_command)

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
                
                child_command = "\n".join(child_command_parts) + "\n\t)\n"
                print(child_command)

        print("\n# ================= #\n")

def main():
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
    # print("Object Colors:", object_colors)

    # dark_red_rgb = object_colors.get("Dark Red")
    # if dark_red_rgb:
    #     print("RGB values of Dark Red:", dark_red_rgb)
    # else:
    #     print("Dark Red not found in object colors!")

    object_colors = get_object_colors(abs_config_dir)
    print("Object Colors:")
    for color, value in object_colors.items():
        print(f"{color}: {value}\n")

    # Search abs_config_dir for Python files that begin with 'library_template'
    for file_name in os.listdir(abs_config_dir):
        if file_name.startswith("library_template") and file_name.endswith(".json"):
            # Define the path to the JSON file
            json_file_path = os.path.join(abs_config_dir, file_name)

            # Call create_and_validate_from_template function with the path to the JSON file
            create_and_validate_from_template(json_file_path)

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
# -------------------------------------------------------------------------- #
# version:               1.0.6
# modified:              2024-05-14 - 15:30:58
# comments:              Defined 'object_colors' in a separate function.
