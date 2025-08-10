# Insight for copy_flame_python_scripts.py

## Purpose

This script is responsible for copying the Flame Python scripts from the repository's `cfg/site-cfg/flame-cfg/flame-python` directory to the Flame project's `setups/python` directory.

## Key Functions

- `copy_flame_python_scripts(flame_projekt_setups_dir: str)`: This is the main function that orchestrates the copying process. It uses `rsync` to perform the file transfer.
- `modify_openclip_python_config_paths(scripts_destination: Path)`: This function modifies the `base_python_path` variable in the copied Python scripts to point to the correct location within the Flame project.

## Process Flow

1. The `copy_flame_python_scripts` function is called with the path to the Flame project's `setups` directory.
2. The function constructs the source and destination paths.
3. It creates the destination directory if it doesn't already exist.
4. It uses `rsync` to copy the Python scripts from the source to the destination.
5. After the copy is complete, the `modify_openclip_python_config_paths` function is called.
6. This function iterates through all the `.py` files in the destination directory.
7. For each file, it reads the content and replaces the hardcoded path with the new, correct path.
8. The modified content is then written back to the file.

## Dependencies

- `os`
- `logging`
- `sys`
- `pathlib`
- `src.core.utils.path_utils.get_repository_root_dir`
- `src.core.functions.get.get_application_paths.GetApplicationPaths`
