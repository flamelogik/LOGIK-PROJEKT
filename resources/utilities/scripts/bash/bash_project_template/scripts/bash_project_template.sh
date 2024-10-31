#!/bin/bash

# -------------------------------------------------------------------------- #

# DISCLAIMER:       This file is part of LOGIK-PROJEKT.
#                   Copyright © 2024 man-made-mekanyzms
                
#                   LOGIK-PROJEKT creates directories, files, scripts & tools
#                   for use with Autodesk Flame and other software.

#                   LOGIK-PROJEKT is free software.

#                   You can redistribute it and/or modify it under the terms
#                   of the GNU General Public License as published by the
#                   Free Software Foundation, either version 3 of the License,
#                   or any later version.
 
#                   This program is distributed in the hope that it will be
#                   useful, but WITHOUT ANY WARRANTY; without even the
#                   implied warranty of MERCHANTABILITY or FITNESS FOR A
#                   PARTICULAR PURPOSE.

#                   See the GNU General Public License for more details.

#                   You should have received a copy of the GNU General
#                   Public License along with this program.

#                   If not, see <https://www.gnu.org/licenses/>.
                
#                   Contact: phil_man@mac.com

# -------------------------------------------------------------------------- #

# File Name:        bash_project_template.sh
# Version:          0.0.0
# Language:         bash script

# Author:           Phil MAN - phil_man@mac.com
# Toolset:          MAN_MADE_MEKANYZMS: LOGIK-PROJEKT

# Created:          2024-01-01
# Modified:         2024-12-31
# Modifier:         Phil MAN - phil_man@mac.com

# License:          GNU General Public License v3.0

# Description:      This script is a template for bash projects.

# Installation:     Copy this script to your project directory.

# Changelist:       The full changelist is at the end of this document.

# -------------------------------------------------------------------------- #

# ========================================================================== #
# This section enables debugging and error tracing:.
# ========================================================================== #

# - 'set -e' Exit immediately if any command exits with a non-zero status.
# - 'set -x' Print each command to the terminal before executing it.
set -ex

# ========================================================================== #
# This section creates a decorative separator for blocks of text.
# ========================================================================== #

# Define a variable called 'separator'.
separator=$(printf '+ %s +' "$(printf -- '-%.0s' {1..75})")

# Define a variable called 'separator_hash'.
separator_hash=$(printf '# %s #' "$(printf -- '-%.0s' {1..74})")

# ========================================================================== #
# This section defines some date variables.
# ========================================================================== #

# Define 'today_underscore' (use underscores instead of hyphens)
today_underscore=$(date +%Y_%m_%d)

# Define 'now_underscore' (use underscores instead of hyphens)
now_underscore=$(date +%H_%M)

# ========================================================================== #
# This section locates the running script and the related directories.
# ========================================================================== #

# Get the directory of this script
path_to_here="$(dirname "$0")"

# Get the parent directory
parent_dir="$(dirname "$path_to_here")"

# Change directory to path_to_here
cd "$parent_dir" || exit

# -------------------------------------------------------------------------- #

# Set the cfg directory
cfg_dir="$parent_dir/cfg"

# Set the data directory
data_dir="$parent_dir/data"

# Set the docs directory
docs_dir="$parent_dir/docs"

# Set the license directory
license_dir="$parent_dir/license"

# Set the log directory
logs_dir="$parent_dir/logs"

# Set the preferences directory
prefs_dir="$parent_dir/prefs"

# Set the scripts directory
scripts_dir="$parent_dir/scripts"

# Set the version directory
version_dir="$parent_dir/version"

# ========================================================================== #
# This section defines the functionality.
# ========================================================================== #

# ========================================================================== #
# This section executes the main function.
# ========================================================================== #

# ========================================================================== #
# C2 A9 32 30 32 34 2D 4D 41 4E 2D 4D 41 44 45 2D 4D 45 4B 41 4E 59 5A 4D 53 #
# ========================================================================== #

# Changelist:

# -------------------------------------------------------------------------- #
