# from PySide6.QtWidgets import QComboBox
# import os

# def create_combo_box_init_config_qt6(directory="logik_projekt_application/config/init_configs/template/"):
#     combo_box = QComboBox()

#     # Populate combo box with filenames from the specified directory
#     try:
#         filenames = [f for f in os.listdir(directory) if os.path.isfile(os.path.join(directory, f))]
#         combo_box.addItems(filenames)
#     except FileNotFoundError:
#         combo_box.addItem("No files found")
    
#     return combo_box






# from PySide6.QtWidgets import QComboBox
# import os

# init_cfgs_dir="../../../../config/init_configs/template/"

# def create_combo_box_init_config_qt6(init_cfgs_dir):
#     combo_box = QComboBox()

#     # Use relative path to populate combo box with filenames from the specified directory
#     directory = os.path.join(os.path.dirname(__file__), init_cfgs_dir)
#     directory = os.path.abspath(directory)

#     try:
#         filenames = [f for f in os.listdir(directory) if os.path.isfile(os.path.join(directory, f))]
#         combo_box.addItems(filenames)
#     except FileNotFoundError:
#         combo_box.addItem("No files found")
    
#     return combo_box











from PySide6.QtWidgets import QComboBox
import os

def create_combo_box_init_config_qt6(init_cfgs_dir):
    combo_box = QComboBox()

    # Use relative path to populate combo box with filenames from the specified directory
    directory = os.path.abspath(os.path.join(os.path.dirname(__file__), init_cfgs_dir))

    try:
        filenames = [f for f in os.listdir(directory) if os.path.isfile(os.path.join(directory, f))]
        if filenames:
            combo_box.addItems(filenames)
        else:
            combo_box.addItem("No files found")
    except FileNotFoundError:
        combo_box.addItem("Directory not found")

    return combo_box
