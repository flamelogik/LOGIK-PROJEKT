# import os
# import re

# def flame_family_app_list(directory):
#     try:
#         # List all entries in the directory
#         entries = os.listdir(directory)
        
#         # Filter for directories that begin with 'flame_'
#         flame_dirs = [entry for entry in entries if entry.startswith('flame_') and os.path.isdir(os.path.join(directory, entry))]
        
#         # Sort the list alphanumerically using custom sorting logic
#         flame_dirs = sorted(flame_dirs, key=version_key)
        
#         # Print the sorted list
#         print("Sorted flame_ directories:")
#         for dir_name in flame_dirs:
#             print(dir_name)
    
#     except Exception as e:
#         print(f"An error occurred: {e}")

# def version_key(directory_name):
#     """
#     Extracts the version information from a directory name and converts it into a tuple
#     that can be used for sorting. Handles prerelease versions by considering them lower value
#     than release versions.
#     """
#     pattern = r'flame_(\d+)(?:\.(\d+))?(?:\.(\d+))?(?:\.(pr\d+))?'
#     match = re.match(pattern, directory_name)
    
#     if not match:
#         return (0, 0, 0, '')  # Return a default tuple for non-matching names
    
#     major = int(match.group(1)) if match.group(1) else 0
#     minor = int(match.group(2)) if match.group(2) else 0
#     patch = int(match.group(3)) if match.group(3) else 0
#     prerelease = match.group(4) or ''
    
#     # Prerelease versions are considered lower value than release versions
#     if prerelease:
#         return (major, minor, patch, prerelease)
#     else:
#         return (major, minor, patch, 'release')

# if __name__ == "__main__":
#     directory_path = "/opt/Autodesk"
#     flame_family_app_list(directory_path)












# import os
# import re

# def flame_family_app_list(directory):
#     flame_family_prefixes = ['flame', 'flame_assist', 'flare', 'smoke', 'project_server']

#     try:
#         # List all entries in the directory
#         entries = os.listdir(directory)
        
#         # Filter for directories that match any of the flame family prefixes
#         flame_dirs = [entry for entry in entries if any(entry.startswith(prefix) for prefix in flame_family_prefixes) and os.path.isdir(os.path.join(directory, entry))]
        
#         # Sort the list alphanumerically using custom sorting logic
#         flame_dirs = sorted(flame_dirs, key=version_key)
        
#         # Print the sorted list
#         print("Sorted flame family directories:")
#         for dir_name in flame_dirs:
#             print(dir_name)
    
#     except Exception as e:
#         print(f"An error occurred: {e}")

# def version_key(directory_name):
#     """
#     Extracts the version information from a directory name and converts it into a tuple
#     that can be used for sorting. Handles prerelease versions by considering them lower value
#     than release versions.
#     """
#     pattern = r'(\w+)_(\d+)(?:\.(\d+))?(?:\.(\d+))?(?:\.(pr\d+))?'
#     match = re.match(pattern, directory_name)
    
#     if not match:
#         return (directory_name, 0, 0, 0, '')  # Return a default tuple for non-matching names
    
#     name = match.group(1)
#     major = int(match.group(2)) if match.group(2) else 0
#     minor = int(match.group(3)) if match.group(3) else 0
#     patch = int(match.group(4)) if match.group(4) else 0
#     prerelease = match.group(5) or ''
    
#     # Prerelease versions are considered lower value than release versions
#     if prerelease:
#         return (name, major, minor, patch, prerelease)
#     else:
#         return (name, major, minor, patch, 'release')

# if __name__ == "__main__":
#     # directory_path = "/opt/Autodesk"
#     directory_path = "/home/pman/dummy_software_folders"
#     flame_family_app_list(directory_path)


















# import os
# import re

# def flame_family_app_list(directory):
#     flame_family_prefixes = ['flame', 'project_server', 'flare', 'flame_assist', 'smoke']

#     try:
#         # List all entries in the directory
#         entries = os.listdir(directory)
        
#         # Filter for directories that match any of the flame family prefixes
#         flame_dirs = [entry for entry in entries if any(entry.startswith(prefix) for prefix in flame_family_prefixes) and os.path.isdir(os.path.join(directory, entry))]
        
#         # Sort the list using custom sorting logic
#         flame_dirs = sorted(flame_dirs, key=custom_sort_key)
        
#         # Print the sorted list
#         print("Sorted flame family directories:")
#         for dir_name in flame_dirs:
#             print(dir_name)
    
#     except Exception as e:
#         print(f"An error occurred: {e}")

# def custom_sort_key(directory_name):
#     """
#     Custom sorting key function that combines software name importance and version information.
#     """
#     software_importance = {
#         'flame': 5,
#         'project_server': 4,
#         'flare': 3,
#         'flame_assist': 2,
#         'smoke': 1
#     }

#     # Extract version information from directory name
#     pattern = r'(\w+)_(\d+)(?:\.(\d+))?(?:\.(\d+))?(?:\.(pr\d+))?'
#     match = re.match(pattern, directory_name)
    
#     if not match:
#         return (0, '', 0, 0, 0, '')  # Return a default tuple for non-matching names
    
