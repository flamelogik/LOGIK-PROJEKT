import json
import re
import os
import tkinter as tk
from tkinter import filedialog
import argparse

def reformat_name(name):
    # This regular expression will capture the dimensions and the rest of the string
    match = re.search(r'^(.*?) \((\d+ x \d+)\)$', name)
    if match:
        string_part = match.group(1)
        dimensions = match.group(2)
        # Reformatting the name to the desired format
        new_name = f'{dimensions} | {string_part}'
        return new_name
    return name

def process_json_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        data = json.load(file)
    
    def process_value(value):
        if isinstance(value, str):
            # Check for the specific patterns you mentioned
            if re.match(r'^.* \(\d+ x \d+\)$', value):
                return reformat_name(value)
        elif isinstance(value, list):
            return [process_value(item) for item in value]
        elif isinstance(value, dict):
            return {k: process_value(v) for k, v in value.items()}
        return value
    
    modified_data = process_value(data)
    
    modified_file_path = f"{os.path.splitext(file_path)[0]}.modified.json"
    with open(modified_file_path, 'w', encoding='utf-8') as file:
        json.dump(modified_data, file, indent=4)
    print(f"Modified file saved as: {modified_file_path}")

def choose_file_and_process():
    root = tk.Tk()
    root.withdraw()  # Hide the root window
    file_path = filedialog.askopenfilename(filetypes=[("JSON files", "*.json"), ("All files", "*.*")])
    if file_path:
        process_json_file(file_path)

# Allow user to specify the file to modify via command-line or GUI
if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Modify JSON files.')
    parser.add_argument('--file', help='The path to the JSON file to modify.')
    args = parser.parse_args()

    if args.file:
        process_json_file(args.file)
    else:
        choose_file_and_process()
