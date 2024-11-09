#!/bin/bash

# -------------------------------------------------------------------------- #

# File Name:        update_changelist_comments.sh
# Version:          1.0.1
# Language:         bash script
# Flame Version:    2025.x
# Author:           Phil MAN - phil_man@mac.com
# Toolset:          MAN_MADE_MATERIAL: LOGIK-PROJEKT
# Created:          2024-10-10
# Modified:         2024-10-11
# Modifier:         Phil MAN - phil_man@mac.com

# Description:      This program updates docstrings and changelists.

# Installation:     Copy the 'LOGIK-PROJEKT' repo to your GitHub directory,
#                   e.g. '/home/$USER/workspace/GitHub'

# Changelist:       The full changelist is at the end of this document.

# -------------------------------------------------------------------------- #

# set -ex

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

# Get the directory of this script
cfg_dir="$(dirname "$0")"

# Get the parent directory
parent_dir="$(dirname "$cfg_dir")"

# Change directory to cfg_dir
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
# This function processes information for logik projekt shell scripts.
# ========================================================================== #

update_shell_scripts() {
    scripts_dir="$parent_dir/scripts"
    # local scripts_dir="$1"

    # Check if the directory exists or create it
    if [ ! -d "$scripts_dir" ]; then
        echo -e "  Directory '$scripts_dir' not found.\n"
        read -p "  Do you want to create it? [y/n]: " create_dir
        echo -e "\n$separator\n"
        if [ "$create_dir" = "y" ]; then
            mkdir -p "$scripts_dir" \
            || { echo "Error: Unable to create directory '$scripts_dir'."; \
            exit 1; }
            echo -e "\n$separator\n"
        else
            echo "Exiting. Directory not created."
            exit 1
            echo -e "\n$separator\n"
        fi
    fi

    # List the logik projekt shell scripts in $scripts_dir
    shell_scripts=$(find "$scripts_dir" -type f -name "*.sh" | sort)

    # Iterate over each shell script
    for shell_script in $shell_scripts; do
        # Get the base name of the logik projekt shell script
        shell_script_name=$(basename "$shell_script")

        # Use sed -i to replace the line that begins '# Version'
        sed -i "s/^# Version:.*/# Version:          $full/" "$shell_script"

        # Use sed -i to replace the line that begins '# Modified'
        sed -i "s/^# Modified:.*/# Modified:         $(date +%F)/" "$shell_script"

        # Append the comment to the shell script
        echo -e "# version:               $full" >> "$shell_script"
        echo -e "# modified:              $(date +%F) - $(date +%H:%M:%S)" >> "$shell_script"
        echo -e "# comments:              $change_comments" >> "$shell_script"
        echo -e "$separator_hash" >> "$shell_script"
    done
}

# ========================================================================== #
# This function processes information for logik projekt Python scripts.
# ========================================================================== #

update_python_scripts() {
    python_scripts_dir="$parent_dir/scripts"
    # local python_scripts_dir="$1"
    
    # Check if the directory exists or create it
    if [ ! -d "$python_scripts_dir" ]; then
        echo -e "  Directory '$python_scripts_dir' not found.\n"
        read -p "  Do you want to create it? [y/n]: " create_dir
        echo -e "\n$separator\n"
        if [ "$create_dir" = "y" ]; then
            mkdir -p "$python_scripts_dir" \
            || { echo "Error: Unable to create directory '$python_scripts_dir'."; \
            exit 1; }
            echo -e "\n$separator\n"
        else
            echo "Exiting. Directory not created."
            echo -e "\n$separator\n"
            exit 1
        fi
    fi

    # List the logik projekt Python scripts in $python_scripts_dir
    python_scripts=$(find "$python_scripts_dir" -type f -name "*.py" | sort)

    # Iterate over each Python script
    for python_script in $python_scripts; do
        # Get the base name of the logik projekt Python script
        python_script_name=$(basename "$python_script")

        # Use sed -i to replace the line that begins '# Version'
        sed -i "s/^# Version:.*/# Version:          $full/" "$python_script"

        # Use sed -i to replace the line that begins '# Modified'
        sed -i "s/^# Modified:.*/# Modified:         $(date +%F)/" "$python_script"

        # Append the comment to the Python script
        echo -e "# version:               $full" >> "$python_script"
        echo -e "# modified:              $(date +%F) - $(date +%H:%M:%S)" >> "$python_script"
        echo -e "# comments:              $change_comments" >> "$python_script"
        echo -e "$separator_hash" >> "$python_script"
    done
}

# ========================================================================== #
# This section runs both script processing functions.
# ========================================================================== #

# Update shell scripts in the scripts directory
update_shell_scripts "$scripts_dir"

# Update Python scripts in the scripts directory
update_python_scripts "$scripts_dir"

# ========================================================================== #
# C2 A9 32 30 32 34 2D 4D 41 4E 2D 4D 41 44 45 2D 4D 45 4B 41 4E 59 5A 4D 53 #
# ========================================================================== #

# Changelist:

# -------------------------------------------------------------------------- #
# version:               1.0.0
# modified:              2024-10-10 - 10:20:24
# comments:              Initial commit
# -------------------------------------------------------------------------- #
# version:               1.0.1
# modified:              2024-10-12 - 18:29:34
# comments:              Added functions to update shell and python scripts.
# -------------------------------------------------------------------------- #
