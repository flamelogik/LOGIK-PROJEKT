from PySide6.QtWidgets import QLineEdit, QGridLayout

def add_line_edits(gridbox):
    line_edits = [
        QLineEdit(), QLineEdit(), QLineEdit()
    ]

    gridbox.addWidget(line_edits[0], 1, 0)
    gridbox.addWidget(line_edits[1], 1, 1)
    gridbox.addWidget(line_edits[2], 4, 1)
