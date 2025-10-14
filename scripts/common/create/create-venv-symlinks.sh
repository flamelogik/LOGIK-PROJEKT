#!/bin/bash
# symlink-generator.sh
# Generates utility script for creating symlinks between Autodesk and virtual environment

# -------------------------------------------------------------------------- #
# Script Execution Options
# -------------------------------------------------------------------------- #

# Uncomment these settings for stricter bash execution
set -e     # Exit on any errors
# set -u     # Exit if any variable is used without being defined
# set -o pipefail  # Exit if any command in a pipeline fails
# set -x     # Print each command before execution

# -------------------------------------------------------------------------- #
# Symlink Generator Functions
# -------------------------------------------------------------------------- #

function create_python_symlinks_script() {
    echo "Creating symlinks script at: $symlinks_script"

    cat > "$symlinks_script" << 'EOF'
#!/usr/bin/env python
# Script to create symlinks from Autodesk site-packages to virtual environment
import os
import site
import sys
import shutil
from pathlib import Path

def create_symlinks(source_site_packages, target_site_packages):
    print(f"Source site-packages: {source_site_packages}")
    print(f"Target site-packages: {target_site_packages}")

    if not os.path.exists(source_site_packages):
        print(f"Error: Source directory does not exist: {source_site_packages}")
        return False

    if not os.path.exists(target_site_packages):
        print(f"Error: Target directory does not exist: {target_site_packages}")
        return False

    # Get list of packages in source directory
    source_packages = []
    for item in os.listdir(source_site_packages):
        if item.startswith('__') or item == 'easy-install.pth':
            continue
        source_packages.append(item)

    print(f"Found {len(source_packages)} packages in source directory")

    # Create symlinks
    created_links = 0
    skipped_links = 0
    for package in source_packages:
        source_path = os.path.join(source_site_packages, package)
        target_path = os.path.join(target_site_packages, package)

        if os.path.exists(target_path):
            print(f"  Skipping {package} - already exists in target")
            skipped_links += 1
            continue

        try:
            # For directories and files, create a symlink
            os.symlink(source_path, target_path)
            print(f"  Created symlink for {package}")
            created_links += 1
        except Exception as e:
            print(f"  Error creating symlink for {package}: {e}")

    print(f"Created {created_links} symlinks, skipped {skipped_links} packages")
    return True

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python create_symlinks.py <source_site_packages> <target_site_packages>")
        sys.exit(1)

    source_site_packages = sys.argv[1]
    target_site_packages = sys.argv[2]

    success = create_symlinks(source_site_packages, target_site_packages)
    sys.exit(0 if success else 1)
EOF

    chmod +x "$symlinks_script"
}

# -------------------------------------------------------------------------- #
# Changelist:
# -------------------------------------------------------------------------- #