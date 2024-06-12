# '''
# # -------------------------------------------------------------------------- #

# # File Name:        debug_and_log.py
# # Version:          1.0.0
# # Language:         python script
# # Flame Version:    2025.x
# # Author:           Phil MAN - phil_man@mac.com
# # Toolset:          MAN_MADE_MATERIAL: LOGIK-PROJEKT
# # Created:          2024-04-20
# # Modified:         2024-06-07
# # Modifier:         Phil MAN - phil_man@mac.com

# # Description:      This program is part of LOGIK-PROJEKT.
# #                   LOGIK-PROJEKT is a library of custom functions and
# #                   modules for autodesk flame.

# # Installation:     Copy the 'LOGIK-PROJEKT' repo to your GitHub directory,
# #                   e.g. '/home/$USER/workspace/GitHub'

# # Changelist:       The full changelist is at the end of this document.

# # -------------------------------------------------------------------------- #
# '''

# # ========================================================================== #
# # This section defines the import staements.
# # ========================================================================== #

# # scripts/openclip_prefs_gui.py
# from PySide6.QtWidgets import (
#     QWidget, 
#     QVBoxLayout, 
#     QLabel, 
#     QFrame, 
#     QApplication, 
#     QTextEdit,
#     QPushButton,
#     QLineEdit
# )

# from PySide6.QtCore import Qt
# from PySide6.QtGui import QScreen

# from modules.gui_components.projekt_qt_buttons import create_button

# from modules.gui_components.projekt_qt_lineedits import (
#     create_serial_id_lineedit,
#     create_client_name_lineedit,
#     create_campaign_name_lineedit
# )

# from modules.gui_components.projekt_qt_dropdowns import (
#     create_projekt_resolution_dropdown,
#     create_projekt_frame_rate_dropdown,
#     create_projekt_scan_mode_dropdown,
#     create_projekt_bit_depth_dropdown,
#     create_projekt_colour_science_dropdown,
#     create_projekt_start_frame_dropdown
# )

# from modules.gui_components.projekt_qt_summary import create_summary_textbox, update_summary_textbox

# from modules.gui_components.projekt_qt_stylesheet import stylesheet

# from modules.functions.prefs_saver import openclip_prefs_saver

# from modules.functions.prefs_loader import openclip_prefs_loader

# from modules.functions.projekt_utilities_strings import string_clean

# # ========================================================================== #
# # This section defines the main functions.
# # ========================================================================== #

# class MyGUI(QWidget):
#     def __init__(self):
#         super().__init__()
#         self.init_ui()
#         self.center()

#     def init_ui(self):
#         self.setWindowTitle("LOGIK-PROJEKT openclip preferences")

#         layout = QVBoxLayout()

#         # Add a label
#         label = QLabel("This is a label")
#         layout.addWidget(label)
#         layout.addWidget(QFrame(frameShape=QFrame.HLine))

#         # Load preferences
#         try:
#             self.prefs = openclip_prefs_loader()
#         except FileNotFoundError:
#             self.prefs = {}
#             # Handle the case where the preferences file does not exist

#         # Create a dictionary to hold line edits
#         self.lineedits = {}

#         # Add line edits with labels and separators
#         self.add_lineedit(layout, "Serial ID", create_serial_id_lineedit(), self.prefs.get("Serial ID"))
#         self.add_lineedit(layout, "Client Name", create_client_name_lineedit(), self.prefs.get("Client Name"))
#         self.add_lineedit(layout, "Campaign Name", create_campaign_name_lineedit(), self.prefs.get("Campaign Name"))

#         # Create a dictionary to hold dropdowns
#         self.dropdowns = {}

#         # Add dropdowns with labels and separators
#         self.add_dropdown(layout, "Projekt Resolution", create_projekt_resolution_dropdown(), self.prefs.get("Projekt Resolution", "True"))
#         self.add_dropdown(layout, "Projekt Frame Rate", create_projekt_frame_rate_dropdown(), self.prefs.get("Projekt Frame Rate", "23.976 fps"))
#         self.add_dropdown(layout, "Projekt Scan Mode", create_projekt_scan_mode_dropdown(), self.prefs.get("Projekt Scan Mode", "PROGRESSIVE"))
#         self.add_dropdown(layout, "Projekt Bit Depth", create_projekt_bit_depth_dropdown(), self.prefs.get("Projekt Bit Depth", "16-bit fp"))
#         self.add_dropdown(layout, "Projekt Color Science", create_projekt_colour_science_dropdown(), self.prefs.get("Projekt Color Science", "ARRI Alexa LogC V3 (K1S1)"))
#         self.add_dropdown(layout, "Projekt Start Frame", create_projekt_start_frame_dropdown(), self.prefs.get("Projekt Start Frame", "1001"))

#         # Add a label
#         label = QLabel("LOGIK-PROJEKT Summary:")
#         layout.addWidget(label)

#         # Add summary text box with stylesheet
#         self.summary_textbox = create_summary_textbox()
#         layout.addWidget(self.summary_textbox)
#         layout.addWidget(QFrame(frameShape=QFrame.HLine))

#         # Add button
#         button = create_button(self.summary_textbox)
#         layout.addWidget(button)

#         # Set layout
#         self.setLayout(layout)

#         # Set initial size
#         self.resize(1024, 1280)

#         # Connect line edits to update summary
#         for lineedit in self.lineedits.values():
#             lineedit.textChanged.connect(self.update_summary)

#         # Connect dropdowns to update summary
#         for dropdown in self.dropdowns.values():
#             dropdown.currentIndexChanged.connect(self.update_summary)

#         # Initialize summary
#         self.update_summary()

#     def add_lineedit(self, layout, label_text, lineedit, default_text=None):
#         layout.addWidget(QLabel(f"{label_text}:"))
#         if default_text:
#             lineedit.setText(default_text)
#         layout.addWidget(lineedit)
#         layout.addWidget(QFrame(frameShape=QFrame.HLine))
#         self.lineedits[label_text] = lineedit

#     def add_dropdown(self, layout, label_text, dropdown, default_text=None):
#         layout.addWidget(QLabel(f"{label_text}:"))
#         if default_text:
#             index = dropdown.findText(default_text, Qt.MatchFixedString)
#             if index >= 0:
#                 dropdown.setCurrentIndex(index)
#         layout.addWidget(dropdown)
#         layout.addWidget(QFrame(frameShape=QFrame.HLine))
#         self.dropdowns[label_text] = dropdown

