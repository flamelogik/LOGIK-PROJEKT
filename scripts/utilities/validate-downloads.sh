#!/bin/bash
# validate-downloads.sh
# Script to analyze Autodesk Flame downloads and match md5 hashes.

# -------------------------------------------------------------------------- #
# Script Execution Options
# -------------------------------------------------------------------------- #

# Uncomment these settings for stricter bash execution
set -e           # Exit on any errors
# set -u           # Exit if any variable is used without being defined
# set -o pipefail  # Exit if any command in a pipeline fails
set -x           # Print each command before execution

# -------------------------------------------------------------------------- #
# Detect Operating System
# -------------------------------------------------------------------------- #

operating_system=$(uname)

# -------------------------------------------------------------------------- #

# Determine the operating system
if [[ "$(uname)" == "Darwin" ]]; then
    # macOS
    operating_system="macOS"

elif [[ "$(uname)" == "Linux" ]]; then
    # Linux
    operating_system="Linux"

else
    # Default to a common directory if the OS is not recognized
    echo -e "\n$separator_plus\n"
    echo -e "  Unsupported operating system."
    echo -e "\n$separator_plus\n"
    exit 1
fi

# -------------------------------------------------------------------------- #
# Detect Workstation Name
# -------------------------------------------------------------------------- #

# Get the workstation name
if [[ "$operating_system" == "macOS" ]]; then
    # For macOS
    workstation_name=$(scutil --get ComputerName)
elif [[ "$operating_system" == "Linux" ]]; then
    # For Linux
    workstation_name=$(hostname)
else
    # Default to a generic name if the OS is not recognized
    workstation_name="UnknownWorkstation"
fi

# -------------------------------------------------------------------------- #
# Detect Current User and Groups
# -------------------------------------------------------------------------- #

# Get username, primary group and group memberships.
CURRENT_USER="$USER"
PRIMARY_GROUP="$(id -gn)"
ALL_GROUPS="$(groups | tr ' ' ',' | sed 's/,/, /g')"

# -------------------------------------------------------------------------- #
# Path Discovery Functions for executable scripts
# -------------------------------------------------------------------------- #

# Get the name of this script
this_script=$(basename "$0")

# Set program_name to the name of this script
program_name="${this_script%.*}"

# Convert program_name to uppercase
program_name_uc=$(echo "$program_name" | tr '[:lower:]' '[:upper:]')

# Get the directory of this script
this_dir="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"

# Find scripts_dir in the path of this_dir
scripts_dir="${this_dir%/scripts/*}"

# Export the variables
export this_script program_name program_name_uc this_dir scripts_dir

# -------------------------------------------------------------------------- #
# Path Discovery Functions for Repository
# -------------------------------------------------------------------------- #

# Define repo_dir as the parent directory of scripts_dir
repo_dir=$(dirname "$scripts_dir")

# Get the name of the repo_dir
repo_name=$(basename "$repo_dir")

# Get the path to the parent directory of the repo_dir
repo_path=$(dirname "$repo_dir")

# Export the variables
export repo_dir repo_name repo_path

# -------------------------------------------------------------------------- #
# Directory and File Path Definitions
# -------------------------------------------------------------------------- #

# Define the path to the prefs_dir
prefs_dir="$repo_dir/prefs"

# -------------------------------------------------------------------------- #
# Imports - common
# -------------------------------------------------------------------------- #

source "$repo_dir/scripts/common/create/create-banners.sh"
source "$repo_dir/scripts/common/create/create-logs.sh"
source "$repo_dir/scripts/common/create/create-separators.sh"
source "$repo_dir/scripts/common/create/create-timestamp.sh"

# -------------------------------------------------------------------------- #
# Imports - lib
# -------------------------------------------------------------------------- #

# -------------------------------------------------------------------------- #
# Imports - utils
# -------------------------------------------------------------------------- #

# -------------------------------------------------------------------------- #
# Initialize a log file
# -------------------------------------------------------------------------- #

# Use log_shell_script_activity to create a log file
log_shell_script_activity "$program_name"

# Redirect all output to the log file
exec > >(tee -a "$program_log") 2>&1

# -------------------------------------------------------------------------- #
# Add a BANNER to the log file
# -------------------------------------------------------------------------- #

# Generate a banner_line_start
echo -e "\n$separator_plus\n"
generate_banner_line_start "$program_name_uc"
echo -e "\n$separator_plus\n"

# Echo the functions/variables
echo -e "  date: $projekt_date"
echo -e "  time: $projekt_time"
echo -e "  now:  $projekt_now"
echo -e "\n$separator_plus\n"

# -------------------------------------------------------------------------- #
# Prompt User to Choose the Downloads Directory
# -------------------------------------------------------------------------- #

