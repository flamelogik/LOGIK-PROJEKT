
# -------------------------------------------------------------------------- #

# DISCLAIMER:       This file is part of LOGIK-PROJEKT.
#                   Copyright © 2024 Silo 84
   
#                   LOGIK-PROJEKT creates directories, files, scripts & tools
#                   for use with Autodesk Flame and other software.

#                   LOGIK-PROJEKT is free software.

#                   You can redistribute it and/or modify it under the terms
#                   of the GNU General Public License as published by the
#                   Free Software Foundation, either version 3 of the License,
#                   or any later version.

#                   This program is distributed in the hope that it will be
#                   useful, but WITHOUT ANY WARRANTY; without even the
#                   implied warranty of MERCHANTABILITY or FITNESS FOR A
#                   PARTICULAR PURPOSE.

#                   See the GNU General Public License for more details.

#                   You should have received a copy of the GNU General
#                   Public License along with this program.

#                   If not, see <https://www.gnu.org/licenses/>.
   
#                   Contact: brian@silo84.com

# -------------------------------------------------------------------------- #

# File Name:        hello_from_pyside2.py
# Version:          0.0.1
# Created:          2024-11-08
# Modified:

# -------------------------------------------------------------------------- #

import nuke

try:
    from PySide import QtGui, QtCore
except ImportError:
    from PySide2 import QtCore, QtWidgets as QtGui

# Your script code here, using QtGui and QtCore as needed

def main():
    """
    Main function to create and display a PySide2 QDialog.

    This function checks if a QApplication instance already exists.
    If not, it creates a new QApplication instance. Then, it creates
    a QDialog with a QLabel displaying "Hello from PySide2!" and
    shows the dialog.

    The dialog has the title "Nuke PySide/PySide2 Compatibility" and
    is set to a geometry of 400x200 pixels at position (100, 100).

    Returns:
        None
    """

    # Check if a QApplication instance already exists
    app = QtGui.QApplication.instance()
    if not app:
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

# -------------------------------------------------------------------------- #

# ========================================================================== #
# 53 54 52 45 4E 47 54 48 2D 49 4E 2D 4E 55 4D 42 45 52 53 C2 A9 32 30 32 35 #
# ========================================================================== #
