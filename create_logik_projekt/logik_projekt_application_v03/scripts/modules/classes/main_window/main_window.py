# from PySide6.QtWidgets import QMainWindow, QVBoxLayout, QWidget
# from PySide6.QtGui import QAction
# from .button.button import CustomButton
# from .combo_box.combo_box import CustomComboBox
# from .line_edit.line_edit import CustomLineEdit

# class MainWindow(QMainWindow):
#     def __init__(self):
#         super().__init__()
#         self.setWindowTitle("Logik Projekt Application")
#         self.setGeometry(100, 100, 800, 600)
        
#         self.initUI()
    
#     def initUI(self):
#         central_widget = QWidget()
#         layout = QVBoxLayout()

#         # Add custom widgets to layout
#         layout.addWidget(CustomButton("Click Me"))
#         layout.addWidget(CustomComboBox(["Option 1", "Option 2", "Option 3"]))
#         layout.addWidget(CustomLineEdit())

#         central_widget.setLayout(layout)
#         self.setCentralWidget(central_widget)

#         # Create menu actions
#         load_action = QAction("&Load Config", self)
#         load_action.triggered.connect(self.load_config)

#         save_action = QAction("&Save Config", self)
#         save_action.triggered.connect(self.save_config)

#         # Add actions to menu
#         menubar = self.menuBar()
#         file_menu = menubar.addMenu("&File")
#         file_menu.addAction(load_action)
#         file_menu.addAction(save_action)

#     def load_config(self):
#         file_name, _ = QFileDialog.getOpenFileName(self, "Open Config File", "", "JSON Files (*.json)")
#         if file_name:
#             # Load config logic
#             QMessageBox.information(self, "Info", f"Loaded config: {file_name}")

#     def save_config(self):
#         file_name, _ = QFileDialog.getSaveFileName(self, "Save Config File", "", "JSON Files (*.json)")
#         if file_name:
#             # Save config logic
#             QMessageBox.information(self, "Info", f"Saved config: {file_name}")










# from PySide6.QtWidgets import QMainWindow, QVBoxLayout, QWidget, QFileDialog, QMessageBox, QComboBox
# from PySide6.QtGui import QAction
# from .button.button import CustomButton
# from .combo_box.combo_box import CustomComboBox
# from .line_edit.line_edit import CustomLineEdit
# from .drop_down.drop_down import CustomDropDown
# from .style_sheet.style_sheet import apply_style_sheet

# class MainWindow(QMainWindow):
#     def __init__(self):
#         super().__init__()
#         self.setWindowTitle("Logik Projekt Application")
#         self.setGeometry(100, 100, 800, 600)
        
#         self.initUI()
#         self.apply_styles()

#     def initUI(self):
#         central_widget = QWidget()
#         layout = QVBoxLayout()

#         # Add custom widgets to layout
#         layout.addWidget(CustomButton("Click Me"))
#         layout.addWidget(CustomComboBox(["Option 1", "Option 2", "Option 3"]))
#         layout.addWidget(CustomLineEdit())
#         layout.addWidget(CustomDropDown(["Choice 1", "Choice 2", "Choice 3"]))

#         central_widget.setLayout(layout)
#         self.setCentralWidget(central_widget)

#         # Create menu actions
#         load_action = QAction("&Load Config", self)
#         load_action.triggered.connect(self.load_config)

#         save_action = QAction("&Save Config", self)
#         save_action.triggered.connect(self.save_config)

#         # Add actions to menu
#         menubar = self.menuBar()
#         file_menu = menubar.addMenu("&File")
#         file_menu.addAction(load_action)
#         file_menu.addAction(save_action)

#     def load_config(self):
#         file_name, _ = QFileDialog.getOpenFileName(self, "Open Config File", "", "JSON Files (*.json)")
#         if file_name:
#             # Load config logic
#             QMessageBox.information(self, "Info", f"Loaded config: {file_name}")

#     def save_config(self):
#         file_name, _ = QFileDialog.getSaveFileName(self, "Save Config File", "", "JSON Files (*.json)")
#         if file_name:
#             # Save config logic
#             QMessageBox.information(self, "Info", f"Saved config: {file_name}")

#     def apply_styles(self):
#         try:
#             apply_style_sheet(self, 'default_style.qss')
#         except Exception as e:
#             QMessageBox.critical(self, "Error", str(e))










# from PySide6.QtWidgets import QMainWindow, QVBoxLayout, QWidget, QFileDialog, QMessageBox
# from PySide6.QtGui import QAction
# from ...widgets.button.button import CustomButton
# from ...widgets.combo_box.combo_box import CustomComboBox
# from ...widgets.line_edit.line_edit import CustomLineEdit
# from ...widgets.drop_down.drop_down import CustomDropDown
# from ...widgets.summary_textbox.summary_textbox import SummaryTextBox
# from ...widgets.style_sheet.style_sheet import apply_style_sheet

# class MainWindow(QMainWindow):
#     def __init__(self):
#         super().__init__()
#         self.setWindowTitle("Logik Projekt Application")
#         self.setGeometry(100, 100, 800, 600)
        
#         self.initUI()
#         self.apply_styles()

#     def initUI(self):
#         central_widget = QWidget()
#         layout = QVBoxLayout()

#         # Add custom widgets to layout
#         layout.addWidget(CustomButton("Click Me"))
#         layout.addWidget(CustomComboBox(["Option 1", "Option 2", "Option 3"]))
#         layout.addWidget(CustomLineEdit())
#         layout.addWidget(CustomDropDown(["Choice 1", "Choice 2", "Choice 3"]))
#         layout.addWidget(SummaryTextBox())

#         central_widget.setLayout(layout)
#         self.setCentralWidget(central_widget)

#         # Create menu actions
#         load_action = QAction("&Load Config", self)
#         load_action.triggered.connect(self.load_config)

#         save_action = QAction("&Save Config", self)
#         save_action.triggered.connect(self.save_config)

#         # Add actions to menu
#         menubar = self.menuBar()
#         file_menu = menubar.addMenu("&File")
#         file_menu.addAction(load_action)
#         file_menu.addAction(save_action)

#     def load_config(self):
#         file_name, _ = QFileDialog.getOpenFileName(self, "Open Config File", "", "JSON Files (*.json)")
#         if file_name:
#             # Load config logic
#             QMessageBox.information(self, "Info", f"Loaded config: {file_name}")

#     def save_config(self):
#         file_name, _ = QFileDialog.getSaveFileName(self, "Save Config File", "", "JSON Files (*.json)")
#         if file_name:
#             # Save config logic
#             QMessageBox.information(self, "Info", f"Saved config: {file_name}")

#     def apply_styles(self):
#         try:
#             apply_style_sheet(self, 'default_style.qss')
#         except Exception as e:
#             QMessageBox.critical(self, "Error", str(e))








# from PySide6.QtWidgets import QMainWindow, QVBoxLayout, QWidget, QFileDialog, QMessageBox
# from PySide6.QtGui import QAction
# from ...widgets.button.button import CustomButton
# from ...widgets.combo_box.combo_box import CustomComboBox
# from ...widgets.combo_box.combo_box_start_frame import create_combo_box_start_frame_qt6
# from ...widgets.line_edit.line_edit import CustomLineEdit
# from ...widgets.drop_down.drop_down import CustomDropDown
# from ...widgets.summary_textbox.summary_textbox import SummaryTextBox
# from ...widgets.style_sheet.style_sheet import apply_style_sheet

# class MainWindow(QMainWindow):
#     def __init__(self):
#         super().__init__()
#         self.setWindowTitle("Logik Projekt Application")
#         self.setGeometry(100, 100, 800, 600)
        
#         self.initUI()
#         self.apply_styles()

#     def initUI(self):
#         central_widget = QWidget()
#         layout = QVBoxLayout()

#         # Add custom widgets to layout
#         layout.addWidget(CustomButton("Click Me"))
#         layout.addWidget(CustomComboBox(["Option 1", "Option 2", "Option 3"]))
#         layout.addWidget(create_combo_box_start_frame_qt6())
#         layout.addWidget(CustomLineEdit())
#         layout.addWidget(CustomDropDown(["Choice 1", "Choice 2", "Choice 3"]))
#         layout.addWidget(SummaryTextBox())

#         central_widget.setLayout(layout)
#         self.setCentralWidget(central_widget)

#         # Create menu actions
#         load_action = QAction("&Load Config", self)
#         load_action.triggered.connect(self.load_config)

#         save_action = QAction("&Save Config", self)
#         save_action.triggered.connect(self.save_config)

#         # Add actions to menu
#         menubar = self.menuBar()
#         file_menu = menubar.addMenu("&File")
#         file_menu.addAction(load_action)
#         file_menu.addAction(save_action)

#     def load_config(self):
#         file_name, _ = QFileDialog.getOpenFileName(self, "Open Config File", "", "JSON Files (*.json)")
#         if file_name:
#             # Load config logic
#             QMessageBox.information(self, "Info", f"Loaded config: {file_name}")

#     def save_config(self):
#         file_name, _ = QFileDialog.getSaveFileName(self, "Save Config File", "", "JSON Files (*.json)")
#         if file_name:
#             # Save config logic
#             QMessageBox.information(self, "Info", f"Saved config: {file_name}")

#     def apply_styles(self):
#         try:
#             apply_style_sheet(self, 'default_style.qss')
#         except Exception as e:
#             QMessageBox.critical(self, "Error", str(e))
















# from PySide6.QtWidgets import QMainWindow, QVBoxLayout, QWidget, QFileDialog, QMessageBox
# from PySide6.QtGui import QAction
# from ...widgets.button.button import CustomButton
# from ...widgets.combo_box.combo_box import CustomComboBox
# from ...widgets.combo_box.combo_box_start_frame import create_combo_box_start_frame_qt6
# from ...widgets.line_edit.line_edit import CustomLineEdit
# from ...widgets.drop_down.drop_down import CustomDropDown
# from ...widgets.summary_textbox.summary_textbox import SummaryTextBox
# from ...widgets.style_sheet.logik_stylesheet import stylesheet  # Updated import

# class MainWindow(QMainWindow):
#     def __init__(self):
#         super().__init__()
#         self.setWindowTitle("Logik Projekt Application")
#         self.setGeometry(100, 100, 800, 600)
        
#         self.initUI()
#         self.apply_styles()

#     def initUI(self):
#         central_widget = QWidget()
#         layout = QVBoxLayout()

#         # Add custom widgets to layout
#         layout.addWidget(CustomButton("Click Me"))
#         layout.addWidget(CustomComboBox(["Option 1", "Option 2", "Option 3"]))
#         layout.addWidget(create_combo_box_start_frame_qt6())
#         layout.addWidget(CustomLineEdit())
#         layout.addWidget(CustomDropDown(["Choice 1", "Choice 2", "Choice 3"]))
#         layout.addWidget(SummaryTextBox())

#         central_widget.setLayout(layout)
#         self.setCentralWidget(central_widget)

#         # Create menu actions
#         load_action = QAction("&Load Config", self)
#         load_action.triggered.connect(self.load_config)

#         save_action = QAction("&Save Config", self)
#         save_action.triggered.connect(self.save_config)

#         # Add actions to menu
#         menubar = self.menuBar()
#         file_menu = menubar.addMenu("&File")
#         file_menu.addAction(load_action)
#         file_menu.addAction(save_action)

#     def load_config(self):
#         file_name, _ = QFileDialog.getOpenFileName(self, "Open Config File", "", "JSON Files (*.json)")
#         if file_name:
#             # Load config logic
#             QMessageBox.information(self, "Info", f"Loaded config: {file_name}")

#     def save_config(self):
#         file_name, _ = QFileDialog.getSaveFileName(self, "Save Config File", "", "JSON Files (*.json)")
#         if file_name:
#             # Save config logic
#             QMessageBox.information(self, "Info", f"Saved config: {file_name}")

#     def apply_styles(self):
#         try:
#             self.setStyleSheet(stylesheet)  # Apply the stylesheet
#         except Exception as e:
#             QMessageBox.critical(self, "Error", str(e))
















# from PySide6.QtWidgets import QMainWindow, QVBoxLayout, QWidget, QFileDialog, QMessageBox
# from PySide6.QtGui import QAction
# from ...widgets.button.button import CustomButton
# from ...widgets.combo_box.combo_box import CustomComboBox
# from ...widgets.combo_box.combo_box_start_frame import create_combo_box_start_frame_qt6
# from ...widgets.line_edit.line_edit import CustomLineEdit
# from ...widgets.drop_down.drop_down import CustomDropDown
# from ...widgets.summary_textbox.summary_textbox import SummaryTextBox
# from ...widgets.style_sheet.logik_stylesheet import stylesheet  # Updated import

# # Import the new line edit functions
# from ...widgets.line_edit.line_edit_projekt_namer import (
#     create_serial_number_qt6,
#     create_client_name_qt6,
#     create_campaign_name_qt6,
#     create_projekt_nickname_qt6
# )

# class MainWindow(QMainWindow):
#     def __init__(self):
#         super().__init__()
#         self.setWindowTitle("Logik Projekt Application")
#         self.setGeometry(100, 100, 800, 600)
        
#         self.initUI()
#         self.apply_styles()

#     def initUI(self):
#         central_widget = QWidget()
#         layout = QVBoxLayout()

#         # Add new line edit widgets as the first widgets
#         layout.addWidget(create_serial_number_qt6())
#         layout.addWidget(create_client_name_qt6())
#         layout.addWidget(create_campaign_name_qt6())
#         layout.addWidget(create_projekt_nickname_qt6())

#         # Add custom widgets to layout
#         layout.addWidget(CustomButton("Click Me"))
#         layout.addWidget(CustomComboBox(["Option 1", "Option 2", "Option 3"]))
#         layout.addWidget(create_combo_box_start_frame_qt6())
#         layout.addWidget(CustomLineEdit())
#         layout.addWidget(CustomDropDown(["Choice 1", "Choice 2", "Choice 3"]))
#         layout.addWidget(SummaryTextBox())

#         central_widget.setLayout(layout)
#         self.setCentralWidget(central_widget)

#         # Create menu actions
#         load_action = QAction("&Load Config", self)
#         load_action.triggered.connect(self.load_config)

#         save_action = QAction("&Save Config", self)
#         save_action.triggered.connect(self.save_config)

#         # Add actions to menu
#         menubar = self.menuBar()
#         file_menu = menubar.addMenu("&File")
#         file_menu.addAction(load_action)
#         file_menu.addAction(save_action)

#     def load_config(self):
#         file_name, _ = QFileDialog.getOpenFileName(self, "Open Config File", "", "JSON Files (*.json)")
#         if file_name:
#             # Load config logic
#             QMessageBox.information(self, "Info", f"Loaded config: {file_name}")

#     def save_config(self):
#         file_name, _ = QFileDialog.getSaveFileName(self, "Save Config File", "", "JSON Files (*.json)")
#         if file_name:
#             # Save config logic
#             QMessageBox.information(self, "Info", f"Saved config: {file_name}")

#     def apply_styles(self):
#         try:
#             self.setStyleSheet(stylesheet)  # Apply the stylesheet
#         except Exception as e:
#             QMessageBox.critical(self, "Error", str(e))












# from PySide6.QtWidgets import QMainWindow, QVBoxLayout, QHBoxLayout, QWidget, QFileDialog, QMessageBox
# from PySide6.QtGui import QAction
# from ...widgets.button.button import CustomButton
# from ...widgets.combo_box.combo_box import CustomComboBox
# from ...widgets.combo_box.combo_box_start_frame import create_combo_box_start_frame_qt6
# from ...widgets.line_edit.line_edit import CustomLineEdit
# from ...widgets.drop_down.drop_down import CustomDropDown
# from ...widgets.summary_textbox.summary_textbox import SummaryTextBox
# from ...widgets.style_sheet.logik_stylesheet import stylesheet

# # Import the new line edit functions
# from ...widgets.line_edit.line_edit_projekt_namer import (
#     create_serial_number_qt6,
#     create_client_name_qt6,
#     create_campaign_name_qt6,
#     create_projekt_nickname_qt6
# )

# # Import the label function
# from ...functions.label.label import create_label_qt6

# class MainWindow(QMainWindow):
#     def __init__(self):
#         super().__init__()
#         self.setWindowTitle("Logik Projekt Application")
#         self.setGeometry(100, 100, 800, 600)
        
#         self.initUI()
#         self.apply_styles()

#     def initUI(self):
#         central_widget = QWidget()
#         main_layout = QVBoxLayout()

#         # Create a function to add labeled widgets
#         def add_labeled_widget(label_text, widget):
#             layout = QHBoxLayout()
#             layout.addWidget(create_label_qt6(label_text))
#             layout.addWidget(widget)
#             main_layout.addLayout(layout)

#         # Add new line edit widgets with labels as the first widgets
#         add_labeled_widget("Serial Number:", create_serial_number_qt6())
#         add_labeled_widget("Client Name:", create_client_name_qt6())
#         add_labeled_widget("Campaign Name:", create_campaign_name_qt6())
#         add_labeled_widget("Projekt Nickname:", create_projekt_nickname_qt6())

#         # Add custom widgets to layout with labels
#         add_labeled_widget("Button:", CustomButton("Click Me"))
#         add_labeled_widget("Combo Box:", CustomComboBox(["Option 1", "Option 2", "Option 3"]))
#         add_labeled_widget("Start Frame:", create_combo_box_start_frame_qt6())
#         add_labeled_widget("Line Edit:", CustomLineEdit())
#         add_labeled_widget("Drop Down:", CustomDropDown(["Choice 1", "Choice 2", "Choice 3"]))
#         add_labeled_widget("Summary Text Box:", SummaryTextBox())

#         central_widget.setLayout(main_layout)
#         self.setCentralWidget(central_widget)

#         # Create menu actions
#         load_action = QAction("&Load Config", self)
#         load_action.triggered.connect(self.load_config)

#         save_action = QAction("&Save Config", self)
#         save_action.triggered.connect(self.save_config)

#         # Add actions to menu
#         menubar = self.menuBar()
#         file_menu = menubar.addMenu("&File")
#         file_menu.addAction(load_action)
#         file_menu.addAction(save_action)

#     def load_config(self):
#         file_name, _ = QFileDialog.getOpenFileName(self, "Open Config File", "", "JSON Files (*.json)")
#         if file_name:
#             # Load config logic
#             QMessageBox.information(self, "Info", f"Loaded config: {file_name}")

#     def save_config(self):
#         file_name, _ = QFileDialog.getSaveFileName(self, "Save Config File", "", "JSON Files (*.json)")
#         if file_name:
#             # Save config logic
#             QMessageBox.information(self, "Info", f"Saved config: {file_name}")

#     def apply_styles(self):
#         try:
#             self.setStyleSheet(stylesheet)  # Apply the stylesheet
#         except Exception as e:
#             QMessageBox.critical(self, "Error", str(e))












# from PySide6.QtWidgets import QMainWindow, QVBoxLayout, QHBoxLayout, QWidget, QFileDialog, QMessageBox
# from PySide6.QtGui import QAction
# from ...widgets.button.button import CustomButton
# from ...widgets.combo_box.combo_box import CustomComboBox
# from ...widgets.combo_box.combo_box_start_frame import create_combo_box_start_frame_qt6
# from ...widgets.line_edit.line_edit import CustomLineEdit
# from ...widgets.drop_down.drop_down import CustomDropDown
# from ...widgets.summary_textbox.summary_textbox import SummaryTextBox
# from ...widgets.style_sheet.logik_stylesheet import stylesheet

# # Import the new line edit functions
# from ...widgets.line_edit.line_edit_projekt_namer import (
#     create_serial_number_qt6,
#     create_client_name_qt6,
#     create_campaign_name_qt6,
#     create_projekt_nickname_qt6
# )

# # Import the label function
# from ...functions.label.label import create_label_qt6

# class MainWindow(QMainWindow):
#     def __init__(self):
#         super().__init__()
#         self.setWindowTitle("Logik Projekt Application")
#         self.setGeometry(100, 100, 1440, 960)  # Set the window size to 1440 x 960
        
#         self.initUI()
#         self.apply_styles()

#     def initUI(self):
#         central_widget = QWidget()
#         main_layout = QVBoxLayout()

#         # Create a function to add labeled widgets with explicit geometry
#         def add_labeled_widget(label_text, widget, x, y, width, height):
#             layout = QHBoxLayout()

#             # Create and set geometry for the label
#             label = create_label_qt6(label_text)
#             label.setGeometry(x, y, 128, 28)

#             # Create and set geometry for the widget
#             widget.setGeometry(x + 140, y, width, height)  # Adjust x-coordinate to the right of the label

#             layout.addWidget(label)
#             layout.addWidget(widget)
#             main_layout.addLayout(layout)

#         # Add new line edit widgets with labels as the first widgets
#         add_labeled_widget("Serial Number:", create_serial_number_qt6(), 10, 10, 320, 28)
#         add_labeled_widget("Client Name:", create_client_name_qt6(), 10, 50, 320, 28)
#         add_labeled_widget("Campaign Name:", create_campaign_name_qt6(), 10, 90, 320, 28)
#         add_labeled_widget("Projekt Nickname:", create_projekt_nickname_qt6(), 10, 130, 320, 28)

