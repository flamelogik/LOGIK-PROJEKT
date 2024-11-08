import nuke

try:
    from PySide import QtGui, QtCore
except ImportError:
    from PySide2 import QtCore
    from PySide2 import QtWidgets as QtGui

# Your script code here, using QtGui and QtCore as needed

def main():
    # Example: Create a simple dialog using PySide2 in Nuke 11 or later
    app = QtGui.QApplication([])
    dialog = QtGui.QDialog()
    dialog.setWindowTitle("Nuke PySide/PySide2 Compatibility")
    dialog.setGeometry(100, 100, 400, 200)

    label = QtGui.QLabel("Hello from PySide2!")
    layout = QtGui.QVBoxLayout()
    layout.addWidget(label)
    dialog.setLayout(layout)

    dialog.exec_()

if __name__ == "__main__":
    main()
