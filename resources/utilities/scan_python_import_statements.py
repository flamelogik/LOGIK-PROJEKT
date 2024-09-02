# resources/utilities/scan_python_import_statements.py

import os
import ast
import importlib.util

def is_standard_library(module_name):
    try:
        spec = importlib.util.find_spec(module_name)
        return spec is not None and 'site-packages' not in spec.origin
    except ImportError:
        return False

def get_imports(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        try:
            tree = ast.parse(file.read())
        except SyntaxError:
            print(f"Syntax error in file: {file_path}")
            return set()

    imports = set()
    for node in ast.walk(tree):
        if isinstance(node, ast.Import):
            for alias in node.names:
                imports.add(alias.name.split('.')[0])
        elif isinstance(node, ast.ImportFrom):
            if node.level == 0:  # absolute import
                imports.add(node.module.split('.')[0])

    return imports

def scan_directory(directory):
    all_imports = set()
    for root, _, files in os.walk(directory):
        for file in files:
            if file.endswith('.py'):
                file_path = os.path.join(root, file)
                all_imports.update(get_imports(file_path))
    return all_imports

def main():
    # directory = input("Enter the directory path to scan: ")
    directory = "/home/pman/workspace/GitHub/projekt_app/modules"

    # output_file = input("Enter the output file name: ")
    output_file = "/home/pman/workspace/GitHub/projekt_app/resources/tmp/scanned_imports"

    if not os.path.isdir(directory):
        print("Invalid directory path.")
        return

    all_imports = scan_directory(directory)

    standard_libs = set(filter(is_standard_library, all_imports))
    third_party = all_imports - standard_libs

    with open(output_file, 'w') as f:
        f.write("Standard library imports:\n")
        for lib in sorted(standard_libs):
            f.write(f"- {lib}\n")
        
        f.write("\nThird-party imports:\n")
        for lib in sorted(third_party):
            f.write(f"- {lib}\n")

    print(f"Import list has been written to {output_file}")

if __name__ == "__main__":
    main()