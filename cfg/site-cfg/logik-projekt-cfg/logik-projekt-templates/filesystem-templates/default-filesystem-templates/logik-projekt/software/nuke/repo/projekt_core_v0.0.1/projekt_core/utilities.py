
# -------------------------------------------------------------------------- #

# DISCLAIMER:       This file is part of LOGIK-PROJEKT.
#                   Copyright © 2024 Silo 84
   
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

# File Name:        utilities.py
# Version:          0.0.1
# Created:          2024-10-25
# Modified:         2021-11-06

# -------------------------------------------------------------------------- #

"""
This module provides utility functions for setting up logging, converting paths,
and opening directories in the file explorer.

Functions:
1. `setup_logger(name="projekt_core", log_level=logging.DEBUG, log_file=None, formatter=None) -> logging.Logger`:
    Configures and returns a logger with the specified name and log level.
2. `convert_to_nuke_path_string(path) -> str`: Converts path separators to forward slash ('/') for Nuke.
3. `convert_to_nuke_path(path) -> Path`: Converts path separators to forward slash ('/') for Nuke and returns a Path object.
4. `openDirectory(directory: Path) -> None`: Opens the specified directory in the file explorer.
5. `openToolsetsDir() -> None`: Opens the directory that contains the toolsets.
6. `openTemplatesDir() -> None`: Opens the directory that contains the templates.
7. `openGizmosDir() -> None`: Opens the directory that contains the gizmos.
8. `openScriptsDir() -> None`: Opens the directory that contains the Python scripts.
9. `placeholder_func() -> None`: Placeholder function.

Dependencies:
- sys
- logging
- pathlib
- subprocess
- projekt_core.settings
"""

import sys
import logging
from pathlib import Path
import subprocess

from projekt_core import settings as settings



# ========================================================================== #
# This section configures the logger.
# ========================================================================== #

def setup_logger(name="projekt_core", log_level=logging.DEBUG, log_file=None, formatter=None):
    """
    Configures and returns a logger with the specified name and log level.

    Parameters:
    - name (str): The name of the logger.
    - log_level (int): The log level to be set for the logger. Default is logging.DEBUG.
    - log_file (str, optional): The file path to log messages to. If None, logs to console only.
    - formatter (logging.Formatter, optional): The formatter to use for the log messages. If None, uses a default formatter.

    Returns:
    - logger (logging.Logger): The configured logger.
    """
    logger = logging.getLogger(name)

      # Prevent the logger from propagating messages to the root logger
    logger.propagate = False

    # Check if the logger is already configured with handlers
    if logger.hasHandlers():
        return logger  # Return the existing logger to avoid duplicates

    logger.setLevel(log_level)


    # Create console handler and set level to log_level
    ch = logging.StreamHandler()
    ch.setLevel(log_level)

    # Create formatter
    if formatter is None:
        # formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        formatter = logging.Formatter('%(asctime)s - %(module)s - %(funcName)s | %(levelname)s - %(message)s')

    # Add formatter to console handler
    ch.setFormatter(formatter)

    # Add console handler to logger
    logger.addHandler(ch)

    # If log_file is specified, add file handler
    if log_file:
        fh = logging.FileHandler(log_file)
        fh.setLevel(log_level)
        fh.setFormatter(formatter)
        logger.addHandler(fh)

    return logger


# Initialize the main logger for the entire project here
logger = setup_logger()

# -------------------------------------------------------------------------- #

# ========================================================================== #
# This section converts path separators to forward slash ('/') for Nuke.
# ========================================================================== #

def convert_to_nuke_path_string(path):
    """
    Convert path separators to forward slash ('/') for Nuke.

    :param path: The path to convert.
    :return: The converted path string.
    """
    path_string = Path(path).as_posix()
    return path_string

# -------------------------------------------------------------------------- #

def convert_to_nuke_path(path):
    """
    Convert path separators to forward slash ('/') for Nuke.

    :param path: The path to convert.
    :return: The converted path object.
    """
    path_object = Path(path).as_posix()
    path_object = Path(path_object)
    return path_object

# -------------------------------------------------------------------------- #

# ========================================================================== #
# This section opens the specified directory in the file explorer.
# ========================================================================== #

def openDirectory(directory: Path) -> None:
    """
    Open the specified directory in the file explorer.

    :param directory: The directory to open.
    """
    logging.info(f'Opening directory: {directory}')
    if not directory.is_dir():
        logging.error(f'{directory} does not exist on disk!')
        return

    commands = {
        'darwin': ['open', str(directory)],
        'linux': ['xdg-open', str(directory)],
        'win32': ['explorer', str(directory.resolve())]
    }

    command = commands.get(sys.platform)
    if command:
        try:
            subprocess.run(command, check=True)
        except Exception as e:
            logging.error(f'Failed to open directory: {str(e)}')
    else:
        logging.error(f'Unsupported platform: {sys.platform}')

# ========================================================================== #
# This section opens various directories in the file explorer.
# ========================================================================== #

def openToolsetsDir() -> None:
    """
    Open the directory that contains the toolset.
    """
    openDirectory(settings.nuke_toolsets_path())

# -------------------------------------------------------------------------- #

def openTemplatesDir() -> None:
    """
    Open the directory that contains the templates.
    """
    openDirectory(settings.nuke_templates_path())

# -------------------------------------------------------------------------- #

def openGizmosDir() -> None:
    """
    Open the directory that contains the gizmos.
    """
    openDirectory(settings.nuke_gizmos_path())

# -------------------------------------------------------------------------- #

def openScriptsDir() -> None:
    """
    Open the directory that contains the python scripts.
    """
    openDirectory(settings.nuke_scripts_path())

# -------------------------------------------------------------------------- #


# ========================================================================== #
# This section ccreates a placeholder function.
# ========================================================================== #

def placeholder_func():
    """
    Placeholder function.
    """
    pass

# -------------------------------------------------------------------------- #

# ========================================================================== #
# 53 54 52 45 4E 47 54 48 2D 49 4E 2D 4E 55 4D 42 45 52 53 C2 A9 32 30 32 35 #
# ========================================================================== #