#         # Add custom widgets to layout with labels
#         add_labeled_widget("Button:", CustomButton("Click Me"), 10, 170, 200, 28)
#         add_labeled_widget("Combo Box:", CustomComboBox(["Option 1", "Option 2", "Option 3"]), 10, 210, 200, 28)
#         add_labeled_widget("Start Frame:", create_combo_box_start_frame_qt6(), 10, 250, 200, 28)
#         add_labeled_widget("Line Edit:", CustomLineEdit(), 10, 290, 200, 28)
#         add_labeled_widget("Drop Down:", CustomDropDown(["Choice 1", "Choice 2", "Choice 3"]), 10, 330, 200, 28)
#         add_labeled_widget("Summary Text Box:", SummaryTextBox(), 10, 370, 400, 100)  # Example larger widget

#         central_widget.setLayout(main_layout)
#         self.setCentralWidget(central_widget)

#         # Create menu actions
#         load_action = QAction("&Load Config", self)
#         load_action.triggered.connect(self.load_config)

#         save_action = QAction("&Save Config", self)
#         save_action.triggered.connect(self.save_config)

#         # Add actions to menu
#         menubar = self.menuBar()
#         file_menu = menubar.addMenu("&File")
#         file_menu.addAction(load_action)
#         file_menu.addAction(save_action)

#     def load_config(self):
#         file_name, _ = QFileDialog.getOpenFileName(self, "Open Config File", "", "JSON Files (*.json)")
#         if file_name:
#             # Load config logic
#             QMessageBox.information(self, "Info", f"Loaded config: {file_name}")

#     def save_config(self):
#         file_name, _ = QFileDialog.getSaveFileName(self, "Save Config File", "", "JSON Files (*.json)")
#         if file_name:
#             # Save config logic
#             QMessageBox.information(self, "Info", f"Saved config: {file_name}")

#     def apply_styles(self):
#         try:
#             self.setStyleSheet(stylesheet)  # Apply the stylesheet
#         except Exception as e:
#             QMessageBox.critical(self, "Error", str(e))














# from PySide6.QtWidgets import QMainWindow, QWidget, QFileDialog, QMessageBox, QLabel, QLineEdit, QPushButton, QComboBox, QTextEdit
# from PySide6.QtGui import QAction
# from ...widgets.button.button import CustomButton
# from ...widgets.combo_box.combo_box import CustomComboBox
# from ...widgets.combo_box.combo_box_start_frame import create_combo_box_start_frame_qt6
# from ...widgets.line_edit.line_edit_projekt_namer import (
#     create_serial_number_qt6,
#     create_client_name_qt6,
#     create_campaign_name_qt6,
#     create_projekt_nickname_qt6
# )
# from ...functions.label.label import create_label_qt6
# from ...widgets.style_sheet.logik_stylesheet import stylesheet
# from ...widgets.summary_textbox.summary_textbox import SummaryTextBox

# class MainWindow(QMainWindow):
#     def __init__(self):
#         super().__init__()
#         self.setWindowTitle("Logik Projekt Application")
#         self.setGeometry(100, 100, 1440, 960)  # Set the window size to 1440 x 960
        
#         self.initUI()
#         self.apply_styles()

#     def initUI(self):
#         central_widget = QWidget(self)
#         self.setCentralWidget(central_widget)
#         central_widget.setGeometry(0, 0, 1440, 960)  # Set central widget size
#         central_widget.setStyleSheet(stylesheet)

#         # Function to create and position labeled widgets
#         def add_labeled_widget(parent, label_text, widget, x, y, width, height):
#             label = create_label_qt6(label_text)
#             label.setParent(parent)
#             label.setGeometry(x, y, 128, 28)
            
#             widget.setParent(parent)
#             widget.setGeometry(x + 140, y, width, height)  # Adjust x-coordinate to the right of the label

#         # Create and position widgets with labels
#         add_labeled_widget(central_widget, "Serial Number:", create_serial_number_qt6(), 10, 10, 200, 28)
#         add_labeled_widget(central_widget, "Client Name:", create_client_name_qt6(), 10, 50, 200, 28)
#         add_labeled_widget(central_widget, "Campaign Name:", create_campaign_name_qt6(), 10, 90, 200, 28)
#         add_labeled_widget(central_widget, "Projekt Nickname:", create_projekt_nickname_qt6(), 10, 130, 200, 28)
#         add_labeled_widget(central_widget, "Combo Box:", CustomComboBox(["Option 1", "Option 2", "Option 3"]), 10, 210, 200, 28)
#         add_labeled_widget(central_widget, "Start Frame:", create_combo_box_start_frame_qt6(), 10, 250, 200, 28)
#         add_labeled_widget(central_widget, "Line Edit:", QLineEdit(), 10, 290, 200, 28)
#         add_labeled_widget(central_widget, "Drop Down:", QComboBox(), 10, 330, 200, 28)
#         add_labeled_widget(central_widget, "Summary Text Box:", SummaryTextBox(), 10, 370, 400, 100)
#         add_labeled_widget(central_widget, "Button:", CustomButton("Click Me"), 10, 170, 200, 28)

#         # Create menu actions
#         load_action = QAction("&Load Config", self)
#         load_action.triggered.connect(self.load_config)

#         save_action = QAction("&Save Config", self)
#         save_action.triggered.connect(self.save_config)

#         # Add actions to menu
#         menubar = self.menuBar()
#         file_menu = menubar.addMenu("&File")
#         file_menu.addAction(load_action)
#         file_menu.addAction(save_action)

#     def load_config(self):
#         file_name, _ = QFileDialog.getOpenFileName(self, "Open Config File", "", "JSON Files (*.json)")
#         if file_name:
#             # Load config logic
#             QMessageBox.information(self, "Info", f"Loaded config: {file_name}")

#     def save_config(self):
#         file_name, _ = QFileDialog.getSaveFileName(self, "Save Config File", "", "JSON Files (*.json)")
#         if file_name:
#             # Save config logic
#             QMessageBox.information(self, "Info", f"Saved config: {file_name}")

#     def apply_styles(self):
#         try:
#             self.setStyleSheet(stylesheet)  # Apply the stylesheet
#         except Exception as e:
#             QMessageBox.critical(self, "Error", str(e))



















# from PySide6.QtWidgets import QMainWindow, QWidget, QFileDialog, QMessageBox, QLabel, QLineEdit, QPushButton, QComboBox, QTextEdit
# from PySide6.QtGui import QAction
# from ...widgets.button.button import CustomButton
# from ...widgets.combo_box.combo_box import CustomComboBox
# from ...widgets.combo_box.combo_box_start_frame import create_combo_box_start_frame_qt6
# from ...widgets.combo_box.combo_box_color_science import create_combo_box_color_science_qt6
# from ...widgets.line_edit.line_edit_projekt_namer import (
#     create_serial_number_qt6,
#     create_client_name_qt6,
#     create_campaign_name_qt6,
#     create_projekt_nickname_qt6
# )
# from ...functions.label.label import create_label_qt6
# from ...widgets.style_sheet.logik_stylesheet import stylesheet
# from ...widgets.summary_textbox.summary_textbox import SummaryTextBox

# class MainWindow(QMainWindow):
#     def __init__(self):
#         super().__init__()
#         self.setWindowTitle("Logik Projekt Application")
#         self.setGeometry(100, 100, 1440, 960)  # Set the window size to 1440 x 960
        
#         self.initUI()
#         self.apply_styles()

#     def initUI(self):
#         central_widget = QWidget(self)
#         self.setCentralWidget(central_widget)
#         central_widget.setGeometry(0, 0, 1440, 960)  # Set central widget size
#         central_widget.setStyleSheet(stylesheet)

#         # Function to create and position labeled widgets
#         def add_labeled_widget(parent, label_text, widget, x, y, width, height):
#             label = create_label_qt6(label_text)
#             label.setParent(parent)
#             label.setGeometry(x, y, 128, 28)
            
#             widget.setParent(parent)
#             widget.setGeometry(x + 140, y, width, height)  # Adjust x-coordinate to the right of the label

#         # Create and position widgets with labels
#         add_labeled_widget(central_widget, "Serial Number:", create_serial_number_qt6(), 10, 10, 320, 28)
#         add_labeled_widget(central_widget, "Client Name:", create_client_name_qt6(), 10, 50, 320, 28)
#         add_labeled_widget(central_widget, "Campaign Name:", create_campaign_name_qt6(), 10, 90, 320, 28)
#         add_labeled_widget(central_widget, "Projekt Nickname:", create_projekt_nickname_qt6(), 10, 130, 320, 28)
#         add_labeled_widget(central_widget, "Combo Box:", CustomComboBox(["Option 1", "Option 2", "Option 3"]), 10, 170, 320, 28)
#         add_labeled_widget(central_widget, "Color Science:", create_combo_box_color_science_qt6(), 10, 250, 320, 28)
#         add_labeled_widget(central_widget, "Start Frame:", create_combo_box_start_frame_qt6(), 10, 210, 320, 28)
#         add_labeled_widget(central_widget, "Line Edit:", QLineEdit(), 10, 290, 320, 28)
#         add_labeled_widget(central_widget, "Drop Down:", QComboBox(), 10, 330, 320, 28)
#         add_labeled_widget(central_widget, "Summary Text Box:", SummaryTextBox(), 10, 370, 400, 100)
#         add_labeled_widget(central_widget, "Button:", CustomButton("Click Me"), 10, 490, 320, 28)

#         # Create menu actions
#         load_action = QAction("&Load Config", self)
#         load_action.triggered.connect(self.load_config)

#         save_action = QAction("&Save Config", self)
#         save_action.triggered.connect(self.save_config)

#         # Add actions to menu
#         menubar = self.menuBar()
#         file_menu = menubar.addMenu("&File")
#         file_menu.addAction(load_action)
#         file_menu.addAction(save_action)

#     def load_config(self):
#         file_name, _ = QFileDialog.getOpenFileName(self, "Open Config File", "", "JSON Files (*.json)")
#         if file_name:
#             # Load config logic
#             QMessageBox.information(self, "Info", f"Loaded config: {file_name}")

#     def save_config(self):
#         file_name, _ = QFileDialog.getSaveFileName(self, "Save Config File", "", "JSON Files (*.json)")
#         if file_name:
#             # Save config logic
#             QMessageBox.information(self, "Info", f"Saved config: {file_name}")

#     def apply_styles(self):
#         try:
#             self.setStyleSheet(stylesheet)  # Apply the stylesheet
#         except Exception as e:
#             QMessageBox.critical(self, "Error", str(e))





































# from PySide6.QtWidgets import (
#     QMainWindow, 
#     QWidget, 
#     QFileDialog, 
#     QMessageBox, 
#     QLabel, 
#     QLineEdit, 
#     QPushButton, 
#     QComboBox, 
#     QTextEdit,
# )

# from PySide6.QtGui import QAction

# from ...widgets.button.button import CustomButton

# from ...widgets.combo_box.combo_box import CustomComboBox

# from ...widgets.combo_box.combo_box_bit_depth import create_combo_box_bit_depth_qt6
# from ...widgets.combo_box.combo_box_frame_rate import create_combo_box_frame_rate_qt6
# from ...widgets.combo_box.combo_box_scan_mode import create_combo_box_scan_mode_qt6
# from ...widgets.combo_box.combo_box_color_science import create_combo_box_color_science_qt6
# from ...widgets.combo_box.combo_box_start_frame import create_combo_box_start_frame_qt6

# from ...widgets.line_edit.line_edit_projekt_namer import (
#     create_serial_number_qt6,
#     create_client_name_qt6,
#     create_campaign_name_qt6,
#     create_projekt_nickname_qt6
# )

# from ...functions.label.label import create_label_qt6
# from ...widgets.style_sheet.logik_stylesheet import stylesheet
# from ...widgets.summary_textbox.summary_textbox import SummaryTextBox

# class MainWindow(QMainWindow):
#     def __init__(self):
#         super().__init__()
#         self.setWindowTitle("Logik Projekt Application")
#         self.setGeometry(100, 100, 1440, 960)  # Set the window size to 1440 x 960
        
#         self.initUI()
#         self.apply_styles()

#     def initUI(self):
#         central_widget = QWidget(self)
#         self.setCentralWidget(central_widget)
#         central_widget.setGeometry(0, 0, 1440, 960)  # Set central widget size
#         central_widget.setStyleSheet(stylesheet)

#         # Function to create and position labeled widgets
#         def add_labeled_widget(parent, label_text, widget, x, y, width, height):
#             label = create_label_qt6(label_text)
#             label.setParent(parent)
#             label.setGeometry(x, y, 128, 28)
            
#             widget.setParent(parent)
#             widget.setGeometry(x + 140, y, width, height)  # Adjust x-coordinate to the right of the label

#         # Create and position widgets with labels
#         add_labeled_widget(central_widget, "Serial Number:", create_serial_number_qt6(), 160, 48, 320, 28)
#         add_labeled_widget(central_widget, "Client Name:", create_client_name_qt6(), 160, 96, 320, 28)
#         add_labeled_widget(central_widget, "Campaign Name:", create_campaign_name_qt6(), 160, 144, 320, 28)
#         add_labeled_widget(central_widget, "Projekt Nickname:", create_projekt_nickname_qt6(), 160, 192, 320, 28)
#         add_labeled_widget(central_widget, "Bit Depth:", create_combo_box_bit_depth_qt6(), 160, 240, 320, 28)
#         add_labeled_widget(central_widget, "Frame Rate:", create_combo_box_frame_rate_qt6(), 160, 288, 320, 28)
#         add_labeled_widget(central_widget, "Scan Mode:", create_combo_box_scan_mode_qt6(), 160, 336, 320, 28)
#         add_labeled_widget(central_widget, "Color Science:", create_combo_box_color_science_qt6(), 160, 384, 320, 28)
#         add_labeled_widget(central_widget, "Start Frame:", create_combo_box_start_frame_qt6(), 160, 432, 320, 28)
#         add_labeled_widget(central_widget, "Combo Box:", CustomComboBox(["Option 1", "Option 2", "Option 3"]), 160, 480, 320, 28)
#         add_labeled_widget(central_widget, "Line Edit:", QLineEdit(), 160, 528, 320, 28)
#         add_labeled_widget(central_widget, "Drop Down:", QComboBox(), 160, 576, 320, 28)
#         add_labeled_widget(central_widget, "Summary Text Box:", SummaryTextBox(), 160, 624, 400, 100)
#         add_labeled_widget(central_widget, "Button:", CustomButton("Click Me"), 160, 672, 320, 28)

#         # Create menu actions
#         load_action = QAction("&Load Config", self)
#         load_action.triggered.connect(self.load_config)

#         save_action = QAction("&Save Config", self)
#         save_action.triggered.connect(self.save_config)

#         # Add actions to menu
#         menubar = self.menuBar()
#         file_menu = menubar.addMenu("&File")
#         file_menu.addAction(load_action)
#         file_menu.addAction(save_action)

#     def load_config(self):
#         file_name, _ = QFileDialog.getOpenFileName(self, "Open Config File", "", "JSON Files (*.json)")
#         if file_name:
#             # Load config logic
#             QMessageBox.information(self, "Info", f"Loaded config: {file_name}")

#     def save_config(self):
#         file_name, _ = QFileDialog.getSaveFileName(self, "Save Config File", "", "JSON Files (*.json)")
#         if file_name:
#             # Save config logic
#             QMessageBox.information(self, "Info", f"Saved config: {file_name}")

#     def apply_styles(self):
#         try:
#             self.setStyleSheet(stylesheet)  # Apply the stylesheet
#         except Exception as e:
#             QMessageBox.critical(self, "Error", str(e))















# from PySide6.QtWidgets import (
#     QMainWindow, 
#     QWidget, 
#     QFileDialog, 
#     QMessageBox, 
#     QLabel, 
#     QLineEdit, 
#     QPushButton, 
#     QComboBox, 
#     QTextEdit,
# )

# from PySide6.QtGui import QAction

# from ...widgets.button.button import CustomButton

# from ...widgets.combo_box.combo_box import CustomComboBox

# from ...widgets.combo_box.combo_box_bit_depth import create_combo_box_bit_depth_qt6
# from ...widgets.combo_box.combo_box_frame_rate import create_combo_box_frame_rate_qt6
# from ...widgets.combo_box.combo_box_scan_mode import create_combo_box_scan_mode_qt6
# from ...widgets.combo_box.combo_box_color_science import create_combo_box_color_science_qt6
# from ...widgets.combo_box.combo_box_start_frame import create_combo_box_start_frame_qt6

# from ...widgets.line_edit.line_edit_projekt_namer import (
#     create_serial_number_qt6,
#     create_client_name_qt6,
#     create_campaign_name_qt6,
#     create_projekt_nickname_qt6
# )

# from ...functions.label.label import create_label_qt6
# from ...widgets.style_sheet.logik_stylesheet import stylesheet
# from ...widgets.summary_textbox.summary_textbox import SummaryTextBox

# class MainWindow(QMainWindow):
#     def __init__(self):
#         super().__init__()
#         self.setWindowTitle("Logik Projekt Application")
#         self.setGeometry(100, 100, 1440, 960)  # Set the window size to 1440 x 960
        
#         self.initUI()
#         self.apply_styles()

#     def initUI(self):
#         central_widget = QWidget(self)
#         self.setCentralWidget(central_widget)
#         central_widget.setGeometry(0, 0, 1440, 960)  # Set central widget size
#         central_widget.setStyleSheet(stylesheet)

#         self.summary_textbox = SummaryTextBox(central_widget)
#         self.summary_textbox.setGeometry(160, 624, 400, 100)

#         # Function to create and position labeled widgets
#         def add_labeled_widget(parent, label_text, widget, x, y, width, height):
#             label = create_label_qt6(label_text)
#             label.setParent(parent)
#             label.setGeometry(x, y, 128, 28)
            
#             widget.setParent(parent)
#             widget.setGeometry(x + 140, y, width, height)  # Adjust x-coordinate to the right of the label
#             widget.label_text = label_text  # Store label text for later use

#             # Connect widget signals to update summary text box
#             if isinstance(widget, QLineEdit):
#                 widget.textChanged.connect(lambda: self.update_summary())
#             elif isinstance(widget, QComboBox):
#                 widget.currentIndexChanged.connect(lambda: self.update_summary())
#             elif isinstance(widget, QPushButton):
#                 widget.clicked.connect(lambda: self.update_summary())

#         # Create and position widgets with labels
#         add_labeled_widget(central_widget, "Serial Number:", create_serial_number_qt6(), 160, 48, 320, 28)
#         add_labeled_widget(central_widget, "Client Name:", create_client_name_qt6(), 160, 96, 320, 28)
#         add_labeled_widget(central_widget, "Campaign Name:", create_campaign_name_qt6(), 160, 144, 320, 28)
#         add_labeled_widget(central_widget, "Projekt Nickname:", create_projekt_nickname_qt6(), 160, 192, 320, 28)
#         add_labeled_widget(central_widget, "Bit Depth:", create_combo_box_bit_depth_qt6(), 160, 240, 320, 28)
#         add_labeled_widget(central_widget, "Frame Rate:", create_combo_box_frame_rate_qt6(), 160, 288, 320, 28)
#         add_labeled_widget(central_widget, "Scan Mode:", create_combo_box_scan_mode_qt6(), 160, 336, 320, 28)
#         add_labeled_widget(central_widget, "Color Science:", create_combo_box_color_science_qt6(), 160, 384, 320, 28)
#         add_labeled_widget(central_widget, "Start Frame:", create_combo_box_start_frame_qt6(), 160, 432, 320, 28)
#         add_labeled_widget(central_widget, "Combo Box:", CustomComboBox(["Option 1", "Option 2", "Option 3"]), 160, 480, 320, 28)
#         add_labeled_widget(central_widget, "Line Edit:", QLineEdit(), 160, 528, 320, 28)
#         add_labeled_widget(central_widget, "Drop Down:", QComboBox(), 160, 576, 320, 28)
#         add_labeled_widget(central_widget, "Button:", CustomButton("Click Me"), 160, 672, 320, 28)

#         # Create menu actions
#         load_action = QAction("&Load Config", self)
#         load_action.triggered.connect(self.load_config)

#         save_action = QAction("&Save Config", self)
#         save_action.triggered.connect(self.save_config)

#         # Add actions to menu
#         menubar = self.menuBar()
#         file_menu = menubar.addMenu("&File")
#         file_menu.addAction(load_action)
#         file_menu.addAction(save_action)

#     def update_summary(self):
#         summary_text = ""
#         for widget in self.findChildren((QLineEdit, QComboBox, QPushButton)):
#             label_text = widget.label_text
#             if isinstance(widget, QLineEdit):
#                 summary_text += f"{label_text} {widget.text()}\n"
#             elif isinstance(widget, QComboBox):
#                 summary_text += f"{label_text} {widget.currentText()}\n"
#             elif isinstance(widget, QPushButton):
#                 summary_text += f"{label_text} Clicked\n"
#         self.summary_textbox.setPlainText(summary_text)

#     def load_config(self):
#         file_name, _ = QFileDialog.getOpenFileName(self, "Open Config File", "", "JSON Files (*.json)")
#         if file_name:
#             # Load config logic
#             QMessageBox.information(self, "Info", f"Loaded config: {file_name}")

