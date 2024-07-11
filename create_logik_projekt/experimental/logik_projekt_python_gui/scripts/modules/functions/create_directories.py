import json
import os

# Load the JSON configuration
with open('config/strukture_projekt_dirs.json', 'r') as f:
    config = json.load(f)

# Prepare the directory path
dir_path = eval(config['dir_template'].format(parent_dir_path=config['parent_dir_path'], name=config['name']))

# Update the config with the actual directory path
config['Path'] = dir_path

# Now you can use `config['Path']` and other variables as needed
print(f"Directory Path: {config['Path']}")
