import flame
import json
import os
import datetime


def modify_flame_desktop(name_template="{date}-{user}"):
    """
    Renames the current Flame desktop based on a template.
    """
    try:
        the_current_desktop = flame.projects.current_project.current_workspace.desktop
        user_nickname = flame.users.current_user.nickname
        today_date = datetime.date.today().strftime("%Y-%m-%d")
        
        new_desktop_name = name_template.replace('{date}', today_date).replace('{user}', user_nickname)
        
        the_current_desktop.name = new_desktop_name
        print(f"Current desktop renamed to: {new_desktop_name}")
    except Exception as e:
        print(f"An error occurred while renaming the desktop: {e}")


def create_batch_group(parent_container, group_name):
    """
    Creates a new Batch Group with the given name in the specified parent container.
    """
    try:
        if not parent_container:
            print("Error: Parent container is None. Cannot create batch group.")
            return None

        print(f"Attempting to create batch group '{group_name}'...")
        new_batch_group = parent_container.create_batch_group(group_name)

        if new_batch_group:
            print(f"Batch group '{new_batch_group.name.get_value()}' created successfully.")
            return new_batch_group
        else:
            print(f"Failed to create batch group '{group_name}'.")
            return None

    except Exception as e:
        print(f"An error occurred while creating batch group: {e}")
        return None


def create_library(
    library_name,
    expanded=None,
    colour=None,
    colour_label=None,
    tags=None
):
    """
    Creates a new library with the given name in the current workspace.
    Optionally sets its expanded state, color, color label, and tags.

    Args:
        library_name (str):
            The name of the library to create.
        expanded (bool, optional):
            Whether the library should be expanded in the Media Panel.
        colour (tuple, optional):
            The RGB color of the library (e.g., (0.0, 1.0, 0.0) for green).
        colour_label (str, optional):
            The color label string for the library.
        tags (list, optional):
            A list of strings representing tags for the library.

    Returns:
        flame.PyLibrary or None:
            The created PyLibrary object if successful, otherwise None.
    """
    try:
        current_project = flame.projects.current_project
        if not current_project:
            print(
                "Error: No Flame project is currently open."
            )
            return None

        current_workspace = current_project.current_workspace
        if not current_workspace:
            print(
                "Error: Could not access the current workspace."
            )
            return None

        print(
            f"Attempting to create library '{library_name}'..."
        )
        new_library = (
            current_workspace.create_library(library_name)
        )

        if new_library:
            print(
                f"Library '{new_library.name.get_value()}' "
                "created successfully."
            )

            # Set optional attributes after creation
            if expanded is not None:
                new_library.expanded = expanded
            if colour is not None:
                if isinstance(colour, list):
                    new_library.colour = tuple(colour)
                else:
                    new_library.colour = colour
            if colour_label is not None:
                new_library.colour_label = colour_label
            if tags is not None:
                new_library.tags = tags
            return new_library
        else:
            print(
                f"Failed to create library '{library_name}'. "
                f"It might already exist or there are permission issues."
            )
            return None

    except Exception as e:
        print(
            f"An error occurred while creating library: {e}"
        )
        return None


def create_folder(
        parent_container,
        folder_name
):
    """
    Creates a new folder with the given name inside the specified parent
    container. The parent_container can be a Library, Folder, or Desktop
    object.

    Args:
        parent_container (
            flame.PyLibrary or flame.PyFolder or flame.PyDesktop
        ):
            The parent container object where the folder will be created.
        folder_name (str): The name of the folder to create.

    Returns:
        flame.PyFolder or None: The created PyFolder object if successful,
        otherwise None.
    """
    try:
        if not parent_container:
            print(
                "Error: Parent container is None. Cannot create folder."
            )
            return None

        print(
            f"Attempting to create folder '{folder_name}' in "
            f"'{parent_container.name.get_value()}'..."
        )
        new_folder = (
            parent_container.create_folder(folder_name)
        )

        if new_folder:
            print(
                f"Folder '{new_folder.name.get_value()}' created "
                f"successfully."
            )
            return new_folder
        else:
            print(
                f"Failed to create folder '{folder_name}' in "
                f"'{parent_container.name.get_value()}'. It might already "
                f"exist or there are permission issues."
            )
            return None

    except Exception as e:
        print(
            f"An error occurred while creating folder: {e}"
        )
        return None


