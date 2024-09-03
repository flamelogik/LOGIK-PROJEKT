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

# File Name:        get_adsk_python.sh
# Version:          0.0.3
# Created:          2024-01-19
# Modified:         2024-09-01

# ========================================================================== #
# This section defines the primary functions for the script.
# ========================================================================== #

# Get the directory of the running script
path_to_here="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"

# Set paths
parent_dir="$(dirname "$path_to_here")"
install_dir="$parent_dir/install"
install_logs_dir="$install_dir/logs"
resources_dir="$parent_dir/resources"
modules_dir="$parent_dir/modules"

# Define the log file with the current date prepended
current_adsk_python_version_log="$install_logs_dir/$(date '+%Y-%m-%d')-current_adsk_python_version_log.txt"

# Define a variable called 'separator'.
separator=$(printf '+ %s +' "$(printf -- '-%.0s' {1..75})")

# -------------------------------------------------------------------------- #

# Change to the parent directory
cd "$parent_dir" || exit

# Define the directory to analyze
# adsk_python_dir="/opt/Autodesk/python"  # PRODUCTION
adsk_python_dir="/home/pman/Documents/test_python_directory"  # TESTING

# # Function to log messages
# log_message() {
#     local message="$1"
#     echo "$(date '+%Y-%m-%d %H:%M:%S') - $message" | tee -a "$current_adsk_python_version_log"
# }

# Function to log messages
log_message() {
    local message="$1"
    echo "  $(date '+%Y-%m-%d %H:%M:%S') - $message"
}

# Redirect all output to the log file and the shell
exec > >(tee -a "$current_adsk_python_version_log") 2>&1

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

# ========================================================================== #
# C2 A9 32 30 32 34 2D 4D 41 4E 2D 4D 41 44 45 2D 4D 45 4B 41 4E 59 5A 4D 53 #
# ========================================================================== #

# Changelist:       

# -------------------------------------------------------------------------- #
# version:          0.0.1
# created:          2024-08-31 - 12:34:56
# comments:         utility to locate and use the Autodesk python version.
# -------------------------------------------------------------------------- #
# version:          0.0.2
# created:          2024-09-01 - 10:23:00
# comments:         Added preference management for Autodesk python version.
# -------------------------------------------------------------------------- #
# version:          0.0.3
# created:          2024-09-01 - 11:00:00
# comments:         Added logic to compare and update the preference file only if needed.
# -------------------------------------------------------------------------- #
