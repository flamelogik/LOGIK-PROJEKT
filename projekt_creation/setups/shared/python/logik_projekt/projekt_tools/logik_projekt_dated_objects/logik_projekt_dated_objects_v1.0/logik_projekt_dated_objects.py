# logik_projekt_dated_objects.py

# -------------------------------------------------------------------------- #

# Program Name:     logik_projekt_dated_objects.py
# Version:          1.0
# Language:         python script
# Flame Version:    2025.x
# Author:           Phil MAN - phil_man@mac.com
# Toolset:          MAN_MADE_MATERIAL
# Created:          2024-04-20
# Modified:         2024-04-20
# Modifier:         Phil MAN - phil_man@mac.com

# Changelist:       Code relabeled for LOGIK.tv distribution

# -------------------------------------------------------------------------- #

# Description:      This script creates dated objects.

# Installation:     Copy the 'LOGIK-PROJEKT' directory to:
#                   '/opt/Autodesk/shared/python/'

# -------------------------------------------------------------------------- #

# ========================================================================== #
# C2 A9 2D 32 30 32 34 2D 4D 41 4E 5F 4D 41 44 45 5F 4D 41 54 45 52 49 61 4C #
# ========================================================================== #

import flame
import datetime

# -------------------------------------------------------------------------- #

# Get today's date and time
today_date = datetime.date.today().strftime("%Y-%m-%d")
today_time = datetime.datetime.now().strftime("%H-%M-%S")

# -------------------------------------------------------------------------- #

# Define object colors
object_colors = {

    # Autodesk Colors
    "Red": (0.376, 0.047, 0.047),             # Red
    "Green": (0.114, 0.263, 0.176),           # Green
    "Bright Green": (0.102, 0.502, 0.208),    # Bright Green
    "Blue": (0.188, 0.263, 0.400),            # Blue
    "Light Blue": (0.263, 0.408, 0.502),      # Light Blue
    "Purple": (0.388, 0.318, 0.541),          # Purple
    "Orange": (0.600, 0.345, 0.165),          # Orange
    "Gold": (0.478, 0.478, 0.271),            # Gold
    "Yellow": (0.784, 0.784, 0.196),          # Yellow
    "Light Grey": (0.706, 0.706, 0.706),      # Light Grey
    "Black": (0.000, 0.000, 0.000),           # Black

    # Custom Colors
    "Dark Red": (0.188, 0.023, 0.023),        # Dark Red
    "Dark Green": (0.057, 0.131, 0.088),      # Dark Green
    "Dark Blue": (0.094, 0.131, 0.200),       # Dark Blue
    "Dark Purple": (0.194, 0.159, 0.270),     # Dark Purple
    "Dark Orange": (0.300, 0.172, 0.082),     # Dark Orange
    "Dark Gold": (0.239, 0.239, 0.135),       # Dark Gold

    # Grey Scale
    "Grey02": (0.928, 0.928, 0.928),          # Grey02
    "Grey03": (0.857, 0.857, 0.857),          # Grey03
    "Grey04": (0.786, 0.786, 0.786),          # Grey04
    "Grey05": (0.714, 0.714, 0.714),          # Grey05
    "Grey06": (0.643, 0.643, 0.643),          # Grey06
    "Grey07": (0.571, 0.571, 0.571),          # Grey07
    "Grey08": (0.500, 0.500, 0.500),          # Grey08
    "Grey09": (0.417, 0.417, 0.417),          # Grey09
    "Grey10": (0.333, 0.333, 0.333),          # Grey10
    "Grey11": (0.250, 0.250, 0.250),          # Grey11
    "Grey12": (0.167, 0.167, 0.167),          # Grey12
    "Grey13": (0.083, 0.083, 0.083)           # Grey13
}

# -------------------------------------------------------------------------- #

