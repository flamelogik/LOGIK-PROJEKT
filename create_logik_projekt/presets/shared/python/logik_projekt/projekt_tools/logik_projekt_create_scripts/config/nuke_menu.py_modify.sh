#!/bin/bash

# File paths
header_file="nuke_menu.py_header.txt"
imports_file="nuke_menu.py_imports.txt"
logic_file="nuke_menu.py_logic.txt"
menu_file=~/.nuke/menu.py

# Function to insert contents of a file at the beginning of another file
insert_at_beginning() {
    local file_to_insert="$1"
    local target_file="$2"
    cat "$file_to_insert" "$target_file" > "$target_file.tmp"
    mv "$target_file.tmp" "$target_file"
}

# Function to check and insert import statements
check_and_insert_imports() {
    local import_stmts_file="$1"
    local target_file="$2"
    
    while IFS= read -r import_stmt; do
        if ! grep -q "$import_stmt" "$target_file"; then
            sed -i "1s/^/$import_stmt\n/" "$target_file"
        fi
    done < "$import_stmts_file"
}

# Check if ~/.nuke/menu.py exists
if [ -f "$menu_file" ]; then
    # Insert contents of header file at the beginning
    insert_at_beginning "$header_file" "$menu_file"

    # Check and insert import statements
    check_and_insert_imports "$imports_file" "$menu_file"
    
    # Append contents of logic file
    cat "$logic_file" >> "$menu_file"

    echo "Script executed successfully."
else
    # Create menu.py and append contents of header, imports, and logic files
    cat "$header_file" "$imports_file" "$logic_file" > "$menu_file"

    echo "File $menu_file created successfully."
fi

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
