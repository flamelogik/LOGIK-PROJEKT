#!bin/bash

# Set editorial_dir
editorial_dir = "$PROJEKT_NAME/editorial"

# Set davinci_resolve_dir
davinci_resolve_dir = "$editorial_dir/davinci_resolve"

# Set final_cut_pro_dir
final_cut_pro_dir = "$editorial_dir/final_cut_pro"

# Set premiere_dir
premiere_dir = "$editorial_dir/premiere"

# Set the target_dirs
target_dirs=(
    "$davinci_reolve_dir"
    "$final_cut_pro_dir"
    "$premiere_dir"
)

# Set the sub_dirs
subdirs=(
    "01_projekts"
    "02_footage"
    "03_audio"
    "04_gfx"
    "05_stills"
    "06_color"
    "07_misc"
    "08_postings"
)

# Create each subdirectory in each target directory
for base_dir in "${target_dirs[@]}"; do
    for subdir in "${subdirs[@]}"; do
        mkdir -p "$base_dir/$subdir"
        echo "Created subdirectory: $base_dir/$subdir"
    done
done

echo "All subdirectories created successfully."
