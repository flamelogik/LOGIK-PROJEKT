
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

# File Name:        toolsetUtilities.py
# Version:          0.0.1
# Created:          2024-10-28
# Modified:         2021-11-06

# -------------------------------------------------------------------------- #

"""
This module provides utility functions for managing Nuke toolsets and templates. 
It includes functions to open directories, export selected nodes as scripts, 
and create menus in Nuke's menu bar.

Functions:
1. `openDirectory(directory: Path) -> None`: Opens the specified directory in the file explorer.
2. `openToolsetsDir(directory: Path) -> None`: Opens the directory that contains the toolsets.
3. `openTemplatesDir(directory: Path) -> None`: Opens the directory that contains the templates.
4. `exportNodesAsScript() -> None`: Exports selected nodes as an nk script on disk in the specified directory.
5. `saveNodesAsToolset() -> None`: Exports selected nodes as an nk script on disk in the toolSetsDir folder.
6. `saveNodesAsTemplate() -> None`: Exports selected nodes as an nk script on disk in the templatesDir folder.
7. `createMenu() -> None`: Creates a menu in Nuke's menu bar with the specified title and index, 
    populated with items found in the specified directory path.
8. `addMenu(menu_title: str, index: int) -> None`: Adds a menu to Nuke.
9. `reloadMenu(menu_title: str, index: int) -> None`: Reloads the specified menu in Nuke.

Dependencies:
- nuke
- os
- sys
- pathlib
- projekt_core.settings
- projekt_core.utilities
- logging (for logger)


"""

import nuke
import os
import sys
from pathlib import Path

import projekt_core.settings as settings
import projekt_core.utilities as utilities


print("# -------------------------------------------------------------------------- #")

# ========================================================================== #
# This section imports the logging module and sets up the logger.
# ========================================================================== #

from projekt_core.utilities import logger

# ========================================================================== #
# This section assigns variables for the toolsets and templates directories.
# ========================================================================== #

try:
    toolSetsDir = Path(settings.nuke_toolsets_path())
    templatesDir = Path(settings.nuke_templates_path())
    # logger.info(f'toolsetsDir is set to: {toolSetsDir}')
    # logger.info(f'templatesDir is set to: {templatesDir}')
except Exception as e:
    logger.info(f'Error: {str(e)}')


# ========================================================================== #
# This section exports selected nodes as a script in the specified directory.
# ========================================================================== #

def exportNodesAsScript(export_type: str, directory: Path, reload_function) -> None:
	# Args:
		# export_type (str): The type of export (e.g., "Template" or "Toolset").
		# directory (Path): The directory where the script will be saved.
		# reload_function: The function to reload the menu.
    """
    Export selected nodes as an nk script on disk in the specified directory.

    :param export_type: The type of export (e.g., "Template" or "Toolset").
    :param directory: The directory where the script will be saved.
    :param reload_function: The function to reload the menu.
    """
    logger.info(f'Saving {export_type}')
    try:
        n = nuke.selectedNode()
        if n is None:
            nuke.message('No nodes selected!')
            return
        nukeExt = ".nknc" if nuke.env['nc'] else ".nk"
        
        # Use f-strings for modern and readable string formatting
        s = nuke.getFilename(f"Export Nodes As {export_type}", f"*{nukeExt}", f"{directory}/", "script", "save", extension=nukeExt)
        if s is not None:
            nuke.nodeCopy(s)
        reload_function()
    except Exception as e:
        logger.error(f'Error saving {export_type}: {str(e)}')
        

# ========================================================================== #
# This section exports selected nodes as a script into the toolsets and templates directories.
# ========================================================================== #

def saveNodesAsToolset() -> None:
    """
    Export selected nodes as an nk script on disk in the toolSetsDir folder.
    """
    exportNodesAsScript("Toolset", toolSetsDir, lambda: reloadMenu("Toolsets", 22))

# -------------------------------------------------------------------------- #

