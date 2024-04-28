#!/bin/bash

# -------------------------------------------------------------------------- #

# filename: "function_23-sync_io.sh"

# -------------------------------------------------------------------------- #

# ========================================================================== #
# This section defines the primary functions for the script.
# ========================================================================== #

# Function to synchronize export and import presets
sync_io_presets() {
    # Set the source and target export presets directories
    local src_shared_export_presets_dir="presets/shared/export/presets"
    local tgt_shared_export_presets_dir="/opt/Autodesk/shared/export/presets"
    local tgt_project_export_presets_dir="$flame_proj_dir/export/presets"

    echo -e "  synchronizing project export presets directories.\n"

    # Use rsync to copy the export presets to the project directory
    rsync "${sync_opts[@]}" "${src_shared_export_presets_dir}/" "${tgt_project_export_presets_dir}/" | sed 's/^/  /'

    echo -e "\n  Project export presets directories synchronized."
    echo -e "\n$separator\n"

    # Set the source and target import presets directories
    local src_shared_import_presets_dir="presets/shared/import"
    local tgt_shared_import_presets_dir="/opt/Autodesk/shared/import"
    local tgt_project_import_presets_dir="$flame_proj_dir/import"

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
    sync_io_presets
fi

# -------------------------------------------------------------------------- #

# ========================================================================== #
# C2 A9 2D 32 30 32 34 2D 4D 41 4E 5F 4D 41 44 45 5F 4D 41 54 45 52 49 61 4C #
# ========================================================================== #