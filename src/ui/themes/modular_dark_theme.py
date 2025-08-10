#!/usr/bin/env python3
# -------------------------------------------------------------------------- #
# Filename:     modular_dark_theme.py
# Purpose:      Provides a modular dark theme for the application.
# Description:  Defines the visual style and color scheme for the UI using QSS.

# Author:       phil_man@mac.com
# Copyright:    Copyright (c) 2025
# Disclaimer:   Disclaimer at bottom of script.
# License:      GNU General Public License v3.0 (GPL-3.0).
#               https://www.gnu.org/licenses/gpl-3.0.en.html

# Version:      2026.1.0
# Status:       Production
# Type:         Module
# Created:      2025-07-01
# Modified:     2025-08-03

# Changelog:    Changelog at bottom of script.
# -------------------------------------------------------------------------- #


class ThemeConfiguration:
    """
    Central configuration for the dark theme
    """

    @staticmethod
    def get_config():
        return {
            "colors": {
                "background_color": "#242424",
                "foreground_color_white": "#ffffff",
                "foreground_color_light_grey": "#cccccc",
                "primary_select_color": "#664e00",
                "entry_background": "#3a3f4f",
                "button_background": "#4a4a4a",
                "border_color": "#555555",
                "disabled_background_color": "#2a2a2a",
                "disabled_foreground_color": "#999999",
                "combobox_arrow_bg": "#4a4a4a",
                "combobox_arrow_fg": "#555555",
                "combobox_arrow_active_bg": "#ffffff",
                "combobox_arrow_active_fg": "#88ff00",
                "export_button_color": "#4D0000", # Reddish-brown
                "export_button_hover": "#610000",
                "export_button_pressed": "#3A0000",
                "create_projekt_button_color": "#2F5F00", # Green
                "create_projekt_button_hover": "#3B7A00",
                "create_projekt_button_pressed": "#224700",

                "export_template_normal": "#4d0000",
                "export_template_hover": "#800000",
                "export_template_pressed": "#e60000",
                "export_template_disabled": "#1a0000",

                "import_template_normal": "#4d2600",
                "import_template_hover": "#804000",
                "import_template_pressed": "#e67300",
                "import_template_disabled": "#1a0d00",

                "create_projekt_normal": "#134d00",
                "create_projekt_hover": "#208000",
                "create_projekt_pressed": "#39e600",
                "create_projekt_disabled": "#061a00",
            },
            "fonts": {
                "default_font_family": "Discreet",
                "default_font_size": "11pt",
                "label_font_weight": "bold",
                "button_font_weight": "bold",
            },
            "widgets": {
                "default_borderwidth": "1px",
                "default_relief": "flat", # Not directly translatable to QSS border-style
                "entry_border_width": "1px",
                "entry_relief": "solid", # Not directly translatable to QSS border-style
                "button_focusthickness": "2px",
                "button_focuscolor": "#cc9c00",
                "button_relief": "raised", # Not directly translatable to QSS border-style
                "text_widget_borderwidth": "1px",
                "text_widget_relief": "solid", # Not directly translatable to QSS border-style
                "default_text_padding": "4px 2px", # QSS padding: top/bottom left/right
            },
        }


from src.ui import ui_config

