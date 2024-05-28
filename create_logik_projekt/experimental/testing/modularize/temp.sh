#!/bin/bash

# touch pyflame_functions/pyflame_get_shot_name.py
# touch pyflame_functions/pyflame_print.py
# touch pyflame_functions/pyflame_get_flame_version.py
# touch pyflame_functions/pyflame_file_browser.py
# touch pyflame_functions/pyflame_resolve_shot_name.py
# touch pyflame_functions/pyflame_resolve_path_tokens.py
# touch pyflame_functions/pyflame_refresh_hooks.py
# touch pyflame_functions/pyflame_open_in_finder.py
# touch pyflame_functions/pyflame_load_config.py
# touch pyflame_functions/pyflame_save_config.py

# from PySide6 import QtWidgets, QtCore, QtGui
# import xml.etree.ElementTree as ET
# from typing import Union, List, Dict, Optional, Callable
# import os, re, datetime, shutil, ast

set -ex

# Define the directory path
directory="pyflame_functions"

# Loop through each Python file in the directory
for file in "$directory"/*.py; do
    # Extract filename without extension
    filename=$(basename -- "$file")
    filename="${filename%.*}"
    
    # Add two lines to the head of the file using sed
    sed -i "1i# filename: $filename" "$file"
    sed -i '1i\' "$file"
done
