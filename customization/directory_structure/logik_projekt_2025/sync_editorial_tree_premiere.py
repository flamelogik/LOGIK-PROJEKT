#

# -------------------------------------------------------------------------- #

# DISCLAIMER:       This file is part of LOGIK-PROJEKT.
#                   Copyright © 2024 man-made-mekanyzms
                
#                   LOGIK-PROJEKT creates directories, files, scripts & tools
#                   LOGIK-PROJEKT creates editorial_dirs_premiere, files, scripts & tools
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

# File Name:        sync_editorial_tree_premiere_working.py
# Version:          0.9.0
# Created:          2024-10-31
# Modified:         2024-10-31

# ========================================================================== #
# This section defines the import statements and directory paths.
# ========================================================================== #

# Standard library imports
import argparse
import datetime
import json
import os
import platform
import shutil
import sys

# -------------------------------------------------------------------------- #

def get_base_path():
    if getattr(sys, 'frozen', False):
        return sys._MEIPASS
    else:
        return os.path.abspath(
            os.path.join(
                os.path.dirname(__file__), '..', '..', '..'
            )
        )
    
# -------------------------------------------------------------------------- #

def get_resource_path(relative_path):
    base_path = get_base_path()
    return os.path.join(
        base_path,
        relative_path
    )

# -------------------------------------------------------------------------- #

# Set the path to the 'modules' directory
modules_dir = get_resource_path('modules')

# Set the path to the 'resources' directory
resources_dir = get_resource_path('resources')

# Append the modules path to the system path
if modules_dir not in sys.path:
    sys.path.append(modules_dir)

# ========================================================================== #
# This section defines environment specific variables.
# ========================================================================== #

# These paths should be passed from the main app.
the_hostname = "delta"
the_projekt_os = "Linux"
the_software_version = "premiere_2024"
the_sanitized_version = "2024"
the_framestore = "stonefs"

# ========================================================================== #
# This section defines common paths.
# ========================================================================== #

projekt_roots_config_path = os.path.join(
    resources_dir,
    'cfg',
    'projekt_configuration',
    'roots',
    'projekt_roots.json'
)

# Read the JSON configuration file
try:
    with open(projekt_roots_config_path, 'r') as config_file:
        config = json.load(config_file)
except Exception as e:
    print(f"  Error reading JSON configuration file: {e}")
    config = {}

# Define common directory paths
the_projekts_dir = config.get(
    'the_projekts_dir',
    "/PROJEKTS"
)

# ========================================================================== #
# This section defines projekt specific paths.
# ========================================================================== #

# These paths should be passed from the main app.

the_projekt_name = "8888_new_job"
the_projekt_flame_name = f"{the_projekt_name}_{the_sanitized_version}"

separator = '# ' + '-' * 75 + ' #'

# ========================================================================== #
# This section defines the primary functions for the script.
# ========================================================================== #

