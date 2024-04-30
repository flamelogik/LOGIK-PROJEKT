#!/bin/bash

# -------------------------------------------------------------------------- #

# File Name:        function_04-setup.sh
# Version:          2.0.1
# Language:         bash script
# Flame Version:    2025.x
# Author:           Phil MAN - phil_man@mac.com
# Toolset:          MAN_MADE_MATERIAL: LOGIK-PROJEKT
# Modified:         2024-04-30
# Modifier:         Phil MAN - phil_man@mac.com

# Description:      This program contains function(s) that are used to
#                   create new logik projekts.

# Installation:     Copy the 'LOGIK-PROJEKT' repo to your GitHub directory,
#                   e.g. '/home/$USER/workspace/GitHub'

# Changelist:       The full changelist is at the end of this document.

# -------------------------------------------------------------------------- #

# ========================================================================== #
# This section defines global variables.
# ========================================================================== #

# Declare global variables
# declare -g projekt_log_dir=""
# declare -g projekt_creation_log_file=""
# declare -g projekt_setup_file=""
# declare -g projekt_setup_template=""
# declare -g has_projekt_setup_template=""
# declare -g has_projekt_setup_template="False"
projekt_log_dir=""
projekt_creation_log_file=""
projekt_setup_file=""
projekt_setup_template=""
has_projekt_setup_template=""

# ========================================================================== #
# This section defines variables based on the date.
# ========================================================================== #

# Year Options
YYYY=$(date "+%Y")

# Month Options
MM=$(date "+%m")

# Day Options
DD=$(date "+%d")

# Current Date and Time Options
NOW_DATE=$(date "+%F")
NOW_TIME=$(date "+%H-%M")
now_h_m=$(date "+%H-%M")
NOW_NOW="$NOW_DATE-$NOW_TIME"

# ========================================================================== #
# This section creates directories and files for the new logik projekt.
# ========================================================================== #

# Function to create directories for logik projekt setup
create_projekt_directories() {
    # $script_path - SEE NOTE AT START OF SCRIPT
    projekt_log_dir="$script_path/log/$YYYY/$MM/$DD"

    if [ ! -d "$projekt_log_dir" ]; then
        mkdir -p "$script_path/log"
        mkdir -p "$script_path/log/$YYYY"
        mkdir -p "$script_path/log/$YYYY/$MM"
        mkdir -p "$script_path/log/$YYYY/$MM/$DD"
    fi
}

# -------------------------------------------------------------------------- #

# Function to backup existing files
backup_file() {
    local file="$1"
    if [ -f "$file" ]; then
        mv "$file" "$file.bak"
    fi
}

# -------------------------------------------------------------------------- #

# Function to create log file
create_log_file() {
    local filename="$1"
    local log_file="$projekt_log_dir/$filename"
    backup_file "$log_file"
    touch "$log_file"
    echo "$(date +"%Y-%m-%d %H:%M:%S") - Logik Projekt Setup Log" > "$log_file"
}

# -------------------------------------------------------------------------- #

# Function to create setup file
create_setup_file() {
    local filename="$1"
    local setup_file="$projekt_log_dir/$filename"
    backup_file "$setup_file"
    touch "$setup_file"
}

# ========================================================================== #
# This section prompts the user to choose a logik projekt template.
# ========================================================================== #

# Function to browse for projekt setup template
browse_for_template() {
    # Browse for a projekt setup template
    if [[ "$operating_system" == "Linux" ]]; then

        # Linux
        chosen_projekt_setup_template=$(zenity \
        --file-selection \
        --title="Select Projekt Setup File"
        )

    else

        # macOS
        chosen_projekt_setup_template=$(osascript \
        -e "tell application \"System Events\" to activate" \
        -e "POSIX path of \
        (choose file with prompt \
        \"Select Projekt Setup File\")\
        ")

    fi

        # Check if user canceled the operation
    if [ $? -ne 0 ]; then
        echo "File selection canceled."
        exit 1
    fi
}

# -------------------------------------------------------------------------- #

# Function to prompt user for projekt setup template
prompt_for_template() {
    # Prompt the user to confirm if they have a projekt setup file
    read -p "  Do you have a projekt setup template? Y/N [N]: " answer

    # Default to 'N' if no input
    answer="${answer:-N}"

    # Convert the answer to uppercase for comparison
    answer=$(echo "$answer" | tr '[:lower:]' '[:upper:]')

    if [ "$answer" = "Y" ]; then

        # Set variable to True
        has_projekt_setup_template=True

        browse_for_template

    else

        # Set variable to True
        has_projekt_setup_template=False

    fi
}

# ========================================================================== #
# This section defines the function to setup a new logik projekt template.
# ========================================================================== #

# Function to setup logik projekt and initialize global variables
setup_logik_projekt() {
    create_projekt_directories

    local projekt_creation_log_filename="$NOW_NOW-projekt_creation_log"
    create_log_file "$projekt_creation_log_filename"
    projekt_creation_log_file="$projekt_log_dir/$projekt_creation_log_filename"

    local projekt_setup_filename="$NOW_NOW-projekt_setup_file"
    create_setup_file "$projekt_setup_filename"
    projekt_setup_file="$projekt_log_dir/$projekt_setup_filename"

    local projekt_setup_template_name="projekt_setup_template"
    projekt_setup_template="$projekt_log_dir/$projekt_setup_template_name"

    prompt_for_template

    if [ "$has_projekt_setup_template" = "True" ]; then

        # ------------------------------------------------------------------ #

        # browse_for_template

        # Check if the template projekt setup template exists
        if [ ! -f "$projekt_setup_template" ]; then

            # Copy the chosen projekt setup template to default template location
            cp "$chosen_projekt_setup_template" "$projekt_setup_template"
            
            echo -e "  Chosen projekt setup template backed up."
        fi

        # ------------------------------------------------------------------ #

    else

        # ------------------------------------------------------------------ #

        create_projekt_directories
        create_log_file

        # ------------------------------------------------------------------ #

    fi

}

# ========================================================================== #
# This section defines how to handle the main script function.
# ========================================================================== #

# Call the setup_logik_projekt function to initialize the global variables
# setup_logik_projekt

# Check if the script is being sourced or executed
if [[ "${BASH_SOURCE[0]}" == "${0}" ]]; then
    setup_logik_projekt
fi

# Now the global variables can be accessed wherever needed
# echo -e "  logs directory:   $projekt_log_dir"
# echo -e "  creation log:     $projekt_creation_log_file"
# echo -e "  setup file:       $projekt_setup_file"
# echo -e "  fetup template:   $projekt_setup_template"

# -------------------------------------------------------------------------- #

# ========================================================================== #
# C2 A9 2D 32 30 32 34 2D 4D 41 4E 5F 4D 41 44 45 5F 4D 41 54 45 52 49 61 4C #
# ========================================================================== #

# Changelist:       
# -------------------------------------------------------------------------- #
# version:               1.0.0
# modified:              2024-04-20 - 16:20:00
# comments:              refactored monolithic program into separate functions
# -------------------------------------------------------------------------- #
# version:               2.0.0
# modified:              2024-04-29 - 11:29:27
# comments:              testing production readiness
# -------------------------------------------------------------------------- #
# version:               2.0.1
# modified:              2024-04-30 - 07:06:00
# comments:              Removed 'declare -g' statements for macOS compatibility
