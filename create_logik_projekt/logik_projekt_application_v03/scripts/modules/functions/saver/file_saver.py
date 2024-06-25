import json
import os

CONFIG_CFG_BAK_DIR = os.path.join(os.path.dirname(__file__), '..', '..', 'config', 'cfg_bak')

def save_file(file_name, data):
    file_path = os.path.join(CONFIG_CFG_BAK_DIR, file_name)
    with open(file_path, 'w') as file:
        json.dump(data, file, indent=4)
    return file_path
