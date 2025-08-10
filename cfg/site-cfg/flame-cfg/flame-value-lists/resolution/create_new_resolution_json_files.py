import json
import os
from pathlib import Path

def update_resolution_names_in_json(folder_path):
    folder = Path(folder_path)
    json_files = list(folder.glob("*.json"))

    for file_path in json_files:
        with open(file_path, "r", encoding="utf-8") as f:
            data = json.load(f)

        # Traverse and update resolution_name
        for group in data.get("items", []):
            for item in group.get("items", []):
                if "resolution_name" in item and "pixel_aspect_ratio" in item:
                    name = item["resolution_name"]
                    par = item["pixel_aspect_ratio"]
                    if f"x {par} |" not in name:  # prevent duplicate insertion
                        parts = name.split(" |", 1)
                        if len(parts) == 2:
                            res, desc = parts
                            new_name = f"{res} x {par} |{desc}"
                            item["resolution_name"] = new_name

        # Write to new file
        new_file_path = file_path.with_stem(file_path.stem + "_new")
        with open(new_file_path, "w", encoding="utf-8") as f:
            json.dump(data, f, indent=4)
        print(f"Created: {new_file_path}")

# Example usage
update_resolution_names_in_json("/home/pman/workspace/GitHub/phil-man-git-hub/LOGIK-PROJEKT-2027/app/parameters/json/resolution")  # Replace with your folder path