#     def save_config(self):
#         file_name, _ = QFileDialog.getSaveFileName(self, "Save Config File", "", "JSON Files (*.json)")
#         if file_name:
#             # Save config logic
#             QMessageBox.information(self, "Info", f"Saved config: {file_name}")

#     def apply_styles(self):
#         try:
#             self.setStyleSheet(stylesheet)  # Apply the stylesheet
#         except Exception as e:
#             QMessageBox.critical(self, "Error", str(e))












# from PySide6.QtWidgets import (
#     QMainWindow, 
#     QWidget, 
#     QFileDialog, 
#     QMessageBox, 
#     QLabel, 
#     QLineEdit, 
#     QPushButton, 
#     QComboBox, 
#     QTextEdit,
# )
# from PySide6.QtGui import QAction

# from ...widgets.button.button import CustomButton
# from ...widgets.combo_box.combo_box import CustomComboBox
# from ...widgets.combo_box.combo_box_bit_depth import create_combo_box_bit_depth_qt6
# from ...widgets.combo_box.combo_box_frame_rate import create_combo_box_frame_rate_qt6
# from ...widgets.combo_box.combo_box_scan_mode import create_combo_box_scan_mode_qt6
# from ...widgets.combo_box.combo_box_color_science import create_combo_box_color_science_qt6
# from ...widgets.combo_box.combo_box_start_frame import create_combo_box_start_frame_qt6
# from ...widgets.line_edit.line_edit_projekt_namer import (
#     create_serial_number_qt6,
#     create_client_name_qt6,
#     create_campaign_name_qt6,
#     create_projekt_nickname_qt6
# )
# from ...functions.label.label import create_label_qt6
# from ...widgets.style_sheet.logik_stylesheet import stylesheet
# from ...widgets.summary_textbox.summary_textbox import SummaryTextBox

# class MainWindow(QMainWindow):
#     def __init__(self):
#         super().__init__()
#         self.setWindowTitle("Logik Projekt Application")
#         self.setGeometry(100, 100, 1440, 960)  # Set the window size to 1440 x 960
        
#         self.initUI()
#         self.apply_styles()

#     def initUI(self):
#         central_widget = QWidget(self)
#         self.setCentralWidget(central_widget)
#         central_widget.setGeometry(0, 0, 1440, 960)  # Set central widget size
#         central_widget.setStyleSheet(stylesheet)

#         # Function to create and position labeled widgets
#         def add_labeled_widget(parent, label_text, widget, x, y, width, height):
#             label = create_label_qt6(label_text)
#             label.setParent(parent)
#             label.setGeometry(x, y, 128, 28)
            
#             widget.setParent(parent)
#             widget.setGeometry(x + 140, y, width, height)  # Adjust x-coordinate to the right of the label

#         # Create and position widgets with labels
#         add_labeled_widget(central_widget, "Serial Number:", create_serial_number_qt6(), 160, 48, 320, 28)
#         add_labeled_widget(central_widget, "Client Name:", create_client_name_qt6(), 160, 96, 320, 28)
#         add_labeled_widget(central_widget, "Campaign Name:", create_campaign_name_qt6(), 160, 144, 320, 28)
#         add_labeled_widget(central_widget, "Projekt Nickname:", create_projekt_nickname_qt6(), 160, 192, 320, 28)
#         add_labeled_widget(central_widget, "Bit Depth:", create_combo_box_bit_depth_qt6(), 160, 240, 320, 28)
#         add_labeled_widget(central_widget, "Frame Rate:", create_combo_box_frame_rate_qt6(), 160, 288, 320, 28)
#         add_labeled_widget(central_widget, "Scan Mode:", create_combo_box_scan_mode_qt6(), 160, 336, 320, 28)
#         add_labeled_widget(central_widget, "Color Science:", create_combo_box_color_science_qt6(), 160, 384, 320, 28)
#         add_labeled_widget(central_widget, "Start Frame:", create_combo_box_start_frame_qt6(), 160, 432, 320, 28)
#         add_labeled_widget(central_widget, "Combo Box:", CustomComboBox(["Option 1", "Option 2", "Option 3"]), 160, 480, 320, 28)
#         add_labeled_widget(central_widget, "Line Edit:", QLineEdit(), 160, 528, 320, 28)
#         add_labeled_widget(central_widget, "Drop Down:", QComboBox(), 160, 576, 320, 28)
        
#         # Position and dimension values for the summary text box
#         summary_text_box = SummaryTextBox()
#         summary_text_box.setParent(central_widget)
#         summary_text_box.setGeometry(160, 624, 800, 200)  # Adjust these values as needed

#         add_labeled_widget(central_widget, "Button:", CustomButton("Click Me"), 160, 840, 320, 28)

#         # Create menu actions
#         load_action = QAction("&Load Config", self)
#         load_action.triggered.connect(self.load_config)

#         save_action = QAction("&Save Config", self)
#         save_action.triggered.connect(self.save_config)

#         # Add actions to menu
#         menubar = self.menuBar()
#         file_menu = menubar.addMenu("&File")
#         file_menu.addAction(load_action)
#         file_menu.addAction(save_action)

#     def load_config(self):
#         file_name, _ = QFileDialog.getOpenFileName(self, "Open Config File", "", "JSON Files (*.json)")
#         if file_name:
#             # Load config logic
#             QMessageBox.information(self, "Info", f"Loaded config: {file_name}")

#     def save_config(self):
#         file_name, _ = QFileDialog.getSaveFileName(self, "Save Config File", "", "JSON Files (*.json)")
#         if file_name:
#             # Save config logic
#             QMessageBox.information(self, "Info", f"Saved config: {file_name}")

#     def apply_styles(self):
#         try:
#             self.setStyleSheet(stylesheet)  # Apply the stylesheet
#         except Exception as e:
#             QMessageBox.critical(self, "Error", str(e))















# from PySide6.QtWidgets import (
#     QMainWindow, 
#     QWidget, 
#     QFileDialog, 
#     QMessageBox, 
#     QLabel, 
#     QLineEdit, 
#     QPushButton, 
#     QComboBox, 
#     QTextEdit,
# )
# from PySide6.QtGui import QAction

# from ...widgets.button.button import CustomButton
# from ...widgets.combo_box.combo_box import CustomComboBox
# from ...widgets.combo_box.combo_box_bit_depth import create_combo_box_bit_depth_qt6
# from ...widgets.combo_box.combo_box_frame_rate import create_combo_box_frame_rate_qt6
# from ...widgets.combo_box.combo_box_scan_mode import create_combo_box_scan_mode_qt6
# from ...widgets.combo_box.combo_box_color_science import create_combo_box_color_science_qt6
# from ...widgets.combo_box.combo_box_start_frame import create_combo_box_start_frame_qt6
# from ...widgets.line_edit.line_edit_projekt_namer import (
#     create_serial_number_qt6,
#     create_client_name_qt6,
#     create_campaign_name_qt6,
#     create_projekt_nickname_qt6
# )
# from ...functions.label.label import create_label_qt6
# from ...widgets.style_sheet.logik_stylesheet import stylesheet
# from ...widgets.summary_textbox.summary_textbox import SummaryTextBox

# class MainWindow(QMainWindow):
#     def __init__(self):
#         super().__init__()
#         self.setWindowTitle("Logik Projekt Application")
#         self.setGeometry(100, 100, 1440, 960)  # Set the window size to 1440 x 960
        
#         self.initUI()
#         self.apply_styles()

#     def initUI(self):
#         central_widget = QWidget(self)
#         self.setCentralWidget(central_widget)
#         central_widget.setGeometry(0, 0, 1440, 960)  # Set central widget size
#         central_widget.setStyleSheet(stylesheet)

#         # Function to create and position labeled widgets
#         def add_labeled_widget(parent, label_text, widget, x, y, width, height):
#             label = create_label_qt6(label_text)
#             label.setParent(parent)
#             label.setGeometry(x, y, 128, 28)
            
#             widget.setParent(parent)
#             widget.setGeometry(x + 140, y, width, height)  # Adjust x-coordinate to the right of the label

#         # Create and position widgets with labels
#         add_labeled_widget(central_widget, "Serial Number:", create_serial_number_qt6(), 160, 48, 320, 28)
#         add_labeled_widget(central_widget, "Client Name:", create_client_name_qt6(), 160, 96, 320, 28)
#         add_labeled_widget(central_widget, "Campaign Name:", create_campaign_name_qt6(), 160, 144, 320, 28)
#         add_labeled_widget(central_widget, "Projekt Nickname:", create_projekt_nickname_qt6(), 160, 192, 320, 28)
#         add_labeled_widget(central_widget, "Bit Depth:", create_combo_box_bit_depth_qt6(), 160, 240, 320, 28)
#         add_labeled_widget(central_widget, "Frame Rate:", create_combo_box_frame_rate_qt6(), 160, 288, 320, 28)
#         add_labeled_widget(central_widget, "Scan Mode:", create_combo_box_scan_mode_qt6(), 160, 336, 320, 28)
#         add_labeled_widget(central_widget, "Color Science:", create_combo_box_color_science_qt6(), 160, 384, 320, 28)
#         add_labeled_widget(central_widget, "Start Frame:", create_combo_box_start_frame_qt6(), 160, 432, 320, 28)
#         add_labeled_widget(central_widget, "Combo Box:", CustomComboBox(["Option 1", "Option 2", "Option 3"]), 160, 480, 320, 28)
#         add_labeled_widget(central_widget, "Line Edit:", QLineEdit(), 160, 528, 320, 28)
#         add_labeled_widget(central_widget, "Drop Down:", QComboBox(), 160, 576, 320, 28)
#         add_labeled_widget(central_widget, "Summary Text Box:", SummaryTextBox(), 160, 624, 400, 100)
#         add_labeled_widget(central_widget, "Button:", CustomButton("Click Me"), 160, 672, 320, 28)

#         # Create menu actions
#         load_action = QAction("&Load Config", self)
#         load_action.triggered.connect(self.load_config)

#         save_action = QAction("&Save Config", self)
#         save_action.triggered.connect(self.save_config)

#         # Add actions to menu
#         menubar = self.menuBar()
#         file_menu = menubar.addMenu("&File")
#         file_menu.addAction(load_action)
#         file_menu.addAction(save_action)

#     def load_config(self):
#         file_name, _ = QFileDialog.getOpenFileName(self, "Open Config File", "", "JSON Files (*.json)")
#         if file_name:
#             # Load config logic
#             QMessageBox.information(self, "Info", f"Loaded config: {file_name}")

#     def save_config(self):
#         file_name, _ = QFileDialog.getSaveFileName(self, "Save Config File", "", "JSON Files (*.json)")
#         if file_name:
#             # Save config logic
#             QMessageBox.information(self, "Info", f"Saved config: {file_name}")

#     def apply_styles(self):
#         try:
#             self.setStyleSheet(stylesheet)  # Apply the stylesheet
#         except Exception as e:
#             QMessageBox.critical(self, "Error", str(e))




















# from PySide6.QtWidgets import (
#     QMainWindow, 
#     QWidget, 
#     QFileDialog, 
#     QMessageBox, 
#     QLabel, 
#     QLineEdit, 
#     QPushButton, 
#     QComboBox, 
#     QTextEdit,
# )
# from PySide6.QtGui import QAction

# from ...widgets.button.button import CustomButton
# from ...widgets.combo_box.combo_box import CustomComboBox
# from ...widgets.combo_box.combo_box_bit_depth import create_combo_box_bit_depth_qt6
# from ...widgets.combo_box.combo_box_frame_rate import create_combo_box_frame_rate_qt6
# from ...widgets.combo_box.combo_box_scan_mode import create_combo_box_scan_mode_qt6
# from ...widgets.combo_box.combo_box_color_science import create_combo_box_color_science_qt6
# from ...widgets.combo_box.combo_box_start_frame import create_combo_box_start_frame_qt6
# from ...widgets.line_edit.line_edit_projekt_namer import (
#     create_serial_number_qt6,
#     create_client_name_qt6,
#     create_campaign_name_qt6,
#     create_projekt_nickname_qt6
# )
# from ...functions.label.label import create_label_qt6
# from ...widgets.style_sheet.logik_stylesheet import stylesheet
# from ...widgets.summary_textbox.summary_textbox import SummaryTextBox

# class MainWindow(QMainWindow):
#     def __init__(self):
#         super().__init__()
#         self.setWindowTitle("Logik Projekt Application")
#         self.setGeometry(100, 100, 1440, 960)  # Set the window size to 1440 x 960
        
#         self.initUI()
#         self.apply_styles()

#     def initUI(self):
#         central_widget = QWidget(self)
#         self.setCentralWidget(central_widget)
#         central_widget.setGeometry(0, 0, 1440, 960)  # Set central widget size
#         central_widget.setStyleSheet(stylesheet)

#         # Function to create and position labeled widgets
#         def add_labeled_widget(parent, label_text, widget, x, y, width, height):
#             label = create_label_qt6(label_text)
#             label.setParent(parent)
#             label.setGeometry(x, y, 128, 28)
            
#             widget.setParent(parent)
#             widget.setGeometry(x + 140, y, width, height)  # Adjust x-coordinate to the right of the label

#         # Create and position widgets with labels
#         add_labeled_widget(central_widget, "Serial Number:", create_serial_number_qt6(), 160, 48, 320, 28)
#         add_labeled_widget(central_widget, "Client Name:", create_client_name_qt6(), 160, 96, 320, 28)
#         add_labeled_widget(central_widget, "Campaign Name:", create_campaign_name_qt6(), 160, 144, 320, 28)
#         add_labeled_widget(central_widget, "Projekt Nickname:", create_projekt_nickname_qt6(), 160, 192, 320, 28)
#         add_labeled_widget(central_widget, "Bit Depth:", create_combo_box_bit_depth_qt6(), 160, 240, 320, 28)
#         add_labeled_widget(central_widget, "Frame Rate:", create_combo_box_frame_rate_qt6(), 160, 288, 320, 28)
#         add_labeled_widget(central_widget, "Scan Mode:", create_combo_box_scan_mode_qt6(), 160, 336, 320, 28)
#         add_labeled_widget(central_widget, "Color Science:", create_combo_box_color_science_qt6(), 160, 384, 320, 28)
#         add_labeled_widget(central_widget, "Start Frame:", create_combo_box_start_frame_qt6(), 160, 432, 320, 28)
#         add_labeled_widget(central_widget, "Combo Box:", CustomComboBox(["Option 1", "Option 2", "Option 3"]), 160, 480, 320, 28)
#         add_labeled_widget(central_widget, "Line Edit:", QLineEdit(), 160, 528, 320, 28)
#         add_labeled_widget(central_widget, "Drop Down:", QComboBox(), 160, 576, 320, 28)
#         add_labeled_widget(central_widget, "Summary:", SummaryTextBox(), 160, 624, 320, 140)
#         add_labeled_widget(central_widget, "Button:", CustomButton("Click Me"), 160, 812, 320, 28)

#         # Create menu actions
#         load_action = QAction("&Load Config", self)
#         load_action.triggered.connect(self.load_config)

#         save_action = QAction("&Save Config", self)
#         save_action.triggered.connect(self.save_config)

#         # Add actions to menu
#         menubar = self.menuBar()
#         file_menu = menubar.addMenu("&File")
#         file_menu.addAction(load_action)
#         file_menu.addAction(save_action)

#     def load_config(self):
#         file_name, _ = QFileDialog.getOpenFileName(self, "Open Config File", "", "JSON Files (*.json)")
#         if file_name:
#             # Load config logic
#             QMessageBox.information(self, "Info", f"Loaded config: {file_name}")

#     def save_config(self):
#         file_name, _ = QFileDialog.getSaveFileName(self, "Save Config File", "", "JSON Files (*.json)")
#         if file_name:
#             # Save config logic
#             QMessageBox.information(self, "Info", f"Saved config: {file_name}")

#     def apply_styles(self):
#         try:
#             self.setStyleSheet(stylesheet)  # Apply the stylesheet
#         except Exception as e:
#             QMessageBox.critical(self, "Error", str(e))




















# from PySide6.QtWidgets import QMainWindow, QWidget, QMessageBox, QLabel, QTextEdit, QPushButton
# from PySide6.QtGui import QAction

# from ...widgets.button.button import CustomButton
# from ...widgets.combo_box.combo_box_bit_depth import create_combo_box_bit_depth_qt6
# from ...widgets.combo_box.combo_box_frame_rate import create_combo_box_frame_rate_qt6
# from ...widgets.combo_box.combo_box_scan_mode import create_combo_box_scan_mode_qt6
# from ...widgets.combo_box.combo_box_color_science import create_combo_box_color_science_qt6
# from ...widgets.combo_box.combo_box_start_frame import create_combo_box_start_frame_qt6
# from ...widgets.line_edit.line_edit_projekt_namer import (
#     create_serial_number_qt6,
#     create_client_name_qt6,
#     create_campaign_name_qt6,
#     create_projekt_nickname_qt6,
# )
# from ...functions.label.label import create_label_qt6
# from ...widgets.style_sheet.logik_stylesheet import stylesheet
# from ...widgets.summary_textbox.summary_textbox import SummaryTextBox

# class MainWindow(QMainWindow):
#     def __init__(self):
#         super().__init__()
#         self.setWindowTitle("Logik Projekt Application")
#         self.setGeometry(100, 100, 1440, 960)  # Set the window size
        
#         self.initUI()
#         self.apply_styles()

#     def initUI(self):
#         central_widget = QWidget(self)
#         self.setCentralWidget(central_widget)
#         central_widget.setGeometry(0, 0, 1440, 960)  # Set central widget size
#         central_widget.setStyleSheet(stylesheet)

#         # Function to create and position labeled widgets
#         def add_labeled_widget(parent, label_text, widget, x, y, width, height):
#             label = create_label_qt6(label_text)
#             label.setParent(parent)
#             label.setGeometry(x, y, 128, 28)
            
#             widget.setParent(parent)
#             widget.setGeometry(x + 140, y, width, height)  # Adjust x-coordinate to the right of the label

#             # Connect widget signals to update summary text box
#             if isinstance(widget, SummaryTextBox):
#                 widget.update_summary.connect(self.update_summary_text_box)
#             else:
#                 if hasattr(widget, 'textChanged'):
#                     widget.textChanged.connect(self.update_summary_text_box)
#                 elif hasattr(widget, 'currentIndexChanged'):
#                     widget.currentIndexChanged.connect(self.update_summary_text_box)

#         # Create and position widgets with labels
#         add_labeled_widget(central_widget, "Serial Number:", create_serial_number_qt6(), 160, 48, 320, 28)
#         add_labeled_widget(central_widget, "Client Name:", create_client_name_qt6(), 160, 96, 320, 28)
#         add_labeled_widget(central_widget, "Campaign Name:", create_campaign_name_qt6(), 160, 144, 320, 28)
#         add_labeled_widget(central_widget, "Projekt Nickname:", create_projekt_nickname_qt6(), 160, 192, 320, 28)
#         add_labeled_widget(central_widget, "Bit Depth:", create_combo_box_bit_depth_qt6(), 160, 240, 320, 28)
#         add_labeled_widget(central_widget, "Frame Rate:", create_combo_box_frame_rate_qt6(), 160, 288, 320, 28)
#         add_labeled_widget(central_widget, "Scan Mode:", create_combo_box_scan_mode_qt6(), 160, 336, 320, 28)
#         add_labeled_widget(central_widget, "Color Science:", create_combo_box_color_science_qt6(), 160, 384, 320, 28)
#         add_labeled_widget(central_widget, "Start Frame:", create_combo_box_start_frame_qt6(), 160, 432, 320, 28)
#         add_labeled_widget(central_widget, "Summary:", SummaryTextBox(), 160, 480, 320, 140)
#         add_labeled_widget(central_widget, "Button:", CustomButton("Click Me"), 160, 624, 320, 28)

#     def update_summary_text_box(self, new_text):
#         if isinstance(new_text, str):
#             summary_text = new_text
#         elif isinstance(new_text, int):
#             summary_text = str(new_text)
#         else:
#             summary_text = ""

#         # Append to the summary text box
#         current_text = self.findChild(QTextEdit, "summary_textbox").toPlainText()
#         if current_text:
#             updated_text = f"{current_text}\n{summary_text}"
#         else:
#             updated_text = summary_text
#         self.findChild(QTextEdit, "summary_textbox").setPlainText(updated_text)

#     def apply_styles(self):
#         try:
#             self.setStyleSheet(stylesheet)  # Apply the stylesheet
#         except Exception as e:
#             QMessageBox.critical(self, "Error", str(e))














# from PySide6.QtWidgets import QMainWindow, QWidget, QMessageBox, QTextEdit
# from PySide6.QtGui import QAction

