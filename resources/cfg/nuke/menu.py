import nuke


print("# -------------------------------------------------------------------------- #")
print("running menu.py...")

# ========================================================================== #
# This section imports various projekt_core tools
# ========================================================================== #


# Import projekt_core modules

# try:
#     import projekt_core
#     print("projekt_core imported successfully.")
# except ImportError as e:
#     print(f"Error importing core: {e}")

try:
    import projekt_core.settings
    print("projekt_core.settings imported successfully.")
except ImportError as e:
    print(f"Error importing core: {e}")

try:
    import projekt_core.utilities
    print("projekt_core.utilities imported successfully.")
except ImportError as e:
    print(f"Error importing core: {e}")

try:
    import projekt_core.vfxtools
    print("projekt_core.vfxtools imported successfully.")
except ImportError as e:
    print(f"Error importing core: {e}")

try:
    import projekt_core.favoritesRedux
    # logger.info("projekt_core.favoritesRedux imported successfully.")
    print("projekt_core.favoritesRedux imported successfully.")

except ImportError as e:
    print(f"Error importing favoritesRedux: {e}")


# ========================================================================== #
# This section imports the logging module and sets up the logger.
# ========================================================================== #

from projekt_core.utilities import logger

# ========================================================================== #
# This section adds a PROJEKT tab on the Root node.
# ========================================================================== #

projekt_core.vfxtools.create_projekt_panel()

# -------------------------------------------------------------------------- #

# add a callback to update the job warnings
# nuke.addKnobChanged(projekt_core.vfxtools.jobWarnings, nodeClass="Root")
#nuke.addUpdateUI(projekt_core.vfxtools.jobWarnings, nodeClass="Root")

# ========================================================================== #
# This section registers a callback for job warnings.
# ========================================================================== #

# Register the callback for any knob change
nuke.addKnobChanged(projekt_core.vfxtools.update_root_warnings_callback, nodeClass='Root')



# ========================================================================== #
# This section builds the PROJEKT menu on the toolbar.
# ========================================================================== #
"""
Work Files...
-----
Create...
Publish...
Load...
Manage...
-----
Library...
-----
Set Resolution
Set Frame Range
Set Colorspace
Apply All Settings
-----
Build Workfile
Template Builder ->
-----
Experimental tools...
"""

menuTitle="PROJEKT"
menubar = nuke.menu("Nuke")

# index=7 places the PROJEKT menu after default nuke menus.
projekt_menu = menubar.addMenu(menuTitle,index=7)

# add a info string to the menu /sh010, compositing {shot}/{task}
projekt_menu.addCommand("{shot}| compositing", 
                             '', 
                             '')
projekt_menu.addSeparator()
projekt_menu.addCommand('work files...', 
                             projekt_core.utilities.placeholder_func, 
                             '')
projekt_menu.addSeparator()
projekt_menu.addCommand('publish...', 
                             projekt_core.utilities.placeholder_func, 
                             '')
projekt_menu.addCommand('load...', 
                             projekt_core.utilities.placeholder_func, 
                             '')
projekt_menu.addCommand('manage...', 
                             projekt_core.utilities.placeholder_func, 
                             '')
projekt_menu.addSeparator()
projekt_menu.addCommand('library...', 
                             projekt_core.utilities.placeholder_func, 
                             '')
projekt_menu.addSeparator()
projekt_menu.addCommand('scripts/print_env_vars', 
                             'projekt_core.utilities.placeholder_func()', 
                             '')
projekt_menu.addCommand('scripts/unpack_direnv_diff', 
                             'print(projekt_core.vfxtools.unpack_direnv_diff())', 
                             '')

# ========================================================================== #
# This section adds gizmos to the menu and node toolbar.
# ========================================================================== #

# add a menu for scanned gizmos, supply the name of the toolbar/node to add.
gizmo_menu = "Toolzz"
# Store the gizmo_menu globally
global current_gizmo_menu
current_gizmo_menu = gizmo_menu

