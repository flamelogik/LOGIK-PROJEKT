from PySide6.QtWidgets import QLineEdit

def create_serial_number_qt6():
    line_edit = QLineEdit()
    line_edit.setPlaceholderText("Enter a Serial Number (Optional)...")
    return line_edit

def create_client_name_qt6():
    line_edit = QLineEdit()
    line_edit.setPlaceholderText("Enter the Client Name...")
    return line_edit

def create_campaign_name_qt6():
    line_edit = QLineEdit()
    line_edit.setPlaceholderText("Enter the Campaign Name...")
    return line_edit

def create_projekt_nickname_qt6():
    line_edit = QLineEdit()
    line_edit.setPlaceholderText("This value will be dynamically calculated...")
    return line_edit
