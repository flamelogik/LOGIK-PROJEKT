#!/bin/bash
# -------------------------------------------------------------------------- #
# Filename:     create_desktop_apps.sh
# Purpose:      Wrapper script to run create_customized_filesystem_template.py
#               with the Autodesk Python interpreter specified in a .pref file.
# Description:  Reads the path to the Autodesk Python executable from
#               install/current_adsk_python_version.pref and then executes
#               src/utils/common/create/create_customized_filesystem_template.py
#               using that specific Python version.

# Author:       phil_man@mac.com
# Copyright:    Copyright (c) 2025
# Disclaimer:   Disclaimer at bottom of script.
# License:      GNU General Public License v3.0 (GPL-3.0).
#               https://www.gnu.org/licenses/gpl-3.0.en.html

# Version:      2026.1.0
# Status:       Development
# Type:         Utility
# Created:      2024-01-19
# Modified:     2025-08-07

# Changelog:    Changelog at bottom of script.
# -------------------------------------------------------------------------- #

# ========================================================================== #
# This section defines paths for the script.
# ========================================================================== #

# Get the directory of the running script
path_to_here="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"

# Set paths
parent_dir="$(dirname "$path_to_here")"
install_dir="$parent_dir/install"
install_logs_dir="$install_dir/logs"
cfg_dir="$parent_dir/cfg"
site_cfg_dir="$cfg_dir/site-cfg"
logik_projekt_cfg_dir="$site_cfg_dir/logik-projekt-cfg"
icons_dir="$logik_projekt_cfg_dir/icons"
src_dir="$parent_dir/src"

# Change to the parent directory
cd "$parent_dir" || exit

# Create the logs directory
mkdir -p "$install_logs_dir" || exit

# Define the directory to analyze (configurable via first argument)
ADSK_PYTHON_BASE_DIR="${1:-/opt/Autodesk/python}"
adsk_python_dir="$ADSK_PYTHON_BASE_DIR"

# Define the log file with the current date prepended
current_adsk_python_version_log="$install_logs_dir/$(date '+%Y-%m-%d')-current_adsk_python_version_log.txt"

# ========================================================================== #
# This section defines the application name and version.
# ========================================================================== #

# Define the application name
app_name="LOGIK-PROJEKT"

# Sanitize the application name (replace spaces and special characters with underscores)
app_name_sanitize=$(echo "$app_name" | tr -d '[:punct:]' | tr ' ' '_')

# Derive the application name in lowercase
app_name_lc=$(echo "$app_name_sanitize" | tr '[:upper:]' '[:lower:]')

# Define the application version number
app_version="2026.1.0"

# Define the macOS application name
macos_app_name="${app_name}-${app_version}.app"

# ========================================================================== #
# This section defines the primary functions for the script.
# ========================================================================== #

# Define a variable called 'separator'.
separator=$(printf '+ %s +' "$(printf -- '-%.0s' {1..75})")

# Function to log messages
log_message() {
    local message="$1"
    echo "  $message"
}

# Redirect all output to the log file and the shell
exec > >(tee -a "$current_adsk_python_version_log") 2>&1

# ========================================================================== #
# This section determines the most recent Autodesk python version.
# ========================================================================== #

# Custom sort function
custom_sort() {
    awk '
    # parse_version: Extracts and normalizes version components for sorting
    function parse_version(str) {
        split(str, parts, /[.]/) # Split version string by dot
        major = parts[1]
        minor = (parts[2] == "") ? 0 : parts[2]
        patch = (parts[3] == "") ? 0 : parts[3]

        # Determine version type priority: qfe > release > pr
        if (str ~ /qfe/) {
            qfe = substr(str, index(str, "qfe") + 3)
            type = sprintf("2%04d", qfe)  # Highest priority for qfe
        } else if (str ~ /pr/) {
            pr = substr(str, index(str, "pr") + 2)
            type = sprintf("0%04d", pr)  # Lowest priority for pr
        } else {
            type = "10000"  # Middle priority for standard releases
        }
        # Format for numeric sorting: major, minor, patch, type, original string
        return sprintf("%04d%03d%03d%s %s", major, minor, patch, type, str)
    }
    { print parse_version($0) }
' | sort -r | cut -d' ' -f2-
}

