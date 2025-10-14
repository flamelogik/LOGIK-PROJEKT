#!/bin/bash
# create-logs.sh
# Create logs for shell execution.

# Usage in main.sh:
#   source create-logs.sh
#   LOG_SCRIPT_ACTIVITY "my_program"
#   exec > >(tee -a "$PROGRAM_LOG") 2>&1

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

# requires: $repo_dir and $projekt_now to be set in the calling script.
log_shell_script_activity() {
    local program_name="$1"
    if [[ -z "$repo_dir" ]]; then
        echo "error: repo_dir is not set." >&2
        return 1
    fi
    if [[ -z "$projekt_now" ]]; then
        echo "error: projekt_now is not set." >&2
        return 1
    fi
    logs_dir="${repo_dir}/logs/shell-logs"
    mkdir -p "${logs_dir}"
    log_name="${projekt_now}-${program_name}.log"
    program_log="${logs_dir}/${log_name}"
    # export for use in calling script
    export program_log
}

# requires: $repo_dir and $projekt_now to be set in the calling script.
log_python_script_activity() {
    local program_name="$1"
    if [[ -z "$repo_dir" ]]; then
        echo "error: repo_dir is not set." >&2
        return 1
    fi
    if [[ -z "$projekt_now" ]]; then
        echo "error: projekt_now is not set." >&2
        return 1
    fi
    logs_dir="${repo_dir}/logs/python-logs"
    mkdir -p "${logs_dir}"
    log_name="${projekt_now}-${program_name}.log"
    program_log="${logs_dir}/${log_name}"
    # export for use in calling script
    export program_log
}

# -------------------------------------------------------------------------- #
# Changelist:
# -------------------------------------------------------------------------- #
