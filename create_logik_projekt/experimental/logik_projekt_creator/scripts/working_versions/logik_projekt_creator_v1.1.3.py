import sys
import json
import os
from PySide6.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel, QComboBox, QTextEdit, QPushButton, QFrame
from PySide6.QtGui import QColor, QFont
from PySide6.QtCore import Qt


class LogikProjektCreator(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('Logik Projekt Creator')

        layout = QVBoxLayout()

        self.resolution_label = QLabel('Projekt Resolution:')
        self.resolution_label.setStyleSheet("color: white;")
        layout.addWidget(self.resolution_label)

        self.separator_line = QFrame()
        self.separator_line.setFrameShape(QFrame.HLine)
        self.separator_line.setFrameShadow(QFrame.Sunken)
        layout.addWidget(self.separator_line)

        self.resolution_dropdown = QComboBox()
        self.resolution_dropdown.setStyleSheet("background-color: #111111; color: white; font-family: 'Courier New';")
        layout.addWidget(self.resolution_dropdown)

        self.summary_text = QTextEdit()
        self.summary_text.setReadOnly(True)
        self.summary_text.setStyleSheet("background-color: #111111; color: white; font-family: 'Courier New';")
        layout.addWidget(self.summary_text)

        self.cancel_button = QPushButton("Cancel")
        self.cancel_button.setStyleSheet("background-color: darkred; color: white; font-family: 'Courier New';")
        layout.addWidget(self.cancel_button)

        self.setLayout(layout)

        self.load_resolutions()
        self.resolution_dropdown.currentIndexChanged.connect(self.update_summary)
        self.cancel_button.clicked.connect(self.close)

        # Set font to Courier New
        font = QFont("Courier New")
        self.setFont(font)

        # Set background color to #333333
        self.setStyleSheet("background-color: #333333;")

        # Set default choice to "HD 1080 16:9 (1920 x 1080)"
        default_index = self.resolution_dropdown.findText("HD 1080 16:9 (1920 x 1080)")
        self.resolution_dropdown.setCurrentIndex(default_index)
        self.update_summary()

    def load_resolutions(self):
        # Get the directory of the current script
        script_dir = os.path.dirname(os.path.abspath(__file__))
        # Construct the absolute path to the resolutions.json file
        resolutions_path = os.path.join(script_dir, '../config/resolutions.json')

        with open(resolutions_path, 'r') as file:
            data = json.load(file)

        separator_names = set()  # To track already added separators

        for category in data["items"]:
            separator_name = category.get("separator_name")
            if separator_name and separator_name not in separator_names:
                self.resolution_dropdown.addItem(separator_name, userData=None)
                separator_names.add(separator_name)

            for item in category["items"]:
                self.resolution_dropdown.addItem(item["name"], userData=item)

    def update_summary(self):
        index = self.resolution_dropdown.currentIndex()
        item_data = self.resolution_dropdown.itemData(index)

        if item_data is None:
            # Separator selected, do nothing
            return

        resolution_name = self.resolution_dropdown.currentText()

        projekt_width = item_data.get("width", 0)
        projekt_height = item_data.get("height", 0)
        projekt_aspect = item_data.get("aspectRatio", 0)

        summary = f'Resolution: {projekt_width} x {projekt_height}\n'
        summary += f'Aspect Ratio: {projekt_aspect}'

        self.summary_text.setText(summary)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    creator = LogikProjektCreator()
    creator.show()
    sys.exit(app.exec())
