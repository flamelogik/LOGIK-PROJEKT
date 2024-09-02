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

# resources/docstrings/append_footer_to_python_files.sh

# This script appends a footer to all Python files 
# in a specified directory and its subdirectories.
# It also logs the process to a file.

# Set paths
parent_dir="/home/pman/workspace/GitHub/projekt_app"
footer_file="$parent_dir/resources/docstrings/footer.txt"
footer_log="$parent_dir/resources/docstrings/append_footer_log.txt"
python_modules="$parent_dir/modules"

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
find "$python_modules" -type f -name "*.py" | while read -r python_file; do
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