#!/bin/bash

# -------------------------------------------------------------------------- #

# File Name:        function_29-create_archive_script.sh
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

# Function to create archive script
create_archive_script() {
    local src_flame_archive_script="presets/templates/archive_template"
    local tgt_flame_archive_script="$tgt_flame_archives_dir/$name.sh"

    # Copy the default archive text to a new archiving shell script
    cp "$src_flame_archive_script" "$tgt_flame_archive_script"

    # Add execution permissions to new archiving shell script
    chmod +x "$tgt_flame_archive_script"

    # Set the search and replace strings
    local search_replace=(
        "ArchiveScriptName:$name.sh"
        "ArchiveScriptProjekt:$name"
        "ScriptCreationDate:$NOW"
        "LogikProjektClient:$client"
        "LogikProjektCampaign:$campaign"
        "LogikProjektName:$nickname"
        "FlameSoftwareVersion:$max_sanitized_sw_ver"
        "FlameWorkstationName:$workstation_name"
    )

    # Use sed to replace the strings in the shell script
    if [ "$operating_system" == "Linux" ]; then
        for pair in "${search_replace[@]}"; do
            IFS=':' read -r search replace <<< "$pair"
            sed -i "s|$search|$replace|g" "$tgt_flame_archive_script"
        done
    elif [ "$operating_system" == "macOS" ]; then
        for pair in "${search_replace[@]}"; do
            IFS=':' read -r search replace <<< "$pair"
            sed -i '' "s|$search|$replace|g" "$tgt_flame_archive_script"
        done
    else
        echo "Unsupported operating system."
        return 1
    fi

    echo -e "  logik projekt flame archive script created:\n"
    echo -e "  $(basename "$tgt_flame_archive_script")"
    echo -e "\n$separator\n"

}

# ========================================================================== #
# This section defines how to handle the main script function.
# ========================================================================== #

# Check if the script is being sourced or executed
if [[ "${BASH_SOURCE[0]}" == "${0}" ]]; then
    create_archive_script
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