#     name = match.group(1)
#     major = int(match.group(2)) if match.group(2) else 0
#     minor = int(match.group(3)) if match.group(3) else 0
#     patch = int(match.group(4)) if match.group(4) else 0
#     prerelease = match.group(5) or ''
    
#     # Determine software importance or default to 0 if not found
#     importance = software_importance.get(name, 0)
    
#     # Return a tuple combining importance and version information for sorting
#     return (importance, name, major, minor, patch, prerelease)

# if __name__ == "__main__":
#     # directory_path = "/opt/Autodesk"
#     directory_path = "/home/pman/dummy_software_folders"
#     flame_family_app_list(directory_path)











# import os
# import re

# def flame_family_app_list(directory):
#     flame_family_prefixes = ['flame', 'project_server', 'flare', 'flame_assist', 'smoke']

#     try:
#         # List all entries in the directory
#         entries = os.listdir(directory)
        
#         # Filter for directories that match any of the flame family prefixes
#         flame_dirs = [entry for entry in entries if any(entry.startswith(prefix) for prefix in flame_family_prefixes) and os.path.isdir(os.path.join(directory, entry))]
        
#         # Sort the list using custom sorting logic
#         flame_dirs = sorted(flame_dirs, key=sorting_key)
        
#         # Print the sorted list
#         print("Sorted flame family directories:")
#         for dir_name in flame_dirs:
#             print(dir_name)
    
#     except Exception as e:
#         print(f"An error occurred: {e}")

# def sorting_key(directory_name):
#     """
#     Sorting key function that prioritizes version information over software importance.
#     """
#     return (version_key(directory_name), app_key(directory_name))

# def version_key(directory_name):
#     """
#     Extracts the version information from a directory name and converts it into a tuple
#     that can be used for sorting. Handles prerelease versions by considering them lower value
#     than release versions.
#     """
#     pattern = r'(\w+)_(\d+)(?:\.(\d+))?(?:\.(\d+))?(?:\.(pr\d+))?'
#     match = re.match(pattern, directory_name)
    
#     if not match:
#         return (0, '', 0, 0, 0, '')  # Return a default tuple for non-matching names
    
#     name = match.group(1)
#     major = int(match.group(2)) if match.group(2) else 0
#     minor = int(match.group(3)) if match.group(3) else 0
#     patch = int(match.group(4)) if match.group(4) else 0
#     prerelease = match.group(5) or ''
    
#     # Prerelease versions are considered lower value than release versions
#     if prerelease:
#         return (1, name, major, minor, patch, prerelease)
#     else:
#         return (2, name, major, minor, patch, 'release')

# def app_key(directory_name):
#     """
#     Application key function that assigns importance based on software name in the Flame family.
#     """
#     software_importance = {
#         'flame': 5,
#         'project_server': 4,
#         'flare': 3,
#         'flame_assist': 2,
#         'smoke': 1
#     }
    
#     name = directory_name.split('_')[0]  # Extract software name from directory_name
    
#     return software_importance.get(name, 0)

# if __name__ == "__main__":
#     # directory_path = "/opt/Autodesk"
#     directory_path = "/home/pman/dummy_software_folders"
#     flame_family_app_list(directory_path)
















# import os
# import re

# def flame_family_app_list(directory):
#     flame_family_prefixes = ['flame', 'project_server', 'flare', 'flame_assist', 'smoke']

#     try:
#         # List all entries in the directory
#         entries = os.listdir(directory)
        
#         # Filter for directories that match any of the flame family prefixes
#         flame_dirs = [entry for entry in entries if any(entry.startswith(prefix) for prefix in flame_family_prefixes) and os.path.isdir(os.path.join(directory, entry))]
        
#         # Sort the list using custom sorting logic
#         flame_dirs = sorted(flame_dirs, key=sorting_key)
        
#         # Print the sorted list
#         print("Sorted flame family directories:")
#         for dir_name in flame_dirs:
#             print(dir_name)
    
#     except Exception as e:
#         print(f"An error occurred: {e}")

# def sorting_key(directory_name):
#     """
#     Sorting key function that prioritizes software name and version information.
#     """
#     return (app_key(directory_name), version_key(directory_name))

# def version_key(directory_name):
#     """
#     Extracts the version information from a directory name and converts it into a tuple
#     that can be used for sorting. Handles prerelease versions by considering them lower value
#     than release versions.
#     """
#     pattern = r'(\w+)_(\d+)(?:\.(\d+))?(?:\.(\d+))?(?:\.(pr\d+))?'
#     match = re.match(pattern, directory_name)
    
#     if not match:
#         return (0, '', 0, 0, 0, '')  # Return a default tuple for non-matching names
    
#     name = match.group(1)
#     major = int(match.group(2)) if match.group(2) else 0
#     minor = int(match.group(3)) if match.group(3) else 0
#     patch = int(match.group(4)) if match.group(4) else 0
#     prerelease = match.group(5) or ''
    
#     # Prerelease versions are considered lower value than release versions
#     if prerelease:
#         return (1, name, major, minor, patch, prerelease)
#     else:
#         return (2, name, major, minor, patch, 'release')