# from ...widgets.button.button import CustomButton
# from ...widgets.combo_box.combo_box_bit_depth import create_combo_box_bit_depth_qt6
# from ...widgets.combo_box.combo_box_frame_rate import create_combo_box_frame_rate_qt6
# from ...widgets.combo_box.combo_box_scan_mode import create_combo_box_scan_mode_qt6
# from ...widgets.combo_box.combo_box_color_science import create_combo_box_color_science_qt6
# from ...widgets.combo_box.combo_box_start_frame import create_combo_box_start_frame_qt6
# from ...widgets.line_edit.line_edit_projekt_namer import (
#     create_serial_number_qt6,
#     create_client_name_qt6,
#     create_campaign_name_qt6,
#     create_projekt_nickname_qt6,
# )
# from ...functions.label.label import create_label_qt6
# from ...widgets.style_sheet.logik_stylesheet import stylesheet
# from ...widgets.summary_textbox.summary_textbox import SummaryTextBox

# class MainWindow(QMainWindow):
#     def __init__(self):
#         super().__init__()
#         self.setWindowTitle("Logik Projekt Application")
#         self.setGeometry(100, 100, 1440, 960)  # Set the window size
        
#         self.initUI()
#         self.apply_styles()

#     def initUI(self):
#         central_widget = QWidget(self)
#         self.setCentralWidget(central_widget)
#         central_widget.setGeometry(0, 0, 1440, 960)  # Set central widget size
#         central_widget.setStyleSheet(stylesheet)

#         # Function to create and position labeled widgets
#         def add_labeled_widget(parent, label_text, widget, x, y, width, height):
#             label = create_label_qt6(label_text)
#             label.setParent(parent)
#             label.setGeometry(x, y, 128, 28)
            
#             widget.setParent(parent)
#             widget.setGeometry(x + 140, y, width, height)  # Adjust x-coordinate to the right of the label

#             # Connect widget signals to update summary text box
#             if isinstance(widget, SummaryTextBox):
#                 widget.update_summary.connect(self.update_summary_text_box)
#             else:
#                 if hasattr(widget, 'textChanged'):
#                     widget.textChanged.connect(lambda text, label=label_text: self.update_summary_text_box(f"{label}: {text}"))
#                 elif hasattr(widget, 'currentIndexChanged'):
#                     widget.currentIndexChanged.connect(lambda index, label=label_text: self.update_summary_text_box(f"{label}: {widget.currentText()}"))

#         # Create and position widgets with labels
#         add_labeled_widget(central_widget, "Serial Number:", create_serial_number_qt6(), 160, 48, 320, 28)
#         add_labeled_widget(central_widget, "Client Name:", create_client_name_qt6(), 160, 96, 320, 28)
#         add_labeled_widget(central_widget, "Campaign Name:", create_campaign_name_qt6(), 160, 144, 320, 28)
#         add_labeled_widget(central_widget, "Projekt Nickname:", create_projekt_nickname_qt6(), 160, 192, 320, 28)
#         add_labeled_widget(central_widget, "Bit Depth:", create_combo_box_bit_depth_qt6(), 160, 240, 320, 28)
#         add_labeled_widget(central_widget, "Frame Rate:", create_combo_box_frame_rate_qt6(), 160, 288, 320, 28)
#         add_labeled_widget(central_widget, "Scan Mode:", create_combo_box_scan_mode_qt6(), 160, 336, 320, 28)
#         add_labeled_widget(central_widget, "Color Science:", create_combo_box_color_science_qt6(), 160, 384, 320, 28)
#         add_labeled_widget(central_widget, "Start Frame:", create_combo_box_start_frame_qt6(), 160, 432, 320, 28)
#         add_labeled_widget(central_widget, "Summary:", SummaryTextBox(), 160, 480, 320, 140)
#         add_labeled_widget(central_widget, "Button:", CustomButton("Click Me"), 160, 624, 320, 28)

#     def update_summary_text_box(self, new_text):
#         current_text = self.findChild(QTextEdit, "summary_textbox").toPlainText()
#         if current_text:
#             updated_text = f"{current_text}\n{new_text}"
#         else:
#             updated_text = new_text
#         self.findChild(QTextEdit, "summary_textbox").setPlainText(updated_text)

#     def apply_styles(self):
#         try:
#             self.setStyleSheet(stylesheet)  # Apply the stylesheet
#         except Exception as e:
#             QMessageBox.critical(self, "Error", str(e))












# from PySide6.QtWidgets import QMainWindow, QWidget, QMessageBox, QTextEdit
# from PySide6.QtGui import QAction
# from PySide6.QtCore import Qt

# from ...widgets.button.button import CustomButton
# from ...widgets.combo_box.combo_box_resolution import create_combo_box_resolution_qt6
# from ...widgets.combo_box.combo_box_bit_depth import create_combo_box_bit_depth_qt6
# from ...widgets.combo_box.combo_box_frame_rate import create_combo_box_frame_rate_qt6
# from ...widgets.combo_box.combo_box_scan_mode import create_combo_box_scan_mode_qt6
# from ...widgets.combo_box.combo_box_color_science import create_combo_box_color_science_qt6
# from ...widgets.combo_box.combo_box_start_frame import create_combo_box_start_frame_qt6
# from ...widgets.line_edit.line_edit_projekt_namer import (
#     create_serial_number_qt6,
#     create_client_name_qt6,
#     create_campaign_name_qt6,
#     create_projekt_nickname_qt6,
# )
# from ...functions.label.label import create_label_qt6
# from ...widgets.style_sheet.logik_stylesheet import stylesheet
# from ...widgets.summary_textbox.summary_textbox import SummaryTextBox

# class MainWindow(QMainWindow):
#     def __init__(self):
#         super().__init__()
#         self.setWindowTitle("Logik Projekt Application")
#         self.setGeometry(100, 100, 1440, 960)  # Set the window size
        
#         self.initUI()
#         self.apply_styles()

#     def initUI(self):
#         central_widget = QWidget(self)
#         self.setCentralWidget(central_widget)
#         central_widget.setGeometry(0, 0, 1440, 960)  # Set central widget size
#         central_widget.setStyleSheet(stylesheet)

#         # Create the summary text box
#         self.summary_text_box = SummaryTextBox()
#         self.summary_text_box.setGeometry(160, 480, 320, 140)
#         self.summary_text_box.setParent(central_widget)

#         # Function to create and position labeled widgets
#         def add_labeled_widget(parent, label_text, widget, x, y, width, height):
#             label = create_label_qt6(label_text)
#             label.setParent(parent)
#             label.setGeometry(x, y, 128, 28)
            
#             widget.setParent(parent)
#             widget.setGeometry(x + 140, y, width, height)  # Adjust x-coordinate to the right of the label

#             # Connect widget signals to update summary text box
#             if isinstance(widget, QTextEdit):
#                 widget.update_summary.connect(self.update_summary_text_box)
#             elif hasattr(widget, 'textChanged'):
#                 widget.textChanged.connect(self.update_summary_text_box)
#             elif hasattr(widget, 'currentIndexChanged'):
#                 widget.currentIndexChanged.connect(self.update_summary_text_box)

#         # Create and position widgets with labels
#         add_labeled_widget(central_widget, "Serial Number:", create_serial_number_qt6(), 16, 48, 384, 28)
#         add_labeled_widget(central_widget, "Client Name:", create_client_name_qt6(), 16, 96, 384, 28)
#         add_labeled_widget(central_widget, "Campaign Name:", create_campaign_name_qt6(), 16, 144, 384, 28)
#         add_labeled_widget(central_widget, "Projekt Nickname:", create_projekt_nickname_qt6(), 16, 192, 384, 28)
#         add_labeled_widget(central_widget, "Resolution:", create_combo_box_resolution_qt6(), 16, 240, 384, 28)
#         add_labeled_widget(central_widget, "Bit Depth:", create_combo_box_bit_depth_qt6(), 16, 288, 384, 28)
#         add_labeled_widget(central_widget, "Frame Rate:", create_combo_box_frame_rate_qt6(), 16, 336, 384, 28)
#         add_labeled_widget(central_widget, "Scan Mode:", create_combo_box_scan_mode_qt6(), 16, 384, 384, 28)
#         add_labeled_widget(central_widget, "Color Science:", create_combo_box_color_science_qt6(), 16, 432, 384, 28)
#         add_labeled_widget(central_widget, "Start Frame:", create_combo_box_start_frame_qt6(), 16, 480, 384, 28)
#         add_labeled_widget(central_widget, "Button:", CustomButton("Click Me"), 16, 624, 384, 28)

#         # Update the summary box initially
#         self.update_summary_text_box()

#     def update_summary_text_box(self):
#         summary_lines = []
#         for child in self.centralWidget().children():
#             if isinstance(child, QWidget) and hasattr(child, 'parentWidget'):
#                 parent_widget = child.parentWidget()
#                 if isinstance(parent_widget, QWidget) and parent_widget.isVisible():
#                     if isinstance(child, QTextEdit):
#                         summary_lines.append(f"{parent_widget.windowTitle()}: {child.toPlainText().strip()}")
#                     elif isinstance(child, QLineEdit):
#                         summary_lines.append(f"{parent_widget.windowTitle()}: {child.text().strip()}")
#                     elif isinstance(child, QComboBox):
#                         summary_lines.append(f"{parent_widget.windowTitle()}: {child.currentText().strip()}")

#         summary_text = '\n'.join(summary_lines)
#         self.summary_text_box.setPlainText(summary_text)

#     def apply_styles(self):
#         try:
#             self.setStyleSheet(stylesheet)  # Apply the stylesheet
#         except Exception as e:
#             QMessageBox.critical(self, "Error", str(e))















# from PySide6.QtWidgets import QApplication, QMainWindow, QWidget, QMessageBox, QTextEdit, QLineEdit, QComboBox
# from PySide6.QtGui import QAction
# from PySide6.QtCore import Qt

# from ...widgets.button.button import CustomButton
# from ...widgets.combo_box.combo_box_resolution import create_combo_box_resolution_qt6
# from ...widgets.combo_box.combo_box_bit_depth import create_combo_box_bit_depth_qt6
# from ...widgets.combo_box.combo_box_frame_rate import create_combo_box_frame_rate_qt6
# from ...widgets.combo_box.combo_box_scan_mode import create_combo_box_scan_mode_qt6
# from ...widgets.combo_box.combo_box_color_science import create_combo_box_color_science_qt6
# from ...widgets.combo_box.combo_box_start_frame import create_combo_box_start_frame_qt6
# from ...widgets.line_edit.line_edit_projekt_namer import (
#     create_serial_number_qt6,
#     create_client_name_qt6,
#     create_campaign_name_qt6,
#     create_projekt_nickname_qt6,
# )
# from ...functions.label.label import create_label_qt6
# from ...functions.string_utilities.string_utilities import string_clean
# from ...widgets.style_sheet.logik_stylesheet import stylesheet
# from ...widgets.summary_textbox.summary_textbox import (
#     create_summary_textbox_qt6, 
#     update_summary_textbox_qt6
# )

# class MainWindow(QMainWindow):
#     def __init__(self):
#         super().__init__()
#         self.setWindowTitle("Logik Projekt Application")
#         self.setGeometry(100, 100, 1440, 960)  # Set the window size
        
#         self.initUI()
#         self.apply_styles()
#         self.center()

#     def initUI(self):
#         central_widget = QWidget(self)
#         self.setCentralWidget(central_widget)
#         central_widget.setGeometry(0, 0, 1440, 960)  # Set central widget size
#         central_widget.setStyleSheet(stylesheet)

#         # Function to create and position labeled widgets
#         def add_labeled_widget(parent, label_text, widget, x, y, width, height):
#             label = create_label_qt6(label_text)
#             label.setParent(parent)
#             label.setGeometry(x, y, 128, 28)
            
#             widget.setParent(parent)
#             widget.setGeometry(x + 140, y, width, height)  # Adjust x-coordinate to the right of the label

#             # Connect widget signals to update summary text box
#             if hasattr(widget, 'textChanged'):
#                 widget.textChanged.connect(self.update_summary_text_box)
#             elif hasattr(widget, 'currentIndexChanged'):
#                 widget.currentIndexChanged.connect(self.update_summary_text_box)

#         # Create and position widgets with labels
#         add_labeled_widget(central_widget, "Serial Number:", create_serial_number_qt6(), 16, 48, 384, 28)
#         add_labeled_widget(central_widget, "Client Name:", create_client_name_qt6(), 16, 96, 384, 28)
#         add_labeled_widget(central_widget, "Campaign Name:", create_campaign_name_qt6(), 16, 144, 384, 28)
#         add_labeled_widget(central_widget, "Projekt Nickname:", create_projekt_nickname_qt6(), 16, 192, 384, 28)
#         add_labeled_widget(central_widget, "Resolution:", create_combo_box_resolution_qt6(), 16, 240, 384, 28)
#         add_labeled_widget(central_widget, "Bit Depth:", create_combo_box_bit_depth_qt6(), 16, 288, 384, 28)
#         add_labeled_widget(central_widget, "Frame Rate:", create_combo_box_frame_rate_qt6(), 16, 336, 384, 28)
#         add_labeled_widget(central_widget, "Scan Mode:", create_combo_box_scan_mode_qt6(), 16, 384, 384, 28)
#         add_labeled_widget(central_widget, "Color Science:", create_combo_box_color_science_qt6(), 16, 432, 384, 28)
#         add_labeled_widget(central_widget, "Start Frame:", create_combo_box_start_frame_qt6(), 16, 480, 384, 28)
#         add_labeled_widget(central_widget, "Button:", CustomButton("Click Me"), 16, 624, 384, 28)

#     def update_summary_text_box(self):
#         summary_lines = []
#         for child in self.centralWidget().children():
#             if isinstance(child, QLineEdit):
#                 summary_lines.append(f"{child.placeholderText()}: {child.text().strip()}")
#             elif isinstance(child, QComboBox):
#                 summary_lines.append(f"{child.currentText().strip()}")

#         summary_text = '\n'.join(summary_lines)
#         print("Summary:\n" + summary_text)

#     def apply_styles(self):
#         try:
#             self.setStyleSheet(stylesheet)  # Apply the stylesheet
#         except Exception as e:
#             QMessageBox.critical(self, "Error", str(e))

#     def center(self):
#         screen = QApplication.primaryScreen()
#         screen_geometry = screen.availableGeometry()
#         window_geometry = self.frameGeometry()
#         window_geometry.moveCenter(screen_geometry.center())
#         self.move(window_geometry.topLeft())








# from PySide6.QtWidgets import QApplication, QMainWindow, QWidget, QMessageBox, QLineEdit, QComboBox
# from PySide6.QtGui import QAction
# from PySide6.QtCore import Qt

# from ...widgets.button.button import CustomButton
# from ...widgets.combo_box.combo_box_resolution import create_combo_box_resolution_qt6
# from ...widgets.combo_box.combo_box_bit_depth import create_combo_box_bit_depth_qt6
# from ...widgets.combo_box.combo_box_frame_rate import create_combo_box_frame_rate_qt6
# from ...widgets.combo_box.combo_box_scan_mode import create_combo_box_scan_mode_qt6
# from ...widgets.combo_box.combo_box_color_science import create_combo_box_color_science_qt6
# from ...widgets.combo_box.combo_box_start_frame import create_combo_box_start_frame_qt6
# from ...widgets.line_edit.line_edit_projekt_namer import (
#     create_serial_number_qt6,
#     create_client_name_qt6,
#     create_campaign_name_qt6,
#     create_projekt_nickname_qt6,
# )
# from ...functions.label.label import create_label_qt6
# from ...widgets.style_sheet.logik_stylesheet import stylesheet
# from ...widgets.summary_textbox.summary_textbox import (
#     create_summary_textbox_qt6, 
#     update_summary_textbox_qt6
# )

# class MainWindow(QMainWindow):
#     def __init__(self):
#         super().__init__()
#         self.setWindowTitle("Logik Projekt Application")
#         self.setGeometry(100, 100, 1440, 960)  # Set the window size
        
#         self.initUI()
#         self.apply_styles()
#         self.center()

#     def initUI(self):
#         central_widget = QWidget(self)
#         self.setCentralWidget(central_widget)
#         central_widget.setGeometry(0, 0, 1440, 960)  # Set central widget size
#         central_widget.setStyleSheet(stylesheet)

#         # Create the summary text box
#         self.summary_text_box = create_summary_textbox_qt6()
#         self.summary_text_box.setGeometry(160, 528, 384, 196)
#         self.summary_text_box.setParent(central_widget)

#         # Dictionary to store references to line edits and combo boxes
#         self.lineedits = {}
#         self.combo_boxes = {}

#         # Function to create and position labeled widgets
#         def add_labeled_widget(parent, label_text, widget, x, y, width, height):
#             label = create_label_qt6(label_text)
#             label.setParent(parent)
#             label.setGeometry(x, y, 128, 28)
            
#             widget.setParent(parent)
#             widget.setGeometry(x + 144, y, width, height)  # Adjust x-coordinate to the right of the label

#             # Store references to the widgets for summary updating
#             if isinstance(widget, QLineEdit):
#                 self.lineedits[label_text] = widget
#                 widget.textChanged.connect(self.update_summary_text_box)
#             elif isinstance(widget, QComboBox):
#                 self.combo_boxes[label_text] = widget
#                 widget.currentIndexChanged.connect(self.update_summary_text_box)

#         # Create and position widgets with labels
#         add_labeled_widget(central_widget, "Serial Number:", create_serial_number_qt6(), 16, 48, 384, 28)
#         add_labeled_widget(central_widget, "Client Name:", create_client_name_qt6(), 16, 96, 384, 28)
#         add_labeled_widget(central_widget, "Campaign Name:", create_campaign_name_qt6(), 16, 144, 384, 28)
#         add_labeled_widget(central_widget, "Projekt Nickname:", create_projekt_nickname_qt6(), 16, 192, 384, 28)
#         add_labeled_widget(central_widget, "Resolution:", create_combo_box_resolution_qt6(), 16, 240, 384, 28)
#         add_labeled_widget(central_widget, "Bit Depth:", create_combo_box_bit_depth_qt6(), 16, 288, 384, 28)
#         add_labeled_widget(central_widget, "Frame Rate:", create_combo_box_frame_rate_qt6(), 16, 336, 384, 28)
#         add_labeled_widget(central_widget, "Scan Mode:", create_combo_box_scan_mode_qt6(), 16, 384, 384, 28)
#         add_labeled_widget(central_widget, "Color Science:", create_combo_box_color_science_qt6(), 16, 432, 384, 28)
#         add_labeled_widget(central_widget, "Start Frame:", create_combo_box_start_frame_qt6(), 16, 480, 384, 28)
#         add_labeled_widget(central_widget, "Button:", CustomButton("Click Me"), 16, 816, 384, 28)

#         # Update the summary box initially
#         self.update_summary_text_box()

#     def update_summary_text_box(self):
#         update_summary_textbox_qt6(self.summary_text_box, self.lineedits, self.combo_boxes)

#     def apply_styles(self):
#         try:
#             self.setStyleSheet(stylesheet)  # Apply the stylesheet
#         except Exception as e:
#             QMessageBox.critical(self, "Error", str(e))

#     def center(self):
#         screen = QApplication.primaryScreen()
#         screen_geometry = screen.availableGeometry()
#         window_geometry = self.frameGeometry()
#         window_geometry.moveCenter(screen_geometry.center())
#         self.move(window_geometry.topLeft())













# from PySide6.QtWidgets import QApplication, QMainWindow, QWidget, QMessageBox, QLineEdit, QComboBox
# from PySide6.QtGui import QAction
# from PySide6.QtCore import Qt

# from ...widgets.button.button import CustomButton
# from ...widgets.combo_box.combo_box_resolution import create_combo_box_resolution_qt6
# from ...widgets.combo_box.combo_box_bit_depth import create_combo_box_bit_depth_qt6
# from ...widgets.combo_box.combo_box_frame_rate import create_combo_box_frame_rate_qt6
# from ...widgets.combo_box.combo_box_scan_mode import create_combo_box_scan_mode_qt6
# from ...widgets.combo_box.combo_box_color_science import create_combo_box_color_science_qt6
# from ...widgets.combo_box.combo_box_start_frame import create_combo_box_start_frame_qt6
# from ...widgets.line_edit.line_edit_projekt_namer import (
#     create_serial_number_qt6,
#     create_client_name_qt6,
#     create_campaign_name_qt6,
#     create_projekt_nickname_qt6,
# )
# from ...functions.label.label import create_label_qt6
# from ...functions.string_utilities.string_utilities import string_clean
# from ...widgets.style_sheet.logik_stylesheet import stylesheet
# from ...widgets.summary_textbox.summary_textbox import (
#     create_summary_textbox_qt6, 
#     update_summary_textbox_qt6
# )

# class MainWindow(QMainWindow):
#     def __init__(self):
#         super().__init__()
#         self.setWindowTitle("Logik Projekt Application")
#         self.setGeometry(100, 100, 1440, 960)  # Set the window size
        
#         self.initUI()
#         self.apply_styles()
#         self.center()

#     def initUI(self):
#         central_widget = QWidget(self)
#         self.setCentralWidget(central_widget)
#         central_widget.setGeometry(0, 0, 1440, 960)  # Set central widget size
#         central_widget.setStyleSheet(stylesheet)

#         # Create the summary text box
#         self.summary_text_box = create_summary_textbox_qt6()
#         self.summary_text_box.setGeometry(160, 528, 384, 196)
#         self.summary_text_box.setParent(central_widget)

#         # Dictionary to store references to line edits and combo boxes
#         self.lineedits = {}
#         self.combo_boxes = {}

