#!/bin/bash

# -------------------------------------------------------------------------- #

# filename: "function_18-sync_batch.sh"

# -------------------------------------------------------------------------- #

# ========================================================================== #
# This section defines the primary functions for the script.
# ========================================================================== #

# Function to create batch project bin nodes
sync_batch_project_bins() {
    # Set the umask to 0
    umask 0

    # Set the source and target directories for copying
    local src_batch_pref_dir="presets/batch/pref"
    local tgt_batch_pref_dir="$flame_proj_dir/batch/pref"

    echo -e "  creating batch project bin.\n"

    # Use rsync to copy nodes to the batch Projects bin
    rsync \
        "${sync_opts[@]}" \
        "${src_batch_pref_dir}/" \
        "${tgt_batch_pref_dir}/" \
        | sed 's/^/  /'

    echo -e "\n  batch project bin created."
    echo -e "\n$separator\n"
}

# ========================================================================== #
# This section defines how to handle the main script function.
# ========================================================================== #

# Call the function to create batch project bins
# sync_batch_project_bins

# Check if the script is being sourced or executed
if [[ "${BASH_SOURCE[0]}" == "${0}" ]]; then
    sync_batch_project_bins
fi

# -------------------------------------------------------------------------- #

# ========================================================================== #
# C2 A9 2D 32 30 32 34 2D 4D 41 4E 5F 4D 41 44 45 5F 4D 41 54 45 52 49 61 4C #
# ========================================================================== #