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

# File Name:        vfxtools.py
# Version:          0.0.1
# Created:          2024-10-25
# Modified:         2021-11-06

# -------------------------------------------------------------------------- #

"""
This module includes functions for setting up logging, converting paths, and opening directories in the file explorer.

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



import nuke
import os
import base64
import zlib
import json
from typing import Dict, Any

# import projekt_core
from projekt_core import settings as settings
from projekt_core import utilities as utilities

# ========================================================================== #
# This section imports the logging module and sets up the logger.
# ========================================================================== #

from projekt_core.utilities import logger

# ========================================================================== #
# This section set up the root.PROJEKT tab in Nuke.
# ========================================================================== #

def add_knob_if_not_exists(knob_name, knob_type, *args):
    """
    Adds a knob to the root node if it does not already exist.

    Args:
        knob_name (str): The name of the knob to be added.
        knob_type (type): The type of the knob to be added.
        *args: Additional arguments to be passed to the knob constructor.

    Returns:
        None
    """
    if nuke.root().knob(knob_name) is None:
        nuke.root().addKnob(knob_type(knob_name, *args))

# -------------------------------------------------------------------------- #

def setup_root_projekt_knobs():
    """
    Sets up the root knobs for the PROJEKT project.
    This function adds various knobs to the root node in Nuke, including:
    - 'PROJEKT' tab knob
    - 'projekt_name_knob' string knob with default value 'PROJEKT:'
    - 'projekt_jumpto_fs' PyScript knob with label 'Show in File System' and callback 'projekt_core.utilities.openDirectory(projekt_core.settings.projekt_path())'
    - 'projekt_path_knob' string knob with label 'Path:'
    - 'projekt_warning' text knob
    - 'projekt_div' text knob
    - 'shot_name_knob' string knob with label 'Shot:'
    - 'shot_jumpto_fs' PyScript knob with label 'Show in File System' and callback 'projekt_core.utilities.openDirectory(projekt_core.settings.projekt_shot_path())'
    - 'shot_warning' text knob
    - 'shot_div' text knob
    - 'favorites' enumeration knob with label 'Bookmarks:' and options ['job', 'shot', 'work']
    - 'user' string knob with label 'User:'
    - 'fav_div' text knob
    - 'set_projekt_from_env_vars' PyScript knob with label 'PROJEKT <-> from env_vars' and callback 'projekt_core.vfxtools.set_projekt_from_env_vars()'
    - 'set_env_from_script' PyScript knob with label 'PROJEKT <-> from nuke script' and callback 'projekt_core.vfxtools.parse_script_for_env()'
    - 'refresh_shell_env' PyScript knob with label 'refresh shell variables' and callback 'projekt_core.vfxtools.read_projekt_env()'
    - 'unpack_direnv_diff' PyScript knob with label 'unpack direnv_diff' and callback 'projekt_core.vfxtools.set_nuke_shell_info()'
    - 'div_name' text knob
    - 'shell_info' text knob with default value 'Output...'
    Note: Some knobs are conditionally added based on the existence of certain knobs in the root node.
    """

    add_knob_if_not_exists('PROJEKT', nuke.Tab_Knob)
    add_knob_if_not_exists('projekt_name_knob', nuke.String_Knob, 'PROJEKT:')
    add_knob_if_not_exists('projekt_jumpto_fs', nuke.PyScript_Knob, 'Show in File System', 'projekt_core.utilities.openDirectory(projekt_core.settings.projekt_path())')
    add_knob_if_not_exists('projekt_path_knob', nuke.String_Knob, 'Path:')
    add_knob_if_not_exists('projekt_warning', nuke.Text_Knob, '')
    add_knob_if_not_exists('path_warning', nuke.Text_Knob, '')
    add_knob_if_not_exists('projekt_div', nuke.Text_Knob, "", "")
    add_knob_if_not_exists('shot_name_knob', nuke.String_Knob, 'Shot:')
    add_knob_if_not_exists('shot_jumpto_fs', nuke.PyScript_Knob, 'Show in File System', 'projekt_core.utilities.openDirectory(projekt_core.settings.projekt_shot_path())')
    add_knob_if_not_exists('shot_warning', nuke.Text_Knob, '')
    add_knob_if_not_exists('shot_div', nuke.Text_Knob, "", "")

    add_knob_if_not_exists('favorites', nuke.Enumeration_Knob, 'Bookmarks:', ['projekt', 'shot', 'work'])
    # add_knob_if_not_exists('user', nuke.String_Knob, 'User:')
    # if nuke.root().knob('user') is not None:
    #     nuke.root().knob('user').setValue('')

    add_knob_if_not_exists('fav_div', nuke.Text_Knob, "", "")
    # PROJEKT <-> from env_vars
    add_knob_if_not_exists('set_projekt_from_env_vars', nuke.PyScript_Knob, '---setup PROJEKT---', 'projekt_core.vfxtools.set_projekt_from_env_vars()')
    
    
    # add_knob_if_not_exists('set_env_from_script', nuke.PyScript_Knob, 'PROJEKT <-> from nuke script', 'projekt_core.vfxtools.parse_script_for_env()')
    # if nuke.root().knob('set_env_from_script') is not None:
        # nuke.root().knob('set_env_from_script').setFlag(nuke.STARTLINE)
    # add_knob_if_not_exists('set_shell_env', nuke.PyScript_Knob, 'set shell variables', 'vfxtools.set_projekt_env()')
    # if nuke.root().knob('set_shell_env') is not None:
    #     nuke.root().knob('set_shell_env').setFlag(nuke.STARTLINE)
    add_knob_if_not_exists('refresh_shell_env', nuke.PyScript_Knob, 'refresh shell variables', 'projekt_core.vfxtools.read_projekt_env()')
    if nuke.root().knob('refresh_shell_env') is not None:
        nuke.root().knob('refresh_shell_env').setFlag(nuke.STARTLINE)

    add_knob_if_not_exists('unpack_direnv_diff', nuke.PyScript_Knob, 'unpack direnv_diff', 'projekt_core.vfxtools.set_nuke_shell_info()')
    if nuke.root().knob('refresh_shell_env') is not None:
        nuke.root().knob('refresh_shell_env').setFlag(nuke.STARTLINE)

    add_knob_if_not_exists('div_name', nuke.Text_Knob, "", "")
    add_knob_if_not_exists('shell_info', nuke.Text_Knob, "", 'Output...')


# -------------------------------------------------------------------------- #

def create_projekt_panel():
    """
    Creates a pipeline panel for the root.PROJEKT in Nuke.

    This function checks if the root.PROJEKT panel already exists in Nuke. 
    If it exists, it logs an information message and moves on. If it doesn't exist, 
    it logs an information message and creates the root.PIPELINE panel using the rootTemplates function. 
    It then parses the script for environment variables using the parseScriptForEnv function.

    Returns:
        None
    """

    if nuke.exists('PROJEKT'):
        logger.info('root.PROJEKT panel exists, moving on')
    else:
        logger.info('creating root.PROJEKT panel.')
        setup_root_projekt_knobs()
    # set_projekt_from_env_vars()
    update_root_warnings()
    return

# ========================================================================== #
# This section defines functions to update the job warnings in Nuke.
# ========================================================================== #

def update_root_warnings():
    """
    Add warnings to the root.PROJEKT tab if the folders do not exist.
    This function checks if the job folder exists and if it is set to the project root.
    If the job folder does not exist or is set to the project root, it adds a warning message 
    to the root.PROJEKT tab.
    """
    projekt_name_value = str(settings.projekt_name())
    projekt_path_value = str(settings.projekt_path())

   
    # root_node = nuke.root()
    projekt_name_knob = nuke.root().knob('projekt_name_knob').value()
    projekt_path_knob = nuke.root().knob('projekt_path_knob').value()
    shot_name_knob = nuke.root().knob('shot_name_knob').value()

  

    job_message = '<b style="color:green">Name: good</b>'
    path_message = '<b style="color:green">Path: good</b>'
    shot_message = '<b style="color:green">Shot: good</b>'

    logger.info('running update_root_warnings...')
    logger.info(f"projekt_name_knob: {projekt_name_knob}")
    logger.info(f"projekt_name_value: {projekt_name_value}")
    logger.info(f"projekt_path_knob: {projekt_path_knob}")
    logger.info(f"projekt_path_value: {projekt_path_value}")
    logger.info(f"shot_name_knob: {shot_name_knob}")



    # PROJEKT checks
    # if not projekt_name_knob and not projekt_path_knob:
    # if not projekt_name_knob:        
    #     job_message = '<b style="color:orange">ERROR: name is blank!</b>'
    #     # path_message = '<b style="color:orange">ERROR: path is blank!</b>'
    #     logger.warning('PROJEKT name is blank!')

    if not projekt_name_knob:
        job_message = '<b style="color:orange">ERROR: name is blank!</b>'
        logger.warning('PROJEKT name is blank!')

    elif projekt_name_knob != projekt_name_value:
        job_message = f'<b style="color:orange">ERROR: name does not match! Expected: {projekt_name_value}</b>'
        logger.warning(f'PROJEKT name does not match! Expected: {projekt_name_value}')

    # Path checks
    if not projekt_path_knob:
        path_message = '<b style="color:orange">ERROR: path is blank!</b>'
        logger.warning('PROJEKT path knob is error!')

    elif projekt_path_knob != projekt_path_value:
        path_message = f'<b style="color:orange">ERROR: Path does not match! Expected: {projekt_path_value}</b>'
        logger.warning(f'PROJEKT path does not match! Expected: {projekt_path_value}')

    elif not os.path.exists(projekt_path_knob):
        path_message = '<b style="color:orange">ERROR: path does not exist on disk!</b>'
        logger.warning('PROJEKT path does not exist on disk')
    # if not projekt_path_knob:
    #     path_message = '<b style="color:orange">ERROR: path is blank!</b>'
    #     logger.warning('PROJEKT name and path are blank!')

    else:
        logger.info(f"PROJEKT name is {projekt_name_knob}")
        logger.info(f"path {projekt_path_knob} exists on disk")

    # Shot checks
    if not shot_name_knob:
        shot_message = '<b style="color:orange">ERROR: shot name is blank!</b>'
        logger.warning('Shot name is blank!')
    else:
        shot_path = os.path.join(projekt_path_knob, 'shots', shot_name_knob)
        if not os.path.exists(shot_path):
            shot_message = '<b style="color:orange">ERROR: shot path does not exist on disk!</b>'
            logger.warning(f'Shot path {shot_path} does not exist on disk')
        else:
            logger.info(f"Shot path {shot_path} exists on disk")

    logger.info("... update_root_warnings completed.")

    nuke.root().knob('projekt_warning').setValue(job_message)
    nuke.root().knob('path_warning').setValue(path_message)
    nuke.root().knob('shot_warning').setValue(shot_message)
    
print("# -------------------------------------------------------------------------- #")

# -------------------------------------------------------------------------- #

def update_root_warnings_callback():
    """
    Callback function that updates root warnings based on the knob name.

    Knob names that trigger the update are 'projekt_name_knob', 'shot_name_knob', 'projekt_path_knob', and 'favorites'.

    If an error occurs during the update, an error message is logged.

    Returns:
        None
    """
    try:
        # Verify that a script is open by checking if nuke.root() is valid
        root = nuke.root()
        if not root:
            logger.warning("No script is currently open; skipping update_root_warnings_callback.")
            return


        projekt_path_knob = nuke.root().knob('projekt_path_knob')
        projekt_name_knob = nuke.root().knob('projekt_name_knob')

        if projekt_path_knob and projekt_name_knob:
            # logger.info('Required knobs exist, proceeding with update_root_warnings')
            knob_name = nuke.thisKnob().name()
            if knob_name in ['projekt_name_knob', 'shot_name_knob', 'projekt_path_knob', 'favorites']:
                try:
                    update_root_warnings()
                except Exception as e:
                    logger.error("An error occurred in update_root_warnings_callback: %s", str(e))
    except ValueError as ve:
        pass
        # logger.error("ValueError in update_root_warnings_callback: %s", str(ve))
    except Exception as e:
        logger.error("An unexpected error occurred in update_root_warnings_callback: %s", str(e))

    # # Check if the required knobs exist
    # if nuke.root().knob('projekt_path_knob') and nuke.root().knob('projekt_name_knob'):
    #     logger.info('Required knobs exist, proceeding with update_root_warnings')
    #     knob_name = nuke.thisKnob().name()
    #     if knob_name in ['projekt_name_knob', 'shot_name_knob', 'projekt_path_knob', 'favorites']:
    #         try:
    #             update_root_warnings()
    #         except Exception as e:
    #             logger.error("An error occurred in update_root_warnings_callback: %s", str(e))
# -------------------------------------------------------------------------- #

# Register the callback dynamically
def enable_update_root_warnings_callback():
    # Adds the knob change callback for the root node
    nuke.addKnobChanged(update_root_warnings_callback, nodeClass='Root')
    logger.info("update_root_warnings_callback enabled.")


def disable_update_root_warnings_callback():
    # Removes the knob change callback to prevent errors when the script is closed
    nuke.removeKnobChanged(update_root_warnings_callback, nodeClass='Root')
    logger.info("update_root_warnings_callback disabled.")


# ========================================================================== #
# This section defines functions to set name, shot, and path knobs based on environment variables.
# ========================================================================== #


def set_projekt_from_env_vars():
    """
    Sets the projekt_name, shot, and projekt_path knobs based on the corresponding environment variables.

    This function retrieves the values of the following environment variables:
    - PROJEKT_NAME: Sets the projekt name.
    - PROJEKT_SHOT: Sets the shot name.
    - PROJEKT_PATH: Sets the projekt path.

    If any of the environment variables are not set, a warning message is logged and the function returns.

    Example usage:
    set_projekt_from_env_vars()
    """

    logger.info('Setting PROJEKT and SHOT from environment variables')

    env_vars_to_knobs = {
        'PROJEKT_NAME': 'projekt_name_knob',
        'PROJEKT_SHOT': 'shot_name_knob',
        'PROJEKT_PATH': 'projekt_path_knob'
    }

    for env_var, knob_name in env_vars_to_knobs.items():
        # value = os.getenv(env_var) if env_var != 'PROJEKT_PATH' else str(projekt_core.settings.projekt_path())
        value = os.getenv(env_var) if env_var != 'PROJEKT_PATH' else str(settings.projekt_path())

        if value:
            logger.info(f'Setting {env_var} to: {value}')
            nuke.root().knob(knob_name).setValue(value)
            # if env_var == 'PROJEKT_NAME':
            #     update_root_warnings()
        else:
            logger.warning(f'{env_var} not set')
    update_root_warnings()
    
# -------------------------------------------------------------------------- #

def on_root_node_create_callback():
    """
    Callback function triggered when a root node is created.
    It logs the event and performs certain actions based on the state of the root node.
    Returns:
        None
    """
    logger.info('on_root_node_create callback triggered')
    
    root_name = nuke.root().name()
    if not root_name:
        logger.info('Root node name is empty, setting projekt from environment variables')
        set_projekt_from_env_vars()
        update_root_warnings()
    else:
        logger.warning(f'Root node name is not empty: {root_name}')

# -------------------------------------------------------------------------- #

def parse_script_for_env():
    """
    Given a script saved onto disk, parseScriptForEnv() will set the projekt, path, and shot in the nuke.root() tab.
    This function checks if the script is saved into a job/seq/shot structure. It verifies the path exists before continuing.
        
    """
 
    projekt_root_value = str(settings.projekt_root_path())

    logger.info('Checking if the script exists...')
    name = nuke.root().name()
    if name != 'Root':
        logger.info('Script exists on disk, setting projekt/path/shot knobs...')
        # Check if the shot is stored in the root path folder.
        if not name.startswith(projekt_root_value):
            logger.warning(f'script not stored in {projekt_root_value}')
            # set the bookmark back to projekt...
            nuke.root().knob('favorites').setValue('projekt')
            return

        # Projekt is in the root path, let's set pull the env variables...
        projekt_name = settings.projekt_name()
        logger.info(f'Setting PROJEKT to: {projekt_name}')
        try:
            nuke.root().knob('projekt_name_knob').setValue(projekt_name)
        except Exception as e:
            logger.error(f'Error setting projekt_name_knob: {e}')

        # Path
        projekt_path = str(settings.projekt_path())
        logger.info(f'Setting Path to: {projekt_path}')
        try:
            nuke.root().knob('projekt_path_knob').setValue(projekt_path)
        except Exception as e:
            logger.error(f'Error setting projekt_path_knob: {e}')

        # Setup current shot... split is not the most reliable method...
        parseShot = name.split('/')[4:5]
        if parseShot:
            logger.info(f'Setting SHOT to: {parseShot[0]}')
            try:
                nuke.root().knob('shot_name_knob').setValue(parseShot[0])
                nuke.root().knob('favorites').setValue('shot')
            except Exception as e:
                logger.error(f'Error setting shot_name_knob: {e}')

    else:
        logger.info('No script found on disk.')
        return

# -------------------------------------------------------------------------- #

def on_script_load_parse_for_env():
    """
    Callback function to run parse_script_for_env when a script is opened.
    """
    logger.info('parse_script_for_env callback triggered')
    try:
        parse_script_for_env()
    except Exception as e:
        logger.error(f'Error in on_script_load callback: {e}')


# ========================================================================== #
# This section defines functions to read and set the shell environment variables in Nuke.
# ========================================================================== #

def read_projekt_env():
    """
    Get the shell env settings for PROJEKT_NAME, SHOT and update the 'shellInfo' knob in the root.PROJEKT tab.
    """
    PROJEKT_NAME = os.getenv('PROJEKT_NAME', '<env not set>') or '<value is empty>'
    PROJEKT_SHOT = os.getenv('PROJEKT_SHOT', '<env not set>') or '<value is empty>'
    PROJEKT_PATH = os.getenv('PROJEKT_PATH', '<env not set>') or '<value is empty>'
    PROJEKT_ROOT = os.getenv('PROJEKT_ROOT', '<env not set>') or '<value is empty>'

    infoStr = f'''
    Shell Environment Variables:
    - PROJEKT: {PROJEKT_NAME}
    - SHOT: {PROJEKT_SHOT}
    - PROJEKT_PATH: {PROJEKT_PATH}
    - PROJEKT_ROOT: {PROJEKT_ROOT}
    '''
    nuke.root().knob('shell_info').setValue(infoStr)

# -------------------------------------------------------------------------- #
# not implemented/updated yet...
# def set_projekt_env():
#     """
#     Sets the shell's env variables after loading a script with nuke.root() job env's set    
#     """
#     if nuke.root().knob('jobEnv'):
#         os.environ['JOB'] = vfxtools.jobDir()
#     if nuke.root().knob('seqEnv'):
#         os.environ['SEQ'] = vfxtools.seqDir()
#     if nuke.root().knob('shotEnv'):
#         os.environ['SHOT'] = vfxtools.shotDir()


