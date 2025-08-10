import flame


def create_reel(parent_container, reel_name):
    """
    Creates a new Reel with the given name in the specified parent container.
    The parent_container can be a Library, ReelGroup, or Desktop object.

    Args:
        parent_container (
            flame.PyLibrary or flame.PyReelGroup or flame.PyDesktop
        ): The parent container object where the reel will be created.
        reel_name (str):
            The name of the reel to create.

    Returns:
        flame.PyReel or None: 
            The created PyReel object if successful, otherwise None.

    Known PyReel Attributes and Methods:
        Attributes:
            .name (str):
                The name of the reel.
            .uid (str):
                The unique identifier of the reel.
            .token_name (str):
                The tokenized name of the reel.
            .expanded (bool):
                The expanded state in the Media Panel.
            .colour (tuple):
                The RGB color of the reel.
            .colour_label (str):
                The color label string.
            .selected (bool):
                Whether the reel is selected in the Media Panel.
            .tags (list):
                A list of strings representing tags.
            .children (list):
                List of immediate children PyObjects (clips, sequences).
            .clips (list):
                List of PyClip objects that are immediate children.
            .sequences (list):
                List of PySequence objects that are immediate children.
            .type (str):
                The Reel type (
                    e.g., "Reel", "Schematic", "Sequences", "Shelf"
                ).

        Methods:
            .clear(confirm=True) -> bool:
                Clears the Reel's content.
            .create_sequence(...) -> flame.PySequence:
                Creates a Sequence in the Reel.
            .save() -> bool:
                Saves the Reel to the defined save destination.
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
            print(
                f"Reel '{new_reel.name.get_value()}' created "
                f"successfully."
            )

            # Example Usage of PyReel Attributes and Methods:
            print(
                f"\n--- PyReel Object Details for "
                f"'{new_reel.name.get_value()}' ---"
            )
            print(
                f"UID: {new_reel.uid.get_value()}"
            )
            print(
                f"Type: {new_reel.type.get_value()}"
            )
            print(
                f"Children count: {len(new_reel.children)}"
            )

            # Example of calling a method: Create a sequence in the reel

            # try:
            #     new_sequence = (
            #         new_reel.create_sequence("MyNewSequence")
            #     )
            #     if new_sequence:
            #         print(
            #             f"Created sequence "
            #             f"'{new_sequence.name.get_value()}' "
            #             f"inside '{new_reel.name.get_value()}'."
            #         )
            # except Exception as e:
            #     print(
            #         f"Error creating sequence in reel: {e}"
            #     )

            # Example of clearing reel contents (use with caution!)

            # if new_reel.children:
            #     print(
            #         f"\nClearing contents of "
            #         f"'{new_reel.name.get_value()}'..."
            #     )
            #     if new_reel.clear(confirm=False):  # Set confirm=False
            #         print(
            #             f"Contents of '{new_reel.name.get_value()}' "
            #             f"cleared."
            #         )
            #     else:
            #         print(
            #             f"Failed to clear contents of "
            #             f"'{new_reel.name.get_value()}'."
            #         )

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


if __name__ == '__main__':
    # Example usage (requires Flame to be running with a project open):

    # current_project = (
    #     flame.projects.current_project
    # )
    # if current_project:
    #     current_workspace = (
    #         current_project.current_workspace
    #     )
    #     if current_workspace:
    #         my_desktop = (
    #             current_workspace.desktop
    #         )
    #         # Assuming a desktop exists and is accessible
    #         new_reel = (
    #             create_reel(my_desktop, "MyNewReel")
    #         )
    #         if new_reel:
    #             print(
    #                 f"Successfully created: "
    #                 f"{new_reel.name.get_value()}"
    #             )

    pass