#     def update_summary(self):
#         update_summary_textbox(self.summary_textbox, self.lineedits, self.dropdowns)

#     def center(self):
#         screen = QApplication.primaryScreen()
#         screen_geometry = screen.availableGeometry()
#         window_geometry = self.frameGeometry()
#         window_geometry.moveCenter(screen_geometry.center())
#         self.move(window_geometry.topLeft())

# # ========================================================================== #
# # C2 A9 32 30 32 34 2D 4D 41 4E 5F 4D 41 44 45 2D 4D 45 4B 41 4E 49 53 4D 5A #
# # ========================================================================== #
# '''
# # -------------------------------------------------------------------------- #

# # Disclaimer:       This program is part of LOGIK-PROJEKT.
# #                   LOGIK-PROJEKT is free software.

# #                   You can redistribute it and/or modify it under the terms
# #                   of the GNU General Public License as published by the
# #                   Free Software Foundation, either version 3 of the License,
# #                   or any later version.

# #                   This program is distributed in the hope that it will be
# #                   useful, but WITHOUT ANY WARRANTY; without even the
# #                   implied warranty of MERCHANTABILITY or FITNESS FOR A
# #                   PARTICULAR PURPOSE.

# #                   See the GNU General Public License for more details.

# #                   You should have received a copy of the GNU General
# #                   Public License along with this program.

# #                   If not, see <https://www.gnu.org/licenses/>.
# # -------------------------------------------------------------------------- #
# '''
# # -------------------------------------------------------------------------- #
# # Changelist:       
# # -------------------------------------------------------------------------- #
# # version:               1.0.0
# # modified:              2024-06-07 - 16:22:45
# # comments:              Working program












# # -------------------------------------------------------------------------- #

# # File Name:        debug_and_log.py
# # Version:          1.0.0
# # Language:         python script
# # Flame Version:    2025.x
# # Author:           Phil MAN - phil_man@mac.com
# # Toolset:          MAN_MADE_MATERIAL: LOGIK-PROJEKT
# # Created:          2024-04-20
# # Modified:         2024-06-07
# # Modifier:         Phil MAN - phil_man@mac.com

# # Description:      This program is part of LOGIK-PROJEKT.
# #                   LOGIK-PROJEKT is a library of custom functions and
# #                   modules for autodesk flame.

# # Installation:     Copy the 'LOGIK-PROJEKT' repo to your GitHub directory,
# #                   e.g. '/home/$USER/workspace/GitHub'

# # Changelist:       The full changelist is at the end of this document.

# # -------------------------------------------------------------------------- #

# # ========================================================================== #
# # This section defines the import staements.
# # ========================================================================== #

# # scripts/openclip_prefs_gui.py
# from PySide6.QtWidgets import (
#     QWidget, 
#     QVBoxLayout, 
#     QLabel, 
#     QFrame, 
#     QApplication, 
#     QTextEdit,
#     QPushButton,
#     QLineEdit
# )

# from PySide6.QtCore import Qt
# from PySide6.QtGui import QScreen

# from modules.gui_components.projekt_qt_buttons import create_button

# from modules.gui_components.projekt_qt_lineedits import (
#     create_serial_id_lineedit,
#     create_client_name_lineedit,
#     create_campaign_name_lineedit
# )

# from modules.gui_components.projekt_qt_dropdowns import (
#     create_projekt_resolution_dropdown,
#     create_projekt_frame_rate_dropdown,
#     create_projekt_scan_mode_dropdown,
#     create_projekt_bit_depth_dropdown,
#     create_projekt_colour_science_dropdown,
#     create_projekt_start_frame_dropdown
# )

# from modules.gui_components.projekt_qt_summary import create_summary_textbox, update_summary_textbox

# from modules.gui_components.projekt_qt_stylesheet import stylesheet

# from modules.functions.prefs_saver import openclip_prefs_saver

# from modules.functions.prefs_loader import openclip_prefs_loader

# from modules.functions.projekt_utilities_strings import string_clean

# # ========================================================================== #
# # This section defines the main functions.
# # ========================================================================== #

# class MyGUI(QWidget):
#     def __init__(self):
#         super().__init__()
#         self.init_ui()
#         self.center()

#     def init_ui(self):
#         self.setWindowTitle("LOGIK-PROJEKT openclip preferences")

#         layout = QVBoxLayout()

#         # Add a label
#         label = QLabel("This is a label")
#         layout.addWidget(label)
#         layout.addWidget(QFrame(frameShape=QFrame.HLine))

#         # Load preferences
#         try:
#             self.prefs = openclip_prefs_loader()
#         except FileNotFoundError:
#             self.prefs = {}
#             # Handle the case where the preferences file does not exist

#         # Create a dictionary to hold line edits
#         self.lineedits = {}

#         # Add line edits with labels and separators
#         self.add_lineedit(layout, "Serial ID", create_serial_id_lineedit(), self.prefs.get("Serial ID"))
#         self.add_lineedit(layout, "Client Name", create_client_name_lineedit(), self.prefs.get("Client Name"))
#         self.add_lineedit(layout, "Campaign Name", create_campaign_name_lineedit(), self.prefs.get("Campaign Name"))

#         # Create a dictionary to hold dropdowns
#         self.dropdowns = {}

#         # Add dropdowns with labels and separators
#         self.add_dropdown(layout, "Projekt Resolution", create_projekt_resolution_dropdown(), self.prefs.get("Projekt Resolution", "True"))
#         self.add_dropdown(layout, "Projekt Frame Rate", create_projekt_frame_rate_dropdown(), self.prefs.get("Projekt Frame Rate", "23.976 fps"))
#         self.add_dropdown(layout, "Projekt Scan Mode", create_projekt_scan_mode_dropdown(), self.prefs.get("Projekt Scan Mode", "PROGRESSIVE"))
#         self.add_dropdown(layout, "Projekt Bit Depth", create_projekt_bit_depth_dropdown(), self.prefs.get("Projekt Bit Depth", "16-bit fp"))
#         self.add_dropdown(layout, "Projekt Color Science", create_projekt_colour_science_dropdown(), self.prefs.get("Projekt Color Science", "ARRI Alexa LogC V3 (K1S1)"))
#         self.add_dropdown(layout, "Projekt Start Frame", create_projekt_start_frame_dropdown(), self.prefs.get("Projekt Start Frame", "1001"))

