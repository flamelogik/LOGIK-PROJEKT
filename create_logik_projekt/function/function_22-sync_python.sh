#!/bin/bash

# -------------------------------------------------------------------------- #

# filename: "function_22-sync_python.sh"

# -------------------------------------------------------------------------- #

# ========================================================================== #
# This section defines the primary functions for the script.
# ========================================================================== #

# Function to synchronize python scripts
sync_python_scripts() {
    # Set the source and target man_made_material python directories
    local src_shared_python_dir="presets/shared/python"
    local tgt_shared_python_dir="/opt/Autodesk/shared/python"

    echo -e "  synchronizing python directories.\n"

    # Remove older man_made_material python directories if they exist
    if [ -d "${tgt_shared_python_dir}/man_made_material" ]; then
        echo -e "  removing older python directories.\n"
        rm -rf "${tgt_shared_python_dir}/man_made_material"
    fi

    # Use rsync to copy the python scripts
    rsync "${sync_opts[@]}" "${src_shared_python_dir}/" "${tgt_shared_python_dir}/" | sed 's/^/  /'

    echo -e "\n  python directories synchronized."
    echo -e "\n$separator\n"
}

# ========================================================================== #
# This section defines how to handle the main script function.
# ========================================================================== #

# Call the function to synchronize MAN MADE MATERIAL python scripts
# sync_python_scripts

# Check if the script is being sourced or executed
if [[ "${BASH_SOURCE[0]}" == "${0}" ]]; then
    sync_python_scripts
fi

# -------------------------------------------------------------------------- #

# ========================================================================== #
# C2 A9 2D 32 30 32 34 2D 4D 41 4E 5F 4D 41 44 45 5F 4D 41 54 45 52 49 61 4C #
# ========================================================================== #