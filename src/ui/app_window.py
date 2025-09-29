#!/usr/bin/env python3
# -------------------------------------------------------------------------- #
# Filename:     app_window.py
# Purpose:      Main application window for LOGIK-PROJEKT.
# Description:  This file defines the main GUI window, including its layout,
#               panels, and the logic for handling user interactions and
#               background tasks.

# Author:       phil_man@mac.com
# Copyright:    Copyright (c) 2025
# Disclaimer:   Disclaimer at bottom of script.
# License:      GNU General Public License v3.0 (GPL-3.0).
#               https://www.gnu.org/licenses/gpl-3.0.en.html

# Version:      2026.1.0
# Status:       Production
# Type:         Application
# Created:      2025-07-01
# Modified:     2025-08-03

# Changelog:    Changelog at bottom of script.
# -------------------------------------------------------------------------- #

from PySide6.QtCore import (
    QThread,
    QObject,
    Signal,
    Slot
)

from PySide6.QtWidgets import (
    QWidget,
    QMainWindow,
    QVBoxLayout,
    QHBoxLayout,
    QFileDialog,
    QMessageBox
)

from src.ui import (
    ui_config
)
from src.ui.panels.template_info_panel import (
    TemplateInfoPanel
)
from src.ui.panels.template_parameters_panel import (
    TemplateParametersPanel
)
from src.ui.panels.template_summary_panel import (
    TemplateSummaryPanel
)
from src.ui.panels.projekt_template_panel import (
    ProjektTemplatePanel
)
from src.ui.panels.flame_options_panel import (
    FlameOptionsPanel
)
from src.ui.panels.projekt_summary_panel import (
    ProjektSummaryPanel
)
from src.core.app_logic import (
    AppLogic
)
from src.core.projekt_manager.projekt_creator import (
    create_projekt
)
from src.core.template_manager.template_models import (
    TemplateInfo,
    TemplateParameters
)
from src.core.utils import (
    ocio_utils
)
from src.core.utils.threaded_logging_utils import (
    SignalHandler
)
import logging
import os
import shutil

import src.core.utils.validation_utils as validation_utils


class Worker(QObject):
    finished = Signal()
    error = Signal(str)
    template_imported = Signal(dict, dict)
    template_exported = Signal(str, str)

    def __init__(self, app_logic):
        super().__init__()
        self.app_logic = app_logic

    @Slot(dict)
    def create_projekt(self, projekt_summary_data):
        try:
            create_projekt(projekt_summary_data)

            logging.info("Create PROJEKT triggered from AppWindow")
            logging.info("LOGIK-PROJEKT creation successful.")
        except Exception as e:
            self.error.emit(str(e))
        finally:
            self.finished.emit()

    @Slot(dict, dict, str)
    def export_template_json(
        self,
        template_info_data,
        template_params_data,
        user_chosen_path
    ):
        try:
            # First, save the current data to the session file
            export_message = self.app_logic.export_logik_projekt_template(
                template_info_data,
                template_params_data
            )
            logging.info(export_message)

            # Now that the session file is updated, copy it to the user's chosen path
            if user_chosen_path:
                source_file_path = "pref/session-preferences/current_session-template.json"
                shutil.copy(source_file_path, user_chosen_path)
                logging.info(f"Template also saved to: {user_chosen_path} (User-chosen path)")

            self.template_exported.emit(export_message, user_chosen_path)
        except Exception as e:
            self.error.emit(str(e))
        finally:
            self.finished.emit()

    @Slot(str)
    def import_template_json(self, file_path):
        try:
            (template_info,
             template_parameters,
             import_message) = (
                self.app_logic.import_logik_projekt_template(
                    file_path
                )
            )
            logging.info(import_message)
            self.template_imported.emit(
                template_info.__dict__, template_parameters.__dict__
            )
        except Exception as e:
            self.error.emit(str(e))
        finally:
            self.finished.emit()


