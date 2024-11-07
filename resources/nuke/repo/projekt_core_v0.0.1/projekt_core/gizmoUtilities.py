
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

# File Name:        gizmoUtilities.py
# Version:          0.0.1
# Created:          2024-10-27
# Modified:         2021-11-06

# -------------------------------------------------------------------------- #

"""
This module is responsible for managing gizmo directories and loading gizmos into Nuke.
It sets up the gizmo directory path and provides utilities for adding gizmos to the Nuke menu.

Key Features:
- Sets up the gizmo directory path based on project settings.
- Logs the gizmo directory path for debugging purposes.
- Provides a mechanism to add gizmos to the Nuke plugin path and menu.

Usage:
- This module is typically imported and used in the `menu.py` file to add gizmos to the Nuke menu.
"""

import nuke
import os
import re
import inspect
from typing import Optional
import projekt_core.settings


# for windows pathing:
try:
    from pathlib import PurePosixPath as Path
except ImportError:
    pass

# ========================================================================== #
# This section imports the logging module and sets up the logger.
# ========================================================================== #

from projekt_core.utilities import logger

# ========================================================================== #
# This section defines the global variables and constants.
# ========================================================================== #


# Set the gizmo directory path based on project settings
gizmo_directory = projekt_core.settings.nuke_gizmos_path()
print("# -------------------------------------------------------------------------- #")
logger.info(f"gizmo_directory: {gizmo_directory}")

# Global variable to store the current gizmo menu
current_gizmo_menu = None
gizManager = None  # Declare gizManager as a global variable

CUSTOM_GIZMO_LOCATION = projekt_core.settings.nuke_custom_gizmos_path()
logger.info(f"CUSTOM_GIZMO_LOCATION: {CUSTOM_GIZMO_LOCATION}")

# -------------------------------------------------------------------------- #

# ========================================================================== #
# This section defines the GizmoPathManager class.
# ========================================================================== #