def create_reel(parent_container, reel_name, reel_type=None, colour=None):
    """
    Creates a new Reel with the given name in the specified parent container.
    The parent_container can be a Library, ReelGroup, or Desktop object.

    Args:
        parent_container (
            flame.PyLibrary or flame.PyReelGroup or flame.PyDesktop
        ): The parent container object where the reel will be created.
        reel_name (str):
            The name of the reel to create.
        reel_type (str, optional):
            The type of the reel to create (e.g., "Sequence", "Schematic").

    Returns:
        flame.PyReel or None: 
            The created PyReel object if successful, otherwise None.
    """
    try:
        if not parent_container:
            print(
                "Error: Parent container is None. Cannot create reel."
            )
            return None

        print(
            f"Attempting to create reel '{reel_name}' in "
            f"'{parent_container.name.get_value()}'..."
        )
        new_reel = (
            parent_container.create_reel(reel_name)
            )

        if new_reel:
            if reel_type:
                new_reel.attributes['Type'] = reel_type
            if colour is not None:
                if isinstance(colour, list):
                    new_reel.colour = tuple(colour)
                else:
                    new_reel.colour = colour
            print(
                f"Reel '{new_reel.name.get_value()}' created "
                f"successfully."
            )
            return new_reel
        else:
            print(
                f"Failed to create reel '{reel_name}' in "
                f"'{parent_container.name.get_value()}'. It might already "
                f"exist or there are permission issues."
            )
            return None

    except Exception as e:
        print(
            f"An error occurred while creating reel: {e}"
        )
        return None


def create_reel_group(parent_container, reel_group_name, reel_names=None, colour=None):
    """
    Creates a new Reel Group and populates it with reels.

    Args:
        parent_container (flame.PyLibrary or flame.PyFolder): The parent object.
        reel_group_name (str): The name for the new reel group.
        reel_names (list, optional): A list of names for the reels. 
                                     If not provided, three numbered reels are created.

    Returns:
        flame.PyReelGroup or None: The created reel group object.
    """
    try:
        if not parent_container:
            print("Error: Parent container is None. Cannot create reel group.")
            return None

        print(f"Attempting to create reel group '{reel_group_name}'...")
        new_reel_group = parent_container.create_reel_group(reel_group_name)

        if not new_reel_group:
            print(f"Failed to create reel group '{reel_group_name}'.")
            return None

        if colour:
            new_reel_group.colour = colour

        print(f"Reel group '{new_reel_group.name.get_value()}' created successfully.")

        # Clean up default reels created by Flame
        print("Cleaning up default reels...")
        reels_to_delete = []
        for reel in new_reel_group.reels:
            if reel.name.get_value().startswith("Reel "):
                reels_to_delete.append(reel)
        
        if reels_to_delete:
            for reel in reels_to_delete:
                print(f"  - Deleting default reel: {reel.name.get_value()}")
                flame.delete(reel)
        else:
            print("  - No default 'Reel ' prefixed reels found to delete.")

        if reel_names:
            for reel_name in reel_names:
                temp_reel = new_reel_group.create_reel("TempReel")
                if temp_reel:
                    temp_reel.name = reel_name
                    print(f"  - Created and renamed reel: {reel_name}")
                else:
                    print(f"  - Failed to create reel '{reel_name}' in group '{reel_group_name}'.")
        else:
            for i in range(1, 4):
                reel_name = f"{reel_group_name}-{i}"
                temp_reel = new_reel_group.create_reel("TempReel")
                if temp_reel:
                    temp_reel.name = reel_name
                    print(f"  - Created and renamed reel: {reel_name}")
                else:
                    print(f"  - Failed to create reel {i} in group '{reel_group_name}'.")
        
        return new_reel_group

    except Exception as e:
        print(f"An error occurred while creating reel group: {e}")
        return None


def delete_default_library():
    """
    Deletes any library named "Default Library" from the current workspace.
    """
    try:
        current_project = flame.projects.current_project
        if not current_project:
            print("Error: No Flame project is currently open. Cannot delete default library.")
            return

        current_workspace = current_project.current_workspace
        if not current_workspace:
            print("Error: Could not access the current workspace. Cannot delete default library.")
            return

        for library in list(current_workspace.libraries): # Iterate over a copy to allow deletion
            if library.name == "Default Library":
                print(f"Deleting default library: {library.name.get_value()}")
                flame.delete(library)
                print("Default Library deleted successfully.")
                return
        print("Default Library not found.")

    except Exception as e:
        print(f"An error occurred while deleting default library: {e}")


