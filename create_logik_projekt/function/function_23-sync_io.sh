#!/bin/bash

# -------------------------------------------------------------------------- #

# File Name:        function_23-sync_io.sh
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

# Function to synchronize export and import presets
sync_io_presets() {
    # Set the source and target export presets directories
    src_shared_export_presets_dir="presets/shared/export/presets"
    tgt_shared_export_presets_dir="/opt/Autodesk/shared/export/presets"
    tgt_project_export_presets_dir="$flame_proj_dir/export/presets"

    echo -e "  synchronizing project export presets directories.\n"

    # Set the umask to 0
    umask 0

    # Use rsync to copy the export presets to the project directory
    rsync "${sync_opts[@]}" "${src_shared_export_presets_dir}/" "${tgt_project_export_presets_dir}/" | sed 's/^/  /'

    echo -e "\n  Project export presets directories synchronized."
    echo -e "\n$separator\n"

    # Set the source and target import presets directories
    src_shared_import_presets_dir="presets/shared/import"
    tgt_shared_import_presets_dir="/opt/Autodesk/shared/import"
    tgt_project_import_presets_dir="$flame_proj_dir/import"

    echo -e "  synchronizing project import presets directories.\n"

    # Use rsync to copy the import presets to the project directory
    rsync "${sync_opts[@]}" "${src_shared_import_presets_dir}/" "${tgt_project_import_presets_dir}/" | sed 's/^/  /'

    echo -e "\n  project import presets directories synchronized."
    echo -e "\n$separator\n"
}

# ========================================================================== #
# This section defines how to handle the main script function.
# ========================================================================== #

# Call the function to synchronize export and import presets
# sync_io_presets

# Check if the script is being sourced or executed
if [[ "${BASH_SOURCE[0]}" == "${0}" ]]; then
    umask 0
    sync_io_presets
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