#         # Add a label
#         label = QLabel("LOGIK-PROJEKT Summary:")
#         layout.addWidget(label)

#         # Add summary text box with stylesheet
#         self.summary_textbox = create_summary_textbox()
#         layout.addWidget(self.summary_textbox)
#         layout.addWidget(QFrame(frameShape=QFrame.HLine))

#         # Add button
#         button = create_button(self.summary_textbox)
#         layout.addWidget(button)

#         # Set layout
#         self.setLayout(layout)

#         # Set initial size
#         self.resize(1024, 1280)

#         # Connect line edits to update summary
#         for lineedit in self.lineedits.values():
#             lineedit.textChanged.connect(self.update_summary)

#         # Connect dropdowns to update summary
#         for dropdown in self.dropdowns.values():
#             dropdown.currentIndexChanged.connect(self.update_summary)

#         # Initialize summary
#         self.update_summary()

#     def add_lineedit(self, layout, label_text, lineedit, default_text=None):
#         layout.addWidget(QLabel(f"{label_text}:"))
#         if default_text:
#             lineedit.setText(default_text)
#         layout.addWidget(lineedit)
#         layout.addWidget(QFrame(frameShape=QFrame.HLine))
#         self.lineedits[label_text] = lineedit

#         # Connect the textChanged signal to a slot that cleans the text
#         lineedit.textChanged.connect(lambda: self.clean_text(lineedit))

#     def add_dropdown(self, layout, label_text, dropdown, default_text=None):
#         layout.addWidget(QLabel(f"{label_text}:"))
#         if default_text:
#             index = dropdown.findText(default_text, Qt.MatchFixedString)
#             if index >= 0:
#                 dropdown.setCurrentIndex(index)
#         layout.addWidget(dropdown)
#         layout.addWidget(QFrame(frameShape=QFrame.HLine))
#         self.dropdowns[label_text] = dropdown

#     def clean_text(self, lineedit):
#         clean_text = string_clean(lineedit.text())
#         if clean_text != lineedit.text():
#             lineedit.setText(clean_text)

#     def update_summary(self):
#         update_summary_textbox(self.summary_textbox, self.lineedits, self.dropdowns)

#     def center(self):
#         screen = QApplication.primaryScreen()
#         screen_geometry = screen.availableGeometry()
#         window_geometry = self.frameGeometry()
#         window_geometry.moveCenter(screen_geometry.center())
#         self.move(window_geometry.topLeft())

# # ========================================================================== #
# # C2 A9 32 30 32 34 2D 4D 41 4E 5F 4D 41 44 45 2D 4D 45 4B 41 4E 49 53 4D 5A #
# # ========================================================================== #
# # -------------------------------------------------------------------------- #

# # Disclaimer:       This program is part of LOGIK-PROJEKT.
# #                   LOGIK-PROJEKT is free software.

# #                   You can redistribute it and/or modify it under the terms
# #                   of the GNU General Public License as published by the
# #                   Free Software Foundation, either version 3 of the License,
# #                   or any later version.

# #                   This program is distributed in the hope that it will be
# #                   useful, but WITHOUT ANY WARRANTY; without even the
# #                   implied warranty of MERCHANTABILITY or FITNESS FOR A
# #                   PARTICULAR PURPOSE.

# #                   See the GNU General Public License for more details.

# #                   You should have received a copy of the GNU General
# #                   Public License along with this program.

# #                   If not, see <https://www.gnu.org/licenses/>.
# # -------------------------------------------------------------------------- #
# # -------------------------------------------------------------------------- #
# # Changelist:       
# # -------------------------------------------------------------------------- #
# # version:               1.0.0
# # modified:              2024-06-07 - 16:22:45
# # comments:              Working program


















# # -------------------------------------------------------------------------- #

# # File Name:        debug_and_log.py
# # Version:          1.0.0
# # Language:         python script
# # Flame Version:    2025.x
# # Author:           Phil MAN - phil_man@mac.com
# # Toolset:          MAN_MADE_MATERIAL: LOGIK-PROJEKT
# # Created:          2024-04-20
# # Modified:         2024-06-07
# # Modifier:         Phil MAN - phil_man@mac.com

# # Description:      This program is part of LOGIK-PROJEKT.
# #                   LOGIK-PROJEKT is a library of custom functions and
# #                   modules for autodesk flame.

# # Installation:     Copy the 'LOGIK-PROJEKT' repo to your GitHub directory,
# #                   e.g. '/home/$USER/workspace/GitHub'

# # Changelist:       The full changelist is at the end of this document.

# # -------------------------------------------------------------------------- #

# # ========================================================================== #
# # This section defines the import staements.
# # ========================================================================== #

# import os

# # scripts/openclip_prefs_gui.py
# from PySide6.QtWidgets import (
#     QWidget, 
#     QVBoxLayout, 
#     QLabel, 
#     QFrame, 
#     QApplication, 
#     QTextEdit,
#     QPushButton,
#     QLineEdit
# )

# from PySide6.QtCore import Qt
# from PySide6.QtGui import QScreen

# from modules.gui_components.projekt_qt_buttons import create_button

# from modules.gui_components.projekt_qt_lineedits import (
#     create_serial_id_lineedit,
#     create_client_name_lineedit,
#     create_campaign_name_lineedit
# )

# from modules.gui_components.projekt_qt_dropdowns import (
#     create_projekt_resolution_dropdown,
#     create_projekt_frame_rate_dropdown,
#     create_projekt_scan_mode_dropdown,
#     create_projekt_bit_depth_dropdown,
#     create_projekt_colour_science_dropdown,
#     create_projekt_start_frame_dropdown
# )

# from modules.gui_components.projekt_qt_summary import create_summary_textbox, update_summary_textbox

# from modules.gui_components.projekt_qt_stylesheet import stylesheet

# from modules.functions.prefs_saver import openclip_prefs_saver

# from modules.functions.prefs_loader import openclip_prefs_loader