class AppWindow(QMainWindow):
    create_projekt_requested = Signal(dict)
    export_template_requested = Signal(dict, dict, str)
    import_template_requested = Signal(str)

    def __init__(self):
        super().__init__()

        self.app_logic = AppLogic()

        logging.debug("AppWindow initialized.")

        central_widget = QWidget()
        self.setCentralWidget(central_widget)

        self.main_layout = QHBoxLayout(central_widget)
        self.main_layout.setContentsMargins(
            *ui_config.MAIN_LAYOUT_MARGINS
        )

        self.left_container = QWidget(self)
        self.left_container.setFixedWidth(
            ui_config.LEFT_CONTAINER_WIDTH
        )
        self.left_layout = QVBoxLayout(self.left_container)
        self.main_layout.addWidget(self.left_container)

        self.right_container = QWidget(self)
        self.right_container.setFixedWidth(
            ui_config.RIGHT_CONTAINER_WIDTH
        )
        self.right_layout = QVBoxLayout(self.right_container)
        self.main_layout.addWidget(self.right_container)

        self.template_info_panel = TemplateInfoPanel(self)
        self.template_info_panel.setProperty("class", "panel")
        self.template_info_panel.setFixedHeight(
            ui_config.TEMPLATE_INFO_PANEL_HEIGHT
        )

        self.template_parameters_panel = TemplateParametersPanel(
            self,
            app_logic=self.app_logic
        )
        self.template_parameters_panel.setProperty("class", "panel")
        self.template_parameters_panel.setFixedHeight(
            ui_config.TEMPLATE_PARAMETERS_PANEL_HEIGHT
        )

        default_params = self.app_logic.get_default_template_values()
        self.template_parameters_panel.set_template_parameters(
            default_params
        )

        self.template_summary_panel = TemplateSummaryPanel(self)
        self.template_summary_panel.setProperty("class", "panel")
        self.template_summary_panel.setFixedHeight(
            ui_config.TEMPLATE_SUMMARY_PANEL_HEIGHT
        )

        self.projekt_template_panel = ProjektTemplatePanel(self)
        self.projekt_template_panel.setProperty("class", "panel")
        self.projekt_template_panel.setFixedHeight(
            ui_config.PROJEKT_TEMPLATE_PANEL_HEIGHT
        )

        self.flame_options_panel = FlameOptionsPanel(
            self,
            default_params=default_params
        )
        self.flame_options_panel.setProperty("class", "panel")
        self.flame_options_panel.setFixedHeight(
            ui_config.FLAME_OPTIONS_PANEL_HEIGHT
        )

        self.projekt_summary_panel = ProjektSummaryPanel(self)
        self.projekt_summary_panel.setProperty("class", "panel")
        self.projekt_summary_panel.setFixedHeight(
            ui_config.PROJEKT_SUMMARY_PANEL_HEIGHT
        )

        self.left_layout.addWidget(self.template_info_panel)
        self.left_layout.addWidget(self.template_parameters_panel)
        self.left_layout.addWidget(self.template_summary_panel)

        self.right_layout.addWidget(self.projekt_template_panel)
        self.right_layout.addWidget(self.flame_options_panel)
        self.right_layout.addWidget(self.projekt_summary_panel)

        # Setup thread-safe logging
        from src.core.utils.threaded_logging_utils import LogEmitter
        self.log_emitter = LogEmitter()
        self.log_emitter.message_logged.connect(
            self.projekt_summary_panel.shell_output_text.append
        )
        self.log_handler = SignalHandler(self.log_emitter)
        logging.getLogger().addHandler(self.log_handler)
        logging.getLogger().setLevel(logging.DEBUG)

        self._update_all_summaries()

        self.template_summary_panel.export_button.button.clicked.connect(
            self._export_template_json
        )
        self.projekt_template_panel.import_button.button.clicked.connect(
            self._import_template_json
        )
        self.projekt_summary_panel.create_projekt_button.button.clicked.connect(
            self._create_projekt
        )

        self.flame_options_panel.path_changed.connect(
            self._update_all_summaries
        )

        # Connect TemplateInfoPanel's calculated_name_updated signal
        self.template_info_panel.calculated_name_updated.connect(
            self._update_all_summaries
        )

        self.template_parameters_panel.parameters_updated.connect(
            self._update_all_summaries
        )

        self.thread = QThread()
        self.worker = Worker(self.app_logic)
        self.worker.moveToThread(self.thread)
        self.worker.finished.connect(self.on_worker_finished)
        self.worker.error.connect(self.on_worker_error)

        self.worker.template_imported.connect(
            self.on_template_imported
        )
        self.worker.template_exported.connect(
            self.on_template_exported
        )

        self.create_projekt_requested.connect(
            self.worker.create_projekt
        )
        self.export_template_requested.connect(
            self.worker.export_template_json
        )
        self.import_template_requested.connect(
            self.worker.import_template_json
        )

        self.thread.start()

    def on_worker_finished(self):
        logging.info("Worker thread finished.")

    def on_worker_error(self, error_message):
        logging.error(
            f"An error occurred in the worker thread: {error_message}"
        )
        QMessageBox.critical(self, "Error", error_message)

    @Slot(str, str)
    def on_template_exported(self, export_message, user_chosen_path):
        display_message = f"Template automatically saved to: {export_message}\n\nTemplate also saved to: {user_chosen_path}"
        QMessageBox.information(self, "Export Template", display_message)

    @Slot(dict, dict)
    def on_template_imported(
        self,
        template_info,
        template_parameters
    ):
        self.template_info_panel.set_template_info(
            template_info
        )
        self.template_parameters_panel.set_template_parameters(
            template_parameters
        )
        self._update_all_summaries()

    def _update_all_summaries(self):
        template_info_data = self.template_info_panel.get_template_info()
        template_params_data = (
            self.template_parameters_panel.get_template_parameters()
        )
        combined_template_data = {
            **template_info_data,
            **template_params_data
        }
        self.template_summary_panel.set_template_summary_panel_data(
            combined_template_data
        )

        template_parameters_keys = [
            "template_resolution",
            "template_resolution_w",
            "template_resolution_h",
            "template_aspect_ratio",
            "template_bit_depth",
            "template_framerate",
            "template_scan_mode",
            "template_start_frame",
            "template_init_config",
            "template_ocio_config",
            "template_cache_integer",
            "template_cache_integer_id",
            "template_cache_float",
            "template_cache_float_id"
        ]

        filtered_template_params_data = {
            k: template_params_data[k]
            for k in template_parameters_keys
            if k in template_params_data
        }

        flame_options = (
            self.flame_options_panel.get_flame_options()
        )

        projekt_summary_data = (
            self.app_logic.get_projekt_summary_data(
                TemplateInfo(**template_info_data),
                TemplateParameters(**filtered_template_params_data),
                flame_options,
            )
        )

        full_flame_projekt_name = projekt_summary_data.get(
            "flame_projekt_name",
            ""
        )
        self.flame_options_panel.set_project_name(full_flame_projekt_name)

        self.projekt_summary_panel.set_projekt_summary_data(
            projekt_summary_data
        )

        self.projekt_template_panel.set_projekt_template_data({
            "projekt_serial_number": template_info_data.get(
                "template_serial_number"
            ),
            "projekt_client_name": template_info_data.get(
                "template_client_name"
            ),
            "projekt_campaign_name": template_info_data.get(
                "template_campaign_name"
            ),
            "projekt_calculated_name": template_info_data.get(
                "template_calculated_name"
            ),
            "projekt_description": template_info_data.get(
                "template_description"
            ),
            "projekt_resolution": template_params_data.get(
                "template_resolution"
            ),
            "projekt_resolution_w": template_params_data.get(
                "template_resolution_w"
            ),
            "projekt_resolution_h": template_params_data.get(
                "template_resolution_h"
            ),
            "projekt_aspect_ratio": template_params_data.get(
                "template_aspect_ratio"
            ),
            "projekt_bit_depth": template_params_data.get(
                "template_bit_depth"
            ),
            "projekt_framerate": template_params_data.get(
                "template_framerate"
            ),
            "projekt_scan_mode": template_params_data.get(
                "template_scan_mode"
            ),
            "projekt_start_frame": template_params_data.get(
                "template_start_frame"
            ),
            "projekt_init_config": template_params_data.get(
                "template_init_config"
            ),
            "projekt_ocio_name": projekt_summary_data.get(
                "flame_projekt_ocio_name"
            ),
            "projekt_cache_integer_id": template_params_data.get(
                "template_cache_integer_id"
            ),
            "projekt_cache_float_id": template_params_data.get(
                "template_cache_float_id"
            ),
        })

    def _export_template_json(self):
        logging.info(
            "Starting export of LOGIK-PROJEKT template."
        )

        template_info_data = self.template_info_panel.get_template_info()
        template_params_data = (
            self.template_parameters_panel.get_template_parameters()
        )

        try:
            # --- Validation Checks ---
            # 1. Validate Client and Campaign Names
            is_valid_names, name_message = (
                validation_utils.validate_client_campaign_names(
                    template_info_data.get("template_client_name", ""),
                    template_info_data.get("template_campaign_name", "")
                )
            )

            if not is_valid_names:
                QMessageBox.warning(
                    self,
                    "Validation Error",
                    name_message
                )
                logging.warning(
                    f"Template export validation failed: {name_message}"
                )
                return  # Stop export if names are invalid

            # 2. Validate Init Config
            is_valid_init_config, init_config_message = (
                validation_utils.validate_init_config(
                    template_params_data.get("template_init_config", ""),
                    template_params_data.get("template_resolution_w", ""),
                    template_params_data.get("template_resolution_h", ""),
                    template_params_data.get("template_framerate", "")
                )
            )

            if not is_valid_init_config:
                # If there's a message, it's a warning/question,
                # otherwise it's a critical error
                if init_config_message:
                    reply = QMessageBox.question(
                        self,
                        "Validation Warning",
                        init_config_message,
                        QMessageBox.Yes | QMessageBox.No
                    )

                    if reply == QMessageBox.No:
                        logging.warning(
                            "Template export cancelled by user "
                            "due to Init Config mismatch."
                        )
                        return  # Stop export if user chooses not to continue
                else:
                    QMessageBox.critical(
                        self,
                        "Validation Error",
                        "Init Config validation failed unexpectedly."
                    )
                    logging.error(
                        "Init Config validation failed unexpectedly "
                        "during template export."
                    )
                    return  # Stop export on critical validation error

            # --- End Validation Checks ---

            # --- End Validation Checks ---

            # Get the calculated name for the suggested filename
            logik_projekt_name = template_info_data.get("template_calculated_name", "untitled_template")

            # Define the source file path (the automatically generated template)
            source_file_path = "pref/session-preferences/current_session-template.json"

            # Define the default target directory (~/Documents/LOGIK-PROJEKT-exported-templates)
            documents_path = os.path.expanduser("~/")
            default_target_dir = os.path.join(documents_path, "Documents/LOGIK-PROJEKT-exported-templates")

            # Ensure the default target directory exists
            os.makedirs(default_target_dir, exist_ok=True)

            # Suggest a default filename
            suggested_file_name = f"{logik_projekt_name}.json"
            default_save_path = os.path.join(default_target_dir, suggested_file_name)

            # Open file dialog for user to choose save location
            file_dialog = QFileDialog(self)
            file_dialog.setFileMode(QFileDialog.AnyFile)
            file_dialog.setAcceptMode(QFileDialog.AcceptSave)
            file_dialog.setNameFilter("JSON files (*.json)")
            file_dialog.setWindowTitle("Save Template As")
            file_dialog.setDirectory(default_target_dir)
            file_dialog.selectFile(suggested_file_name)
            file_dialog.resize(1200, file_dialog.height()) # Set width to 1200 pixels

            save_file_path = None
            if file_dialog.exec():
                save_file_path = file_dialog.selectedFiles()[0]

            if save_file_path: # If user didn't cancel the dialog
                # The worker will handle the file copy
                pass

            self.export_template_requested.emit(
                template_info_data,
                template_params_data,
                save_file_path # Pass the user-chosen path
            )

        except Exception as e:
            logging.error(
                f"Error during template export: {e}"
            )
            QMessageBox.critical(
                self,
                "Export Error",
                f"Failed to export template: {e}"
            )
        finally:
            logging.info(
                "Finished export of LOGIK-PROJEKT template."
            )

    def _import_template_json(self):
        logging.info("Starting import of LOGIK-PROJEKT template.")
        file_path, _ = QFileDialog.getOpenFileName(
            self,
            "Import Template From",
            "",
            "JSON files (*.json)"
        )
        if file_path:
            self.import_template_requested.emit(file_path)

    def _create_projekt(self):
        logging.info("Starting LOGIK-PROJECKT creation.")
        if self.projekt_summary_panel.run_validation():
            reply = QMessageBox.question(
                self,
                "Launch Flame",
                "Do you wish to launch Flame after projekt creation?",
                QMessageBox.Yes | QMessageBox.No,
                QMessageBox.No,
            )
            launch_flame = reply == QMessageBox.Yes

            template_info_data = (
                self.template_info_panel.get_template_info()
            )
            template_params_data = (
                self.template_parameters_panel.get_template_parameters()
            )
            flame_options = (
                self.flame_options_panel.get_flame_options()
            )
            projekt_summary_data = (
                self.app_logic.get_projekt_summary_data(
                    TemplateInfo(**template_info_data),
                    TemplateParameters(**template_params_data),
                    flame_options
                )
            )
            projekt_summary_data["launch_flame_after_creation"] = launch_flame
            self.create_projekt_requested.emit(projekt_summary_data)
        else:
            logging.warning(
                "LOGIK-PROJEKT creation aborted due to validation failure."
            )

    def closeEvent(self, event):
        """
        Handles the window close event to ensure the worker thread is
        properly terminated.
        """
        logging.info("Close event triggered. Shutting down worker thread...")

        if self.thread.isRunning():
            self.thread.quit()
            # Wait for the thread to finish. Give it a reasonable timeout.
            if not self.thread.wait(5000):  # 5 seconds
                logging.warning("Worker thread did not quit in time. Terminating...")
                self.thread.terminate()
                self.thread.wait()  # Wait for termination to complete

        logging.info("Worker thread stopped. Accepting close event.")
        event.accept()


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