# Function to create or validate folders, reel groups, or reel objects.
def create_or_validate_object(
        library,
        object_name,
        object_type,
        object_color=None,
        object_reel_type=None,
        batch_group=False,
        reel_type='reel'  # Default to standard reel type
        ):

    # ---------------------------------------------------------------------- #

    # Check if the object exists in the library

    # For batch groups, continue with the existing logic
    if object_type == 'batch group':

        if batch_group:

            for group in library.batch_groups:

                if group.name == object_name:

                    print(
                        f"Batch group '{object_name}' already exists in library "
                        f"'{library.name}'."
                    )

                    return group

            # If the batch group doesn't exist, create it
            new_group = library.create_batch_group(
                name=object_name
                )

            if object_color:

                new_group.colour = object_color

            print(
                f"New batch group '{object_name}' created successfully in library "
                f"'{library.name}'."
            )
            return new_group

    # ---------------------------------------------------------------------- #

    # Reel groups need to be handled separately
    if object_type == 'reel group':

        for group in library.reel_groups:

            if group.name == object_name:

                print(
                    f"Reel group '{object_name}' already exists in library "
                    f"'{library.name}'."
                    )

                return group

        # If the reel group doesn't exist, create it
        new_group = library.create_reel_group(
            name=object_name
            )

        if object_color:

            new_group.colour = object_color

        print(
            f"New reel group '{object_name}' created successfully in library "
            f"'{library.name}'.")
        return new_group

    # ---------------------------------------------------------------------- #

    # For folders and reels, continue with the existing logic
    for obj in getattr(
        library,
        f"{object_type}s"
        ):

        if obj.name == object_name:

            print(
                f"{object_type.capitalize()} '{object_name}' already "
                f"exists in library '{library.name}'."
                )

            return obj

    # ---------------------------------------------------------------------- #

    # If the object doesn't exist, create it
    new_object = getattr(
        library,
        f"create_{object_type}"
        )(name=object_name)

    if object_color:

        new_object.colour = object_color

    if object_type == 'reel':
        if object_reel_type:
            new_object.attributes['Type'] = object_reel_type
            print(f"New reel '{object_name}' created successfully in library "
                f"'{library.name}' with Type '{object_reel_type}'.")
        else:
            print(f"New reel '{object_name}' created successfully in library "
                f"'{library.name}'.")
    else:
        print(
            f"New {object_type} '{object_name}' created successfully in library "
            f"'{library.name}'."
            )

    return new_object

# -------------------------------------------------------------------------- #

# Function to create or validate library objects.
def create_or_validate_library(
        workspace,
        library_name,
        object_color=None
        ):

    # ---------------------------------------------------------------------- #

    # Check if the library exists in the workspace
    for library in workspace.libraries:

        if library.name == library_name:

            print(
                f"Library '{library_name}' already exists in workspace "
                f"'{workspace.name}'."
                )

            return library

    # ---------------------------------------------------------------------- #

    # If the library doesn't exist, create it.
    new_library = workspace.create_library(
        name=library_name
        )

    if object_color:
        new_library.colour = object_color
    print(
        f"New library '{library_name}' created successfully in workspace "
        f"'{workspace.name}'."
        )

    return new_library

# -------------------------------------------------------------------------- #

# Rename current desktop with today's date
def create_logik_projekt_dated_desktop(*args):

    # If Flame passes any arguments, you can handle them here
    if args:
        print("Received arguments from Flame:", args)

    # ---------------------------------------------------------------------- #

    the_current_project = flame.projects.current_project
    the_current_workspace = the_current_project.current_workspace
    the_current_desktop = the_current_workspace.desktop

    # ---------------------------------------------------------------------- #

    # Validate or create 'desktops' library
    desktops_library = \
        create_or_validate_library(
            the_current_workspace,
            'desktops',
            object_colors.get("Dark Red")
            )

    # Validate or create 'work' folder in 'desktops'
    work_folder = \
        create_or_validate_object(
            desktops_library,
            'work',
            'folder'
            )

    # ---------------------------------------------------------------------- #

    # Change the current desktop name
    new_desktop_name = today_date + '-work'
    the_current_desktop.name = new_desktop_name

    # Print the name of the current desktop
    print(f"Current desktop: {the_current_desktop.name}")

    # Change the name and color of the reel group in the current desktop
    for desktop_reel_group in the_current_desktop.reel_groups:
        if desktop_reel_group.name == 'Reels':
            desktop_reel_group.name = today_date + '-conform'
            desktop_reel_group.colour = object_colors.get("Dark Purple")
            for reel in desktop_reel_group.reels:
                    if reel.name == 'Reel 1':
                        reel.name = 'ref'
                        reel.colour = object_colors.get("Dark Blue")
                    if reel.name == 'Reel 2':
                        reel.name = 'Sources'
                        reel.colour = object_colors.get("Dark Green")
                    if reel.name == 'Sequences':
                        reel.colour = object_colors.get("Dark Red")

    # Validate or create dated postings reel in 'pattern_browsed_clips'
    published_sequences_reel = \
        create_or_validate_object(
            desktop_reel_group,
            'Published-Sequences',
            'reel',
            # object_reel_type='Sequences',
            object_colors.get("Red")
            )

    # Validate or create dated postings reel in 'pattern_browsed_clips'
    published_versions_reel = \
        create_or_validate_object(
            desktop_reel_group,
            'Published-Versions',
            'reel',
            object_colors.get("Green")
            )

    # Validate or create dated postings reel in 'pattern_browsed_clips'
    todays_postings_reel = \
        create_or_validate_object(
            desktop_reel_group,
            today_date + '-postings',
            'reel',
            object_colors.get("Blue")
            )

    # ---------------------------------------------------------------------- #