# from modules.functions.projekt_utilities_strings import string_clean

# from modules.functions.projekt_utilities_json import load_combined_json_data

# # ========================================================================== #
# # This section defines the main functions.
# # ========================================================================== #

# # class MyGUI(QWidget):
# #     def __init__(self):
# #         super().__init__()
# #         self.init_ui()
# #         self.center()

# #     def init_ui(self):
# #         self.setWindowTitle("LOGIK-PROJEKT")

# #         layout = QVBoxLayout()

# #         # Add a label
# #         label = QLabel("This is a label")
# #         layout.addWidget(label)
# #         layout.addWidget(QFrame(frameShape=QFrame.HLine))

# #         # Load preferences
# #         try:
# #             self.prefs = openclip_prefs_loader()
# #         except FileNotFoundError:
# #             self.prefs = {}
# #             # Handle the case where the preferences file does not exist

# #         # Create a dictionary to hold line edits
# #         self.lineedits = {}

# #         # Add line edits with labels and separators
# #         self.add_lineedit(layout, "Serial ID", create_serial_id_lineedit(), self.prefs.get("Serial ID"))
# #         self.add_lineedit(layout, "Client Name", create_client_name_lineedit(), self.prefs.get("Client Name"))
# #         self.add_lineedit(layout, "Campaign Name", create_campaign_name_lineedit(), self.prefs.get("Campaign Name"))

# #         # Create a dictionary to hold dropdowns
# #         self.dropdowns = {}

# #         # Add dropdowns with labels and separators
# #         self.add_dropdown(layout, "Projekt Resolution", create_projekt_resolution_dropdown(), self.prefs.get("Projekt Resolution", "True"))
# #         self.add_dropdown(layout, "Projekt Frame Rate", create_projekt_frame_rate_dropdown(), self.prefs.get("Projekt Frame Rate", "23.976 fps"))
# #         self.add_dropdown(layout, "Projekt Scan Mode", create_projekt_scan_mode_dropdown(), self.prefs.get("Projekt Scan Mode", "PROGRESSIVE"))
# #         self.add_dropdown(layout, "Projekt Bit Depth", create_projekt_bit_depth_dropdown(), self.prefs.get("Projekt Bit Depth", "16-bit fp"))
# #         self.add_dropdown(layout, "Projekt Color Science", create_projekt_colour_science_dropdown(), self.prefs.get("Projekt Color Science", "ARRI Alexa LogC V3 (K1S1)"))
# #         self.add_dropdown(layout, "Projekt Start Frame", create_projekt_start_frame_dropdown(), self.prefs.get("Projekt Start Frame", "1001"))

# #         # Add a label
# #         label = QLabel("LOGIK-PROJEKT Summary:")
# #         layout.addWidget(label)

# #         # Add summary text box with stylesheet
# #         self.summary_textbox = create_summary_textbox()
# #         layout.addWidget(self.summary_textbox)
# #         layout.addWidget(QFrame(frameShape=QFrame.HLine))

# #         # Add button
# #         button = create_button(self.summary_textbox)
# #         layout.addWidget(button)

# #         # Set layout
# #         self.setLayout(layout)

# #         # Set initial size
# #         self.resize(640, 1280)

# #         # Connect line edits to update summary
# #         for lineedit in self.lineedits.values():
# #             lineedit.textChanged.connect(self.update_summary)

# #         # Connect dropdowns to update summary
# #         for dropdown in self.dropdowns.values():
# #             dropdown.currentIndexChanged.connect(self.update_summary)

# #         # Initialize summary
# #         self.update_summary()

# #     def add_lineedit(self, layout, label_text, lineedit, default_text=None):
# #         layout.addWidget(QLabel(f"{label_text}:"))
# #         if default_text:
# #             lineedit.setText(default_text)
# #         layout.addWidget(lineedit)
# #         layout.addWidget(QFrame(frameShape=QFrame.HLine))
# #         self.lineedits[label_text] = lineedit

# #     def add_dropdown(self, layout, label_text, dropdown, default_text=None):
# #         layout.addWidget(QLabel(f"{label_text}:"))
# #         if default_text:
# #             index = dropdown.findText(default_text, Qt.MatchFixedString)
# #             if index >= 0:
# #                 dropdown.setCurrentIndex(index)
# #         layout.addWidget(dropdown)
# #         layout.addWidget(QFrame(frameShape=QFrame.HLine))
# #         self.dropdowns[label_text] = dropdown

# #     # def update_summary(self):
# #     #     cleaned_lineedits = {k: string_clean(v.text()) for k, v in self.lineedits.items()}
# #     #     update_summary_textbox(self.summary_textbox, cleaned_lineedits, self.dropdowns)

# #     def update_summary(self):
# #         # Create a dictionary of cleaned strings
# #         cleaned_lineedits = {k: string_clean(v.text()) for k, v in self.lineedits.items()}
# #         # Pass both dictionaries to the update_summary_textbox function
# #         update_summary_textbox(self.summary_textbox, self.lineedits, cleaned_lineedits, self.dropdowns)

# #     def center(self):
# #         screen = QApplication.primaryScreen()
# #         screen_geometry = screen.availableGeometry()
# #         window_geometry = self.frameGeometry()
# #         window_geometry.moveCenter(screen_geometry.center())
# #         self.move(window_geometry.topLeft())

# class MyGUI(QWidget):
#     def __init__(self):
#         super().__init__()
#         self.init_ui()
#         self.center()

#     def init_ui(self):
#         self.setWindowTitle("LOGIK-PROJEKT openclip preferences")

#         layout = QVBoxLayout()

#         # Add a label
#         label = QLabel("This is a label")
#         layout.addWidget(label)
#         layout.addWidget(QFrame(frameShape=QFrame.HLine))

#         # Load preferences
#         try:
#             self.prefs = openclip_prefs_loader()
#         except FileNotFoundError:
#             self.prefs = {}
#             # Handle the case where the preferences file does not exist

#         # Create a dictionary to hold line edits
#         self.lineedits = {}

#         # Add line edits with labels and separators
#         self.add_lineedit(layout, "Serial ID", create_serial_id_lineedit(), self.prefs.get("Serial ID"))
#         self.add_lineedit(layout, "Client Name", create_client_name_lineedit(), self.prefs.get("Client Name"))
#         self.add_lineedit(layout, "Campaign Name", create_campaign_name_lineedit(), self.prefs.get("Campaign Name"))

