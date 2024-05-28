#!/usr/bin/env python3

'''
File Name:        build_app.py
'''

import sys
import os

# Add the current directory to the Python path
current_dir = os.path.dirname(os.path.abspath(__file__))
sys.path.append(current_dir)

from PySide6.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton, QLineEdit, QComboBox, QLabel, QTextEdit
from PySide6.QtGui import QFont, QScreen
from define_popup_menud import popup_menu_definitions

def generate_template():
    print("Generate LOGIK-PROJEKT Template button clicked")
    # Add functionality to generate LOGIK-PROJEKT template here

def create_popup_menu(items, label_text):
    label = QLabel(label_text)
    label.setStyleSheet("color: #CCCCCC; font-weight: bold;")  # Slightly less than white

    popup_menu = QComboBox()
    popup_menu.setStyleSheet("background-color: #111111; color: white;")  # Darker than the background, text color white
    popup_menu.addItems(items)
    popup_menu.currentIndexChanged.connect(update_summary)  # Connect the signal to update summary when value changes
    
    return label, popup_menu

def update_summary():
    global proj_res, proj_res_h, proj_res_v, proj_aspect_ratio, proj_color_depth, proj_fcm, proj_color_science, default_start_frame
    
    selected_resolution = define_popup_menud.popup_menu_definitions["Resolution"][1].currentText()
    proj_res_h, proj_res_v = selected_resolution.split(' x ')
    proj_res_h = int(proj_res_h.split()[0])  # Extract numeric part and convert to integer
    proj_res_v = int(proj_res_v.split()[0])  # Extract numeric part and convert to integer
    
    proj_res = f"{proj_res_h} x {proj_res_v}"
    proj_aspect_ratio = float(proj_res_h) / float(proj_res_v)
    proj_color_depth = define_popup_menud.popup_menu_definitions["Bit Depth"][1].currentText()
    proj_fcm = define_popup_menud.popup_menu_definitions["Frame Rate"][1].currentText()
    proj_color_science = define_popup_menud.popup_menu_definitions["Color Science"][1].currentText()
    default_start_frame = define_popup_menud.popup_menu_definitions["Start Frame"][1].currentText()
    
    # Update summary text
    summary_textbox.clear()
    summary_textbox.append(f"Client Name: {client_name_entry.text()}")
    summary_textbox.append(f"Campaign Name: {campaign_name_entry.text()}")
    summary_textbox.append(f"Resolution: {proj_res}")
    summary_textbox.append(f"Aspect Ratio: {proj_aspect_ratio}")
    summary_textbox.append(f"Color Depth: {proj_color_depth}")
    summary_textbox.append(f"Frame Rate: {proj_fcm}")
    summary_textbox.append(f"Color Science: {proj_color_science}")
    summary_textbox.append(f"Start Frame: {default_start_frame}")

def build_app():
    global client_name_entry, campaign_name_entry, summary_textbox
    
    app = QApplication(sys.argv)
    window = QWidget()
    window.setWindowTitle("LOGIK-PROJEKT")
    window.resize(640, 480)  # Set the initial size of the window

    # Set the background color to much darker grey
    window.setStyleSheet("background-color: #333333;")

    layout = QVBoxLayout()

    # Text Entry Boxes
    client_name_entry = QLineEdit()
    client_name_entry.setStyleSheet("background-color: #808080;")  # Set text entry box color to 50% grey
    client_name_entry.setPlaceholderText("Enter client name")
    client_name_label = QLabel("Client Name:")
    client_name_label.setStyleSheet("color: #CCCCCC; font-weight: bold;")  # Slightly less than white
    layout.addWidget(client_name_label)
    layout.addWidget(client_name_entry)

    campaign_name_entry = QLineEdit()
    campaign_name_entry.setStyleSheet("background-color: #808080;")  # Set text entry box color to 50% grey
    campaign_name_entry.setPlaceholderText("Enter campaign name")
    campaign_name_label = QLabel("Campaign Name:")
    campaign_name_label.setStyleSheet("color: #CCCCCC; font-weight: bold;")  # Slightly less than white
    layout.addWidget(campaign_name_label)
    layout.addWidget(campaign_name_entry)

    # Pop-Up Menus
    for label_text, items in define_popup_menud.popup_menu_definitions.items():
        label, menu = create_popup_menu(items, label_text)
        layout.addWidget(label)
        layout.addWidget(menu)

    # Summary Text Box
    summary_label = QLabel("Projekt Summary:")
    summary_label.setStyleSheet("color: #CCCCCC; font-weight: bold;")  # Slightly less than white
    layout.addWidget(summary_label)

    summary_textbox = QTextEdit()
    summary_textbox.setStyleSheet("background-color: #555555; color: white;")  # Darker than the background, text color white
    layout.addWidget(summary_textbox)

    # Call update_summary to populate the summary initially
    update_summary()

    # Generate Template Button
    generate_button = QPushButton("Generate LOGIK-PROJEKT Template")
    generate_button.clicked.connect(generate_template)
    generate_button.setStyleSheet("color: white; font-weight: bold;")
    layout.addWidget(generate_button)

    # Cancel Button
    cancel_button = QPushButton("Cancel")
    cancel_button.clicked.connect(window.close)  # Close the window when the Cancel button is clicked
    cancel_button.setStyleSheet("color: white; font-weight: bold;")
    layout.addWidget(cancel_button)

    window.setLayout(layout)

    # Get the geometry of the screen
    screen_geometry = app.primaryScreen().geometry()

    # Get the center position of the screen
    center_point = screen_geometry.center()

    # Calculate the top-left corner position of the window
    top_left_corner = center_point - window.rect().center()

    # Move the window to the calculated position
    window.move(top_left_corner)

    # Set the minimum font size for labels
    font = window.font()
    font.setPointSize(24)  # Set the minimum font size to 24 points
    window.setFont(font)

    window.show()

    sys.exit(app.exec())

if __name__ == "__main__":
    build_app()
