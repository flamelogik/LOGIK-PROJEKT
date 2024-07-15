# logik_projekt_application/scripts/modules/widgets/drop_down/drop_down_flame_family_software.py

from PySide6.QtWidgets import QComboBox
from ...functions.list_software.list_flame_family_software import flame_family_app_list

def create_drop_down_flame_software_qt6():
    # Create a QComboBox
    combo_box = QComboBox()

    # Populate the combo box with flame family apps
    flame_family_apps = flame_family_app_list("/home/pman/testing")  # Adjust the directory path
    combo_box.addItems(flame_family_apps)

    return combo_box
