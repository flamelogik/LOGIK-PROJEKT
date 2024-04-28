#!/bin/bash

# -------------------------------------------------------------------------- #

# filename: "function_25-sync_col_transforms.sh"

# -------------------------------------------------------------------------- #

# ========================================================================== #
# This section defines the primary functions for the script.
# ========================================================================== #

# Function to synchronize color management transforms
sync_color_transforms() {
    # Set the source parent directory
    local src_transforms_dir="presets/Syncolor/transforms"

    # Set the target parent directory based on the operating system
    if [ "$operating_system" == "Linux" ]; then
        local tgt_synergy_dir="/opt/Autodesk/Synergy"
        local tgt_transforms_dir="$tgt_synergy_dir/SynColor/Shared/transforms"
    elif [ "$operating_system" == "macOS" ]; then
        local tgt_synergy_dir="/Applications/Autodesk/Synergy"
        local tgt_transforms_dir="$tgt_synergy_dir/SynColor/Shared/transforms"
    else
        echo "unsupported operating system."
        return 1
    fi

    echo -e "  synchronizing Syncolor transforms directories.\n"

    # Use rsync to copy the transforms
    rsync "${sync_opts[@]}" "${src_transforms_dir}/" "${tgt_transforms_dir}/" | sed 's/^/  /'

    echo -e "\n  Syncolor transforms directories synchronized."
    echo -e "\n$separator\n"
}

# ========================================================================== #
# This section defines how to handle the main script function.
# ========================================================================== #

# Call the function to synchronize color management transforms
# sync_color_transforms

# Check if the script is being sourced or executed
if [[ "${BASH_SOURCE[0]}" == "${0}" ]]; then
    sync_color_transforms
fi

# -------------------------------------------------------------------------- #

# ========================================================================== #
# C2 A9 2D 32 30 32 34 2D 4D 41 4E 5F 4D 41 44 45 5F 4D 41 54 45 52 49 61 4C #
# ========================================================================== #