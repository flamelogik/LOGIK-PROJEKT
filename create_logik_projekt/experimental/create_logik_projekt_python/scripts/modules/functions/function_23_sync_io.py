import os
import shutil

# -------------------------------------------------------------------------- #

# File Name:        function_23-sync_io.sh
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

# Function to synchronize export and import presets
def sync_io_presets():
    # Set the source and target export presets directories
    src_shared_export_presets_dir = "presets/shared/export/presets"
    tgt_shared_export_presets_dir = "/opt/Autodesk/shared/export/presets"
    tgt_project_export_presets_dir = os.path.join(flame_proj_dir, "export/presets/flame")

    print("  synchronizing project export presets directories.\n")

    # Set the umask to 0
    os.umask(0)

    # Use shutil to copy the export presets to the project directory
    shutil.copytree(src_shared_export_presets_dir, tgt_project_export_presets_dir)
    print("\n  Project export presets directories synchronized.")
    print("\n$separator\n")

    # Set the source and target import presets directories
    src_shared_import_presets_dir = "presets/shared/import"
    tgt_shared_import_presets_dir = "/opt/Autodesk/shared/import"
    tgt_project_import_presets_dir = os.path.join(flame_proj_dir, "import")

    print("  synchronizing project import presets directories.\n")

    # Use shutil to copy the import presets to the project directory
    shutil.copytree(src_shared_import_presets_dir, tgt_project_import_presets_dir)
    print("\n  project import presets directories synchronized.")
    print("\n$separator\n")

# ========================================================================== #
# This section defines how to handle the main script function.
# ========================================================================== #

# Check if the script is being sourced or executed
if __name__ == "__main__":
    os.umask(0)
    sync_io_presets()
