stylesheet = """
/* Set the background color */
QWidget {
    background-color: #242424; /* Replace with your desired color */
}

/* Text color (white) */
QPushButton, QLineEdit, QComboBox {
    color: #ffffff; /* White color */
}

/* Label text color */
QLabel {
    color: #9F9F9F; /* Label color */
}

/* Font (Discreet 14 px) */
QLabel, QPushButton, QLineEdit, QComboBox {
    font: 14px "Discreet"; /* Replace with the actual font name */
}

/* Disabled Button color */
QPushButton:disabled {
    background-color: #4D0000; /* Replace with your desired color */
}

/* Enabled Button Color */
QPushButton {
    background-color: #4D0000; /* Replace with your desired color */
}

/* Lineedit Text Entry Background */
QLineEdit {
    background-color: #37414b; /* Replace with your desired color */
    padding: 4px;
}

/* Dropdown menu */
QComboBox {
    background-color: #2c3644; /* Replace with your desired color */
    border: none; /* Remove border */
    border-radius: 0; /* Remove rounded corners */
    padding: 5px;
}

# /* Remove 3D relief from dropdown arrow */
# QComboBox::drop-down {
#     border: none; /* Remove border */
#     background: none; /* Remove background */
# }

# QComboBox::down-arrow {
#     image: url(your_icon_path/down-arrow.png); /* Replace with your desired icon path */
#     width: 12px; /* Adjust width if necessary */
#     height: 12px; /* Adjust height if necessary */
# }

/* Dropdown menu selection */
QComboBox QAbstractItemView::item:selected {
    background-color: #2c3644; /* Replace with your desired color */
}

/* QComboBox Popup styling */
QComboBox QAbstractItemView {
    border: none; /* Remove border */
    background-color: #2a3341; /* Background color of dropdown items */
}

/* Summary box (QTextEdit) */
QTextEdit {
    background-color: #37414b;  /* Replace with your desired color */
    color: #ffffff;  /* Text color */
    font: 14px "Discreet";  /* Font */
    border: 1px solid #007acc;  /* Border */
    border-radius: 0px;  /* No rounded corners */
}
"""
