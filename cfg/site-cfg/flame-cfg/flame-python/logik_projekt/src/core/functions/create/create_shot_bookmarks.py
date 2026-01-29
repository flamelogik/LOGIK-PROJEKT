import os
import json

def get_shot_folders(shots_dir):
    """
    Get all shot folders in the specified directory and sort them.
    """
    shot_folders = [f for f in os.listdir(shots_dir) if os.path.isdir(os.path.join(shots_dir, f))]
    return sorted(shot_folders)  # Sort the list of shot folders

def update_bookmarks_json(shots_dir, json_file_path):
    """
    Update the bookmarks JSON file with shot folders.
    """
    # Read existing JSON file
    with open(json_file_path, 'r') as f:
        bookmarks_data = json.load(f)

    # Find the "shots" folder in the JSON structure
    shots_folder = None
    for section in bookmarks_data['DlBookmark']['Sections']:
        if section['Section'] == 'Project':
            for bookmark in section['Bookmarks']:
                if 'Folder' in bookmark and bookmark['Folder'] == 'projekt directories':
                    for subfolder in bookmark['Bookmarks']:
                        if subfolder['Folder'] == 'shots':
                            shots_folder = subfolder
                            break
                if shots_folder:
                    break
        if shots_folder:
            break

    if not shots_folder:
        raise ValueError("Shots folder not found in the JSON structure")

    # Get shot folders
    shot_folders = get_shot_folders(shots_dir)

    # Update shots folder bookmarks
    shots_folder['Bookmarks'] = [
        {
            "Bookmark": shot,
            "Path": os.path.join(shots_dir, shot),
            "Visibility": "Global"
        } for shot in shot_folders
    ]

    # Write updated JSON back to file
    with open(json_file_path, 'w') as f:
        json.dump(bookmarks_data, f, indent=4)

    print(f"Updated {len(shot_folders)} shot bookmarks in {json_file_path}")

if __name__ == "__main__":
    shots_dir = "/PROJEKTS/example_projekt_name/shots"  # Replace with your actual shots directory
    json_file_path = "/path/to/your/bookmarks.json"  # Replace with your actual JSON file path
    update_bookmarks_json(shots_dir, json_file_path)