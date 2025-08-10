#!/bin/bash

# -------------------------------------------------------------------------- #
# DISCLAIMER:       This file is part of LOGIK-PROJEKT.
#                   Copyright © 2024 man-made-mekanyzms
#                   
#                   LOGIK-PROJEKT creates directories, files, scripts & tools
#                   for use with Autodesk Flame and other software.
#                   
#                   LOGIK-PROJEKT is free software.
#                   
#                   You can redistribute it and/or modify it under the terms
#                   of the GNU General Public License as published by the
#                   Free Software Foundation, either version 3 of the License,
#                   or any later version.
#                   
#                   This program is distributed in the hope that it will be
#                   useful, but WITHOUT ANY WARRANTY; without even the
#                   implied warranty of MERCHANTABILITY or FITNESS FOR A
#                   PARTICULAR PURPOSE.
#                   
#                   See the GNU General Public License for more details.
#                   
#                   You should have received a copy of the GNU General
#                   Public License along with this program.
#                   
#                   If not, see <https://www.gnu.org/licenses/>.
#                   
#                   Contact: phil_man@mac.com
# -------------------------------------------------------------------------- #

# File Name:        dummy_rsync.sh
# Version:          0.9.9
# Created:          2024-01-19
# Modified:         2024-09-07

# ========================================================================== #
# This section defines paths for the script.
# ========================================================================== #

# Define the base directory as the directory of the script being executed
base_dir="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"

# Define the log files directory
log_files_dir="$base_dir/test_logs/"

# Ensure the log files directory exists
mkdir -p "$log_files_dir"

# Define a fixed log file name (without timestamp)
log_file="$log_files_dir/rsync_log.log"

# Define the source and destination paths
source_path="$base_dir/test_src/"
destination_path="$base_dir/test_dst/"

# ========================================================================== #
# This section defines the primary functions for the script.
# ========================================================================== #

# Append a start marker with timestamp to the log file
echo -e "\n=== Rsync started at $(date +"%Y-%m-%d %H:%M:%S") ===\n" >> "$log_file"

# Run rsync with the log file option, appending to the existing log
rsync -av --log-file="$log_file" "$source_path" "$destination_path"

# Append an end marker with timestamp to the log file
echo -e "\n=== Rsync completed at $(date +"%Y-%m-%d %H:%M:%S") ===\n" >> "$log_file"

# ========================================================================== #
# C2 A9 32 30 32 34 2D 4D 41 4E 2D 4D 41 44 45 2D 4D 45 4B 41 4E 59 5A 4D 53 #
# ========================================================================== #

# Changelist:       

# -------------------------------------------------------------------------- #
# version:          0.0.1
# created:          2024-09-07 - 10:38:56
# comments:         generic rsync script for testing.
# -------------------------------------------------------------------------- #
