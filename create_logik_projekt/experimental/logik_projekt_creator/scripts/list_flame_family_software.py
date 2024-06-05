import os
import re

def list_flame_family_software(directory):
    try:
        # List all entries in the directory
        entries = os.listdir(directory)
        
        # Filter for directories that begin with 'flame_'
        flame_dirs = [entry for entry in entries if entry.startswith('flame_') and os.path.isdir(os.path.join(directory, entry))]
        
        # Sort the list alphanumerically using custom sorting logic
        flame_dirs = sorted(flame_dirs, key=version_key)
        
        # Print the sorted list
        print("Sorted flame_ directories:")
        for dir_name in flame_dirs:
            print(dir_name)
    
    except Exception as e:
        print(f"An error occurred: {e}")

def version_key(directory_name):
    """
    Extracts the version information from a directory name and converts it into a tuple
    that can be used for sorting. Handles prerelease versions by considering them lower value
    than release versions.
    """
    pattern = r'flame_(\d+)(?:\.(\d+))?(?:\.(\d+))?(?:\.(pr\d+))?'
    match = re.match(pattern, directory_name)
    
    if not match:
        return (0, 0, 0, '')  # Return a default tuple for non-matching names
    
    major = int(match.group(1)) if match.group(1) else 0
    minor = int(match.group(2)) if match.group(2) else 0
    patch = int(match.group(3)) if match.group(3) else 0
    prerelease = match.group(4) or ''
    
    # Prerelease versions are considered lower value than release versions
    if prerelease:
        return (major, minor, patch, prerelease)
    else:
        return (major, minor, patch, 'release')

if __name__ == "__main__":
    directory_path = "/opt/Autodesk"
    list_flame_family_software(directory_path)
