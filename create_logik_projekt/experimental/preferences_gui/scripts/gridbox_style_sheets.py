# scripts/modules/gui_components/pyside6_stylesheet.py

stylesheet = """
/* General styling */
QWidget {
    background-color: #f0f0f0;
}

QLabel {
    font-size: 16px;
    color: #333333;
}

QPushButton {
    background-color: #4CAF50;
    color: white;
    border: none;
    padding: 10px 20px;
    text-align: center;
    text-decoration: none;
    display: inline-block;
    font-size: 16px;
    margin: 4px 2px;
    cursor: pointer;
}

QPushButton:hover {
    background-color: #45a049;
}

QComboBox {
    background-color: white;
    border: 1px solid #ccc;
    border-radius: 4px;
    padding: 5px;
    min-width: 100px;
}

QLineEdit {
    background-color: white;
    border: 1px solid #ccc;
    border-radius: 4px;
    padding: 5px;
    min-width: 100px;
}

/* Menu styling */
QMenu {
    color: #9a9a9a;
    background-color: #2d3744;
    border: none;
    font: 14px "Discreet";
}

QMenu::item:selected {
    color: #d9d9d9;
    background-color: #3a4551;
}
"""
