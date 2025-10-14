#!/bin/bash
# create-separators.sh
# Create display separators for shell decoration.

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

# define a variable called 'separator_plus'
separator_plus=$(printf '+ %s +' "$(printf -- '-%.0s' {1..75})")

# -------------------------------------------------------------------------- #

# define a variable called 'separator_hash'
separator_hash=$(printf '# %s #' "$(printf -- '-%.0s' {1..75})")

# -------------------------------------------------------------------------- #
# Changelist:
# -------------------------------------------------------------------------- #
