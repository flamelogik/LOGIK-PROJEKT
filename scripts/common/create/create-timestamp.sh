#!/bin/bash
# create-timestamp.sh
# Create timestamps for shell processes.

# -------------------------------------------------------------------------- #
# Script Execution Options
# -------------------------------------------------------------------------- #

# Uncomment these settings for stricter bash execution
set -e           # Exit on any errors
# set -u           # Exit if any variable is used without being defined
# set -o pipefail  # Exit if any command in a pipeline fails
# set -x           # Print each command before execution

# -------------------------------------------------------------------------- #
# function definitions
# -------------------------------------------------------------------------- #

# define 'projekt_date' (use underscores instead of hyphens)
projekt_date=$(date +%Y_%m_%d)

# -------------------------------------------------------------------------- #

# define 'projekt_time' (use underscores instead of colons)
projekt_time=$(date +%H_%M_%S)

# -------------------------------------------------------------------------- #

# define 'projekt_now' (separated by a hyphen)
projekt_now="$projekt_date"-"$projekt_time"

# -------------------------------------------------------------------------- #
# Changelist:
# -------------------------------------------------------------------------- #