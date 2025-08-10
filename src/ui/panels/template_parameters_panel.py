#!/usr/bin/env python3
# -------------------------------------------------------------------------- #
# Filename:     template_parameters_panel.py
# Purpose:      Panel for configuring template parameters.
# Description:  This panel provides various widgets for setting template-specific
#               parameters such as resolution, bit depth, frame rate, and OCIO config.

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

from PySide6.QtWidgets import QWidget, QGridLayout
from PySide6.QtCore import Signal

from src.ui import ui_config
from src.core.utils import ocio_utils

from src.ui.widgets.combobox.resolution_widget import ResolutionWidget
from src.ui.widgets.combobox.bit_depth_widget import BitDepthWidget
from src.ui.widgets.combobox.frame_rate_widget import FrameRateWidget
from src.ui.widgets.combobox.scan_mode_widget import ScanModeWidget
from src.ui.widgets.combobox.start_frame_widget import StartFrameWidget
from src.ui.widgets.combobox.init_config_widget import InitConfigWidget
from src.ui.widgets.combobox.ocio_config_widget import OcioConfigWidget
from src.ui.widgets.combobox.cache_integer_widget import CacheIntegerWidget
from src.ui.widgets.combobox.cache_float_widget import CacheFloatWidget

from src.ui.widgets.entry.resolution_width_widget import ResolutionWidthWidget
from src.ui.widgets.entry.resolution_height_widget import ResolutionHeightWidget
from src.ui.widgets.entry.aspect_ratio_widget import AspectRatioWidget

from src.core.functions.get.get_resolution_values import get_resolution_values
from src.core.functions.get.get_bit_depth_values import get_bit_depth_values
from src.core.functions.get.get_frame_rate_values import get_frame_rate_values
from src.core.functions.get.get_scan_mode_values import get_scan_mode_values
from src.core.functions.get.get_start_frame_values import get_start_frame_values
from src.core.functions.get.get_init_config_values import get_init_config_values
from src.core.functions.get.get_ocio_config_values import get_ocio_config_values
from src.core.functions.get.get_cache_integers_values import get_cache_integer_values
from src.core.functions.get.get_cache_float_values import get_cache_float_values


