#!/bin/bash

# -------------------------------------------------------------------------- #

# File Name:        function_21-sync_overlays.sh
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

# Function to synchronize burn_metadata overlays
sync_overlays() {
    # Set the source and target directories for copying
    src_burn_metadata_dir="presets/shared/burn_metadata"
    tgt_shared_burn_metadata_dir="/opt/Autodesk/shared/burn_metadata"
    tgt_project_burn_metadata_dir="$flame_proj_dir/burn_metadata"

    echo -e "  synchronizing burn_metadata overlays.\n"

    # Use rsync to copy the shared burn_metadata overlays
    rsync "${sync_opts[@]}" "${src_burn_metadata_dir}/" "${tgt_shared_burn_metadata_dir}/" | sed 's/^/  /'
    echo -e "\n  shared burn_metadata overlays synchronized."
    echo -e "\n$separator\n"

    # Use rsync to copy the project-specific burn_metadata overlays
    rsync "${sync_opts[@]}" "${src_burn_metadata_dir}/" "${tgt_project_burn_metadata_dir}/" | sed 's/^/  /'
    echo -e "\n  project burn_metadata overlays synchronized."
    echo -e "\n$separator\n"
}

# ========================================================================== #
# This section defines how to handle the main script function.
# ========================================================================== #

# Call the function to synchronize burn_metadata overlays
# sync_overlays

# Check if the script is being sourced or executed
if [[ "${BASH_SOURCE[0]}" == "${0}" ]]; then
    umask 0
    sync_overlays
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
