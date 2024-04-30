#!/bin/bash

# -------------------------------------------------------------------------- #

# File Name:        function_20-sync_bookmarks.sh
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

# Function to create bookmarks for the logik project and job
sync_bookmarks() {
    # Set the source and target files for copying
    src_project_bookmarks="presets/status/cf_bookmarks.json"
    tgt_project_bookmarks="$flame_proj_dir/status/cf_bookmarks.json"
    local tgt_job_dir="/JOBS/$nickname"

    echo -e "  creating project bookmarks.\n"

    # Check if tgt_project_bookmarks exists and rename if it does
    if [ -e "$tgt_project_bookmarks" ]; then
        echo -e "  * $tgt_project_bookmarks exists\n"
        echo -e "  * Backing up older bookmarks file:\n"
        echo -e "  *   $tgt_project_bookmarks.bak"
        mv "$tgt_project_bookmarks" "$tgt_project_bookmarks.bak"
    fi

    # Copy bookmarks
    cp "$src_project_bookmarks" "$tgt_project_bookmarks"

    # Set the search and replace strings
    local search_replace=(
        "PROJECT_PRIVATEDATA_BOOKMARK:$name"
        "PROJECT_PATH_BOOKMARK:$name"
        "PROJECT_NAME_BOOKMARK:$name"
        "/JOBS/PROJECT_NAME:$tgt_job_dir"
    )

    # Use sed to replace the strings in the shell script
    if [ "$operating_system" == "Linux" ]; then
        for pair in "${search_replace[@]}"; do
            IFS=':' read -r search replace <<< "$pair"
            sed -i "s|$search|$replace|g" "$tgt_project_bookmarks"
        done
    elif [ "$operating_system" == "macOS" ]; then
        for pair in "${search_replace[@]}"; do
            IFS=':' read -r search replace <<< "$pair"
            sed -i '' "s|$search|$replace|g" "$tgt_project_bookmarks"
        done
    else
        echo "Unsupported operating system."
        return 1
    fi

    # ---------------------------------------------------------------------- #

    # # Set the search and replace strings
    # local search_string_01="/JOBS/PROJECT_NAME"
    # local replace_string_01="$tgt_job_dir"
    # local search_string_02="PROJECT_NAME_BOOKMARK"
    # local replace_string_02="$name"
    # local search_string_03="PROJECT_PATH_BOOKMARK"
    # local replace_string_03="$name"
    # local search_string_04="PROJECT_PRIVATEDATA_BOOKMARK"
    # local replace_string_04="$name"

    # # Use sed to replace the strings in the JSON file
    # if [ "$operating_system" == "Linux" ]; then
    #     sed -i "s|$search_string_01|$replace_string_01|g" \
    #         "$tgt_project_bookmarks"
    #     sed -i "s|$search_string_02|$replace_string_02|g" \
    #         "$tgt_project_bookmarks"
    #     sed -i "s|$search_string_03|$replace_string_03|g" \
    #         "$tgt_project_bookmarks"
    #     sed -i "s|$search_string_04|$replace_string_04|g" \
    #         "$tgt_project_bookmarks"
    # elif [ "$operating_system" == "macOS" ]; then
    #     sed -i '' "s|$search_string_01|$replace_string_01|g" \
    #         "$tgt_project_bookmarks"
    #     sed -i '' "s|$search_string_02|$replace_string_02|g" \
    #         "$tgt_project_bookmarks"
    #     sed -i '' "s|$search_string_03|$replace_string_03|g" \
    #         "$tgt_project_bookmarks"
    #     sed -i '' "s|$search_string_04|$replace_string_04|g" \
    #         "$tgt_project_bookmarks"
    # else
    #     echo "Unsupported operating system."
    #     return 1
    # fi

    echo -e "\n  $tgt_project_bookmarks\n"

    echo -e "\n  project bookmarks created."
    echo -e "\n$separator\n"
}

# ========================================================================== #
# This section defines how to handle the main script function.
# ========================================================================== #

# Call the function to create bookmarks
# sync_bookmarks

# Check if the script is being sourced or executed
if [[ "${BASH_SOURCE[0]}" == "${0}" ]]; then
    umask 0
    sync_bookmarks
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
