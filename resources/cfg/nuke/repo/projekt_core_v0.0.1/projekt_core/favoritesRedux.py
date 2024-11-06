import os
import nuke

import projekt_core
from projekt_core import settings as settings
from projekt_core import utilities as utilities

# import projekt_core.settings
# import projekt_core.utilities



"""
- we'll need callbacks for on project load, close to dynamically add those to the FileChooser_Favorites.pref. 
- if nuke crashes, we might have stale entries, so maybe we need another function to clean those lines on nuke's launch.


"""
# ========================================================================== #
# This section imports the logging module and sets up the logger.
# ========================================================================== #

import projekt_core.settings
from projekt_core.utilities import logger

# ========================================================================== #
# This section clears the default bookmarks in Nuke.
# ========================================================================== #


def clear_default_bookmarks():
    """
    Clears the default bookmarks in Nuke.

    This function removes the default bookmarks from the favorites list in Nuke.
    The default bookmarks that are removed are 'Home', 'Root', 'Current', and 'Nuke'.
    """
    logger.info('Clearing default bookmarks')
    bookmarks = ['Home', 'Root', 'Current', 'Nuke']
    for bookmark in bookmarks:
        nuke.removeFavoriteDir(bookmark)

clear_default_bookmarks()

# ========================================================================== #
# This section defines the global and shot favorite configurations.
# ========================================================================== #
    
"""
type – Optional bitwise OR combination of nuke.IMAGE, nuke.SCRIPT, nuke.FONT or nuke.GEO.

nuke.IMAGE = 1
nuke.SCRIPT = 2
nuke.FONT = 4
nuke.GEO = 16
nuke.PYTHON = 32
nuke.IMAGE|nuke.GEO = 17
nuke.IMAGE|nuke.SCRIPT|nuke.GEO = 19
nuke.IMAGE|nuke.SCRIPT|nuke.GEO|nuke.PYTHON = 51
"""

def global_favorite_config():
    projekt_root_path = projekt_core.settings.projekt_root_path()
    projekt_path = projekt_core.settings.projekt_path()
    projList = [
            # ['--job context--','projekt_core.settings.projekt_root_path()',0,''],
            ['Projekt  root', projekt_root_path, 0, 'Server.png'],
            ['========== ', projekt_root_path, 0, 'Server.png'],
            ['Projekt dir', projekt_path, 0, 'Server.png'],
            ['==========', projekt_path / 'shots',0,''],
            ['→ assets', projekt_path / 'assets', 0, 'Server.png'],             
            ['→ shots', projekt_path /  'shots', 0, 'Server.png'], 
            ['→ editorial', projekt_path / 'editorial', 0, 'Server.png'], 
            ['→ reference', projekt_path / 'reference', 0, 'Server.png'], 


            #    ['EDITORIAL-Jobs', projekt_core.settings.projekt_root_path(), 0, 'Server.png'],
            #    ['PIPELINE-Resource', os.path.join(projekt_core.settings.projekt_path(), 'resource'), 0, 'FXElements.png'],
            #    ['PIPELINE', os.path.join(projekt_core.settings.projekt_path(), 'nukePipeline'), 32,'Pipeline.png'],
            #    ['  ','projekt_core.vfxtools.rootPath()',0,'']
              ]
    return projList

def shot_favorite_config():
    """
    
    """
    projekt_name = projekt_core.settings.projekt_name()
    projekt_path = projekt_core.settings.projekt_path()
    projekt_shots_dir = (projekt_path / 'shots')
    shot_name = nuke.root().knob('shot_name_knob').value()


    projList =[

        ['projekt dir', projekt_path, 0, 'Folder.png'],
        ['shots dir', projekt_path / 'shots', 0,''],
        ['========== ', projekt_path / 'shots',0,'Folder.png'],
        [f"{shot_name}", projekt_shots_dir / shot_name,0, 'Folder.png'],   
        ['==========', projekt_path / 'shots',0,''],
        [f" → {'scripts'}", projekt_shots_dir / shot_name / 'scripts' / 'nuke',0, 'Folder.png'], 
        [f" → {'sources'}", projekt_shots_dir / shot_name / 'media' / 'sources',0, 'Folder.png'],  
        [f" → {'renders'}", projekt_shots_dir / shot_name / 'media' /'renders',0, 'Folder.png'],  
             

        # [projekt_core.settings.projekt_name(), projekt_core.settings.projekt_path(),0, 'Folder.png'],
        # [f"----{shot_name}", str(projekt_shots_dir / shot_name),0, 'Folder.png'],        
        # ['------------------',utilities.convert_to_nuke_path_string(projekt_core.settings.projekt_path() / 'shots'),0,''],
        # [projekt_core.settings.projekt_shot(), projekt_core.settings.projekt_shot_path(),0, 'Folder.png'],

        #   ['IO', os.path.join(projekt_core.vfxtools.jobPath(),'IO'),1, 'Read.png'],
        #   ['Maya', os.path.join(projekt_core.vfxtools.jobPath(),'Maya'),16, 'Camera.png'],
        #   ['nk_scripts', os.path.join(projekt_core.settings.projekt_path(),'nuke','scripts'),2, 'NukeApp64.png'],
        #   ['cg_render', os.path.join(projekt_core.settings.projekt_path(),'cg','render'),1, 'Camera.png'],
        #   ['cg_cam', os.path.join(projekt_core.settings.projekt_path(),'cg','cam'),16, 'Camera.png'],
        #   ['cg_geo', os.path.join(projekt_core.settings.projekt_path(),'cg','geo'),16, 'Camera.png'],
        #   ['nuke_renders', os.path.join(projekt_core.settings.projekt_path(),'nuke', 'renders'),1, 'Write.png'],
        #   ['nuke_prerenders', os.path.join(projekt_core.settings.projekt_path(),'nuke', 'prerenders'),1, 'Write.png'],
        #   ['elements', os.path.join(projekt_core.settings.projekt_path(),'elements'),1, 'Read.png'],
        #   ['plates', os.path.join(projekt_core.settings.projekt_path(),'plates'),1, 'Read.png'],
        ]

    return projList

