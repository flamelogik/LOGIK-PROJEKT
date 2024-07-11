# logik_projekt_application/scripts/modules/widgets/drop_down/drop_down_flame_framestores.py

from PySide6.QtWidgets import QComboBox
from ...functions.list_volumes.list_flame_framestores import list_framestores

def create_drop_down_framestores_qt6():
    # Create a QComboBox
    combo_box = QComboBox()

    # Populate the combo box with framestores
    framestore_list = list_framestores()
    if framestore_list:
        combo_box.addItems(framestore_list)
    else:
        combo_box.addItem("No framestores available")

    return combo_box