# -------------------------------------------------------------------------- #

# Create new dated folder in reference library
def create_logik_projekt_dated_ref_folder(*args):

    # If Flame passes any arguments, you can handle them here
    if args:
        print("Received arguments from Flame:", args)

    # ---------------------------------------------------------------------- #

    the_current_project = flame.projects.current_project
    the_current_workspace = the_current_project.current_workspace
    the_current_desktop = the_current_workspace.desktop

    # ---------------------------------------------------------------------- #

    # Validate or create 'reference' library
    reference_library = \
        create_or_validate_library(
            the_current_workspace,
            'reference',
            object_colors.get("Dark Orange")
            )

    # Validate or create dated reference folder in 'reference'
    todays_reference_folder = \
        create_or_validate_object(
            reference_library,
            today_date + '-reference',
            'folder'
            )

    # ---------------------------------------------------------------------- #

# -------------------------------------------------------------------------- #

# Create new dated reel group in editorial library
def create_logik_projekt_dated_conforms_reel_group(*args):

    # If Flame passes any arguments, you can handle them here
    if args:
        print("Received arguments from Flame:", args)

    # ---------------------------------------------------------------------- #

    the_current_project = flame.projects.current_project
    the_current_workspace = the_current_project.current_workspace
    the_current_desktop = the_current_workspace.desktop

    # ---------------------------------------------------------------------- #

    # Validate or create 'editorial' library
    editorial_library = \
        create_or_validate_library(
            the_current_workspace,
            'editorial',
            object_colors.get("Dark Gold")
            )

    # Validate or create folder 'conforms' in 'editorial'
    conforms_folder = \
        create_or_validate_object(
            editorial_library,
            'conforms',
            'folder'
            )

    # Validate or create dated conforms reel group in 'conforms'
    dated_conforms_reel_group = \
        create_or_validate_object(
            conforms_folder,
            today_date + '-conform',
            'reel group'
            )

    # Rename reels in 'dated conforms reel group'
    for reel in dated_conforms_reel_group.reels:
        if reel.name == 'Reel 1':
            reel.name = 'ref'
            reel.colour = object_colors.get("Dark Blue")
        if reel.name == 'Reel 2':
            reel.name = 'Sources'
            reel.colour = object_colors.get("Dark Green")
        if reel.name == 'Sequences':
            reel.colour = object_colors.get("Dark Red")

    # ---------------------------------------------------------------------- #

# -------------------------------------------------------------------------- #

# Create new dated postings reel
def create_logik_projekt_dated_postings_reel(*args):

    # If Flame passes any arguments, you can handle them here
    if args:
        print("Received arguments from Flame:", args)

    # ---------------------------------------------------------------------- #

    the_current_project = flame.projects.current_project
    the_current_workspace = the_current_project.current_workspace
    the_current_desktop = the_current_workspace.desktop

    # ---------------------------------------------------------------------- #

    # Validate or create 'editorial' library
    editorial_library = \
        create_or_validate_library(
            the_current_workspace,
            'editorial',
            object_colors.get("Dark Gold")
            )

    # Validate or create folder 'work_in_progress' in 'editorial'
    work_in_progress_folder = \
        create_or_validate_object(
            editorial_library,
            'work_in_progress',
            'folder'
            )

    # Validate or create folder 'postings' in 'work_in_progress'
    postings_folder = \
        create_or_validate_object(
            work_in_progress_folder,
            'postings',
            'folder',
            object_colors.get("Blue")
            )

    # Validate or create dated postings reel in 'postings'
    todays_postings_reel = \
        create_or_validate_object(
            postings_folder,
            today_date + '-postings',
            'reel'
            )

    # ---------------------------------------------------------------------- #

# -------------------------------------------------------------------------- #

# Add custom UI actions
def get_main_menu_custom_ui_actions():

    return [
        {
            'name': 'logik_projekt',
            'hierarchy': [],
            'actions': []
        },
        {
            'name': 'logik_projekt_layout',
            'hierarchy': ['logik_projekt'],
            'order': 5,
            'actions': [
                {
                    'name': 'create logik_projekt_dated_desktop',
                    'execute': create_logik_projekt_dated_desktop,
                    'minimumVersion': '2025'
                }
            ]
        },
        {
            'name': 'logik_projekt_layout',
            'hierarchy': ['logik_projekt'],
            'order': 6,
            'actions': [
                {
                    'name': 'create logik_projekt_dated_ref_folder',
                    'execute': create_logik_projekt_dated_ref_folder,
                    'minimumVersion': '2025'
                }
            ]
        },
        {
            'name': 'logik_projekt_layout',
            'hierarchy': ['logik_projekt'],
            'order': 7,
            'actions': [
                {
                    'name': 'create logik_projekt_dated_conforms_reel_group',
                    'execute': create_logik_projekt_dated_conforms_reel_group,
                    'minimumVersion': '2025'
                }
            ]
        },
        {
            'name': 'logik_projekt_layout',
            'hierarchy': ['logik_projekt'],
            'order': 8,
            'actions': [
                {
                    'name': 'create logik_projekt_dated_postings_reel',
                    'execute': create_logik_projekt_dated_postings_reel,
                    'minimumVersion': '2025'
                }
            ]
        }
    ]

