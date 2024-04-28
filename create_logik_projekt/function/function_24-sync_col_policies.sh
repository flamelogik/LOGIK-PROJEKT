#!/bin/bash

# -------------------------------------------------------------------------- #

# filename: "function_24-sync_col_policies.sh"

# -------------------------------------------------------------------------- #

# ========================================================================== #
# This section defines the primary functions for the script.
# ========================================================================== #

# Function to synchronize color management policies
sync_color_policies() {
    # Set the source parent directory
    local src_policies_dir="presets/Syncolor/policies"

    # Set the target parent directory based on the operating system
    if [ "$operating_system" == "Linux" ]; then
        local tgt_synergy_dir="/opt/Autodesk/Synergy"
        local tgt_policies_dir="$tgt_synergy_dir/SynColor/Shared/policies"
    elif [ "$operating_system" == "macOS" ]; then
        local tgt_synergy_dir="/Applications/Autodesk/Synergy"
        local tgt_policies_dir="$tgt_synergy_dir/SynColor/Shared/policies"
    else
        echo "unsupported operating system."
        return 1
    fi

    echo -e "  synchronizing Syncolor policies directories.\n"

    # Use rsync to copy the policies
    rsync "${sync_opts[@]}" "${src_policies_dir}/" "${tgt_policies_dir}/" | sed 's/^/  /'

    echo -e "\n  Syncolor policies directories synchronized."
    echo -e "\n$separator\n"
}

# ========================================================================== #
# This section defines how to handle the main script function.
# ========================================================================== #

# Call the function to synchronize color management policies
# sync_color_policies

# Check if the script is being sourced or executed
if [[ "${BASH_SOURCE[0]}" == "${0}" ]]; then
    sync_color_policies
fi

# -------------------------------------------------------------------------- #

# ========================================================================== #
# C2 A9 2D 32 30 32 34 2D 4D 41 4E 5F 4D 41 44 45 5F 4D 41 54 45 52 49 61 4C #
# ========================================================================== #