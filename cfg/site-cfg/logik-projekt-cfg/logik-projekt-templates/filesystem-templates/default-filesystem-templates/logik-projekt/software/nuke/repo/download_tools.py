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
# File Name:        download_tools.py
# Version:          0.0.4
# Created:          2024-11-03
# Modified:         2024-11-08
# -------------------------------------------------------------------------- #

"""
This script downloads and extracts tools and scripts from specified
GitHub repositories and zip URLs. It sets up logging to track the process
and includes functions to:

1. Download and extract zip files from given URLs with retry logic.
2. Download the latest release from specified GitHub repositories.
3. Process lists of repository and zip URLs and track them for updates.
4. Create an `init.py` and `menu.py` file with `nuke.pluginAddPath()`
   statements based on the extracted directories.
"""

from pathlib import Path
import urllib.request
import zipfile
import io
import logging
import time
from typing import Dict, Optional


# ========================================================================== #
# This section and sets up the logger.
# ========================================================================== #
logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

# File and stream handlers
file_handler = logging.FileHandler('download_tools.log', mode='w')
stream_handler = logging.StreamHandler()
formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
file_handler.setFormatter(formatter)
stream_handler.setFormatter(formatter)
logger.addHandler(file_handler)
logger.addHandler(stream_handler)


# ========================================================================== #
# This section contains the URLs for repositories and zip files.
# ========================================================================== #
# github releases
repo_urls = {
    "https://github.com/CreativeLyons/NukeSurvivalToolkit_publicRelease": "init",
    "https://github.com/adrianpueyo/Stamps": "menu",
    "https://github.com/adrianpueyo/KnobScripter": "menu"
}

# tools distributed as zip files
zip_urls = {
    "https://github.com/xbourque/pixelfudger/raw/main/downloads/pixelfudger_3.2v1_nov_2023.zip": "init"
}

# list of directories to avoid drilling down into when creating the menu and init files
no_drill_down_list = ["KnobScripter"]
# ========================================================================== #
# This section contains the dictionaries for the `init.py` and `menu.py` files.
# ========================================================================== #

menu_py_items: Dict[str, str] = {}
init_py_items: Dict[str, str] = {}

# ========================================================================== #
# This section deletes existing init.py and menu.py files from the current directory.
# ========================================================================== #

def delete_existing_files() -> None:
    """
    Deletes 'menu.py' and 'init.py' files from the current directory.

    This function iterates through all items in the current working directory.
    If an item is a file and its name is either 'menu.py' or 'init.py', the file
    is deleted. A log entry is created for each deleted file.
    """
    for item in Path.cwd().iterdir():
        if item.is_file() and item.name in ["menu.py", "init.py"]:
            item.unlink()
            logger.info(f"Deleted {item}")

# ========================================================================== #
# This section contains the function to fetch content from a URL with retries.
# ========================================================================== #

def fetch_url_with_retries(url: str, retries: int = 3, delay: int = 5) -> Optional[bytes]:
    """
    Attempts to fetch content from a URL with a specified number of retries and delay between attempts.

    Args:
        url (str): The URL to fetch content from.
        retries (int, optional): The number of retry attempts. Defaults to 3.
        delay (int, optional): The delay in seconds between retry attempts. Defaults to 5.

    Returns:
        Optional[bytes]: The content fetched from the URL as bytes if successful, otherwise None.
    """
    for attempt in range(retries):
        try:
            with urllib.request.urlopen(url, timeout=10) as response:
                if response.status == 200:
                    return response.read()
        except Exception as e:
            logger.warning(f"Attempt {attempt + 1} failed for URL {url}: {e}")
            time.sleep(delay)
    logger.error(f"All retries failed for URL: {url}")
    return None

# ========================================================================== #
# This section contains the function to move files from a temporary directory to a final directory.
# ========================================================================== #

def add_extracted_dir(temp_dir: Path, final_dir: Path) -> None:
    """
    Moves all files and directories from a temporary directory to a final directory,
    then removes the temporary directory and its contents.
    Args:
        temp_dir (Path): The temporary directory containing files and directories to be moved.
        final_dir (Path): The destination directory where files and directories will be moved to.
    Returns:
        None
    """
    for item in temp_dir.iterdir():
        if item.is_dir():
            for sub_item in item.iterdir():
                sub_item.rename(final_dir / sub_item.name)
        else:
            item.rename(final_dir / item.name)
    # Remove temp_dir and its contents
    for item in temp_dir.iterdir():
        if item.is_dir():
            for sub_item in item.iterdir():
                sub_item.unlink()
            item.rmdir()
        else:
            item.unlink()
    temp_dir.rmdir()

