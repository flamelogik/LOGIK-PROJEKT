'''
File Name:        main.py
Version:          1.2.0
Language:         python script
Author:           Phil MAN - phil_man@mac.com
Created:          2024-05-23
Modified:         2024-06-02
Description:      This program is part of LOGIK-PROJEKT.
'''
# -------------------------------------------------------------------------- #

import sys
from PySide6.QtWidgets import (
    QApplication, QMainWindow, QWidget, QVBoxLayout, QLabel, QComboBox, 
    QTextEdit, QPushButton, QFrame, QLineEdit)
from PySide6.QtGui import QFont
from PySide6.QtCore import Qt
from modules.functions.projekt_utilities_strings import string_clean
from modules.functions.data_loader import (
    load_resolutions, load_bit_depths, load_frame_rates, 
    load_color_sciences, load_start_frames)

# -------------------------------------------------------------------------- #

class LogikProjektMainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.init_projekt_UI()

    def init_projekt_UI(self):
        self.setWindowTitle("LOGIK-PROJEKT Creator")
        self.setGeometry(0, 0, 1024, 960)
        self.center()
        
        self.setStyleSheet("background-color: #333333;")
        
        central_widget = QWidget()
        layout = QVBoxLayout()
        central_widget.setLayout(layout)
        self.setCentralWidget(central_widget)
        
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
        
        self.projekt_bit_depth = QComboBox()
        self.projekt_bit_depth.setStyleSheet("""
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
        layout.addWidget(self.projekt_bit_depth)
        
        self.projekt_frame_rate = QComboBox()
        self.projekt_frame_rate.setStyleSheet("""
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
        layout.addWidget(self.projekt_frame_rate)

        self.projekt_color_science = QComboBox()
        self.projekt_color_science.setStyleSheet("""
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
        layout.addWidget(self.projekt_color_science)

        self.projekt_start_frame = QComboBox()
        self.projekt_start_frame.setStyleSheet("""
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
        layout.addWidget(self.projekt_start_frame)

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

        self.create_logik_projekt_button = self.create_button(layout, "Create LOGIK-PROJEKT", "#014400", self.create_logik_projekt)
        self.create_projekt_template_button = self.create_button(layout, "Create PROJEKT Template", "#864B00", self.create_projekt_template)
        self.cancel_button = self.create_button(layout, "Cancel", "#630000", self.cancel)

        self.projekt_serial_number.textChanged.connect(self.update_summary)
        self.projekt_client_name.textChanged.connect(self.update_summary)
        self.projekt_campaign_name.textChanged.connect(self.update_summary)
        self.projekt_resolution.currentTextChanged.connect(self.update_summary)
        self.projekt_bit_depth.currentTextChanged.connect(self.update_summary)
        self.projekt_frame_rate.currentTextChanged.connect(self.update_summary)
        self.projekt_color_science.currentTextChanged.connect(self.update_summary)
        self.projekt_start_frame.currentTextChanged.connect(self.update_summary)

        load_resolutions(self.projekt_resolution)
        load_bit_depths(self.projekt_bit_depth)
        load_frame_rates(self.projekt_frame_rate)
        load_color_sciences(self.projekt_color_science)
        load_start_frames(self.projekt_start_frame)

        self.projekt_resolution.currentIndexChanged.connect(self.update_summary)

        default_index = self.projekt_resolution.findText("1920 x 1080 | HD 1080 16:9")
        self.projekt_resolution.setCurrentIndex(default_index)
        self.update_summary()

        default_index = self.projekt_bit_depth.findText("16-bit fp")
        self.projekt_bit_depth.setCurrentIndex(default_index)
        self.update_summary()

        default_index = self.projekt_frame_rate.findText("23.976 fps")
        self.projekt_frame_rate.setCurrentIndex(default_index)
        self.update_summary()

        default_index = self.projekt_color_science.findText("Autodesk ACES 1.1")
        self.projekt_color_science.setCurrentIndex(default_index)
        self.update_summary()

        default_index = self.projekt_start_frame.findText("1001")
        self.projekt_start_frame.setCurrentIndex(default_index)
        self.update_summary()

        self.update_summary()
    
    def center(self):
        frame_geometry = self.frameGeometry()
        screen_center = QApplication.primaryScreen().availableGeometry().center()
        frame_geometry.moveCenter(screen_center)
        self.move(frame_geometry.topLeft())

    def create_labeled_entry(self, layout, label_text):
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
    
    def create_button(self, layout, text, color, function):
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

    # def update_summary(self):
    #     serial_number = string_clean(self.projekt_serial_number.text())
    #     client_name = string_clean(self.projekt_client_name.text())
    #     campaign_name = string_clean(self.projekt_campaign_name.text())
    #     resolution = string_clean(self.projekt_resolution.currentText())
    #     bit_depth = string_clean(self.projekt_bit_depth.currentText())
    #     frame_rate = string_clean(self.projekt_frame_rate.currentText())
    #     color_science = string_clean(self.projekt_color_science.currentText())
    #     start_frame = string_clean(self.projekt_start_frame.currentText())

    #     summary = (
    #         f"Serial Number: {serial_number}\n"
    #         f"Client Name:   {client_name}\n"
    #         f"Campaign Name: {campaign_name}\n"
    #         f"Resolution:    {resolution}\n"
    #         f"Bit Depth:     {bit_depth}\n"
    #         f"Frame Rate:    {frame_rate}\n"
    #         f"Color Science: {color_science}\n"
    #         f"Start Frame:   {start_frame}\n"
    #     )
# -------------------------------------------------------------------------- #

    def update_summary(self):

        # ------------------------------------------------------------------ #

        resolution_index = self.projekt_resolution.currentIndex()
        resolution_item_data = self.projekt_resolution.itemData(resolution_index)

        if resolution_item_data is None:
            # Separator selected, do nothing
            return

        resolution_name = self.projekt_resolution.currentText()

        projekt_width = resolution_item_data.get("width", 0)
        projekt_height = resolution_item_data.get("height", 0)
        # projekt_aspect = resolution_item_data.get("display_aspect_ratio", 0)

        # ------------------------------------------------------------------ #

        bit_depth_index = self.projekt_bit_depth.currentIndex()
        bit_depth_item_data = self.projekt_bit_depth.itemData(bit_depth_index)

        if bit_depth_item_data is None:
            # Separator selected, do nothing
            return

        bit_depth_name = self.projekt_bit_depth.currentText()

        projekt_bit_depth = bit_depth_item_data.get("bit_depth_nickname", 0)

        # ------------------------------------------------------------------ #

        frame_rate_index = self.projekt_frame_rate.currentIndex()
        frame_rate_item_data = self.projekt_frame_rate.itemData(frame_rate_index)

        if frame_rate_item_data is None:
            # Separator selected, do nothing
            return

        frame_rate_name = self.projekt_frame_rate.currentText()

        projekt_frame_rate = frame_rate_item_data.get("frame_rate_nickname", 0)

        # ------------------------------------------------------------------ #

        color_science_index = self.projekt_color_science.currentIndex()
        color_science_item_data = self.projekt_color_science.itemData(color_science_index)

        if color_science_item_data is None:
            # Separator selected, do nothing
            return

        color_science_name = self.projekt_color_science.currentText()

        projekt_color_science = color_science_item_data.get("policy_nickname", 0)

        # ------------------------------------------------------------------ #

        start_frame_index = self.projekt_start_frame.currentIndex()
        start_frame_item_data = self.projekt_start_frame.itemData(start_frame_index)

        if start_frame_item_data is None:
            # Separator selected, do nothing
            return

        start_frame_name = self.projekt_start_frame.currentText()

        projekt_start_frame = start_frame_item_data.get("start_frame_nickname", 0)

        # ------------------------------------------------------------------ #

        """Update the summary text."""
        serial_number = string_clean(self.projekt_serial_number.text())
        client_name = string_clean(self.projekt_client_name.text())
        campaign_name = string_clean(self.projekt_campaign_name.text())
        # bit_depth = self.projekt_bit_depth.currentText()
        # frame_rate = self.projekt_frame_rate.currentText()
        # color_science = self.projekt_color_science.currentText()
        # start_frame = self.projekt_start_frame.currentText()

        summary = f"Projekt Serial Number:  {serial_number}\n"
        summary += f"Projekt Client Name:    {client_name}\n"
        summary += f"Projekt Campaign Name:  {campaign_name}\n"
        summary += f'Projekt Resolution:     {projekt_width} x {projekt_height}\n'
        summary += f"Projekt Bit Depth:      {projekt_bit_depth}\n"
        summary += f"Projekt Frame Rate:     {projekt_frame_rate}\n"
        summary += f"Projekt Color Science:  {projekt_color_science}\n"
        summary += f"Projekt Start Frame:    {projekt_start_frame}\n"

        self.summary_text.setPlainText(summary)

        # ------------------------------------------------------------------ #

    def create_logik_projekt(self):
        # Implement the logic to create the LOGIK-PROJEKT here
        print("Create LOGIK-PROJEKT clicked")
    
    def create_projekt_template(self):
        # Implement the logic to create the PROJEKT template here
        print("Create PROJEKT Template clicked")
    
    def cancel(self):
        # Implement the logic to cancel the operation here
        print("Cancel clicked")
        QApplication.quit()

# -------------------------------------------------------------------------- #

if __name__ == "__main__":
    app = QApplication(sys.argv)
    main_window = LogikProjektMainWindow()
    main_window.show()
    sys.exit(app.exec())