#         # Function to create and position labeled widgets
#         def add_labeled_widget(parent, label_text, widget, x, y, width, height):
#             label = create_label_qt6(label_text)
#             label.setParent(parent)
#             label.setGeometry(x, y, 128, 28)
            
#             widget.setParent(parent)
#             widget.setGeometry(x + 140, y, width, height)  # Adjust x-coordinate to the right of the label

#             # Store references to the widgets for summary updating
#             if isinstance(widget, QLineEdit):
#                 self.lineedits[label_text] = widget
#                 widget.textChanged.connect(self.update_summary_text_box)
#             elif isinstance(widget, QComboBox):
#                 self.combo_boxes[label_text] = widget
#                 widget.currentIndexChanged.connect(self.update_summary_text_box)

#         # Create and position widgets with labels
#         add_labeled_widget(central_widget, "Serial Number:", create_serial_number_qt6(), 16, 48, 384, 28)
#         add_labeled_widget(central_widget, "Client Name:", create_client_name_qt6(), 16, 96, 384, 28)
#         add_labeled_widget(central_widget, "Campaign Name:", create_campaign_name_qt6(), 16, 144, 384, 28)
#         add_labeled_widget(central_widget, "Projekt Nickname:", create_projekt_nickname_qt6(), 16, 192, 384, 28)
#         add_labeled_widget(central_widget, "Resolution:", create_combo_box_resolution_qt6(), 16, 240, 384, 28)
#         add_labeled_widget(central_widget, "Bit Depth:", create_combo_box_bit_depth_qt6(), 16, 288, 384, 28)
#         add_labeled_widget(central_widget, "Frame Rate:", create_combo_box_frame_rate_qt6(), 16, 336, 384, 28)
#         add_labeled_widget(central_widget, "Scan Mode:", create_combo_box_scan_mode_qt6(), 16, 384, 384, 28)
#         add_labeled_widget(central_widget, "Color Science:", create_combo_box_color_science_qt6(), 16, 432, 384, 28)
#         add_labeled_widget(central_widget, "Start Frame:", create_combo_box_start_frame_qt6(), 16, 480, 384, 28)
#         add_labeled_widget(central_widget, "Button:", CustomButton("Click Me"), 16, 816, 384, 28)

#         # Update the summary box initially
#         self.update_summary_text_box()

#     def update_summary_text_box(self):
#         summary_lines = []
#         for label, lineedit in self.lineedits.items():
#             summary_lines.append(f"{label}: {string_clean(lineedit.text())}")
        
#         for label, combo_box in self.combo_boxes.items():
#             if label == "Resolution:":
#                 value_data = combo_box.itemData(combo_box.currentIndex())
#                 if value_data:
#                     summary_lines.append(f"{label} {value_data['width']} x {value_data['height']}")
#             else:
#                 summary_lines.append(f"{label}: {combo_box.currentText()}")

#         summary_text = '\n'.join(summary_lines)
#         self.summary_text_box.setPlainText(summary_text)

#     def apply_styles(self):
#         try:
#             self.setStyleSheet(stylesheet)  # Apply the stylesheet
#         except Exception as e:
#             QMessageBox.critical(self, "Error", str(e))

#     def center(self):
#         screen = QApplication.primaryScreen()
#         screen_geometry = screen.availableGeometry()
#         window_geometry = self.frameGeometry()
#         window_geometry.moveCenter(screen_geometry.center())
#         self.move(window_geometry.topLeft())









# from PySide6.QtWidgets import QApplication, QMainWindow, QWidget, QMessageBox, QLineEdit, QComboBox
# from PySide6.QtGui import QAction
# from PySide6.QtCore import Qt

# from ...widgets.button.button import CustomButton
# from ...widgets.combo_box.combo_box_resolution import create_combo_box_resolution_qt6
# from ...widgets.combo_box.combo_box_bit_depth import create_combo_box_bit_depth_qt6
# from ...widgets.combo_box.combo_box_frame_rate import create_combo_box_frame_rate_qt6
# from ...widgets.combo_box.combo_box_scan_mode import create_combo_box_scan_mode_qt6
# from ...widgets.combo_box.combo_box_color_science import create_combo_box_color_science_qt6
# from ...widgets.combo_box.combo_box_start_frame import create_combo_box_start_frame_qt6
# from ...widgets.line_edit.line_edit_projekt_namer import (
#     create_serial_number_qt6,
#     create_client_name_qt6,
#     create_campaign_name_qt6,
#     create_projekt_nickname_qt6,
# )
# from ...functions.label.label import create_label_qt6
# from ...functions.string_utilities.string_utilities import string_clean
# from ...widgets.style_sheet.logik_stylesheet import stylesheet
# from ...widgets.summary_textbox.summary_textbox import (
#     create_summary_textbox_qt6, 
#     update_summary_textbox_qt6
# )

# class MainWindow(QMainWindow):
#     def __init__(self):
#         super().__init__()
#         self.setWindowTitle("Logik Projekt Application")
#         self.setGeometry(100, 100, 1440, 960)  # Set the window size
        
#         self.initUI()
#         self.apply_styles()
#         self.center()

#     def initUI(self):
#         central_widget = QWidget(self)
#         self.setCentralWidget(central_widget)
#         central_widget.setGeometry(0, 0, 1440, 960)  # Set central widget size
#         central_widget.setStyleSheet(stylesheet)

#         # Create the summary text box
#         self.summary_text_box = create_summary_textbox_qt6()
#         self.summary_text_box.setGeometry(160, 528, 384, 216)
#         self.summary_text_box.setParent(central_widget)

#         # Dictionary to store references to line edits and combo boxes
#         self.lineedits = {}
#         self.combo_boxes = {}

#         # Function to create and position labeled widgets
#         def add_labeled_widget(parent, label_text, widget, x, y, width, height):
#             label = create_label_qt6(label_text)
#             label.setParent(parent)
#             label.setGeometry(x, y, 128, 28)
            
#             widget.setParent(parent)
#             widget.setGeometry(x + 144, y, width, height)  # Adjust x-coordinate to the right of the label

#             # Store references to the widgets for summary updating
#             if isinstance(widget, QLineEdit):
#                 self.lineedits[label_text] = widget
#                 widget.textChanged.connect(self.update_summary_text_box)
#             elif isinstance(widget, QComboBox):
#                 self.combo_boxes[label_text] = widget
#                 widget.currentIndexChanged.connect(self.update_summary_text_box)

#         # Create and position widgets with labels
#         add_labeled_widget(central_widget, "Serial Number:", create_serial_number_qt6(), 16, 48, 384, 28)
#         add_labeled_widget(central_widget, "Client Name:", create_client_name_qt6(), 16, 96, 384, 28)
#         add_labeled_widget(central_widget, "Campaign Name:", create_campaign_name_qt6(), 16, 144, 384, 28)
#         add_labeled_widget(central_widget, "Projekt Nickname:", create_projekt_nickname_qt6(), 16, 192, 384, 28)
#         add_labeled_widget(central_widget, "Resolution:", create_combo_box_resolution_qt6(), 16, 240, 384, 28)
#         add_labeled_widget(central_widget, "Bit Depth:", create_combo_box_bit_depth_qt6(), 16, 288, 384, 28)
#         add_labeled_widget(central_widget, "Frame Rate:", create_combo_box_frame_rate_qt6(), 16, 336, 384, 28)
#         add_labeled_widget(central_widget, "Scan Mode:", create_combo_box_scan_mode_qt6(), 16, 384, 384, 28)
#         add_labeled_widget(central_widget, "Color Science:", create_combo_box_color_science_qt6(), 16, 432, 384, 28)
#         add_labeled_widget(central_widget, "Start Frame:", create_combo_box_start_frame_qt6(), 16, 480, 384, 28)
#         add_labeled_widget(central_widget, "Button:", CustomButton("Click Me"), 16, 816, 384, 28)

#         # Update the summary box initially
#         self.update_summary_text_box()

#     def update_summary_text_box(self):
#         summary_lines = []
#         projekt_serial = self.lineedits["Serial Number:"].text().strip()
#         projekt_client = self.lineedits["Client Name:"].text().strip()
#         projekt_campaign = self.lineedits["Campaign Name:"].text().strip()

#         # Construct projekt_nickname based on conditions
#         if not projekt_client or not projekt_campaign:
#             projekt_nickname = ""
#         elif projekt_serial:
#             projekt_nickname = f"{projekt_serial}_{projekt_client}_{projekt_campaign}"
#         else:
#             projekt_nickname = f"{projekt_client}_{projekt_campaign}"

#         self.lineedits["Projekt Nickname:"].setText(projekt_nickname)

#         for label, lineedit in self.lineedits.items():
#             summary_lines.append(f"{label} {string_clean(lineedit.text())}")

#         for label, combo_box in self.combo_boxes.items():
#             if label == "Resolution:":
#                 value_data = combo_box.itemData(combo_box.currentIndex())
#                 if value_data:
#                     summary_lines.append(f"{label} {value_data['width']} x {value_data['height']}")
#             else:
#                 summary_lines.append(f"{label} {combo_box.currentText()}")

#         summary_text = '\n'.join(summary_lines)
#         self.summary_text_box.setPlainText(summary_text)

#     def apply_styles(self):
#         try:
#             self.setStyleSheet(stylesheet)  # Apply the stylesheet
#         except Exception as e:
#             QMessageBox.critical(self, "Error", str(e))

#     def center(self):
#         screen = QApplication.primaryScreen()
#         screen_geometry = screen.availableGeometry()
#         window_geometry = self.frameGeometry()
#         window_geometry.moveCenter(screen_geometry.center())
#         self.move(window_geometry.topLeft())















# from PySide6.QtWidgets import QApplication, QMainWindow, QWidget, QMessageBox, QLineEdit, QComboBox
# from PySide6.QtGui import QAction
# from PySide6.QtCore import Qt

# from ...widgets.button.button import CustomButton
# from ...widgets.combo_box.combo_box_resolution import create_combo_box_resolution_qt6
# from ...widgets.combo_box.combo_box_bit_depth import create_combo_box_bit_depth_qt6
# from ...widgets.combo_box.combo_box_frame_rate import create_combo_box_frame_rate_qt6
# from ...widgets.combo_box.combo_box_scan_mode import create_combo_box_scan_mode_qt6
# from ...widgets.combo_box.combo_box_color_science import create_combo_box_color_science_qt6
# from ...widgets.combo_box.combo_box_start_frame import create_combo_box_start_frame_qt6
# from ...widgets.line_edit.line_edit_projekt_namer import (
#     create_serial_number_qt6,
#     create_client_name_qt6,
#     create_campaign_name_qt6,
#     create_projekt_nickname_qt6,
# )
# from ...functions.label.label import create_label_qt6
# from ...functions.string_utilities.string_utilities import string_clean
# from ...widgets.style_sheet.logik_stylesheet import stylesheet
# from ...widgets.summary_textbox.summary_textbox import (
#     create_summary_textbox_qt6, 
#     update_summary_textbox_qt6
# )

# class MainWindow(QMainWindow):
#     def __init__(self):
#         super().__init__()
#         self.setWindowTitle("Logik Projekt Application")
#         self.setGeometry(100, 100, 1440, 960)  # Set the window size
        
#         self.initUI()
#         self.apply_styles()
#         self.center()

#     def initUI(self):
#         central_widget = QWidget(self)
#         self.setCentralWidget(central_widget)
#         central_widget.setGeometry(0, 0, 1440, 960)  # Set central widget size
#         central_widget.setStyleSheet(stylesheet)

#         # Create the summary text box
#         self.summary_text_box = create_summary_textbox_qt6()
#         self.summary_text_box.setGeometry(16, 528, 528, 216)
#         self.summary_text_box.setParent(central_widget)

#         # Dictionary to store references to line edits and combo boxes
#         self.lineedits = {}
#         self.combo_boxes = {}

#         # Function to create and position labeled widgets
#         def add_labeled_widget(parent, label_text, widget, x, y, width, height):
#             label = create_label_qt6(label_text)
#             label.setParent(parent)
#             label.setGeometry(x, y, 128, 28)
            
#             widget.setParent(parent)
#             widget.setGeometry(x + 144, y, width, height)  # Adjust x-coordinate to the right of the label

#             # Store references to the widgets for summary updating
#             if isinstance(widget, QLineEdit):
#                 self.lineedits[label_text] = widget
#                 widget.textChanged.connect(self.update_summary_text_box)
#             elif isinstance(widget, QComboBox):
#                 self.combo_boxes[label_text] = widget
#                 widget.currentIndexChanged.connect(self.update_summary_text_box)

#         # Create and position widgets with labels
#         add_labeled_widget(central_widget, "Serial Number:", create_serial_number_qt6(), 16, 48, 384, 28)
#         add_labeled_widget(central_widget, "Client Name:", create_client_name_qt6(), 16, 96, 384, 28)
#         add_labeled_widget(central_widget, "Campaign Name:", create_campaign_name_qt6(), 16, 144, 384, 28)
#         projekt_nickname_edit = create_projekt_nickname_qt6()
#         projekt_nickname_edit.setReadOnly(True)  # Set to read-only
#         add_labeled_widget(central_widget, "Projekt Nickname:", projekt_nickname_edit, 16, 192, 384, 28)
#         add_labeled_widget(central_widget, "Resolution:", create_combo_box_resolution_qt6(), 16, 240, 384, 28)
#         add_labeled_widget(central_widget, "Bit Depth:", create_combo_box_bit_depth_qt6(), 16, 288, 384, 28)
#         add_labeled_widget(central_widget, "Frame Rate:", create_combo_box_frame_rate_qt6(), 16, 336, 384, 28)
#         add_labeled_widget(central_widget, "Scan Mode:", create_combo_box_scan_mode_qt6(), 16, 384, 384, 28)
#         add_labeled_widget(central_widget, "Color Science:", create_combo_box_color_science_qt6(), 16, 432, 384, 28)
#         add_labeled_widget(central_widget, "Start Frame:", create_combo_box_start_frame_qt6(), 16, 480, 384, 28)
#         add_labeled_widget(central_widget, "Button:", CustomButton("Click Me"), 16, 816, 384, 28)

#         # Update the summary box initially
#         self.update_summary_text_box()

#     def update_summary_text_box(self):
#         summary_lines = []
#         projekt_serial = string_clean(self.lineedits["Serial Number:"].text().strip())
#         projekt_client = string_clean(self.lineedits["Client Name:"].text().strip())
#         projekt_campaign = string_clean(self.lineedits["Campaign Name:"].text().strip())

#         # Construct projekt_nickname based on conditions
#         if not projekt_client or not projekt_campaign:
#             projekt_nickname = ""
#         elif projekt_serial:
#             projekt_nickname = f"{projekt_serial}_{projekt_client}_{projekt_campaign}"
#         else:
#             projekt_nickname = f"{projekt_client}_{projekt_campaign}"

#         self.lineedits["Projekt Nickname:"].setText(projekt_nickname)

#         for label, lineedit in self.lineedits.items():
#             summary_lines.append(f"{label} {string_clean(lineedit.text())}")

#         for label, combo_box in self.combo_boxes.items():
#             if label == "Resolution:":
#                 value_data = combo_box.itemData(combo_box.currentIndex())
#                 if value_data:
#                     summary_lines.append(f"{label} {value_data['width']} x {value_data['height']}")
#             else:
#                 summary_lines.append(f"{label} {combo_box.currentText()}")

#         summary_text = '\n'.join(summary_lines)
#         self.summary_text_box.setPlainText(summary_text)

#     def apply_styles(self):
#         try:
#             self.setStyleSheet(stylesheet)  # Apply the stylesheet
#         except Exception as e:
#             QMessageBox.critical(self, "Error", str(e))

#     def center(self):
#         screen = QApplication.primaryScreen()
#         screen_geometry = screen.availableGeometry()
#         window_geometry = self.frameGeometry()
#         window_geometry.moveCenter(screen_geometry.center())
#         self.move(window_geometry.topLeft())

# if __name__ == "__main__":
#     import sys
#     app = QApplication(sys.argv)
#     mainWin = MainWindow()
#     mainWin.show()
#     sys.exit(app.exec())
















# from PySide6.QtWidgets import QApplication, QMainWindow, QWidget, QMessageBox, QLineEdit, QComboBox, QFileDialog
# from PySide6.QtGui import QAction
# from PySide6.QtCore import Qt

# from ...widgets.button.button import CustomButton
# from ...widgets.combo_box.combo_box_resolution import create_combo_box_resolution_qt6
# from ...widgets.combo_box.combo_box_bit_depth import create_combo_box_bit_depth_qt6
# from ...widgets.combo_box.combo_box_frame_rate import create_combo_box_frame_rate_qt6
# from ...widgets.combo_box.combo_box_scan_mode import create_combo_box_scan_mode_qt6
# from ...widgets.combo_box.combo_box_color_science import create_combo_box_color_science_qt6
# from ...widgets.combo_box.combo_box_start_frame import create_combo_box_start_frame_qt6
# from ...widgets.line_edit.line_edit_projekt_namer import (
#     create_serial_number_qt6,
#     create_client_name_qt6,
#     create_campaign_name_qt6,
#     create_projekt_nickname_qt6,
# )
# from ...functions.label.label import create_label_qt6
# from ...functions.string_utilities.string_utilities import string_clean
# from ...widgets.style_sheet.logik_stylesheet import stylesheet
# from ...widgets.summary_textbox.summary_textbox import (
#     create_summary_textbox_qt6, 
#     update_summary_textbox_qt6
# )
# from ...functions.saver.template_saver import projekt_template_saver_qt6

# class MainWindow(QMainWindow):
#     def __init__(self):
#         super().__init__()
#         self.setWindowTitle("Logik Projekt Application")
#         self.setGeometry(100, 100, 1440, 960)  # Set the window size
        
#         self.initUI()
#         self.apply_styles()
#         self.center()

#     def initUI(self):
#         central_widget = QWidget(self)
#         self.setCentralWidget(central_widget)
#         central_widget.setGeometry(0, 0, 1440, 960)  # Set central widget size
#         central_widget.setStyleSheet(stylesheet)

#         # Create the summary text box
#         self.summary_text_box = create_summary_textbox_qt6()
#         self.summary_text_box.setGeometry(160, 528, 384, 216)
#         self.summary_text_box.setParent(central_widget)

#         # Dictionary to store references to line edits and combo boxes
#         self.lineedits = {}
#         self.combo_boxes = {}

#         # Function to create and position labeled widgets
#         def add_labeled_widget(parent, label_text, widget, x, y, width, height):
#             label = create_label_qt6(label_text)
#             label.setParent(parent)
#             label.setGeometry(x, y, 128, 28)
            
#             widget.setParent(parent)
#             widget.setGeometry(x + 144, y, width, height)  # Adjust x-coordinate to the right of the label

#             # Store references to the widgets for summary updating
#             if isinstance(widget, QLineEdit):
#                 self.lineedits[label_text] = widget
#                 widget.textChanged.connect(self.update_summary_text_box)
#             elif isinstance(widget, QComboBox):
#                 self.combo_boxes[label_text] = widget
#                 widget.currentIndexChanged.connect(self.update_summary_text_box)

#         # Create and position widgets with labels
#         add_labeled_widget(central_widget, "Serial Number:", create_serial_number_qt6(), 16, 48, 384, 28)
#         add_labeled_widget(central_widget, "Client Name:", create_client_name_qt6(), 16, 96, 384, 28)
#         add_labeled_widget(central_widget, "Campaign Name:", create_campaign_name_qt6(), 16, 144, 384, 28)
#         projekt_nickname_edit = create_projekt_nickname_qt6()
#         projekt_nickname_edit.setReadOnly(True)  # Set to read-only
#         add_labeled_widget(central_widget, "Projekt Nickname:", projekt_nickname_edit, 16, 192, 384, 28)
#         add_labeled_widget(central_widget, "Resolution:", create_combo_box_resolution_qt6(), 16, 240, 384, 28)
#         add_labeled_widget(central_widget, "Bit Depth:", create_combo_box_bit_depth_qt6(), 16, 288, 384, 28)
#         add_labeled_widget(central_widget, "Frame Rate:", create_combo_box_frame_rate_qt6(), 16, 336, 384, 28)
#         add_labeled_widget(central_widget, "Scan Mode:", create_combo_box_scan_mode_qt6(), 16, 384, 384, 28)
#         add_labeled_widget(central_widget, "Color Science:", create_combo_box_color_science_qt6(), 16, 432, 384, 28)
#         add_labeled_widget(central_widget, "Start Frame:", create_combo_box_start_frame_qt6(), 16, 480, 384, 28)
        
#         # Create and position the save button
#         save_button = CustomButton("Save Template")
#         save_button.setParent(central_widget)
#         save_button.setGeometry(16, 816, 384, 28)
#         save_button.clicked.connect(self.save_template)  # Connect the save button to the save_template function

#         # Update the summary box initially
#         self.update_summary_text_box()

#     def update_summary_text_box(self):
#         summary_lines = []
#         projekt_serial = string_clean(self.lineedits["Serial Number:"].text().strip())
#         projekt_client = string_clean(self.lineedits["Client Name:"].text().strip())
#         projekt_campaign = string_clean(self.lineedits["Campaign Name:"].text().strip())