# ========================================================================== #
# This section contains the function to download and extract a zip file.
# ========================================================================== #

def download_and_extract_zip(zip_url: str, final_dir: str) -> None:
    """
    Downloads a ZIP file from the given URL and extracts its contents to the specified directory.
    If the URL is from GitHub and does not end with "?raw=true", this suffix is appended to the URL.
    Args:
        zip_url (str): The URL of the ZIP file to download.
        final_dir (str): The directory where the contents of the ZIP file will be extracted.
    Returns:
        None
    Raises:
        Exception: If there is an error during the extraction process.
    Logs:
        Info: When the ZIP file is successfully extracted.
        Error: If the ZIP file cannot be downloaded or if there is an error during extraction.
    """
    if "github.com" in zip_url and not zip_url.endswith("?raw=true"):
        zip_url += "?raw=true"

    zip_content = fetch_url_with_retries(zip_url)
    if zip_content:
        try:
            with zipfile.ZipFile(io.BytesIO(zip_content)) as z:
                temp_dir = Path(final_dir) / "temp"
                temp_dir.mkdir(parents=True, exist_ok=True)
                z.extractall(temp_dir)
                add_extracted_dir(temp_dir, Path(final_dir))
            logger.info(f"Extracted {zip_url} to {final_dir}")
        except Exception as e:
            logger.error(f"Error extracting {zip_url}: {e}")
    else:
        logger.error(f"Failed to download zip from {zip_url}")

# ========================================================================== #
# This section contains the function to download the latest release from a GitHub repository.
# ========================================================================== #

def download_latest_release(repo_url: str) -> Optional[str]:
    """
    Download the latest release from a GitHub repository.
    Args:
        repo_url (str): The URL of the GitHub repository.
    Returns:
        Optional[str]: The directory name where the release was extracted, or None if the download failed.
    Raises:
        Exception: If there is an error fetching the release information or downloading the release.
    """
    owner, repo = repo_url.rstrip('/').split('/')[-2:]
    release_url = f"https://github.com/{owner}/{repo}/releases/latest"

    try:
        with urllib.request.urlopen(release_url, timeout=10) as response:
            tag_name = response.geturl().split('/')[-1]
            zip_url = f"https://github.com/{owner}/{repo}/archive/refs/tags/{tag_name}.zip"
            final_dir = f"{repo}_{tag_name}"

            if Path(final_dir).exists():
                logger.info(f"Directory {final_dir} already exists. Skipping download.")
                return final_dir
            download_and_extract_zip(zip_url, final_dir)
            return final_dir
    except Exception as e:
        logger.error(f"Failed to fetch release information: {e}")
    return None

# ========================================================================== #
# This section contains the function to add a directory to a dictionary.
# ========================================================================== #

def add_item_to_dict(item_dict: Dict[str, str], final_dir: str, key: str) -> None:
    """
    Adds a key-value pair to a dictionary if the key does not already exist.

    Args:
        item_dict (Dict[str, str]): The dictionary to add the item to.
        final_dir (str): The key to check in the dictionary.
        key (str): The value to associate with the key if the key does not exist.

    Returns:
        None
    """
    if final_dir not in item_dict:
        item_dict[final_dir] = key

# ========================================================================== #
# This section contains the function to process repository URLs.
# ========================================================================== #

def process_repo_urls(repo_urls: Dict[str, str]) -> None:
    """
    Process a dictionary of repository URLs and add the processed data to respective dictionaries.

    Args:
        repo_urls (Dict[str, str]): A dictionary where the keys are repository URLs and the values are
                                    strings indicating the type of processing ('init' or other).

    Returns:
        None
    """
    for repo_url, key in repo_urls.items():
        logger.info(f"Processing repo URL: {repo_url}")
        final_dir = download_latest_release(repo_url) or f"{repo_url.rstrip('/').split('/')[-1]}_latest"
        add_item_to_dict(init_py_items if key == "init" else menu_py_items, final_dir, key)

# ========================================================================== #
# This section contains the function to process zip URLs.
# ========================================================================== #

def process_zip_urls(zip_urls: Dict[str, str]) -> None:
    """
    Processes a dictionary of zip URLs and their corresponding keys.

    For each zip URL in the dictionary, this function checks if the directory
    corresponding to the zip file already exists. If it does not exist, it
    downloads and extracts the zip file into that directory. If the directory
    already exists, it logs an informational message. Additionally, it adds
    the directory to either the `init_py_items` or `menu_py_items` dictionary
    based on the provided key.

    Args:
        zip_urls (Dict[str, str]): A dictionary where the keys are zip URLs
                                   and the values are strings indicating
                                   whether the zip file should be added to
                                   `init_py_items` or `menu_py_items`.

    Returns:
        None
    """
    for zip_url, key in zip_urls.items():
        final_dir = zip_url.split('/')[-1].replace('.zip', '')
        if not Path(final_dir).exists():
            download_and_extract_zip(zip_url, final_dir)
        else:
            logger.info(f"Directory {final_dir} already exists.")
        add_item_to_dict(init_py_items if key == "init" else menu_py_items, final_dir, key)

