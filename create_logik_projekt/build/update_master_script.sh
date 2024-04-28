#!/bin/bash

# filename: "update_master_script.sh"

# -------------------------------------------------------------------------- #

# Program Name:     update_master_script.sh
# Version:          1.0.0
# Language:         bash script
# Flame Version:    2025.x
# Author:           Phil MAN - phil_man@mac.com
# Toolset:          MAN_MADE_MATERIAL
# Created:          2024-04-20
# Modified:         2024-04-24
# Modifier:         Phil MAN - phil_man@mac.com

# Changelist:       

# -------------------------------------------------------------------------- #

# Description:      This program concatenates the subprograms into a new 
#                   master script.

# Installation:     Copy the 'LOGIK-PROJEKT' repo to your home directory,

# -------------------------------------------------------------------------- #

# ========================================================================== #
# This section creates a decorative separator for blocks of text.
# ========================================================================== #

# Define a variable called 'separator'
separator=$(printf '+ %s +' "$(printf -- '-%.0s' {1..75})")

# Display a separator
echo -e "\n$separator\n"

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

# Directory containing bash scripts
subprograms_dir="$script_dir/../subprograms"

# Check if the directory exists or create it
if [ ! -d "$subprograms_dir" ]; then
    echo -e "  Directory '$subprograms_dir' not found.\n"
    read -p "  Do you want to create it? [y/n]: " create_dir
    echo -e "\n$separator\n"
    if [ "$create_dir" = "y" ]; then
        mkdir -p "$subprograms_dir" \
        || { echo "Error: Unable to create directory '$subprograms_dir'."; \
        exit 1; }
        echo -e "\n$separator\n"
    else
        echo "Exiting. Directory not created."
        exit 1
        echo -e "\n$separator\n"
    fi
fi

# -------------------------------------------------------------------------- #

# Define builds_dir
builds_dir="$script_dir/../builds"

# Check if the directory exists or create it
if [ ! -d "$builds_dir" ]; then
    echo -e "  Directory '$builds_dir' not found.\n"
    read -p "  Do you want to create it? [y/n]: " create_dir
    echo -e "\n$separator\n"
    if [ "$create_dir" = "y" ]; then
        mkdir -p "$builds_dir" \
        || { echo "Error: Unable to create directory '$builds_dir'."; \
        exit 1; }
        echo -e "\n$separator\n"
    else
        echo "Exiting. Directory not created."
        exit 1
        echo -e "\n$separator\n"
    fi
fi

# Define output_script
output_script_name="$today_underscore-$now_underscore-build.sh"
output_script="$builds_dir/$output_script_name"

# ========================================================================== #
# This section reads the latest version from a JSON file.
# ========================================================================== #

# Read version information from JSON file
major=$(jq -r '.major' version.json)
minor=$(jq -r '.minor' version.json)
patch=$(jq -r '.patch' version.json)
full=$(jq -r '.full' version.json)

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
   > version.json

echo "  Version updated to $full"
echo -e "\n$separator\n"

# ========================================================================== #
# This section concatenates the subprograms shell scripts.
# ========================================================================== #

# List bash scripts in the directory and sort alphabetically
bash_scripts=$(find "$subprograms_dir" -type f -name "*.sh" | sort)

# Concatenate the bash scripts into a new script
cat $bash_scripts > "$output_script"

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
# This section modfifies the newly concatenated file.
# ========================================================================== #

# Perform find and replace operations in the output script
sed -i "s/LATEST_VERSION/$full/" "$output_script"
sed -i "s/YYYY-MM-DD/$(date +%F)/" "$output_script"
sed -i "s/CHANGE_COMMENTS/$change_comments/" "$output_script"

# ========================================================================== #
# This section modfifies the newly concatenated file.
# ========================================================================== #

# Display success message
echo -e "  Bash scripts concatenated into:\n"
echo -e "  '$output_script_name'"
echo -e "\n$separator\n"

# ========================================================================== #
# C2 A9 2D 32 30 32 34 2D 4D 41 4E 5F 4D 41 44 45 5F 4D 41 54 45 52 49 61 4C #
# ========================================================================== #
