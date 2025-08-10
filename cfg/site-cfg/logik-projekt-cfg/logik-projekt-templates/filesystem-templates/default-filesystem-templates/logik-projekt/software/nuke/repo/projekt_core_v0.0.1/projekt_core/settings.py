
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

# File Name:        settings.py
# Version:          0.0.1
# Created:          2024-10-25
# Modified:         2021-11-06

# -------------------------------------------------------------------------- #

"""
This module provides functions to retrieve various directory paths used in the Nuke pipeline.
The paths are returned as pathlib.Path objects and include:

1. `projekt_root_windows_path()`: Returns the root path of the pipeline on Windows.
2. `projekt_root_path()`: Returns the root path of the project, either from an environment variable or a default location.
3. `projekt_full_path(projekt_name)`: Returns the full path to a project by combining the root path and the project name.
4. `get_projekt_path_from_env()`: Returns the path to the project job from an environment variable.
5. `projekt_path()`: Returns the resolved path of the project.
6. `projekt_name()`: Retrieves the value of the 'PROJEKT_NAME' environment variable.
7. `projekt_shot()`: Retrieves the value of the 'PROJEKT_SHOT' environment variable.
8. `projekt_shot_path()`: Returns the path of the current shot in the project.
9. `pipeline_root_path()`: Returns the pipeline root path from an environment variable.
10. `nuke_pipeline_path()`: Returns the root path of the Nuke pipeline.
11. `nuke_gizmos_path()`: Returns the path to the directory where the Nuke gizmos are located.
12. `nuke_custom_gizmos_path()`: Returns the path to the custom gizmos directory.
13. `nuke_scripts_path()`: Returns the path to the Nuke pyScripts directory.
14. `nuke_toolsets_path()`: Returns the path to the Nuke toolsets folder.
15. `nuke_templates_path()`: Returns the path to the Nuke templates folder.
16. `ocio_configs_path()`: Returns the file path for the OpenColorIO (OCIO) configuration.

Dependencies:
- pathlib
- os
- logging
- projekt_core.utilities (for convert_to_nuke_path and logger)
"""

import os
import logging
from pathlib import Path
from projekt_core.utilities import convert_to_nuke_path

# ========================================================================== #
# This section imports the logging module and sets up the logger.
# ========================================================================== #

from projekt_core.utilities import logger

# -------------------------------------------------------------------------- #

def projekt_root_windows_path():
	"""
	Returns the root path of the pipeline on Windows.

	Returns:
		pathlib.Path: The root path of the pipeline on Windows.
	"""
	return Path('M:/pipeline')

# -------------------------------------------------------------------------- #

def projekt_root_path():
	"""
	Returns a Path to PROJEKT mount point. ie. /PROJEKTS

	If the environment variable 'PROJEKT_ROOT' is set, the function converts it to a Nuke path and returns it.
	Otherwise, it prints a message indicating that the project root was not found and sets it manually.

	Returns:
		pathlib.Path: The root path of the project.
	"""

	projekt_root_env = os.getenv('PROJEKT_ROOT')
	if projekt_root_env:
		projekt_root = convert_to_nuke_path(Path(projekt_root_env))
		return projekt_root
	else:
		logger.warning("PROJEKT_ROOT not found...")

# -------------------------------------------------------------------------- #

# ========================================================================== #
# Various ways to access the projekt path
# ========================================================================== #


def projekt_full_path(projekt_name):
    """
    Returns the full path to the projekt by combining the root path and the projekt name.

    Args:
        projekt_name (str): The name of the projekt.

    Returns:
        pathlib.Path: The full path to the projekt.
    """
    root_path = projekt_root_path()
    full_path = root_path / projekt_name
    return full_path





def get_projekt_path_from_env():
	"""
	Returns the path to the projekt job from the environment variable PROJEKT_PATH.

	If the environment variable PROJEKT_PATH is set, the function converts the path to a Nuke-compatible format
	using the convert_to_nuke_path function and returns it. Otherwise, it prints a message indicating that the
	PROJEKT_PATH environment variable was not found and sets the path manually.

	Returns:
		pathlib.Path: The path to the projekt job.
	"""
	projekt_job_path_env = os.getenv('PROJEKT_PATH')
	if projekt_job_path_env:
		projekt_job = convert_to_nuke_path(Path(projekt_job_path_env))
		return projekt_job_path_env
	else:
		logger.warning("PROJEKT_PATH not found...")



