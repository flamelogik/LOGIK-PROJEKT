import flame
import json
import os

# Imports for create functions
from create_library import create_library
from create_folder import create_folder
from create_reel import create_reel

# Config file path
CONFIG_FILE_PATH = "/home/pman/workspace/GitHub/phil-man-git-hub/FLAME-API-TOOLS/src/config/layout.json"


# --- Functions from sin_menus.py ---
def hello_flame_action(selection):
    """
    A simple action that prints a message to the Flame Python Console,
    showing what was selected.
    """
    print("Hello Flame! You selected:", selection)


# --- Media Panel Scope ---
# This menu appears when you right-click on items within the Media Panel
# (e.g., Libraries, Folders, Clips, Sequences, Desktops).
def get_media_panel_custom_ui_actions():
    return [
        {
            "name": "Sin Tools",
            "actions": [
                {
                    "name": "Hello Media Panel!",
                    "execute": hello_flame_action,
                    "isVisible": True,
                    "isEnabled": True
                },
                {
                    "name": "Create Library Media Panel!",
                    "execute": create_library,
                    "isVisible": True,
                    "isEnabled": True
                }
            ]
        }
    ]


# --- Main Menu Scope ---
# This menu appears in the main Flame application menu bar
# (e.g., File, Edit, Tools).
# The exact location might vary depending on Flame version and customization.
def get_main_menu_custom_ui_actions():
    return [
        {
            "name": "Sin Tools",
            "actions": [
                {
                    "name": "Hello Main Menu!",
                    "execute": hello_flame_action,
                    "isVisible": True,
                    "isEnabled": True
                }
            ]
        }
    ]


# --- MediaHub Files Scope ---
# This menu appears when you right-click on files or folders within
# the MediaHub's Files browser.
def get_mediahub_files_custom_ui_actions():
    return [
        {
            "name": "Sin Tools",
            "actions": [
                {
                    "name": "Hello MediaHub Files!",
                    "execute": hello_flame_action,
                    "isVisible": True,
                    "isEnabled": True
                }
            ]
        }
    ]


# --- MediaHub Projects Scope ---
# the MediaHub's Projects browser.
def get_mediahub_projects_custom_ui_actions():
    return [
        {
            "name": "Sin Tools",
            "actions": [
                {
                    "name": "Hello MediaHub Projects!",
                    "execute": hello_flame_action,
                    "isVisible": True,
                    "isEnabled": True
                }
            ]
        }
    ]


# --- MediaHub Archives Scope ---
# This menu appears when you right-click on archives within
# the MediaHub's Archives browser.
def get_mediahub_archives_custom_ui_actions():
    return [
        {
            "name": "Sin Tools",
            "actions": [
                {
                    "name": "Hello MediaHub Archives!",
                    "execute": hello_flame_action,
                    "isVisible": True,
                    "isEnabled": True
                }
            ]
        }
    ]


# --- Timeline Scope ---
# This menu appears when you right-click on segments or tracks w
# ithin the Timeline.
def get_timeline_custom_ui_actions():
    return [
        {
            "name": "Sin Tools",
            "actions": [
                {
                    "name": "Hello Timeline!",
                    "execute": hello_flame_action,
                    "isVisible": True,
                    "isEnabled": True
                }
            ]
        }
    ]


# --- Batch Scope ---
# This menu appears when you right-click on nodes or the background
# within the Batch schematic.
def get_batch_custom_ui_actions():
    return [
        {
            "name": "Sin Tools",
            "actions": [
                {
                    "name": "Hello Batch!",
                    "execute": hello_flame_action,
                    "isVisible": True,
                    "isEnabled": True
                }
            ]
        }
    ]


# --- Action Scope ---
# This menu appears when you right-click on nodes or the background
# within the Action schematic.
def get_action_custom_ui_actions():
    return [
        {
            "name": "Sin Tools",
            "actions": [
                {
                    "name": "Hello Action!",
                    "execute": hello_flame_action,
                    "isVisible": True,
                    "isEnabled": True
                }
            ]
        }
    ]


# --- Original create_flame_structure_from_config from main.py ---
def create_flame_structure_from_config():
    """
    Reads 'layout.json' and creates Flame structures based on its content.
    """
    print("Starting Flame structure creation from config...")

    current_project = flame.projects.current_project
    if not current_project:
        print("Error: No Flame project is currently open. Aborting.")
        return

    current_parent_container = None # This will hold the last created container (library or folder)

    try:
        with open(CONFIG_FILE_PATH, 'r') as f:
            layout_data = json.load(f)

        if not isinstance(layout_data, list):
            print(f"Error: JSON file '{CONFIG_FILE_PATH}' does not contain a list. Aborting.")
            return

        for item in layout_data:
            item_type = item.get("type")
            item_name = item.get("name")

            if not item_type or not item_name:
                print(f"Warning: Skipping item with missing 'type' or 'name': {item}")
                continue

            if item_type == "library":
                new_container = create_library(item_name)
                if new_container:
                    current_parent_container = new_container
                else:
                    print(f"Error: Failed to create library '{item_name}'. Subsequent nested items might fail.")
                    current_parent_container = None # Reset parent if creation fails

            elif item_type == "folder":
                if current_parent_container:
                    new_container = create_folder(current_parent_container, item_name)
                    if new_container:
                        current_parent_container = new_container # Folder can also be a parent
                    else:
                        print(f"Error: Failed to create folder '{item_name}'. Subsequent nested items might fail.")
                        current_parent_container = None
                else:
                    print(f"Warning: Cannot create folder '{item_name}'. No parent container available.")

            elif item_type == "reel":
                if current_parent_container:
                    create_reel(current_parent_container, item_name)
                else:
                    print(f"Warning: Cannot create reel '{item_name}'. No parent container available.")

            else:
                print(f"Warning: Unknown item type '{item_type}' in config. Skipping.")

    except FileNotFoundError:
        print(f"Error: Config file not found at '{CONFIG_FILE_PATH}'.")
    except json.JSONDecodeError as e:
        print(f"Error: Could not decode JSON from '{CONFIG_FILE_PATH}': {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

    print("Flame structure creation from config completed.")


if __name__ == '__main__':
    create_flame_structure_from_config()
