'''
# -------------------------------------------------------------------------- #
File Name:        logik_projekt_creator.py
Version:          1.1.8
Language:         python script
Author:           Phil MAN - phil_man@mac.com
Created:          2024-05-23
Modified:         2024-06-01
Description:      This program is part of LOGIK-PROJEKT.
# -------------------------------------------------------------------------- #
'''
import sys
import json
import os
from PySide6.QtWidgets import (
    QApplication, QWidget, QVBoxLayout, QLabel, QComboBox, QTextEdit, 
    QPushButton, QFrame, QLineEdit, QMainWindow)
from PySide6.QtGui import QFont, QGuiApplication
from PySide6.QtCore import Qt
from modules.functions.list_flame_family_software import list_flame_family_software
from modules.functions.projekt_utilities_strings import string_clean
from modules.functions.define_dropdown_menus import dropdown_menu_definitions

# -------------------------------------------------------------------------- #

class logik_projekt_main_window(QMainWindow):
    def __init__(self):
        super().__init__()
        self.init_projekt_UI()

    def init_projekt_UI(self):
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
        
        # Add text entry boxes
        self.projekt_serial_number = self.create_labeled_entry(layout, "Projekt Serial Number")
        self.projekt_client_name = self.create_labeled_entry(layout, "Projekt Client Name")
        self.projekt_campaign_name = self.create_labeled_entry(layout, "Projekt Campaign Name")

        self.projekt_resolution_label = QLabel('Projekt Resolution:')
        self.projekt_resolution_label.setStyleSheet("color: white; font-family: 'Courier New';")
        layout.addWidget(self.projekt_resolution_label)

        self.separator_line_top = QFrame()
        self.separator_line_top.setFrameShape(QFrame.HLine)
        self.separator_line_top.setFrameShadow(QFrame.Sunken)
        layout.addWidget(self.separator_line_top)

        # self.projekt_resolution = self.create_dropdown_menu(layout, "Projekt Resolution")
        self.projekt_resolution = QComboBox()
        self.projekt_resolution.setStyleSheet("""
            QComboBox {
                background-color: #111111;
                color: white;
                font-family: 'Courier New';
            }
            QComboBox::drop-down {
                border: 0px;
            }
            QComboBox QAbstractItemView {
                background-color: #111111;
                color: white;
                selection-background-color: #333333;
                selection-color: yellow;
            }
            QComboBox QAbstractItemView::item {
                height: 30px;
            }
            QComboBox QAbstractItemView::item:hover {
                background-color: #555555;
                color: yellow;
            }
        """)
        layout.addWidget(self.projekt_resolution)
        
        # Add dropdown menus
        self.projekt_bit_depth = self.create_dropdown_menu(layout, "Projekt Bit Depth")
        self.projekt_frame_rate = self.create_dropdown_menu(layout, "Projekt Frame Rate")
        self.projekt_color_science = self.create_dropdown_menu(layout, "Projekt Color Science")
        self.projekt_start_frame = self.create_dropdown_menu(layout, "Projekt Start Frame")

        self.separator_line_bottom = QFrame()
        self.separator_line_bottom.setFrameShape(QFrame.HLine)
        self.separator_line_bottom.setFrameShadow(QFrame.Sunken)
        layout.addWidget(self.separator_line_bottom)

        summary_label = QLabel("LOGIK-PROJEKT Summary")
        summary_label.setStyleSheet("color: white; font-family: 'Courier New', monospace; font-weight: bold;")
        layout.addWidget(summary_label)

        self.summary_text = QTextEdit()
        self.summary_text.setReadOnly(True)
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
        self.projekt_resolution.currentTextChanged.connect(self.update_summary)
        self.projekt_bit_depth.currentTextChanged.connect(self.update_summary)
        self.projekt_frame_rate.currentTextChanged.connect(self.update_summary)
        self.projekt_color_science.currentTextChanged.connect(self.update_summary)
        self.projekt_start_frame.currentTextChanged.connect(self.update_summary)

        self.load_resolutions()
        self.projekt_resolution.currentIndexChanged.connect(self.update_summary)

        # Set default choice to "HD 1080 16:9 (1920 x 1080)"
        default_index = self.projekt_resolution.findText("1920 x 1080 | HD 1080 16:9")
        self.projekt_resolution.setCurrentIndex(default_index)
        self.update_summary()

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
    
    def create_dropdown_menu(self, layout, label_text):
        """Create a labeled dropdown menu."""
        label = QLabel(label_text)
        label.setStyleSheet("color: white; font-family: 'Courier New', monospace;")
        layout.addWidget(label)
        
        combo_box = QComboBox()
        combo_box.addItems(dropdown_menu_definitions.get(label_text, []))
        combo_box.setStyleSheet("""
            background-color: #111111;
            color: white;
            font-family: 'Courier New', monospace;
            font-weight: bold;
        """)
        layout.addWidget(combo_box)
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

    def load_resolutions(self):
        # Get the directory of the current script
        script_dir = os.path.dirname(os.path.abspath(__file__))

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

        combined_data = {"items": []}

        # Read and combine data from all JSON files
        for file_name in json_files:
            resolutions_path = os.path.join(script_dir, '../config', file_name)
            with open(resolutions_path, 'r') as file:
                data = json.load(file)
                combined_data["items"].extend(data["items"])

        separator_names = set()  # To track already added separators

        for category in combined_data["items"]:
            separator_name = category.get("separator_name")
            if separator_name and separator_name not in separator_names:
                self.projekt_resolution.addItem(separator_name, userData=None)
                separator_names.add(separator_name)

            for item in category["items"]:
                self.projekt_resolution.addItem(item["name"], userData=item)

    # def update_summary(self):
    #     index = self.projekt_resolution.currentIndex()
    #     item_data = self.projekt_resolution.itemData(index)

    #     if item_data is None:
    #         # Separator selected, do nothing
    #         return

    #     resolution_name = self.projekt_resolution.currentText()

    #     projekt_width = item_data.get("width", 0)
    #     projekt_height = item_data.get("height", 0)
    #     projekt_aspect = item_data.get("display_aspect_ratio", 0)

    #     """Update the summary text."""
    #     serial_number = string_clean(self.projekt_serial_number.text())
    #     client_name = string_clean(self.projekt_client_name.text())
    #     campaign_name = string_clean(self.projekt_campaign_name.text())
    #     # resolution = self.projekt_resolution.currentText()
    #     bit_depth = self.projekt_bit_depth.currentText()
    #     frame_rate = self.projekt_frame_rate.currentText()
    #     color_science = self.projekt_color_science.currentText()
    #     start_frame = self.projekt_start_frame.currentText()
        
    #     summary = f"Projekt Serial Number: {serial_number}\n"
    #     summary += f"Projekt Client Name: {client_name}\n"
    #     summary += f"Projekt Campaign Name: {campaign_name}\n"
    #     # summary += f"Projekt Resolution: {resolution}\n"
    #     summary = f'Resolution:   {projekt_width} x {projekt_height}\n'
    #     summary += f"Projekt Bit Depth: {bit_depth}\n"
    #     summary += f"Projekt Frame Rate: {frame_rate}\n"
    #     summary += f"Projekt Color Science: {color_science}\n"
    #     summary += f"Projekt Start Frame: {start_frame}\n"
        
    #     self.summary_text.setPlainText(summary)
    
    def update_summary(self):
        index = self.projekt_resolution.currentIndex()
        item_data = self.projekt_resolution.itemData(index)

        if item_data is None:
            # Separator selected, do nothing
            return

        resolution_name = self.projekt_resolution.currentText()

        projekt_width = item_data.get("width", 0)
        projekt_height = item_data.get("height", 0)
        projekt_aspect = item_data.get("display_aspect_ratio", 0)

        """Update the summary text."""
        serial_number = string_clean(self.projekt_serial_number.text())
        client_name = string_clean(self.projekt_client_name.text())
        campaign_name = string_clean(self.projekt_campaign_name.text())
        bit_depth = self.projekt_bit_depth.currentText()
        frame_rate = self.projekt_frame_rate.currentText()
        color_science = self.projekt_color_science.currentText()
        start_frame = self.projekt_start_frame.currentText()

        summary = f"Projekt Serial Number: {serial_number}\n"
        summary += f"Projekt Client Name: {client_name}\n"
        summary += f"Projekt Campaign Name: {campaign_name}\n"
        summary += f'Resolution: {projekt_width} x {projekt_height}\n'
        summary += f"Projekt Bit Depth: {bit_depth}\n"
        summary += f"Projekt Frame Rate: {frame_rate}\n"
        summary += f"Projekt Color Science: {color_science}\n"
        summary += f"Projekt Start Frame: {start_frame}\n"
        
        self.summary_text.setPlainText(summary)


    def create_logik_projekt(self):
        """Placeholder for create_logik_projekt function."""
        pass

    def create_projekt_template(self):
        """Placeholder for create_projekt_template function."""
        pass

    def cancel(self):
        """Exit the application."""
        QApplication.quit()

# -------------------------------------------------------------------------- #

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = logik_projekt_main_window()
    window.show()
    sys.exit(app.exec())
