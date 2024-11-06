__author__ = "Brian Willard"
__copyright__ = "Copyright 2023 Brian Willard"
__license__ = "Apache-2.0 - https://opensource.org/licenses/apache-2-0"
__version__ = "0.0.1"
__email__ = "brian@silo84.com"
__website__ = "www.silo84.com"
__status__ = "Testing"

"""
reloading existing modules works, but we are having issues accessing newly 
imported_modules in globals() after the fact.

"""

from pathlib import Path
import importlib
import nuke
import os
import sys


import projekt_core.settings as settings
from projekt_core.utilities import convert_to_nuke_path_string



# ========================================================================== #
# This section imports the logging module and sets up the logger.
# ========================================================================== #

from projekt_core.utilities import logger

# ========================================================================== #
# This section adds a menu to Nuke.
# ========================================================================== #

# ========================================================================== #
# This section reloads the specified menu in Nuke.
# ========================================================================== #

print("# -------------------------------------------------------------------------- #")
print(f"running setupScripts.py...")
# Initialize variables
logger.info("variables....")

try:
    scriptsRootDir = Path(settings.nuke_scripts_path())
    nuke_pipeline_path = Path(settings.nuke_pipeline_path())
    logger.info(f'scriptsRootDir: {scriptsRootDir}')
    logger.info(f'nuke_pipeline_path: {nuke_pipeline_path}')
except Exception as e:
    logger.info(f'Error: {str(e)}')



_index = -6
menuTitle = "pyScripts"
menubar = nuke.menu("Nuke")
m = menubar.addMenu(f"&{menuTitle}", index=-1)


logger.info("loading pyScripts")
logger.info(f'scriptsRootDir: {scriptsRootDir}')


# Check if the 'imported_modules' variable is defined in the global namespace
if 'imported_modules' not in globals():
    logger.info('imported_modules not found in global namespace. init empty set')
    global imported_modules
    imported_modules = set()

# ========================================================================== #
# This section opens the specified directory in the file explorer.
# ========================================================================== #

def openDirectory(directory: Path) -> None:
    """
    Open the specified directory in the file explorer.

    :param directory: The directory to open.
    """
    logger.info(f'Opening directory: {directory}')
    try:
        if not directory.is_dir():
            logger.error(f'{directory} does not exist on disk!')
            return

        if sys.platform == 'darwin':
            os.system(f'open {directory}')
        elif sys.platform == 'linux':
            os.system(f'xdg-open {directory}')
        elif sys.platform == 'win32':
            path = str(directory).replace('/', '\\')
            os.system(f'explorer {path}')
        else:
            logging.error(f'Unsupported platform: {sys.platform}')
    except Exception as e:
        logger.error(f'Failed to open directory: {str(e)}')

# -------------------------------------------------------------------------- #

# def openScriptsDir() -> None:
#     """
#     Open the directory that contains the python scripts.
#     """
#     openDirectory(scriptsRootDir)

# -------------------------------------------------------------------------- #



# ========================================================================== #
# This section 
# ========================================================================== #

def reload_module(module_name: str):
    try:
        module = importlib.import_module(module_name)
        importlib.reload(module)
    except ImportError:
        logger.info(f"Module {module_name} not imported. Skipping reload.")


# ========================================================================== #
# This section 
# ========================================================================== #

for path, dirs, files in os.walk(scriptsRootDir):
    files.sort()
    dirs.sort()

    for f in files:
        if not '#' in path and not '#' in f and f.endswith(".py") and not f.startswith("__"):
            nuke.pluginAddPath(path)
            pyScriptPath = convert_to_nuke_path_string(Path(path) / f)
            # print(f"pyScriptPath: {pyScriptPath}")

            localDirPath = convert_to_nuke_path_string(
                str(pyScriptPath).replace(str(nuke_pipeline_path), '').replace(os.sep, '.').rstrip('.py').lstrip('.').lstrip(os.sep)
            )
            # print(f'debug: {localDirPath}')

            filename = f.split(".")[0]

            if localDirPath in imported_modules:
                reload_module(localDirPath)
                _state = 'reloaded'
            else:
                importlib.import_module(localDirPath)
                imported_modules.add(localDirPath)
                _state = 'found'

            menus = pyScriptPath.replace(str(scriptsRootDir), '').lstrip(os.sep).split("/")
            parentMenu = m
            for menu in menus[:-1]:
                if menu:
                    newMenu = parentMenu.addMenu(f"&{menu}", index=_index)
                    parentMenu = newMenu

            parentMenu.addCommand(str(filename), f"{localDirPath}.main()", "")
            # print(f"{localDirPath} {_state}")

# ========================================================================== #
# This section 
# ========================================================================== #

logger.info(f'imported_modules: {imported_modules}')

# ========================================================================== #
# This section 
# ========================================================================== #
m.addSeparator()
#m.addCommand('reload pyScripts Menu', 'pyScripts.reload.reload_pyScripts.main()', '')
m.addCommand('reload pyScripts Menu (fails if new scripts added)', 'projekt_core.setupScripts.reload_main()', '')
m.addCommand('openScriptsDir', 'projekt_core.utilities.openScriptsDir()', '')



# logger.info(f'debug: scriptsRootDir: {scriptsRootDir}')
# logger.info(f'debug: nuke_pipeline_path: {nuke_pipeline_path}')


# ========================================================================== #
# This section 
# ========================================================================== #

def reload_main():
    menubar = nuke.menu("Nuke")

    # reload scripts:
    print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~`')
    print('rebuilding pyScripts menu')
    print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~`')

    # remove the menu
    menubar.removeItem('pyScripts')

    # Directory containing the scripts
    scripts_dir = os.path.join(nuke_pipeline_path, 'pyScripts')

    # Clear the pyScripts package from sys.modules to ensure new modules are detected
    for module in list(sys.modules.keys()):
        if module.startswith('pyScripts'):
            del sys.modules[module]

    # Reimport the pyScripts package
    import pyScripts

    # Iterate over all Python files in the scripts directory
    for root, dirs, files in os.walk(scripts_dir):
        dirs.sort()  # Ensure directories are processed in a consistent order
        for file in files:
            if file.endswith('.py'):
                module_name = os.path.splitext(file)[0]
                module_path = os.path.relpath(os.path.join(root, module_name), nuke_pipeline_path).replace(os.sep, '.')

                # Debug information
                #print(f"Processing file: {file}")
                #print(f"Module name: {module_name}")
                #print(f"Module path: {module_path}")

                try:
                    # Import or reload the module
                    if module_path in sys.modules:
                        importlib.reload(sys.modules[module_path])
                        #print(f'{module_path} reloaded')
                    else:
                        importlib.import_module(module_path)
                        #print(f'{module_path} imported')
                except ModuleNotFoundError as e:
                    logger.info(f"Error loading {module_path}: {e}")
                except Exception as e:
                    logger.info(f"Unexpected error loading {module_path}: {e}")

    # Reload core.setupScripts and handle potential import errors
    try:
        import projekt_core.setupScripts
        importlib.reload(projekt_core.setupScripts)
    except ModuleNotFoundError as e:
        logger.info(f"Error reloading core.setupScripts: {e}")
    except Exception as e:
        logger.info(f"Unexpected error reloading core.setupScripts: {e}")


    logger.info('rebuilding pyScripts menu complete')



logger.info('setupScripts complete')
