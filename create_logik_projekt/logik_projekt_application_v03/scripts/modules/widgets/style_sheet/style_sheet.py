import os

def load_style_sheet(file_name):
    style_sheet_path = os.path.join(os.path.dirname(__file__), file_name)
    if not os.path.exists(style_sheet_path):
        raise FileNotFoundError(f"Style sheet {file_name} not found")
    
    with open(style_sheet_path, 'r') as file:
        style_sheet = file.read()
    return style_sheet

def apply_style_sheet(app, file_name):
    style_sheet = load_style_sheet(file_name)
    app.setStyleSheet(style_sheet)
