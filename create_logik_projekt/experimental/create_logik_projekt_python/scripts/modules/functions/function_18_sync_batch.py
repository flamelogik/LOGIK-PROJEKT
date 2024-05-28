import os
import sys

# -------------------------------------------------------------------------- #

# File Name:        function_18-sync_batch.sh
# Version:          2.1.5
# Language:         bash script
# Flame Version:    2025.x
# Author:           Phil MAN - phil_man@mac.com
# Toolset:          MAN_MADE_MATERIAL: LOGIK-PROJEKT
# Modified:         2024-05-18
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

# Function to create batch project bin nodes
def sync_batch_project_bins():
    # Set the source and target directories for copying
    src_batch_pref_dir = "presets/batch/pref"
    tgt_batch_pref_dir = f"{flame_proj_dir}/batch/pref"

    print("  creating batch project bin.\n")

    # Use rsync to copy nodes to the batch Projects bin
    os.system(f"rsync {' '.join(sync_opts)} {src_batch_pref_dir}/ {tgt_batch_pref_dir}/")

    print("\n  batch project bin created.")
    print("\n$separator\n")

# ========================================================================== #
# This section defines how to handle the main script function.
# ========================================================================== #

# Check if the script is being sourced or executed
if __name__ == "__main__":
    # Mocking the missing variables to prevent errors
    flame_proj_dir = "mocked_flame_proj_dir"
    sync_opts = ["-avz", "--delete"]

    sync_batch_project_bins()
