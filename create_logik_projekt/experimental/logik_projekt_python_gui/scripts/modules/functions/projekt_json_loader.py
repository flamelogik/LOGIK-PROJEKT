# import json
# import os

# # Define the base directory relative to the main script
# BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
# CONFIG_DIR = os.path.join(BASE_DIR, 'config')

# def load_json_file(file_path):
#     with open(file_path, 'r') as file:
#         return json.load(file)

# def load_projekt_json_resolutions():
#     resolution_files = [
#         'resolutions-aja.json',
#         'resolutions-arri.json',
#         'resolutions-bmd.json',
#         'resolutions-broadcast.json',
#         'resolutions-canon.json',
#         'resolutions-dcp.json',
#         'resolutions-film.json',
#         'resolutions-full.json',
#         'resolutions-miscellaneous.json',
#         'resolutions-panasonic.json',
#         'resolutions-red.json',
#         'resolutions-sony.json',
#         'resolutions-zcam.json',
#     ]
#     resolutions = {}
#     for filename in resolution_files:
#         file_path = os.path.join(CONFIG_DIR, filename)
#         key = os.path.splitext(filename)[0]
#         resolutions[key] = load_json_file(file_path)
#     return resolutions

# def load_projekt_json_frame_rates():
#     file_path = os.path.join(CONFIG_DIR, 'frame_rates.json')
#     return load_json_file(file_path)

# def load_projekt_json_scan_modes():
#     file_path = os.path.join(CONFIG_DIR, 'scan_modes.json')
#     return load_json_file(file_path)

# def load_projekt_json_bit_depths():
#     file_path = os.path.join(CONFIG_DIR, 'bit_depths.json')
#     return load_json_file(file_path)

# def load_projekt_json_color_science():
#     file_path = os.path.join(CONFIG_DIR, 'color_science.json')
#     return load_json_file(file_path)

# def load_projekt_json_start_frames():
#     file_path = os.path.join(CONFIG_DIR, 'start_frames.json')
#     return load_json_file(file_path)


import json
import os

# Define the base directory relative to the main script
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CONFIG_DIR = os.path.join(BASE_DIR, 'config')

# def load_json_file(file_path):
#     with open(file_path, 'r') as file:
#         return json.load(file)

# def load_json_file(file_path):
#     with open(file_path, 'r') as file:
#         data = json.load(file)
#         print(f"Loaded JSON file from: {file_path}")
#         return data

def load_json_file(file_path):
    print(f"Loading JSON file: {file_path}")
    with open(file_path, 'r') as file:
        print(f"File opened successfully")
        data = json.load(file)
        print(f"JSON data loaded successfully from {file_path}:")
        print(data)
        return data

def extract_items(data):
    """
    Recursively extract items from nested structure.
    """
    items = []
    if isinstance(data, list):
        for element in data:
            items.extend(extract_items(element))
    elif isinstance(data, dict):
        if 'items' in data:
            items.extend(extract_items(data['items']))
        else:
            items.append(data)
    return items

def load_projekt_json_resolutions():
    resolution_files = [
        'resolutions-aja.json',
        'resolutions-arri.json',
        'resolutions-bmd.json',
        'resolutions-broadcast.json',
        'resolutions-canon.json',
        'resolutions-dcp.json',
        'resolutions-film.json',
        'resolutions-full.json',
        'resolutions-miscellaneous.json',
        'resolutions-panasonic.json',
        'resolutions-red.json',
        'resolutions-sony.json',
        'resolutions-zcam.json',
    ]
    resolutions = {}
    for filename in resolution_files:
        file_path = os.path.join(CONFIG_DIR, filename)
        key = os.path.splitext(filename)[0]
        resolutions[key] = extract_items(load_json_file(file_path))
    return resolutions

def load_projekt_json_frame_rates():
    file_path = os.path.join(CONFIG_DIR, 'frame_rates.json')
    return extract_items(load_json_file(file_path))

def load_projekt_json_scan_modes():
    file_path = os.path.join(CONFIG_DIR, 'scan_modes.json')
    return extract_items(load_json_file(file_path))

def load_projekt_json_bit_depths():
    file_path = os.path.join(CONFIG_DIR, 'bit_depths.json')
    return extract_items(load_json_file(file_path))

def load_projekt_json_color_science():
    file_path = os.path.join(CONFIG_DIR, 'color_science.json')
    return extract_items(load_json_file(file_path))

def load_projekt_json_start_frames():
    file_path = os.path.join(CONFIG_DIR, 'start_frames.json')
    return extract_items(load_json_file(file_path))
