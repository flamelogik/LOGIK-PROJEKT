# import os
# import re

# def list_flame_family_software(directory):
#     try:
#         # List all entries in the directory
#         entries = os.listdir(directory)
        
#         # Filter for directories that begin with 'flame_'
#         flame_dirs = [entry for entry in entries if entry.startswith('flame_') and os.path.isdir(os.path.join(directory, entry))]
        
#         # Sort the list alphanumerically using custom sorting logic
#         flame_dirs = sorted(flame_dirs, key=flame_version_key)
        
#         return flame_dirs
    
#     except Exception as e:
#         print(f"An error occurred: {e}")
#         return []

# def flame_version_key(directory_name):
#     """
#     Extracts the version information from a directory name and converts it into a tuple
#     that can be used for sorting. Handles prerelease versions by considering them lower value
#     than release versions.
#     """
#     pattern = r'(\w+)_flame_(\d+)(?:\.(\d+))?(?:\.(\d+))?(?:\.(pr\d+))?'
#     match = re.match(pattern, directory_name)
    
#     if not match:
#         return ('', 0, 0, 0, 0, 0)  # Return a default tuple for non-matching names
    
#     app_name = match.group(1) if match.group(1) else ''
#     major_version = int(match.group(2)) if match.group(2) else 0
#     minor_version = int(match.group(3)) if match.group(3) else 0
#     patch_version = int(match.group(4)) if match.group(4) else 0
#     pr_version = match.group(5) or ''
    
#     pr_major_version = int(pr_version.split('pr')[1]) if pr_version else 0
#     pr_patch_version = int(pr_version.split('.')[1]) if '.' in pr_version else 0
    
#     return (app_name, major_version, minor_version, patch_version, pr_major_version, pr_patch_version)

# def latest_flame_version(directory):
#     flame_dirs = list_flame_family_software(directory)
#     if flame_dirs:
#         return flame_dirs[-1]
#     else:
#         return None

# def sanitize_latest_flame_version_name(version):
#     # Remove 'pr' suffix if it exists
#     version = version.replace('pr', '')
    
#     # Remove 'pr' string if it exists
#     version = version.replace('_pr', '')

#     # Remove any values for pr_version, pr_major_version, or pr_patch_version
#     version_parts = version.split('_')
#     if len(version_parts) > 3:
#         version_parts = version_parts[:3]
#     version = '_'.join(version_parts)
    
#     # Replace periods with underscores
#     version = version.replace('.', '_')
    
#     return version

# import os
# import re

# def list_flame_family_software(directory):
#     try:
#         # List all entries in the directory
#         entries = os.listdir(directory)
        
#         # Filter for directories that begin with 'flame_'
#         flame_dirs = [entry for entry in entries if entry.startswith('flame_') and os.path.isdir(os.path.join(directory, entry))]
        
#         # Sort the list alphanumerically using custom sorting logic
#         flame_dirs = sorted(flame_dirs, key=flame_version_key, reverse=True)
        
#         return flame_dirs
    
#     except Exception as e:
#         print(f"An error occurred: {e}")
#         return []

# def flame_version_key(directory_name):
#     """
#     Extracts the version information from a directory name and converts it into a tuple
#     that can be used for sorting. Handles prerelease versions by considering them lower value
#     than release versions.
#     """
#     pattern = r'flame_(\d+)(?:\.(\d+))?(?:\.(\d+))?(?:\.pr(\d+))?'
#     match = re.match(pattern, directory_name)
    
#     if not match:
#         return ('', 0, 0, 0)  # Return a default tuple for non-matching names
    
#     major_version = int(match.group(1)) if match.group(1) else 0
#     minor_version = int(match.group(2)) if match.group(2) else 0
#     patch_version = int(match.group(3)) if match.group(3) else 0
#     pr_version = int(match.group(4)) if match.group(4) else 0
    
#     return (major_version, minor_version, patch_version, pr_version)

# def latest_flame_version(directory):
#     flame_dirs = list_flame_family_software(directory)
#     if flame_dirs:
#         return flame_dirs[-1]
#     else:
#         return None

# def sanitize_latest_flame_version_name(version):
#     # Remove 'pr' suffix if it exists
#     version = version.replace('pr', '')
    
#     # Replace periods with underscores
#     version = version.replace('.', '_')
    
#     return version




























# import os
# import re

# def list_flame_family_software(directory):
#     try:
#         # List all entries in the directory
#         entries = os.listdir(directory)
        
#         # Filter for directories that begin with 'flame_'
#         flame_dirs = [entry for entry in entries if entry.startswith('flame_') and os.path.isdir(os.path.join(directory, entry))]
        