class GizmoPathManager(object):
    '''
    Class used to automatically add directory trees to the Nuke plugin path,
    and to build menu items for any gizmos found in those trees.
    '''
    def __init__(self, searchPaths=None, exclude=r'^\.|^_', ):
        '''
        'searchPaths': An iterable of paths to recursively search. If omitted,
        the search will first try to use the `NUKE_GIZMO_PATH` environment
        variable. If that is also undefined, it will resolve and use the
        directory in which this file resides. If that cannot be determined, the
        contents of the Nuke plugin path will be used.

        'exclude': A regular expression for folders and gizmo files to ignore.
        The default pattern ignores anything beginning with `.`.
        '''
        if isinstance(exclude, str):
            exclude = re.compile(exclude)
        self.exclude = exclude
        self.logger = logger
        self.logger.info(f'Search path: {searchPaths}')
        self.logger.info(f'Exclude pattern: {exclude}')
        if searchPaths is None:
            searchPaths = os.environ.get('NUKE_GIZMO_PATH', '').split(os.pathsep)
            if not searchPaths:
                thisFile = inspect.getsourcefile(lambda: None)
                if thisFile:
                    searchPaths = [os.path.dirname(os.path.abspath(thisFile))]
                else:
                    searchPaths = list(nuke.pluginPath())
        self.searchPaths = searchPaths
        self.reset()

    @classmethod
    def canonical_path(cls, path):
        return os.path.normcase(os.path.normpath(os.path.realpath(os.path.abspath(path))))

    def reset(self):
        self._crawlData = {}

    def addGizmoPaths(self):
        '''Recursively search ``self.searchPaths`` for folders whose names do not
        match the exclusion pattern ``self.exclude``, and add them to the Nuke
        plugin path.'''
        self.reset()
        self._visited = set()
        for gizPath in self.searchPaths:
            self.logger.info(f'GizPath: {gizPath}')
            self._recursiveAddGizmoPaths(gizPath, self._crawlData,
                                         foldersOnly=True)

    def _recursiveAddGizmoPaths(self, folder, crawlData, foldersOnly=False):
        # If we're in GUI mode, also store away data in _crawlData to to be used
        # later by addGizmoMenuItems
        if not os.path.isdir(folder):
            return

        if nuke.GUI:
            if 'files' not in crawlData:
                crawlData['gizmos'] = []
            if 'dirs' not in crawlData:
                crawlData['dirs'] = {}

        # avoid an infinite loop due to symlinks...
        canonical_path = self.canonical_path(folder)
        if canonical_path in self._visited:
            return
        self._visited.add(canonical_path)

        for subItem in sorted(os.listdir(canonical_path)):
            if self.exclude and self.exclude.search(subItem):
                continue
            subPath = os.path.join(canonical_path, subItem)
            if os.path.isdir(subPath):
                nuke.pluginAppendPath(subPath)
                subData = {}
                if nuke.GUI:
                    crawlData['dirs'][subItem] = subData
                self._recursiveAddGizmoPaths(subPath, subData)
            elif nuke.GUI and (not foldersOnly) and os.path.isfile(subPath):
                name, ext = os.path.splitext(subItem)
                if ext == '.gizmo':
                    crawlData['gizmos'].append(name)
                if ext == '.nk':
                    crawlData['gizmos'].append(name + '.nk')

    def addGizmoMenuItems(self, rootMenu=None, defaultTopMenu=None):
        '''
        Recursively creates menu items for gizmos found on this instance's
        search paths. This only has an effect if Nuke is in GUI mode.

        'rootMenu': The root Nuke menu to which the menus and menu items should
        be added, either as a ``nuke.Menu`` object or a string. If omitted, the
        Nuke 'Nodes' menu will be used.

        'defaultTopMenu': If you do not wish to create new menu items at the
        top level of the target parent menu, directories for which top-level
        menus do not already exist will be added to this menu instead. This
        must be the name of an existing menu.
        '''
        if not nuke.GUI:
            return

        if not self._crawlData:
            self.addGizmoPaths()

        if rootMenu is None:
            rootMenu = nuke.menu('Nodes')
        elif isinstance(rootMenu, str):
            rootMenu = nuke.menu(rootMenu).addMenu('menuTitle')


        self._recursiveAddGizmoMenuItems(rootMenu, self._crawlData,
                                         defaultSubMenu=defaultTopMenu,
                                         topLevel=True)

    def _recursiveAddGizmoMenuItems(self, toolbar, crawlData,
                                    defaultSubMenu=None, topLevel=False):
        """
        sorting only crawlData.get 'dirs', not crawlData.get 'gizmos'
        """
        for name in crawlData.get('gizmos', ()):
            niceName = name
            if name.endswith(".nk"):
                niceName = name[:-3]
            if niceName.find('_v') == len(name) - 4:
                niceName = name[:-4]
            toolbar.addCommand(niceName, f"nuke.createNode('{name}')")

        for folder, data in sorted(crawlData.get('dirs', {}).items()):
            subMenu = toolbar.findItem(folder)
            if subMenu is None:
                if defaultSubMenu:
                    subMenu = toolbar.findItem(defaultSubMenu)
                else:
                    subMenu = toolbar.addMenu(folder, icon=f"{folder}.png")
            self._recursiveAddGizmoMenuItems(subMenu, data)


# ========================================================================== #
# This section defines the utility functions.
# ========================================================================== #

def add_menu(root_menu: Optional[str] = None, index=9, default_top_menu: Optional[str] = None) -> None:
    """
    Add gizmos to the Nuke menu and the DAG tab menu, making them accessible.
    
    Parameters:
    root_menu (str, optional): The menu to which the gizmos will be added.
    default_top_menu (str, optional): The default top menu.
    
    Returns:
    None
    """
    global current_gizmo_menu
    current_gizmo_menu = root_menu

    try:
        # Access gizManager
        giz_manager = projekt_core.gizmoUtilities.gizManager  # Access gizManager directly from gizmoUtilities
        if giz_manager is None:
            logger.warning('gizManager is not available as a global')
            return

        # create the Nuke menu...
        nuke.menu("Nuke").addMenu(root_menu, index=index)
        logger.info(f'Adding menu items to {root_menu} at index {index}')

        logger.info('Adding gizmo menu items...')
        add_gizmo_menu_items(giz_manager, root_menu)
        logger.info('Gizmo menu items added')
        del giz_manager

        add_additional_items_to_menu("Nodes", root_menu)
        add_additional_items_to_menu("Nuke", root_menu)
    except Exception as e:
        logger.error(f"An error occurred while adding menu items: {e}")

