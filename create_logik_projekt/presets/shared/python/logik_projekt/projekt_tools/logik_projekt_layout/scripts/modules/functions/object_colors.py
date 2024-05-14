# File Name:        object_colors.py

# -------------------------------------------------------------------------- #

# File Name:        object_colors.py
# Version:          0.0.9
# Language:         python script
# Flame Version:    2025.x
# Author:           Phil MAN - phil_man@mac.com
# Toolset:          MAN_MADE_MATERIAL: LOGIK-PROJEKT
# Created:          2024-04-20
# Modified:         2024-05-14
# Modifier:         Phil MAN - phil_man@mac.com

# Description:      This python script is part of a program that creates 
#                   logik projekt flame layouts.

# Installation:     Copy the 'LOGIK-PROJEKT' directory to:
#                   '/opt/Autodesk/shared/python/'

# Changelist:       The full changelist is at the end of this document.

# -------------------------------------------------------------------------- #

# ========================================================================== #
# This section defines color variables.
# ========================================================================== #

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

# return object_colors

# ========================================================================== #
# C2 A9 2D 32 30 32 34 2D 4D 41 4E 5F 4D 41 44 45 5F 4D 41 54 45 52 49 61 4C #
# ========================================================================== #

# Changelist:  
# -------------------------------------------------------------------------- #
# version:               0.0.1
# modified:              2024-05-03 - 01:53:36
# comments:              Basic functionality defined and tested
# -------------------------------------------------------------------------- #
# version:               0.0.2
# modified:              2024-05-03 - 02:13:01
# comments:              Fixed some formatting and flame menus
# -------------------------------------------------------------------------- #
# version:               0.0.3
# modified:              2024-05-03 - 11:26:02
# comments:              Changed 'the_current_project' to 'the_current_projekt'
# -------------------------------------------------------------------------- #
# version:               0.0.4
# modified:              2024-05-03 - 11:38:53
# comments:              Standardized 'logik-projekt' menu entries
# -------------------------------------------------------------------------- #
# version:               0.0.5
# modified:              2024-05-12 - 15:37:50
# comments:              Added function to read directories from JSON files.
# -------------------------------------------------------------------------- #
# version:               0.0.6
# modified:              2024-05-12 - 18:16:05
# comments:              Added a 'separators' function and tested in flame 2025.

# -------------------------------------------------------------------------- #
# version:               0.0.7
# modified:              2024-05-14 - 16:30:58
# comments:              Minor reformatting.
# -------------------------------------------------------------------------- #
# version:               0.0.8
# modified:              2024-05-14 - 16:31:23
# comments:              Changed object_colors from python to JSON.
# -------------------------------------------------------------------------- #
# version:               0.0.9
# modified:              2024-05-14 - 16:31:47
# comments:              Tested in flame 2025.