def projekt_path():
	"""
	Returns the resolved path of the project. Two options are available:
	- get the project path from the environment variables using the `get_projekt_path_from_env()` function.
	- the  `projekt_full_path()` function with the project name to get the resolved project path.
	Returns:
		str: The resolved path of the project.
	"""
	# resolved_projekt_path = get_projekt_path_from_env()
	resolved_projekt_path = projekt_full_path(projekt_name())
	return resolved_projekt_path


# -------------------------------------------------------------------------- #

def projekt_name():
	"""
	Retrieves the value of the 'PROJEKT_NAME' environment variable.
	
	If the environment variable is set, the function returns its value.
	If the environment variable is not set, the function prints a message and sets the value manually.
	
	Returns:
		str: The value of the 'PROJEKT_NAME' environment variable, if set.
	
	"""
	PROJEKT_NAME_env = os.getenv('PROJEKT_NAME')
	if PROJEKT_NAME_env:
		PROJEKT_NAME = PROJEKT_NAME_env
		return PROJEKT_NAME
	else:
		logger.warning("PROJEKT_NAME not found...")

# -------------------------------------------------------------------------- #

def projekt_shot():
	"""
	Retrieves the value of the 'PROJEKT_SHOT' environment variable.

	If the environment variable is set, the function converts its value to a Nuke path using the 'convert_to_nuke_path' function and returns it.
	If the environment variable is not set, the function returns None.

	Returns:
		str: The value of the 'PROJEKT_SHOT' environment variable, if set. Otherwise, None.
	"""
	projekt_current_shot_env = os.getenv('PROJEKT_SHOT')
	if projekt_current_shot_env:
		# projekt_current_shot = convert_to_nuke_path(Path(projekt_current_shot_env))
		return projekt_current_shot_env
	else:
		return None

# -------------------------------------------------------------------------- #

def projekt_shot_path():
	"""
	Returns the path of the current shot in the Projekt.

	If the current shot exists, it converts the path to a Nuke-compatible format and returns it.
	If the current shot does not exist, it logs an info message stating that PROJEKT_SHOT was not found.

	Returns:
		pathlib.Path: The path of the current shot in the Projekt, converted to a Nuke-compatible format if it exists.
	"""
	projekt_current_shot = projekt_shot()
	if projekt_current_shot:
		projekt_shot_path = convert_to_nuke_path(projekt_path() / 'shots' / projekt_current_shot)
		return projekt_shot_path
	else:
		logger.warning("projektCurrentShotPath: current shot has no path...")

# -------------------------------------------------------------------------- #


def pipeline_root_path():

	"""
	Returns the pipeline root path.

	If the environment variable 'PROJEKT_PIPELINE_ROOT' is set, the function converts the value to a Nuke path
	using the 'convert_to_nuke_path' function and returns it. Otherwise, it prints a message indicating that
	'PROJEKT_PIPELINE_ROOT' was not found and calls the 'pipelineRootPath0' function.

	Returns:
		pathlib.Path: The pipeline root path.

	"""
	pipeline_root_env = os.getenv('PROJEKT_PIPELINE_ROOT')
	if pipeline_root_env:
		pipeline_root_path = convert_to_nuke_path(Path(pipeline_root_env))
		return pipeline_root_path
	else:
		logger.warning("PROJEKT_PIPELINE_ROOT not found...")
		return projekt_root_windows_path() # temp fix for windows...

# -------------------------------------------------------------------------- #

