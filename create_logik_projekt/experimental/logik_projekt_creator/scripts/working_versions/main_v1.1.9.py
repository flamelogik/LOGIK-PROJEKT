import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QWidget, QLabel, QTextEdit, QFrame, QComboBox, QLineEdit
from PySide6.QtCore import Qt
from modules.functions.projekt_utilities_ui import create_labeled_entry, create_dropdown_menu, create_button
from modules.functions.data_loader import load_resolutions
from modules.functions.projekt_utilities_strings import string_clean

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

        self.projekt_serial_number = create_labeled_entry(layout, "Projekt Serial Number")
        self.projekt_client_name = create_labeled_entry(layout, "Projekt Client Name")
        self.projekt_campaign_name = create_labeled_entry(layout, "Projekt Campaign Name")

        # ------------------------------------------------------------------ #

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

        # ------------------------------------------------------------------ #

        self.projekt_bit_depth = create_dropdown_menu(layout, "Projekt Bit Depth")
        self.projekt_frame_rate = create_dropdown_menu(layout, "Projekt Frame Rate")
        self.projekt_color_science = create_dropdown_menu(layout, "Projekt Color Science")
        self.projekt_start_frame = create_dropdown_menu(layout, "Projekt Start Frame")

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

        self.create_logik_projekt_button = create_button(layout, "Create LOGIK-PROJEKT", "#014400", self.create_logik_projekt)
        self.create_projekt_template_button = create_button(layout, "Create PROJEKT Template", "#864B00", self.create_projekt_template)
        self.cancel_button = create_button(layout, "Cancel", "#630000", self.cancel)

        self.projekt_serial_number.textChanged.connect(self.update_summary)
        self.projekt_client_name.textChanged.connect(self.update_summary)
        self.projekt_campaign_name.textChanged.connect(self.update_summary)
        self.projekt_resolution.currentTextChanged.connect(self.update_summary)
        self.projekt_bit_depth.currentTextChanged.connect(self.update_summary)
        self.projekt_frame_rate.currentTextChanged.connect(self.update_summary)
        self.projekt_color_science.currentTextChanged.connect(self.update_summary)
        self.projekt_start_frame.currentTextChanged.connect(self.update_summary)

        load_resolutions(self.projekt_resolution)

        default_index = self.projekt_resolution.findText("1920 x 1080 | HD 1080 16:9")
        self.projekt_resolution.setCurrentIndex(default_index)
        self.update_summary()
        self.update_summary()
    
    def center(self):
        frame_geometry = self.frameGeometry()
        screen_center = QApplication.primaryScreen().availableGeometry().center()
        frame_geometry.moveCenter(screen_center)
        self.move(frame_geometry.topLeft())

    def update_summary(self):
        index = self.projekt_resolution.currentIndex()
        item_data = self.projekt_resolution.itemData(index)

        if item_data is None:
            return

        resolution_name = self.projekt_resolution.currentText()
        projekt_width = item_data.get("width", 0)
        projekt_height = item_data.get("height", 0)
        projekt_aspect = item_data.get("display_aspect_ratio", 0)

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
        pass

    def create_projekt_template(self):
        pass

    def cancel(self):
        QApplication.quit()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = LogikProjektMainWindow()
    window.show()
    sys.exit(app.exec())
