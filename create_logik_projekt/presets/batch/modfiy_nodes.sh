#!/bin/bash

# -------------------------------------------------------------------------- #

# ========================================================================== #
# This section defines a variable for the path to the running program.
# ========================================================================== #

# -------------------------------------------------------------------------- #

# Define the path to the current script in a variable called 'path_to_here'
path_to_here=$(cd $(dirname "$0") && pwd)

# change directory to path_to_here
cd $path_to_here

# -------------------------------------------------------------------------- #

# -------------------------------------------------------------------------- #
# C2 A9 32 30 32 34 20 2D 20 70 68 69 6C 5F 6D 61 6E 40 6D 61 63 2E 63 6F 6D #
# -------------------------------------------------------------------------- #

# ========================================================================== #
# This section defines variables for the relevant directories.
# ========================================================================== #

# -------------------------------------------------------------------------- #

# Set the parent_dir
home_dir="/home/pman/workspace/GitHub"
project_dir="FLAME-DEPLOYMENT"
workspace_dir="programs/configuration/opt/Autodesk/wiretap/setups/batch"
test_dir="pref_tmp"

# -------------------------------------------------------------------------- #

# -------------------------------------------------------------------------- #
# C2 A9 32 30 32 34 20 2D 20 70 68 69 6C 5F 6D 61 6E 40 6D 61 63 2E 63 6F 6D #
# -------------------------------------------------------------------------- #

# ========================================================================== #
# This section defines the program logic.
# ========================================================================== #
# c2 a9 2d 32 30 32 34 2d 4d 41 4e 5f 4d 41 44 45 5f 4d 41 54 45 52 49 41 4c #
# -------------------------------------------------------------------------- #

# Create a list of any files in any subdirectory of $test_dir whose name
# ends in '.lut_node'
file_list=$(find "$home_dir/$project_dir/$workspace_dir/$test_dir" \
-type f -name '*.lut_node')

# Print the list of files (optional, for verification)
echo -e "List of '.lut_node' files:"
echo -e "$file_list"
echo -e ""

# # Encode this UTF-8 string in hexadecimal format
# hex_value8=$(echo -n '©-2024-MAN_MADE_MATERIAL' | xxd -p)
# echo -e "$hex_value8"

# # Convert this UTF-8 string to UTF-16 and encode in hexadecimal format
# # hex_value16=$(echo -n '© MMXXIV man_made' | iconv -t UTF-16LE | xxd -p)
# # echo -e $hex_value16

# # Convert the hexadecimal string to UTF-8
# utf8_string=$(echo -n "$hex_value8" | xxd -r -p)
# echo -e "$utf8_string"

# Loop through each file in file_list
for file_path in $file_list; do
    # Extract the basename of the file
    file_basename=$(basename "$file_path")

    # Extract the sanitized_basename
    sanitized_basename=$(echo "$file_basename" \
    | sed 's/\.lut_node//;s/_/ /g')

    # Search for the string '<Note></Note>' and replace it with
    # '<Note>$sanitized_basename</Note>'
    sed -i "s|<Note></Note>|<Note>$sanitized_basename</Note>|g" "$file_path"

    # Search for the string '/hosts/delta' and replace it with
    # an empty string
    sed -i 's|/hosts/delta||g' "$file_path"

    # Print a message for each file (optional, for verification)
    echo -e "Updated file: $file_path"
done
