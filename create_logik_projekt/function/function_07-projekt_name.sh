#!/bin/bash

# -------------------------------------------------------------------------- #

# File Name:        function_07-projekt_name.sh
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
# declare -g client=""
# declare -g campaign=""
client=""
campaign=""

# ========================================================================== #
# This section defines functions to coerce data.
# ========================================================================== #

# Function to convert uppercase characters to lowercase
to_lowercase() {
    local input="$1"
    echo "$input" | tr '[:upper:]' '[:lower:]'
}

# -------------------------------------------------------------------------- #

# Function to sanitize input (letters, numbers, and underscores only)
sanitize_input() {
    local input="$1"
    input=$(echo "$input" | \
            # Replace non-alphanumeric characters with underscores
            sed 's/[^a-zA-Z0-9]/_/g' | \
            # Convert to lowercase
            tr '[:upper:]' '[:lower:]')
    # Replace consecutive sequences of underscores with one underscore
    input=$(echo "$input" | sed 's/_\{2,\}/_/g')
    # Remove leading and trailing underscores
    input=$(echo "$input" | sed 's/^_//;s/_*$//')
    if [[ "$input" =~ ^[a-z0-9_]+$ ]]; then
        echo "$input"
    else
        echo "error: format must be letters, numbers, or underscores."
        return 1
    fi
}

# ========================================================================== #
# This section defines the primary functions for the script.
# ========================================================================== #

# Function to gather the client name
gather_client_name() {
    local raw_client

    echo -e "  enter the client name for this logik projekt.\n"
    echo -e "  Use letters, numbers, spaces or underscores:\n"
    echo -e "  e.g. Apple, BMW, Chevron, Delta, 23 and Me"
    echo -e "\n$separator\n"
    read -p "  enter client name:   " raw_client
    echo -e "\n$separator\n"
    client=$(sanitize_input "$raw_client") || return 1

    # ---------------------------------------------------------------------- #

    # Display client
    echo -e "  client name:         $client"
    echo -e "\n$separator\n"

    # ---------------------------------------------------------------------- #

    # Write the information into the projekt_setup_file
    echo "client name: $client" > "$projekt_setup_file"

    # ---------------------------------------------------------------------- #

    # Write the information into the projekt_setup_template
    echo "client name: $client" > "$projekt_setup_template"
}

# -------------------------------------------------------------------------- #

# Function to gather the campaign name
gather_campaign_name() {
    local raw_campaign

    echo -e "  enter the campaign name for this logik projekt.\n"
    echo -e "  Use letters, numbers, or underscores:\n"
    echo -e "  e.g. iPhone 25, M7, Carwash, Business Class, DNA test 2025"
    echo -e "\n$separator\n"
    read -p "  enter campaign name: " raw_campaign
    echo -e "\n$separator\n"
    campaign=$(sanitize_input "$raw_campaign") || return 1

    # ---------------------------------------------------------------------- #

    # Display campaign
    echo -e "  campaign name:       $campaign"
    echo -e "\n$separator\n"

    # ---------------------------------------------------------------------- #

    # Write the information into the projekt_setup_file
    echo "campaign name: $campaign" >> "$projekt_setup_file"

    # ---------------------------------------------------------------------- #

    # Write the information into the projekt_setup_template
    echo "campaign name: $campaign" >> "$projekt_setup_template"
}

# Function to gather projekt name information
gather_projekt_name() {

    # Check if $has_projekt_setup_template is true
    if [ "$has_projekt_setup_template" = "True" ]; then
        if [ -f "$projekt_setup_template" ]; then
            client=$(sed -n '1p' "$projekt_setup_template" | cut -d ' ' -f3-)
            campaign=$(sed -n '2p' "$projekt_setup_template" | cut -d ' ' -f3-)
        else
            echo "Error: $projekt_setup_template not found."
            return 1
        fi
    else
        gather_client_name
        gather_campaign_name
    fi
}

# ========================================================================== #
# This section defines how to handle the main script function.
# ========================================================================== #

# # Call the function to gather projekt name information
# gather_projekt_name

# Check if the script is being sourced or executed
if [[ "${BASH_SOURCE[0]}" == "${0}" ]]; then
    gather_projekt_name
fi

# Now the global variables can be accessed wherever needed
# echo -e "  client:           $client"
# echo -e "  campaign:         $campaign"

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
