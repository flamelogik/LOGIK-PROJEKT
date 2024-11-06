from pathlib import Path
import requests
import zipfile
import io
import logging


# Usage
repo_urls = [
    # "https://github.com/adrianpueyo/KnobScripter",
    "https://github.com/CreativeLyons/NukeSurvivalToolkit_publicRelease",
    "https://github.com/adrianpueyo/Stamps"
]

zip_urls = [
    "https://github.com/xbourque/pixelfudger/raw/main/downloads/pixelfudger_3.2v1_nov_2023.zip"   
]


extracted_dirs = []

# Set up logger
logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

# Create file handler and set level to DEBUG
file_handler = logging.FileHandler('download_tools.log', mode='w')
file_handler.setLevel(logging.DEBUG)

# Create stream handler and set level to DEBUG
stream_handler = logging.StreamHandler()
stream_handler.setLevel(logging.DEBUG)

# Create formatter
formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')

# Add formatter to handlers
file_handler.setFormatter(formatter)
stream_handler.setFormatter(formatter)

# Add handlers to logger
logger.addHandler(file_handler)
logger.addHandler(stream_handler)

# Usage
repo_urls = [
    "https://github.com/CreativeLyons/NukeSurvivalToolkit_publicRelease",
    "https://github.com/adrianpueyo/Stamps"
]

repo_menupy_urls = [
    "https://github.com/adrianpueyo/KnobScripter",
]

zip_urls = [
    "https://github.com/xbourque/pixelfudger/raw/main/downloads/pixelfudger_3.2v1_nov_2023.zip"   
]

extracted_dirs = []

def download_and_extract_zip(zip_url, final_dir):
    """
    Downloads a zip file from the given URL and extracts its contents to the specified directory.
    Args:
        zip_url (str): The URL of the zip file to download.
        final_dir (str): The directory where the extracted files will be placed.
    Raises:
        zipfile.BadZipFile: If the downloaded file is not a valid zip file.
    Returns:
        None
    """
    # Ensure the URL points to the raw content if it's a GitHub URL
    if "github.com" in zip_url and not zip_url.endswith("?raw=true"):
        zip_url += "?raw=true"
    
    response = requests.get(zip_url)
    if response.status_code == 200:
        try:
            with zipfile.ZipFile(io.BytesIO(response.content)) as z:
                # Extract all files to a temporary directory first
                temp_dir = Path(final_dir) / "temp"
                temp_dir.mkdir(parents=True, exist_ok=True)
                z.extractall(temp_dir)
                
                # Move files from the temporary directory to the final directory
                for item in temp_dir.iterdir():
                    if item.is_dir():
                        for sub_item in item.iterdir():
                            sub_item.rename(Path(final_dir) / sub_item.name)
                    else:
                        item.rename(Path(final_dir) / item.name)
                
                # Remove the temporary directory
                for item in temp_dir.iterdir():
                    if item.is_dir():
                        for sub_item in item.iterdir():
                            sub_item.unlink()
                        item.rmdir()
                    else:
                        item.unlink()
                temp_dir.rmdir()
                
            logger.info(f"Extracted {zip_url} to {final_dir}")
            extracted_dirs.append(final_dir)
        except zipfile.BadZipFile:
            logger.error(f"Failed to extract {zip_url}: File is not a zip file")
    else:
        logger.error(f"Failed to download {zip_url}: {response.status_code}")

def download_latest_release(repo_url):
    """
    Downloads the latest release from a GitHub repository.
    Args:
        repo_url (str): The URL of the GitHub repository.
    Returns:
        None
    Raises:
        None
    """
    # Extract owner and repo from the URL
    owner, repo = repo_url.rstrip('/').split('/')[-2:]
    
    # Existing logic for downloading the latest release from a repo URL
    response = requests.get(f"https://api.github.com/repos/{owner}/{repo}/releases/latest")
    if response.status_code == 200:
        release_info = response.json()
        tag_name = release_info['tag_name']
        zip_url = f"https://github.com/{owner}/{repo}/archive/refs/tags/{tag_name}.zip"
    else:
        logger.error(f"Failed to fetch release information: {response.status_code}")
        return
    
    final_dir = f"{repo}_{tag_name}"
    if Path(final_dir).exists():
        logger.info(f"Directory {final_dir} already exists. Skipping download.")
        return
    
    logger.info(f"Extract directory: {final_dir}")
    download_and_extract_zip(zip_url, final_dir)

def process_repo_urls(repo_urls):
    """
    Process a list of repository URLs.

    Args:
        repo_urls (list): A list of repository URLs.

    Returns:
        None
    """
    for repo_url in repo_urls:
        logger.info(f"Processing repo URL: {repo_url}")
        download_latest_release(repo_url)
        logger.info("")  # Add an empty line for better readability

def process_zip_urls(zip_urls):
    """
    Process a list of zip URLs.
    Args:
        zip_urls (list): A list of zip URLs to process.
    Returns:
        None
    """
    for zip_url in zip_urls:
        final_dir = zip_url.split('/')[-1].replace('.zip', '')
        if Path(final_dir).exists():
            logger.info(f"Directory {final_dir} already exists. Skipping download.")
            continue
        
        logger.info(f"Extract directory: {final_dir}")
        download_and_extract_zip(zip_url, final_dir)

def create_init_py(base_dir):
    """
    Creates an `init.py` file and writes `nuke.pluginAddPath()` statements based on the directories found in `base_dir`.
    Parameters:
    - base_dir (str): The base directory to scan for extracted directories.
    Returns:
    - None
    Description:
    - The function iterates over each directory in `base_dir`.
    - For each directory, it checks if any of the following files exist in the root of the directory: `init.py`, `__init__.py`, `menu.py`.
    - If any of these files exist, it writes a `nuke.pluginAddPath()` statement to the `init.py` file, with the directory path as the argument.
    - If none of the files exist in the root directory, it checks for a subdirectory that matches the repository name (case insensitive).
    - If a matching subdirectory is found, it checks if any of the init files exist in that subdirectory.
    - If any of the init files exist in the subdirectory, it writes a `nuke.pluginAddPath()` statement to the `init.py` file, with the subdirectory path as the argument.
    - The function continues this process for each directory in `base_dir`.
    """
    
    base_path = Path(base_dir)
    with open("init.py", "w") as f:
        for dir_path in base_path.iterdir():
            if dir_path.is_dir():
                init_files = ["init.py", "__init__.py", "menu.py"]
                found = False
                
                # Check if any init file exists in the root of the extracted directory
                for init_file in init_files:
                    if (dir_path / init_file).exists():
                        f.write(f"nuke.pluginAddPath('{dir_path}')\n")
                        found = True
                        break
                
                if not found:
                    # Check for a subdirectory matching the repo name (case insensitive)
                    repo_name = dir_path.name.split('_')[0].lower()
                    for sub_dir in dir_path.iterdir():
                        if sub_dir.is_dir() and sub_dir.name.lower() == repo_name:
                            for init_file in init_files:
                                if (sub_dir / init_file).exists():
                                    f.write(f"nuke.pluginAddPath('{sub_dir}')\n")
                                    found = True
                                    break
                        if found:
                            break

                    # Additional check for subdirectories that may contain init files
                    if not found:
                        for sub_dir in dir_path.iterdir():
                            if sub_dir.is_dir():
                                for init_file in init_files:
                                    if (sub_dir / init_file).exists():
                                        f.write(f"nuke.pluginAddPath('{sub_dir}')\n")
                                        found = True
                                        break
                                if found:
                                    break
                                
process_repo_urls(repo_urls)
process_zip_urls(zip_urls)
create_init_py(".")