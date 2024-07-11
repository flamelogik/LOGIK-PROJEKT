from PySide6.QtWidgets import QComboBox

class CustomDropDown(QComboBox):
    def __init__(self, items=None, parent=None):
        super().__init__(parent)
        if items:
            self.addItems(items)
        self.currentIndexChanged.connect(self.handle_index_change)

    def handle_index_change(self, index):
        print(f"Selected index: {index}, value: {self.itemText(index)}")