# -------------------------------------------------------------------------- #

def add_gizmo_menu_items(giz_manager, root_menu: Optional[str]) -> None:
    """
    Add gizmo menu items to the specified root menu.
    
    Parameters:
    giz_manager: The gizManager object to manage gizmos.
    root_menu (str, optional): The menu to which the gizmos will be added.
    
    Returns:
    None
    """
    giz_manager.addGizmoMenuItems(nuke.menu("Nodes").addMenu(root_menu))
    giz_manager.addGizmoMenuItems(nuke.menu("Nuke").addMenu(root_menu))

# -------------------------------------------------------------------------- #

def add_additional_items_to_menu(menu_name: str, root_menu: Optional[str]) -> None:
    """
    Add additional items to the specified menu.
    
    Parameters:
    menu_name (str): The name of the menu to which items will be added.
    root_menu (str, optional): The root menu to find the item.
    
    Returns:
    None
    """
    menu_item = nuke.menu(menu_name).findItem(root_menu)
    if menu_item:
        menu_item.addSeparator()
        menu_item.addCommand('refreshMenu', 'projekt_core.gizmoUtilities.reload_menu()', '')
        menu_item.addCommand('openGizmosFolder', 'projekt_core.utilities.openGizmosDir()', '')
    else:
        logger.warning(f'Menu "{menu_name}" not found')

# -------------------------------------------------------------------------- #

def remove_menu(root_menu: Optional[str] = None) -> None:
    """
    Remove gizmos from the Nuke menu and the DAG tab menu.
    
    Parameters:
    root_menu (str, optional): The menu from which the gizmos will be removed.
    
    Returns:
    None
    """
    try:
        logger.info('Removing gizmo menu items...')
        nuke.menu("Nodes").removeItem(root_menu)
        nuke.menu("Nuke").removeItem(root_menu)
        logger.info('Gizmo menu items removed')
    except Exception as e:
        logger.error(f"An error occurred while removing menu items: {e}")

# -------------------------------------------------------------------------- #

def reload_menu() -> None:
    """
    Reload gizmos in the Nuke menu by removing and then adding them again.
    
    Returns:
    None
    """
    global current_gizmo_menu, gizManager
    if current_gizmo_menu:
        remove_menu(current_gizmo_menu)
        # Re-initialize gizManager to pick up changes
        if CUSTOM_GIZMO_LOCATION and os.path.isdir(CUSTOM_GIZMO_LOCATION):
            gizManager = GizmoPathManager(searchPaths=[CUSTOM_GIZMO_LOCATION])
        else:
            gizManager = GizmoPathManager()
        gizManager.addGizmoPaths()
        add_menu(current_gizmo_menu)


# ========================================================================== #
# This section defines the main function.
# ========================================================================== #

def main(): 
    global gizManager
    if CUSTOM_GIZMO_LOCATION and os.path.isdir(CUSTOM_GIZMO_LOCATION):
        logger.info('CUSTOM_GIZMO_LOCATION found, and path exists')
        gizManager = GizmoPathManager(searchPaths=[CUSTOM_GIZMO_LOCATION])
    else:
        gizManager = GizmoPathManager()
    gizManager.addGizmoPaths()
    
    logger.info('Gizmo paths added')
    
    # check if gizManager is available as a global
    if 'gizManager' in globals():
        logger.info('gizManager is available as a global')
    else:
        logger.warning('gizManager is not available as a global')

if __name__ == '__main__':
    logger.info('running __main__')
    main()

print("# -------------------------------------------------------------------------- #")

# -------------------------------------------------------------------------- #

# ========================================================================== #
# C2 A9 32 30 32 34 20 7C 20 62 72 69 61 6E 40 73 69 6C 6F 38 34 2E 63 6F 6D #
# ========================================================================== #