# ========================================================================== #
# This section contains the function to create an `init.py` or `menu.py` file.
# # ========================================================================== #
from pathlib import Path
from typing import Dict, List


def create_nuke_py(file_name: str, items: Dict[str, str], file_types: List[str], no_drill_down_list: List[str]) -> None:
    """
    Creates a Python file with nuke.pluginAddPath() statements for specified directories and file types.

    Args:
        file_name (str): The name of the Python file to be created.
        items (Dict[str, str]): A dictionary where keys are directory paths to be processed.
        file_types (List[str]): A list of file types to look for in the directories.
        no_drill_down_list (List[str]): A list of directory names to avoid drilling down into.

    Returns:
        None
    """
    logger.info(f"Creating {file_name} with nuke.pluginAddPath() statements.")
    with open(file_name, "w") as f:
        f.write("import nuke\n\n")
        for dir_path_item in items.keys():
            dir_path_item = Path(dir_path_item)
            logger.debug(f"Processing directory: {dir_path_item}")

            if dir_path_item.is_dir():
                found = False

                # Check if the directory is in the no_drill_down_list
                if any(no_drill in dir_path_item.name for no_drill in no_drill_down_list):
                    f.write(f"nuke.pluginAddPath('{dir_path_item}')\n")
                    found = True

                # Check for file types in main directory
                if not found:
                    for file_type in file_types:
                        if (dir_path_item / file_type).exists():
                            f.write(f"nuke.pluginAddPath('{dir_path_item}')\n")
                            found = True
                            break

                # If not found, check for subdirectory matching repository name
                if not found:
                    repo_name = dir_path_item.name.split('_')[0].lower()
                    for sub_dir in dir_path_item.iterdir():
                        if sub_dir.is_dir() and sub_dir.name.lower() == repo_name:
                            for file_type in file_types:
                                if (sub_dir / file_type).exists():
                                    f.write(f"nuke.pluginAddPath('{sub_dir}')\n")
                                    found = True
                                    break
                        if found:
                            break

                # If still not found, check any subdirectory for the desired file types
                if not found:
                    for sub_dir in dir_path_item.iterdir():
                        if sub_dir.is_dir():
                            for file_type in file_types:
                                if (sub_dir / file_type).exists():
                                    f.write(f"nuke.pluginAddPath('{sub_dir}')\n")
                                    found = True
                                    break
                            if found:
                                break
    logger.info(f"Finished creating {file_name}.")



# ========================================================================== #
# This section contains the main function to orchestrate the download, extraction, and file creation process.
# ========================================================================== #
def main() -> None:
    """
    Main function to execute the script.

    This function performs the following steps:
    1. Deletes existing files.
    2. Processes repository URLs.
    3. Processes ZIP file URLs.
    4. Creates and writes to 'init.py' with specified items.
    5. Creates and writes to 'menu.py' with specified items.
    6. Logs the completion of the script execution.
    7. Prints the items for 'init.py' and 'menu.py'.
    8. Logs a summary of what packages were found and which package was added to what file.

    Returns:
        None
    """
    delete_existing_files()
    process_repo_urls(repo_urls)
    process_zip_urls(zip_urls)
    create_nuke_py("init.py", init_py_items, ["init.py", "__init__.py"], no_drill_down_list)
    create_nuke_py("menu.py", menu_py_items, ["menu.py", "__menu__.py", "__init__.py"], no_drill_down_list)
    logger.info("Script execution completed.")
    print(f"init_py_items: {init_py_items}")
    print(f"menu_py_items: {menu_py_items}")

    # Log summary information
    logger.info("Summary of packages found and added:")
    for item, file_type in init_py_items.items():
        logger.info(f"Package '{item}' added to 'init.py' ")
    for item, file_type in menu_py_items.items():
        logger.info(f"Package '{item}' added to 'menu.py' ")


# ========================================================================== #
# This section calls the main function when the script is executed.
# ========================================================================== #

if __name__ == "__main__":
    main()

# -------------------------------------------------------------------------- #

# ========================================================================== #
# 53 54 52 45 4E 47 54 48 2D 49 4E 2D 4E 55 4D 42 45 52 53 C2 A9 32 30 32 35 #
# ========================================================================== #
