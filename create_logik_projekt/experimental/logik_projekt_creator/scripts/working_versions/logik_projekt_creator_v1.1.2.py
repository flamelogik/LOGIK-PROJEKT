'''
# -------------------------------------------------------------------------- #
File Name:        logik_projekt_creator.py
Version:          1.1.2
Language:         python script
Author:           Phil MAN - phil_man@mac.com
Created:          2024-05-23
Modified:         2024-05-29
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
        QFileDialog,
        QMainWindow, 
        QWidget, 
        QVBoxLayout, 
        QHBoxLayout, 
        QLabel, 
        QLineEdit, 
        QTextEdit, 
        QComboBox,
        QPushButton
    )
    from PySide6.QtGui import (
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
        QHBoxLayout, 
        QLabel, 
        QLineEdit, 
        QTextEdit, 
        QComboBox,
        QPushButton
    )
    from PySide2.QtGui import (
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
from define_dropdown_menus import dropdown_menu_definitions
from create_projekt_template import create_projekt_template

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
        self.projekt_resolution = self.create_dropdown_menu(layout, "Projekt Resolution")
        self.projekt_bit_depth = self.create_dropdown_menu(layout, "Projekt Bit Depth")
        self.projekt_frame_rate = self.create_dropdown_menu(layout, "Projekt Frame Rate")
        self.projekt_color_science = self.create_dropdown_menu(layout, "Projekt Color Science")
        self.projekt_start_frame = self.create_dropdown_menu(layout, "Projekt Start Frame")
        
        # Add text entries for resolution horizontal and vertical directly under the resolution dropdown menu
        self.projekt_resolution_horizontal = self.create_labeled_entry(layout, "Horizontal Resolution")
        self.projekt_resolution_horizontal.setVisible(False)
        
        self.projekt_resolution_vertical = self.create_labeled_entry(layout, "Vertical Resolution")
        self.projekt_resolution_vertical.setVisible(False)
        
        # Add summary label and text
        summary_label = QLabel("LOGIK-PROJEKT Summary")
        summary_label.setStyleSheet("color: white; font-family: 'Courier New', monospace; font-weight: bold;")
        layout.addWidget(summary_label)
        
        self.summary_text = QTextEdit()
        self.summary_text.setStyleSheet("""
            background-color: #111111;
            color: white;
            font-family: 'Courier New', monospace;
            font-weight: bold;
        """)
        layout.addWidget(self.summary_text)
        
        # Add buttons
        self.create_logik_projekt_button = self.create_button(layout, "Create LOGIK-PROJEKT", "#014400", self.create_logik_projekt)
        self.create_projekt_template_button = self.create_button(layout, "Create PROJEKT Template", "#864B00", self.create_projekt_template)
        self.cancel_button = self.create_button(layout, "Cancel", "#630000", self.cancel)

        # Connect signals
        self.projekt_serial_number.textChanged.connect(self.update_summary)
        self.projekt_client_name.textChanged.connect(self.update_summary)
        self.projekt_campaign_name.textChanged.connect(self.update_summary)
        self.projekt_resolution.currentTextChanged.connect(self.on_resolution_changed)
        self.projekt_resolution_horizontal.textChanged.connect(self.update_summary)
        self.projekt_resolution_vertical.textChanged.connect(self.update_summary)
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
        container = QWidget()
        container_layout = QVBoxLayout()
        container.setLayout(container_layout)
        
        label = QLabel(label_text)
        label.setStyleSheet("color: white; font-family: 'Courier New', monospace;")
        container_layout.addWidget(label)
        
        entry = QLineEdit()
        entry.setStyleSheet("""
            background-color: #111111;
            color: white;
            font-family: 'Courier New', monospace;
            font-weight: bold;
        """)
        container_layout.addWidget(entry)
        
        layout.addWidget(container)
        return entry
    
    def create_dropdown_menu(self, layout, label_text):
        """Create a labeled dropdown menu."""
        container = QWidget()
        container_layout = QVBoxLayout()
        container.setLayout(container_layout)
        
        label = QLabel(label_text)
        label.setStyleSheet("color: white; font-family: 'Courier New', monospace;")
        container_layout.addWidget(label)
        
        combo_box = QComboBox()
        combo_box.addItems(dropdown_menu_definitions[label_text])
        combo_box.setStyleSheet("""
            background-color: #111111;
            color: white;
            font-family: 'Courier New', monospace;
            font-weight: bold;
        """)
        container_layout.addWidget(combo_box)
        
        layout.addWidget(container)
        return combo_box
    
    def create_button(self, layout, text, color, function):
        """Create a button with specified text, color, and function."""
        button = QPushButton(text)
        button.setStyleSheet(f"""
            background-color: {color};
            color: white;
            font-family: 'Courier New', monospace;
            font-weight: bold;
        """)
        button.clicked.connect(function)
        layout.addWidget(button)
        return button

    def on_resolution_changed(self):
        """Handle changes in the Projekt Resolution dropdown."""
        resolution = self.projekt_resolution.currentText()
        if resolution == 'Other':
            self.projekt_resolution_horizontal.setVisible(True)
            self.projekt_resolution_vertical.setVisible(True)
        else:
            self.projekt_resolution_horizontal.setVisible(False)
            self.projekt_resolution_vertical.setVisible(False)
            self.projekt_resolution_horizontal.clear()
            self.projekt_resolution_vertical.clear()
        self.update_summary()

    def update_summary(self):
        """Update the summary text."""
        client_name = string_clean(self.projekt_client_name.text())
        campaign_name = string_clean(self.projekt_campaign_name.text())
        bit_depth = self.projekt_bit_depth.currentText()
        frame_rate = self.projekt_frame_rate.currentText()
        color_science = self.projekt_color_science.currentText()
        start_frame = self.projekt_start_frame.currentText()
        
        resolution_horizontal = self.projekt_resolution_horizontal.text()
        resolution_vertical = self.projekt_resolution_vertical.text()
        resolution = f"{resolution_horizontal}x{resolution_vertical}"
        
        summary = f"Projekt Client Name: {client_name}\n"
        summary += f"Projekt Campaign Name: {campaign_name}\n"
        summary += f"Projekt Resolution: {resolution}\n"
        summary += f"Projekt Bit Depth: {bit_depth}\n"
        summary += f"Projekt Frame Rate: {frame_rate}\n"
        summary += f"Projekt Color Science: {color_science}\n"
        summary += f"Projekt Start Frame: {start_frame}\n"
        
        self.summary_text.setPlainText(summary)

    def create_logik_projekt(self):
        """Placeholder for create_logik_projekt function."""
        pass

    def create_projekt_template(self):
        """Create the PROJEKT Template."""
        client_name = string_clean(self.projekt_client_name.text())
        campaign_name = string_clean(self.projekt_campaign_name.text())
        summary_text = self.summary_text.toPlainText()

        try:
            file_path = create_projekt_template(client_name, campaign_name, summary_text)
            logging.info(f"Projekt template created at {file_path}")
            self.summary_text.append(f"\nProjekt template created at {file_path}")
        except ValueError as e:
            logging.error(f"Error: {e}")
            self.summary_text.append(f"\nError: {e}")

    def cancel(self):
        """Exit the application."""
        QApplication.quit()

# ========================================================================== #
# Main Execution
# ========================================================================== #

if __name__ == '__main__':
    check_operating_system()
    
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
