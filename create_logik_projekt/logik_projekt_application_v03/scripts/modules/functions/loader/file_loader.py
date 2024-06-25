# import json
# import os

# CONFIG_TEMPLATE_DIR = os.path.join(os.path.dirname(__file__), '..', '..', 'config', 'template')

# def load_file(file_name):
#     file_path = os.path.join(CONFIG_TEMPLATE_DIR, file_name)
#     if not os.path.exists(file_path):
#         raise FileNotFoundError(f"File {file_name} not found in {CONFIG_TEMPLATE_DIR}")
    
#     with open(file_path, 'r') as file:
#         data = json.load(file)
#     return data







import json
import os

def load_json(file_path):
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"File {file_path} not found")
    
    with open(file_path, 'r') as file:
        data = json.load(file)
    return data
