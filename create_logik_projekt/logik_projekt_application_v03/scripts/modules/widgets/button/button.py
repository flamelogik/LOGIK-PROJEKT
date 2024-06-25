# from PySide6.QtWidgets import QPushButton

# class CustomButton(QPushButton):
#     def __init__(self, text, parent=None):
#         super().__init__(text, parent)
#         # Additional initialization




# from PySide6.QtWidgets import QPushButton, QMessageBox
# from ...functions.loader.file_loader import file_loader
# from ...functions.saver.file_saver import file_saver

# class CustomButton(QPushButton):
#     def __init__(self, text, parent=None):
#         super().__init__(text, parent)
#         self.setText(text)
#         self.clicked.connect(self.handle_click)

#     def handle_click(self):
#         try:
#             data = file_loader.load_file('example_template.json')
#             QMessageBox.information(self, "Info", f"Loaded data: {data}")

#             # Modify data as needed
#             file_saver.save_file('example_config_bak.json', data)
#             QMessageBox.information(self, "Info", "File saved successfully")

#         except Exception as e:
#             QMessageBox.critical(self, "Error", str(e))









from PySide6.QtWidgets import QPushButton

class CustomButton(QPushButton):
    def __init__(self, text, parent=None):
        super().__init__(text, parent)
        self.clicked.connect(self.on_click)

    def on_click(self):
        print(f"Button {self.text()} clicked")


# Create a new script called 'logik_projekt_application/scripts/modules/widgets/button/button_load_template.py'.
# Add a function called 'load_logik_projekt_template_qt6'.
# When the button is pressed open a file browser so that the user can choose a logik projekt template