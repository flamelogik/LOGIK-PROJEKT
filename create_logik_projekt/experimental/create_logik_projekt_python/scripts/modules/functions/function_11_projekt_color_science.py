import os

# -------------------------------------------------------------------------- #

# File Name:        function_11-projekt_color_science.py
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
proj_color_science = ""

# -------------------------------------------------------------------------- #

# Function to validate user input for color science
def validate_color_choice(choice):
    """
    Validate user input for color science choice.
    """
    if choice.isdigit() and 1 <= int(choice) <= 12:
        return True  # Valid choice
    else:
        print("Invalid input. Please enter a number between 1 and 12.")
        print("\n$separator\n")
        return False  # Invalid choice

# ========================================================================== #
# This section defines the primary functions for the script.
# ========================================================================== #

# Function to gather project color science information
def gather_projekt_color_science():
    """
    Gather project color science information.
    """
    global proj_color_science

    # Check if $has_projekt_setup_template is true
    if has_projekt_setup_template:

        # Read $projekt_setup_template
        if os.path.isfile(projekt_setup_template):

            # Read the value from projekt_setup_template
            with open(projekt_setup_template, 'r') as f:
                lines = f.readlines()
                proj_color_science = lines[5].split(': ')[1].strip()

        else:
            print(f"Error: {projekt_setup_template} not found.")
            exit(1)

    else:
        while True:
            # Display menu for project color science
            print("  select project color policy:\n")
            print("   1. Autodesk ACES 1.0")
            print("   2. Autodesk ACES 1.1")
            print("   3. Autodesk Legacy Workflow")
            print("   4. Autodesk Simple Linear Workflow")
            print("   5. ARRI Alexa LogC V3 (K1S1)")
            print("   6. ARRI Alexa LogC v4")
            print("   7. R3D Log3g10 Red Wide Gamut RGB (Do Not Use)")
            print("   8. Sony Cine+ 709")
            print("   9. Sony Low Contrast 709")
            print("  10. Sony Low Contrast 709 Type A (Alexa Emulation)")
            print("  11. Sony SLog2 709")
            print("  12. Apple Log (ADSK ACES 1.1)")
            print("\n$separator\n")

            # Read user's choice
            choice = input("  enter your choice (1 to 12): ")
            print("\n$separator\n")

            # Validate user's choice
            if validate_color_choice(choice):
                break  # Break out of the loop if the choice is valid

        # Handle user's choice
        choices = {
            "1": "adsk_aces_1",
            "2": "adsk_aces_11",
            "3": "adsk_legacy",
            "4": "adsk_linear",
            "5": "arri_logc_v3",
            "6": "arri_logc_v4",
            "7": "aces_11_sdr",
            "8": "sony_cine_709",
            "9": "sony_lc_709",
            "10": "sony_lca_709",
            "11": "sony_slog2_709",
            "12": "adsk_aces_11"
        }
        proj_color_science = choices.get(choice)

    # Display the project color science
    print("  color policy:        ", proj_color_science)
    print("\n$separator\n")

    # Write the project information into the projekt_setup_file
    with open(projekt_setup_file, 'a') as f:
        f.write(f"projekt color science: {proj_color_science}\n")

    # Write the information into the projekt_setup_template
    with open(projekt_setup_template, 'a') as f:
        f.write(f"projekt color science: {proj_color_science}\n")

# ========================================================================== #
# This section defines how to handle the main script function.
# ========================================================================== #

# Check if the script is being sourced or executed
if __name__ == "__main__":
    gather_projekt_color_science()