#         # Create a dictionary to hold dropdowns
#         self.dropdowns = {}

#         # Load resolutions and populate dropdown
#         resolutions = self.load_resolutions()
#         resolution_dropdown = create_projekt_resolution_dropdown()
#         for item in resolutions["items"]:
#             resolution_dropdown.addItem(item["label"], item["value"])
#         self.add_dropdown(layout, "Projekt Resolution", resolution_dropdown, self.prefs.get("Projekt Resolution", "True"))

#         # Add other dropdowns with labels and separators
#         self.add_dropdown(layout, "Projekt Frame Rate", create_projekt_frame_rate_dropdown(), self.prefs.get("Projekt Frame Rate", "23.976 fps"))
#         self.add_dropdown(layout, "Projekt Scan Mode", create_projekt_scan_mode_dropdown(), self.prefs.get("Projekt Scan Mode", "PROGRESSIVE"))
#         self.add_dropdown(layout, "Projekt Bit Depth", create_projekt_bit_depth_dropdown(), self.prefs.get("Projekt Bit Depth", "16-bit fp"))
#         self.add_dropdown(layout, "Projekt Color Science", create_projekt_colour_science_dropdown(), self.prefs.get("Projekt Color Science", "ARRI Alexa LogC V3 (K1S1)"))
#         self.add_dropdown(layout, "Projekt Start Frame", create_projekt_start_frame_dropdown(), self.prefs.get("Projekt Start Frame", "1001"))

#         # Add a label
#         label = QLabel("LOGIK-PROJEKT Summary:")
#         layout.addWidget(label)

#         # Add summary text box with stylesheet
#         self.summary_textbox = create_summary_textbox()
#         layout.addWidget(self.summary_textbox)
#         layout.addWidget(QFrame(frameShape=QFrame.HLine))

#         # Add button
#         button = create_button(self.summary_textbox)
#         layout.addWidget(button)

#         # Set layout
#         self.setLayout(layout)

#         # Set initial size
#         self.resize(1024, 1280)

#         # Connect line edits to update summary
#         for lineedit in self.lineedits.values():
#             lineedit.textChanged.connect(self.update_summary)

#         # Connect dropdowns to update summary
#         for dropdown in self.dropdowns.values():
#             dropdown.currentIndexChanged.connect(self.update_summary)

#         # Initialize summary
#         self.update_summary()

#     def load_resolutions(self):
#         # Get the directory of the current script
#         script_dir = os.path.dirname(os.path.abspath(__file__))
        
#         # List of JSON files in the order they should be read
#         json_files = [
#             'resolutions-broadcast.json',
#             'resolutions-film.json',
#             'resolutions-dcp.json',
#             'resolutions-aja.json',
#             'resolutions-arri.json',
#             'resolutions-bmd.json',
#             'resolutions-canon.json',
#             'resolutions-panasonic.json',
#             'resolutions-red.json',
#             'resolutions-sony.json',
#             'resolutions-zcam.json',
#             'resolutions-miscellaneous.json'
#         ]
        
#         return load_combined_json_data(script_dir, json_files)

#     def add_lineedit(self, layout, label_text, lineedit, default_text=None):
#         layout.addWidget(QLabel(f"{label_text}:"))
#         if default_text:
#             lineedit.setText(default_text)
#         layout.addWidget(lineedit)
#         layout.addWidget(QFrame(frameShape=QFrame.HLine))
#         self.lineedits[label_text] = lineedit

#     def add_dropdown(self, layout, label_text, dropdown, default_text=None):
#         layout.addWidget(QLabel(f"{label_text}:"))
#         if default_text:
#             index = dropdown.findText(default_text, Qt.MatchFixedString)
#             if index >= 0:
#                 dropdown.setCurrentIndex(index)
#         layout.addWidget(dropdown)
#         layout.addWidget(QFrame(frameShape=QFrame.HLine))
#         self.dropdowns[label_text] = dropdown

#     def update_summary(self):
#         cleaned_lineedits = {k: string_clean(v.text()) for k, v in self.lineedits.items()}
#         update_summary_textbox(self.summary_textbox, self.lineedits, cleaned_lineedits, self.dropdowns)

#     def center(self):
#         screen = QApplication.primaryScreen()
#         screen_geometry = screen.availableGeometry()
#         window_geometry = self.frameGeometry()
#         window_geometry.moveCenter(screen_geometry.center())
#         self.move(window_geometry.topLeft())

# # ========================================================================== #
# # C2 A9 32 30 32 34 2D 4D 41 4E 5F 4D 41 44 45 2D 4D 45 4B 41 4E 49 53 4D 5A #
# # ========================================================================== #
# # -------------------------------------------------------------------------- #

# # Disclaimer:       This program is part of LOGIK-PROJEKT.
# #                   LOGIK-PROJEKT is free software.

# #                   You can redistribute it and/or modify it under the terms
# #                   of the GNU General Public License as published by the
# #                   Free Software Foundation, either version 3 of the License,
# #                   or any later version.

# #                   This program is distributed in the hope that it will be
# #                   useful, but WITHOUT ANY WARRANTY; without even the
# #                   implied warranty of MERCHANTABILITY or FITNESS FOR A
# #                   PARTICULAR PURPOSE.

# #                   See the GNU General Public License for more details.

# #                   You should have received a copy of the GNU General
# #                   Public License along with this program.

# #                   If not, see <https://www.gnu.org/licenses/>.
# # -------------------------------------------------------------------------- #
# # -------------------------------------------------------------------------- #
# # Changelist:       
# # -------------------------------------------------------------------------- #
# # version:               1.0.0
# # modified:              2024-06-07 - 16:22:45
# # comments:              Working program