if [[ "$operating_system" == "Linux" ]]; then
    if ! command -v zenity &> /dev/null; then
        echo -e "  Error: 'zenity' is not installed."
        echo -e "  Please install it to use this script on Linux."
        exit 1
    fi

    chosen_downloads_dir=$(zenity \
    --file-selection \
    --directory \
    --title="Select Downloads Directory" \
    --filename="/home/$USER/Downloads/")

    if [ $? -eq 1 ]; then
        echo -e "  Operation canceled by the user."
        exit 0
    fi

    # For Linux
    # calculated_md5=$(md5sum "$file_path" | awk '{print $1}')

elif [[ "$operating_system" == "macOS" ]]; then

    chosen_downloads_dir=$(
        osascript -e 'POSIX path of (choose folder with prompt "Select ADSK Downloads Directory")')

    if [ -z "$chosen_downloads_dir" ]; then
        echo -e "  Operation canceled by the user."
        exit 0
    fi

    # For macOS
    # calculated_md5=$(md5 -r "$file_path" | awk '{print $1}')

else
    echo -e "  Unsupported operating system."
    exit 1
fi

echo -e "  Chosen Downloads Directory: $chosen_downloads_dir"
echo -e "\n$separator_plus\n"

if [ ! -d "$chosen_downloads_dir" ]; then
    echo -e "  Error: Downloads directory does not exist. Exiting."
    exit 1
fi

# -------------------------------------------------------------------------- #
# Populate the File List
# -------------------------------------------------------------------------- #

file_list=()

while IFS= read -r -d '' file_path; do
    if [[ ! "$file_path" == *.md5 ]]; then
        file_list+=("$file_path")
    fi
done < <(find "$chosen_downloads_dir" -type f -print0)

# -------------------------------------------------------------------------- #

# Set the list_count
list_count=1

# Print the entire file list
echo -e "  The list of files is:"
for file_path in "${file_list[@]}"; do
    file_basename=$(basename "$file_path")
    # echo -e "    $file_basename\n"
    echo -e "\n    $list_count. $file_basename"
    list_count=$((list_count + 1))
done

echo -e "\n$separator_plus\n"

# -------------------------------------------------------------------------- #
# Process the File List
# -------------------------------------------------------------------------- #

# Set the file_count
file_count=1

# Process the entire file list
for file_path in "${file_list[@]}"; do
    file_basename=$(basename "$file_path")
    echo -e "  $file_count. $file_basename"
    file_count=$((file_count + 1))

    # Calculate MD5 checksum for each file
    if [[ "$operating_system" == "Linux" ]]; then
        calculated_md5=$(md5sum "$file_path" | awk '{print $1}')
    else
        calculated_md5=$(md5 -r "$file_path" | awk '{print $1}')
    fi

    md5_file="$file_path.md5"
    if [ ! -e "$md5_file" ]; then
        echo -e "\n     No corresponding .md5 file found."
        echo -e "\n     Skipping $file_basename:"
        echo -e "\n$separator_plus\n"
       continue
    fi

    expected_md5=$(cut -d' ' -f1 "$md5_file")

    # echo -e "  $expected_md5 - Expected MD5 for $file_basename"
    echo -e "\n     Expected Checksum: $expected_md5"

    # echo -e "  $calculated_md5 - Checksum for $file_basename"
    echo -e "     Actual Checksum:   $calculated_md5"

    if [ "$calculated_md5" == "$expected_md5" ]; then
        echo -e "\n     Checksums match for $file_basename"
        echo -e "\n     This file is valid."
        echo -e "\n$separator_plus\n"
    else
        echo -e "\n     Checksums DO NOT MATCH for $file_basename"
        echo -e "\n     This file may be corrupted."
        echo -e "\n$separator_plus\n"
    fi
done

# -------------------------------------------------------------------------- #
# 53 54 52 45 4E 47 54 48 2D 49 4E 2D 4E 55 4D 42 45 52 53 C2 A9 32 30 32 35 #
# -------------------------------------------------------------------------- #
# Changelist:
# -------------------------------------------------------------------------- #
# version:          0.0.1
# created:          2024-01-19 - 12:34:56
# comments:         scripts to create flame projekts, presets & templates.
# -------------------------------------------------------------------------- #
# version:          0.1.0
# modified:         2024-04-20 - 16:20:00
# comments:         refactored monolithic program into separate functions.
# -------------------------------------------------------------------------- #
# version:          0.5.0
# modified:         2024-05-24 - 20:24:00
# comments:         merged flame_colortoolkit with projekt.
# -------------------------------------------------------------------------- #
# version:          0.6.0
# modified:         2024-05-25 - 15:00:03
# comments:         started conversion to python3.
# -------------------------------------------------------------------------- #
# version:          0.7.0
# modified:         2024-06-21 - 18:21:03
# comments:         started gui design with pyside6.
# -------------------------------------------------------------------------- #
# version:          0.9.9
# modified:         2024-08-31 - 16:51:09
# comments:         prep for release - code appears to be functional
# -------------------------------------------------------------------------- #
# Version:          1.9.9
# modified:         2024-12-25 - 09:50:16
# comments:         Preparation for future features
# -------------------------------------------------------------------------- #
