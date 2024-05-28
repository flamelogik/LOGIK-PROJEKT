#!/usr/bin/env python3

"""
File Name:        function_28-backup_logs.py
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

# Function to backup creation log
def backup_creation_log():
    """
    Backup creation log.

    Copy projekt_creation_log_file to flame_proj_dir/cfg.
    Move projekt_creation_log_file to tgt_configs_workstation_dir.
    """
    shutil.copy(projekt_creation_log_file, os.path.join(flame_proj_dir, "cfg"))
    shutil.move(projekt_creation_log_file, tgt_configs_workstation_dir)
    print("  logik projekt creation log backed up to config directory:\n")
    print("  {}".format(os.path.basename(projekt_creation_log_file)))
    print("\n{}\n".format(separator))

# Function to backup logik projekt metadata XML
def backup_projekt_xml():
    """
    Backup logik projekt metadata XML.

    Copy projekt_metadata_xml_file to flame_proj_dir/cfg.
    Move projekt_metadata_xml_file to tgt_configs_workstation_dir.
    """
    shutil.copy(projekt_metadata_xml_file, os.path.join(flame_proj_dir, "cfg"))
    shutil.move(projekt_metadata_xml_file, tgt_configs_workstation_dir)
    print("  logik projekt metadata xml backed up to config directory:\n")
    print("  {}".format(os.path.basename(projekt_metadata_xml_file)))
    print("\n{}\n".format(separator))

# Function to backup logik projekt setup file
def backup_projekt_setup_file():
    """
    Backup logik projekt setup file.

    Copy logik projekt_setup files to flame_proj_dir/cfg.
    Move logik projekt_setup file to tgt_configs_workstation_dir.
    """
    shutil.copy(projekt_setup_file, os.path.join(flame_proj_dir, "cfg"))
    shutil.move(projekt_setup_file, tgt_configs_workstation_dir)
    print("  logik projekt setup file backed up to config directory:\n")
    print("  {}".format(os.path.basename(projekt_setup_file)))
    print("\n{}\n".format(separator))

# Function to backup logik projekt setup template
def backup_projekt_setup_template():
    """
    Backup logik projekt setup template.

    Copy logik projekt_setup template to flame_proj_dir/cfg.
    Move logik projekt_setup template to tgt_configs_dir.
    """
    shutil.copy(projekt_setup_template, os.path.join(flame_proj_dir, "cfg"))
    shutil.move(projekt_setup_template, tgt_configs_dir)
    print("  logik projekt setup template backed up to config directory:\n")
    print("  {}".format(os.path.basename(projekt_setup_template)))
    print("\n{}\n".format(separator))

# Check if the script is being sourced or executed
if __name__ == "__main__":
    backup_creation_log()
    backup_projekt_xml()
    backup_projekt_setup_file()
    backup_projekt_setup_template()
