#!/usr/bin/env python3
# -------------------------------------------------------------------------- #
# Filename:     create_folder.py
# Purpose:      
# Description:  

# Author:       phil_man@mac.com
# Copyright:    Copyright (c) 2025
# Disclaimer:   Disclaimer at bottom of script.
# License:      GNU General Public License v3.0 (GPL-3.0).
#               https://www.gnu.org/licenses/gpl-3.0.en.html

# Version:      2026.1.0
# Status:       Development
# Type:         Application
# Created:      2025-07-01
# Modified:     2025-10-07

# Changelog:    Changelog at bottom of script.
# -------------------------------------------------------------------------- #


import flame


def create_folder(parent_container, folder_name):
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

    Known PyFolder Attributes and Methods:
        Attributes:
            .name (str):
                The name of the folder.
            .uid (str):
                The unique identifier of the folder.
            .token_name (str):
                The tokenized name of the folder.
            .expanded (bool):
                The expanded state in the Media Panel.
            .colour (tuple):
                The RGB color of the folder.
            .colour_label (str):
                The color label string.
            .selected (bool):
                Whether folder is selected in the Media Panel.
            .tags (list):
                A list of strings representing tags.
            .batch_groups (list):
                List of PyBatch objects that are children.
            .batch_iterations (list):
                List of PyBatchIteration objects that are children.
            .children (list):
                List of immediate children PyObjects.
            .clips (list):
                List of PyClip objects that are children.
            .desktops (list):
                List of PyDesktop objects that are children.
            .folders (list):
                List of PyFolder objects that are children.
            .reel_groups (list):
                List of PyReelGroup objects that are children.
            .reels (list):
                List of PyReel objects that are children.
            .sequences (list):
                List of PySequence objects that are children.

        Methods:
            .clear(confirm=True) -> bool:
                Clears the folder's contents.
            .create_folder(name: str) -> flame.PyFolder:
                Creates a Folder inside the Folder.
            .create_reel(name: str) -> flame.PyReel:
                Creates a Reel inside the Folder.
            .create_reel_group(name: str) -> flame.PyReelGroup:
                Creates a Reel Group inside the Folder.
            .create_sequence(...) -> flame.PySequence:
                Creates a Sequence in the Folder.
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
        new_folder = parent_container.create_folder(folder_name)

        if new_folder:
            print(
                f"Folder '{new_folder.name.get_value()}' created "
                f"successfully."
            )

            # Example Usage of PyFolder Attributes and Methods:
            print(
                f"\n--- PyFolder Object Details for "
                f"'{new_folder.name.get_value()}' ---"
            )
            print(f"UID: {new_folder.uid.get_value()}")
            print(f"Is Expanded: {new_folder.expanded.get_value()}")
            print(f"Children count: {len(new_folder.children)}")

            # Example of calling a method: Create a sub-folder

            # try:
            #     sub_folder = new_folder.create_folder("SubFolder")
            #     if sub_folder:
            #         print(
            #             f"Created sub-folder "
            #             f"'{sub_folder.name.get_value()}' "
            #             f"inside '{new_folder.name.get_value()}'."
            #         )
            # except Exception as e:
            #     print(f"Error creating sub-folder: {e}")

            # Example of clearing folder contents (use with caution!)

            # if new_folder.children:
            #     print(
            #         f"\nClearing contents of "
            #         f"'{new_folder.name.get_value()}'..."
            #     )
            #     if new_folder.clear(confirm=False):  # Set confirm=False
            #         print(
            #             f"Contents of '{new_folder.name.get_value()}' "
            #             f"cleared."
            #         )
            #     else:
            #         print(
            #             f"Failed to clear contents of "
            #             f"'{new_folder.name.get_value()}'"
            #         )

            return new_folder
        else:
            print(
                f"Failed to create folder '{folder_name}' in "
                f"'{parent_container.name.get_value()}'. It might "
                f"already exist or there are permission issues."
            )
            return None

    except Exception as e:
        print(f"An error occurred while creating folder: {e}")
        return None


if __name__ == '__main__':
    # Example usage (requires Flame to be running with a project open):

    # current_project = flame.projects.current_project
    # if current_project:
    #     current_workspace = current_project.current_workspace
    #     if current_workspace:
    #         # Assuming a library named 'MyTestLibrary' exists and is open
    #         # You might need to iterate through current_workspace.libraries
    #         # or current_workspace.desktop.children to find it.
    #         my_library = None
    #         for lib in current_workspace.libraries:
    #             if lib.name.get_value() == "MyTestLibrary":
    #                 my_library = lib
    #                 break
    #         if my_library:
    #             new_folder = create_folder(my_library, "MyNewFolder")
    #             if new_folder:
    #                 print(
    #                     f"Successfully created: "
    #                     f"{new_folder.name.get_value()}"
    #                 )
    #         else:
    #             print(
    #                 f"MyTestLibrary not found. "
    #                 f"Please create it first or adjust the example."
    #             )

    pass


# -------------------------------------------------------------------------- #

# DISCLAIMER:   This file is part of LOGIK-PROJEKT.

#               Copyright © 2025 STRENGTH IN NUMBERS

#               LOGIK-PROJEKT creates directories, files, scripts & tools
#               for use with Autodesk Flame and other software.

#               LOGIK-PROJEKT is free software.

#               You can redistribute it and/or modify it under the terms
#               of the GNU General Public License as published by the
#               Free Software Foundation, either version 3 of the License,
#               or any later version.

#               This program is distributed in the hope that it will be
#               useful, but WITHOUT ANY WARRANTY; without even the

#               implied warranty of MERCHANTABILITY or
#               FITNESS FOR A PARTICULAR PURPOSE.

#               See the GNU General Public License for more details.
#               You should have received a copy of the GNU General
#               Public License along with this program.

#               If not, see <https://www.gnu.org/licenses/gpl-3.0.en.html>.

#               Contact: phil_man@mac.com

# -------------------------------------------------------------------------- #
# C2 A9 32 30 32 35 53 54 52 45 4E 47 54 48 2D 49 4E 2D 4E 55 4D 42 45 52 53 #
# -------------------------------------------------------------------------- #
# Changelog:
# -------------------------------------------------------------------------- #
