#!/usr/bin/env python3

"""
File Name:        function_29-create_archive_script.py
Version:          2.1.5
Language:         Python 3
Flame Version:    2025.x
Author:           Phil MAN - phil_man@mac.com
Toolset:          MAN_MADE_MATERIAL: LOGIK-PROJEKT
Modified:         2024-05-18
Modifier:         Phil MAN - phil_man@mac.com

Description:      This program contains function(s) that are used to
                  create new logik projekts.

Installation:     Copy the 'LOGIK-PROJEKT' repo to your GitHub directory,
                  e.g. '/home/$USER/workspace/GitHub'

Changelist:       The full changelist is at the end of this document.
"""

import os
import shutil
import datetime

# Function to create archive script
def create_archive_script():
    """
    Create archive script.

    Copies the default archive text to a new archiving shell script.
    Adds execution permissions to the new archiving shell script.
    Replaces placeholders in the shell script with actual values.
    """
    src_flame_archive_script = "presets/templates/archive_template"
    tgt_flame_archive_script = os.path.join(tgt_flame_archives_dir, name + ".sh")

    # Copy the default archive text to a new archiving shell script
    shutil.copy(src_flame_archive_script, tgt_flame_archive_script)

    # Add execution permissions to new archiving shell script
    os.chmod(tgt_flame_archive_script, 0o755)

    # Set the search and replace strings
    search_replace = [
        ("ArchiveScriptName", name + ".sh"),
        ("ArchiveScriptProjekt", name),
        ("ScriptCreationDate", str(datetime.datetime.now())),
        ("LogikProjektClient", client),
        ("LogikProjektCampaign", campaign),
        ("LogikProjektName", nickname),
        ("FlameSoftwareVersion", max_sanitized_sw_ver),
        ("FlameWorkstationName", workstation_name)
    ]

    # Use sed to replace the strings in the shell script
    if operating_system == "Linux":
        sed_command = "sed -i"
    elif operating_system == "macOS":
        sed_command = "sed -i ''"
    else:
        print("Unsupported operating system.")
        return 1

    for search, replace in search_replace:
        os.system(f"{sed_command} 's|{search}|{replace}|g' {tgt_flame_archive_script}")

    print("  logik projekt flame archive script created:\n")
    print(f"  {os.path.basename(tgt_flame_archive_script)}")
    print(f"\n{separator}\n")

# Check if the script is being sourced or executed
if __name__ == "__main__":
    create_archive_script()
