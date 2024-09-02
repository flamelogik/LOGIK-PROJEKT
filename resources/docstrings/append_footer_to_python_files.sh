#!/bin/bash

# -------------------------------------------------------------------------- #

# DISCLAIMER:       This file is part of LOGIK-PROJEKT.
#                   Copyright © 2024 man-made-mekanyzms
                
#                   LOGIK-PROJEKT creates directories, files, scripts & tools
#                   for use with Autodesk Flame and other software.

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
                
#                   Contact: phil_man@mac.com

# -------------------------------------------------------------------------- #

# File Name:        append_footer_to_python_files.sh
# Version:          0.0.1
# Created:          2024-01-19
# Modified:         2024-08-31

# ========================================================================== #
# This section defines the import statements and diresctory paths.
# ========================================================================== #

# This script appends a footer to all Python files 
# in a specified directory and its subdirectories.
# It also logs the process to a file.

# Get the directory of the running script
path_to_here="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"

# Set paths
parent_dir="$(dirname $(dirname "$path_to_here"))"
resources_dir="$parent_dir/resources"
docstrings_dir="$resources_dir/docstrings"
footer_file="$docstrings_dir/footer.txt"
footer_log="$docstrings_dir/append_footer_log.txt"
modules_dir="$parent_dir/modules"

# Ensure footer_log exists
touch "$footer_log"

# Start logging
echo "---- Starting footer append process ----" >> "$footer_log"
echo "Timestamp: $(date)" >> "$footer_log"
echo "" >> "$footer_log"

# Check if footer_file exists
if [ ! -f "$footer_file" ]; then
    echo "Error: Disclaimer file does not exist." | tee -a "$footer_log"
    exit 1
fi

# Read footer text
footer_text=$(cat "$footer_file")

# Iterate through each Python file in the directory and its subdirectories
find "$modules_dir" -type f -name "*.py" | while read -r python_file; do
    # Append footer to the Python file
    if echo "$footer_text" >> "$python_file"; then
        echo "Successfully updated: $python_file" | tee -a "$footer_log"
    else
        echo "Failed to update: $python_file" | tee -a "$footer_log"
    fi
done

# Finish logging
echo "" >> "$footer_log"
echo "---- Disclaimer append process completed ----" >> "$footer_log"
echo "Timestamp: $(date)" >> "$footer_log"

# ========================================================================== #
# C2 A9 32 30 32 34 2D 4D 41 4E 2D 4D 41 44 45 2D 4D 45 4B 41 4E 59 5A 4D 53 #
# ========================================================================== #

# Changelist:       

# -------------------------------------------------------------------------- #
# version:          0.0.1
# created:          2024-08-31 - 12:34:56
# comments:         utilities to add text to python files.
# -------------------------------------------------------------------------- #
