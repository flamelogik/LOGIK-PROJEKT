#!/bin/bash
# delete-init-py-files.sh
# Script to remove __init__.py files.

# -------------------------------------------------------------------------- #
# Script Execution Options
# -------------------------------------------------------------------------- #

# Uncomment these settings for stricter bash execution
set -e           # Exit on any errors
# set -u           # Exit if any variable is used without being defined
# set -o pipefail  # Exit if any command in a pipeline fails
# set -x           # Print each command before execution

# -------------------------------------------------------------------------- #
# Detect Operating System
# -------------------------------------------------------------------------- #

OPERATING_SYSTEM=$(uname)

# -------------------------------------------------------------------------- #
# Path Discovery Functions for executable scripts
# -------------------------------------------------------------------------- #

# Get the name of this script
THIS_SCRIPT=$(basename "$0")

# Set PROGRAM_NAME to the name of this script
PROGRAM_NAME="${THIS_SCRIPT%.*}"

# Convert PROGRAM_NAME to uppercase
PROGRAM_NAME_UC=$(echo "$PROGRAM_NAME" | tr '[:lower:]' '[:upper:]')

# Get the directory of this script
THIS_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"

# Find BIN_DIR in the path of THIS_DIR
BIN_DIR="${THIS_DIR%/bin/*}"

# Export the variables
export THIS_SCRIPT PROGRAM_NAME PROGRAM_NAME_UC THIS_DIR BIN_DIR

# -------------------------------------------------------------------------- #
# Path Discovery Functions for Repository
# -------------------------------------------------------------------------- #

# Define REPO_DIR as the parent directory of BIN_DIR
REPO_DIR=$(dirname "$BIN_DIR")

# Get the name of the REPO_DIR
REPO_NAME=$(basename "$REPO_DIR")

# Get the path to the parent directory of the REPO_DIR
REPO_PATH=$(dirname "$REPO_DIR")

# Export the variables
export REPO_DIR REPO_NAME REPO_PATH

# -------------------------------------------------------------------------- #
# Directory and File Path Definitions
# -------------------------------------------------------------------------- #

# -------------------------------------------------------------------------- #
# Imports - common
# -------------------------------------------------------------------------- #

source "$REPO_DIR/src/common/create/create-banners.sh"
source "$REPO_DIR/src/common/create/create-logs.sh"
source "$REPO_DIR/src/common/create/create-separators.sh"
source "$REPO_DIR/src/common/create/create-timestamp.sh"

# -------------------------------------------------------------------------- #
# Imports - lib
# -------------------------------------------------------------------------- #

# -------------------------------------------------------------------------- #
# Imports - utils
# -------------------------------------------------------------------------- #

# -------------------------------------------------------------------------- #
# Initialize a log file
# -------------------------------------------------------------------------- #

# Use LOG_SHELL_SCRIPT_ACTIVITY to create a log file
LOG_SHELL_SCRIPT_ACTIVITY "$PROGRAM_NAME"

# Redirect all output to the log file
exec > >(tee -a "$PROGRAM_LOG") 2>&1

# -------------------------------------------------------------------------- #
# Add a BANNER to the log file
# -------------------------------------------------------------------------- #

# Generate a BANNER_LINE_START
echo -e "\n$separator_plus\n"
GENERATE_BANNER_LINE_START "$PROGRAM_NAME_UC"
echo -e "\n$separator_plus\n"

# Echo the functions/variables
echo -e "  Date: $PROJEKT_DATE"
echo -e "  Time: $PROJEKT_TIME"
echo -e "  Now:  $PROJEKT_NOW"
echo -e "\n$separator_plus\n"

# -------------------------------------------------------------------------- #

# Set the target directory (modify this to your specific directory)
TARGET_DIRECTORY="$REPO_DIR/src"

# Change to the target directory
cd "$TARGET_DIRECTORY" || exit 1

# Remove __init__.py files
find . -type f -name "__init__.py" -delete

# add execution permissions to every .sh and every .zsh file of every subdirectory
find . -type f \( -name "*.sh" -o -name "*.zsh" \) -exec chmod +x {} \;

# Print a message indicating the completion of the operation
echo -e "  Removed __init__.py in every subdirectory of $TARGET_DIRECTORY."

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
