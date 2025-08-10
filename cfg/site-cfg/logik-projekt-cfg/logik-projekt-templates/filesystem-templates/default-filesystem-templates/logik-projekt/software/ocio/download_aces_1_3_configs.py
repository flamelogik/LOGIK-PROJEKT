
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

# File Name:        download_aces_1_3_configs.py
# Version:          0.0.2
# Created:          2024-11-03
# Modified:         2024-11-06

# -------------------------------------------------------------------------- #

"""
This script downloads and modifies OpenColorIO (OCIO) configuration files from a specified GitHub repository.
It fetches assets based on tags, platform data, and configuration data, and then modifies the downloaded files
to keep only specified active views and displays. The modifications include commenting out unwanted sections
and adding a note with a timestamp and details of the changes made.

If run inside a PROJEKT, the script will download the files to the software/ocio folder.
If run outside a PROJEKT, the files will be downloaded to the current directory.

Functions:
- download_assets: Downloads assets for a given tag and processes them based on platform and configuration data.
- download_file: Downloads a file from a given URL to a specified path.
- modify_ocio_file: Modifies the content of an OCIO configuration file to keep specified active views and displays.
- comment_out_unwanted_sections: Comments out unwanted sections in the OCIO configuration content.
- replace_section: Replaces a section in the OCIO configuration content with a new section containing only specified entries.

Example usage:
- Define the active views and displays to keep.
- Call the download_assets function for each tag in TAG_DATA.

Setup:
Modify the tag, platform_data, and config_data variables to match the desired VFX Reference Platform.

References:
https://github.com/AcademySoftwareFoundation/OpenColorIO-Config-ACES/releases

"""

import os
import logging
from pathlib import Path
import re
import json
import urllib.request
from typing import List, Dict
from datetime import datetime

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# ========================================================================== #
# This section defines the release tags, VFX Reference Platform , and configs to download.
# ========================================================================== #
# Select a tag to download the ocio configs from
TAG_DATA = [
    'v2.1.0-v2.2.0'
]

# VFX RP lines up to the OCIO versions as follows:
PLATFORM_DATA = {
    # "CY2024": "2.3.x", # Nuke XX.X
    "CY2023": "2.2.x",  # Nuke 15.1, 15.0
    "CY2022": "2.1.x",  # Nuke 14.1, 14.0
    # "CY2021": "2.0.x"  # Nuke 13.0
}

# Options are: cg-config, studio-config, reference-config
CONFIG_DATA = ['cg-config', 'studio-config']

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

# ========================================================================== #
# This section defines precompiled regex patterns used in the script.
# ========================================================================== #
# Precompiled regex patterns
ACTIVE_DISPLAYS_PATTERN = re.compile(r'active_displays:\s*\[(.*?)\]', re.DOTALL)
ACTIVE_VIEWS_PATTERN = re.compile(r'active_views:\s*\[(.*?)\]', re.DOTALL)
DESCRIPTION_PATTERN = re.compile(r'description:\s*\|')
OCIO_VERSION_PATTERN = re.compile(r'ocio-v(\d+\.\d+)')

# ========================================================================== #
# This section downloads the assets for a given tag and processes them based on platform and configuration data.
# ========================================================================== #