def modify_desktop_contents(desktop_contents):
    """
    Modifies the contents of the Flame desktop based on a template.
    It attempts to rename existing default items (like the "Reels" group)
    and then creates or updates other items based on exact name matches.
    """
    try:
        the_current_desktop = flame.projects.current_project.current_workspace.desktop
        today_date = datetime.date.today().strftime("%Y-%m-%d")
        user_nickname = flame.users.current_user.nickname

        # Step 1: Identify and process the default "Reels" group if it exists
        default_reels_group = next((rg for rg in the_current_desktop.reel_groups if rg.name == 'Reels'), None)
        
        # Find the first reel_group entry in the JSON that is intended to replace the default "Reels" group.
        # This is a "best guess" - assuming the first reel_group in the template is for the default.
        template_default_reel_group = None
        for item in desktop_contents:
            if item.get("type") == "reel_group":
                template_default_reel_group = item
                break

        if default_reels_group and template_default_reel_group:
            print(f"Found default 'Reels' group. Attempting to map to template: {template_default_reel_group.get('name')}")
            
            # Rename the default reel group
            new_group_name = template_default_reel_group.get("name").replace('{date}', today_date).replace('{user}', user_nickname)
            default_reels_group.name = new_group_name
            if "colour" in template_default_reel_group:
                default_reels_group.colour = tuple(template_default_reel_group["colour"])
            print(f"Renamed default 'Reels' group to '{new_group_name}' and set color.")

            # Process existing reels within the default group
            # Create a mapping from default reel names to template reel names
            template_reels = template_default_reel_group.get("reels", [])
            processed_template_reels = set() # Store the actual template reel dicts that have been processed

            for reel in list(default_reels_group.reels): # Iterate over a copy to allow deletion
                current_reel_name = reel.name.get_value()
                
                # Try to find a matching template reel for the current default reel
                matched_template_reel = None
                if current_reel_name == 'Reel 1' and len(template_reels) > 0:
                    matched_template_reel = template_reels[0]
                elif current_reel_name == 'Reel 2' and len(template_reels) > 1:
                    matched_template_reel = template_reels[1]
                elif current_reel_name == 'Sequences' and len(template_reels) > 2:
                    matched_template_reel = template_reels[2]
                
                if matched_template_reel:
                    if not isinstance(matched_template_reel, dict):
                        print(f"ERROR: Expected dictionary for reel template, but got {type(matched_template_reel)}: {matched_template_reel}")
                        continue # Skip this reel if it's not a dictionary

                    # Rename and update properties of existing default reels
                    new_reel_name = matched_template_reel["name"].replace('{date}', today_date).replace('{user}', user_nickname)
                    reel.name = new_reel_name
                    if "colour" in matched_template_reel:
                        reel.colour = tuple(matched_template_reel["colour"])
                    if "reel_type" in matched_template_reel:
                        reel.attributes['Type'] = matched_template_reel["reel_type"]
                    print(f"Renamed '{current_reel_name}' to '{new_reel_name}' and updated properties.")
                    hashable_items = []
                    for k, v in matched_template_reel.items():
                        if isinstance(v, list):
                            hashable_items.append((k, tuple(v)))
                        else:
                            hashable_items.append((k, v))
                    processed_template_reels.add(frozenset(hashable_items)) # Add immutable version to set
                else:
                    # Delete any other default reels not explicitly handled
                    print(f"Deleting unexpected default reel: {current_reel_name}")
                    flame.delete(reel)
            
            # Create additional reels from the template that were not mapped to default ones
            for reel_item in template_reels:
                # Convert list values in reel_item to tuples for hashability
                hashable_reel_item_items = []
                for k, v in reel_item.items():
                    if isinstance(v, list):
                        hashable_reel_item_items.append((k, tuple(v)))
                    else:
                        hashable_reel_item_items.append((k, v))

                if frozenset(hashable_reel_item_items) not in processed_template_reels:
                    reel_item_name = reel_item["name"].replace('{date}', today_date).replace('{user}', user_nickname)
                    create_reel(default_reels_group, reel_item_name, reel_item.get("reel_type"), reel_item.get("colour"))
                    print(f"Created additional reel: {reel_item_name}")

            # Remove the processed template_default_reel_group from desktop_contents
            # to avoid re-processing it in the next loop
            desktop_contents = [item for item in desktop_contents if item != template_default_reel_group]


        # Step 2: Process remaining items from JSON (create or update if exact name match)
        for item in desktop_contents:
            item_type = item.get("type")
            item_name_template = item.get("name")

            if not item_type or not item_name_template:
                print(f"Skipping invalid item in desktop_contents: {item}")
                continue

            item_name = item_name_template.replace('{date}', today_date).replace('{user}', user_nickname)

            existing_item = None
            if item_type == "reel_group":
                existing_item = next((rg for rg in the_current_desktop.reel_groups if rg.name == item_name), None)
            elif item_type == "batch_group":
                existing_item = next((bg for bg in the_current_desktop.batch_groups if bg.name == item_name), None)
            elif item_type == "reel":
                existing_item = next((r for r in the_current_desktop.reels if r.name == item_name), None)
            
            if existing_item:
                print(f"Item '{item_name}' of type '{item_type}' already exists. Updating properties.")
                # Update properties of existing item
                if "colour" in item:
                    existing_item.colour = tuple(item["colour"])
                if item_type == "reel" and "reel_type" in item:
                    existing_item.attributes['Type'] = item["reel_type"]
                # Add more property updates as needed (e.g., expanded for libraries, tags)
                
                # If it's a reel group, process its children (reels)
                if item_type == "reel_group" and "reels" in item:
                    for reel_item in item["reels"]:
                        if isinstance(reel_item, dict):
                            child_reel_name = reel_item["name"].replace('{date}', today_date).replace('{user}', user_nickname)
                            # Check if child reel already exists within this reel group
                            existing_child_reel = next((r for r in existing_item.reels if r.name == child_reel_name), None)
                            if existing_child_reel:
                                print(f"  Child reel '{child_reel_name}' already exists in '{item_name}'. Updating properties.")
                                if "colour" in reel_item:
                                    existing_child_reel.colour = tuple(reel_item["colour"])
                                if "reel_type" in reel_item:
                                    existing_child_reel.attributes['Type'] = reel_item["reel_type"]
                            else:
                                create_reel(existing_item, child_reel_name, reel_item.get("reel_type"), reel_item.get("colour"))
                        else:
                            print(f"Skipping invalid reel_item (not a dictionary): {reel_item}")

            else:
                print(f"Item '{item_name}' of type '{item_type}' does not exist. Creating it.")
                if item_type == "reel_group":
                    new_reel_group = create_reel_group(the_current_desktop, item_name, colour=item.get("colour"))
                    if new_reel_group and "reels" in item:
                        for reel_item in item["reels"]:
                            if isinstance(reel_item, dict):
                                reel_item_name = reel_item["name"].replace('{date}', today_date).replace('{user}', user_nickname)
                                create_reel(new_reel_group, reel_item_name, reel_item.get("reel_type"), reel_item.get("colour"))
                            else:
                                print(f"Skipping invalid reel_item (not a dictionary): {reel_item}")
                elif item_type == "batch_group":
                    create_batch_group(the_current_desktop, item_name)
                elif item_type == "reel":
                    create_reel(the_current_desktop, item_name, item.get("reel_type"), item.get("colour"))

    except Exception as e:
        print(f"An error occurred while modifying desktop contents: {e}")


