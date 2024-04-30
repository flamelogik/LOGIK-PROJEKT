#!/bin/bash

# -------------------------------------------------------------------------- #

# File Name:        function_01-separators.sh
# Version:          2.0.2
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
# This section creates a decorative separator for blocks of text.
# ========================================================================== #

# Define a variable called 'separator'.
separator=$(printf '+ %s +' "$(printf -- '-%.0s' {1..75})")

# ========================================================================== #
# This section creates a decorative separator for blocks of code.
# ========================================================================== #

# Define a variable called 'separator_hash'.
separator_hash=$(printf '# %s #' "$(printf -- '-%.0s' {1..75})")

# ========================================================================== #
# This section creates decorative separators for titles and banners.
# ========================================================================== #

# Function to repeat a character n times.
repeat_char() {
    local char=$1
    local count=$2
    printf "%0.s$char" $(seq 1 "$count")
}

# -------------------------------------------------------------------------- #

# Function to ensure a line is exactly 79 characters.
make_line_79_chars() {
    local line=$1
    local current_length=${#line}

    # Calculate the number of additional "=" characters needed.
    local pad=$((79 - current_length))

    # Add the required pad before the " #" at the end.
    line="${line% #}$(repeat_char "=" "$pad") #"

    echo -e "$line"
}

# -------------------------------------------------------------------------- #

# Function to generate title line.
generate_title_line() {
    local title=$1
    local total_length=79

    # Calculate pad on each side of the title.
    local title_pad_length=$(( (total_length - ${#title} - 8) / 2 ))

    # Generate the title_line.
    local title_line=$(printf "# %s %s %s #\n" \
        "$(repeat_char "=" "$title_pad_length")" \
        "$title" \
        "$(repeat_char "=" "$title_pad_length")")

    # Ensure title_line is exactly 79 characters.
    title_line=$(make_line_79_chars "$title_line")

    echo -e "$title_line"
}

# -------------------------------------------------------------------------- #

# Function to generate end of title line.
generate_end_title_line() {
    local end_title=$1
    local total_length=79

    # Calculate pad on each side of the end_title.
    local end_title_pad_length=$(( (total_length - ${#end_title} - 8) / 2 ))

    # Generate the end_title_line.
    local end_title_line=$(printf "# %s %s %s #\n" \
        "$(repeat_char "=" "$end_title_pad_length")" \
        "$end_title" \
        "$(repeat_char "=" "$end_title_pad_length")")

    # Ensure end_title_line is exactly 79 characters.
    end_title_line=$(make_line_79_chars "$end_title_line")

    echo -e "$end_title_line"
}

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
# -------------------------------------------------------------------------- #
# version:               2.0.2
# modified:              2024-04-30 - 12:29:07
# comments:              added 'umask 0' statements for rsync commands