# -------------------------------------------------------------------------- #

# def get_mediahub_files_custom_ui_actions():

#     return [
#         {
#             'name': 'logik_projekt_layout',
#             'hierarchy': ['logik_projekt'],
#             'order': 5,
#             'actions': [
#                 {
#                     'name': 'create logik_projekt_dated_desktop',
#                     'execute': create_logik_projekt_dated_desktop,
#                     'minimumVersion': '2025'
#                 }
#             ]
#         },
#         {
#             'name': 'logik_projekt_layout',
#             'hierarchy': ['logik_projekt'],
#             'order': 6,
#             'actions': [
#                 {
#                     'name': 'create logik_projekt_dated_ref_folder',
#                     'order': 2,
#                     'separator': 'below',
#                     'execute': create_logik_projekt_dated_ref_folder,
#                     'minimumVersion': '2025'
#                 }
#             ]
#         },
#         {
#             'name': 'logik_projekt_layout',
#             'hierarchy': ['logik_projekt'],
#             'order': 7,
#             'actions': [
#                 {
#                     'name': 'create logik_projekt_dated_conforms_reel_group',
#                     'order': 3,
#                     'separator': 'below',
#                     'execute': create_logik_projekt_dated_conforms_reel_group,
#                     'minimumVersion': '2025'
#                 }
#             ]
#         },
#         {
#             'name': 'logik_projekt_layout',
#             'hierarchy': ['logik_projekt'],
#             'order': 8,
#             'actions': [
#                 {
#                     'name': 'create logik_projekt_dated_postings_reel',
#                     'order': 4,
#                     'separator': 'below',
#                     'execute': create_logik_projekt_dated_postings_reel,
#                     'minimumVersion': '2025'
#                 }
#             ]
#         }
#     ]

# -------------------------------------------------------------------------- #

def get_media_panel_custom_ui_actions():

    return [
        {
            'name': 'logik_projekt_layout',
            'hierarchy': ['logik_projekt'],
            'order': 5,
            'actions': [
                {
                    'name': 'create logik_projekt_dated_desktop',
                    'order': 5,
                    'separator': 'below',
                    'execute': create_logik_projekt_dated_desktop,
                    'minimumVersion': '2025'
                }
            ]
        },
        {
            'name': 'logik_projekt_layout',
            'hierarchy': ['logik_projekt'],
            'order': 6,
            'actions': [
                {
                    'name': 'create logik_projekt_dated_ref_folder',
                    'order': 6,
                    'separator': 'below',
                    'execute': create_logik_projekt_dated_ref_folder,
                    'minimumVersion': '2025'
                }
            ]
        },
        {
            'name': 'logik_projekt_layout',
            'hierarchy': ['logik_projekt'],
            'order': 7,
            'actions': [
                {
                    'name': 'create logik_projekt_dated_conforms_reel_group',
                    'order': 7,
                    'separator': 'below',
                    'execute': create_logik_projekt_dated_conforms_reel_group,
                    'minimumVersion': '2025'
                }
            ]
        },
        {
            'name': 'logik_projekt_layout',
            'hierarchy': ['logik_projekt'],
            'order': 8,
            'actions': [
                {
                    'name': 'create logik_projekt_dated_postings_reel',
                    'order': 8,
                    'separator': 'below',
                    'execute': create_logik_projekt_dated_postings_reel,
                    'minimumVersion': '2025'
                }
            ]
        }
    ]

# -------------------------------------------------------------------------- #

# If this script is executed as main:
# Call functions for immediate execution
if __name__ == "__main__":
    create_logik_projekt_dated_ref_folder()
    create_logik_projekt_dated_desktop()
    create_logik_projekt_dated_conforms_reel_group()
    create_logik_projekt_dated_postings_reel()

# -------------------------------------------------------------------------- #

# ========================================================================== #
# C2 A9 2D 32 30 32 34 2D 4D 41 4E 5F 4D 41 44 45 5F 4D 41 54 45 52 49 61 4C #
# ========================================================================== #
