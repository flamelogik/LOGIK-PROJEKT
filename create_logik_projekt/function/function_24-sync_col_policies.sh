#!/bin/bash

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
sync_color_policies() {
    # Set the source parent directory
    src_policies_dir="presets/Syncolor/policies"

    # Set the target parent directory based on the operating system
    if [ "$operating_system" == "Linux" ]; then
        tgt_synergy_dir="/opt/Autodesk/Synergy"
        tgt_policies_dir="$tgt_synergy_dir/SynColor/Shared/policies"
    elif [ "$operating_system" == "macOS" ]; then
        tgt_synergy_dir="/Applications/Autodesk/Synergy"
        tgt_policies_dir="$tgt_synergy_dir/SynColor/Shared/policies"
    else
        echo "unsupported operating system."
        return 1
    fi

    echo -e "  synchronizing Syncolor policies directories.\n"

    # Set the umask to 0
    umask 0

    # Use rsync to copy the policies
    rsync "${sync_opts[@]}" "${src_policies_dir}/" "${tgt_policies_dir}/" | sed 's/^/  /'

    echo -e "\n  Syncolor policies directories synchronized."
    echo -e "\n$separator\n"
}

# ========================================================================== #
# This section defines how to handle the main script function.
# ========================================================================== #

# Call the function to synchronize color management policies
# sync_color_policies

# Check if the script is being sourced or executed
if [[ "${BASH_SOURCE[0]}" == "${0}" ]]; then
    umask 0
    sync_color_policies
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
# modified:              2024-05-18 - 18:45:00
# comments:              Minor modification to Disclaimer.
