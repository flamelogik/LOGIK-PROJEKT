# from PySide6.QtWidgets import QComboBox
# from ...functions.loader.file_loader import load_json
# import os

# class ComboBoxStartFrame(QComboBox):
#     def __init__(self, json_file_path, parent=None):
#         super().__init__(parent)
#         self.json_file_path = json_file_path
#         self.projekt_start_frame = None
#         self.load_items()
#         self.currentIndexChanged.connect(self.update_projekt_start_frame)

#     def load_items(self):
#         data = load_json(self.json_file_path)
#         for item in data['items'][0]['items']:
#             self.addItem(item['name'], item['value_data'])

#     def update_projekt_start_frame(self, index):
#         self.projekt_start_frame = self.itemData(index)
#         print(f"Selected Start Frame: {self.projekt_start_frame}")

# def create_combo_box_start_frame_qt6(parent=None):
#     json_file_path = os.path.join(
#         os.path.dirname(__file__),
#         '../../../../config/json/projekt_parameters/projekt_start_frame.json'
#     )
#     return ComboBoxStartFrame(json_file_path, parent)













from PySide6.QtWidgets import QComboBox
from ...functions.loader.file_loader import load_json
import os

class ComboBoxStartFrame(QComboBox):
    def __init__(self, json_file_path, parent=None):
        super().__init__(parent)
        self.json_file_path = json_file_path
        self.projekt_start_frame = None
        self.load_items()
        self.currentIndexChanged.connect(self.update_projekt_start_frame)

    def load_items(self):
        data = load_json(self.json_file_path)
        default_value = "1001"
        default_index = -1
        index = 0  # Initialize index counter
        for group in data['items']:
            if 'separator' in group:
                separator_name = group['separator_name']
                self.addItem(separator_name)  # Add separator name
                index += 1  # Increment index counter for separators
            for item in group['items']:
                self.addItem(item['name'], item['value_data'])  # Add item name and value
                if item['value_data'] == default_value:
                    default_index = index
                index += 1  # Increment index counter for items
        if default_index != -1:
            self.setCurrentIndex(default_index)

    def update_projekt_start_frame(self, index):
        self.projekt_start_frame = self.itemData(index)
        print(f"Selected Start Frame: {self.projekt_start_frame}")

def create_combo_box_start_frame_qt6(parent=None):
    json_file_path = os.path.join(
        os.path.dirname(__file__),
        '../../../../config/json/projekt_parameters/projekt_start_frame.json'
    )
    return ComboBoxStartFrame(json_file_path, parent)
