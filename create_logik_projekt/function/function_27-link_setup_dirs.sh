#!/bin/bash

# -------------------------------------------------------------------------- #

# filename: "function_27-link_setup_dirs.sh"

# -------------------------------------------------------------------------- #

# ========================================================================== #
# This section defines the primary functions for the script.
# ========================================================================== #

# Function to remove older symbolic links
remove_old_links() {
    # Loop through each symbolic link in the target setups directory
    for link in "$tgt_workstation_dir"/*; do
        # Check if it is a symbolic link
        if [ -L "$link" ]; then
            # Unlink the symbolic link
            unlink "$link"
            echo -e "  Symbolic link removed: $link"
        fi
    done
}

# -------------------------------------------------------------------------- #

# Function to create symbolic links for each subdir in the flame project directory
create_links() {
    # Loop through each subdir in the new source directory
    for subdir in "$flame_proj_dir"/*; do
        # Check if it is a directory
        if [ -d "$subdir" ]; then
            # Extract the subdir name
            subdir_name=$(basename "$subdir")
            
            # Create a symbolic link in the target directory
            ln -s "$subdir" "$tgt_workstation_dir/$subdir_name"
            
            echo -e "  symbolic link created for: $subdir_name"
        fi
    done
}

# ========================================================================== #
# This section defines how to handle the main script function.
# ========================================================================== #

# Check if the script is being sourced or executed
if [[ "${BASH_SOURCE[0]}" == "${0}" ]]; then
    # Call the function to remove older symbolic links
    remove_old_links

    echo -e "  Older symbolic links removed."
    echo -e "\n$separator\n"

    # Call the function to create symbolic links
    create_links

    echo -e "\n  Symbolic links created."
    echo -e "\n$separator\n"
fi

# -------------------------------------------------------------------------- #

# ========================================================================== #
# C2 A9 2D 32 30 32 34 2D 4D 41 4E 5F 4D 41 44 45 5F 4D 41 54 45 52 49 61 4C #
# ========================================================================== #