class TemplateParametersPanel(QWidget):
    parameters_updated = Signal()
    def __init__(self, master=None, app_logic=None):
        super().__init__(master)

        self.app_logic = app_logic
        self.layout = QGridLayout(self)
        self.layout.setSpacing(ui_config.PANEL_LAYOUT_SPACING)
        self.layout.setContentsMargins(*ui_config.PANEL_PADDING)

        # Create widgets
        self.resolution_widget = ResolutionWidget(self)
        self.resolution_width_widget = ResolutionWidthWidget(self)
        self.resolution_height_widget = ResolutionHeightWidget(self)
        self.aspect_ratio_widget = AspectRatioWidget(self)
        self.bit_depth_widget = BitDepthWidget(self)
        self.frame_rate_widget = FrameRateWidget(self)
        self.scan_mode_widget = ScanModeWidget(self)
        self.start_frame_widget = StartFrameWidget(self)
        self.init_config_widget = InitConfigWidget(self)
        self.ocio_config_widget = OcioConfigWidget(self)
        self.cache_integer_widget = CacheIntegerWidget(self)
        self.cache_float_widget = CacheFloatWidget(self)

        self.layout.setColumnMinimumWidth(0, 160)  # Label column
        self.layout.setColumnStretch(1, 1)  # Widget column takes remaining space

        # Add widgets to layout
        row = 0
        for widget in [
            (self.resolution_widget.label, self.resolution_widget.combobox),
            (self.resolution_width_widget.label, self.resolution_width_widget.entry),
            (self.resolution_height_widget.label, self.resolution_height_widget.entry),
            (self.aspect_ratio_widget.label, self.aspect_ratio_widget.entry),
            (self.bit_depth_widget.label, self.bit_depth_widget.combobox),
            (self.frame_rate_widget.label, self.frame_rate_widget.combobox),
            (self.scan_mode_widget.label, self.scan_mode_widget.combobox),
            (self.start_frame_widget.label, self.start_frame_widget.combobox),
            (self.init_config_widget.label, self.init_config_widget.combobox),
            (self.ocio_config_widget.label, self.ocio_config_widget.combobox),
            (self.cache_integer_widget.label, self.cache_integer_widget.combobox),
            (self.cache_float_widget.label, self.cache_float_widget.combobox),
        ]:
            self.layout.addWidget(widget[0], row, 0)
            self.layout.addWidget(widget[1], row, 1)
            row += 1

        self.cache_integer_id = None
        self.cache_float_id = None

        # Dummy data for comboboxes
        self.resolution_widget.set_values(
            get_resolution_values()
        )
        self.bit_depth_widget.set_values(
            get_bit_depth_values()
        )
        self.frame_rate_widget.set_values(
            get_frame_rate_values()
        )
        self.scan_mode_widget.set_values(
            get_scan_mode_values()
        )
        self.start_frame_widget.set_values(
            get_start_frame_values()
        )
        self.init_config_widget.set_values(
            get_init_config_values()
        )
        self.ocio_config_widget.set_values(
            get_ocio_config_values()
        )
        self.cache_integer_widget.set_values(
            get_cache_integer_values()
        )
        self.cache_float_widget.set_values(
            get_cache_float_values()
        )

        # Bind resolution change event
        self.resolution_widget.combobox.currentIndexChanged.connect(
            self._update_resolution_fields
        )
        self.cache_integer_widget.combobox.currentIndexChanged.connect(
            self._update_cache_integer_id
        )
        self.cache_float_widget.combobox.currentIndexChanged.connect(
            self._update_cache_float_id
        )

        # Connect all relevant widgets to emit parameters_updated signal
        self.resolution_widget.combobox.currentIndexChanged.connect(self._emit_parameters_updated)
        self.resolution_width_widget.entry.textChanged.connect(self._emit_parameters_updated)
        self.resolution_height_widget.entry.textChanged.connect(self._emit_parameters_updated)
        self.aspect_ratio_widget.entry.textChanged.connect(self._emit_parameters_updated)
        self.bit_depth_widget.combobox.currentIndexChanged.connect(self._emit_parameters_updated)
        self.frame_rate_widget.combobox.currentIndexChanged.connect(self._emit_parameters_updated)
        self.scan_mode_widget.combobox.currentIndexChanged.connect(self._emit_parameters_updated)
        self.start_frame_widget.combobox.currentIndexChanged.connect(self._emit_parameters_updated)
        self.init_config_widget.combobox.currentIndexChanged.connect(self._emit_parameters_updated)
        self.ocio_config_widget.combobox.currentIndexChanged.connect(self._emit_parameters_updated)
        self.cache_integer_widget.combobox.currentIndexChanged.connect(self._emit_parameters_updated)
        self.cache_float_widget.combobox.currentIndexChanged.connect(self._emit_parameters_updated)

        # Initial update for calculated fields
        self._update_resolution_fields()
        self._update_cache_integer_id()
        self._update_cache_float_id()

    def _emit_parameters_updated(self):
        self.parameters_updated.emit()

    def _update_resolution_fields(self):
        selected_resolution_data = (
            self.resolution_widget.get_selected_resolution_data()
        )

        if selected_resolution_data:
            width = selected_resolution_data.get("width", "")
            height = selected_resolution_data.get("height", "")
            aspect_ratio = selected_resolution_data.get("aspect_ratio", "")

            self.resolution_width_widget.set(str(width))
            self.resolution_height_widget.set(str(height))
            self.aspect_ratio_widget.set(str(aspect_ratio))
        else:
            self.resolution_width_widget.set("")
            self.resolution_height_widget.set("")
            self.aspect_ratio_widget.set("")

    def _update_cache_integer_id(self):
        self.cache_integer_id = self.cache_integer_widget.get()

    def _update_cache_float_id(self):
        self.cache_float_id = self.cache_float_widget.get()

    def get_template_parameters(self):
        selected_ocio_relative_path = self.ocio_config_widget.get()

        ocio_name, ocio_path = ocio_utils.get_ocio_details_from_relative_path(
            selected_ocio_relative_path
        )

        return {
            "template_resolution": self.resolution_widget.get(),
            "template_resolution_w": self.resolution_width_widget.get(),
            "template_resolution_h": self.resolution_height_widget.get(),
            "template_aspect_ratio": self.aspect_ratio_widget.get(),
            "template_bit_depth": self.bit_depth_widget.get(),
            "template_framerate": self.frame_rate_widget.get(),
            "template_scan_mode": self.scan_mode_widget.get(),
            "template_start_frame": self.start_frame_widget.get(),
            "template_init_config": self.init_config_widget.get(),
            "template_ocio_config": selected_ocio_relative_path,
            "template_ocio_name": ocio_name,
            "template_ocio_path": ocio_path,
            "template_cache_integer": self.cache_integer_widget.combobox.currentText(),
            "template_cache_integer_id": self.cache_integer_id,
            "template_cache_float": self.cache_float_widget.combobox.currentText(),
            "template_cache_float_id": self.cache_float_id,
        }

    def set_template_parameters(self, params):
        self.resolution_widget.set(
            params.get("template_resolution", "")
        )
        self.resolution_width_widget.set(
            params.get("template_resolution_w", "")
        )
        self.resolution_height_widget.set(
            params.get("template_resolution_h", "")
        )
        self.aspect_ratio_widget.set(
            params.get("template_aspect_ratio", "")
        )
        self.bit_depth_widget.set(
            params.get("template_bit_depth", "")
        )
        self.frame_rate_widget.set(
            params.get("template_framerate", "")
        )
        self.scan_mode_widget.set(
            params.get("template_scan_mode", "")
        )
        self.start_frame_widget.set(
            params.get("template_start_frame", "")
        )
        self.init_config_widget.set(
            params.get("template_init_config", "")
        )
        self.ocio_config_widget.set(
            params.get("template_ocio_config", "")
        )
        self.cache_integer_widget.set(
            params.get("template_cache_integer_id", 0)
        )
        self.cache_float_widget.set(
            params.get("template_cache_float_id", 0)
        )

        self._update_resolution_fields()


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
