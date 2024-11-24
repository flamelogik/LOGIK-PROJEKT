#!/bin/bash

# Define the target file
target_file="customization/directory_structure/O2_pos/resources/cfg/projekt_configuration/tree/projekt/docs.json"

# Define the search_replace_pairs array file
search_replace_pairs_file="customization/directory_structure/O2_pos/resources/utilities/scripts/bash/search_replace_pairs.txt"

# Read the search_replace_pairs.txt file and perform replacements
while IFS= read -r line; do
    search=$(echo "$line" | cut -d':' -f1)
    replace=$(echo "$line" | cut -d':' -f2)
    sed -i "s/$search/$replace/g" "$target_file"
done < "$search_replace_pairs_file"