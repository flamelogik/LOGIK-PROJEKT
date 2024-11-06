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
# This section configures the logger.
# ========================================================================== #


def placeholder_func():
    """
    Placeholder function.
    """
    pass
