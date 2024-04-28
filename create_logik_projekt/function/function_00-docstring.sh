#!/bin/bash

# -------------------------------------------------------------------------- #

# filename: "function_00-docstring.sh"

# -------------------------------------------------------------------------- #

# Program Name:     create_logik_projekts.sh
# Version:          LATEST_VERSION
# Language:         bash script
# Flame Version:    2025.x
# Author:           Phil MAN - phil_man@mac.com
# Toolset:          MAN_MADE_MATERIAL: LOGIK-PROJEKT
# Created:          2024-01-19
# Modified:         YYYY-MM-DD
# Modifier:         Phil MAN - phil_man@mac.com

# Description:      This program determines system information and collects
#                   user input to create new logik projekts.

# Installation:     Copy the 'LOGIK-PROJEKT' repo to your home directory,

# -------------------------------------------------------------------------- #

# Changelist:       CHANGE_COMMENTS

# -------------------------------------------------------------------------- #

# ========================================================================== #
# This section identifies and locates this script when executed.
# ========================================================================== #

# Get the base name of the script.
script_name=$(basename "$0")

# Get the full path to the script using realpath.
script_path=$(dirname "$(realpath "$0")")

# Change directory to $script_path.
cd $script_path

# Construct the full path to the script.
alias_path="$script_path/$script_name"

# -------------------------------------------------------------------------- #

# Define functions_dir.
functions_dir="$script_path/functions"