# import os
# from PySide6.QtWidgets import (
#     QWidget, 
#     QVBoxLayout, 
#     QLabel, 
#     QFrame, 
#     QApplication, 
#     QTextEdit,
#     QPushButton,
#     QLineEdit
# )
# from PySide6.QtCore import Qt
# from PySide6.QtGui import QScreen
# from modules.gui_components.projekt_qt_buttons import create_button
# from modules.gui_components.projekt_qt_lineedits import (
#     create_serial_id_lineedit,
#     create_client_name_lineedit,
#     create_campaign_name_lineedit
# )
# from modules.gui_components.projekt_qt_dropdowns import (
#     create_projekt_resolution_dropdown,
#     create_projekt_frame_rate_dropdown,
#     create_projekt_scan_mode_dropdown,
#     create_projekt_bit_depth_dropdown,
#     create_projekt_colour_science_dropdown,
#     create_projekt_start_frame_dropdown
# )
# from modules.gui_components.projekt_qt_summary import create_summary_textbox, update_summary_textbox
# from modules.gui_components.projekt_qt_stylesheet import stylesheet
# from modules.functions.prefs_saver import openclip_prefs_saver
# from modules.functions.prefs_loader import openclip_prefs_loader
# from modules.functions.projekt_utilities_strings import string_clean
# from modules.functions.projekt_utilities_json import load_combined_json_data

# class MyGUI(QWidget):
#     def __init__(self):
#         super().__init__()
#         self.init_ui()
#         self.center()

#     def init_ui(self):
#         self.setWindowTitle("LOGIK-PROJEKT openclip preferences")

#         layout = QVBoxLayout()

#         # Add a label
#         label = QLabel("This is a label")
#         layout.addWidget(label)
#         layout.addWidget(QFrame(frameShape=QFrame.HLine))

#         # Load preferences
#         try:
#             self.prefs = openclip_prefs_loader()
#         except FileNotFoundError:
#             self.prefs = {}
#             # Handle the case where the preferences file does not exist

#         # Create a dictionary to hold line edits
#         self.lineedits = {}

#         # Add line edits with labels and separators
#         self.add_lineedit(layout, "Serial ID", create_serial_id_lineedit(), self.prefs.get("Serial ID"))
#         self.add_lineedit(layout, "Client Name", create_client_name_lineedit(), self.prefs.get("Client Name"))
#         self.add_lineedit(layout, "Campaign Name", create_campaign_name_lineedit(), self.prefs.get("Campaign Name"))

#         # Create a dictionary to hold dropdowns
#         self.dropdowns = {}

#         # Load resolutions and populate dropdown
#         resolutions = self.load_resolutions()
#         resolution_dropdown = create_projekt_resolution_dropdown()
#         for item in resolutions["items"]:
#             resolution_dropdown.addItem(item["label"], item["value"])
#         self.add_dropdown(layout, "Projekt Resolution", resolution_dropdown, self.prefs.get("Projekt Resolution", "True"))

#         # Add other dropdowns with labels and separators
#         self.add_dropdown(layout, "Projekt Frame Rate", create_projekt_frame_rate_dropdown(), self.prefs.get("Projekt Frame Rate", "23.976 fps"))
#         self.add_dropdown(layout, "Projekt Scan Mode", create_projekt_scan_mode_dropdown(), self.prefs.get("Projekt Scan Mode", "PROGRESSIVE"))
#         self.add_dropdown(layout, "Projekt Bit Depth", create_projekt_bit_depth_dropdown(), self.prefs.get("Projekt Bit Depth", "16-bit fp"))
#         self.add_dropdown(layout, "Projekt Color Science", create_projekt_colour_science_dropdown(), self.prefs.get("Projekt Color Science", "ARRI Alexa LogC V3 (K1S1)"))
#         self.add_dropdown(layout, "Projekt Start Frame", create_projekt_start_frame_dropdown(), self.prefs.get("Projekt Start Frame", "1001"))

#         # Add a label
#         label = QLabel("LOGIK-PROJEKT Summary:")
#         layout.addWidget(label)

#         # Add summary text box with stylesheet
#         self.summary_textbox = create_summary_textbox()
#         layout.addWidget(self.summary_textbox)
#         layout.addWidget(QFrame(frameShape=QFrame.HLine))

#         # Add button
#         button = create_button(self.summary_textbox)
#         layout.addWidget(button)

#         # Set layout
#         self.setLayout(layout)

#         # Set initial size
#         self.resize(1024, 1280)

#         # Connect line edits to update summary
#         for lineedit in self.lineedits.values():
#             lineedit.textChanged.connect(self.update_summary)

#         # Connect dropdowns to update summary
#         for dropdown in self.dropdowns.values():
#             dropdown.currentIndexChanged.connect(self.update_summary)

#         # Initialize summary
#         self.update_summary()

#     def load_resolutions(self):
#         # Get the directory of the current script
#         script_dir = os.path.dirname(os.path.abspath(__file__))
#         config_dir = os.path.join(script_dir, '..', 'config')

#         # List of JSON files in the order they should be read
#         json_files = [
#             'resolutions-broadcast.json',
#             'resolutions-film.json',
#             'resolutions-dcp.json',
#             'resolutions-aja.json',
#             'resolutions-arri.json',
#             'resolutions-bmd.json',
#             'resolutions-canon.json',
#             'resolutions-panasonic.json',
#             'resolutions-red.json',
#             'resolutions-sony.json',
#             'resolutions-zcam.json',
#             'resolutions-miscellaneous.json'
#         ]
        
#         return load_combined_json_data(config_dir, json_files)

#     def add_lineedit(self, layout, label_text, lineedit, default_text=None):
#         layout.addWidget(QLabel(f"{label_text}:"))
#         if default_text:
#             lineedit.setText(default_text)
#         layout.addWidget(lineedit)
#         layout.addWidget(QFrame(frameShape=QFrame.HLine))
#         self.lineedits[label_text] = lineedit

#     def add_dropdown(self, layout, label_text, dropdown, default_text=None):
#         layout.addWidget(QLabel(f"{label_text}:"))
#         if default_text:
#             index = dropdown.findText(default_text, Qt.MatchFixedString)
#             if index >= 0:
#                 dropdown.setCurrentIndex(index)
#         layout.addWidget(dropdown)
#         layout.addWidget(QFrame(frameShape=QFrame.HLine))
#         self.dropdowns[label_text] = dropdown

#     def update_summary(self):
#         cleaned_lineedits = {k: string_clean(v.text()) for k, v in self.lineedits.items()}
#         update_summary_textbox(self.summary_textbox, self.lineedits, cleaned_lineedits, self.dropdowns)

