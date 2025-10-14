import json
import os
import logging

def directory_structure_to_workspace(filesystem_tree_file, workspace_file, chosen_folder):
    """
    Generates a Flame workspace JSON file from a directory structure analysis file.

    Args:
        filesystem_tree_file (str): Path to the JSON file containing the directory analysis.
        workspace_file (str): Path to write the output workspace JSON file.
        chosen_folder (str): The path to the chosen folder template.
    """
    logging.info("--- Starting directory_structure_to_workspace ---")
    logging.info(f"Attempting to generate workspace for template: {os.path.basename(chosen_folder)}")
    logging.info(f"Reading analysis data from: {filesystem_tree_file}")
    logging.info(f"Target output file: {workspace_file}")

    try:
        with open(filesystem_tree_file, 'r', encoding='utf-8') as f:
            data = json.load(f)
        logging.info("Successfully read and parsed analysis data.")
    except (IOError, json.JSONDecodeError) as e:
        logging.error(f"CRITICAL: Could not read or parse analysis file {filesystem_tree_file}. Error: {e}")
        return

    template_name = os.path.basename(chosen_folder)
    
    workspace = [
        {
            "type": "library",
            "name": f"{template_name} Library",
            "expanded": True,
            "children": []
        }
    ]

    library_children = workspace[0]["children"]
    folders = {}

    subdirectories = data.get("subdirectories", [])
    if not subdirectories:
        logging.warning("Analysis data contains no subdirectories. The workspace file will be minimal.")

    # First pass: create folders for top-level directories
    logging.info("First pass: Creating folders for top-level directories (depth == 1).")
    for item in subdirectories:
        if item.get("depth") == 1:
            folder_name = item.get("name")
            if not folder_name:
                logging.warning(f"Found item with depth 1 but no name: {item}")
                continue
            
            folder = {
                "type": "folder",
                "name": folder_name,
                "children": []
            }
            library_children.append(folder)
            folders[folder_name] = folder
            logging.info(f"  + Created folder: '{folder_name}'")

    # Second pass: create reels for second-level directories
    logging.info("Second pass: Creating reels for nested directories (depth == 2).")
    for item in subdirectories:
        if item.get("depth") == 2:
            reel_name = item.get("name")
            parent_name = item.get("parent")

            if not reel_name or not parent_name:
                logging.warning(f"Found item with depth 2 but missing name or parent: {item}")
                continue

            if parent_name in folders:
                reel = {
                    "type": "reel",
                    "name": reel_name
                }
                folders[parent_name]["children"].append(reel)
                logging.info(f"  + Created reel: '{reel_name}' inside folder: '{parent_name}'")
            else:
                logging.warning(f"Found reel '{reel_name}' but its parent folder '{parent_name}' was not created.")

    logging.info(f"Final workspace structure generated.")

    try:
        # Ensure the parent directory exists
        output_dir = os.path.dirname(workspace_file)
        if not os.path.exists(output_dir):
            logging.info(f"Output directory does not exist. Creating: {output_dir}")
            os.makedirs(output_dir)

        with open(workspace_file, 'w', encoding='utf-8') as f:
            json.dump(workspace, f, indent=2, ensure_ascii=False)
        logging.info(f"SUCCESS: Flame workspace file created at: {workspace_file}")
    except IOError as e:
        logging.error(f"CRITICAL: Could not write to output file {workspace_file}. Error: {e}")
    except Exception as e:
        logging.error(f"An unexpected error occurred during file writing: {e}")

    logging.info("--- Finished directory_structure_to_workspace ---")
