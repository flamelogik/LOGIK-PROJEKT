#!/bin/bash

# -------------------------------------------------------------------------- #

# File Name:        function_25-sync_col_transforms.sh
# Version:          2.0.2
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

# Function to synchronize color management transforms
sync_color_transforms() {
    # Set the source parent directory
    src_transforms_dir="presets/Syncolor/transforms"

    # Set the target parent directory based on the operating system
    if [ "$operating_system" == "Linux" ]; then
        tgt_synergy_dir="/opt/Autodesk/Synergy"
        tgt_transforms_dir="$tgt_synergy_dir/SynColor/Shared/transforms"
    elif [ "$operating_system" == "macOS" ]; then
        tgt_synergy_dir="/Applications/Autodesk/Synergy"
        tgt_transforms_dir="$tgt_synergy_dir/SynColor/Shared/transforms"
    else
        echo "unsupported operating system."
        return 1
    fi

    echo -e "  synchronizing Syncolor transforms directories.\n"
    
    # Set the umask to 0
    umask 0

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
    umask 0
    sync_color_transforms
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
