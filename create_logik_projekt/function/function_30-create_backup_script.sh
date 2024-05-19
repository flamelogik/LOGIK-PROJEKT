#!/bin/bash

# -------------------------------------------------------------------------- #

# File Name:        function_30-create_backup_script.sh
# Version:          2.1.4
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

# Function to create backup script
create_backup_script() {

    # Set the source and target files for copying
    local src_rsync_script="presets/templates/backup_template"
    local tgt_rsync_script="$tgt_rsync_dir/backup_$name.sh"
    
    # Copy the default job backup text to a new backup shell script
    cp "$src_rsync_script" "$tgt_rsync_script"

    # Set the source and target files for copying
    local src_rsync_exclusion_list="presets/templates/exclusion_list.txt"
    local tgt_rsync_exclusion_list="$tgt_rsync_dir/exclusion_list.txt"
    
    # Copy the default job backup text to a new backup shell script
    cp "$src_rsync_exclusion_list" "$tgt_rsync_exclusion_list"

    # Add execution permissions to new backup shell script
    chmod +x "$tgt_rsync_script"

    # Set the search and replace strings
    local search_replace=(
        "BackupScriptName:backup_$name.sh"
        "BackupScriptProjekt:$nickname"
        "ScriptCreationDate:$NOW"
        "LogikProjektClient:$client"
        "LogikProjektCampaign:$campaign"
        "LogikProjektName:$nickname"
        "FlameSoftwareVersion:$max_sanitized_sw_ver"
        "FlameWorkstationName:$workstation_name"
    )

    # Use sed to replace the strings in the backup script
    if [ "$operating_system" == "Linux" ]; then
        # sed_command='sed -i'
        for pair in "${search_replace[@]}"; do
            IFS=':' read -r search replace <<< "$pair"
            sed -i "s|$search|$replace|g" "$tgt_rsync_script"
        done
    elif [ "$operating_system" == "macOS" ]; then
        # sed_command='sed -i '''
        for pair in "${search_replace[@]}"; do
            IFS=':' read -r search replace <<< "$pair"
            sed -i '' "s|$search|$replace|g" "$tgt_rsync_script"
        done
    else
        echo "Unsupported operating system."
        return 1
    fi

    echo -e "  logik projekt backup script created:\n"
    echo -e "  $(basename "$tgt_rsync_script")"
    echo -e "\n$separator\n"
    
}

# ========================================================================== #
# This section defines how to handle the main script function.
# ========================================================================== #

# Check if the script is being sourced or executed
if [[ "${BASH_SOURCE[0]}" == "${0}" ]]; then
    create_backup_script "$src_rsync_script" "$tgt_rsync_script"
fi

# -------------------------------------------------------------------------- #

# ========================================================================== #
# C2 A9 32 30 32 34 2D 4D 41 4E 5F 4D 41 44 45 2D 4D 45 4B 41 4E 49 53 4D 5A #
# ========================================================================== #

# -------------------------------------------------------------------------- #

# Disclaimer:       This program is free software.

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
