#!/usr/bin/env python3
# -------------------------------------------------------------------------- #
# Filename:     app.py
# Purpose:      Main entry point for the LOGIK-PROJEKT application.
# Description:  Initializes and runs the PySide6 GUI application.

# Author:       phil_man@mac.com
# Copyright:    Copyright (c) 2025
# Disclaimer:   Disclaimer at bottom of script.
# License:      GNU General Public License v3.0 (GPL-3.0).
#               https://www.gnu.org/licenses/gpl-3.0.en.html

# Version:      2026.1.0
# Status:       Development
# Type:         Application
# Created:      2025-07-01
# Modified:     2025-08-04

# Changelog:    Changelog at bottom of script.
# -------------------------------------------------------------------------- #
import sys
import logging
import os
from datetime import (
    datetime
)
from PySide6.QtWidgets import (
    QApplication
)
from src.ui.app_window import (
    AppWindow
)
from src.ui.themes.modular_dark_theme import (
    LogikProjektModularTheme
)
from src.ui import (
    ui_config
)


def main():
    # Configure root logger for console output
    logging.basicConfig(
        level=logging.DEBUG,
        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
    )

    # Generate session log file path
    log_dir_base = (
        "logs/"
        "session-logs"
    )
    current_time = (
        datetime.now()
    )
    year = (
        current_time.strftime("%Y")
    )
    month = (
        current_time.strftime("%m")
    )
    day = (
        current_time.strftime("%d")
    )
    log_dir = (
        os.path.join(log_dir_base, year, month, day)
    )
    os.makedirs(
        log_dir,
        exist_ok=True
    )
    log_filename = (
        current_time.strftime("%Y-%m-%d-%H-%M-%S-session.log")
    )
    session_log_filepath = (
        os.path.join(log_dir, log_filename)
    )

    # Add a FileHandler to the root logger
    file_handler = (
        logging.FileHandler(session_log_filepath)
    )
    file_handler.setLevel(logging.DEBUG)
    formatter = (
        logging.Formatter(
            '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
        )
    )
    file_handler.setFormatter(formatter)
    logging.getLogger().addHandler(file_handler)

    app = (
        QApplication(sys.argv)
    )
    app.setStyleSheet(
        LogikProjektModularTheme.get_stylesheet()
    )

    main_window = AppWindow()
    main_window.setWindowTitle(
        "LOGIK-PROJEKT 2026.1"
    )

    # Center the window on the screen
    screen = (
        app.primaryScreen()
    )

    if screen:
        screen_geometry = (
            screen.geometry()
        )

        x = (
            screen_geometry.width() - ui_config.WINDOW_WIDTH
        ) / 2
        y = (
            screen_geometry.height() - ui_config.WINDOW_HEIGHT
        ) / 2

        main_window.setGeometry(
            int(x),
            int(y),
            ui_config.WINDOW_WIDTH,
            ui_config.WINDOW_HEIGHT
        )
    else:
        main_window.setGeometry(
            100,
            100,
            ui_config.WINDOW_WIDTH,
            ui_config.WINDOW_HEIGHT
        )

    main_window.show()
    sys.exit(app.exec())


if __name__ == "__main__":
    main()


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
