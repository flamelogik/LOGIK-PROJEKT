# # from PySide6.QtWidgets import QComboBox
# # from ...functions.loader.file_loader import load_json
# # import os

# # class ComboBoxResolution(QComboBox):
# #     def __init__(self, json_file_path, parent=None):
# #         super().__init__(parent)
# #         self.json_file_path = json_file_path
# #         self.projekt_resolution = None
# #         self.load_items()
# #         self.currentIndexChanged.connect(self.update_projekt_resolution)

# #     def load_items(self):
# #         data = load_json(self.json_file_path)
# #         default_value = "1920 x 1080 | HD 1080 16:9"
# #         default_index = -1
# #         index = 0  # Initialize index counter
# #         for group in data['items']:
# #             if 'separator' in group:
# #                 separator_name = group['separator_name']
# #                 self.addItem(separator_name)  # Add separator name
# #                 index += 1  # Increment index counter for separators
# #             for item in group['items']:
# #                 self.addItem(item['name'], item['value_data'])  # Add item name and value
# #                 if item['value_data'] == default_value:
# #                     default_index = index
# #                 index += 1  # Increment index counter for items
# #         if default_index != -1:
# #             self.setCurrentIndex(default_index)

# #     def update_projekt_resolution(self, index):
# #         self.projekt_resolution = self.itemData(index)
# #         print(f"Selected Bit Depth: {self.projekt_resolution}")

# # def create_combo_box_resolution_qt6(parent=None):
# #     json_file_path = os.path.join(
# #         os.path.dirname(__file__),
# #         '../../../../config/json/projekt_parameters/projekt_resolution-broadcast.json'
# #     )
# #     return ComboBoxResolution(json_file_path, parent)










# from PySide6.QtWidgets import QComboBox
# from ...functions.loader.file_loader import load_json
# import os

# class ComboBoxResolution(QComboBox):
#     def __init__(self, json_file_path, parent=None):
#         super().__init__(parent)
#         self.json_file_path = json_file_path
#         self.projekt_resolution = None
#         self.projekt_width = None
#         self.projekt_height = None
#         self.projekt_sar = None
#         self.projekt_dar = None
#         self.projekt_par = None
#         self.projekt_aspect_ratio = None
#         self.load_items()
#         self.currentIndexChanged.connect(self.update_projekt_resolution)

#     def load_items(self):
#         data = load_json(self.json_file_path)
#         default_value = "1920 x 1080 | HD 1080 16:9"
#         default_index = -1
#         index = 0  # Initialize index counter
#         for group in data['items']:
#             if 'separator' in group:
#                 separator_name = group['separator_name']
#                 self.addItem(separator_name)  # Add separator name
#                 index += 1  # Increment index counter for separators
#             for item in group['items']:
#                 self.addItem(item['name'], item['value_data'])  # Add item name and value
#                 if item['value_data'] == default_value:
#                     default_index = index
#                 index += 1  # Increment index counter for items
#         if default_index != -1:
#             self.setCurrentIndex(default_index)

#     def update_projekt_resolution(self, index):
#         self.projekt_resolution = self.itemData(index)
#         if self.projekt_resolution:
#             self.projekt_width = self.projekt_resolution['width']
#             self.projekt_height = self.projekt_resolution['height']
#             self.projekt_sar = self.projekt_resolution['storage_aspect_ratio']
#             self.projekt_dar = self.projekt_resolution['display_aspect_ratio']
#             self.projekt_par = self.projekt_resolution['pixel_aspect_ratio']
#             self.projekt_aspect_ratio = self.projekt_sar * self.projekt_par
#             self.print_projekt_details()

#     def print_projekt_details(self):
#         print(f"Selected Resolution: {self.projekt_resolution['name']}")
#         print(f"Width: {self.projekt_width}")
#         print(f"Height: {self.projekt_height}")
#         print(f"Storage Aspect Ratio: {self.projekt_sar}")
#         print(f"Display Aspect Ratio: {self.projekt_dar}")
#         print(f"Pixel Aspect Ratio: {self.projekt_par}")
#         print(f"Calculated Project Aspect Ratio: {self.projekt_aspect_ratio}")

# def create_combo_box_resolution_qt6(parent=None):
#     json_file_path = os.path.join(
#         os.path.dirname(__file__),
#         '../../../../config/json/projekt_parameters/projekt_resolution-broadcast.json'
#     )
#     return ComboBoxResolution(json_file_path, parent)








from PySide6.QtWidgets import QComboBox
from ...functions.loader.file_loader import load_json
import os

class ComboBoxResolution(QComboBox):
    def __init__(self, json_file_path, parent=None):
        super().__init__(parent)
        self.json_file_path = json_file_path
        self.projekt_resolution = None
        self.projekt_width = None
        self.projekt_height = None
        self.projekt_sar = None
        self.projekt_dar = None
        self.projekt_par = None
        self.projekt_aspect_ratio = None
        self.load_items()
        self.currentIndexChanged.connect(self.update_projekt_resolution)

    def load_items(self):
        data = load_json(self.json_file_path)
        default_value = "1920 x 1080 | HD 1080 16:9"
        default_index = -1
        index = 0  # Initialize index counter
        for group in data['items']:
            if 'separator' in group:
                separator_name = group['separator_name']
                self.addItem(separator_name)  # Add separator name
                index += 1  # Increment index counter for separators
            for item in group['items']:
                self.addItem(item['name'], item['value_data'])  # Add item name and value
                if item['name'] == default_value:
                    default_index = index
                index += 1  # Increment index counter for items
        if default_index != -1:
            self.setCurrentIndex(default_index)

    def update_projekt_resolution(self, index):
        self.projekt_resolution = self.itemData(index)
        if self.projekt_resolution:
            self.projekt_width = self.projekt_resolution['width']
            self.projekt_height = self.projekt_resolution['height']
            self.projekt_sar = self.projekt_resolution['storage_aspect_ratio']
            self.projekt_dar = self.projekt_resolution['display_aspect_ratio']
            self.projekt_par = self.projekt_resolution['pixel_aspect_ratio']
            self.projekt_aspect_ratio = self.projekt_sar * self.projekt_par
            self.print_projekt_details()

    def print_projekt_details(self):
        print(f"Selected Resolution: {self.projekt_resolution['name']}")
        print(f"Width: {self.projekt_width}")
        print(f"Height: {self.projekt_height}")
        print(f"Storage Aspect Ratio: {self.projekt_sar}")
        print(f"Display Aspect Ratio: {self.projekt_dar}")
        print(f"Pixel Aspect Ratio: {self.projekt_par}")
        print(f"Calculated Project Aspect Ratio: {self.projekt_aspect_ratio}")

def create_combo_box_resolution_qt6(parent=None):
    json_file_path = os.path.join(
        os.path.dirname(__file__),
        '../../../../config/json/projekt_parameters/projekt_resolution-broadcast.json'
    )
    return ComboBoxResolution(json_file_path, parent)
