# preferences_gui/preferences_gui.py

import sys
from PySide6 import QtWidgets, QtCore
from functools import partial

# Import the extracted functions
from scripts.functions.create_menu import create_menu
from scripts.functions.compression import compression
from scripts.functions.render_node_type_toggle import render_node_type_toggle
from scripts.functions.write_file_create_open_clip_btn_check import write_file_create_open_clip_btn_check
from scripts.functions.write_file_include_setup_btn_check import write_file_include_setup_btn_check
from scripts.functions.media_path_browse import media_path_browse
from scripts.functions.save_config import save_config
from scripts.functions.refresh_write_file import refresh_write_file
from scripts.functions.write_file_menu import write_file_menu
from scripts.functions.center_window import center_window

class PreferencesGUI:
    def __init__(self):
        self.setup_window = QtWidgets.QWidget()
        self.setup_window.setWindowTitle('Write File Menu')

        gridbox = QtWidgets.QGridLayout()

        # Write File Node Type Menu
        self.write_file_render_node_type_label = QtWidgets.QLabel('Render Node Type', self.setup_window)
        self.write_file_render_node_type_push_btn = QtWidgets.QPushButton('Render Node', self.setup_window)
        
        render_node_type_menu = QtWidgets.QMenu(self.setup_window)
        render_node_type_menu.addAction('Render Node', lambda: self.write_file_render_node_type_push_btn.setText('Render Node'))
        render_node_type_menu.addAction('Write File Node', lambda: self.write_file_render_node_type_push_btn.setText('Write File Node'))
        self.write_file_render_node_type_push_btn.setMenu(render_node_type_menu)

        # Connect button events to corresponding functions
        self.write_file_create_open_clip_btn.clicked.connect(write_file_create_open_clip_btn_check)
        self.write_file_include_setup_btn.clicked.connect(write_file_include_setup_btn_check)
        self.write_file_render_node_type_push_btn.clicked.connect(render_node_type_toggle)
        self.write_file_media_path_browse_btn.clicked.connect(media_path_browse)
        self.write_file_save_btn.clicked.connect(save_config)
        self.write_file_cancel_btn.clicked.connect(self.setup_window.close)

        # Add all your widgets to gridbox
        # Example:
        gridbox.addWidget(self.write_file_render_node_type_label, 1, 0, QtCore.Qt.AlignRight)
        gridbox.addWidget(self.write_file_render_node_type_push_btn, 1, 1, QtCore.Qt.AlignLeft)

        # Initialize Write File Menu
        write_file_menu(self)

        self.setup_window.setLayout(gridbox)

        # Center Window
        center_window(self.setup_window)

        self.setup_window.show()

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    gui = PreferencesGUI()
    sys.exit(app.exec())
