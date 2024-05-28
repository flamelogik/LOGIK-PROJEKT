'''
# -------------------------------------------------------------------------- #
File Name:        logik_projekt_creator.py
Version:          1.0.6
Language:         python script
Author:           Phil MAN - phil_man@mac.com
Created:          2024-05-23
Modified:         2024-05-27
Description:      This program is part of LOGIK-PROJEKT.
# -------------------------------------------------------------------------- #
'''

import sys
import os
import logging
from datetime import datetime

# Try to import PySide6 modules first; fall back to PySide2 if not available
try:
    from PySide6.QtWidgets import (
        QApplication, 
        QMainWindow, 
        QWidget, 
        QVBoxLayout, 
        QLabel, 
        QLineEdit, 
        QPushButton, 
        QTextEdit, 
        QMenuBar, 
        QMenu, 
        QComboBox
    )
    from PySide6.QtGui import (
        QAction, 
        QPalette, 
        QColor
    )
    from PySide6.QtCore import (
        Qt
    )
    print("Using PySide6")
except ImportError:
    from PySide2.QtWidgets import (
        QApplication, 
        QMainWindow, 
        QWidget, 
        QVBoxLayout, 
        QLabel, 
        QLineEdit, 
        QPushButton, 
        QTextEdit, 
        QMenuBar, 
        QMenu, 
        QComboBox
    )
    from PySide2.QtGui import (
        QAction, 
        QPalette, 
        QColor
    )
    from PySide2.QtCore import (
        Qt
    )
    print("Using PySide2")

# Add the modules/functions directory to the system path
script_path = os.path.abspath(__file__)
script_directory = os.path.dirname(script_path)
modules_dir = os.path.join(script_directory, 'modules', 'functions')
sys.path.append(modules_dir)

from debug_and_log import setup_logging
from os_check import check_operating_system
from string_utils import string_clean
from projekt_structure import create_logik_projekt_structure
from define_dropdown_menus import dropdown_menu_definitions

# ========================================================================== #
# Set up logging
# ========================================================================== #

log_filepath = setup_logging()

