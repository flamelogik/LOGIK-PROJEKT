#!/bin/bash

# -------------------------------------------------------------------------- #

# File Name:        function_28-backup_logs.sh
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

# Function to backup creation log
backup_creation_log() {
    # Copy $projekt_creation_log_file to $flame_proj_dir/cfg.
    cp "${projekt_creation_log_file}" "${flame_proj_dir}/cfg"
    # Move $projekt_creation_log_file to $tgt_configs_workstation_dir.
    mv "${projekt_creation_log_file}" "${tgt_configs_workstation_dir}"
    echo -e "  logik projekt creation log backed up to config directory:\n"
    echo -e "  $(basename "$projekt_creation_log_file")"
    echo -e "\n$separator\n"
}

# -------------------------------------------------------------------------- #

# Function to backup logik projekt metadata XML
backup_projekt_xml() {
    # Copy $projekt_metadata_xml_file to $flame_proj_dir/cfg.
    cp "${projekt_metadata_xml_file}" "${flame_proj_dir}/cfg"
    # Move $projekt_metadata_xml_file to $tgt_configs_workstation_dir.
    mv "${projekt_metadata_xml_file}" "${tgt_configs_workstation_dir}"
    echo -e "  logik projekt metadata xml backed up to config directory:\n"
    echo -e "  $(basename "$projekt_metadata_xml_file")"
    echo -e "\n$separator\n"
}

# -------------------------------------------------------------------------- #

# Function to backup logik projekt setup file
backup_projekt_setup_file() {
    # Copy logik projekt_setup files to $flame_proj_dir/cfg.
    cp "${projekt_setup_file}" "${flame_proj_dir}/cfg"
    # Move logik projekt_setup file to $tgt_configs_workstation_dir.
    mv "${projekt_setup_file}" "${tgt_configs_workstation_dir}"
    echo -e "  logik projekt setup file backed up to config directory:\n"
    echo -e "  $(basename "$projekt_setup_file")"
    echo -e "\n$separator\n"
}

# -------------------------------------------------------------------------- #

# Function to backup logik projekt setup template
backup_projekt_setup_template() {
    # Copy logik projekt_setup template to $flame_proj_dir/cfg.
    cp "${projekt_setup_template}" "${flame_proj_dir}/cfg"
    # Move logik projekt_setup template to $tgt_configs_dir.
    mv "${projekt_setup_template}" "${tgt_configs_dir}"
    echo -e "  logik projekt setup template backed up to config directory:\n"
    echo -e "  $(basename "$projekt_setup_template")"
    echo -e "\n$separator\n"
}

# ========================================================================== #
# This section defines how to handle the main script function.
# ========================================================================== #

# Check if the script is being sourced or executed
if [[ "${BASH_SOURCE[0]}" == "${0}" ]]; then
    backup_creation_log
    backup_projekt_xml
    backup_projekt_setup_file
    backup_projekt_setup_template
fi

# -------------------------------------------------------------------------- #

# ========================================================================== #
# C2 A9 32 30 32 34 2D 4D 41 4E 5F 4D 41 44 45 2D 4D 45 4B 41 4E 49 53 4D 5A #
# ========================================================================== #

# -------------------------------------------------------------------------- #

# Disclaimer:       This program is part of LOGIK-PROJEKT.
#                   LOGIK-PROJEKT is free software.

#                   You can redistribute it and/or modify it under the terms
#                   of the GNU General Public License as published by the
#                   Free Software Foundation, either version 3 of the License,
#                   or any later version.

#                   This program is distributed in the hope that it will be
#                   useful, but WITHOUT ANY WARRANTY; without even the
#                   implied warranty of MERCHANTABILITY or FITNESS FOR A
#                   PARTICULAR PURPOSE.

#                   See the GNU General Public License for more details.

#                   You should have received a copy of the GNU General
#                   Public License along with this program.

#                   If not, see <https://www.gnu.org/licenses/>.

# -------------------------------------------------------------------------- #
# Changelist:       
# -------------------------------------------------------------------------- #
# version:               1.0.0
# modified:              2024-04-20 - 16:20:00
# comments:              refactored monolithic program into separate functions
# -------------------------------------------------------------------------- #
# version:               2.0.0
# modified:              2024-04-29 - 11:29:27
# comments:              testing production readiness
# -------------------------------------------------------------------------- #
# version:               2.0.1
# modified:              2024-04-30 - 07:06:00
# comments:              Removed 'declare -g' statements for macOS compatibility
# -------------------------------------------------------------------------- #
# version:               2.0.2
# modified:              2024-04-30 - 12:29:07
# comments:              added 'umask 0' statements for rsync commands
# -------------------------------------------------------------------------- #
# version:               2.0.3
# modified:              2024-05-03 - 10:16:10
# comments:              Restored CamelCase keys for projekt_metadata_xml_file
# -------------------------------------------------------------------------- #
# version:               2.0.4
# modified:              2024-05-03 - 10:56:34
# comments:              Restore 'jobs_dir' to /JOBS
# -------------------------------------------------------------------------- #
# version:               2.1.4
# modified:              2024-05-18 - 18:00:11
# comments:              Added GNU GPLv3 Disclaimer.
# -------------------------------------------------------------------------- #
# version:               2.1.5
# modified:              2024-05-18 - 18:45:01
# comments:              Minor modification to Disclaimer.
