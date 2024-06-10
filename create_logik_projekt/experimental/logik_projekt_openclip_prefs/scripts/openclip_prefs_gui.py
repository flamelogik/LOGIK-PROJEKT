'''
# -------------------------------------------------------------------------- #

# File Name:        debug_and_log.py
# Version:          1.0.0
# Language:         python script
# Flame Version:    2025.x
# Author:           Phil MAN - phil_man@mac.com
# Toolset:          MAN_MADE_MATERIAL: LOGIK-PROJEKT
# Created:          2024-04-20
# Modified:         2024-06-07
# Modifier:         Phil MAN - phil_man@mac.com

# Description:      This program is part of LOGIK-PROJEKT.
#                   LOGIK-PROJEKT is a library of custom functions and
#                   modules for autodesk flame.

# Installation:     Copy the 'LOGIK-PROJEKT' repo to your GitHub directory,
#                   e.g. '/home/$USER/workspace/GitHub'

# Changelist:       The full changelist is at the end of this document.

# -------------------------------------------------------------------------- #
'''

# ========================================================================== #
# This section defines the import staements.
# ========================================================================== #

# scripts/openclip_prefs_gui.py
from PySide6.QtWidgets import (
    QWidget, 
    QVBoxLayout, 
    QLabel, 
    QFrame, 
    QApplication, 
    QTextEdit,
    QPushButton,
    QLineEdit
)

from PySide6.QtCore import Qt
from PySide6.QtGui import QScreen

from modules.gui_components.pyside6_buttons import create_button

from modules.gui_components.pyside6_dropdowns import (
    create_openclip_dropdown,
    create_setup_dropdown,
    create_node_type_dropdown,
    create_node_format_dropdown,
    create_render_resolution_dropdown,
    create_frame_rate_dropdown,
    create_file_format_dropdown,
    create_bit_depth_dropdown,
    create_compression_dropdown,
    create_media_path_tokens_dropdown,
    create_workspace_tokens_dropdown,
    create_version_dropdown,
    create_zero_padding_dropdown,
    create_start_frame_dropdown,
    create_version_prefix_dropdown
)

from modules.gui_components.pyside6_lineedits import (
    create_render_node_type_lineedit,
    create_write_node_projekt_root_path_lineedit,
    create_write_node_file_path_lineedit,
    create_write_node_openclip_path_lineedit,
    create_write_node_setup_path_lineedit,
    create_write_node_create_openclip_lineedit,
    create_write_node_include_setup_lineedit,
    create_write_node_image_format_lineedit,
    create_write_node_compression_lineedit,
    create_write_node_padding_lineedit,
    create_write_node_frame_index_lineedit,
    create_write_node_version_name_lineedit
)

from modules.gui_components.pyside6_summary import create_summary_textbox, update_summary_textbox

from modules.gui_components.pyside6_stylesheet import stylesheet

from modules.functions.prefs_saver import openclip_prefs_saver

from modules.functions.prefs_loader import openclip_prefs_loader

# ========================================================================== #
# This section defines the main functions.
# ========================================================================== #

