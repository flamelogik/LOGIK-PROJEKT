import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QLabel, QTextEdit, QVBoxLayout, QWidget
from modules.functions.list_flame_family_software import list_flame_family_software, latest_flame_version, sanitize_latest_flame_version_name

class LogikProjektEnvironmentGUI(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Logik Projekt Environment GUI")

        # Set up the main widget and layout
        main_widget = QWidget()
        main_layout = QVBoxLayout()

        # Environment Info label and text box
        self.env_info_label = QLabel("Environment Info:")
        self.environment_info = QTextEdit()
        self.environment_info.setReadOnly(True)
        main_layout.addWidget(self.env_info_label)
        main_layout.addWidget(self.environment_info)

        # Latest Flame Version label and text box
        self.latest_flame_version_label = QLabel("Latest Flame Version:")
        self.latest_flame_version_text = QTextEdit()
        self.latest_flame_version_text.setReadOnly(True)
        main_layout.addWidget(self.latest_flame_version_label)
        main_layout.addWidget(self.latest_flame_version_text)

        # Latest Sanitized Flame Version label and text box
        self.latest_sanitized_flame_version_label = QLabel("Latest Sanitized Flame Version:")
        self.latest_sanitized_flame_version_text = QTextEdit()
        self.latest_sanitized_flame_version_text.setReadOnly(True)
        main_layout.addWidget(self.latest_sanitized_flame_version_label)
        main_layout.addWidget(self.latest_sanitized_flame_version_text)

        # Set the main layout to the central widget
        main_widget.setLayout(main_layout)
        self.setCentralWidget(main_widget)

        # Populate the text boxes
        self.populate_text_boxes()

    def populate_text_boxes(self):
        directory_path = "/opt/Autodesk"

        # Populate environment info text box
        flame_dirs = list_flame_family_software(directory_path)
        if flame_dirs:
            self.environment_info.append("Sorted flame_ directories:")
            for dir_name in flame_dirs:
                self.environment_info.append(dir_name)

        # Populate latest flame version text box
        latest_version = latest_flame_version(directory_path)
        if latest_version:
            self.latest_flame_version_text.append(latest_version)

        # Populate latest sanitized flame version text box
        sanitized_version = sanitize_latest_flame_version_name(latest_version)
        if sanitized_version:
            self.latest_sanitized_flame_version_text.append(sanitized_version)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = LogikProjektEnvironmentGUI()
    window.show()
    sys.exit(app.exec())