def sync_editorial_tree_premiere(
        the_projekts_dir,
        the_projekt_name,
        the_projekt_flame_name,
        separator
    ):
    """
    Function to create the directory structure for Premiere projects,
    set up symbolic links to asset directories, and copy template resources.
    """
    
    # # Nested function to generate backup name with current date
    # def generate_backup_name(path):
    #     date_str = datetime.datetime.now().strftime("%Y_%m_%d")
    #     return f"{path}.{date_str}.bak"

    # Define the base paths
    projekt_base = os.path.join(the_projekts_dir, the_projekt_name)
    premiere_dir = os.path.join(projekt_base, 'editorial', 'adobe_premiere')
    resources_base = get_resource_path("resources")

    # # Define the main directory structure
    # premiere_folders = [
    #     "01_projekts",
    #     "02_footage",
    #     "03_audio",
    #     "04_gfx",
    #     "05_stills",
    #     "06_color",
    #     "07_misc",
    #     "08_postings"
    # ]

    # Define the main directory structure
    premiere_folders = [
        "02_footage",
        "03_audio",
        "04_gfx",
        "05_stills",
        "06_color",
        "07_misc",
        "08_postings"
    ]

    # Define subfolders and their corresponding symbolic links
    symbolic_links = [
        # Footage links
        {"src": f"{projekt_base}/assets/footage", "dst": f"{premiere_dir}/02_footage/03_misc"},
        {"src": f"{projekt_base}/assets/footage/graded", "dst": f"{premiere_dir}/02_footage/05_graded"},
        {"src": f"{projekt_base}/assets/footage/raw", "dst": f"{premiere_dir}/02_footage/04_raw"},
        {"src": f"{projekt_base}/assets/footage/stock", "dst": f"{premiere_dir}/02_footage/02_stock"},
        {"src": f"{projekt_base}/assets/footage/transcodes", "dst": f"{premiere_dir}/02_footage/01_transcodes"},
        # Audio links
        {"src": f"{projekt_base}/assets/audio/mix", "dst": f"{premiere_dir}/03_audio/01_mix"},
        {"src": f"{projekt_base}/assets/audio/music", "dst": f"{premiere_dir}/03_audio/02_music"},
        {"src": f"{projekt_base}/assets/audio/sound_effects", "dst": f"{premiere_dir}/03_audio/03_sfx"},
        {"src": f"{projekt_base}/assets/audio/voiceover", "dst": f"{premiere_dir}/03_audio/04_vo"},
        {"src": f"{projekt_base}/assets/audio/production", "dst": f"{premiere_dir}/03_audio/05_production"},
        # Graphics links
        {"src": f"{projekt_base}/assets/graphics", "dst": f"{premiere_dir}/04_gfx/01_aftereffects"},
        {"src": f"{projekt_base}/assets/graphics", "dst": f"{premiere_dir}/04_gfx/02_input"},
        {"src": f"{projekt_base}/assets/graphics", "dst": f"{premiere_dir}/04_gfx/03_output"},
        # Stills links
        {"src": f"{projekt_base}/assets/photoshop", "dst": f"{premiere_dir}/05_stills/01_photoshop"},
        {"src": f"{projekt_base}/assets/images", "dst": f"{premiere_dir}/05_stills/02_images"},
        {"src": f"{projekt_base}/assets/supers", "dst": f"{premiere_dir}/05_stills/03_supers"},
        {"src": f"{projekt_base}/assets/legal", "dst": f"{premiere_dir}/05_stills/04_legal"},
        # Postings links
        {"src": f"{projekt_base}/work_in_progress/postings", "dst": f"{premiere_dir}/08_postings/01_postings"},
        {"src": f"{projekt_base}/masters", "dst": f"{premiere_dir}/08_postings/02_masters"}
    ]

    # Define template directories to copy
    template_dirs = [
        {
            "src": os.path.join(resources_base, "adobe/premiere/premiere_templates/premiere_projekts"),
            "dst": f"{premiere_dir}/01_projekts"
        },
        {
            "src": os.path.join(resources_base, "adobe/premiere/premiere_presets/premiere_export_presets"),
            "dst": f"{premiere_dir}/07_misc/01_export_presets"
        },
        {
            "src": os.path.join(resources_base, "adobe/premiere/premiere_fonts"),
            "dst": f"{premiere_dir}/07_misc/02_fonts"
        },
        {
            "src": os.path.join(resources_base, "adobe/premiere/premiere_scripts"),
            "dst": f"{premiere_dir}/07_misc/03_scripts"
        },
        {
            "src": os.path.join(resources_base, "adobe/premiere/premiere_templates/premiere_slates"),
            "dst": f"{premiere_dir}/07_misc/04_slates"
        },
        {
            "src": os.path.join(resources_base, "adobe/premiere/premiere_notes"),
            "dst": f"{premiere_dir}/07_misc/05_notes"
        },
        {
            "src": os.path.join(resources_base, "adobe/premiere/premiere_templates/premiere_aspect_ratio_masks"),
            "dst": f"{premiere_dir}/07_misc/06_aspect_ratio_masks"
        }
    ]

    print("  Creating Premiere project directory structure.\n")

    # Set the umask to 0 to ensure proper permissions
    os.umask(0)

    # Create the base premiere directory if it doesn't exist
    os.makedirs(premiere_dir, exist_ok=True)

    # Create main folders
    for folder in premiere_folders:
        folder_path = os.path.join(premiere_dir, folder)
        
        # # If directory exists, back it up
        # if os.path.exists(folder_path):
        #     backup_path = generate_backup_name(folder_path)
        #     print(f"  * {folder_path} exists")
        #     print(f"  * Backing up directory to:")
        #     print(f"  *   {backup_path}")
        #     shutil.move(folder_path, backup_path)
        #     print()

        # Create the directory
        os.makedirs(folder_path, exist_ok=True)  # Addendum: exist_ok=True

        print(f"  Created directory: {folder_path}")

    print("\n  Creating symbolic links...")

    # Create symbolic links
    for link in symbolic_links:
        src_path = link["src"]
        dst_path = link["dst"]

        # Create parent directory if it doesn't exist
        os.makedirs(os.path.dirname(dst_path), exist_ok=True)

        # # Remove existing symlink if it exists
        # if os.path.islink(dst_path):
        #     backup_path = generate_backup_name(dst_path)
        #     print(f"  * Existing symlink found: {dst_path}")
        #     print(f"  * Backing up to: {backup_path}")
        #     os.rename(dst_path, backup_path)
        #     print()

        # Remove existing symlink if it exists
        if os.path.islink(dst_path):
            os.unlink(dst_path)

        # Create the symbolic link
        try:
            if os.path.exists(src_path):
                os.symlink(src_path, dst_path)
                print(f"  Created symlink: {dst_path} -> {src_path}")
            else:
                print(f"  Warning: Source path does not exist: {src_path}")
        except Exception as e:
            print(f"  Error creating symlink {dst_path}: {str(e)}")

    print("\n  Copying template directories...")

    # Copy template directories
    for template in template_dirs:
        src_path = template["src"]
        dst_path = template["dst"]

        # Create parent directory if it doesn't exist
        os.makedirs(os.path.dirname(dst_path), exist_ok=True)

        # # If destination exists, back it up
        # if os.path.exists(dst_path):
        #     backup_path = generate_backup_name(dst_path)
        #     print(f"  * {dst_path} exists")
        #     print(f"  * Backing up directory to:")
        #     print(f"  *   {backup_path}")
        #     shutil.move(dst_path, backup_path)
        #     print()

        # Remove existing directory if it exists
        if os.path.exists(dst_path):
            shutil.rmtree(dst_path)

        # Copy the directory
        try:
            if os.path.exists(src_path):
                shutil.copytree(src_path, dst_path)
                print(f"  Copied directory: {src_path} -> {dst_path}")
            else:
                print(f"  Warning: Source template directory does not exist: {src_path}")
        except Exception as e:
            print(f"  Error copying directory {src_path}: {str(e)}")

    print("\n  Premiere project directory structure, symbolic links, and templates created successfully.")
    print(f"  Location: {premiere_dir}")