def process_workspace_item(item, parent_container=None):
    """
    Recursively processes a workspace item from the template.

    Args:
        item (dict): A dictionary representing a workspace item.
        parent_container (flame object, optional): The parent container for the item. Defaults to None.
    """
    item_type = item.get("type")
    item_name = item.get("name")

    if not item_type:
        print(f"Skipping invalid item in template: {item}")
        return

    if item_type == "desktop":
        name_template = item.get("name_template", "{date}-{user}")
        modify_flame_desktop(name_template)
        return
    
    if item_type == "desktop_contents":
        modify_desktop_contents(item.get("items", []))
        return

    if not item_name:
        print(f"Skipping invalid item in template: {item}")
        return

    new_item = None
    if item_type == "library":
        new_item = create_library(
            item_name,
            expanded=item.get("expanded"),
            colour=item.get("colour"),
            colour_label=item.get("colour_label"),
            tags=item.get("tags")
        )
    elif parent_container:
        if item_type == "folder":
            new_item = create_folder(parent_container, item_name)
        elif item_type == "reel":
            new_item = create_reel(parent_container, item_name, item.get("reel_type"))
        elif item_type == "reel_group":
            new_item = create_reel_group(parent_container, item_name, item.get("reel_names"))
    else:
        print(f"Skipping item '{item_name}' of type '{item_type}' because it has no valid parent.")

    if new_item and "children" in item:
        for child_item in item["children"]:
            process_workspace_item(child_item, new_item)


def create_workspace_from_template():
    """
    Creates a Flame workspace structure from a JSON template file.
    Assumes 'flame-workspace.json' is in the same directory.
    """
    workspace_file = "flame-workspace.json"
    try:
        with open(workspace_file, 'r') as f:
            workspace_data = json.load(f)
    except FileNotFoundError:
        print(f"Error: Workspace file not found at {workspace_file}")
        return
    except json.JSONDecodeError:
        print(f"Error: Could not decode JSON from {workspace_file}")
        return

    for item in workspace_data:
        process_workspace_item(item)

    # Clean up: Delete Default Library if it still exists
    delete_default_library()


if __name__ == '__main__':
    create_workspace_from_template()
