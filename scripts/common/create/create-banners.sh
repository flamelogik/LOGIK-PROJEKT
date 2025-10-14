#!/bin/bash
# create-banners.sh
# Create display banners for shell decoration.

# -------------------------------------------------------------------------- #
# Script Execution Options
# -------------------------------------------------------------------------- #

# Uncomment these settings for stricter bash execution
set -e           # Exit on any errors
# set -u           # Exit if any variable is used without being defined
# set -o pipefail  # Exit if any command in a pipeline fails
# set -x           # Print each command before execution

# -------------------------------------------------------------------------- #
# Function Definitions
# -------------------------------------------------------------------------- #

# Function to repeat a character n times
function repeat_char() {
    local char=$1
    local count=$2
    printf "%0.s$char" $(seq 1 "$count")
}

# -------------------------------------------------------------------------- #

# Function to ensure a line is exactly 79 characters
function make_line_79_chars() {
    local line=$1
    local current_length=${#line}

    # calculate the number of additional "=" characters needed
    local pad=$((79 - current_length))

    # add the required pad before the " #" at the end
    line="${line% #}$(repeat_char "=" "$pad") #"

    echo -e "$line"
}

# -------------------------------------------------------------------------- #

# Function to generate banner line
function generate_banner_line() {
    local banner=$1
    local total_length=79

    # calculate pad on each side of the banner
    local banner_pad_length=$(( (total_length - ${#banner} - 8) / 2 ))

    # generate the banner_line
    local banner_line=$(printf "# %s %s %s #\n" \
        "$(repeat_char "=" "$banner_pad_length")" \
        "$banner" \
        "$(repeat_char "=" "$banner_pad_length")")

    # ensure banner_line is exactly 79 characters
    banner_line=$(make_line_79_chars "$banner_line")

    echo -e "$banner_line"
}

# -------------------------------------------------------------------------- #

# Function to generate banner end line
function generate_banner_line_end() {
    local banner_end=$1
    local total_length=79

    # calculate pad on each side of the banner_end
    local banner_end_pad_length=$(( (total_length - ${#banner_end} - 8) / 2 ))

    # generate the banner_end_line
    local banner_end_line=$(printf "# %s %s %s #\n" \
        "$(repeat_char "=" "$banner_end_pad_length")" \
        "$banner_end" \
        "$(repeat_char "=" "$banner_end_pad_length")")

    # ensure banner_end_line is exactly 79 characters
    banner_end_line=$(make_line_79_chars "$banner_end_line")

    echo -e "$banner_end_line"
}

# -------------------------------------------------------------------------- #

# Function to generate banner start line
function generate_banner_line_start() {
    local banner_start=$1
    local total_length=79

    # calculate pad on each side of the banner_start
    local banner_start_pad_length=$(( (total_length - ${#banner_start} - 8) / 2 ))

    # generate the banner_start_line
    local banner_start_line=$(printf "# %s %s %s #\n" \
        "$(repeat_char "=" "$banner_start_pad_length")" \
        "$banner_start" \
        "$(repeat_char "=" "$banner_start_pad_length")")

    # ensure banner_start_line is exactly 79 characters
    banner_start_line=$(make_line_79_chars "$banner_start_line")

    echo -e "$banner_start_line"
}

# -------------------------------------------------------------------------- #
# Changelist:
# -------------------------------------------------------------------------- #
