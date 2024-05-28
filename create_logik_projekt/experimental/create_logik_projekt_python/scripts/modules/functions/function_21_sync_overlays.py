import os
import shutil

# -------------------------------------------------------------------------- #

# File Name:        function_21-sync_overlays.sh
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

# Function to synchronize burn_metadata overlays
def sync_overlays():
    # Set the source and target directories for copying
    src_burn_metadata_dir = "presets/shared/burn_metadata"
    tgt_shared_burn_metadata_dir = "/opt/Autodesk/shared/burn_metadata"
    tgt_project_burn_metadata_dir = f"{flame_proj_dir}/burn_metadata"

    print("  synchronizing burn_metadata overlays.\n")
    
    # Set the umask to 0
    os.umask(0)

    # Use shutil to copy the shared burn_metadata overlays
    shutil.copytree(src_burn_metadata_dir, tgt_shared_burn_metadata_dir)
    print("\n  shared burn_metadata overlays synchronized.")
    print("\n$separator\n")

    # Use shutil to copy the project-specific burn_metadata overlays
    shutil.copytree(src_burn_metadata_dir, tgt_project_burn_metadata_dir)
    print("\n  project burn_metadata overlays synchronized.")
    print("\n$separator\n")

# ========================================================================== #
# This section defines how to handle the main script function.
# ========================================================================== #

# Check if the script is being sourced or executed
if __name__ == "__main__":
    # Mocking the missing variable to prevent errors
    flame_proj_dir = "mocked_flame_proj_dir"

    os.umask(0)
    sync_overlays()
