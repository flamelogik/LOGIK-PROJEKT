
# -------------------------------------------------------------------------- #

# DISCLAIMER:       This file is part of LOGIK-PROJEKT.
#                   Copyright © 2024 silo 84
               
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
               
#                   Contact: brian@silo84.com

# -------------------------------------------------------------------------- #

# File Name:        download_aces_1_2_config.py
# Version:          0.0.1
# Created:          2024-11-03

"""
This script downloads the ACES 1.2 OpenColorIO (OCIO) configuration file from a specified URL.
It fetches the asset, extracts it, and modifies the downloaded files to keep only specified active views and displays.
The modifications include commenting out unwanted sections and adding a note with a timestamp and details of the changes made.

If run inside a PROJEKT, the script will download the files to the software/ocio folder. 
If run outside a PROJEKT, the files will be downloaded to the current directory.

Functions:
- download_and_extract_zip: Downloads and extracts a zip file from a given URL to a specified path.
- modify_ocio_file: Modifies the content of an OCIO configuration file to keep specified active views and displays.
- comment_out_unwanted_sections: Comments out unwanted sections in the OCIO configuration content.
- replace_section: Replaces a section in the OCIO configuration content with a new section containing only specified entries.

Example usage:
- Define the active views and displays to keep.
- Call the download_and_extract_zip function with the URL and destination directory.

References:
https://github.com/colour-science/OpenColorIO-Configs/releases/download/v1.2/OpenColorIO-Config-ACES-1.2.zip

"""

import os
import logging
from pathlib import Path
import re
import urllib.request
import zipfile
from typing import List
from datetime import datetime
import shutil

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# URL for the ACES 1.2 config
ACES_1_2_URL = "https://github.com/colour-science/OpenColorIO-Configs/releases/download/v1.2/OpenColorIO-Config-ACES-1.2.zip"

# get the path to the current projekt using $PROJEKT_PATH
PROJEKT_PATH = os.getenv('PROJEKT_PATH')
if PROJEKT_PATH is None:
    DESTINATION_DIR = Path(".")  # use current directory if $PROJEKT_PATH is not set
else:
    projekt_root = Path(PROJEKT_PATH)
    OCIO_DIR = projekt_root / 'software' / 'ocio'
    if not OCIO_DIR.exists():
        OCIO_DIR.mkdir(parents=True, exist_ok=True)
    DESTINATION_DIR = OCIO_DIR

logger.info(f"Destination directory: {DESTINATION_DIR}")

# Precompiled regex patterns
ACTIVE_DISPLAYS_PATTERN = re.compile(r'active_displays:\s*\[(.*?)\]', re.DOTALL)
ACTIVE_VIEWS_PATTERN = re.compile(r'active_views:\s*\[(.*?)\]', re.DOTALL)
DESCRIPTION_PATTERN = re.compile(r'description:\s*')


def download_and_extract_zip(url: str, destination_dir: Path):
    zip_path = destination_dir / "OpenColorIO-Config-ACES-1.2.zip"
    temp_extract_dir = destination_dir / "temp_extract"

    try:
        with urllib.request.urlopen(url) as response:
            if response.status == 200:
                zip_path.write_bytes(response.read())
            else:
                raise Exception(f"Failed to download file from {url}")
    except Exception as e:
        logger.warning(f"Error downloading file from {url}: {e}")
        return

    try:
        # Create a temporary extraction directory
        temp_extract_dir.mkdir(exist_ok=True)

        with zipfile.ZipFile(zip_path, 'r') as zip_ref:
            zip_ref.extractall(temp_extract_dir)

        # Move only the 'aces_1.2' folder to destination_dir
        aces_dir = temp_extract_dir / "OpenColorIO-Config-ACES-1.2" / "aces_1.2"
        if aces_dir.exists() and aces_dir.is_dir():
            shutil.move(str(aces_dir), destination_dir)


        logger.info(f"Extracted zip file to {destination_dir}")
    except Exception as e:
        logger.warning(f"Error extracting zip file {zip_path}: {e}")
    finally:
        # delete the zip file and temp extraction directory after extraction
        # Ensure all file operations are completed before deleting
        zip_ref.close()
        zip_path.unlink(missing_ok=True)
        shutil.rmtree(temp_extract_dir, ignore_errors=True)


def modify_ocio_file(file_path: Path, keep_active_views: List[str], keep_displays: List[str]):
    try:
        config_content = file_path.read_text()
        config_content = comment_out_unwanted_sections(config_content, keep_active_views, keep_displays)
        
        match = DESCRIPTION_PATTERN.search(config_content)
        if match:
            insert_pos = match.start()
            timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            note = (
                f"\n#  --------------------------------------------------------------------------------------\n"
                f"#  PROJEKT - OCIO config tweaks\n"
                f"#  config modified on {timestamp}\n"
                f"#  Change: Keep Active Views: {', '.join(keep_active_views)}\n"
                f"#  Change: Keep Displays: {', '.join(keep_displays)}\n"
                f"#  --------------------------------------------------------------------------------------\n"
            )
            config_content = config_content[:insert_pos] + note + config_content[insert_pos:]

        file_path.write_text(config_content)
        logger.info(f"File modified: {file_path}")
    except Exception as e:
        logger.warning(f"Error modifying file {file_path}: {e}")

def comment_out_unwanted_sections(config_content: str, keep_active_views: List[str], keep_displays: List[str]) -> str:
    config_content = replace_section(config_content, ACTIVE_DISPLAYS_PATTERN, keep_displays, "active_displays")
    config_content = replace_section(config_content, ACTIVE_VIEWS_PATTERN, keep_active_views, "active_views")
    return config_content

def replace_section(config_content: str, pattern: re.Pattern, keep_list: List[str], section_name: str) -> str:
    match = pattern.search(config_content)
    if match:
        section_content = match.group(1)
        entries = section_content.split(',')
        new_entries = [entry.strip() for entry in entries if entry.strip().strip('\'"') in keep_list]
        commented_section = f"# {section_name}: [{section_content}]"
        new_section = f"{section_name}: [{', '.join(new_entries)}]"
        config_content = config_content.replace(match.group(0), f"{commented_section}\n{new_section}")
    return config_content

# Main execution
if __name__ == "__main__":
    keep_active_views = ['sRGB', 'Rec.709', 'Raw', 'Log']
    keep_displays = ['ACES']

    download_and_extract_zip(ACES_1_2_URL, DESTINATION_DIR)

    # Modify the extracted .ocio file
    ocio_file_path = DESTINATION_DIR / "aces_1.2" / "config.ocio"
    if ocio_file_path.exists():
        modify_ocio_file(ocio_file_path, keep_active_views, keep_displays)
    
    logger.info("ACES 1.2 config download and modification complete.")