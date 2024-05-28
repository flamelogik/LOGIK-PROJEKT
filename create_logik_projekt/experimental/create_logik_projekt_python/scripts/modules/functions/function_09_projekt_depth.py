import os

# -------------------------------------------------------------------------- #

# File Name:        function_09-projekt_depth.py
# Version:          2.1.5
# Language:         Python script
# Flame Version:    2025.x
# Author:           Phil MAN - phil_man@mac.com
# Toolset:          MAN_MADE_MATERIAL: LOGIK-PROJEKT
# Modified:         2024-05-18
# Modifier:         Phil MAN - phil_man@mac.com

# Description:      This program contains function(s) that are used to
#                   create new logik projekts.

# Installation:     Copy the 'LOGIK-PROJEKT' repo to your GitHub directory,
#                   e.g. '/home/$USER/workspace/GitHub'

# Changelist:       The full changelist is at the end of this document.

# -------------------------------------------------------------------------- #

# ========================================================================== #
# This section defines global variables.
# ========================================================================== #

# Declare global variables
proj_color_depth = ""

# -------------------------------------------------------------------------- #

# Function to validate user input for bit depth
def validate_depth_choice(choice):
    """
    Validate user input for bit depth.
    """
    if choice.isdigit() and 1 <= int(choice) <= 5:
        return True  # Valid choice
    else:
        print("  invalid input. enter a number between 1 and 5.")
        print("\n$separator\n")
        return False  # Invalid choice

# ========================================================================== #
# This section defines the primary functions for the script.
# ========================================================================== #

# Function to gather projekt bit depth information
def gather_projekt_depth():
    """
    Gather project bit depth information.
    """
    global proj_color_depth

    # Check if $has_projekt_setup_template is true
    if has_projekt_setup_template:

        # Read $projekt_setup_template
        if os.path.isfile(projekt_setup_template):

            # Read the value from projekt_setup_template
            with open(projekt_setup_template, 'r') as f:
                lines = f.readlines()
                proj_color_depth = lines[3].split(': ')[1].strip()

        else:
            print(f"Error: {projekt_setup_template} not found.")
            exit(1)

    else:
        while True:
            # Prompt user for project bit depth
            print("  select project bit depth:\n")
            print("  1. 16-bit fp")
            print("  2. 32-bit fp")
            print("  3. 12-bit")
            print("  4. 10-bit")
            print("  5. 8-bit\n")
            print("$separator\n")

            # Read user's depth_choice
            depth_choice = input("  enter your choice (1 - 5): ")
            print("\n$separator\n")

            # Validate user's depth_choice
            if validate_depth_choice(depth_choice):
                break  # Break out of the loop if the choice is valid

        # Handle user's depth_choice
        choices = {
            "1": "16-bit fp",
            "2": "32-bit fp",
            "3": "12-bit",
            "4": "10-bit",
            "5": "8-bit"
        }
        proj_color_depth = choices.get(depth_choice)

    # Display the project bit depth
    print("  project depth:       ", proj_color_depth)
    print("\n$separator\n")

    # Write the project information into the projekt_setup_file
    with open(projekt_setup_file, 'a') as f:
        f.write(f"project bit-depth: {proj_color_depth}\n")

    # Write the information into the projekt_setup_template
    with open(projekt_setup_template, 'a') as f:
        f.write(f"project bit-depth: {proj_color_depth}\n")

# ========================================================================== #
# This section defines how to handle the main script function.
# ========================================================================== #

# Check if the script is being sourced or executed
if __name__ == "__main__":
    gather_projekt_depth()
