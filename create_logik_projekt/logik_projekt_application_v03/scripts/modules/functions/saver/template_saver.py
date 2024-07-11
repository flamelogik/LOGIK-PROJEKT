# import json
# from PySide6.QtWidgets import QFileDialog, QMessageBox

# def projekt_template_saver_qt6(parent, summary_text):
#     # Prompt the user for the save destination
#     file_dialog = QFileDialog(parent)
#     file_dialog.setAcceptMode(QFileDialog.AcceptSave)
#     file_dialog.setNameFilter("JSON Files (*.json)")
#     file_dialog.setDefaultSuffix("json")
    
#     if file_dialog.exec():
#         template_save_destination = file_dialog.selectedFiles()[0]
        
#         # Save the summary_text to the selected file
#         try:
#             with open(template_save_destination, 'w') as file:
#                 json.dump({"summary": summary_text}, file, indent=4)
#             QMessageBox.information(parent, "Success", "Template saved successfully.")
#         except Exception as e:
#             QMessageBox.critical(parent, "Error", f"Failed to save template: {e}")










# import json
# import datetime
# from PySide6.QtWidgets import QFileDialog, QMessageBox

# def projekt_template_saver_qt6(parent, summary_text, projekt_nickname):
#     # Get the current date and time
#     current_time = datetime.datetime.now().strftime("%Y_%m_%d-%H_%M")
    
#     # Clean the projekt_nickname to be filesystem-friendly
#     projekt_nickname = ''.join(c if c.isalnum() or c in (' ', '-') else '_' for c in projekt_nickname)
#     projekt_nickname = projekt_nickname.replace(' ', '_')
    
#     # Generate the default filename
#     default_filename = f"projekt_template-{current_time}-{projekt_nickname}.json"

#     # Prompt the user for the save destination with the default filename
#     file_dialog = QFileDialog(parent)
#     file_dialog.setAcceptMode(QFileDialog.AcceptSave)
#     file_dialog.setNameFilter("JSON Files (*.json)")
#     file_dialog.selectFile(default_filename)
    
#     if file_dialog.exec():
#         template_save_destination = file_dialog.selectedFiles()[0]
        
#         # Save the summary_text to the selected file
#         try:
#             with open(template_save_destination, 'w') as file:
#                 json.dump({"summary": summary_text}, file, indent=4)
#             QMessageBox.information(parent, "Success", "Template saved successfully.")
#         except Exception as e:
#             QMessageBox.critical(parent, "Error", f"Failed to save template: {e}")



















import json
import datetime
from PySide6.QtWidgets import QFileDialog, QMessageBox

def projekt_template_saver_qt6(parent, summary_text, projekt_nickname):
    # Get the current date and time
    current_time = datetime.datetime.now().strftime("%Y_%m_%d-%H_%M")
    
    # Clean the projekt_nickname to be filesystem-friendly
    projekt_nickname = ''.join(c if c.isalnum() or c in (' ', '-') else '_' for c in projekt_nickname)
    projekt_nickname = projekt_nickname.replace(' ', '_')
    
    # Generate the default filename
    default_filename = f"projekt_template-{current_time}-{projekt_nickname}.json"

    # Prompt the user for the save destination with the default filename
    file_dialog = QFileDialog(parent)
    file_dialog.setAcceptMode(QFileDialog.AcceptSave)
    file_dialog.setNameFilter("JSON Files (*.json)")
    file_dialog.selectFile(default_filename)
    
    if file_dialog.exec():
        template_save_destination = file_dialog.selectedFiles()[0]
        
        # Process the summary_text into a JSON structure
        summary_lines = summary_text.split('\n')
        summary_dict = {}
        for line in summary_lines:
            if ': ' in line:
                key, value = line.split(': ', 1)
                summary_dict[key] = value

        # Create the final JSON structure
        json_data = {
            "summary": projekt_nickname,
            "items": [summary_dict]
        }

        # Save the JSON structure to the selected file
        try:
            with open(template_save_destination, 'w') as file:
                json.dump(json_data, file, indent=4)
            QMessageBox.information(parent, "Success", "Template saved successfully.")
        except Exception as e:
            QMessageBox.critical(parent, "Error", f"Failed to save template: {e}")