def nuke_pipeline_path():
	"""
	Returns the root path of the Nuke pipeline.

	This function attempts to retrieve the pipeline root path using the `pipelineRootPath` function.
	If the pipeline root path is not found, it falls back to the `projekt_root_windows_path` function.
	The retrieved pipeline root path is then extended by appending '/nuke' to it. then converted to a Nuke path.

	Returns:
		pathlib.Path: The root path of the Nuke pipeline.

	Raises:
		KeyError: If the pipeline root path cannot be found.

	"""

	try:
		nuke_pipeline_root = pipeline_root_path()
	except KeyError:
		logger.warning(f"KeyError: Pipeline Root not found... using windows path")
		nuke_pipeline_root = projekt_root_windows_path()
	nuke_pipeline_root = convert_to_nuke_path(nuke_pipeline_root / 'nuke')
	if not os.path.exists(nuke_pipeline_root):
		logger.error(f"Nuke pipeline root path does not exist: {nuke_pipeline_root}")
		raise FileNotFoundError(f"Nuke pipeline root path does not exist: {nuke_pipeline_root}")
	return nuke_pipeline_root

# -------------------------------------------------------------------------- #

def nuke_gizmos_path():
	"""
	Returns the path to the directory where the Nuke gizmos are located.

	:return: The path to the gizmo directory.
	:rtype: pathlib.Path
	"""
	gizmo_directory = nuke_pipeline_path() / "gizmos"
	return gizmo_directory

# -------------------------------------------------------------------------- #

def nuke_custom_gizmos_path():
    custom_gizmo_location = nuke_pipeline_path() / "gizmos"
    return custom_gizmo_location

# -------------------------------------------------------------------------- #

def nuke_scripts_path():

	"""
	Returns the path to the Nuke scripts directory.

	:return: The path to the Nuke scripts directory.
	:rtype: pathlib.Path
	"""
	nk_scripts_path = convert_to_nuke_path(nuke_pipeline_path() / 'pyScripts')
	return nk_scripts_path

# -------------------------------------------------------------------------- #

def nuke_toolsets_path():
	"""
	Returns the path to the nuke toolsets folder.

	Returns:
		pathlib.Path: The path to the nuke toolsets folder.
	"""
	nk_toolsets_path = nuke_pipeline_path() / 'toolsets'
	return nk_toolsets_path

# -------------------------------------------------------------------------- #

def nuke_templates_path():
	"""
	Returns the path to the nuke templates folder.

	Returns:
		pathlib.Path: The path to the nuke templates folder.
	"""
	try:
		template_root = Path(os.getenv('PROJEKT_PIPE_TEMPLATES'))
		nuke_templates = template_root / 'nuke'
	except TypeError:
		nuke_templates = nuke_pipeline_path() / 'Templates'
	return nuke_templates

# -------------------------------------------------------------------------- #

def ocio_configs_path():
	"""
	Returns the file path for the OCIO (OpenColorIO) configuration.

	Returns:
		pathlib.Path: The file path for the OCIO configuration.
	"""
	ocio_config_location = pipeline_root_path() / 'ocio'
	return ocio_config_location

# -------------------------------------------------------------------------- #

print("# -------------------------------------------------------------------------- #")
# logger.info("configured paths...")

print("# -------------------------------------------------------------------------- #")
print("path settings...")
print
print("projekt_root_path:	", projekt_root_path())
print("projekt_path:		", projekt_path())
print("PROJEKT_NAME		", projekt_name())	
print("projekt_shot:		", projekt_shot())
print("pipeline_root_path:	", pipeline_root_path())
print("nuke_pipeline_path:	", nuke_pipeline_path())
print("nuke_gizmos_path:	", nuke_gizmos_path())
print("nuke_custom_gizmos_path:", nuke_custom_gizmos_path())
print("nuke_scripts_path:	", nuke_scripts_path())
print("nuke_toolsets_path:	", nuke_toolsets_path())
print("nuke_templates_path:	", nuke_templates_path())
print("ocio_configs_path:	", ocio_configs_path())
print("# -------------------------------------------------------------------------- #")

# Move the logging statements for missing paths here
if projekt_root_path() is None:
	logger.warning("Projekt Root not found... ")
if projekt_shot() is None:
    logger.warning("PROJEKT_SHOT not found... ")

# -------------------------------------------------------------------------- #

# ========================================================================== #
# 53 54 52 45 4E 47 54 48 2D 49 4E 2D 4E 55 4D 42 45 52 53 C2 A9 32 30 32 35 #
# ========================================================================== #