# ========================================================================== #
# This section unpacks the DIRENV_DIFF environment variable and sets the shell_info knob in Nuke.
# ========================================================================== #


def unpack_direnv_diff() -> Dict[str, Any]:
    """
    Process the DIRENV_DIFF environment variable, decode and decompress it,
    and return the resulting environment variables.

    The DIRENV_DIFF environment variable is expected to be a base64-encoded,
    zlib-compressed JSON string containing a dictionary with environment variables.

    Returns:
        Dict[str, Any]: The decompressed and decoded dictionary of environment variables.
    """
    direnv_diff_str = os.environ.get('DIRENV_DIFF')
    if not direnv_diff_str:
        print("DIRENV_DIFF environment variable not found.")
        return {}

    try:
        decoded = base64.urlsafe_b64decode(direnv_diff_str)
        decompressed = zlib.decompress(decoded)
        direnv_vars = json.loads(decompressed)['n']
        return direnv_vars
    except (base64.binascii.Error, zlib.error, json.JSONDecodeError, KeyError) as e:
        print(f"Error processing DIRENV_DIFF: {e}")
        return {}

# -------------------------------------------------------------------------- #

def set_nuke_shell_info() -> None:
    """
    Set the Nuke shell_info knob with the environment variables from DIRENV_DIFF.
    """
    direnv_vars = unpack_direnv_diff()
    if direnv_vars:
        nuke.root().knob('shell_info').setValue(json.dumps(direnv_vars, indent=4))

# -------------------------------------------------------------------------- #

def direnv_diff_to_string() -> str:
    """
    Convert the environment variables from DIRENV_DIFF to a formatted JSON string.

    Returns:
        str: The formatted JSON string of environment variables.
    """
    direnv_dict = unpack_direnv_diff()
    return json.dumps(direnv_dict, indent=4)

# -------------------------------------------------------------------------- #

# ========================================================================== #
# C2 A9 32 30 32 34 20 7C 20 62 72 69 61 6E 40 73 69 6C 6F 38 34 2E 63 6F 6D #
# ========================================================================== #