#         # Sort the list alphanumerically using custom sorting logic
#         flame_dirs = sorted(flame_dirs, key=flame_version_key, reverse=True)
        
#         return flame_dirs
    
#     except Exception as e:
#         print(f"An error occurred: {e}")
#         return []

# def flame_version_key(directory_name):
#     """
#     Extracts the version information from a directory name and converts it into a tuple
#     that can be used for sorting. Handles prerelease versions by considering them lower value
#     than release versions.
#     """
#     pattern = r'flame_(\d+)(?:\.(\d+))?(?:\.(\d+))?(?:\.pr(\d+))?'
#     match = re.match(pattern, directory_name)
    
#     if not match:
#         return (0, 0, 0, 0)  # Return a default tuple for non-matching names
    
#     major_version = int(match.group(1)) if match.group(1) else 0
#     minor_version = int(match.group(2)) if match.group(2) else 0
#     patch_version = int(match.group(3)) if match.group(3) else 0
#     pr_version = int(match.group(4)) if match.group(4) else 0
    
#     return (major_version, minor_version, patch_version, pr_version)

# def latest_flame_version(directory):
#     flame_dirs = list_flame_family_software(directory)
#     if flame_dirs:
#         return flame_dirs[0]  # The first element in the reversed sorted list
#     else:
#         return None

# # def sanitize_latest_flame_version_name(version):
# #     # Remove 'pr' suffix if it exists
# #     version = version.replace('pr', '')
    
# #     # Remove 'pr' string if it exists
# #     version = version.replace('_pr', '')

# #     # Remove any values for pr_version, pr_major_version, or pr_patch_version
# #     version_parts = version.split('_')
# #     if len(version_parts) > 3:
# #         version_parts = version_parts[:3]
# #     version = '_'.join(version_parts)
    
# #     # Replace periods with underscores
# #     version = version.replace('.', '_')

# def sanitize_latest_flame_version_name(version):
#     # Remove the 'pr' suffix and everything after it
#     version = re.sub(r'\.pr\d+', '', version)
    
#     # Replace periods with underscores
#     version = version.replace('.', '_')
    
#     return version






























import os
import re

def list_flame_family_software(directory):
    try:
        # List all entries in the directory
        entries = os.listdir(directory)
        
        # Filter for directories that begin with 'flame_'
        flame_dirs = [entry for entry in entries if entry.startswith('flame_') and os.path.isdir(os.path.join(directory, entry))]
        
        # Sort the list alphanumerically using custom sorting logic
        flame_dirs = sorted(flame_dirs, key=flame_version_key, reverse=True)
        
        return flame_dirs
    
    except Exception as e:
        print(f"An error occurred: {e}")
        return []

def flame_version_key(directory_name):
    """
    Extracts the version information from a directory name and converts it into a tuple
    that can be used for sorting. Handles prerelease versions by considering them lower value
    than release versions.
    """
    pattern = r'flame_(\d+)(?:\.(\d+))?(?:\.(\d+))?(?:\.pr(\d+)(?:\.(\d+))?)?'
    match = re.match(pattern, directory_name)
    
    if not match:
        return (0, 0, 0, 0, 0)  # Return a default tuple for non-matching names
    
    major_version = int(match.group(1)) if match.group(1) else 0
    minor_version = int(match.group(2)) if match.group(2) else 0
    patch_version = int(match.group(3)) if match.group(3) else 0
    pr_version = int(match.group(4)) if match.group(4) else 0
    sub_pr_version = int(match.group(5)) if match.group(5) else 0
    
    return (major_version, minor_version, patch_version, pr_version, sub_pr_version)

def latest_flame_version(directory):
    flame_dirs = list_flame_family_software(directory)
    if flame_dirs:
        return flame_dirs[0]  # The first element in the reversed sorted list
    else:
        return None

def sanitize_latest_flame_version_name(version):
    # Remove the 'pr' suffix and everything after it
    version = re.sub(r'\.pr\d+(\.\d+)?', '', version)
    
    # Replace periods with underscores
    version = version.replace('.', '_')
    
    return version

# Example usage
if __name__ == "__main__":
    directory = '/opt/Autodesk'
    
    flame_dirs = list_flame_family_software(directory)
    print("Sorted flame_ directories:")
    for flame_dir in flame_dirs:
        print(flame_dir)
    
    latest_version = latest_flame_version(directory)
    print("\nThe latest flame version is:")
    print(latest_version)
    
    sanitized_version = sanitize_latest_flame_version_name(latest_version)
    print("\nThe sanitized latest flame version is:")
    print(sanitized_version)
