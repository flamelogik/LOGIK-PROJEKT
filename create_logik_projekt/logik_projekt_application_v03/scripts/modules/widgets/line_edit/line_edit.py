# from PySide6.QtWidgets import QLineEdit

# class CustomLineEdit(QLineEdit):
#     def __init__(self, parent=None):
#         super().__init__(parent)
#         # Additional initialization




from PySide6.QtWidgets import QLineEdit
from ...functions.string_utilities.string_utilities import to_snake_case

class CustomLineEdit(QLineEdit):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.textChanged.connect(self.handle_text_change)

    def handle_text_change(self, text):
        snake_case_text = to_snake_case(text)
        print(f"Converted to snake_case: {snake_case_text}")
