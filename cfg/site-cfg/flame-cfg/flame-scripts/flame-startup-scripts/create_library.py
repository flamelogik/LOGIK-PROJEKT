#!/usr/bin/env python3
# -------------------------------------------------------------------------- #
# Filename:     create_library.py
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
            The RGB color of the library (e.g., (0.0, 1.0, 0.0)
            for green).
        colour_label (str, optional):
            The color label string for the library.
        tags (list, optional):
            A list of strings representing tags for the library.

    Returns:
        flame.PyLibrary or None:
            The created PyLibrary object if successful, otherwise None.

    Known PyLibrary Attributes and Methods:
        Attributes:
            .name (str):
                The name of the library.
            .uid (str):
                The unique identifier of the library.
            .token_name (str):
                The tokenized name of the library.
            .expanded (bool):
                The expanded state in the Media Panel.
            .colour (tuple):
                The RGB color of the library.
            .colour_label (str):
                The color label string.
            .selected (bool):
                Whether the library is selected in the Media Panel.
            .tags (list):
                A list of strings representing tags.
            .opened (bool):
                Returns True if the Library is in the open state
                (loaded in memory).

        Methods:
            .close() -> bool:
                Closes the Library to release it from application memory.
            .open() -> bool:
                Opens a Library and loads it into application memory.
                (Libraries are created open).
            .acquire_exclusive_access() -> bool:
                Acquires exclusive access to a Shared Library.
            .release_exclusive_access() -> bool:
                Releases exclusive access to a Shared Library.
            .clear() -> bool:
                Clears the Library's contents.
            .create_folder(name: str) -> flame.PyFolder:
                Creates a Folder inside the Library.
            .create_reel(name: str) -> flame.PyReel:
                Creates a Reel inside the Library.
            .create_reel_group(name: str) -> flame.PyReelGroup:
                Creates a Reel Group inside the Library.
            .create_sequence(...) -> flame.PySequence:
                Creates a Sequence in the Library.
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
        new_library = current_workspace.create_library(library_name)

        if new_library:
            print(
                f"Library '{new_library.name.get_value()}' "
                "created successfully."
            )

            # Set optional attributes after creation
            if expanded is not None:
                new_library.expanded = expanded
            if colour is not None:
                new_library.colour = colour
            if colour_label is not None:
                new_library.colour_label = colour_label
            if tags is not None:
                new_library.tags = tags

            # Example Usage of PyLibrary Attributes and Methods:
            print(
                f"\n--- PyLibrary Object Details for "
                f"'{new_library.name.get_value()}' ---"
            )
            print(
                f"UID: {new_library.uid.get_value()}"
            )
            print(
                f"Token Name: {new_library.token_name.get_value()}"
            )
            print(
                f"Is Expanded: {new_library.expanded.get_value()}"
            )
            print(
                f"Current Color: {new_library.colour.get_value()}"
            )
            print(
                f"Color Label: {new_library.colour_label.get_value()}"
            )
            print(
                f"Is Selected: {new_library.selected.get_value()}"
            )
            print(
                f"Tags: {new_library.tags.get_value()}"
            )
            print(
                f"Is Opened (in memory): "
                f"{new_library.opened.get_value()}"
            )

            """
            Example of calling a method: Close the library

                Note: Closing a library might affect subsequent operations.

            This is just an example of method usage:

            if new_library.opened.get_value():
                print(
                    f"Attempting to close library "
                    f"'{new_library.name.get_value()}'..."
                )
                if new_library.close():
                    print(
                        f"Library '{new_library.name.get_value()}' "
                        f"successfully closed."
                    )
                else:
                    print(
                        f"Failed to close library "
                        f"'{new_library.name.get_value()}'."
                    )
            else:
                print(
                    f"Library '{new_library.name.get_value()}' "
                    f"is already closed."
                )

            Example of creating a child folder within the library

            try:
                new_folder = new_library.create_folder("MyNewFolder")
                if new_folder:
                    print(
                        f"Created folder '{new_folder.name.get_value()}' "
                        f"inside '{new_library.name.get_value()}'."
                    )
            except Exception as e:
                print(
                    f"Error creating folder in library: {e}"
                )
            """

            return new_library
        else:
            print(
                f"Failed to create library '{library_name}'. "
                f"It might already exist or there are permission issues."
            )
            return None

    except Exception as e:
        print(f"An error occurred while creating library: {e}")
        return None


if __name__ == '__main__':
    """
    Example usage (requires Flame to be running with a project open):
    library = create_library(
        "MyTestLibrary",
        expanded=True,
        colour=(1.0, 0.5, 0.0),
        tags=["WIP", "Review"]
    )
    if library:
        print(
            f"Created library with attributes: "
            f"Expanded={library.expanded.get_value()}, "
            f"Colour={library.colour.get_value()},
            Tags={library.tags.get_value()}"
        )
    """
    """
    Example of creating another library and then closing it

    library_to_close = create_library("TemporaryLibrary")

    if library_to_close and library_to_close.opened.get_value():
        print(
            f"\nAttempting to close TemporaryLibrary..."
        )
        if library_to_close.close():
                    print(
                        f"TemporaryLibrary successfully closed. "\
                        f"Opened state: {library_to_close.opened.get_value()}"
                    )
        else:
            print(
                f"Failed to close TemporaryLibrary."
            )
    """
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
