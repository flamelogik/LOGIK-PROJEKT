import os
import shutil

# -------------------------------------------------------------------------- #

# File Name:        function_24-sync_col_policies.sh
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

# Function to synchronize color management policies
def sync_color_policies():
    # Set the source parent directory
    src_policies_dir = "presets/Syncolor/policies"

    # Set the target parent directory based on the operating system
    if operating_system == "Linux":
        tgt_synergy_dir = "/opt/Autodesk/Synergy"
        tgt_policies_dir = os.path.join(tgt_synergy_dir, "SynColor/Shared/policies")
    elif operating_system == "macOS":
        tgt_synergy_dir = "/Applications/Autodesk/Synergy"
        tgt_policies_dir = os.path.join(tgt_synergy_dir, "SynColor/Shared/policies")
    else:
        print("unsupported operating system.")
        return

    print("  synchronizing Syncolor policies directories.\n")

    # Set the umask to 0
    os.umask(0)

    # Use shutil to copy the policies
    shutil.copytree(src_policies_dir, tgt_policies_dir)

    print("\n  Syncolor policies directories synchronized.")
    print("\n$separator\n")

# ========================================================================== #
# This section defines how to handle the main script function.
# ========================================================================== #

# Check if the script is being sourced or executed
if __name__ == "__main__":
    operating_system = "Linux"  # or "macOS"
    umask = 0
    sync_color_policies()
