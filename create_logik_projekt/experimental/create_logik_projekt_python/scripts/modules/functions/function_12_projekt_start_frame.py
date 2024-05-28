import os

# -------------------------------------------------------------------------- #

# File Name:        function_12-projekt_start_frame.py
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
default_start_frame = ""

# -------------------------------------------------------------------------- #

# Function to validate user input for start frame
def validate_start_frame_choice(choice):
    """
    Validate user input for start frame choice.
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

# Function to gather project start frame information
def gather_projekt_start_frame():
    """
    Gather project start frame information.
    """
    global default_start_frame

    # Check if $has_projekt_setup_template is true
    if has_projekt_setup_template:

        # Read $projekt_setup_template
        if os.path.isfile(projekt_setup_template):

            # Read the value from projekt_setup_template
            with open(projekt_setup_template, 'r') as f:
                lines = f.readlines()
                default_start_frame = lines[7].split(': ')[1].strip()

        else:
            print(f"Error: {projekt_setup_template} not found.")
            exit(1)

    else:
        # Set the default_start_frame
        default_start_frame = "1001"

    # Display the project start frame
    print("  start frame:         ", default_start_frame)
    print("\n$separator\n")

    # Write the project information into the projekt_setup_file
    with open(projekt_setup_file, 'a') as f:
        f.write(f"start frame: {default_start_frame}\n")

    # Write the information into the projekt_setup_template
    with open(projekt_setup_template, 'a') as f:
        f.write(f"start frame: {default_start_frame}\n")

# ========================================================================== #
# This section defines how to handle the main script function.
# ========================================================================== #

# Check if the script is being sourced or executed
if __name__ == "__main__":
    gather_projekt_start_frame()
