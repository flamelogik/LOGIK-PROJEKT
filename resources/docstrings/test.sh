#!/bin/bash

# This script prepends a disclaimer to all Python files 
# in a specified directory and its subdirectories.
# It also logs the process to a file.

# Get the directory of the running script
path_to_here="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"

# Set paths
parent_dir="$(dirname $(dirname "$path_to_here"))"
resources_dir="$parent_dir/resources"
docstrings_dir="$resources_dir/docstrings"
disclaimer_file="$docstrings_dir/disclaimer.txt"
disclaimer_log="$docstrings_dir/prepend_disclaimer_log.txt"
modules_dir="$parent_dir/modules"

echo "$path_to_here"
echo "$parent_dir"
echo "$resources_dir"
echo "$docstrings_dir"
echo "$disclaimer_file"
echo "$disclaimer_log"
echo "$modules_dir"