def saveNodesAsTemplate() -> None:
    """
    Export selected nodes as an nk script on disk in the templatesDir folder.
    """
    exportNodesAsScript("Template", templatesDir, lambda: reloadMenu("Templates", 23))


# ========================================================================== #
# This section creates a menu in Nuke.
# ========================================================================== #
def createMenu(menu_title: str, index: int, directory_path: Path, reload_command: str, open_folder_command: str, export_command: str) -> None:
    """
    Creates a menu in Nuke's menu bar with the specified title and index.
    The menu is populated with items found in the specified directory path.

    Args:
        menu_title (str): The title of the menu.
        index (int): The index at which the menu should be inserted in the menu bar.
        directory_path (Path): The path to the directory containing the menu items.
        reload_command (str): The command to execute when the "refreshMenu" item is selected.
        open_folder_command (str): The command to execute when the "open{menu_title}Folder" item is selected.
        export_command (str): The command to execute when the "exportNodesAs{menu_title}" item is selected.

    Returns:
        None
    """
    menubar = nuke.menu("Nuke")
    menu = menubar.addMenu(f"&{menu_title}", index=index)

    logger.info(f'Loading items from {directory_path}')

    for path, dirs, files in os.walk(directory_path):
        files.sort()
        dirs.sort()
        for file in files:
            if '#' not in path and '#' not in file and file.endswith(".nk") and not file.startswith("__"):
                name = file.split('.')[0]
                file_path = Path(path) / file
                menus = file_path.relative_to(directory_path).parts
                parent_menu = menu
                for menu_name in menus[:-1]:
                    if menu_name:
                        parent_menu = parent_menu.addMenu(f"&{menu_name}")
                parent_menu.addCommand(name, f'nuke.loadToolset("{file_path.as_posix()}")')

    menu.addSeparator()
    menu.addCommand('refreshMenu', reload_command, '')
    menu.addCommand(f'open{menu_title}Folder', open_folder_command, '')
    menu.addCommand(f'exportNodesAs{menu_title.rstrip("s")}', export_command, '') # strip the trailing 's'




# ========================================================================== #
# This section adds a menu to Nuke.
# ========================================================================== #

def addMenu(menu_title: str, index: int) -> None:
    """
    Adds a menu to Nuke.

    :param menu_title: The title of the menu to add.
    :param index: The index at which the menu should be inserted.
    """
    if menu_title == "Toolsets":
        createMenu(
            menu_title="Toolsets",
            index=index,
            directory_path=toolSetsDir,
            reload_command=f'projekt_core.toolsetUtilities.reloadMenu("Toolsets", {index})',
            open_folder_command=f'projekt_core.utilities.openToolsetsDir()',
            export_command='projekt_core.toolsetUtilities.saveNodesAsToolset()'
        )
    elif menu_title == "Templates":
        createMenu(
            menu_title="Templates",
            index=index,
            directory_path=templatesDir,
            reload_command=f'projekt_core.toolsetUtilities.reloadMenu("Templates", {index})',
            open_folder_command=f'projekt_core.utilities.openTemplatesDir()',
            export_command='projekt_core.toolsetUtilities.saveNodesAsTemplate()'
        )


# ========================================================================== #
# This section reloads the specified menu in Nuke.
# ========================================================================== #

def reloadMenu(menu_title: str, index: int) -> None:
    """
    Reloads the specified menu in Nuke.

    :param menu_title: The title of the menu to reload.
    :param index: The index at which the reloaded menu should be inserted.
    """
    menubar = nuke.menu("Nuke")
    menu = menubar.addMenu(f"&{menu_title}", str(index))
    menu.clearMenu()
    addMenu(menu_title, index)


# -------------------------------------------------------------------------- #

# ========================================================================== #
# C2 A9 32 30 32 34 20 7C 20 62 72 69 61 6E 40 73 69 6C 6F 38 34 2E 63 6F 6D #
# ========================================================================== #