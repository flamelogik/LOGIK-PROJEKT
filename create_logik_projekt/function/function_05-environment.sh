#!/bin/bash

# -------------------------------------------------------------------------- #

# File Name:        function_05-environment.sh
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
# declare -g operating_system=""
# declare -g workstation_name=""
# declare -g current_user=""
# declare -g primary_group=""
# declare -g all_groups=""
# declare -g other_groups=""
# declare -g user_home=""

# declare -g shell_type=""
# declare -g rc_filename=""
# declare -g rc_filepath=""

operating_system=""
workstation_name=""
current_user=""
primary_group=""
all_groups=""
other_groups=""
user_home=""

shell_type=""
rc_filename=""
rc_filepath=""

# ========================================================================== #
# This section defines functions to gather environment information.
# ========================================================================== #

# Function to get operating system
get_operating_system() {
    if [[ "$(uname)" == "Linux" ]]; then
        operating_system="Linux"
    elif [[ "$(uname)" == "Darwin" ]]; then
        operating_system="macOS"
    fi
}

# -------------------------------------------------------------------------- #

# Function to get workstation name
get_workstation_name() {
    local operating_system="$1"
    if [[ "$operating_system" == "Linux" ]]; then
        workstation_name="$(hostname -s)"
    elif [[ "$operating_system" == "macOS" ]]; then
        workstation_name="$(scutil --get ComputerName)"
    fi
}

# -------------------------------------------------------------------------- #

# Function to get current user
get_current_user() {
    current_user="$USER"
}

# -------------------------------------------------------------------------- #

# Function to get primary group
get_primary_group() {
    primary_group="$(id -gn)"
}

# -------------------------------------------------------------------------- #

# Function to get all group memberships
get_all_groups() {
    # all_groups="$(groups | tr ' ' ',' | sed 's/,/, /g')"
    all_groups="$(groups | tr ' ' ',')"
}

# -------------------------------------------------------------------------- #

# Function to get other group memberships
# (all groups except the primary group)
get_other_groups() {
    local primary_group="$1"
    # local all_groups="$(groups | tr ' ' ',' | sed 's/,/, /g')"
    local all_groups="$(groups | tr ' ' ',')"
    # Exclude the primary group
    other_groups="$(echo "$all_groups" | sed "s/\b$primary_group\b//g")"
    # Remove leading comma, if any
    other_groups="${other_groups#,}"
}

# -------------------------------------------------------------------------- #

# Function to get user's home directory
get_user_home() {
    user_home="$HOME"
}

# -------------------------------------------------------------------------- #

# Function to get current shell type
get_shell_type() {
    shell="$SHELL"
    if [[ "$shell" == *"bash"* ]]; then
        shell_type="bash"
    elif [[ "$shell" == *"zsh"* ]]; then
        shell_type="zsh"
    else
        shell_type="unknown"
    fi
}

# -------------------------------------------------------------------------- #

# Function to get rc filename based on OS and shell
get_rc_filename() {
    local operating_system="$1"
    local shell="$2"
    if [[ "$operating_system" == "Linux" && "$shell" == "bash" ]]; then
        rc_filename=".bashrc"
    elif [[ "$operating_system" == "macOS" && "$shell" == "zsh" ]]; then
        rc_filename=".zprofile"
    else
        rc_filename=".rc"
    fi
}

# -------------------------------------------------------------------------- #

# Function to get rc filepath
get_rc_filepath() {
    local user_home="$1"
    local rc_filename="$2"
    rc_filepath="${user_home}/${rc_filename}"
}

# ========================================================================== #
# This section defines functions to parse environment information.
# ========================================================================== #

# Function to get the base name of a file
get_base_name() {
    local file="$1"
    basename="$(basename "$file")"
}

# -------------------------------------------------------------------------- #

# Function to get the full path to a file
get_full_path() {
    local file="$1"
    full_path="$(realpath "$file")"
}

# -------------------------------------------------------------------------- #

# Function to get the directory name of a file
get_directory_name() {
    local file="$1"
    directory_name="$(dirname "$(realpath "$file")")"
}

# -------------------------------------------------------------------------- #

# Function to create aliases
create_alias() {
    local alias_name="$1"
    local alias_path="$2"
    local rc_filepath="$3"

    if ! grep -q "alias $alias_name=" "$rc_filepath"; then
        echo "" >> "$rc_filepath"
        echo "# Alias for $alias_name" >> "$rc_filepath"
        echo "alias $alias_name=\"$alias_path\"" >> "$rc_filepath"
        echo "" >> "$rc_filepath"
    fi
}

# -------------------------------------------------------------------------- #

# Function to set permissions for a file
set_permissions() {
    local file="$1"
    chmod 600 "$file"
}

# ========================================================================== #
# This section defines the primary functions for the script.
# ========================================================================== #

# Function to initialize environment variables
initialize_environment() {
    get_user_home
    get_rc_filename "$operating_system" "$shell_type"
    get_rc_filepath "$user_home" "$rc_filename"

    # Create rc_filepath if it does not exist
    if [ ! -f "$rc_filepath" ]; then
        touch "$rc_filepath"
        chmod 600 "$rc_filepath"
    fi

    # Create the alias
    if ! grep -q "alias projekt=" "$rc_filepath"; then
        echo "" >> "$rc_filepath"
        echo "# Alias for projekt" >> "$rc_filepath"
        echo "alias projekt=\"$alias_path\"" >> "$rc_filepath"
        echo "" >> "$rc_filepath"
    fi
}

# -------------------------------------------------------------------------- #

# Function to gather system information
gather_system_info() {
    get_operating_system
    get_workstation_name "$operating_system"
    get_current_user
    get_primary_group
    get_all_groups
    get_other_groups "$primary_group"
    get_shell_type
}

# -------------------------------------------------------------------------- #

# Function to print system information
print_system_info() {
    echo -e "  current user:        $current_user"
    echo -e "  primary group:       $primary_group"
    echo -e "  all groups:          $all_groups"
    echo -e "  other groups:        $other_groups"
    echo -e "\n$separator\n"

    echo -e "  operating system:    $operating_system"
    echo -e "\n$separator\n"

    echo -e "  workstation name:    $workstation_name"
    echo -e "\n$separator\n"

    echo -e "  user home:           $user_home"
    echo -e "  shell type:          $shell_type"
    echo -e "  .rc filename:        $rc_filename"
    echo -e "\n$separator\n"
}

# ========================================================================== #
# This section defines how to handle the main script function.
# ========================================================================== #

# Main function
get_environment() {
    initialize_environment
    gather_system_info
}

# Call the main function
get_environment

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
