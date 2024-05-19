#!/bin/bash

# -------------------------------------------------------------------------- #

# File Name:        update_changelists.sh
# Version:          1.0.0
# Language:         bash script
# Flame Version:    2025.x
# Author:           Phil MAN - phil_man@mac.com
# Toolset:          MAN_MADE_MATERIAL
# Created:          2024-04-20
# Modified:         2024-04-24
# Modifier:         Phil MAN - phil_man@mac.com

# Description:      This program updates the docstrings and changelists.

# Installation:     Copy the 'LOGIK-PROJEKT' repo to your GitHub directory,
#                   e.g. '/home/$USER/workspace/GitHub'

# Changelist:       The full changelist is at the end of this document.

# -------------------------------------------------------------------------- #

# ========================================================================== #
# This section creates a decorative separator for blocks of text.
# ========================================================================== #

# Define a variable called 'separator'.
separator=$(printf '+ %s +' "$(printf -- '-%.0s' {1..75})")

# ========================================================================== #
# This section creates a decorative separator for blocks of code.
# ========================================================================== #

# Define a variable called 'separator_hash'.
separator_hash=$(printf '# %s #' "$(printf -- '-%.0s' {1..74})")

# ========================================================================== #
# This section defines some date variables.
# ========================================================================== #

# Define 'today_underscore' (use underscores instead of hyphens)
today_underscore=$(date +%Y_%m_%d)

# Define 'now_underscore' (use underscores instead of hyphens)
now_underscore=$(date +%H_%M)

# ========================================================================== #
# This section locates the running script and the related directories.
# ========================================================================== #

# Get the directory of the script
script_dir="$(dirname "$0")"

# Change directory to script_dir
cd "$script_dir" || exit

# -------------------------------------------------------------------------- #

# Get the parent directory
parent_dir="$(dirname "$script_dir")"

# Change directory to script_dir
cd "$parent_dir" || exit

# -------------------------------------------------------------------------- #

# Define version_dir
version_dir="$parent_dir/version"

echo $version_dir

# Check if the directory exists or create it
if [ ! -d "$version_dir" ]; then
    echo -e "  Directory '$version_dir' not found.\n"
    read -p "  Do you want to create it? [y/n]: " create_dir
    echo -e "\n$separator\n"
    if [ "$create_dir" = "y" ]; then
        mkdir -p "$version_dir" \
        || { echo "Error: Unable to create directory '$version_dir'."; \
        exit 1; }
        echo -e "\n$separator\n"
    else
        echo "Exiting. Directory not created."
        exit 1
        echo -e "\n$separator\n"
    fi
fi

# Define version_file
version_file="$version_dir/version.json"

# ========================================================================== #
# This section reads the latest version from a JSON file.
# ========================================================================== #

# Read version information from JSON file
major=$(jq -r '.major' $version_file)
minor=$(jq -r '.minor' $version_file)
patch=$(jq -r '.patch' $version_file)
full=$(jq -r '.full' $version_file)

# -------------------------------------------------------------------------- #

# Print current full version
echo -e "  Current full version: $full"
echo -e "\n$separator\n"

# -------------------------------------------------------------------------- #

# Prompt user for the type of version update
read -p "  Is this a:

  1. Major update
  2. Minor update
  3. Patch update

$separator

  Enter the number corresponding to the type of update: " update_type

echo -e "\n$separator\n"

# ========================================================================== #
# This section updates the latest version based on user choice.
# ========================================================================== #

# Update version information based on user input
case $update_type in
    1)  ((major++));;
    2)  
        ((minor++))
        if [ "$minor" -eq 10 ]; then
            minor=0
            ((major++))
        fi
        ;;
    3)  
        ((patch++))
        if [ "$patch" -eq 10 ]; then
            patch=0
            ((minor++))
            if [ "$minor" -eq 10 ]; then
                minor=0
                ((major++))
            fi
        fi
        ;;
    *)  echo "Invalid input. Exiting."; exit 1;;