# ========================================================================== #
# This section defines how to handle the main script function.
# ========================================================================== #

def main():
    separator = "-" * 80

    # Call the main sync function
    sync_editorial_tree_premiere(
        the_projekts_dir,
        the_projekt_name,
        the_projekt_flame_name,
        separator
    )

if __name__ == "__main__":
    main()

# ========================================================================== #
# C2 A9 32 30 32 34 2D 4D 41 4E 2D 4D 41 44 45 2D 4D 45 4B 41 4E 59 5A 4D 53 #
# ========================================================================== #

# Changelist:       

# -------------------------------------------------------------------------- #
# version:          0.0.1
# created:          2024-01-19 - 12:34:56
# comments:         scripts to create flame projekts, presets & templates.
# -------------------------------------------------------------------------- #
# version:          0.1.0
# modified:         2024-04-20 - 16:20:00
# comments:         refactored monolithic program into separate functions.
# -------------------------------------------------------------------------- #
# version:          0.5.0
# modified:         2024-05-24 - 20:24:00
# comments:         merged flame_colortoolkit with projekt.
# -------------------------------------------------------------------------- #
# version:          0.6.0
# modified:         2024-05-25 - 15:00:03
# comments:         started conversion to python3.
# -------------------------------------------------------------------------- #
# version:          0.7.0
# modified:         2024-06-21 - 18:21:03
# comments:         started gui design with pyside6.
# -------------------------------------------------------------------------- #
# version:          0.9.9
# modified:         2024-08-31 - 16:51:09
# comments:         prep for release - code appears to be functional
# -------------------------------------------------------------------------- #
