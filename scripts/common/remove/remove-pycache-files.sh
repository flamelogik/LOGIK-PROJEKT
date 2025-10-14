#!/bin/bash
# remove-pycache-files.sh
# Script to remove __pycache__ and .pyc files.

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
scripts_dir="${this_dir%/scripts/*}/scripts"

# scripts_dir="$this_dir"
# while [[ "$scripts_dir" != "/" ]]; do
#     if [[ "$(basename "$scripts_dir")" == "scripts" ]]; then
#         break
#     fi
#     scripts_dir="$(dirname "$scripts_dir")"
# done

# # Verify we found it
# if [[ "$(basename "$scripts_dir")" != "scripts" ]]; then
#     echo "Error: Could not find scripts directory in path" >&2
#     exit 1
# fi


# Export the variables
export this_script program_name program_name_uc this_dir scripts_dir

# -------------------------------------------------------------------------- #
# Path Discovery Functions for Repository
# -------------------------------------------------------------------------- #

# # Define app_dir as the parent directory of scripts_dir
# app_dir=$(dirname "$scripts_dir")

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

source "$scripts_dir/common/create/create-banners.sh"
source "$scripts_dir/common/create/create-logs.sh"
source "$scripts_dir/common/create/create-separators.sh"
source "$scripts_dir/common/create/create-timestamp.sh"

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

# Set the target directory (modify this to your specific directory)
target_directory="$repo_dir"
echo "Target directory: $target_directory"
# Change to the target directory
cd "$target_directory" || exit 1

# Remove __pycache__ directories
find . -type d -name "__pycache__" -exec rm -rfv {} +

# Remove all .pyc files
find . -type f -name "*.pyc" -delete

# Print a message indicating the completion of the operation
echo "Cleanup completed!"

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