esac

# -------------------------------------------------------------------------- #

# Calculate full version string
full="$major.$minor.$patch"

# ========================================================================== #
# This section updates the latest version based on user choice.
# ========================================================================== #

# Update version.json
jq \
    -n \
    --arg major "$major" \
    --arg minor "$minor" \
    --arg patch "$patch" \
    --arg full "$full" \
   '{major: $major, minor: $minor, patch: $patch, full: $full}' \
   > $version_file

echo "  Version updated to $full"
echo -e "\n$separator\n"

# ========================================================================== #
# This section prompts for a comment for the changelist.
# ========================================================================== #

# Prompt user for change comments
echo -e "  Add a comment for the ChangeList.\n"
comment_measure="|<-------- * Limit comment to 56 characters * -------->|"
echo -e "  Example:  $comment_measure\n"
read -p "  Comment:  " change_comments
echo -e "\n$separator\n"

# Limit change comments to 56 characters
change_comments="${change_comments:0:56}"

# ========================================================================== #
# This section processes information for the shell scripts.
# ========================================================================== #

# Directory containing bash scripts
function_dir="$parent_dir/function"
# function_dir="$parent_dir/testing"

# Check if the directory exists or create it
if [ ! -d "$function_dir" ]; then
    echo -e "  Directory '$function_dir' not found.\n"
    read -p "  Do you want to create it? [y/n]: " create_dir
    echo -e "\n$separator\n"
    if [ "$create_dir" = "y" ]; then
        mkdir -p "$function_dir" \
        || { echo "Error: Unable to create directory '$function_dir'."; \
        exit 1; }
        echo -e "\n$separator\n"
    else
        echo "Exiting. Directory not created."
        exit 1
        echo -e "\n$separator\n"
    fi
fi

# List the shell scripts in $function_dir
# function_scripts=$(find "$function_dir" -maxdepth 1 -type f -name '*.sh')
function_scripts=$(find "$function_dir" -type f -name "*.sh" | sort)

# Iterate over each shell script
for function_script in $function_scripts; do
    # Get the base name of the shell script
    function_script_name=$(basename "$function_script")

    # # Use sed -i to replace the line that begins '# File Name'
    # sed -i "s/^# File Name:.*/# File Name:        $function_script_name/" "$function_script"

    # Use sed -i to replace the line that begins '# Version'
    sed -i "s/^# Version:.*/# Version:          $full/" "$function_script"

    # Use sed -i to replace the line that begins '# Modified'
    sed -i "s/^# Modified:.*/# Modified:         $(date +%F)/" "$function_script"

    # Append the comment to the shell script
    echo -e "$separator_hash" >> "$function_script"
    echo -e "# version:               $full" >> "$function_script"
    echo -e "# modified:              $(date +%F) - $(date +%H:%M:%S)" >> "$function_script"
    echo -e "# comments:              $change_comments" >> "$function_script"

done

# ========================================================================== #
# This section processes information for the create_logik_projekt.sh script.
# ========================================================================== #

# Directory containing bash scripts
master_script="$parent_dir/create_logik_projekt.sh"

# Use sed -i to replace the line that begins '# Version'
sed -i "s/^# Version:.*/# Version:          $full/" "$master_script"

# Use sed -i to replace the line that begins '# Modified'
sed -i "s/^# Modified:.*/# Modified:         $(date +%F)/" "$master_script"

# Append the comment to the shell script
echo -e "$separator_hash" >> "$master_script"
echo -e "# version:               $full" >> "$master_script"
echo -e "# modified:              $(date +%F) - $(date +%H:%M:%S)" >> "$master_script"
echo -e "# comments:              $change_comments" >> "$master_script"

# ========================================================================== #
# C2 A9 2D 32 30 32 34 2D 4D 41 4E 5F 4D 41 44 45 5F 4D 41 54 45 52 49 61 4C #
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
