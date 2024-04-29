#!/bin/bash

set -ex

# Define the target directory
tgt_dir='/home/pman/workspace/GitHub/FLAME-DEPLOYMENT/programs/flame_project_creation/setups/batch/pref'

# Loop through files ending with ".batch" in the target directory
for file in "$tgt_dir"/*.batch; do
    # Check if the file exists and is readable
    if [ -f "$file" ] && [ -r "$file" ]; then
        # Replace the string "2025.pr193" with "2025" using sed
        # sed -i 's/2025\.pr193/2025/g' "$file"

        # Replace the string "<BatchLength>266</BatchLength>" with "<BatchLength>100</BatchLength>"
        # sed -i 's/<BatchLength>266<\/BatchLength>/<BatchLength>100<\/BatchLength>/g' "$file"

        # Replace the string "test30_test30" with "flame_beta" using sed
        # sed -i 's/test30_test30/flame_beta/g' "$file"

        # Replace the string "<BatchUser>pman</BatchUser>" with "<BatchUser>Philip_Che_Sung_MAN</BatchUser>"
        sed -i 's/<BatchUser>pman<\/BatchUser>/<BatchUser>Philip_Che_Sung_MAN<\/BatchUser>/g' "$file"

        # Replace the string "pman_pr193" with "pman" using sed
        # sed -i 's/pman_pr193/pman/g' "$file"

        echo "String replaced in file: $file"
    else
        echo "Error: File $file does not exist or is not readable."
    fi
done
