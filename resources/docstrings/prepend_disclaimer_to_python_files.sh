#!/bin/bash

# This script prepends a disclaimer to all Python files 
# in a specified directory and its subdirectories.
# It also logs the process to a file.

# Set paths
parent_dir="/home/pman/workspace/GitHub/projekt_app"
disclaimer_file="$parent_dir/resources/docstrings/disclaimer.txt"
disclaimer_log="$parent_dir/resources/docstrings/prepend_disclaimer_log.txt"
python_modules="$parent_dir/modules/widgets"

# Ensure disclaimer_log exists
touch "$disclaimer_log"

# Start logging
echo "---- Starting disclaimer prepend process ----" >> "$disclaimer_log"
echo "Timestamp: $(date)" >> "$disclaimer_log"
echo "" >> "$disclaimer_log"

# Check if disclaimer_file exists
if [ ! -f "$disclaimer_file" ]; then
    echo "Error: Disclaimer file does not exist." | tee -a "$disclaimer_log"
    exit 1
fi

# Read disclaimer text
disclaimer_text=$(cat "$disclaimer_file")

# Iterate through each Python file in the directory and its subdirectories
find "$python_modules" -type f -name "*.py" | while read -r python_file; do
    # Read the existing content of the Python file
    existing_content=$(cat "$python_file")
    
    # Combine the disclaimer and the existing content
    updated_content="$disclaimer_text"$'\n'"$existing_content"

    # Write the updated content back to the Python file
    if echo "$updated_content" > "$python_file"; then
        echo "Successfully updated: $python_file" | tee -a "$disclaimer_log"
    else
        echo "Failed to update: $python_file" | tee -a "$disclaimer_log"
    fi
done

# Finish logging
echo "" >> "$disclaimer_log"
echo "---- Disclaimer prepend process completed ----" >> "$disclaimer_log"
echo "Timestamp: $(date)" >> "$disclaimer_log"
