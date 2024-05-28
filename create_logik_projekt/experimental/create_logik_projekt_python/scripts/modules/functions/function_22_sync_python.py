import os
import shutil

# -------------------------------------------------------------------------- #

# File Name:        function_22-sync_python.sh
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

# Function to synchronize python scripts
def sync_python_scripts():
    # Set the source and target man_made_material python directories
    src_shared_python_dir = "presets/shared/python"
    tgt_shared_python_dir = "/opt/Autodesk/shared/python"

    print("  synchronizing python directories.\n")

    # Set the umask to 0
    os.umask(0)

    # Remove older man_made_material python directories if they exist
    if os.path.isdir(os.path.join(tgt_shared_python_dir, "man_made_material")):
        print("  removing older python directories.\n")
        shutil.rmtree(os.path.join(tgt_shared_python_dir, "man_made_material"))

    # Use shutil to copy the python scripts
    shutil.copytree(src_shared_python_dir, tgt_shared_python_dir)
    print("\n  python directories synchronized.")
    print("\n$separator\n")

# ========================================================================== #
# This section defines how to handle the main script function.
# ========================================================================== #

# Check if the script is being sourced or executed
if __name__ == "__main__":
    os.umask(0)
    sync_python_scripts()