def work_favorite_config():
    """
    Project dir: /s84/jobs/The_Easy_Kind/
    Shot dir: /s84/jobs/The_Easy_Kind/sh010/
    Work dir: /s84/jobs/The_Easy_Kind/sh010/work/compositing/
    """
    projList = [
        ["Projekt dir", settings.projekt_path(),0, 'LoadParent.png'],
        ["Shot dir", settings.projekt_shot_path(),0, 'LoadParentPartly.png'],
        ['Work dir', settings.projekt_shot_path() / 'work' / 'compositing',0 ,'LoadNone.png'],        
    ]

    return projList



# ========================================================================== #
# This section manages favorites in Nuke based on the given action.
# ========================================================================== #

def manageFavorites(action, config_func, log_message):
    """
    Manages favorites in Nuke based on the given action.

    Args:
        action (str): The action to perform. Can be 'add' or 'remove'.
        config_func (function): A function that returns a list of items to be processed.
        log_message (str): The log message template to be used for logging.

    Returns:
        None

    Raises:
        None
    """
    icon_path = os.path.join(projekt_core.settings.nuke_pipeline_path(), 'icons')
    items = config_func()
    processed = []

    for item in items:
        if action == 'add':
            nuke.addFavoriteDir(item[0], directory=str(item[1]), type=item[2], icon=os.path.join(icon_path, item[3]))
        elif action == 'remove':
            nuke.removeFavoriteDir(item[0], item[2])
        processed.append(item[0])

    logger.info(log_message % ', '.join(processed))

# ========================================================================== #
# This section adds and removes global and shot favorites in Nuke.
# ========================================================================== #

def addGlobalFavorites():
    manageFavorites('add', global_favorite_config, 'Adding global favorites: %s')

def removeGlobalFavorites():
    manageFavorites('remove', global_favorite_config, 'Removing global favorites: %s')

def addFavoritesForCurrentShot():
    manageFavorites('add', shot_favorite_config, 'Adding Shot favorites: %s')

def removeFavoritesForCurrentShot():
    manageFavorites('remove', shot_favorite_config, 'Removing Shot favorites: %s')

def addWorkFavorites():
    manageFavorites('add', work_favorite_config, 'Adding Work favorites: %s')

def removeWorkFavorites():
    manageFavorites('remove', work_favorite_config, 'Removing Work favorites: %s')


# ========================================================================== #
# This section adds a callback to the 'favorites' knob to handle changes.
# ========================================================================== #

def favoritesKnobChanged():
    """
    Callback function triggered when the 'favorites' knob is changed.

    This function checks the value of the 'favorites' knob and performs different actions based on the value.
    If the value is 'projekt', it removes the favorites for the current shot and adds the global favorites.
    If the value is 'shot', it removes the global favorites and adds the favorites for the current shot.
    If the value is 'work', it removes the favorites for the current shot and adds the work favorites.

    Parameters:
        None

    Returns:
        None
    """
    knob = nuke.thisKnob()
    if knob.name() == 'favorites':
        logger.info("favoritesKnobChanged called")
        knob_value = knob.value()
        projekt_core.favoritesRedux.removeFavoritesForCurrentShot()
        projekt_core.favoritesRedux.removeGlobalFavorites()
        projekt_core.favoritesRedux.removeWorkFavorites()
        if knob_value == 'projekt':
            projekt_core.favoritesRedux.addGlobalFavorites()
        # shot bookmark checks...
        elif knob_value == 'shot':
            shot_name_knob = nuke.root().knob('shot_name_knob')
            if shot_name_knob.value() != '':
                # todo: add check if shot folder exists...
                projekt_core.favoritesRedux.addFavoritesForCurrentShot()
            else:
                nuke.message('Shot is not set. Please set the shot name.')
                knob_value = 'projekt'
        elif knob_value == 'work':
            projekt_core.favoritesRedux.addWorkFavorites()
