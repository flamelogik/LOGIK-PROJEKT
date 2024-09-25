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

# File Name:        create_desktop_apps.sh
# Version:          0.0.4
# Created:          2024-01-19
# Modified:         2024-09-02

# ========================================================================== #
# This section defines paths for the script.
# ========================================================================== #

# Get the directory of the running script
path_to_here="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"

# Set paths
parent_dir="$(dirname "$path_to_here")"
install_dir="$parent_dir/install"
install_logs_dir="$install_dir/logs"
resources_dir="$parent_dir/resources"
modules_dir="$parent_dir/modules"

# Change to the parent directory
cd "$parent_dir" || exit

# Create the logs directory
mkdir -p "$install_logs_dir" || exit

# Define the directory to analyze
adsk_python_dir="/opt/Autodesk/python"  # PRODUCTION
# adsk_python_dir="/home/pman/Documents/test_python_directory"  # TESTING

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

# Define the macOS application name
macos_app_name="${app_name}.app"

# Define the application version number
app_version="1.0"

# ========================================================================== #
# This section defines the primary functions for the script.
# ========================================================================== #

# Define a variable called 'separator'.
separator=$(printf '+ %s +' "$(printf -- '-%.0s' {1..75})")

# Function to log messages
log_message() {
    local message="$1"
    echo "  $(date '+%Y-%m-%d %H:%M:%S') - $message"
}

# Redirect all output to the log file and the shell
exec > >(tee -a "$current_adsk_python_version_log") 2>&1

# ========================================================================== #
# This section determines the most recent Autodesk python version.
# ========================================================================== #

# Custom sort function
custom_sort() {
    awk '
    function parse_version(str) {
        split(str, parts, /[.]/)
        major = parts[1]
        minor = (parts[2] == "") ? 0 : parts[2]
        patch = (parts[3] == "") ? 0 : parts[3]
        if (str ~ /qfe/) {
            qfe = substr(str, index(str, "qfe") + 3)
            type = sprintf("2%04d", qfe)  # qfe gets highest priority
        } else if (str ~ /pr/) {
            pr = substr(str, index(str, "pr") + 2)
            type = sprintf("0%04d", pr)  # pr gets lowest priority
        } else {
            type = "10000"  # release versions are between qfe and pr
        }
        return sprintf("%04d%03d%03d%s %s", major, minor, patch, type, str)
    }
    {
        print parse_version($0)
    }' | sort -r | cut -d' ' -f2-
}

# Function to get the highest version
get_highest_version() {
    ls -1d "$adsk_python_dir"/*/ | sed 's:/$::' | xargs -n1 basename | grep -E '^[0-9]{4}' | custom_sort | head -n 1
}

# Function to read and write the current_adsk_python_version from/to a preference file
manage_preferences() {
    local pref_file="$install_dir/current_adsk_python_version.pref"
    
    if [ ! -f "$pref_file" ]; then
        echo -e "\n$separator\n"
        log_message "Preference file not found."
        log_message "Creating $pref_file."
        log_message ""
        touch "$pref_file"
    else
        echo -e "\n$separator\n"
        log_message "Reading preference file:"
        log_message "$pref_file"
        log_message ""
        current_adsk_python_version=$(cat "$pref_file")
        log_message "Preference file loaded:"
        log_message "$current_adsk_python_version"
        log_message ""
    fi
}

# Write the current version to the preference file if it has changed
write_preference() {
    local pref_file="$install_dir/current_adsk_python_version.pref"
    local new_version_path="/opt/Autodesk/python/$current_adsk_python_version/bin/python"
    
    # Read the current preference value
    local current_pref_version=$(cat "$pref_file")
    
    if [ "$current_pref_version" != "$new_version_path" ]; then
        echo "$new_version_path" > "$pref_file"
        log_message "Updated preference file with:"
        log_message "$new_version_path"
        log_message ""
        echo -e "\n$separator\n"
    else
        log_message ""
        log_message "No update needed."
        log_message ""
        log_message "Preference file already contains the latest version:"
        log_message "$new_version_path"
        echo -e "\n$separator\n"
    fi
}

# Manage the preferences
manage_preferences

# -------------------------------------------------------------------------- #

# Check if the directory to analyze exists
if [ ! -d "$adsk_python_dir" ]; then
    log_message "Directory $adsk_python_dir does not exist"
    echo -e "\n$separator\n"
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
    write_preference
    # You can add commands here to use this Python version
else
    log_message "Warning: Python version $current_adsk_python_version is not available or not executable"
    echo -e "\n$separator\n"
    # You might want to add fallback logic here
fi

# Ensure current_adsk_python_version is set
current_adsk_python_version=$(cat "$install_dir/current_adsk_python_version.pref")

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

echo -e "\n$separator\n"

# Copy the icon to the Resources directory
cp "$resources_dir/icons/logik_projekt_icon.icns" "$macos_app_name/Contents/Resources"

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

# Create the file and add the block of text
cat <<EOF > "$projekt_script_runner_linux"
#!/bin/bash
cd $parent_dir
$current_adsk_python_version $parent_dir/logik_projekt.py
EOF

# Echo progress to the shell and log to the log file
log_message "Making the file executable: $projekt_script_runner_linux"

# Make the file executable
chmod +x "$projekt_script_runner_linux"

# Echo progress to the shell and log to the log file
log_message "Creating macOS application shell script: $projekt_script_runner_macos"

# Copy the shell script to the macOS application
cp "$projekt_script_runner_linux" "$macos_app_name/Contents/MacOS/$projekt_script_runner_macos"

echo -e "\n$separator\n"

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
Version=1.0
Exec=$parent_dir/$projekt_script_runner_linux
Icon=$resources_dir/icons/logik_projekt_icon_01.png
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
elif [[ "$(uname)" == "Darwin" ]]; then
    log_message "This script is not configured to move files on macOS (Darwin)."
else
    log_message "Unsupported operating system: $(uname)"
fi

# Final confirmation
log_message "File '$desktop_entry_file' has been created and made executable."

echo -e "\n$separator\n"

# ========================================================================== #
# C2 A9 32 30 32 34 2D 4D 41 4E 2D 4D 41 44 45 2D 4D 45 4B 41 4E 59 5A 4D 53 #
# ========================================================================== #

# Changelist:       

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