class LogikProjektModularTheme:
    """Main theme class that orchestrates all widget styles using QSS"""

    @staticmethod
    def _lighten_color(hex_color, percent):
        """Lightens a hex color by a given percentage."""
        hex_color = hex_color.lstrip('#')
        rgb = tuple(int(hex_color[i:i+2], 16) for i in (0, 2, 4))
      
        lightened_rgb = [min(255, int(c * (1 + percent / 100.0))) for c in rgb]
      
        return '#%02x%02x%02x' % tuple(lightened_rgb)

    @staticmethod
    def get_stylesheet():
        config = ThemeConfiguration.get_config()
        colors = config["colors"]
        fonts = config["fonts"]
        widgets = config["widgets"]

        qss = f"""
            QWidget {{
                background-color: {colors["background_color"]};
                color: {colors["foreground_color_white"]};
                font-family: {fonts["default_font_family"]};
                font-size: {fonts["default_font_size"]};
            }}

            /* QLabel */
            QLabel {{
                color: {colors["foreground_color_light_grey"]};
            }}

            /* QLineEdit */
            QLineEdit {{
                background-color: {colors["entry_background"]};
                border: {widgets["entry_border_width"]} solid {colors["border_color"]};
                padding: 4px; /* Consistent padding */
                height: {ui_config.ENTRY_HEIGHT}px;
            }}
            QLineEdit:hover {{
                background-color: {LogikProjektModularTheme._lighten_color(colors["entry_background"], 10)};
            }}
            QLineEdit:focus {{
                background-color: {LogikProjektModularTheme._lighten_color(colors["entry_background"], 15)};
                border: {widgets["entry_border_width"]} solid {widgets["button_focuscolor"]};
            }}

            /* QPushButton */
            QPushButton {{
                background-color: {colors["button_background"]};
                border: {widgets["default_borderwidth"]} solid {colors["border_color"]};
                font-weight: {fonts["button_font_weight"]};
                padding: 5px 10px;
                height: {ui_config.BUTTON_HEIGHT}px;
            }}
            QPushButton:hover {{
                background-color: #5a5a5a; /* Slightly lighter on hover */
            }}
            QPushButton:pressed {{
                background-color: #3a3a3a; /* Darker when pressed */
            }}
            QPushButton:focus {{
                border: {widgets["button_focusthickness"]} solid {widgets["button_focuscolor"]};
            }}

            /* Specific Button Styles */
            QPushButton#exportButton {{
                background-color: {colors["export_button_color"]};
            }}
            QPushButton#exportButton:hover {{
                background-color: {colors["export_button_hover"]};
            }}
            QPushButton#exportButton:pressed {{
                background-color: {colors["export_button_pressed"]};
            }}

            /* Export Template Button */
            QPushButton#exportTemplateButton {{
                background-color: {colors["export_template_normal"]};
            }}
            QPushButton#exportTemplateButton:hover {{
                background-color: {colors["export_template_hover"]};
            }}
            QPushButton#exportTemplateButton:pressed {{
                background-color: {colors["export_template_pressed"]};
            }}
            QPushButton#exportTemplateButton:disabled {{
                background-color: {colors["export_template_disabled"]};
            }}

            /* Import Template Button */
            QPushButton#importTemplateButton {{
                background-color: {colors["import_template_normal"]};
            }}
            QPushButton#importTemplateButton:hover {{
                background-color: {colors["import_template_hover"]};
            }}
            QPushButton#importTemplateButton:pressed {{
                background-color: {colors["import_template_pressed"]};
            }}
            QPushButton#importTemplateButton:disabled {{
                background-color: {colors["import_template_disabled"]};
            }}

            /* Create Projekt Button */
            QPushButton#createProjektButton {{
                background-color: {colors["create_projekt_normal"]};
            }}
            QPushButton#createProjektButton:hover {{
                background-color: {colors["create_projekt_hover"]};
            }}
            QPushButton#createProjektButton:pressed {{
                background-color: {colors["create_projekt_pressed"]};
            }}
            QPushButton#createProjektButton:disabled {{
                background-color: {colors["create_projekt_disabled"]};
            }}

            /* Flame Directory Buttons */
            QPushButton#flameHomeDirButton,
            QPushButton#flameSetupsDirButton,
            QPushButton#flameMediaDirButton,
            QPushButton#flameCatalogDirButton {{
                background-color: {colors["entry_background"]};
                font-family: "Discreet";
                font-size: 11pt;
                font-weight: normal;
                text-align: left;
                padding-left: 5px;
            }}
            QPushButton#flameHomeDirButton:hover,
            QPushButton#flameSetupsDirButton:hover,
            QPushButton#flameMediaDirButton:hover,
            QPushButton#flameCatalogDirButton:hover {{
                background-color: {LogikProjektModularTheme._lighten_color(colors["entry_background"], 10)};
            }}
            QPushButton#flameHomeDirButton:pressed,
            QPushButton#flameSetupsDirButton:pressed,
            QPushButton#flameMediaDirButton:pressed,
            QPushButton#flameCatalogDirButton:pressed {{
                background-color: {LogikProjektModularTheme._lighten_color(colors["entry_background"], 25)};
            }}

            /* QComboBox */
            QComboBox {{
                background-color: {colors["entry_background"]};
                border: {widgets["default_borderwidth"]} solid {colors["border_color"]};
                padding: 4px; /* Consistent padding */
                height: {ui_config.COMBOBOX_HEIGHT}px;
            }}
            QComboBox:hover {{
                background-color: {LogikProjektModularTheme._lighten_color(colors["entry_background"], 10)};
            }}
            QComboBox:focus {{
                background-color: {LogikProjektModularTheme._lighten_color(colors["entry_background"], 15)};
                border: {widgets["default_borderwidth"]} solid {widgets["button_focuscolor"]};
            }}
            QComboBox::drop-down {{
                subcontrol-origin: padding;
                subcontrol-position: top right;
                width: 20px;
                border-left-width: 1px;
                border-left-color: {colors["border_color"]};
                border-left-style: solid;
                border-top-right-radius: 3px;
                border-bottom-right-radius: 3px;
                background-color: {colors["combobox_arrow_bg"]};
            }}
            QComboBox::drop-down:hover {{
                background-color: {LogikProjektModularTheme._lighten_color(colors["combobox_arrow_bg"], 15)};
            }}
            QComboBox QAbstractItemView {{
                border: 1px solid {colors["border_color"]};
                selection-background-color: {colors["primary_select_color"]};
                background-color: {colors["entry_background"]};
                color: {colors["foreground_color_white"]};
                outline: none;
                padding: 2px;
            }}
            QComboBox QAbstractItemView::item {{
                padding: 4px;
                border: none;
                background-color: transparent;
            }}
            QComboBox QAbstractItemView::item:selected {{
                background-color: {LogikProjektModularTheme._lighten_color(colors["primary_select_color"], 60)};
                color: {colors["foreground_color_white"]};
                border: 2px solid #ff6600; /* Bright orange outline */
            }}
            QComboBox QAbstractItemView::item:hover {{
                background-color: {LogikProjektModularTheme._lighten_color(colors["primary_select_color"], 40)};
                color: {colors["foreground_color_white"]};
                border: 2px solid #33cc00; /* Bright green outline */
            }}

            /* QScrollArea and QScrollBar */
            QScrollArea {{
                border: none;
            }}

            /* Panel Style */
            QWidget[class="panel"] {{
                border: 1px solid #555555;
            }}
          
            /* TemplateSummaryPanel specific styling */
            QWidget#TemplateSummaryPanel {{
                background-color: {colors["entry_background"]};
                border: {widgets["default_borderwidth"]} solid {colors["foreground_color_white"]};
                padding: 5px; /* Small inset */
            }}
            QScrollBar:vertical {{
                border: {widgets["default_borderwidth"]} solid {colors["border_color"]};
                background: {colors["entry_background"]};
                width: 10px;
                margin: 0px 0px 0px 0px;
            }}
            QScrollBar::handle:vertical {{
                background: {colors["button_background"]};
                min-height: 20px;
            }}
            QScrollBar::add-line:vertical, QScrollBar::sub-line:vertical {{
                background: none;
            }}
            QScrollBar::up-arrow:vertical, QScrollBar::down-arrow:vertical {{
                background: none;
            }}
            QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical {{
                background: none;
            }}
        """
        return qss


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
