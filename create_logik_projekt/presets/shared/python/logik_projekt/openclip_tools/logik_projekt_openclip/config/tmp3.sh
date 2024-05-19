#!/bin/bash

# Define function name mappings in an associative array
declare -A function_map=(
    [FlameButton]=pyside6_qt_button
    [FlameClickableLineEdit]=pyside6_qt_clickable_line_edit
    [FlameLabel]=pyside6_qt_label
    [FlameLineEdit]=pyside6_qt_line_edit
    [FlameListWidget]=pyside6_qt_list_widget
    [FlameMessageWindow]=pyside6_qt_message_window
    [FlamePasswordWindow]=pyside6_qt_password_window
    [FlamePresetWindow]=pyside6_qt_preset_window
    [FlameProgressWindow]=pyside6_qt_progress_window
    [FlamePushButton]=pyside6_qt_push_button
    [FlamePushButtonMenu]=pyside6_qt_push_button_menu
    [FlameQDialog]=pyside6_qt_qdialog
    [FlameSlider]=pyside6_qt_slider
    [FlameTextEdit]=pyside6_qt_textedit
    [FlameTokenPushButton]=pyside6_qt_token_push_button
    [FlameTreeWidget]=pyside6_qt_tree_widget
    [FlameWindow]=pyside6_qt_window
    [pyflame_file_browser]=pyside6_qt_file_browser
    [pyflame_get_flame_version]=pyside6_qt_get_flame_version
    [pyflame_get_shot_name]=pyside6_qt_get_shot_name
    [pyflame_load_config]=pyside6_qt_load_config
    [pyflame_open_in_finder]=pyside6_qt_open_in_finder
    [pyflame_print]=pyside6_qt_print
    [pyflame_refresh_hooks]=pyside6_qt_refresh_hooks
    [pyflame_resolve_path_tokens]=pyside6_qt_resolve_path_tokens
    [pyflame_resolve_shot_name]=pyside6_qt_resolve_shot_name
    [pyflame_save_config]=pyside6_qt_save_config
)

# Define decorative separators
separator=$(printf '+ %s +' "$(printf -- '-%.0s' {1..75})")
separator_hash=$(printf '# %s #' "$(printf -- '-%.0s' {1..74})")

# Locate script and related directories
script_dir="$(dirname "$0")"
cd "$script_dir" || exit
parent_dir="$(dirname "$script_dir")"
cd "$parent_dir" || exit
version_dir="$parent_dir/version"

# Create version directory if not exists
if [ ! -d "$version_dir" ]; then
    echo "Directory '$version_dir' not found."
    read -p "Do you want to create it? [y/n]: " create_dir
    if [ "$create_dir" = "y" ]; then
        mkdir -p "$version_dir" || { echo "Error: Unable to create directory '$version_dir'."; exit 1; }
    else
        echo "Exiting. Directory not created."
        exit 1
    fi
fi

# Define version file
version_file="$version_dir/version.json"

# Directory containing scripts
scripts_dir="$parent_dir/scripts"

# Create scripts directory if not exists
if [ ! -d "$scripts_dir" ]; then
    echo "Directory '$scripts_dir' not found."
    read -p "Do you want to create it? [y/n]: " create_dir
    if [ "$create_dir" = "y" ]; then
        mkdir -p "$scripts_dir" || { echo "Error: Unable to create directory '$scripts_dir'."; exit 1; }
    else
        echo "Exiting. Directory not created."
        exit 1
    fi
fi

# List python scripts in $scripts_dir
function_scripts=$(find "$scripts_dir" -type f -name "*.py" | sort)

# Function to increment version
increment_version() {
    local version=$1
    IFS='.' read -r major minor patch <<< "$version"
    ((patch++))
    if [ "$patch" -eq 10 ]; then
        patch=0
        ((minor++))
        if [ "$minor" -eq 10 ]; then
            minor=0
            ((major++))
        fi
    fi
    echo "$major.$minor.$patch"
}

# Process each python script
for function_script in $function_scripts; do
    function_script_name=$(basename "$function_script")

    # Loop until no replacements are made
    while true; do
        replacements_made=false

        # Read version information from JSON file
        full_version=$(jq -r '.full' "$version_file")
        new_version=$(increment_version "$full_version")

        # Replace all instances of old_function_name with new_function_name
        for old_function_name in "${!function_map[@]}"; do
            new_function_name=${function_map[$old_function_name]}
            if grep -q "$old_function_name" "$function_script"; then
                sed -i "s/$old_function_name/$new_function_name/g" "$function_script"
                replacements_made=true

                # Update version.json
                jq -n --arg full "$new_version" \
                    --arg major "${new_version%%.*}" \
                    --arg minor "${new_version#*.}" --arg minor "${minor%%.*}" \
                    --arg patch "${new_version##*.}" \
                    '{major: $major, minor: $minor, patch: $patch, full: $full}' > "$version_file"

                # Update docstring with new version
                sed -i "s/^# File Name:.*/# File Name:        $function_script_name/" "$function_script"
                sed -i "s/^# Version:.*/# Version:          $new_version/" "$function_script"
                sed -i "s/^# Modified:.*/# Modified:         $(date +%F)/" "$function_script"

                # Append changelist comments
                echo -e "$separator_hash\n# version:               $new_version\n# modified:              $(date +%F) - $(date +%H:%M:%S)\n# comments:              Replaced $old_function_name with $new_function_name" >> "$function_script"
            fi
        done

        # Exit loop if no replacements were made
        if [ "$replacements_made" = false ]; then
            break
        fi

        echo "Processed $function_script"
    done
done