# Add the menu
projekt_core.gizmoUtilities.add_menu(root_menu=current_gizmo_menu)



# ========================================================================== #
# This section adds Toolsets, Templates to the menu.
# ========================================================================== #

try:
    import projekt_core.toolsetUtilities
    print("projekt_core.toolsetUtilities imported successfully.")
except ImportError as e:
    print(f"Error importing core: {e}")

# -------------------------------------------------------------------------- #
# Add the Toolsets Menu...
projekt_core.toolsetUtilities.addMenu("Toolsets", index=9)

# -------------------------------------------------------------------------- #
# Add the Templates Menu...
projekt_core.toolsetUtilities.addMenu("Templates", index=10)


# ========================================================================== #
# This section adds pyScripts to the menu.
# ========================================================================== #

try:
    import pyScripts
    import projekt_core.setupScripts
    print("projekt_core.setupScripts imported successfully.")
    print("# -------------------------------------------------------------------------- #")
except ImportError as e:
    print(f"Error importing core: {e}")



# ========================================================================== #
# This section handles dynamic favorites, includes callback.
# ========================================================================== #


# # -------------------------------------------------------------------------- #
# # callback to add global favorites
nuke.addOnCreate(projekt_core.favoritesRedux.addGlobalFavorites, nodeClass = 'Root')

# Flag to ensure single registration
if not hasattr(nuke, 'favoritesKnobChanged_registered'):
    nuke.addKnobChanged(projekt_core.favoritesRedux.favoritesKnobChanged, nodeClass='Root')
    nuke.favoritesKnobChanged_registered = True

# -------------------------------------------------------------------------- #
# def setShotFavesOnLoad(): 
    # 
    # todo: this is not implemented yet... should be moved into favoritesRedux.py...
    # """
#     logger.info("Running setShotFavesOnLoad")
#     projekt_core.favoritesRedux.removeFavoritesForCurrentShot()
#     projekt_core.favoritesRedux.addFavoritesForCurrentShot()


# nuke.addOnScriptLoad(setShotFavesOnLoad, nodeClass='Root')



# ========================================================================== #
# This section registers callbacks for script load...
# ========================================================================== #

# Register the callback to set the set environment variables on empty script load
# nuke.addOnCreate(projekt_core.vfxtools.on_root_node_create_callback, nodeClass='Root')
# nuke.addOnScriptLoad(projekt_core.vfxtools.on_root_node_create_callback, nodeClass='Root')


# ========================================================================== #
# This section loads knob defaults.
# ========================================================================== #

# Node defaults
#import defaults

# ========================================================================== #
# This section loads additional tools.
# ========================================================================== #

# Toggle Viewer Pipes
# import viewerOps
# nuke.menu("Nuke").addCommand('Viewer/Toggle Viewer Pipes', 
#                              viewerOps.toggleViewerPipes, 
#                              'alt+t')

# # -------------------------------------------------------------------------- #

# # ReadFromWrite
# import readFromWrite
# nuke.menu('Nuke').addCommand('Edit/Node/Read from Write',
#                              'readFromWrite.ReadFromWrite()',
#                              'alt+r')

# ========================================================================== #
# This section defines third party tool packages.
# ========================================================================== #

# Example:
# KnobScripter v3.1.0
# https://github.com/adrianpueyo/KnobScripter

# print("Importing KnobScripter:")
# nuke.pluginAddPath("./repo/KnobScripter-3.1.0")
# try:
#     import KnobScripter
# except ImportError:
#     print("Failed to import KnobScripter... Continuing without it.")


# -------------------------------------------------------------------------- #

print("# -------------------------------------------------------------------------- #")


#nuke.addOnCreate(createWriteDirectories, nodeClass='Write')
#nuke.addOnCreate(createWriteDirectories, nodeClass='DeepWrite')
#nuke.addOnCreate(createWriteDirectories, nodeClass='WriteGeo')
#nuke.addOnCreate(createWriteDirectories, nodeClass='SmartVector')
