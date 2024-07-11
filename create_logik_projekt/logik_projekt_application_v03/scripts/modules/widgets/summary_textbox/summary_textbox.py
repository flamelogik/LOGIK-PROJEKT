# from PySide6.QtWidgets import QTextEdit

# class SummaryTextBox(QTextEdit):
#     def __init__(self, parent=None):
#         super().__init__(parent)
#         self.setObjectName("SummaryTextBox")
#         self.setReadOnly(True)
#         # self.setPlaceholderText("Summary information will be displayed here.")

#     def set_summary(self, summary_text):
#         self.setText(summary_text)









# from PySide6.QtWidgets import QTextEdit
# from PySide6.QtCore import Signal

# class SummaryTextBox(QTextEdit):
#     # Custom signal declaration
#     update_summary = Signal(str)

#     def __init__(self, parent=None):
#         super().__init__(parent)
#         self.setObjectName("SummaryTextBox")
#         self.setReadOnly(True)
#         # self.setPlaceholderText("Summary information will be displayed here.")

#     def set_summary(self, summary_text):
#         self.setText(summary_text)
#         # Emit the update_summary signal with the new summary_text
#         self.update_summary.emit(summary_text)













# from PySide6.QtWidgets import QTextEdit
# from PySide6.QtCore import Signal

# class SummaryTextBox(QTextEdit):
#     # Custom signal declaration
#     update_summary = Signal(str)

#     def __init__(self, parent=None):
#         super().__init__(parent)
#         self.setObjectName("summary_textbox")  # Set object name for easy finding
#         self.setReadOnly(True)

#     def set_summary(self, summary_text):
#         self.setText(summary_text)
#         # Emit the update_summary signal with the new summary_text
#         self.update_summary.emit(summary_text)














# from PySide6.QtWidgets import QTextEdit
# from PySide6.QtCore import Signal

# class SummaryTextBox(QTextEdit):
#     # Custom signal declaration
#     update_summary = Signal(str)

#     def __init__(self, parent=None):
#         super().__init__(parent)
#         self.setObjectName("summary_textbox")  # Set object name for easy finding
#         self.setReadOnly(True)

#     def set_summary(self, summary_text):
#         self.setText(summary_text)
#         # Emit the update_summary signal with the new summary_text
#         self.update_summary.emit(summary_text)














# from PySide6.QtWidgets import QTextEdit

# def string_clean(string):

#     string = string.lower()
#     string = ''.join(
#         character 
#         if character.islower() 
#         or character.isdigit() 
#         or character == '_' 
#         or character.isspace() 
#         else '_' for character in string)
#     string = string.replace(' ', '_')
#     string = '_'.join(filter(None, string.split('_')))
#     string = string.strip('_')

#     return string

# local_stylesheet = """
# /* Summary box (QTextEdit) */
# QTextEdit {
#     background-color: #37414b;  /* Replace with your desired color */
#     color: #ffffff;  /* Text color */
#     font: 14px "Discreet";  /* Font */
#     border: 1px solid #007acc;  /* Border */
#     border-radius: 0px;  /* No rounded corners */
# }
# """

# def create_summary_textbox_qt6():
#     textbox = QTextEdit()
#     textbox.setReadOnly(True)  # Make it read-only
#     textbox.setStyleSheet(local_stylesheet)  # Apply the local stylesheet
#     return textbox

# def update_summary_textbox_qt6(textbox, lineedits, combo_boxes):
#     summary_text = ""
#     for label, lineedit in lineedits.items():
#         summary_text += f"{label} {string_clean(lineedit.text())}\n"
#     for label, combo_box in combo_boxes.items():
#         summary_text += f"{label} {combo_box.currentText()}\n"
#     textbox.setPlainText(summary_text)


















from PySide6.QtWidgets import QTextEdit

def string_clean(string):
    string = string.lower()
    string = ''.join(
        character 
        if character.islower() 
        or character.isdigit() 
        or character == '_' 
        or character.isspace() 
        else '_' for character in string)
    string = string.replace(' ', '_')
    string = '_'.join(filter(None, string.split('_')))
    string = string.strip('_')

    return string

local_stylesheet = """
/* Summary box (QTextEdit) */
QTextEdit {
    background-color: #37414b;  /* Replace with your desired color */
    color: #ffffff;  /* Text color */
    font: 14px "Discreet";  /* Font */
    border: 1px solid #007acc;  /* Border */
    border-radius: 0px;  /* No rounded corners */
}
"""

def create_summary_textbox_qt6():
    textbox = QTextEdit()
    textbox.setReadOnly(True)  # Make it read-only
    textbox.setStyleSheet(local_stylesheet)  # Apply the local stylesheet
    return textbox

def update_summary_textbox_qt6(textbox, lineedits, combo_boxes, excluded_labels=None):
    if excluded_labels is None:
        excluded_labels = []

    summary_text = ""
    for label, lineedit in lineedits.items():
        summary_text += f"{label} {string_clean(lineedit.text())}\n"
    for label, combo_box in combo_boxes.items():
        if label not in excluded_labels:
            summary_text += f"{label} {combo_box.currentText()}\n"
    textbox.setPlainText(summary_text)
