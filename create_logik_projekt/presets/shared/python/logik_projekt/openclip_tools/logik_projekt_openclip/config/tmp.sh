#!/bin/bash

# -------------------------------------------------------------------------- #

# File Name:        rename_functions.sh
# Version:          0.0.0
# Language:         bash script
# Flame Version:    2025.x
# Author:           Phil MAN - phil_man@mac.com
# Toolset:          MAN_MADE_MATERIAL: LOGIK-PROJEKT
# Created:          2024-04-20
# Modified:         2024-05-16
# Modifier:         ChatGPT

# Description:      This program replaces function names in Python files.
#                   Additionally, it updates the docstrings and changelists.

# Installation:     Copy the 'LOGIK-PROJEKT' repo to your GitHub directory,
#                   e.g. '/home/$USER/workspace/GitHub'

# Changelist:       The full changelist is at the end of this document.

# -------------------------------------------------------------------------- #

# ========================================================================== #
# This section defines old and new function names.
# ========================================================================== #

# Define 'old_function_name'.
# old_function_name="FlameButton"
# old_function_name="FlameClickableLineEdit"
# old_function_name="FlameLabel"
# old_function_name="FlameLineEdit"
# old_function_name="FlameListWidget"
# old_function_name="FlameMessageWindow"
# old_function_name="FlamePasswordWindow"
# old_function_name="FlamePresetWindow"
# old_function_name="FlameProgressWindow"
# old_function_name="FlamePushButtonMenu"
# old_function_name="FlamePushButton"
# old_function_name="FlameQDialog"
# old_function_name="FlameSlider"
# old_function_name="FlameTextEdit"
# old_function_name="FlameTokenPushButton"
# old_function_name="FlameTreeWidget"
# old_function_name="FlameWindow"

# old_function_name="pyflame_file_browser"
# old_function_name="pyflame_get_flame_version"
# old_function_name="pyflame_get_shot_name"
# old_function_name="pyflame_load_config"
# old_function_name="pyflame_open_in_finder"
# old_function_name="pyflame_print"
# old_function_name="pyflame_refresh_hooks"
# old_function_name="pyflame_resolve_path_tokens"
# old_function_name="pyflame_resolve_shot_name"
# old_function_name="pyflame_save_config"

# Define 'new_function_name'.
# new_function_name="pyside6_qt_button"
# new_function_name="pyside6_qt_clickable_line_edit"
# new_function_name="pyside6_qt_label"
# new_function_name="pyside6_qt_line_edit"
# new_function_name="pyside6_qt_list_widget"
# new_function_name="pyside6_qt_message_window"
# new_function_name="pyside6_qt_password_window"
# new_function_name="pyside6_qt_preset_window"
# new_function_name="pyside6_qt_progress_window"
# new_function_name="pyside6_qt_push_button_menu"
# new_function_name="pyside6_qt_push_button"
# new_function_name="pyside6_qt_qdialog"
# new_function_name="pyside6_qt_slider"
# new_function_name="pyside6_qt_text_edit"
# new_function_name="pyside6_qt_token_push_button"
# new_function_name="pyside6_qt_tree_widget"
# new_function_name="pyside6_qt_window"

# new_function_name="pyside6_qt_file_browser"
# new_function_name="pyside6_qt_get_flame_version"
# new_function_name="pyside6_qt_get_shot_name"
# new_function_name="pyside6_qt_load_config"
# new_function_name="pyside6_qt_open_in_finder"
# new_function_name="pyside6_qt_print"
# new_function_name="pyside6_qt_refresh_hooks"
# new_function_name="pyside6_qt_resolve_path_tokens"
# new_function_name="pyside6_qt_resolve_shot_name"
# new_function_name="pyside6_qt_save_config"

# ========================================================================== #
# This section defines the replace_function_name function.
# ========================================================================== #

# # Function to replace all instances of old_function_name with new_function_name
# replace_function_name() {

#     # Iterate over each python script
#     for function_script in $function_scripts; do
#         # Replace all instances of old_function_name with new_function_name
#         sed -i "s/$old_function_name/$new_function_name/g" "$function_script"
#     done

#     echo -e "Replaced all instances of '$old_function_name' with '$new_function_name' in all Python scripts."
#     echo -e "\n$separator\n"
# }

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

# Change directory to parent_dir
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

# ========================================================================== #
# This section updates the latest version.
# ========================================================================== #

# Increment patch version
((patch++))
if [ "$patch" -eq 10 ]; then
    patch=0
    ((minor++))
    if [ "$minor" -eq 10 ]; then
        minor=0
        ((major++))
    fi
fi

# Calculate full version string
full="$major.$minor.$patch"

# ========================================================================== #
# This section updates the version.json file.
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
# This section adds a comment for the changelist.
# ========================================================================== #

# Automatically set the change comment
change_comments="Replaced $old_function_name with $new_function_name"
echo -e "\n$separator\n"

# ========================================================================== #
# This section processes information for logik projekt python scripts.
# ========================================================================== #

# Directory containing logik projekt python scripts.
scripts_dir="$parent_dir/scripts"
# scripts_dir="$parent_dir/testing"

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

# List the logik projekt python scripts in $scripts_dir
function_scripts=$(find "$scripts_dir" -type f -name "*.py" | sort)

# Iterate over each python script
for function_script in $function_scripts; do
    # Get the base name of the logik projekt python script
    function_script_name=$(basename "$function_script")

    # # Use sed -i to replace the line that begins '# File Name'
    # sed -i "s/^# File Name:.*/# File Name:        $function_script_name/" "$function_script"

    # Replace all instances of old_function_name with new_function_name
    sed -i "s/$old_function_name/$new_function_name/g" "$function_script"

    # Use sed -i to replace the line that begins '# Version'
    sed -i "s/^# Version:.*/# Version:          $full/" "$function_script"

    # Use sed -i to replace the line that begins '# Modified'
    sed -i "s/^# Modified:.*/# Modified:         $(date +%F)/" "$function_script"

    # Append the comment to the python script
    echo -e "$separator_hash" >> "$function_script"
    echo -e "# version:               $full" >> "$function_script"
    echo -e "# modified:              $(date +%F) - $(date +%H:%M:%S)" >> "$function_script"
    echo -e "# comments:              $change_comments" >> "$function_script"
done

# ========================================================================== #
# C2 A9 2D 32 30 32 34 2D 4D 41 4E 5F 4D 41 44 45 5F 4D 41 54 45 52 49 41 4C #
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
