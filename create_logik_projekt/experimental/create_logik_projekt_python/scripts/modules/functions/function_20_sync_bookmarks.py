import os
import sys

# -------------------------------------------------------------------------- #

# File Name:        function_20-sync_bookmarks.sh
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

# Function to create bookmarks for the logik project and job
def sync_bookmarks():
    # Set the source and target files for copying
    src_project_bookmarks = "presets/status/cf_bookmarks.json"
    tgt_project_bookmarks = f"{flame_proj_dir}/status/cf_bookmarks.json"
    tgt_job_dir = f"/JOBS/{nickname}"

    print("  creating project bookmarks.\n")

    # Set the umask to 0
    os.umask(0)

    # Check if tgt_project_bookmarks exists and rename if it does
    if os.path.exists(tgt_project_bookmarks):
        print(f"  * {tgt_project_bookmarks} exists\n")
        print("  * Backing up older bookmarks file:\n")
        print(f"  *   {tgt_project_bookmarks}.bak")
        os.rename(tgt_project_bookmarks, f"{tgt_project_bookmarks}.bak")

    # Copy bookmarks
    shutil.copy(src_project_bookmarks, tgt_project_bookmarks)

    # Set the search and replace strings
    search_replace = [
        ("PROJECT_PRIVATEDATA_BOOKMARK:" + name, name),
        ("PROJECT_PATH_BOOKMARK:" + name, name),
        ("PROJECT_NAME_BOOKMARK:" + name, name),
        ("/JOBS/PROJECT_NAME:" + tgt_job_dir, tgt_job_dir)
    ]

    # Use sed to replace the strings in the shell script
    if operating_system == "Linux":
        for search, replace in search_replace:
            os.system(f"sed -i 's|{search}|{replace}|g' {tgt_project_bookmarks}")
    elif operating_system == "macOS":
        for search, replace in search_replace:
            os.system(f"sed -i '' 's|{search}|{replace}|g' {tgt_project_bookmarks}")
    else:
        print("Unsupported operating system.")
        return 1

    print(f"\n  {tgt_project_bookmarks}\n")

    print("\n  project bookmarks created.")
    print("\n$separator\n")

# ========================================================================== #
# This section defines how to handle the main script function.
# ========================================================================== #

# Check if the script is being sourced or executed
if __name__ == "__main__":
    # Mocking the missing variables to prevent errors
    flame_proj_dir = "mocked_flame_proj_dir"
    nickname = "mocked_nickname"
    operating_system = "Linux"

    os.umask(0)
    sync_bookmarks()