#     def center(self):
#         screen = QApplication.primaryScreen()
#         screen_geometry = screen.availableGeometry()
#         window_geometry = self.frameGeometry()
#         window_geometry.moveCenter(screen_geometry.center())
#         self.move(window_geometry.topLeft())

















# import json

# import os

# from PySide6.QtWidgets import (
#     QWidget, 
#     QVBoxLayout, 
#     QLabel, 
#     QFrame, 
#     QApplication, 
#     QTextEdit,
#     QPushButton,
#     QLineEdit
# )
# from PySide6.QtCore import Qt
# from PySide6.QtGui import QScreen
# from modules.gui_components.projekt_qt_buttons import create_button
# from modules.gui_components.projekt_qt_lineedits import (
#     create_serial_id_lineedit,
#     create_client_name_lineedit,
#     create_campaign_name_lineedit
# )
# from modules.gui_components.projekt_qt_dropdowns import (
#     create_projekt_resolution_dropdown,
#     create_projekt_frame_rate_dropdown,
#     create_projekt_scan_mode_dropdown,
#     create_projekt_bit_depth_dropdown,
#     create_projekt_colour_science_dropdown,
#     create_projekt_start_frame_dropdown
# )
# from modules.gui_components.projekt_qt_summary import create_summary_textbox, update_summary_textbox
# from modules.gui_components.projekt_qt_stylesheet import stylesheet
# from modules.functions.prefs_saver import openclip_prefs_saver
# from modules.functions.prefs_loader import openclip_prefs_loader
# from modules.functions.projekt_utilities_strings import string_clean
# from modules.functions.projekt_utilities_json import load_combined_json_data


# def load_combined_json_data(directory, json_files):
#     combined_data = {"items": []}
#     for json_file in json_files:
#         with open(os.path.join(directory, json_file), 'r') as file:
#             data = json.load(file)
#             for item in data.get("items", []):
#                 if "separator" in item and "items" in item:
#                     combined_data["items"].extend(item["items"])
#                 else:
#                     combined_data["items"].append(item)
#     return combined_data

# class MyGUI(QWidget):
#     def __init__(self):
#         super().__init__()
#         self.init_ui()
#         self.center()

#     def init_ui(self):
#         self.setWindowTitle("LOGIK-PROJEKT openclip preferences")

#         layout = QVBoxLayout()

#         # Add a label
#         label = QLabel("This is a label")
#         layout.addWidget(label)
#         layout.addWidget(QFrame(frameShape=QFrame.HLine))

#         # Load preferences
#         try:
#             self.prefs = openclip_prefs_loader()
#         except FileNotFoundError:
#             self.prefs = {}
#             # Handle the case where the preferences file does not exist

#         # Create a dictionary to hold line edits
#         self.lineedits = {}

#         # Add line edits with labels and separators
#         self.add_lineedit(layout, "Serial ID", create_serial_id_lineedit(), self.prefs.get("Serial ID"))
#         self.add_lineedit(layout, "Client Name", create_client_name_lineedit(), self.prefs.get("Client Name"))
#         self.add_lineedit(layout, "Campaign Name", create_campaign_name_lineedit(), self.prefs.get("Campaign Name"))

#         # Create a dictionary to hold dropdowns
#         self.dropdowns = {}

#         # Load resolutions and populate dropdown
#         resolutions = self.load_resolutions()
#         resolution_dropdown = create_projekt_resolution_dropdown()
#         for item in resolutions.get("items", []):
#             name = item.get("name")
#             if name:
#                 resolution_dropdown.addItem(name)
#             else:
#                 print(f"Skipping item with missing name: {item}")
#         self.add_dropdown(layout, "Projekt Resolution", resolution_dropdown, self.prefs.get("Projekt Resolution", "1920 x 1080 | HD 1080 16:9"))

#         # Add other dropdowns with labels and separators
#         self.add_dropdown(layout, "Projekt Frame Rate", create_projekt_frame_rate_dropdown(), self.prefs.get("Projekt Frame Rate", "23.976 fps"))
#         self.add_dropdown(layout, "Projekt Scan Mode", create_projekt_scan_mode_dropdown(), self.prefs.get("Projekt Scan Mode", "PROGRESSIVE"))
#         self.add_dropdown(layout, "Projekt Bit Depth", create_projekt_bit_depth_dropdown(), self.prefs.get("Projekt Bit Depth", "16-bit fp"))
#         self.add_dropdown(layout, "Projekt Color Science", create_projekt_colour_science_dropdown(), self.prefs.get("Projekt Color Science", "ARRI Alexa LogC V3 (K1S1)"))
#         self.add_dropdown(layout, "Projekt Start Frame", create_projekt_start_frame_dropdown(), self.prefs.get("Projekt Start Frame", "1001"))

#         # Add a label
#         label = QLabel("LOGIK-PROJEKT Summary:")
#         layout.addWidget(label)

#         # Add summary text box with stylesheet
#         self.summary_textbox = create_summary_textbox()
#         layout.addWidget(self.summary_textbox)
#         layout.addWidget(QFrame(frameShape=QFrame.HLine))

#         # Add button
#         button = create_button(self.summary_textbox)
#         layout.addWidget(button)

#         # Set layout
#         self.setLayout(layout)

#         # Set initial size
#         self.resize(640, 1280)

#         # Connect line edits to update summary
#         for lineedit in self.lineedits.values():
#             lineedit.textChanged.connect(self.update_summary)

#         # Connect dropdowns to update summary
#         for dropdown in self.dropdowns.values():
#             dropdown.currentIndexChanged.connect(self.update_summary)

#         # Initialize summary
#         self.update_summary()

#     def load_resolutions(self):
#         # Get the directory of the current script
#         script_dir = os.path.dirname(os.path.abspath(__file__))
#         config_dir = os.path.join(script_dir, '..', 'config')

#         # List of JSON files in the order they should be read
#         json_files = [
#             'resolutions-broadcast.json',
#             'resolutions-film.json',
#             'resolutions-dcp.json',
#             'resolutions-aja.json',
#             'resolutions-arri.json',
#             'resolutions-bmd.json',
#             'resolutions-canon.json',
#             'resolutions-panasonic.json',
#             'resolutions-red.json',
#             'resolutions-sony.json',
#             'resolutions-zcam.json',
#             'resolutions-miscellaneous.json'
#         ]
        
