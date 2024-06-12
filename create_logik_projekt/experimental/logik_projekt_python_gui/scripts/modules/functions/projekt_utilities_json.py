# import os
# import json

# def load_combined_json_data(json_dir, json_files):
#     combined_data = {"items": []}
    
#     for json_file in json_files:
#         file_path = os.path.join(json_dir, json_file)
#         with open(file_path, 'r') as file:
#             data = json.load(file)
#             combined_data["items"].extend(data.get("items", []))
    
#     return combined_data

import os
import json

def load_combined_json_data(base_dir, json_files):
    combined_data = {"items": []}
    
    for json_file in json_files:
        file_path = os.path.join(base_dir, json_file)
        with open(file_path, 'r') as file:
            data = json.load(file)
            combined_data["items"].extend(data.get("items", []))
    
    return combined_data
