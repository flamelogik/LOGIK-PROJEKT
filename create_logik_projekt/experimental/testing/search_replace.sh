#!/bin/bash

set -ex

search_dir="/JOBS/dry_run_01/shots"
search_string="/JOBS/dry_run_01/shots//JOBS/dry_run_01/shots/"
replace_string="/JOBS/dry_run_01/shots/"

# Find all .nk files recursively in the search directory
files=$(find "$search_dir" -type f -name "*.nk")

# Iterate over each file and perform the replacement using sed
for file in $files; do
    sed -i "s|$search_string|$replace_string|g" "$file"
done

echo "Replacement completed."