#         return load_combined_json_data(config_dir, json_files)

#     def add_lineedit(self, layout, label_text, lineedit, default_text=None):
#         layout.addWidget(QLabel(f"{label_text}:"))
#         if default_text:
#             lineedit.setText(default_text)
#         layout.addWidget(lineedit)
#         layout.addWidget(QFrame(frameShape=QFrame.HLine))
#         self.lineedits[label_text] = lineedit

#     def add_dropdown(self, layout, label_text, dropdown, default_text=None):
#         layout.addWidget(QLabel(f"{label_text}:"))
#         if default_text:
#             index = dropdown.findText(default_text, Qt.MatchFixedString)
#             if index >= 0:
#                 dropdown.setCurrentIndex(index)
#         layout.addWidget(dropdown)
#         layout.addWidget(QFrame(frameShape=QFrame.HLine))
#         self.dropdowns[label_text] = dropdown

#     def update_summary(self):
#         cleaned_lineedits = {k: string_clean(v.text()) for k, v in self.lineedits.items()}
#         update_summary_textbox(self.summary_textbox, self.lineedits, cleaned_lineedits, self.dropdowns)

#     def center(self):
#         screen = QApplication.primaryScreen()
#         screen_geometry = screen.availableGeometry()
#         window_geometry = self.frameGeometry()
#         window_geometry.moveCenter(screen_geometry.center())
#         self.move(window_geometry.topLeft())

# if __name__ == "__main__":
#     app = QApplication([])
#     gui = MyGUI()
#     gui.show()
#     app.exec()































import os
import json
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
from modules.gui_components.projekt_qt_buttons import create_button
from modules.gui_components.projekt_qt_lineedits import (
    create_serial_id_lineedit,
    create_client_name_lineedit,
    create_campaign_name_lineedit
)
from modules.gui_components.projekt_qt_dropdowns import (
    create_projekt_resolution_dropdown,
    create_projekt_frame_rate_dropdown,
    create_projekt_scan_mode_dropdown,
    create_projekt_bit_depth_dropdown,
    create_projekt_colour_science_dropdown,
    create_projekt_start_frame_dropdown,
    SeparatorItemDelegate
)
from modules.gui_components.projekt_qt_summary import create_summary_textbox, update_summary_textbox
from modules.gui_components.projekt_qt_stylesheet import stylesheet
from modules.functions.prefs_saver import openclip_prefs_saver
from modules.functions.prefs_loader import openclip_prefs_loader
from modules.functions.projekt_utilities_strings import string_clean

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
        self.add_lineedit(layout, "Serial ID", create_serial_id_lineedit(), self.prefs.get("Serial ID"))
        self.add_lineedit(layout, "Client Name", create_client_name_lineedit(), self.prefs.get("Client Name"))
        self.add_lineedit(layout, "Campaign Name", create_campaign_name_lineedit(), self.prefs.get("Campaign Name"))

        # Create a dictionary to hold dropdowns
        self.dropdowns = {}

        # Load resolutions and populate dropdown
        resolutions = self.load_resolutions()
        resolution_dropdown = create_projekt_resolution_dropdown()
        for item in resolutions.get("items", []):
            name = item.get("name")
            if name:
                resolution_dropdown.addItem(name)
            else:
                print(f"Skipping item with missing name: {item}")
        self.add_dropdown(layout, "Projekt Resolution", resolution_dropdown, self.prefs.get("Projekt Resolution", "1920 x 1080 | HD 1080 16:9"))

        # Add other dropdowns with labels and separators
        self.add_dropdown(layout, "Projekt Frame Rate", create_projekt_frame_rate_dropdown(), self.prefs.get("Projekt Frame Rate", "23.976 fps"))
        self.add_dropdown(layout, "Projekt Scan Mode", create_projekt_scan_mode_dropdown(), self.prefs.get("Projekt Scan Mode", "PROGRESSIVE"))
        self.add_dropdown(layout, "Projekt Bit Depth", create_projekt_bit_depth_dropdown(), self.prefs.get("Projekt Bit Depth", "16-bit fp"))
        self.add_dropdown(layout, "Projekt Color Science", create_projekt_colour_science_dropdown(), self.prefs.get("Projekt Color Science", "ARRI Alexa LogC V3 (K1S1)"))
        self.add_dropdown(layout, "Projekt Start Frame", create_projekt_start_frame_dropdown(), self.prefs.get("Projekt Start Frame", "1001"))

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
        self.resize(640, 1280)

        # Connect line edits to update summary
        for lineedit in self.lineedits.values():
            lineedit.textChanged.connect(self.update_summary)

        # Connect dropdowns to update summary
        for dropdown in self.dropdowns.values():
            dropdown.currentIndexChanged.connect(self.update_summary)

        # Initialize summary
        self.update_summary()

    def load_resolutions(self):
        # Get the directory of the current script
        script_dir = os.path.dirname(os.path.abspath(__file__))
        config_dir = os.path.join(script_dir, '..', 'config')

        # List of JSON files in the order they should be read
        json_files = [
            'resolutions-broadcast.json',
            'resolutions-film.json',
            'resolutions-dcp.json',
            'resolutions-aja.json',
            'resolutions-arri.json',
            'resolutions-bmd.json',
            'resolutions-canon.json',
            'resolutions-panasonic.json',
            'resolutions-red.json',
            'resolutions-sony.json',
            'resolutions-zcam.json',
            'resolutions-miscellaneous.json'
        ]
        
        return load_combined_json_data(config_dir, json_files)

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
        cleaned_lineedits = {k: string_clean(v.text()) for k, v in self.lineedits.items()}
        update_summary_textbox(self.summary_textbox, self.lineedits, cleaned_lineedits, self.dropdowns)

    def center(self):
        screen = QApplication.primaryScreen()
        screen_geometry = screen.availableGeometry()
        window_geometry = self.frameGeometry()
        window_geometry.moveCenter(screen_geometry.center())
        self.move(window_geometry.topLeft())

if __name__ == "__main__":
    app = QApplication([])
    gui = MyGUI()
    gui.show()
    app.exec()