#         # Construct projekt_nickname based on conditions
#         if not projekt_client or not projekt_campaign:
#             projekt_nickname = ""
#         elif projekt_serial:
#             projekt_nickname = f"{projekt_serial}_{projekt_client}_{projekt_campaign}"
#         else:
#             projekt_nickname = f"{projekt_client}_{projekt_campaign}"

#         self.lineedits["Projekt Nickname:"].setText(projekt_nickname)

#         for label, lineedit in self.lineedits.items():
#             summary_lines.append(f"{label} {string_clean(lineedit.text())}")

#         for label, combo_box in self.combo_boxes.items():
#             if label == "Resolution:":
#                 value_data = combo_box.itemData(combo_box.currentIndex())
#                 if value_data:
#                     summary_lines.append(f"{label} {value_data['width']} x {value_data['height']}")
#             else:
#                 summary_lines.append(f"{label} {combo_box.currentText()}")

#         summary_text = '\n'.join(summary_lines)
#         self.summary_text_box.setPlainText(summary_text)

#     def save_template(self):
#         summary_text = self.summary_text_box.toPlainText()
#         projekt_template_saver_qt6(self, summary_text)

#     def apply_styles(self):
#         try:
#             self.setStyleSheet(stylesheet)  # Apply the stylesheet
#         except Exception as e:
#             QMessageBox.critical(self, "Error", str(e))

#     def center(self):
#         screen = QApplication.primaryScreen()
#         screen_geometry = screen.availableGeometry()
#         window_geometry = self.frameGeometry()
#         window_geometry.moveCenter(screen_geometry.center())
#         self.move(window_geometry.topLeft())

# if __name__ == "__main__":
#     import sys
#     app = QApplication(sys.argv)
#     mainWin = MainWindow()
#     mainWin.show()
#     sys.exit(app.exec())
















# from PySide6.QtWidgets import QApplication, QMainWindow, QWidget, QMessageBox, QLineEdit, QComboBox, QFileDialog
# from PySide6.QtGui import QAction
# from PySide6.QtCore import Qt

# from ...widgets.button.button import CustomButton
# from ...widgets.combo_box.combo_box_resolution import create_combo_box_resolution_qt6
# from ...widgets.combo_box.combo_box_bit_depth import create_combo_box_bit_depth_qt6
# from ...widgets.combo_box.combo_box_frame_rate import create_combo_box_frame_rate_qt6
# from ...widgets.combo_box.combo_box_scan_mode import create_combo_box_scan_mode_qt6
# from ...widgets.combo_box.combo_box_color_science import create_combo_box_color_science_qt6
# from ...widgets.combo_box.combo_box_start_frame import create_combo_box_start_frame_qt6
# from ...widgets.line_edit.line_edit_projekt_namer import (
#     create_serial_number_qt6,
#     create_client_name_qt6,
#     create_campaign_name_qt6,
#     create_projekt_nickname_qt6,
# )
# from ...functions.label.label import create_label_qt6
# from ...functions.string_utilities.string_utilities import string_clean
# from ...widgets.style_sheet.logik_stylesheet import stylesheet
# from ...widgets.summary_textbox.summary_textbox import (
#     create_summary_textbox_qt6, 
#     update_summary_textbox_qt6
# )
# from ...functions.saver.template_saver import projekt_template_saver_qt6

# class MainWindow(QMainWindow):
#     def __init__(self):
#         super().__init__()
#         self.setWindowTitle("Logik Projekt Application")
#         self.setGeometry(100, 100, 1440, 960)  # Set the window size
        
#         self.initUI()
#         self.apply_styles()
#         self.center()

#     def initUI(self):
#         central_widget = QWidget(self)
#         self.setCentralWidget(central_widget)
#         central_widget.setGeometry(0, 0, 1440, 960)  # Set central widget size
#         central_widget.setStyleSheet(stylesheet)

#         # Create the summary text box
#         self.summary_text_box = create_summary_textbox_qt6()
#         self.summary_text_box.setGeometry(160, 528, 384, 216)
#         self.summary_text_box.setParent(central_widget)

#         # Dictionary to store references to line edits and combo boxes
#         self.lineedits = {}
#         self.combo_boxes = {}

#         # Function to create and position labeled widgets
#         def add_labeled_widget(parent, label_text, widget, x, y, width, height):
#             label = create_label_qt6(label_text)
#             label.setParent(parent)
#             label.setGeometry(x, y, 128, 28)
            
#             widget.setParent(parent)
#             widget.setGeometry(x + 144, y, width, height)  # Adjust x-coordinate to the right of the label

#             # Store references to the widgets for summary updating
#             if isinstance(widget, QLineEdit):
#                 self.lineedits[label_text] = widget
#                 widget.textChanged.connect(self.update_summary_text_box)
#             elif isinstance(widget, QComboBox):
#                 self.combo_boxes[label_text] = widget
#                 widget.currentIndexChanged.connect(self.update_summary_text_box)

#         # Create and position widgets with labels
#         add_labeled_widget(central_widget, "Serial Number:", create_serial_number_qt6(), 16, 48, 384, 28)
#         add_labeled_widget(central_widget, "Client Name:", create_client_name_qt6(), 16, 96, 384, 28)
#         add_labeled_widget(central_widget, "Campaign Name:", create_campaign_name_qt6(), 16, 144, 384, 28)
#         projekt_nickname_edit = create_projekt_nickname_qt6()
#         projekt_nickname_edit.setReadOnly(True)  # Set to read-only
#         add_labeled_widget(central_widget, "Projekt Nickname:", projekt_nickname_edit, 16, 192, 384, 28)
#         add_labeled_widget(central_widget, "Resolution:", create_combo_box_resolution_qt6(), 16, 240, 384, 28)
#         add_labeled_widget(central_widget, "Bit Depth:", create_combo_box_bit_depth_qt6(), 16, 288, 384, 28)
#         add_labeled_widget(central_widget, "Frame Rate:", create_combo_box_frame_rate_qt6(), 16, 336, 384, 28)
#         add_labeled_widget(central_widget, "Scan Mode:", create_combo_box_scan_mode_qt6(), 16, 384, 384, 28)
#         add_labeled_widget(central_widget, "Color Science:", create_combo_box_color_science_qt6(), 16, 432, 384, 28)
#         add_labeled_widget(central_widget, "Start Frame:", create_combo_box_start_frame_qt6(), 16, 480, 384, 28)
        
#         # Create and position the save button
#         save_button = CustomButton("Save Template")
#         save_button.setParent(central_widget)
#         save_button.setGeometry(16, 816, 384, 28)
#         save_button.clicked.connect(self.save_template)  # Connect the save button to the save_template function

#         # Update the summary box initially
#         self.update_summary_text_box()

#     def update_summary_text_box(self):
#         summary_lines = []
#         projekt_serial = string_clean(self.lineedits["Serial Number:"].text().strip())
#         projekt_client = string_clean(self.lineedits["Client Name:"].text().strip())
#         projekt_campaign = string_clean(self.lineedits["Campaign Name:"].text().strip())

#         # Construct projekt_nickname based on conditions
#         if not projekt_client or not projekt_campaign:
#             projekt_nickname = ""
#         elif projekt_serial:
#             projekt_nickname = f"{projekt_serial}_{projekt_client}_{projekt_campaign}"
#         else:
#             projekt_nickname = f"{projekt_client}_{projekt_campaign}"

#         self.lineedits["Projekt Nickname:"].setText(projekt_nickname)

#         for label, lineedit in self.lineedits.items():
#             summary_lines.append(f"{label} {string_clean(lineedit.text())}")

#         for label, combo_box in self.combo_boxes.items():
#             if label == "Resolution:":
#                 value_data = combo_box.itemData(combo_box.currentIndex())
#                 if value_data:
#                     summary_lines.append(f"{label} {value_data['width']} x {value_data['height']}")
#             else:
#                 summary_lines.append(f"{label} {combo_box.currentText()}")

#         summary_text = '\n'.join(summary_lines)
#         self.summary_text_box.setPlainText(summary_text)

#     def save_template(self):
#         summary_text = self.summary_text_box.toPlainText()
#         projekt_nickname = self.lineedits["Projekt Nickname:"].text()
#         projekt_template_saver_qt6(self, summary_text, projekt_nickname)

#     def apply_styles(self):
#         try:
#             self.setStyleSheet(stylesheet)  # Apply the stylesheet
#         except Exception as e:
#             QMessageBox.critical(self, "Error", str(e))

#     def center(self):
#         screen = QApplication.primaryScreen()
#         screen_geometry = screen.availableGeometry()
#         window_geometry = self.frameGeometry()
#         window_geometry.moveCenter(screen_geometry.center())
#         self.move(window_geometry.topLeft())

# if __name__ == "__main__":
#     import sys
#     app = QApplication(sys.argv)
#     mainWin = MainWindow()
#     mainWin.show()
#     sys.exit(app.exec())















# from PySide6.QtWidgets import QApplication, QMainWindow, QWidget, QMessageBox, QLineEdit, QComboBox, QFileDialog
# from PySide6.QtGui import QAction
# from PySide6.QtCore import Qt

# from ...widgets.button.button import CustomButton
# from ...widgets.combo_box.combo_box_resolution import create_combo_box_resolution_qt6
# from ...widgets.combo_box.combo_box_bit_depth import create_combo_box_bit_depth_qt6
# from ...widgets.combo_box.combo_box_frame_rate import create_combo_box_frame_rate_qt6
# from ...widgets.combo_box.combo_box_scan_mode import create_combo_box_scan_mode_qt6
# from ...widgets.combo_box.combo_box_color_science import create_combo_box_color_science_qt6
# from ...widgets.combo_box.combo_box_start_frame import create_combo_box_start_frame_qt6
# from ...widgets.line_edit.line_edit_projekt_namer import (
#     create_serial_number_qt6,
#     create_client_name_qt6,
#     create_campaign_name_qt6,
#     create_projekt_nickname_qt6,
# )
# from ...functions.label.label import create_label_qt6
# from ...functions.string_utilities.string_utilities import string_clean
# from ...widgets.style_sheet.logik_stylesheet import stylesheet
# from ...widgets.summary_textbox.summary_textbox import (
#     create_summary_textbox_qt6, 
#     update_summary_textbox_qt6
# )
# from ...functions.saver.template_saver import projekt_template_saver_qt6

# class MainWindow(QMainWindow):
#     def __init__(self):
#         super().__init__()
#         self.setWindowTitle("Logik Projekt Application")
#         self.setGeometry(100, 100, 1440, 960)  # Set the window size
        
#         self.initUI()
#         self.apply_styles()
#         self.center()

#     def initUI(self):
#         central_widget = QWidget(self)
#         self.setCentralWidget(central_widget)
#         central_widget.setGeometry(0, 0, 1440, 960)  # Set central widget size
#         central_widget.setStyleSheet(stylesheet)

#         # Create the summary text box
#         self.summary_text_box = create_summary_textbox_qt6()
#         self.summary_text_box.setGeometry(160, 528, 384, 216)
#         self.summary_text_box.setParent(central_widget)

#         # Dictionary to store references to line edits and combo boxes
#         self.lineedits = {}
#         self.combo_boxes = {}

#         # Function to create and position labeled widgets
#         def add_labeled_widget(parent, label_text, widget, x, y, width, height):
#             label = create_label_qt6(label_text)
#             label.setParent(parent)
#             label.setGeometry(x, y, 128, 28)
            
#             widget.setParent(parent)
#             widget.setGeometry(x + 144, y, width, height)  # Adjust x-coordinate to the right of the label

#             # Store references to the widgets for summary updating
#             if isinstance(widget, QLineEdit):
#                 self.lineedits[label_text] = widget
#                 widget.textChanged.connect(self.update_summary_text_box)
#             elif isinstance(widget, QComboBox):
#                 self.combo_boxes[label_text] = widget
#                 widget.currentIndexChanged.connect(self.update_summary_text_box)

#         # Create and position widgets with labels
#         add_labeled_widget(central_widget, "Serial Number:", create_serial_number_qt6(), 16, 48, 384, 28)
#         add_labeled_widget(central_widget, "Client Name:", create_client_name_qt6(), 16, 96, 384, 28)
#         add_labeled_widget(central_widget, "Campaign Name:", create_campaign_name_qt6(), 16, 144, 384, 28)
#         projekt_nickname_edit = create_projekt_nickname_qt6()
#         projekt_nickname_edit.setReadOnly(True)  # Set to read-only
#         add_labeled_widget(central_widget, "Projekt Nickname:", projekt_nickname_edit, 16, 192, 384, 28)
#         add_labeled_widget(central_widget, "Resolution:", create_combo_box_resolution_qt6(), 16, 240, 384, 28)
#         add_labeled_widget(central_widget, "Bit Depth:", create_combo_box_bit_depth_qt6(), 16, 288, 384, 28)
#         add_labeled_widget(central_widget, "Frame Rate:", create_combo_box_frame_rate_qt6(), 16, 336, 384, 28)
#         add_labeled_widget(central_widget, "Scan Mode:", create_combo_box_scan_mode_qt6(), 16, 384, 384, 28)
#         add_labeled_widget(central_widget, "Color Science:", create_combo_box_color_science_qt6(), 16, 432, 384, 28)
#         add_labeled_widget(central_widget, "Start Frame:", create_combo_box_start_frame_qt6(), 16, 480, 384, 28)
        
#         # Create and position the save button
#         save_button = CustomButton("Save Template")
#         save_button.setParent(central_widget)
#         save_button.setGeometry(16, 816, 384, 28)
#         save_button.clicked.connect(self.save_template)  # Connect the save button to the save_template function

#         # Update the summary box initially
#         self.update_summary_text_box()

#     def update_summary_text_box(self):
#         summary_lines = []
#         projekt_serial = string_clean(self.lineedits["Serial Number:"].text().strip())
#         projekt_client = string_clean(self.lineedits["Client Name:"].text().strip())
#         projekt_campaign = string_clean(self.lineedits["Campaign Name:"].text().strip())

#         # Construct projekt_nickname based on conditions
#         if not projekt_client or not projekt_campaign:
#             projekt_nickname = ""
#         elif projekt_serial:
#             projekt_nickname = f"{projekt_serial}_{projekt_client}_{projekt_campaign}"
#         else:
#             projekt_nickname = f"{projekt_client}_{projekt_campaign}"

#         self.lineedits["Projekt Nickname:"].setText(projekt_nickname)

#         for label, lineedit in self.lineedits.items():
#             summary_lines.append(f"{label} {string_clean(lineedit.text())}")

#         for label, combo_box in self.combo_boxes.items():
#             if label == "Resolution:":
#                 value_data = combo_box.itemData(combo_box.currentIndex())
#                 if value_data:
#                     summary_lines.append(f"{label} {value_data['width']} x {value_data['height']}")
#             else:
#                 summary_lines.append(f"{label} {combo_box.currentText()}")

#         summary_text = '\n'.join(summary_lines)
#         self.summary_text_box.setPlainText(summary_text)

#     def save_template(self):
#         summary_text = self.summary_text_box.toPlainText()
#         projekt_nickname = self.lineedits["Projekt Nickname:"].text()
#         projekt_template_saver_qt6(self, summary_text, projekt_nickname)

#     def apply_styles(self):
#         try:
#             self.setStyleSheet(stylesheet)  # Apply the stylesheet
#         except Exception as e:
#             QMessageBox.critical(self, "Error", str(e))

#     def center(self):
#         screen = QApplication.primaryScreen()
#         screen_geometry = screen.availableGeometry()
#         window_geometry = self.frameGeometry()
#         window_geometry.moveCenter(screen_geometry.center())
#         self.move(window_geometry.topLeft())

# if __name__ == '__main__':
#     app = QApplication([])
#     window = MainWindow()
#     window.show()
#     app.exec()
















# from PySide6.QtWidgets import QApplication, QMainWindow, QWidget, QLineEdit, QComboBox
# from PySide6.QtGui import QTextCursor
# from PySide6.QtCore import Qt

# from ...widgets.button.button import CustomButton
# from ...widgets.combo_box.combo_box_resolution import create_combo_box_resolution_qt6
# from ...widgets.combo_box.combo_box_bit_depth import create_combo_box_bit_depth_qt6
# from ...widgets.combo_box.combo_box_frame_rate import create_combo_box_frame_rate_qt6
# from ...widgets.combo_box.combo_box_scan_mode import create_combo_box_scan_mode_qt6
# from ...widgets.combo_box.combo_box_color_science import create_combo_box_color_science_qt6
# from ...widgets.combo_box.combo_box_start_frame import create_combo_box_start_frame_qt6
# from ...widgets.line_edit.line_edit_projekt_namer import (
#     create_serial_number_qt6,
#     create_client_name_qt6,
#     create_campaign_name_qt6,
#     create_projekt_nickname_qt6,
# )
# from ...functions.label.label import create_label_qt6
# from ...functions.string_utilities.string_utilities import string_clean
# from ...widgets.style_sheet.logik_stylesheet import stylesheet
# from ...widgets.summary_textbox.summary_textbox import create_summary_textbox_qt6
# from ...functions.saver.template_saver import projekt_template_saver_qt6
# from ...functions.list_software.list_flame_family_software import flame_family_app_list, sanitize_app_name

# class MainWindow(QMainWindow):
#     def __init__(self):
#         super().__init__()
#         self.setWindowTitle("Logik Projekt Application")
#         self.setGeometry(100, 100, 1440, 960)  # Set the window size
        
#         self.initUI()
#         self.apply_styles()
#         self.center()

#     def initUI(self):
#         central_widget = QWidget(self)
#         self.setCentralWidget(central_widget)
#         central_widget.setGeometry(0, 0, 1440, 960)  # Set central widget size
#         central_widget.setStyleSheet(stylesheet)

#         # Create the summary text box
#         self.summary_text_box = create_summary_textbox_qt6()
#         self.summary_text_box.setGeometry(160, 528, 384, 216)
#         self.summary_text_box.setParent(central_widget)

#         # Dictionary to store references to line edits and combo boxes
#         self.lineedits = {}
#         self.combo_boxes = {}

#         # Function to create and position labeled widgets
#         def add_labeled_widget(parent, label_text, widget, x, y, width, height):
#             label = create_label_qt6(label_text)
#             label.setParent(parent)
#             label.setGeometry(x, y, 128, 28)
            
#             widget.setParent(parent)
#             widget.setGeometry(x + 144, y, width, height)  # Adjust x-coordinate to the right of the label

#             # Store references to the widgets for summary updating
#             if isinstance(widget, QLineEdit):
#                 self.lineedits[label_text] = widget
#                 widget.textChanged.connect(self.update_summary_text_box)
#             elif isinstance(widget, QComboBox):
#                 self.combo_boxes[label_text] = widget
#                 widget.currentIndexChanged.connect(self.update_summary_text_box)

#         # Create and position widgets with labels
#         add_labeled_widget(central_widget, "Serial Number:", create_serial_number_qt6(), 16, 48, 384, 28)
#         add_labeled_widget(central_widget, "Client Name:", create_client_name_qt6(), 16, 96, 384, 28)
#         add_labeled_widget(central_widget, "Campaign Name:", create_campaign_name_qt6(), 16, 144, 384, 28)
#         projekt_nickname_edit = create_projekt_nickname_qt6()
#         projekt_nickname_edit.setReadOnly(True)  # Set to read-only
#         add_labeled_widget(central_widget, "Projekt Nickname:", projekt_nickname_edit, 16, 192, 384, 28)
#         add_labeled_widget(central_widget, "Resolution:", create_combo_box_resolution_qt6(), 16, 240, 384, 28)
#         add_labeled_widget(central_widget, "Bit Depth:", create_combo_box_bit_depth_qt6(), 16, 288, 384, 28)
#         add_labeled_widget(central_widget, "Frame Rate:", create_combo_box_frame_rate_qt6(), 16, 336, 384, 28)
#         add_labeled_widget(central_widget, "Scan Mode:", create_combo_box_scan_mode_qt6(), 16, 384, 384, 28)
#         add_labeled_widget(central_widget, "Color Science:", create_combo_box_color_science_qt6(), 16, 432, 384, 28)
#         add_labeled_widget(central_widget, "Start Frame:", create_combo_box_start_frame_qt6(), 16, 480, 384, 28)
        
#         # Create and position the Flame Family software combo box
#         flame_family_apps = flame_family_app_list("/home/pman/dummy_software_folders")  # Adjust the directory path
#         flame_family_drop_down = QComboBox()
#         flame_family_drop_down.addItems(flame_family_apps)
#         add_labeled_widget(central_widget, "Flame Family Apps:", flame_family_drop_down, 16, 528, 384, 28)
#         flame_family_drop_down.currentIndexChanged.connect(self.on_flame_family_app_selected)

#         # Create and position the save button
#         save_button = CustomButton("Save Template")
#         save_button.setParent(central_widget)
#         save_button.setGeometry(16, 816, 384, 28)
#         save_button.clicked.connect(self.save_template)  # Connect the save button to the save_template function

#         # Update the summary box initially
#         self.update_summary_text_box()

#     def on_flame_family_app_selected(self, index):
#         chosen_item = self.combo_boxes["Flame Family Apps:"].currentText()
#         self.chosen_software = sanitize_app_name(chosen_item)

