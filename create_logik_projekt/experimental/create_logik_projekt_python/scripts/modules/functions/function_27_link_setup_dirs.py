import os

# -------------------------------------------------------------------------- #

# File Name:        function_27-link_setup_dirs.sh
# Version:          2.1.5
# Language:         bash script
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
# This section defines the primary functions for the script.
# ========================================================================== #

# Function to remove older symbolic links
def remove_old_links():
    # Loop through each symbolic link in the target setups directory
    for link in os.listdir(tgt_workstation_dir):
        # Check if it is a symbolic link
        if os.path.islink(link):
            # Unlink the symbolic link
            os.unlink(os.path.join(tgt_workstation_dir, link))
            print(f"  Symbolic link removed: {link}")

# -------------------------------------------------------------------------- #

# Function to create symbolic links for each subdir in the flame project directory
def create_links():
    # Loop through each subdir in the new source directory
    for subdir in os.listdir(flame_proj_dir):
        subdir_path = os.path.join(flame_proj_dir, subdir)
        # Check if it is a directory
        if os.path.isdir(subdir_path):
            # Create a symbolic link in the target directory
            os.symlink(subdir_path, os.path.join(tgt_workstation_dir, subdir))
            print(f"  Symbolic link created for: {subdir}")

# ========================================================================== #
# This section defines how to handle the main script function.
# ========================================================================== #

# Check if the script is being sourced or executed
if __name__ == "__main__":
    # Call the function to remove older symbolic links
    remove_old_links()

    print("  Older symbolic links removed.")
    print("\n$separator\n")

    # Call the function to create symbolic links
    create_links()

    print("\n  Symbolic links created.")
    print("\n$separator\n")