# ========================================================================== #
# GUI Setup
# ========================================================================== #

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        
        # Set window properties
        self.setWindowTitle("LOGIK-PROJEKT Creator")
        self.setGeometry(0, 0, 1024, 960)
        self.center()
        
        # Set the background color
        self.setStyleSheet("background-color: #333333;")
        
        # Create central widget and layout
        central_widget = QWidget()
        layout = QVBoxLayout()
        central_widget.setLayout(layout)
        self.setCentralWidget(central_widget)
        
        # Add widgets
        self.projekt_serial_number = self.create_labeled_entry(layout, "Projekt Serial Number")
        self.projekt_client_name = self.create_labeled_entry(layout, "Projekt Client Name")
        self.projekt_campaign_name = self.create_labeled_entry(layout, "Projekt Campaign Name")
        
        # Add dropdown menus
        resolution_label = QLabel("Projekt Resolution")
        resolution_label.setStyleSheet("color: white; font-family: 'Courier New', monospace;")
        layout.addWidget(resolution_label)
        self.projekt_resolution = QComboBox()
        self.projekt_resolution.addItems(["1920x1080", "3840x2160", "4096x2160"])  # Example resolutions
        layout.addWidget(self.projekt_resolution)
        
        bit_depth_label = QLabel("Projekt Bit Depth")
        bit_depth_label.setStyleSheet("color: white; font-family: 'Courier New', monospace;")
        layout.addWidget(bit_depth_label)
        self.projekt_bit_depth = QComboBox()
        self.projekt_bit_depth.addItems(["8-bit", "10-bit", "12-bit"])  # Example bit depths
        layout.addWidget(self.projekt_bit_depth)
        
        frame_rate_label = QLabel("Projekt Frame Rate")
        frame_rate_label.setStyleSheet("color: white; font-family: 'Courier New', monospace;")
        layout.addWidget(frame_rate_label)
        self.projekt_frame_rate = QComboBox()
        self.projekt_frame_rate.addItems(["24 fps", "30 fps", "60 fps"])  # Example frame rates
        layout.addWidget(self.projekt_frame_rate)
        
        color_science_label = QLabel("Projekt Color Science")
        color_science_label.setStyleSheet("color: white; font-family: 'Courier New', monospace;")
        layout.addWidget(color_science_label)
        self.projekt_color_science = QComboBox()
        self.projekt_color_science.addItems(["ACES", "Rec. 709", "Rec. 2020"])  # Example color sciences
        layout.addWidget(self.projekt_color_science)
        
        start_frame_label = QLabel("Projekt Start Frame")
        start_frame_label.setStyleSheet("color: white; font-family: 'Courier New', monospace;")
        layout.addWidget(start_frame_label)
        self.projekt_start_frame = QComboBox()
        self.projekt_start_frame.addItems(["0", "1", "100"])  # Example start frames
        layout.addWidget(self.projekt_start_frame)
        
        # Add summary text
        self.summary_text = QTextEdit()
        self.summary_text.setStyleSheet("""
            background-color: #111111;
            color: white;
            font-family: 'Courier New', monospace;
            font-weight: bold;
        """)
        layout.addWidget(self.summary_text)
        
        # Connect signals
        self.projekt_serial_number.textChanged.connect(self.update_summary)
        self.projekt_client_name.textChanged.connect(self.update_summary)
        self.projekt_campaign_name.textChanged.connect(self.update_summary)
        self.projekt_resolution.currentTextChanged.connect(self.update_summary)
        self.projekt_bit_depth.currentTextChanged.connect(self.update_summary)
        self.projekt_frame_rate.currentTextChanged.connect(self.update_summary)
        self.projekt_color_science.currentTextChanged.connect(self.update_summary)
        self.projekt_start_frame.currentTextChanged.connect(self.update_summary)
        
        # Initialize summary
        self.update_summary()
                
    def center(self):
        frame_geometry = self.frameGeometry()
        screen_center = QApplication.primaryScreen().availableGeometry().center()
        frame_geometry.moveCenter(screen_center)
        self.move(frame_geometry.topLeft())
    
    def create_labeled_entry(self, layout, label_text):
        """Create a labeled text entry box."""
        label = QLabel(label_text)
        label.setStyleSheet("color: white; font-family: 'Courier New', monospace;")
        layout.addWidget(label)
        
        entry = QLineEdit()
        entry.setStyleSheet("""
            background-color: #111111;
            color: white;
            font-family: 'Courier New', monospace;
            font-weight: bold;
        """)
        layout.addWidget(entry)
        return entry
        
    # Update the update_summary method to apply string_clean
    def update_summary(self):
        """Update the summary text."""
        serial_number = string_clean(self.projekt_serial_number.text())
        client_name = string_clean(self.projekt_client_name.text())
        campaign_name = string_clean(self.projekt_campaign_name.text())
        resolution = self.projekt_resolution.currentText()
        bit_depth = self.projekt_bit_depth.currentText()
        frame_rate = self.projekt_frame_rate.currentText()
        color_science = self.projekt_color_science.currentText()
        start_frame = self.projekt_start_frame.currentText()
        
        summary = f"Projekt Serial Number: {serial_number}\n"
        summary += f"Projekt Client Name: {client_name}\n"
        summary += f"Projekt Campaign Name: {campaign_name}\n"
        summary += f"Projekt Resolution: {resolution}\n"
        summary += f"Projekt Bit Depth: {bit_depth}\n"
        summary += f"Projekt Frame Rate: {frame_rate}\n"
        summary += f"Projekt Color Science: {color_science}\n"
        summary += f"Projekt Start Frame: {start_frame}\n"
        
        self.summary_text.setPlainText(summary)

# ========================================================================== #
# Application Entry Point
# ========================================================================== #

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
