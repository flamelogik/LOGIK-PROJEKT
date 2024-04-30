#!/bin/bash

# -------------------------------------------------------------------------- #

# File Name:        function_22-sync_python.sh
# Version:          2.0.1
# Language:         bash script
# Flame Version:    2025.x
# Author:           Phil MAN - phil_man@mac.com
# Toolset:          MAN_MADE_MATERIAL: LOGIK-PROJEKT
# Modified:         2024-04-30
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

# Function to synchronize python scripts
sync_python_scripts() {
    # Set the source and target man_made_material python directories
    src_shared_python_dir="presets/shared/python"
    tgt_shared_python_dir="/opt/Autodesk/shared/python"

    echo -e "  synchronizing python directories.\n"

    # Remove older man_made_material python directories if they exist
    if [ -d "${tgt_shared_python_dir}/man_made_material" ]; then
        echo -e "  removing older python directories.\n"
        rm -rf "${tgt_shared_python_dir}/man_made_material"
    fi

    # Use rsync to copy the python scripts
    rsync "${sync_opts[@]}" "${src_shared_python_dir}/" "${tgt_shared_python_dir}/" | sed 's/^/  /'

    echo -e "\n  python directories synchronized."
    echo -e "\n$separator\n"
}

# ========================================================================== #
# This section defines how to handle the main script function.
# ========================================================================== #

# Call the function to synchronize MAN MADE MATERIAL python scripts
# sync_python_scripts

# Check if the script is being sourced or executed
if [[ "${BASH_SOURCE[0]}" == "${0}" ]]; then
    umask 0
    sync_python_scripts
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