# Function to get the highest version
get_highest_version() {
    ls -1d "$adsk_python_dir"/*/ | sed 's:/$::' | xargs -n1 basename | grep -E '^[0-9]{4}' | custom_sort | head -n 1
}

# Function to read and write the current_adsk_python_version from/to a preference file
update_adsk_python_preference() {
    local pref_file="$install_dir/current_adsk_python_version.pref"
    local new_version_path="$adsk_python_dir/$1/bin/python"

    local current_pref_version=""
    if [ -f "$pref_file" ]; then
        log_message "Reading preference file:"
        log_message "$pref_file"
        current_pref_version=$(cat "$pref_file" 2>/dev/null)
        if [ -n "$current_pref_version" ]; then
            log_message "Preference file loaded:"
            log_message "$current_pref_version"
        else
            log_message "Preference file is empty or unreadable."
        fi
    else
        log_message "Preference file not found."
        log_message "Creating $pref_file."
        touch "$pref_file" || { log_message "Error: Could not create preference file."; exit 1; }
    fi

    if [ "$current_pref_version" != "$new_version_path" ]; then
        echo "$new_version_path" > "$pref_file" || { log_message "Error: Could not write to preference file."; exit 1; }
        log_message "Updated preference file with:"
        log_message "$new_version_path"
        printf "\n%s\n" "$separator"
    else
        log_message "No update needed."
        log_message "Preference file already contains the latest version:"
        log_message "$new_version_path"
        printf "\n%s\n" "$separator"
    fi
}

# Manage the preferences (now handled by update_adsk_python_preference after version detection)

# -------------------------------------------------------------------------- #

# Check if the directory to analyze exists
if [ ! -d "$adsk_python_dir" ]; then
    log_message "Directory $adsk_python_dir does not exist"
    printf "\n%s\n" "$separator"
    exit 1
fi

log_message "Analyzing directory: $adsk_python_dir"

# List and custom sort the contents of the directory
log_message "Sorted contents of $adsk_python_dir:"
ls -1d "$adsk_python_dir"/*/ | sed 's:/$::' | xargs -n1 basename | grep -E '^[0-9]{4}' | custom_sort | while read -r line; do
    log_message "$line"
done
log_message ""

# Get the highest version
current_adsk_python_version=$(get_highest_version)
log_message "The highest version is: $current_adsk_python_version"
log_message ""

# Check if the highest version exists and is executable
if [ -x "$adsk_python_dir/$current_adsk_python_version/bin/python" ]; then
    log_message "Python version $current_adsk_python_version is available and executable"
    update_adsk_python_preference "$current_adsk_python_version"
    # You can add commands here to use this Python version
else
    log_message "Warning: Python version $current_adsk_python_version is not available or not executable"
    printf "\n%s\n" "$separator"
    # You might want to add fallback logic here
fi

# Ensure current_adsk_python_version is set
# Ensure current_adsk_python_version is set (no longer needed, handled by update_adsk_python_preference)

# ========================================================================== #
# This section creates components for the desktop gui applications.
# ========================================================================== #

# Create the macOS application
mkdir -p "$macos_app_name"

# Echo progress to the shell and log to the log file
log_message "Creating macOS application: $macos_app_name"

# Create the necessary directories
mkdir -p "$macos_app_name/Contents"
mkdir -p "$macos_app_name/Contents/MacOS"
mkdir -p "$macos_app_name/Contents/Resources"

# Echo progress to the shell and log to the log file
log_message "Creating the macOS application components"

printf "\n%s\n" "$separator"

# Copy the icon to the Resources directory
cp "$icons_dir/logik_projekt_icon.icns" "$macos_app_name/Contents/Resources"

# Create the Info.plist file
cat <<EOF > "$macos_app_name/Contents/Info.plist"
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
    <key>CFBundleName</key>
    <string>$app_name</string>
    <key>CFBundleIdentifier</key>
    <string>com.logik.projekt</string>
    <key>CFBundleVersion</key>
    <string>$app_version</string>
    <key>CFBundleExecutable</key>
    <string>run_${app_name_lc}_macos</string>
    <key>CFBundlePackageType</key>
    <string>APPL</string>
    <key>CFBundleSignature</key>
    <string>????</string>
    <key>CFBundleInfoDictionaryVersion</key>
    <string>6.0</string>
    <key>CFBundleIconFile</key>
    <string>logik_projekt_icon</string>
</dict>
</plist>
EOF

# -------------------------------------------------------------------------- #

# Define the shell script
projekt_script_runner_linux="run_${app_name_lc}_linux.sh"
projekt_script_runner_macos="run_${app_name_lc}_macos"

# Echo progress to the shell and log to the log file
log_message "Creating $app_name shell script for linux: $projekt_script_runner_linux"

# Read the full Python executable path from the preference file
PYTHON_EXECUTABLE=$(cat "$install_dir/current_adsk_python_version.pref")

# Create the file and add the block of text
sed "s|__PYTHON_EXECUTABLE__|$PYTHON_EXECUTABLE|" "$install_dir/run_logikprojekt_linux.sh.template" > "$projekt_script_runner_linux"

# Echo progress to the shell and log to the log file
log_message "Making the file executable: $projekt_script_runner_linux"

# Make the file executable
chmod +x "$projekt_script_runner_linux"

# Echo progress to the shell and log to the log file
log_message "Creating macOS application shell script: $projekt_script_runner_macos"

# Copy the shell script to the macOS application
cp "$projekt_script_runner_linux" "$macos_app_name/Contents/MacOS/$projekt_script_runner_macos"

printf "\n%s\n" "$separator"

# -------------------------------------------------------------------------- #

# Define the desktop entry file for linux
desktop_entry_file="${app_name}.desktop"

# Echo progress to the shell and log to the log file
log_message "Creating desktop entry file: $desktop_entry_file"

# Create the file and add the block of text
cat <<EOF > $desktop_entry_file
[Desktop Entry]
Name=$app_name
Comment=This application will create a brand new PROJEKT
Version=$app_version
Exec=$parent_dir/$projekt_script_runner_linux
Icon=$icons_dir/logik_projekt_icon_01.png
Type=Application
Terminal=True
EOF

# Echo progress to the shell and log to the log file
log_message "Making the file executable: $desktop_entry_file"

# Make the file executable
chmod +x $desktop_entry_file

# Check the operating system and log the appropriate message
if [[ "$(uname)" == "Linux" ]]; then
    log_message "Moving the file to ~/.local/share/applications/"
    mv $desktop_entry_file ~/.local/share/applications/
elif [[ "	$(uname)" == "Darwin" ]]; then
    log_message "This script is not configured to move files on macOS (Darwin)."
else
    log_message "Unsupported operating system: $(uname)"
fi

# Final confirmation
log_message "File '$desktop_entry_file' has been created and made executable."

printf "\n%s\n" "$separator"


# -------------------------------------------------------------------------- #

# DISCLAIMER:   This file is part of LOGIK-PROJEKT.

#               Copyright © 2025 STRENGTH IN NUMBERS

#               LOGIK-PROJEKT creates directories, files, scripts & tools
#               for use with Autodesk Flame and other software.

#               LOGIK-PROJEKT is free software.

#               You can redistribute it and/or modify it under the terms
#               of the GNU General Public License as published by the
#               Free Software Foundation, either version 3 of the License,
#               or any later version.

#               This program is distributed in the hope that it will be
#               useful, but WITHOUT ANY WARRANTY; without even the

#               implied warranty of MERCHANTABILITY or
#               FITNESS FOR A PARTICULAR PURPOSE.

#               See the GNU General Public License for more details.
#               You should have received a copy of the GNU General
#               Public License along with this program.

#               If not, see <https://www.gnu.org/licenses/gpl-3.0.en.html>.

#               Contact: phil_man@mac.com

# -------------------------------------------------------------------------- #
# C2 A9 32 30 32 35 53 54 52 45 4E 47 54 48 2D 49 4E 2D 4E 55 4D 42 45 52 53 #
# -------------------------------------------------------------------------- #
# Changelog:
# -------------------------------------------------------------------------- #
# version:          0.0.1
# created:          2024-08-31 - 12:34:56
# comments:         utility to create desktop apps for LOGIK-PROJEKT.
# -------------------------------------------------------------------------- #
# version:          0.0.2
# created:          2024-09-01 - 10:23:00
# comments:         Added preference management for Autodesk python version.
# -------------------------------------------------------------------------- #
# version:          0.0.3
# created:          2024-09-01 - 11:00:00
# comments:         Added logic to compare and update the preference file only if needed.
# -------------------------------------------------------------------------- #
# version:          0.0.4
# created:          2024-09-02 - 17:18:56
# comments:         Makes the linux and macos apps.
# -------------------------------------------------------------------------- #
