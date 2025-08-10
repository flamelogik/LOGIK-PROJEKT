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

# Filename: replace_title_and_sanitize.sh

# Prompt the user to enter the directory containing the CMX3600.EDL files
read -p "Choose the directory containing the CMX3600.EDL files: " directory

# Verify that the provided directory exists
if [ ! -d "$directory" ]; then
    echo "Directory $directory does not exist."
    exit 1
fi

# -------------------------------------------------------------------------- #

# Function to sanitize title
sanitize_title() {
    local title="$1"
    # Convert to uppercase, replace non-alphanumeric with underscores
    title=$(echo "$title" | tr '[:lower:]' '[:upper:]' | sed 's/[^A-Z0-9]/_/g')
    # Remove consecutive underscores
    title=$(echo "$title" | sed 's/_\{2,\}/_/g')
    # Remove leading and trailing underscores
    title=$(echo "$title" | sed 's/^_//; s/_$//')
    echo "$title"
}

# -------------------------------------------------------------------------- #

# Flag to check if any .EDL or .edl files were found
found_files=false

# -------------------------------------------------------------------------- #

# Iterate over each CMX3600.EDL and .edl file in the directory
for file in "$directory"/*.EDL "$directory"/*.edl; do
    # Check if the file exists (to handle cases with no matching files)
    if [ -e "$file" ]; then
        # Set the flag to true
        found_files=true

        # Create a backup of the original file
        backup_file="${file}.orig.bak"
        cp "$file" "$backup_file"

        # Extract the filename with extension
        filename=$(basename "$file")

        # Sanitize the replacement string
        sanitized_title=$(sanitize_title "$filename")
        replacement="TITLE: $sanitized_title"

        # Extract the original first line of the file
        original_first_line=$(head -n 1 "$file")

        # Replace the first line of the file with the replacement string using sed
        sed -i "1s/.*/$replacement/" "$file"

        # Display the confirmation message
        echo "File: $file"
        echo "Backup created: $backup_file"
        echo "OLD TITLE: $original_first_line"
        echo "NEW TITLE: $replacement"
        echo "------------------------------------"
    fi
done

# -------------------------------------------------------------------------- #

# Inform the user if no .EDL or .edl files were found
if [ "$found_files" = false ]; then
    echo "No .EDL or .edl files found in $directory."
    exit 1
fi

# -------------------------------------------------------------------------- #

# ========================================================================== #
# C2 A9 32 30 32 34 2D 4D 41 4E 2D 4D 41 44 45 2D 4D 45 4B 41 4E 59 5A 4D 53 #
# ========================================================================== #

# Changelist:       

# -------------------------------------------------------------------------- #
# version:          0.0.1
# created:          2024-01-19 - 12:34:56
# comments:         scripts to create flame projekts, presets & templates.
# -------------------------------------------------------------------------- #
# version:          0.1.0
# modified:         2024-04-20 - 16:20:00
# comments:         refactored monolithic program into separate functions.
# -------------------------------------------------------------------------- #
# version:          0.5.0
# modified:         2024-05-24 - 20:24:00
# comments:         merged flame_colortoolkit with projekt.
# -------------------------------------------------------------------------- #
# version:          0.6.0
# modified:         2024-05-25 - 15:00:03
# comments:         started conversion to python3.
# -------------------------------------------------------------------------- #
# version:          0.7.0
# modified:         2024-06-21 - 18:21:03
# comments:         started gui design with pyside6.
# -------------------------------------------------------------------------- #
