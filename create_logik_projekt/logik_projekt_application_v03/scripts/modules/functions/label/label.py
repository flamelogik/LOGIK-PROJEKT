from PySide6.QtWidgets import QLabel
from PySide6.QtCore import Qt

def create_label_qt6(text):
    label = QLabel(text)
    label.setFixedSize(128, 28)
    label.setAlignment(Qt.AlignRight | Qt.AlignVCenter)
    return label