#     def update_summary_text_box(self):
#         summary_lines = []
#         projekt_serial = string_clean(self.lineedits["Serial Number:"].text().strip())
#         projekt_client = string_clean(self.lineedits["Client Name:"].text().strip())
#         projekt_campaign = string_clean(self.lineedits["Campaign Name:"].text().strip())

#         # Construct projekt_nickname based on conditions
#         if not projekt_client or not projekt_campaign:
#             projekt_nickname = ""
#         elif projekt_serial:
#             projekt_nickname = f"{projekt_serial}_{projekt_client}_{projekt_campaign}"
#         else:
#             projekt_nickname = f"{projekt_client}_{projekt_campaign}"

#         self.lineedits["Projekt Nickname:"].setText(projekt_nickname)

#         for label, lineedit in self.lineedits.items():
#             summary_lines.append(f"{label} {string_clean(lineedit.text())}")

#         for label, combo_box in self.combo_boxes.items():
#             if label == "Resolution:":
#                 value_data = combo_box.itemData(combo_box.currentIndex())
#                 if value_data:
#                     summary_lines.append(f"{label} {value_data['width']} x {value_data['height']}")
#             else:
#                 summary_lines.append(f"{label} {combo_box.currentText()}")

#         summary_text = '\n'.join(summary_lines)
#         self.summary_text_box.setPlainText(summary_text)

#     def save_template(self):
#         summary_text = self.summary_text_box.toPlainText()
#         projekt_nickname = self.lineedits["Projekt Nickname:"].text()
#         projekt_template_saver_qt6(self, summary_text, projekt_nickname)

#     def apply_styles(self):
#         try:
#             self.setStyleSheet(stylesheet)  # Apply the stylesheet
#         except Exception as e:
#             QMessageBox.critical(self, "Error", str(e))

#     def center(self):
#         screen = QApplication.primaryScreen()
#         screen_geometry = screen.availableGeometry()
#         window_geometry = self.frameGeometry()
#         window_geometry.moveCenter(screen_geometry.center())
#         self.move(window_geometry.topLeft())

# if __name__ == '__main__':
#     app = QApplication([])
#     window = MainWindow()
#     window.show()
#     app.exec()

















# from PySide6.QtWidgets import QApplication, QMainWindow, QWidget, QLineEdit, QComboBox
# from PySide6.QtCore import Qt

# from ...widgets.button.button import CustomButton
# from ...widgets.combo_box.combo_box_resolution import create_combo_box_resolution_qt6
# from ...widgets.combo_box.combo_box_bit_depth import create_combo_box_bit_depth_qt6
# from ...widgets.combo_box.combo_box_frame_rate import create_combo_box_frame_rate_qt6
# from ...widgets.combo_box.combo_box_scan_mode import create_combo_box_scan_mode_qt6
# from ...widgets.combo_box.combo_box_color_science import create_combo_box_color_science_qt6
# from ...widgets.combo_box.combo_box_start_frame import create_combo_box_start_frame_qt6
# from ...widgets.line_edit.line_edit_projekt_namer import (
#     create_serial_number_qt6,
#     create_client_name_qt6,
#     create_campaign_name_qt6,
#     create_projekt_nickname_qt6,
# )
# from ...functions.label.label import create_label_qt6
# from ...functions.string_utilities.string_utilities import string_clean
# from ...widgets.style_sheet.logik_stylesheet import stylesheet
# from ...widgets.summary_textbox.summary_textbox import create_summary_textbox_qt6
# from ...functions.saver.template_saver import projekt_template_saver_qt6
# from ...functions.list_software.list_flame_family_software import flame_family_app_list, sanitize_app_name
# from ...functions.list_volumes.list_flame_framestores import list_framestores

# class MainWindow(QMainWindow):
#     def __init__(self):
#         super().__init__()
#         self.setWindowTitle("Logik Projekt Application")
#         self.setGeometry(100, 100, 1440, 960)  # Set the window size
        
#         self.initUI()
#         self.apply_styles()
#         self.center()

#     def initUI(self):
#         central_widget = QWidget(self)
#         self.setCentralWidget(central_widget)
#         central_widget.setGeometry(0, 0, 1440, 960)  # Set central widget size
#         central_widget.setStyleSheet(stylesheet)

#         # Create the summary text box
#         self.summary_text_box = create_summary_textbox_qt6()
#         self.summary_text_box.setGeometry(160, 528, 384, 216)
#         self.summary_text_box.setParent(central_widget)

#         # Dictionary to store references to line edits and combo boxes
#         self.lineedits = {}
#         self.combo_boxes = {}

#         # Function to create and position labeled widgets
#         def add_labeled_widget(parent, label_text, widget, x, y, width, height):
#             label = create_label_qt6(label_text)
#             label.setParent(parent)
#             label.setGeometry(x, y, 128, 28)
            
#             widget.setParent(parent)
#             widget.setGeometry(x + 144, y, width, height)  # Adjust x-coordinate to the right of the label

#             # Store references to the widgets for summary updating
#             if isinstance(widget, QLineEdit):
#                 self.lineedits[label_text] = widget
#                 widget.textChanged.connect(self.update_summary_text_box)
#             elif isinstance(widget, QComboBox):
#                 self.combo_boxes[label_text] = widget

#         # Create and position widgets with labels
#         add_labeled_widget(central_widget, "Serial Number:", create_serial_number_qt6(), 16, 48, 384, 28)
#         add_labeled_widget(central_widget, "Client Name:", create_client_name_qt6(), 16, 96, 384, 28)
#         add_labeled_widget(central_widget, "Campaign Name:", create_campaign_name_qt6(), 16, 144, 384, 28)
#         projekt_nickname_edit = create_projekt_nickname_qt6()
#         projekt_nickname_edit.setReadOnly(True)  # Set to read-only
#         add_labeled_widget(central_widget, "Projekt Nickname:", projekt_nickname_edit, 16, 192, 384, 28)
#         add_labeled_widget(central_widget, "Resolution:", create_combo_box_resolution_qt6(), 16, 240, 384, 28)
#         add_labeled_widget(central_widget, "Bit Depth:", create_combo_box_bit_depth_qt6(), 16, 288, 384, 28)
#         add_labeled_widget(central_widget, "Frame Rate:", create_combo_box_frame_rate_qt6(), 16, 336, 384, 28)
#         add_labeled_widget(central_widget, "Scan Mode:", create_combo_box_scan_mode_qt6(), 16, 384, 384, 28)
#         add_labeled_widget(central_widget, "Color Science:", create_combo_box_color_science_qt6(), 16, 432, 384, 28)
#         add_labeled_widget(central_widget, "Start Frame:", create_combo_box_start_frame_qt6(), 16, 480, 384, 28)
        
#         # Create and position the Flame Family software combo box
#         flame_family_apps = flame_family_app_list("/home/pman/dummy_software_folders")  # Adjust the directory path
#         flame_family_drop_down = QComboBox()
#         flame_family_drop_down.addItems(flame_family_apps)
#         add_labeled_widget(central_widget, "Flame Family Apps:", flame_family_drop_down, 16, 528, 384, 28)
#         flame_family_drop_down.currentIndexChanged.connect(self.on_flame_family_app_selected)

#         # Create and position the framestore combo box
#         framestore_combo_box = QComboBox()
#         framestore_combo_box.setGeometry(16, 576, 384, 28)
#         framestore_combo_box.setParent(central_widget)
        
#         # Populate the framestore combo box
#         framestores = list_framestores()
#         if framestores:
#             framestore_combo_box.addItems(framestores)
        
#         framestore_combo_box.currentIndexChanged.connect(self.on_framestore_selected)

#         # Create and position the save button
#         save_button = CustomButton("Save Template")
#         save_button.setParent(central_widget)
#         save_button.setGeometry(16, 816, 384, 28)
#         save_button.clicked.connect(self.save_template)  # Connect the save button to the save_template function

#         # Initialize chosen_framestore and chosen_software
#         self.chosen_framestore = None
#         self.chosen_software = None

#         # Update the summary box initially
#         self.update_summary_text_box()

#     def on_flame_family_app_selected(self, index):
#         chosen_item = self.combo_boxes["Flame Family Apps:"].currentText()
#         self.chosen_software = sanitize_app_name(chosen_item)
        
#     def on_framestore_selected(self, index):
#         self.chosen_framestore = self.combo_boxes["Framestore:"].currentText()

#     def update_summary_text_box(self):
#         summary_lines = []
#         projekt_serial = string_clean(self.lineedits["Serial Number:"].text().strip())
#         projekt_client = string_clean(self.lineedits["Client Name:"].text().strip())
#         projekt_campaign = string_clean(self.lineedits["Campaign Name:"].text().strip())

#         # Construct projekt_nickname based on conditions
#         if not projekt_client or not projekt_campaign:
#             projekt_nickname = ""
#         elif projekt_serial:
#             projekt_nickname = f"{projekt_serial}_{projekt_client}_{projekt_campaign}"
#         else:
#             projekt_nickname = f"{projekt_client}_{projekt_campaign}"

#         self.lineedits["Projekt Nickname:"].setText(projekt_nickname)

#         for label, lineedit in self.lineedits.items():
#             summary_lines.append(f"{label} {string_clean(lineedit.text())}")

#         for label, combo_box in self.combo_boxes.items():
#             if label == "Resolution:":
#                 value_data = combo_box.itemData(combo_box.currentIndex())
#                 if value_data:
#                     summary_lines.append(f"{label} {value_data['width']} x {value_data['height']}")
#             elif label == "Framestore:" and self.chosen_framestore:
#                 summary_lines.append(f"{label} {self.chosen_framestore}")
#             else:
#                 summary_lines.append(f"{label} {combo_box.currentText()}")

#         summary_text = '\n'.join(summary_lines)
#         self.summary_text_box.setPlainText(summary_text)

#     def save_template(self):
#         summary_text = self.summary_text_box.toPlainText()
#         projekt_nickname = self.lineedits["Projekt Nickname:"].text()
#         projekt_template_saver_qt6(self, summary_text, projekt_nickname)

#     def apply_styles(self):
#         try:
#             self.setStyleSheet(stylesheet)  # Apply the stylesheet
#         except Exception as e:
#             QMessageBox.critical(self, "Error", str(e))

#     def center(self):
#         screen = QApplication.primaryScreen()
#         screen_geometry = screen.availableGeometry()
#         window_geometry = self.frameGeometry()
#         window_geometry.moveCenter(screen_geometry.center())
#         self.move(window_geometry.topLeft())

# if __name__ == '__main__':
#     app = QApplication([])
#     window = MainWindow()
#     window.show()
#     app.exec()

















# from PySide6.QtWidgets import QApplication, QMainWindow, QWidget, QLineEdit, QComboBox, QLabel
# from PySide6.QtCore import Qt

# from ...widgets.button.button import CustomButton
# from ...widgets.combo_box.combo_box_resolution import create_combo_box_resolution_qt6
# from ...widgets.combo_box.combo_box_bit_depth import create_combo_box_bit_depth_qt6
# from ...widgets.combo_box.combo_box_frame_rate import create_combo_box_frame_rate_qt6
# from ...widgets.combo_box.combo_box_scan_mode import create_combo_box_scan_mode_qt6
# from ...widgets.combo_box.combo_box_color_science import create_combo_box_color_science_qt6
# from ...widgets.combo_box.combo_box_start_frame import create_combo_box_start_frame_qt6
# from ...widgets.drop_down.drop_down_flame_family_software import create_drop_down_flame_software_qt6
# from ...widgets.drop_down.drop_down_flame_framestores import create_drop_down_framestores_qt6
# from ...widgets.line_edit.line_edit_projekt_namer import (
#     create_serial_number_qt6,
#     create_client_name_qt6,
#     create_campaign_name_qt6,
#     create_projekt_nickname_qt6,
# )
# from ...functions.label.label import create_label_qt6
# from ...functions.list_software.list_flame_family_software import flame_family_app_list, sanitize_app_name
# from ...functions.list_volumes.list_flame_framestores import list_framestores
# from ...functions.saver.template_saver import projekt_template_saver_qt6
# from ...functions.string_utilities.string_utilities import string_clean
# from ...widgets.style_sheet.logik_stylesheet import stylesheet
# from ...widgets.summary_textbox.summary_textbox import create_summary_textbox_qt6

# class MainWindow(QMainWindow):
#     def __init__(self):
#         super().__init__()
#         self.setWindowTitle("Logik Projekt Application")
#         self.setGeometry(100, 100, 1440, 960)  # Set the window size
        
#         self.initUI()
#         self.apply_styles()
#         self.center()

#     def initUI(self):
#         central_widget = QWidget(self)
#         self.setCentralWidget(central_widget)
#         central_widget.setGeometry(0, 0, 1440, 960)  # Set central widget size
#         central_widget.setStyleSheet(stylesheet)

#         # Create the summary text box
#         self.summary_text_box = create_summary_textbox_qt6()
#         self.summary_text_box.setGeometry(160, 528, 384, 216)
#         self.summary_text_box.setParent(central_widget)

#         # Dictionary to store references to line edits and combo boxes
#         self.lineedits = {}
#         self.combo_boxes = {}

#         # Function to create and position labeled widgets
#         def add_labeled_widget(parent, label_text, widget, x, y, width, height):
#             label = create_label_qt6(label_text)
#             label.setParent(parent)
#             label.setGeometry(x, y, 128, 28)
            
#             widget.setParent(parent)
#             widget.setGeometry(x + 144, y, width, height)  # Adjust x-coordinate to the right of the label

#             # Store references to the widgets for summary updating
#             if isinstance(widget, QLineEdit):
#                 self.lineedits[label_text] = widget
#                 widget.textChanged.connect(self.update_summary_text_box)
#             elif isinstance(widget, QComboBox):
#                 self.combo_boxes[label_text] = widget
#                 widget.currentIndexChanged.connect(self.update_summary_text_box)

#         # Create and position widgets with labels
#         add_labeled_widget(central_widget, "Serial Number:", create_serial_number_qt6(), 16, 48, 384, 28)
#         add_labeled_widget(central_widget, "Client Name:", create_client_name_qt6(), 16, 96, 384, 28)
#         add_labeled_widget(central_widget, "Campaign Name:", create_campaign_name_qt6(), 16, 144, 384, 28)
#         projekt_nickname_edit = create_projekt_nickname_qt6()
#         projekt_nickname_edit.setReadOnly(True)  # Set to read-only
#         add_labeled_widget(central_widget, "Projekt Nickname:", projekt_nickname_edit, 16, 192, 384, 28)
#         add_labeled_widget(central_widget, "Resolution:", create_combo_box_resolution_qt6(), 16, 240, 384, 28)
#         add_labeled_widget(central_widget, "Bit Depth:", create_combo_box_bit_depth_qt6(), 16, 288, 384, 28)
#         add_labeled_widget(central_widget, "Frame Rate:", create_combo_box_frame_rate_qt6(), 16, 336, 384, 28)
#         add_labeled_widget(central_widget, "Scan Mode:", create_combo_box_scan_mode_qt6(), 16, 384, 384, 28)
#         add_labeled_widget(central_widget, "Color Science:", create_combo_box_color_science_qt6(), 16, 432, 384, 28)
#         add_labeled_widget(central_widget, "Start Frame:", create_combo_box_start_frame_qt6(), 16, 480, 384, 28)
        
#         # Create and position the Flame Family software combo box using the new function
#         flame_family_drop_down = create_drop_down_flame_software_qt6()
#         add_labeled_widget(central_widget, "Flame Family Apps:", flame_family_drop_down, 720, 48, 192, 28)
#         flame_family_drop_down.currentIndexChanged.connect(self.on_flame_family_app_selected)

#         # Create and position the Flame Framestores combo box using the new function
#         framestores_combo_box = create_drop_down_framestores_qt6()
#         add_labeled_widget(central_widget, "Flame Framestores:", framestores_combo_box, 720, 96, 192, 28)
#         framestores_combo_box.currentIndexChanged.connect(self.on_framestore_selected)

#         # Create and position the save button
#         save_button = CustomButton("Save Template")
#         save_button.setParent(central_widget)
#         save_button.setGeometry(16, 816, 384, 28)
#         save_button.clicked.connect(self.save_template)  # Connect the save button to the save_template function

#         # Initialize chosen_framestore and chosen_software
#         self.chosen_framestore = None
#         self.chosen_software = None

#         # Update the summary box initially
#         self.update_summary_text_box()

#     def on_flame_family_app_selected(self, index):
#         chosen_item = self.combo_boxes["Flame Family Apps:"].currentText()
#         self.chosen_software = sanitize_app_name(chosen_item)
#         self.chosen_software_widget.setText(self.chosen_software)
        
#     def on_framestore_selected(self, index):
#         self.chosen_framestore = self.combo_boxes["Framestore:"].currentText()
#         self.chosen_framestore_widget.setText(self.chosen_framestore)

#     def update_summary_text_box(self):
#         summary_lines = []
#         projekt_serial = string_clean(self.lineedits["Serial Number:"].text().strip())
#         projekt_client = string_clean(self.lineedits["Client Name:"].text().strip())
#         projekt_campaign = string_clean(self.lineedits["Campaign Name:"].text().strip())

#         # Construct projekt_nickname based on conditions
#         if not projekt_client or not projekt_campaign:
#             projekt_nickname = ""
#         elif projekt_serial:
#             projekt_nickname = f"{projekt_serial}_{projekt_client}_{projekt_campaign}"
#         else:
#             projekt_nickname = f"{projekt_client}_{projekt_campaign}"

#         self.lineedits["Projekt Nickname:"].setText(projekt_nickname)

#         for label, lineedit in self.lineedits.items():
#             summary_lines.append(f"{label} {string_clean(lineedit.text())}")

#         for label, combo_box in self.combo_boxes.items():
#             if label == "Resolution:":
#                 value_data = combo_box.itemData(combo_box.currentIndex())
#                 if value_data:
#                     summary_lines.append(f"{label} {value_data['width']} x {value_data['height']}")
#             else:
#                 summary_lines.append(f"{label} {combo_box.currentText()}")

#         summary_text = '\n'.join(summary_lines)
#         self.summary_text_box.setPlainText(summary_text)

#     def save_template(self):
#         summary_text = self.summary_text_box.toPlainText()
#         projekt_nickname = self.lineedits["Projekt Nickname:"].text()
#         projekt_template_saver_qt6(self, summary_text, projekt_nickname)

#     def apply_styles(self):
#         try:
#             self.setStyleSheet(stylesheet)  # Apply the stylesheet
#         except Exception as e:
#             QMessageBox.critical(self, "Error", str(e))

#     def center(self):
#         screen = QApplication.primaryScreen()
#         screen_geometry = screen.availableGeometry()
#         window_geometry = self.frameGeometry()
#         window_geometry.moveCenter(screen_geometry.center())
#         self.move(window_geometry.topLeft())

# if __name__ == '__main__':
#     app = QApplication([])
#     window = MainWindow()
#     window.show()
#     app.exec()























# from PySide6.QtWidgets import QApplication, QMainWindow, QWidget, QLineEdit, QComboBox, QLabel, QMessageBox
# from PySide6.QtCore import Qt

# from ...widgets.button.button import CustomButton
# from ...widgets.combo_box.combo_box_resolution import create_combo_box_resolution_qt6
# from ...widgets.combo_box.combo_box_bit_depth import create_combo_box_bit_depth_qt6
# from ...widgets.combo_box.combo_box_frame_rate import create_combo_box_frame_rate_qt6
# from ...widgets.combo_box.combo_box_scan_mode import create_combo_box_scan_mode_qt6
# from ...widgets.combo_box.combo_box_color_science import create_combo_box_color_science_qt6
# from ...widgets.combo_box.combo_box_start_frame import create_combo_box_start_frame_qt6
# from ...widgets.drop_down.drop_down_flame_family_software import create_drop_down_flame_software_qt6
# from ...widgets.drop_down.drop_down_flame_framestores import create_drop_down_framestores_qt6
# from ...widgets.line_edit.line_edit_projekt_namer import (
#     create_serial_number_qt6,
#     create_client_name_qt6,
#     create_campaign_name_qt6,
#     create_projekt_nickname_qt6,
# )
# from ...functions.label.label import create_label_qt6
# from ...functions.list_software.list_flame_family_software import sanitize_app_name
# from ...functions.saver.template_saver import projekt_template_saver_qt6
# from ...functions.string_utilities.string_utilities import string_clean
# from ...widgets.style_sheet.logik_stylesheet import stylesheet
# from ...widgets.summary_textbox.summary_textbox import create_summary_textbox_qt6

# class MainWindow(QMainWindow):
#     def __init__(self):
#         super().__init__()
#         self.setWindowTitle("Logik Projekt Application")
#         self.setGeometry(100, 100, 1440, 960)  # Set the window size
        
#         self.initUI()
#         self.apply_styles()
#         self.center()

#     def initUI(self):
#         central_widget = QWidget(self)
#         self.setCentralWidget(central_widget)
#         central_widget.setGeometry(0, 0, 1440, 960)  # Set central widget size
#         central_widget.setStyleSheet(stylesheet)

