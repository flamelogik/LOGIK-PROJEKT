'''
# -------------------------------------------------------------------------- #
File Name:        logik_projekt_creator.py
Version:          1.1.6
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
    QPushButton, QFrame)
from PySide6.QtGui import (
    QFont, QColor, QBrush, QGuiApplication, QScreen)
from PySide6.QtCore import Qt
from modules.functions.list_flame_family_software import list_flame_family_software

# -------------------------------------------------------------------------- #

class logik_projekt_main_window(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('Logik Projekt Creator')

        layout = QVBoxLayout()

        self.resolution_label = QLabel('Projekt Resolution:')
        self.resolution_label.setStyleSheet("color: white; font-family: 'Courier New';")
        layout.addWidget(self.resolution_label)

        self.separator_line_top = QFrame()
        self.separator_line_top.setFrameShape(QFrame.HLine)
        self.separator_line_top.setFrameShadow(QFrame.Sunken)
        layout.addWidget(self.separator_line_top)

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

        self.separator_line_bottom = QFrame()
        self.separator_line_bottom.setFrameShape(QFrame.HLine)
        self.separator_line_bottom.setFrameShadow(QFrame.Sunken)
        layout.addWidget(self.separator_line_bottom)

        self.summary_text_label = QLabel('Projekt Summary:')
        self.summary_text_label.setStyleSheet("color: white; font-family: 'Courier New';")
        layout.addWidget(self.summary_text_label)
        self.summary_text = QTextEdit()
        self.summary_text.setReadOnly(True)
        self.summary_text.setStyleSheet("background-color: #111111; color: white; font-family: 'Courier New';")
        layout.addWidget(self.summary_text)

        self.cancel_button = QPushButton("Cancel")
        self.cancel_button.setStyleSheet("background-color: darkred; color: white; font-family: 'Courier New';")
        layout.addWidget(self.cancel_button)

        self.setLayout(layout)

        self.load_resolutions()
        self.projekt_resolution.currentIndexChanged.connect(self.update_summary)
        self.cancel_button.clicked.connect(self.close)

        # Set font to Courier New
        font = QFont("Courier New")
        self.setFont(font)

        # Set background color to #333333
        self.setStyleSheet("background-color: #333333;")

        # Set default choice to "HD 1080 16:9 (1920 x 1080)"
        default_index = self.projekt_resolution.findText("1920 x 1080 | HD 1080 16:9")
        self.projekt_resolution.setCurrentIndex(default_index)
        self.update_summary()

        # Center the application on the screen
        self.center()

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

        summary = f'Resolution:   {projekt_width} x {projekt_height}\n'
        summary += f'Aspect Ratio: {projekt_aspect}'

        self.summary_text.setText(summary)

    def center(self):
        # Get the primary screen
        screen = QGuiApplication.primaryScreen()

        # Get the screen geometry
        screen_geometry = screen.geometry()

        # Calculate the center position of the screen
        center_point = screen_geometry.center()

        # Move the window to the center of the screen
        self.move(center_point - self.rect().center())


if __name__ == '__main__':
    app = QApplication(sys.argv)
    creator = logik_projekt_main_window()
    creator.show()
    sys.exit(app.exec())
