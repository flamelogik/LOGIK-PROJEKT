import os
import sys

# -------------------------------------------------------------------------- #

# File Name:        function_19-sync_mediaimport.sh
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

# Function to create default mediaImport rules for the MediaHub
def sync_mediaImport_rules():
    # Set the source and target directories for copying
    src_mediaimport_dir = "presets/mediaImport"
    tgt_mediaimport_dir = f"{flame_proj_dir}/mediaImport"

    print("  synchronizing media import preferences & rules.\n")
    
    # Set the umask to 0
    os.umask(0)

    # Use rsync to copy the media import rules and files
    os.system(f"rsync {' '.join(sync_opts)} {src_mediaimport_dir}/ {tgt_mediaimport_dir}/")

    print("\n  media import preferences & rules synchronized.")
    print("\n$separator\n")

# ========================================================================== #
# This section defines how to handle the main script function.
# ========================================================================== #

# Check if the script is being sourced or executed
if __name__ == "__main__":
    # Mocking the missing variables to prevent errors
    flame_proj_dir = "mocked_flame_proj_dir"
    sync_opts = ["-avz", "--delete"]

    os.umask(0)
    sync_mediaImport_rules()