def download_assets(
    tag: str,
    platform_data: Dict[str, str],
    config_data: List[str],
    keep_active_views: List[str],
    keep_displays: List[str],
    destination_dir: Path
) -> int:
    url = f"https://api.github.com/repos/AcademySoftwareFoundation/OpenColorIO-Config-ACES/releases/tags/{tag}"
    logger.info(f"Downloading assets for tag: {tag}")
    downloaded_count = 0
    try:
        with urllib.request.urlopen(url) as response:
            if response.status != 200:
                raise Exception(f"Failed to fetch data from {url}")
            release_data = json.loads(response.read().decode())
    except Exception as e:
        logger.warning(f"Error fetching assets: {e}")
        return downloaded_count

    assets = release_data.get('assets', [])

    for asset in assets:
        asset_name = asset['name']
        if any(asset_name.startswith(config) for config in config_data):
            ocio_version = OCIO_VERSION_PATTERN.search(asset_name)
            if ocio_version:
                version = ocio_version.group(1)
                logger.info(f"Found OCIO version: {version} in asset: {asset_name}")
                matched = False
                for year, version_pattern in platform_data.items():
                    if re.match(rf"{version_pattern.split('.')[0]}\.{version_pattern.split('.')[1]}", version):
                        folder = destination_dir / f"{year}-{version_pattern}"
                        folder.mkdir(parents=True, exist_ok=True)
                        download_url = asset['browser_download_url']
                        download_path = folder / asset_name
                        download_file(download_url, download_path)
                        modify_ocio_file(download_path, keep_active_views, keep_displays)
                        matched = True
                        downloaded_count += 1
                        break
                if not matched:
                    logger.info(f"No matching platform data for OCIO version: {version} in asset: {asset_name}")
            else:
                logger.info(f"No OCIO version found in asset: {asset_name}")
    return downloaded_count

# -------------------------------------------------------------------------- #

def download_file(url: str, path: Path):
    try:
        with urllib.request.urlopen(url) as response:
            if response.status == 200:
                path.write_bytes(response.read())
            else:
                raise Exception(f"Failed to download file from {url}")
    except Exception as e:
        logger.warning(f"Error downloading file from {url}: {e}")

# ========================================================================== #
# This section modifies the content of an OCIO configuration file to keep specified active views and displays.
# ========================================================================== #

def modify_ocio_file(file_path: Path, keep_active_views: List[str], keep_displays: List[str]):
    try:
        config_content = file_path.read_text()
        config_content = comment_out_unwanted_sections(config_content, keep_active_views, keep_displays)

        match = DESCRIPTION_PATTERN.search(config_content)
        if match:
            insert_pos = match.end()
            timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            note = (
                f"\n  --------------------------------------------------------------------------------------\n"
                f"  PROJEKT - OCIO config tweaks\n"
                f"  config modified on {timestamp}\n"
                f"  Change: Keep Active Views: {', '.join(keep_active_views)}\n"
                f"  Change: Keep Displays: {', '.join(keep_displays)}\n"
                f"  --------------------------------------------------------------------------------------\n"
            )



            config_content = config_content[:insert_pos] + note + config_content[insert_pos:]

        file_path.write_text(config_content)
        logger.info(f"File modified: {file_path}")
    except Exception as e:
        logger.warning(f"Error modifying file {file_path}: {e}")

# -------------------------------------------------------------------------- #

def comment_out_unwanted_sections(config_content: str, keep_active_views: List[str], keep_displays: List[str]) -> str:
    config_content = replace_section(config_content, ACTIVE_DISPLAYS_PATTERN, keep_displays, "active_displays")
    config_content = replace_section(config_content, ACTIVE_VIEWS_PATTERN, keep_active_views, "active_views")
    return config_content

# -------------------------------------------------------------------------- #

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

# -------------------------------------------------------------------------- #


# ========================================================================== #
# This section is the main execution of the script.
# ========================================================================== #
# Main execution
if __name__ == "__main__":
    keep_active_views = ['ACES 1.0 - SDR Video', 'Un-tone-mapped', 'Raw']
    keep_displays = ['sRGB - Display', 'Rec.1886 Rec.709 - Display']

    total_downloaded = 0
    for tag in TAG_DATA:
        total_downloaded += download_assets(tag, PLATFORM_DATA, CONFIG_DATA, keep_active_views, keep_displays, DESTINATION_DIR)

    logger.info(f"Total .ocio assets downloaded: {total_downloaded}")

# -------------------------------------------------------------------------- #

# ========================================================================== #
# 53 54 52 45 4E 47 54 48 2D 49 4E 2D 4E 55 4D 42 45 52 53 C2 A9 32 30 32 35 #
# ========================================================================== #
