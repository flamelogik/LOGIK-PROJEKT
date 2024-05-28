import os
import shutil

# -------------------------------------------------------------------------- #

# File Name:        function_25-sync_col_transforms.sh
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

# Function to synchronize color management transforms
def sync_color_transforms():
    # Set the source parent directory
    src_transforms_dir = "presets/Syncolor/transforms"

    # Set the target parent directory based on the operating system
    if operating_system == "Linux":
        tgt_synergy_dir = "/opt/Autodesk/Synergy"
        tgt_transforms_dir = os.path.join(tgt_synergy_dir, "SynColor/Shared/transforms")
    elif operating_system == "macOS":
        tgt_synergy_dir = "/Applications/Autodesk/Synergy"
        tgt_transforms_dir = os.path.join(tgt_synergy_dir, "SynColor/Shared/transforms")
    else:
        print("unsupported operating system.")
        return

    print("  synchronizing Syncolor transforms directories.\n")
    
    # Set the umask to 0
    os.umask(0)

    # Use shutil to copy the transforms
    shutil.copytree(src_transforms_dir, tgt_transforms_dir)

    print("\n  Syncolor transforms directories synchronized.")
    print("\n$separator\n")

# ========================================================================== #
# This section defines how to handle the main script function.
# ========================================================================== #

# Check if the script is being sourced or executed
if __name__ == "__main__":
    operating_system = "Linux"  # or "macOS"
    umask = 0
    sync_color_transforms()
