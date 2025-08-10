#!/usr/bin/env python3
# -------------------------------------------------------------------------- #
# File:         logik_projekt_dark_theme.py
# Version:      0.0.0
# Purpose:      Dark theme configuration for LOGIK-PROJEKT GUI
# Author:       phil_man@mac.com
# Creation:     2025-07-04
# Modification: 2025-07-04
# Changelist:   changes are listed at the foot of this document
# -------------------------------------------------------------------------- #

from tkinter import ttk


class LogikProjektDarkTheme:
    @staticmethod
    def configure_root(root):
        root.tk_setPalette(
            background="#242424",
            foreground="#ffffff",
            activeBackground="#4a4a4a",
            activeForeground="#ffffff",
        )

        root.option_add("*Font", ("Discreet", 11))

    @staticmethod
    def get_settings():
        return {
            "background_color": "#242424",
            "foreground_color_white": "#ffffff",
            "foreground_color_light_grey": "#cccccc",
            "primary_select_color": "#cc9c00",
            "entry_background": "#3a3f4f",
            "button_background": "#4a4a4a",
            "border_color": "#555555",
            "disabled_background_color": "#2a2a2a",
            "disabled_foreground_color": "#999999",
            "default_font": (
                "Discreet",
                11,
            ),
            "label_font": (
                "Discreet",
                11,
                "bold",
            ),
            "button_font": (
                "Discreet",
                11,
                "bold",
            ),
            "default_borderwidth": 1,
            "default_relief": "flat",
            "entry_border_width": 1,
            "entry_relief": "solid",
            "button_focusthickness": 2,
            "button_focuscolor": "#cc9c00",
            "button_relief": "raised",
            "text_widget_borderwidth": 1,
            "text_widget_relief": "solid",
            "combobox_arrow_bg": "#4a4a4a",
            "combobox_arrow_fg": "#555555",
            "combobox_arrow_active_bg": "#ffffff",
            "combobox_arrow_active_fg": "#88ff00",
        }

    @staticmethod
    def configure_ttk_style(
        root,
        custom_settings=None
    ):
        style = ttk.Style(root)

        style.theme_use(
            "clam"
        )

        settings = LogikProjektDarkTheme.get_settings()

        if custom_settings:
            settings.update(
                custom_settings
            )

        root.tk_setPalette(
            background=settings["background_color"],
            foreground=settings["foreground_color_white"],
            activeBackground=settings["button_background"],
            activeForeground=settings["foreground_color_white"],
        )
        root.option_add(
            "*Font",
            settings["default_font"]
        )

        style.configure(
            ".",
            background=settings["background_color"],
            foreground=settings["foreground_color_white"],
            font=settings["default_font"],
        )

        style.configure(
            "TFrame",
            background=settings["background_color"]
        )
        style.configure(
            "TLabelframe",
            background=settings["background_color"],
            foreground=settings["foreground_color_light_grey"],
            relief=settings["default_relief"],
            borderwidth=settings["default_borderwidth"],
        )
        style.configure(
            "TLabelframe.Label",
            background=settings["background_color"],
            foreground=settings["foreground_color_light_grey"],
            font=settings["label_font"],
        )

        style.configure(
            "TLabel",
            background=settings["background_color"],
            foreground=settings["foreground_color_light_grey"],
            font=settings["default_font"],
        )

        style.configure(
            "TEntry",
            fieldbackground=settings["entry_background"],
            foreground=settings["foreground_color_white"],
            insertcolor=settings["foreground_color_white"],
            bordercolor=settings["border_color"],
            darkcolor=settings["entry_background"],
            lightcolor=settings["entry_background"],
            selectbackground=settings["primary_select_color"],
            selectforeground=settings["foreground_color_white"],
            font=settings["default_font"],
            borderwidth=settings["entry_border_width"],
            relief=settings["entry_relief"],
        )

        style.map(
            "TEntry",
            foreground=[
                (
                    "!disabled",
                    settings["foreground_color_white"],
                ),
                (
                    "readonly",
                    settings["foreground_color_white"],
                ),
                (
                    "focus",
                    settings["foreground_color_white"],
                ),
                (
                    "active",
                    settings["foreground_color_white"],
                ),
                (
                    "disabled",
                    settings["disabled_foreground_color"],
                ),
            ],
            fieldbackground=[
                (
                    "disabled",
                    settings["disabled_background_color"],
                ),
            ],
        )

        style.configure(
            "TText",
            background=settings["entry_background"],
            foreground=settings["foreground_color_white"],
            insertbackground=settings["foreground_color_white"],
            selectbackground=settings["primary_select_color"],
            selectforeground=settings["foreground_color_white"],
            borderwidth=settings["text_widget_borderwidth"],
            relief=settings["text_widget_relief"],
            font=settings["default_font"],
        )

        style.configure(
            "TButton",
            background=settings["button_background"],
            foreground=settings["foreground_color_white"],
            font=settings["button_font"],
            borderwidth=settings["default_borderwidth"],
            focusthickness=settings["button_focusthickness"],
            focuscolor=settings["button_focuscolor"],
            relief=settings["button_relief"],
            padding=[
                5,
                1,
            ],
        )
        style.map(
            "TButton",
            background=[
                (
                    "active",
                    "#00008B",
                ),
                (
                    "pressed",
                    "#3a3a3a",
                ),
            ],
            foreground=[
                (
                    "active",
                    settings["foreground_color_white"],
                ),
                (
                    "pressed",
                    settings["foreground_color_white"],
                ),
            ],
        )

        style.configure(
            "FlameProjekt.TButton",
            background=settings["entry_background"],
            foreground=settings["foreground_color_white"],
            font=settings["default_font"],
            anchor="w",
            relief=settings["entry_relief"],
            borderwidth=settings["entry_border_width"],
            padding=[
                5,
                1,
            ],
        )
        style.map(
            "FlameProjekt.TButton",
            background=[
                (
                    "active",
                    "#00008B",
                ),
                (
                    "pressed",
                    "#000055",
                ),
            ],
            foreground=[
                (
                    "active",
                    settings["foreground_color_white"],
                ),
                (
                    "pressed",
                    settings["foreground_color_white"],
                ),
            ],
        )

        style.configure(
            "Export.TButton",
            font=settings["button_font"],
            foreground=settings["foreground_color_white"],
        )
        style.map(
            "Export.TButton",
            background=[
                (
                    "active",
                    "#8B0000",
                ),
                (
                    "pressed",
                    "#550000",
                ),
            ],
            foreground=[
                (
                    "active",
                    "#FFFFFF",
                ),
                (
                    "pressed",
                    "#FFFFFF",
                ),
            ],
        )

        style.configure(
            "ImportTemplate.TButton",
            font=settings["button_font"],
            foreground=settings["foreground_color_white"],
        )
        style.map(
            "ImportTemplate.TButton",
            background=[
                (
                    "active",
                    "#FF8C00",
                ),
                (
                    "pressed",
                    "#CC7000",
                ),
            ],
            foreground=[
                (
                    "active",
                    "#FFFFFF",
                ),
                (
                    "pressed",
                    "#FFFFFF",
                ),
            ],
        )

        style.configure(
            "CreateProjekt.TButton",
            font=settings["button_font"],
            foreground=settings["foreground_color_white"],
        )
        style.map(
            "CreateProjekt.TButton",
            background=[
                (
                    "active",
                    "#006400",
                ),
                (
                    "pressed",
                    "#004d00",
                ),
            ],
            foreground=[
                (
                    "active",
                    "#FFFFFF",
                ),
                (
                    "pressed",
                    "#FFFFFF",
                ),
            ],
        )

        style.configure(
            "CreateCustomDir.TButton",
            font=settings["button_font"],
            foreground=settings["foreground_color_white"],
        )
        style.map(
            "CreateCustomDir.TButton",
            background=[
                (
                    "active",
                    "#006400",
                ),
                (
                    "pressed",
                    "#004d00",
                ),
            ],
            foreground=[
                (
                    "active",
                    "#FFFFFF",
                ),
                (
                    "pressed",
                    "#FFFFFF",
                ),
            ],
        )

        style.configure(
            "TCombobox",
            fieldbackground=settings["entry_background"],
            background=settings["button_background"],
            foreground=settings["foreground_color_white"],
            selectbackground=settings["primary_select_color"],
            selectforeground=settings["foreground_color_white"],
            arrowcolor=settings["border_color"],
            bordercolor=settings["border_color"],
            darkcolor=settings["border_color"],
            lightcolor=settings["border_color"],
            relief=settings["entry_relief"],
            font=settings["default_font"],
        )

        style.configure(
            "TCombobox.Listbox",
            font=settings["default_font"],
            background=settings["entry_background"],
            foreground=settings["foreground_color_white"],
            selectbackground=settings["primary_select_color"],
            selectforeground=settings["foreground_color_white"],
            borderwidth=settings["default_borderwidth"],
        )

        style.map(
            "TCombobox",
            background=[
                (
                    "readonly",
                    settings["button_background"],
                ),
            ],
            fieldbackground=[
                (
                    "readonly",
                    settings["entry_background"],
                ),
            ],
            foreground=[
                (
                    "readonly",
                    settings["foreground_color_white"],
                ),
            ],
            selectbackground=[
                (
                    "!disabled",
                    settings["primary_select_color"],
                ),
            ],
            selectforeground=[
                (
                    "!disabled",
                    settings["foreground_color_white"],
                ),
            ],
            font=[
                (
                    "!disabled",
                    settings["default_font"],
                ),
                (
                    "readonly",
                    settings["default_font"],
                ),
            ],
        )

        style.configure(
            "TCombobox.Downarrow",
            background=settings["combobox_arrow_bg"],
            foreground=settings["combobox_arrow_fg"],
            relief="flat",
        )
        style.map(
            "TCombobox.Downarrow",
            background=[
                (
                    "active",
                    settings["combobox_arrow_active_bg"],
                ),
                (
                    "pressed",
                    settings["combobox_arrow_active_bg"],
                ),
            ],
            foreground=[
                (
                    "active",
                    settings["combobox_arrow_active_fg"],
                ),
                (
                    "pressed",
                    settings["combobox_arrow_active_fg"],
                ),
            ],
        )

        root.option_add("*TCombobox*Listbox.Font", settings["default_font"])
        root.option_add(
            "*TCombobox*Listbox.Background",
            settings["entry_background"],
        )
        root.option_add(
            "*TCombobox*Listbox.Foreground",
            settings["foreground_color_white"],
        )
        root.option_add(
            "*TCombobox*Listbox.selectBackground",
            settings["primary_select_color"],
        )
        root.option_add(
            "*TCombobox*Listbox.selectForeground",
            settings["foreground_color_white"],
        )

        style.configure(
            "Vertical.TScrollbar",
            background=settings["button_background"],
            troughcolor=settings["entry_background"],
            bordercolor=settings["border_color"],
            arrowcolor=settings["border_color"],
        )
        style.map(
            "Vertical.TScrollbar",
            background=[
                (
                    "active",
                    "#5a5a5a",
                ),
            ],
        )


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
