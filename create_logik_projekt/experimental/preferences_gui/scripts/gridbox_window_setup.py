from PySide6.QtWidgets import QMainWindow, QWidget

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        
        self.setWindowTitle("PySide6 Example")
        self.setGeometry(100, 100, 1000, 570)

        # Create a central widget
        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)
