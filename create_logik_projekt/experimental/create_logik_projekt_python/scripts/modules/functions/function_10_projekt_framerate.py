import os

# -------------------------------------------------------------------------- #

# File Name:        function_10-projekt_framerate.py
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
proj_fcm = ""

# -------------------------------------------------------------------------- #

# Function to validate user input
def validate_framerate_choice(choice):
    """
    Validate user input for frame rate choice.
    """
    if choice.isdigit() and 1 <= int(choice) <= 8:
        return True  # Valid choice
    else:
        print("Invalid input. Please enter a number between 1 and 8.")
        print("\n$separator\n")
        return False  # Invalid choice

# ========================================================================== #
# This section defines the primary functions for the script.
# ========================================================================== #

# Function to gather project frame rate information
def gather_projekt_framerate():
    """
    Gather project frame rate information.
    """
    global proj_fcm

    # Check if $has_projekt_setup_template is true
    if has_projekt_setup_template:

        # Read $projekt_setup_template
        if os.path.isfile(projekt_setup_template):

            # Read the value from projekt_setup_template
            with open(projekt_setup_template, 'r') as f:
                lines = f.readlines()
                proj_fcm = lines[4].split(': ')[1].strip()

        else:
            print(f"Error: {projekt_setup_template} not found.")
            exit(1)

    else:
        while True:
            # Display menu for project frame rate options
            print("  select project frame rate:\n")
            print("  1. 23.976 fps")
            print("  2. 24 fps")
            print("  3. 25 fps")
            print("  4. 29.97 fps")
            print("  5. 30 fps")
            print("  6. 50 fps")
            print("  7. 59.94 fps")
            print("  8. 60 fps\n")
            print("$separator\n")

            # Read user's choice
            choice = input("  enter your choice (1 to 8): ")
            print("\n$separator\n")

            # Validate user's choice
            if validate_framerate_choice(choice):
                break  # Break out of the loop if the choice is valid

        # Handle user's choice
        choices = {
            "1": "23.976 fps",
            "2": "24 fps",
            "3": "25 fps",
            "4": "29.97 fps",
            "5": "30 fps",
            "6": "50 fps",
            "7": "59.94 fps",
            "8": "60 fps"
        }
        proj_fcm = choices.get(choice)

    # Display the project frame rate
    print("  frame rate:          ", proj_fcm)
    print("\n$separator\n")

    # Write the project information into the projekt_setup_file
    with open(projekt_setup_file, 'a') as f:
        f.write(f"project framerate: {proj_fcm}\n")

    # Write the information into the projekt_setup_template
    with open(projekt_setup_template, 'a') as f:
        f.write(f"project framerate: {proj_fcm}\n")

# ========================================================================== #
# This section defines how to handle the main script function.
# ========================================================================== #

# Check if the script is being sourced or executed
if __name__ == "__main__":
    gather_projekt_framerate()
