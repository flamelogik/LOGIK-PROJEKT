#!/bin/bash

# -------------------------------------------------------------------------- #

# File Name:        function_27-link_setup_dirs.sh
# Version:          2.0.3
# Language:         bash script
# Flame Version:    2025.x
# Author:           Phil MAN - phil_man@mac.com
# Toolset:          MAN_MADE_MATERIAL: LOGIK-PROJEKT
# Modified:         2024-05-03
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

# Changelist:       
# -------------------------------------------------------------------------- #
# version:               1.0.0
# modified:              2024-04-20 - 16:20:00
# comments:              refactored monolithic program into separate functions
# -------------------------------------------------------------------------- #
# version:               2.0.0
# modified:              2024-04-29 - 11:29:27
# comments:              testing production readiness
# -------------------------------------------------------------------------- #
# version:               2.0.1
# modified:              2024-04-30 - 07:06:00
# comments:              Removed 'declare -g' statements for macOS compatibility
# -------------------------------------------------------------------------- #
# version:               2.0.2
# modified:              2024-04-30 - 12:29:07
# comments:              added 'umask 0' statements for rsync commands
# -------------------------------------------------------------------------- #
# version:               2.0.3
# modified:              2024-05-03 - 10:16:10
# comments:              Restored CamelCase keys for projekt_metadata_xml_file
