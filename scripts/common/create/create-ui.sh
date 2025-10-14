#!/bin/bash
# create-ui.sh
# Create UI components for displaying information in shells.

# -------------------------------------------------------------------------- #
# Script Execution Options
# -------------------------------------------------------------------------- #

# Uncomment these settings for stricter bash execution
set -e           # Exit on any errors
# set -u           # Exit if any variable is used without being defined
# set -o pipefail  # Exit if any command in a pipeline fails
# set -x           # Print each command before execution

# -------------------------------------------------------------------------- #
# Source Function Scripts
# -------------------------------------------------------------------------- #

# # Not currently working
# source "create-banners.sh"
# source "create-separators.sh"
# source "create-timestamp.sh"

# -------------------------------------------------------------------------- #
# function definitions
# -------------------------------------------------------------------------- #

function generate_timestamp() {
    date "+%y_%m_%d-%h_%m_%s"
}

# -------------------------------------------------------------------------- #

function display_welcome_banner() {
    echo -e ""
    generate_banner_line_start "create a virtual python environment"
    echo -e "\n$separator_plus\n"
    echo -e "   repository name:  $repo_name"
    echo -e "       script name:  $script_name"
    echo -e "\n$separator_plus\n"
    echo -e "  parent directory:  $repo_parent_dir"
    echo -e "    repo directory:  $repo_dir"
    echo -e "  source directory:  $src_dir"
    echo -e "    venv directory:  $venv_dir"
    echo -e "\n$separator_plus\n"
}

# -------------------------------------------------------------------------- #

function display_section_header() {
    local section_name="$1"
    echo -e "\n$separator_hash\n"
    echo "$section_name"
    echo -e "\n$separator_hash\n"
}

# -------------------------------------------------------------------------- #

function display_completion_message() {
    echo -e "\n$separator_plus\n"
    echo "virtual environment setup complete!"
    echo "to activate the virtual environment, run:"
    echo "source $activate_venv_script"
    echo -e "\n$separator_plus\n"

    echo "virtual environment created and ready to use."
    echo -e "\n$separator_hash\n"
}

# -------------------------------------------------------------------------- #
# Changelist:
# -------------------------------------------------------------------------- #
