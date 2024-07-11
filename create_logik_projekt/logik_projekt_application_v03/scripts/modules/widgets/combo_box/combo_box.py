# from PySide6.QtWidgets import QComboBox

# class CustomComboBox(QComboBox):
#     def __init__(self, items, parent=None):
#         super().__init__(parent)
#         self.addItems(items)
#         # Additional initialization



from PySide6.QtWidgets import QComboBox
from ...functions.string_utilities.string_utilities import validate_string

class CustomComboBox(QComboBox):
    def __init__(self, items, parent=None):
        super().__init__(parent)
        self.addItems(items)
        self.currentTextChanged.connect(self.handle_text_change)

    def handle_text_change(self, text):
        if validate_string(text, r'^[A-Za-z0-9_]+$'):
            print(f"Valid text: {text}")
        else:
            print(f"Invalid text: {text}")