class MyGUI(QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()
        self.center()

    def init_ui(self):
        self.setWindowTitle("LOGIK-PROJEKT openclip preferences")

        layout = QVBoxLayout()

        # Add a label
        label = QLabel("This is a label")
        layout.addWidget(label)
        layout.addWidget(QFrame(frameShape=QFrame.HLine))

        # Load preferences
        try:
            self.prefs = openclip_prefs_loader()
        except FileNotFoundError:
            self.prefs = {}
            # Handle the case where the preferences file does not exist

        # Create a dictionary to hold line edits
        self.lineedits = {}

        # Add line edits with labels and separators
        self.add_lineedit(layout, "Projekt Root", create_write_node_projekt_root_path_lineedit(), self.prefs.get("Projekt Root"))
        self.add_lineedit(layout, "File Path", create_write_node_file_path_lineedit(), self.prefs.get("File Path"))
        self.add_lineedit(layout, "Openclip Path", create_write_node_openclip_path_lineedit(), self.prefs.get("Openclip Path"))
        self.add_lineedit(layout, "Batch Group Path", create_write_node_setup_path_lineedit(), self.prefs.get("Batch Group Path"))

        # Create a dictionary to hold dropdowns
        self.dropdowns = {}

        # Add dropdowns with labels and separators
        self.add_dropdown(layout, "Create Openclip", create_openclip_dropdown(), self.prefs.get("Create Openclip", "True"))
        self.add_dropdown(layout, "Create Batch Setup", create_setup_dropdown(), self.prefs.get("Create Batch Setup", "True"))
        self.add_dropdown(layout, "Node Type", create_node_type_dropdown(), self.prefs.get("Node Type", "Write File"))
        self.add_dropdown(layout, "File Format", create_file_format_dropdown(), self.prefs.get("File Format", "OpenEXR"))
        self.add_dropdown(layout, "Bit Depth", create_bit_depth_dropdown(), self.prefs.get("Bit Depth", "16-bit fp"))
        self.add_dropdown(layout, "Compression", create_compression_dropdown(), self.prefs.get("Compression", "PIZ"))
        self.add_dropdown(layout, "Zero Padding", create_zero_padding_dropdown(), self.prefs.get("Zero Padding", "8"))
        self.add_dropdown(layout, "Start Frame", create_start_frame_dropdown(), self.prefs.get("Start Frame", "Follow Iteration"))
        self.add_dropdown(layout, "Version Prefix", create_version_prefix_dropdown(), self.prefs.get("Version Prefix", "v"))

        # Add a label
        label = QLabel("LOGIK-PROJEKT Summary:")
        layout.addWidget(label)

        # Add summary text box with stylesheet
        self.summary_textbox = create_summary_textbox()
        layout.addWidget(self.summary_textbox)
        layout.addWidget(QFrame(frameShape=QFrame.HLine))

        # Add button
        button = create_button(self.summary_textbox)
        layout.addWidget(button)

        # Set layout
        self.setLayout(layout)

        # Set initial size
        self.resize(1024, 1280)

        # Connect line edits to update summary
        for lineedit in self.lineedits.values():
            lineedit.textChanged.connect(self.update_summary)

        # Connect dropdowns to update summary
        for dropdown in self.dropdowns.values():
            dropdown.currentIndexChanged.connect(self.update_summary)

        # Initialize summary
        self.update_summary()

    def add_lineedit(self, layout, label_text, lineedit, default_text=None):
        layout.addWidget(QLabel(f"{label_text}:"))
        if default_text:
            lineedit.setText(default_text)
        layout.addWidget(lineedit)
        layout.addWidget(QFrame(frameShape=QFrame.HLine))
        self.lineedits[label_text] = lineedit

    def add_dropdown(self, layout, label_text, dropdown, default_text=None):
        layout.addWidget(QLabel(f"{label_text}:"))
        if default_text:
            index = dropdown.findText(default_text, Qt.MatchFixedString)
            if index >= 0:
                dropdown.setCurrentIndex(index)
        layout.addWidget(dropdown)
        layout.addWidget(QFrame(frameShape=QFrame.HLine))
        self.dropdowns[label_text] = dropdown

    def update_summary(self):
        update_summary_textbox(self.summary_textbox, self.lineedits, self.dropdowns)

    def center(self):
        screen = QApplication.primaryScreen()
        screen_geometry = screen.availableGeometry()
        window_geometry = self.frameGeometry()
        window_geometry.moveCenter(screen_geometry.center())
        self.move(window_geometry.topLeft())

# ========================================================================== #
# C2 A9 32 30 32 34 2D 4D 41 4E 5F 4D 41 44 45 2D 4D 45 4B 41 4E 49 53 4D 5A #
# ========================================================================== #
'''
# -------------------------------------------------------------------------- #

# Disclaimer:       This program is part of LOGIK-PROJEKT.
#                   LOGIK-PROJEKT is free software.

#                   You can redistribute it and/or modify it under the terms
#                   of the GNU General Public License as published by the
#                   Free Software Foundation, either version 3 of the License,
#                   or any later version.

#                   This program is distributed in the hope that it will be
#                   useful, but WITHOUT ANY WARRANTY; without even the
#                   implied warranty of MERCHANTABILITY or FITNESS FOR A
#                   PARTICULAR PURPOSE.

#                   See the GNU General Public License for more details.

#                   You should have received a copy of the GNU General
#                   Public License along with this program.

#                   If not, see <https://www.gnu.org/licenses/>.
# -------------------------------------------------------------------------- #
'''
# -------------------------------------------------------------------------- #
# Changelist:       
# -------------------------------------------------------------------------- #
# version:               1.0.0
# modified:              2024-06-07 - 16:22:45
# comments:              Working program
