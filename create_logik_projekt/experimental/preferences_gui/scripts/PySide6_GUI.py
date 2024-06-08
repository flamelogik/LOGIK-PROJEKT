import sys
from PySide6.QtWidgets import QApplication, QGridLayout, QLineEdit, QSlider
from gridbox_window_setup import MainWindow
from gridbox_add_widgets import add_widgets
from gridbox_style_sheets import label_stylesheet, line_edit_stylesheet, slider_stylesheet

def main():
    # Create the application instance
    app = QApplication(sys.argv)
    
    # Create the main window instance
    main_window = MainWindow()
    gridbox = QGridLayout(main_window.centralWidget())
    add_widgets(gridbox)
    
    # Apply stylesheets
    apply_stylesheets(main_window.centralWidget())
    
    main_window.show()
    
    # Start the event loop
    sys.exit(app.exec())

def apply_stylesheets(widget):
    widget.setStyleSheet(label_stylesheet)
    for child in widget.findChildren(QLineEdit):
        child.setStyleSheet(line_edit_stylesheet)
    for child in widget.findChildren(QSlider):
        child.setStyleSheet(slider_stylesheet)

if __name__ == "__main__":
    main()
