#!/bin/bash

# -------------------------------------------------------------------------- #

# filename: "function_21-sync_overlays.sh"

# -------------------------------------------------------------------------- #

# ========================================================================== #
# This section defines the primary functions for the script.
# ========================================================================== #

# Function to synchronize burn_metadata overlays
sync_overlays() {
    # Set the source and target directories for copying
    local src_burn_metadata_dir="presets/shared/burn_metadata"
    local tgt_shared_burn_metadata_dir="/opt/Autodesk/shared/burn_metadata"
    local tgt_project_burn_metadata_dir="$flame_proj_dir/burn_metadata"

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
    sync_overlays
fi

# -------------------------------------------------------------------------- #

# ========================================================================== #
# C2 A9 2D 32 30 32 34 2D 4D 41 4E 5F 4D 41 44 45 5F 4D 41 54 45 52 49 61 4C #
# ========================================================================== #