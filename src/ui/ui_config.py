#!/usr/bin/env python3
# -------------------------------------------------------------------------- #
# Filename:     ui_config.py
# Purpose:      Centralizes UI configuration for the application.
# Description:  This module defines dimensions, paddings, and other layout-related
#               values to ensure a consistent look and feel across the application.

# Author:       phil_man@mac.com
# Copyright:    Copyright (c) 2025
# Disclaimer:   Disclaimer at bottom of script.
# License:      GNU General Public License v3.0 (GPL-3.0).
#               https://www.gnu.org/licenses/gpl-3.0.en.html

# Version:      2026.1.0
# Status:       Production
# Type:         Configuration
# Created:      2025-07-01
# Modified:     2025-08-03

# Changelog:    Changelog at bottom of script.
# -------------------------------------------------------------------------- #

"""
UI Configuration
================

This module centralizes the configuration for the user interface,
including dimensions, paddings, and other layout-related values.
By managing these settings in one place, we can ensure a consistent
look and feel across the application and easily make adjustments.

Sections:
---------
- Window Settings: Main window dimensions.
- Panel Settings: Dimensions for the main panels.
- Widget Settings: Default dimensions for common widgets.
- Layout Settings: Margins, spacing, and paddings.
"""

# 1. Window Settings
# ==================
# Main window dimensions
WINDOW_WIDTH = 1920
WINDOW_HEIGHT = 1080

# 2. Panel Settings
# =================
# Width of the left and right containers in the main AppWindow
LEFT_CONTAINER_WIDTH = 720
RIGHT_CONTAINER_WIDTH = 1200

# Height for the panels
PANEL_HEIGHT = 64
TEMPLATE_INFO_PANEL_HEIGHT = 180
TEMPLATE_PARAMETERS_PANEL_HEIGHT = 456
TEMPLATE_SUMMARY_PANEL_HEIGHT = 444
PROJEKT_TEMPLATE_PANEL_HEIGHT = 336
FLAME_OPTIONS_PANEL_HEIGHT = 216
PROJEKT_SUMMARY_PANEL_HEIGHT = 528

# To set a fixed width for all panels, uncomment the following line:
# PANEL_WIDTH = 700

# 3. Widget Settings
# ==================
# Default height for standard widgets like QLineEdit, QComboBox, etc.
WIDGET_HEIGHT = 28

# You can also define specific heights for different widget types
ENTRY_HEIGHT = 28
COMBOBOX_HEIGHT = 28
BUTTON_HEIGHT = 32

# 4. Layout Settings
# ==================
# Margins for the main layout in AppWindow
MAIN_LAYOUT_MARGINS = (16, 0, 16, 0) # (left, top, right, bottom)

# Spacing for layouts within panels
PANEL_LAYOUT_SPACING = 4
PANEL_LAYOUT_MARGINS = (0, 0, 0, 0)
PANEL_PADDING = (0, 4, 0, 4)


# -------------------------------------------------------------------------- #

# DISCLAIMER:   This file is part of LOGIK-PROJEKT.

#               Copyright © 2025 STRENGTH IN NUMBERS

#               LOGIK-PROJEKT creates directories, files, scripts & tools
#               for use with Autodesk Flame and other software.

#               LOGIK-PROJEKT is free software.

#               You can redistribute it and/or modify it under the terms
#               of the GNU General Public License as published by the
#               Free Software Foundation, either version 3 of the License,
#               or any later version.

#               This program is distributed in the hope that it will be
#               useful, but WITHOUT ANY WARRANTY; without even the
#               implied warranty of MERCHANTABILITY or
#               FITNESS FOR A PARTICULAR PURPOSE.

#               See the GNU General Public License for more details.
#               You should have received a copy of the GNU General
#               Public License along with this program.

#               If not, see <https://www.gnu.org/licenses/gpl-3.0.en.html>.

#               Contact: phil_man@mac.com

# -------------------------------------------------------------------------- #
# C2 A9 32 30 32 35 53 54 52 45 4E 47 54 48 2D 49 4E 2D 4E 55 4D 42 45 52 53 #
# -------------------------------------------------------------------------- #
# Changelog:
# -------------------------------------------------------------------------- #