# def app_key(directory_name):
#     """
#     Application key function that assigns importance based on software name in the Flame family.
#     """
#     software_importance = {
#         'flame': 5,
#         'project_server': 4,
#         'flare': 3,
#         'flame_assist': 2,
#         'smoke': 1
#     }
    
#     name = directory_name.split('_')[0]  # Extract software name from directory_name
    
#     return software_importance.get(name, 0)

# if __name__ == "__main__":
#     # directory_path = "/opt/Autodesk"
#     directory_path = "/home/pman/dummy_software_folders"
#     flame_family_app_list(directory_path)






# import os
# import re

# def flame_family_app_list(directory):
#     flame_family_prefixes = ['flame', 'project_server', 'flare', 'flame_assist', 'smoke']

#     try:
#         # List all entries in the directory
#         entries = os.listdir(directory)
        
#         # Filter for directories that match any of the flame family prefixes
#         flame_dirs = [entry for entry in entries if any(entry.startswith(prefix) for prefix in flame_family_prefixes) and os.path.isdir(os.path.join(directory, entry))]
        
#         # Sort the list using custom sorting logic
#         flame_dirs = sorted(flame_dirs, key=sort_key)
        
#         # Print the sorted list
#         print("Sorted flame family directories:")
#         for dir_name in flame_dirs:
#             print(dir_name)
    
#     except Exception as e:
#         print(f"An error occurred: {e}")

# def sort_key(directory_name):
#     """
#     Sorting key function that composes a numeric value for sorting based on major, minor, patch,
#     app_key, and prerelease.
#     """
#     pattern = r'(\w+)_(\d+)(?:\.(\d+))?(?:\.(\d+))?(?:\.(pr\d+))?'
#     match = re.match(pattern, directory_name)
    
#     if not match:
#         return (0, 0, 0, 0, 0)  # Return a default tuple for non-matching names
    
#     name = match.group(1)
#     major = int(match.group(2)) if match.group(2) else 0
#     minor = int(match.group(3)) if match.group(3) else 0
#     patch = int(match.group(4)) if match.group(4) else 0
#     prerelease = match.group(5) or ''
    
#     # Determine app_key value
#     app_importance = {
#         'flame': 5,
#         'project_server': 4,
#         'flare': 3,
#         'flame_assist': 2,
#         'smoke': 1
#     }
#     app_value = app_importance.get(name, 0)
    
#     # Set prerelease_value based on whether it's a release or prerelease version
#     prerelease_value = 999 if not prerelease else int(prerelease[2:])
    
#     # Create a tuple for sorting
#     return (major, minor, patch, app_value, prerelease_value)

# if __name__ == "__main__":
#     # directory_path = "/opt/Autodesk"
#     directory_path = "/home/pman/dummy_software_folders"
#     flame_family_app_list(directory_path)









import os
import re

def flame_family_app_list(directory):
    flame_family_prefixes = ['flame', 'project_server', 'flare', 'flame_assist', 'smoke']

    try:
        # List all entries in the directory
        entries = os.listdir(directory)
        
        # Filter for directories that match any of the flame family prefixes
        flame_dirs = [entry for entry in entries if any(entry.startswith(prefix) for prefix in flame_family_prefixes) and os.path.isdir(os.path.join(directory, entry))]
        
        # # Sort the list using custom sorting logic
        # flame_dirs = sorted(flame_dirs, key=sort_key)
        
        # Sort the list in descending order using custom sorting logic
        flame_dirs = sorted(flame_dirs, key=sort_key, reverse=True)

        return flame_dirs
    
    except Exception as e:
        print(f"An error occurred: {e}")
        return []

def sort_key(directory_name):
    """
    Sorting key function that composes a numeric value for sorting based on major, minor, patch,
    app_key, and prerelease.
    """
    pattern = r'(\w+)_(\d+)(?:\.(\d+))?(?:\.(\d+))?(?:\.(pr\d+))?'
    match = re.match(pattern, directory_name)
    
    if not match:
        return (0, 0, 0, 0, 0)  # Return a default tuple for non-matching names
    
    name = match.group(1)
    major = int(match.group(2)) if match.group(2) else 0
    minor = int(match.group(3)) if match.group(3) else 0
    patch = int(match.group(4)) if match.group(4) else 0
    prerelease = match.group(5) or ''
    
    # Determine app_key value
    app_importance = {
        'flame': 5,
        'project_server': 4,
        'flare': 3,
        'flame_assist': 2,
        'smoke': 1
    }
    app_value = app_importance.get(name, 0)
    
    # Set prerelease_value based on whether it's a release or prerelease version
    prerelease_value = 999 if not prerelease else int(prerelease[2:])
    
    # Create a tuple for sorting
    return (major, minor, patch, app_value, prerelease_value)

def sanitize_app_name(app_name):
    """
    Reformat the application name by replacing periods with underscores.
    """
    return app_name.replace('.', '_')

if __name__ == "__main__":
    directory_path = "/opt/Autodesk"  # Example directory path
    flame_apps = flame_family_app_list(directory_path)
    print(flame_apps)