#         # Create the summary text box
#         self.summary_text_box = create_summary_textbox_qt6()
#         self.summary_text_box.setGeometry(160, 528, 384, 216)
#         self.summary_text_box.setParent(central_widget)

#         # Dictionary to store references to line edits and combo boxes
#         self.lineedits = {}
#         self.combo_boxes = {}
#         self.drop_downs = {}

#         # Function to create and position labeled widgets
#         def add_labeled_widget(parent, label_text, widget, x, y, width, height):
#             label = create_label_qt6(label_text)
#             label.setParent(parent)
#             label.setGeometry(x, y, 128, 28)
            
#             widget.setParent(parent)
#             widget.setGeometry(x + 144, y, width, height)  # Adjust x-coordinate to the right of the label

#             # Store references to the widgets for summary updating
#             if isinstance(widget, QLineEdit):
#                 self.lineedits[label_text] = widget
#                 widget.textChanged.connect(self.update_summary_text_box)
#             elif isinstance(widget, QComboBox):
#                 self.combo_boxes[label_text] = widget
#                 widget.currentIndexChanged.connect(self.update_summary_text_box)
#             else:
#                 self.drop_downs[label_text] = widget

#         # Create and position widgets with labels
#         add_labeled_widget(central_widget, "Serial Number:", create_serial_number_qt6(), 16, 48, 384, 28)
#         add_labeled_widget(central_widget, "Client Name:", create_client_name_qt6(), 16, 96, 384, 28)
#         add_labeled_widget(central_widget, "Campaign Name:", create_campaign_name_qt6(), 16, 144, 384, 28)
#         projekt_nickname_edit = create_projekt_nickname_qt6()
#         projekt_nickname_edit.setReadOnly(True)  # Set to read-only
#         add_labeled_widget(central_widget, "Projekt Nickname:", projekt_nickname_edit, 16, 192, 384, 28)
#         add_labeled_widget(central_widget, "Resolution:", create_combo_box_resolution_qt6(), 16, 240, 384, 28)
#         add_labeled_widget(central_widget, "Bit Depth:", create_combo_box_bit_depth_qt6(), 16, 288, 384, 28)
#         add_labeled_widget(central_widget, "Frame Rate:", create_combo_box_frame_rate_qt6(), 16, 336, 384, 28)
#         add_labeled_widget(central_widget, "Scan Mode:", create_combo_box_scan_mode_qt6(), 16, 384, 384, 28)
#         add_labeled_widget(central_widget, "Color Science:", create_combo_box_color_science_qt6(), 16, 432, 384, 28)
#         add_labeled_widget(central_widget, "Start Frame:", create_combo_box_start_frame_qt6(), 16, 480, 384, 28)
        
#         # Create and position the Flame Family software drop-down using the new function
#         flame_family_drop_down = create_drop_down_flame_software_qt6()
#         add_labeled_widget(central_widget, "Flame Family Apps:", flame_family_drop_down, 720, 48, 192, 28)
#         flame_family_drop_down.currentIndexChanged.connect(self.on_flame_family_app_selected)

#         # Create and position the Flame Framestores drop-down using the new function
#         framestores_drop_down = create_drop_down_framestores_qt6()
#         add_labeled_widget(central_widget, "Flame Framestores:", framestores_drop_down, 720, 96, 192, 28)
#         framestores_drop_down.currentIndexChanged.connect(self.on_framestore_selected)

#         # Create and position the save button
#         save_button = CustomButton("Save Template")
#         save_button.setParent(central_widget)
#         save_button.setGeometry(16, 816, 384, 28)
#         save_button.clicked.connect(self.save_template)  # Connect the save button to the save_template function

#         # Initialize chosen_framestore and chosen_software
#         self.chosen_framestore = None
#         self.chosen_software = None

#         # Update the summary box initially
#         self.update_summary_text_box()

#     def on_flame_family_app_selected(self, index):
#         chosen_item = self.drop_downs["Flame Family Apps:"].currentText()
#         self.chosen_software = sanitize_app_name(chosen_item)
        
#     def on_framestore_selected(self, index):
#         self.chosen_framestore = self.drop_downs["Flame Framestores:"].currentText()

#     def update_summary_text_box(self):
#         summary_lines = []
#         projekt_serial = string_clean(self.lineedits["Serial Number:"].text().strip())
#         projekt_client = string_clean(self.lineedits["Client Name:"].text().strip())
#         projekt_campaign = string_clean(self.lineedits["Campaign Name:"].text().strip())

#         # Construct projekt_nickname based on conditions
#         if not projekt_client or not projekt_campaign:
#             projekt_nickname = ""
#         elif projekt_serial:
#             projekt_nickname = f"{projekt_serial}_{projekt_client}_{projekt_campaign}"
#         else:
#             projekt_nickname = f"{projekt_client}_{projekt_campaign}"

#         self.lineedits["Projekt Nickname:"].setText(projekt_nickname)

#         for label, lineedit in self.lineedits.items():
#             summary_lines.append(f"{label} {string_clean(lineedit.text())}")

#         for label, combo_box in self.combo_boxes.items():
#             if label == "Resolution:":
#                 value_data = combo_box.itemData(combo_box.currentIndex())
#                 if value_data:
#                     summary_lines.append(f"{label} {value_data['width']} x {value_data['height']}")
#             else:
#                 summary_lines.append(f"{label} {combo_box.currentText()}")

#         # Exclude specific dropdowns from the summary
#         excluded_labels = ["Flame Family Apps:", "Flame Framestores:"]
#         for label, drop_down in self.drop_downs.items():
#             if label not in excluded_labels:
#                 summary_lines.append(f"{label} {drop_down.currentText()}")

#         summary_text = '\n'.join(summary_lines)
#         self.summary_text_box.setPlainText(summary_text)

#     def save_template(self):
#         summary_text = self.summary_text_box.toPlainText()
#         projekt_nickname = self.lineedits["Projekt Nickname:"].text()
#         projekt_template_saver_qt6(self, summary_text, projekt_nickname)

#     def apply_styles(self):
#         try:
#             self.setStyleSheet(stylesheet)  # Apply the stylesheet
#         except Exception as e:
#             QMessageBox.critical(self, "Error", str(e))

#     def center(self):
#         screen = QApplication.primaryScreen()
#         screen_geometry = screen.availableGeometry()
#         window_geometry = self.frameGeometry()
#         window_geometry.moveCenter(screen_geometry.center())
#         self.move(window_geometry.topLeft())

# if __name__ == '__main__':
#     app = QApplication([])
#     window = MainWindow()
#     window.show()
#     app.exec()

















# from PySide6.QtWidgets import QApplication, QMainWindow, QWidget, QLineEdit, QComboBox, QLabel, QMessageBox
# from PySide6.QtCore import Qt

# from ...widgets.button.button import CustomButton
# from ...widgets.combo_box.combo_box_resolution import create_combo_box_resolution_qt6
# from ...widgets.combo_box.combo_box_bit_depth import create_combo_box_bit_depth_qt6
# from ...widgets.combo_box.combo_box_frame_rate import create_combo_box_frame_rate_qt6
# from ...widgets.combo_box.combo_box_scan_mode import create_combo_box_scan_mode_qt6
# from ...widgets.combo_box.combo_box_color_science import create_combo_box_color_science_qt6
# from ...widgets.combo_box.combo_box_start_frame import create_combo_box_start_frame_qt6
# from ...widgets.drop_down.drop_down_flame_family_software import create_drop_down_flame_software_qt6
# from ...widgets.drop_down.drop_down_flame_framestores import create_drop_down_framestores_qt6
# from ...widgets.line_edit.line_edit_projekt_namer import (
#     create_serial_number_qt6,
#     create_client_name_qt6,
#     create_campaign_name_qt6,
#     create_projekt_nickname_qt6,
# )
# from ...functions.label.label import create_label_qt6
# from ...functions.list_software.list_flame_family_software import sanitize_app_name
# from ...functions.saver.template_saver import projekt_template_saver_qt6
# from ...functions.string_utilities.string_utilities import string_clean
# from ...widgets.style_sheet.logik_stylesheet import stylesheet
# from ...widgets.summary_textbox.summary_textbox import create_summary_textbox_qt6, update_summary_textbox_qt6

# class MainWindow(QMainWindow):
#     def __init__(self):
#         super().__init__()
#         self.setWindowTitle("Logik Projekt Application")
#         self.setGeometry(100, 100, 1440, 960)  # Set the window size
        
#         self.initUI()
#         self.apply_styles()
#         self.center()

#     def initUI(self):
#         central_widget = QWidget(self)
#         self.setCentralWidget(central_widget)
#         central_widget.setGeometry(0, 0, 1440, 960)  # Set central widget size
#         central_widget.setStyleSheet(stylesheet)

#         # Create the summary text box
#         self.summary_text_box = create_summary_textbox_qt6()
#         self.summary_text_box.setGeometry(28, 528, 516, 216)
#         self.summary_text_box.setParent(central_widget)

#         # Dictionary to store references to line edits and combo boxes
#         self.lineedits = {}
#         self.combo_boxes = {}
#         self.drop_downs = {}

#         # Function to create and position labeled widgets
#         def add_labeled_widget(parent, label_text, widget, x, y, width, height):
#             label = create_label_qt6(label_text)
#             label.setParent(parent)
#             label.setGeometry(x, y, 128, 28)
            
#             widget.setParent(parent)
#             widget.setGeometry(x + 144, y, width, height)  # Adjust x-coordinate to the right of the label

#             # Store references to the widgets for summary updating
#             if isinstance(widget, QLineEdit):
#                 self.lineedits[label_text] = widget
#                 widget.textChanged.connect(self.update_summary_text_box)
#             elif isinstance(widget, QComboBox):
#                 self.combo_boxes[label_text] = widget
#                 widget.currentIndexChanged.connect(self.update_summary_text_box)
#             else:
#                 self.drop_downs[label_text] = widget

#         # Create and position widgets with labels
#         add_labeled_widget(central_widget, "Serial Number:", create_serial_number_qt6(), 16, 48, 384, 28)
#         add_labeled_widget(central_widget, "Client Name:", create_client_name_qt6(), 16, 96, 384, 28)
#         add_labeled_widget(central_widget, "Campaign Name:", create_campaign_name_qt6(), 16, 144, 384, 28)
#         projekt_nickname_edit = create_projekt_nickname_qt6()
#         projekt_nickname_edit.setReadOnly(True)  # Set to read-only
#         add_labeled_widget(central_widget, "Projekt Nickname:", projekt_nickname_edit, 16, 192, 384, 28)
#         add_labeled_widget(central_widget, "Resolution:", create_combo_box_resolution_qt6(), 16, 240, 384, 28)
#         add_labeled_widget(central_widget, "Bit Depth:", create_combo_box_bit_depth_qt6(), 16, 288, 384, 28)
#         add_labeled_widget(central_widget, "Frame Rate:", create_combo_box_frame_rate_qt6(), 16, 336, 384, 28)
#         add_labeled_widget(central_widget, "Scan Mode:", create_combo_box_scan_mode_qt6(), 16, 384, 384, 28)
#         add_labeled_widget(central_widget, "Color Science:", create_combo_box_color_science_qt6(), 16, 432, 384, 28)
#         add_labeled_widget(central_widget, "Start Frame:", create_combo_box_start_frame_qt6(), 16, 480, 384, 28)
        
#         # Create and position the Flame Family software drop-down using the new function
#         flame_family_drop_down = create_drop_down_flame_software_qt6()
#         add_labeled_widget(central_widget, "Flame Family Apps:", flame_family_drop_down, 576, 48, 192, 28)
#         flame_family_drop_down.currentIndexChanged.connect(self.on_flame_family_app_selected)

#         # Create and position the Flame Framestores drop-down using the new function
#         framestores_drop_down = create_drop_down_framestores_qt6()
#         add_labeled_widget(central_widget, "Flame Framestores:", framestores_drop_down, 960, 48, 192, 28)
#         framestores_drop_down.currentIndexChanged.connect(self.on_framestore_selected)

#         # Create and position the save button
#         save_button = CustomButton("Save Template")
#         save_button.setParent(central_widget)
#         save_button.setGeometry(160, 816, 384, 28)
#         save_button.clicked.connect(self.save_template)  # Connect the save button to the save_template function

#         # Initialize chosen_framestore and chosen_software
#         self.chosen_framestore = None
#         self.chosen_software = None

#         # Update the summary box initially
#         self.update_summary_text_box()

#     def on_flame_family_app_selected(self, index):
#         chosen_item = self.drop_downs["Flame Family Apps:"].currentText()
#         self.chosen_software = sanitize_app_name(chosen_item)
        
#     def on_framestore_selected(self, index):
#         self.chosen_framestore = self.drop_downs["Flame Framestores:"].currentText()

#     def update_summary_text_box(self):
#         excluded_labels = ["Flame Family Apps:", "Flame Framestores:"]
#         update_summary_textbox_qt6(self.summary_text_box, self.lineedits, self.combo_boxes, excluded_labels)

#     def save_template(self):
#         summary_text = self.summary_text_box.toPlainText()
#         projekt_nickname = self.lineedits["Projekt Nickname:"].text()
#         projekt_template_saver_qt6(self, summary_text, projekt_nickname)

#     def apply_styles(self):
#         try:
#             self.setStyleSheet(stylesheet)  # Apply the stylesheet
#         except Exception as e:
#             QMessageBox.critical(self, "Error", str(e))

#     def center(self):
#         screen = QApplication.primaryScreen()
#         screen_geometry = screen.availableGeometry()
#         window_geometry = self.frameGeometry()
#         window_geometry.moveCenter(screen_geometry.center())
#         self.move(window_geometry.topLeft())

# if __name__ == '__main__':
#     app = QApplication([])
#     window = MainWindow()
#     window.show()
#     app.exec()



















from PySide6.QtWidgets import QApplication, QMainWindow, QWidget, QLineEdit, QComboBox, QLabel, QMessageBox
from PySide6.QtCore import Qt

from ...widgets.button.button import CustomButton
from ...widgets.combo_box.combo_box_resolution import create_combo_box_resolution_qt6
from ...widgets.combo_box.combo_box_bit_depth import create_combo_box_bit_depth_qt6
from ...widgets.combo_box.combo_box_frame_rate import create_combo_box_frame_rate_qt6
from ...widgets.combo_box.combo_box_scan_mode import create_combo_box_scan_mode_qt6
from ...widgets.combo_box.combo_box_color_science import create_combo_box_color_science_qt6
from ...widgets.combo_box.combo_box_start_frame import create_combo_box_start_frame_qt6
from ...widgets.drop_down.drop_down_flame_family_software import create_drop_down_flame_software_qt6
from ...widgets.drop_down.drop_down_flame_framestores import create_drop_down_framestores_qt6
from ...widgets.combo_box.combo_box_init_config import create_combo_box_init_config_qt6
from ...widgets.line_edit.line_edit_projekt_namer import (
    create_serial_number_qt6,
    create_client_name_qt6,
    create_campaign_name_qt6,
    create_projekt_nickname_qt6,
)
from ...functions.label.label import create_label_qt6
from ...functions.list_software.list_flame_family_software import sanitize_app_name
from ...functions.saver.template_saver import projekt_template_saver_qt6
from ...functions.string_utilities.string_utilities import string_clean
from ...widgets.style_sheet.logik_stylesheet import stylesheet
from ...widgets.summary_textbox.summary_textbox import create_summary_textbox_qt6, update_summary_textbox_qt6

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Logik Projekt Application")
        self.setGeometry(100, 100, 1440, 960)  # Set the window size
        
        self.initUI()
        self.apply_styles()
        self.center()

    def initUI(self):
        central_widget = QWidget(self)
        self.setCentralWidget(central_widget)
        central_widget.setGeometry(0, 0, 1440, 960)  # Set central widget size
        central_widget.setStyleSheet(stylesheet)

        # Create the summary text box
        self.summary_text_box = create_summary_textbox_qt6()
        self.summary_text_box.setGeometry(160, 528, 384, 216)
        self.summary_text_box.setParent(central_widget)

        # Dictionary to store references to line edits, combo boxes, and drop-downs
        self.lineedits = {}
        self.combo_boxes = {}
        self.drop_downs = {}

        # Function to create and position labeled widgets
        def add_labeled_widget(parent, label_text, widget, x, y, width, height):
            label = create_label_qt6(label_text)
            label.setParent(parent)
            label.setGeometry(x, y, 128, 28)
            
            widget.setParent(parent)
            widget.setGeometry(x + 144, y, width, height)  # Adjust x-coordinate to the right of the label

            # Store references to the widgets for summary updating
            if isinstance(widget, QLineEdit):
                self.lineedits[label_text] = widget
                widget.textChanged.connect(self.update_summary_text_box)
            elif isinstance(widget, QComboBox):
                self.combo_boxes[label_text] = widget
                widget.currentIndexChanged.connect(self.update_summary_text_box)
            else:
                self.drop_downs[label_text] = widget

        # Create and position widgets with labels
        add_labeled_widget(central_widget, "Serial Number:", create_serial_number_qt6(), 16, 48, 384, 28)
        add_labeled_widget(central_widget, "Client Name:", create_client_name_qt6(), 16, 96, 384, 28)
        add_labeled_widget(central_widget, "Campaign Name:", create_campaign_name_qt6(), 16, 144, 384, 28)
        projekt_nickname_edit = create_projekt_nickname_qt6()
        projekt_nickname_edit.setReadOnly(True)  # Set to read-only
        add_labeled_widget(central_widget, "Projekt Nickname:", projekt_nickname_edit, 16, 192, 384, 28)
        add_labeled_widget(central_widget, "Resolution:", create_combo_box_resolution_qt6(), 16, 240, 384, 28)
        add_labeled_widget(central_widget, "Bit Depth:", create_combo_box_bit_depth_qt6(), 16, 288, 384, 28)
        add_labeled_widget(central_widget, "Frame Rate:", create_combo_box_frame_rate_qt6(), 16, 336, 384, 28)
        add_labeled_widget(central_widget, "Scan Mode:", create_combo_box_scan_mode_qt6(), 16, 384, 384, 28)
        add_labeled_widget(central_widget, "Color Science:", create_combo_box_color_science_qt6(), 16, 432, 384, 28)
        add_labeled_widget(central_widget, "Start Frame:", create_combo_box_start_frame_qt6(), 16, 480, 384, 28)
        
        # Create and position the Flame Family software drop-down using the new function
        flame_family_drop_down = create_drop_down_flame_software_qt6()
        add_labeled_widget(central_widget, "Flame Family Apps:", flame_family_drop_down, 720, 48, 192, 28)
        flame_family_drop_down.currentIndexChanged.connect(self.on_flame_family_app_selected)

        # Create and position the Flame Framestores drop-down using the new function
        framestores_drop_down = create_drop_down_framestores_qt6()
        add_labeled_widget(central_widget, "Flame Framestores:", framestores_drop_down, 720, 96, 192, 28)
        framestores_drop_down.currentIndexChanged.connect(self.on_framestore_selected)
        
        # Create and position the Init Config combo box using the new function
        init_cfgs_dir = "../../../../config/init_configs/template/"
        init_config_combo_box = create_combo_box_init_config_qt6(init_cfgs_dir)
        add_labeled_widget(central_widget, "Init Config:", init_config_combo_box, 720, 144, 192, 28)
        init_config_combo_box.currentIndexChanged.connect(self.on_init_config_selected)

        # Create and position the save button
        save_button = CustomButton("Save Template")
        save_button.setParent(central_widget)
        save_button.setGeometry(16, 816, 384, 28)
        save_button.clicked.connect(self.save_template)  # Connect the save button to the save_template function

        # Initialize chosen_framestore, chosen_software, and projekt_init_cfg
        self.chosen_framestore = None
        self.chosen_software = None
        self.projekt_init_cfg = None

        # Update the summary box initially
        self.update_summary_text_box()

    def on_flame_family_app_selected(self, index):
        chosen_item = self.drop_downs["Flame Family Apps:"].currentText()
        self.chosen_software = sanitize_app_name(chosen_item)
        
    def on_framestore_selected(self, index):
        self.chosen_framestore = self.drop_downs["Flame Framestores:"].currentText()

    def on_init_config_selected(self, index):
        self.projekt_init_cfg = self.combo_boxes["Init Config:"].currentText()

    def update_summary_text_box(self):
        excluded_labels = ["Flame Family Apps:", "Flame Framestores:"]
        update_summary_textbox_qt6(self.summary_text_box, self.lineedits, self.combo_boxes, excluded_labels)

    def save_template(self):
        summary_text = self.summary_text_box.toPlainText()
        projekt_nickname = self.lineedits["Projekt Nickname:"].text()
        projekt_template_saver_qt6(self, summary_text, projekt_nickname)

    def apply_styles(self):
        try:
            self.setStyleSheet(stylesheet)  # Apply the stylesheet
        except Exception as e:
            QMessageBox.critical(self, "Error", str(e))

    def center(self):
        screen = QApplication.primaryScreen()
        screen_geometry = screen.availableGeometry()
        window_geometry = self.frameGeometry()
        window_geometry.moveCenter(screen_geometry.center())
        self.move(window_geometry.topLeft())

if __name__ == '__main__':
    app = QApplication([])
    window = MainWindow()
    window.show()
    app.exec()
