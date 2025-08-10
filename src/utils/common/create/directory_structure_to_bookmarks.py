#!/usr/bin/env python3
# -------------------------------------------------------------------------- #
# Filename:     directory_structure_to_bookmarks.py
# Purpose:      Converts directory structure data to Autodesk Flame bookmarks JSON format.
# Description:  This script processes a data file representing a directory
#               structure and generates a JSON file compatible with Autodesk
#               Flame's bookmark system, including hierarchical folders and links.

# Author:       phil_man@mac.com
# Copyright:    Copyright (c) 2025
# Disclaimer:   Disclaimer at bottom of script.
# License:      GNU General Public License v3.0 (GPL-3.0).
#               https://www.gnu.org/licenses/gpl-3.0.en.html

# Version:      2026.1.0
# Status:       Production
# Type:         Utility
# Created:      2025-07-01
# Modified:     2025-08-03

# Changelog:    Changelog at bottom of script.
# -------------------------------------------------------------------------- #

"""
Directory structure to bookmarks converter.
Converts directory structure data to Autodesk Flame bookmarks JSON format.
"""

import json
import os
import sys
import logging
from pathlib import Path
from typing import Dict, List, Any, Optional


class FlameBookmarksGenerator:
    """Generator for Autodesk Flame bookmarks JSON structure."""
  
    DEFAULT_PROJECT_NICKNAME = "<project nickname>"
    BOOKMARK_VERSION = 1
  
    def __init__(self, project_nickname: Optional[str] = None):
        """
        Initialize the bookmarks generator.
      
        Args:
            project_nickname: Custom project nickname, uses default token if None
        """
        self.project_nickname = project_nickname or self.DEFAULT_PROJECT_NICKNAME
        if not project_nickname:
            logging.warning(f"No project nickname provided, using token: {self.DEFAULT_PROJECT_NICKNAME}")
  
    def parse_data_file(self, data_file: str) -> Dict[str, Any]:
        """
        Parse the directory structure data file.
      
        Args:
            data_file: Path to the data file
          
        Returns:
            Dictionary containing parsed structure data
          
        Raises:
            IOError: If file cannot be read
            ValueError: If file format is invalid
        """
        if not os.path.exists(data_file):
            raise IOError(f"Data file does not exist: {data_file}")
      
        try:
            with open(data_file, "r", encoding='utf-8') as f:
                lines = f.readlines()
        except IOError as e:
            logging.error(f"Error reading data file: {e}")
            raise

        if len(lines) < 2:
            raise ValueError("Invalid data file format: insufficient lines")

        try:
            root_dir_name = lines[0].strip()
            subdir_count = int(lines[1].strip())
        except (IndexError, ValueError) as e:
            raise ValueError(f"Invalid data file format: {e}")

        structure = {}
        processed_count = 0

        for i in range(2, min(subdir_count + 2, len(lines))):
            line = lines[i].strip()
            if not line:
                continue
              
            parts = line.split("|")
            if len(parts) < 3:
                logging.warning(f"Skipping malformed line {i}: {line}")
                continue

            subdir = parts[0]
            has_children_flag = parts[1]
            parent_name = parts[2] if len(parts) > 2 else ""

            has_children = has_children_flag.lower() == "true"
            dir_name = os.path.basename(subdir)

            # Remove leading ./ if present
            if subdir.startswith('./'):
                subdir = subdir[2:]

            # Generate bookmark path
            if subdir == root_dir_name:
                path = f"/PROJEKTS/{self.project_nickname}/"
            else:
                path = f"/PROJEKTS/{self.project_nickname}/{subdir}"

            # Normalize path separators
            path = path.replace("\\", "/")

            structure[subdir] = {
                "type": "folder" if has_children else "bookmark",
                "path": path,
                "parent": parent_name,
                "name": dir_name,
                "has_children": has_children
            }
            processed_count += 1

        logging.info(f"Parsed {processed_count} directory entries from data file")
        return {
            "root_dir_name": root_dir_name,
            "structure": structure,
            "processed_count": processed_count,
            "expected_count": subdir_count
        }

    def build_bookmarks_structure(self, key: str, structure: Dict[str, Dict], root_dir_name: str) -> List[Dict[str, Any]]:
        """
        Recursively build the bookmarks structure.
      
        Args:
            key: Current directory key
            structure: Full directory structure
            root_dir_name: Name of the root directory
          
        Returns:
            List of bookmark/folder dictionaries
        """
        result = []
      
        for child_key, child_info in structure.items():
            type_ = child_info["type"]
            path = child_info["path"]
            child_parent = child_info["parent"]
            dir_name = child_info["name"]

            # Determine expected parent name
            if key == root_dir_name:
                expected_parent = "projekt directories"
            else:
                expected_parent = os.path.basename(key)

            # Check if this child belongs to the current parent
            is_child = (
                (key == root_dir_name and child_parent == "projekt directories") or
                (key != root_dir_name and child_parent == expected_parent)
            )

            if is_child:
                if type_ == "folder":
                    folder_entry = {
                        "Folder": dir_name,
                        "Bookmarks": self.build_bookmarks_structure(child_key, structure, root_dir_name),
                    }
                    result.append(folder_entry)
                else:
                    bookmark_entry = {
                        "Bookmark": dir_name,
                        "Path": path,
                        "Visibility": "Global",
                    }
                    result.append(bookmark_entry)
      
        return result

    def generate_flame_bookmarks(self, parsed_data: Dict[str, Any]) -> Dict[str, Any]:
        """
        Generate the complete Flame bookmarks JSON structure.
      
        Args:
            parsed_data: Parsed directory structure data
          
        Returns:
            Complete bookmarks JSON structure
        """
        root_dir_name = parsed_data["root_dir_name"]
        structure = parsed_data["structure"]
      
        # Build the main bookmarks structure
        projekt_bookmarks = self.build_bookmarks_structure(root_dir_name, structure, root_dir_name)
      
        # Create the complete JSON structure
        json_data = {
            "DlBookmark": {
                "Version": self.BOOKMARK_VERSION,
                "Sections": [
                    {
                        "Section": "Project",
                        "Bookmarks": [
                            {
                                "Bookmark": "flame setups",
                                "Path": "<project home>",
                                "Visibility": "Global"
                            },
                            {
                                "Bookmark": "PROJEKTS",
                                "Path": "/PROJEKTS/",
                                "Visibility": "Global"
                            },
                            {
                                "Bookmark": "projekt home",
                                "Path": f"/PROJEKTS/{self.project_nickname}/",
                                "Visibility": "Global"
                            },
                            {
                                "Folder": "projekt directories",
                                "Bookmarks": projekt_bookmarks,
                            }
                        ],
                    }
                ],
            }
        }
      
        return json_data

    def write_bookmarks_file(self, json_data: Dict[str, Any], output_file: str) -> None:
        """
        Write the bookmarks JSON to file.
      
        Args:
            json_data: Complete bookmarks structure
            output_file: Output file path
          
        Raises:
            IOError: If file cannot be written
        """
        # Ensure output directory exists
        output_path = Path(output_file)
        output_path.parent.mkdir(parents=True, exist_ok=True)

        try:
            with open(output_file, "w", encoding='utf-8') as f:
                json.dump(json_data, f, indent=4, ensure_ascii=False)
        except IOError as e:
            logging.error(f"Error writing bookmarks file: {e}")
            raise

        logging.info(f"Successfully created Flame bookmarks file: {output_file}")


def directory_structure_to_bookmarks(
    data_file: str,
    output_file: str,
    original_path: Optional[str] = None,
    project_nickname: Optional[str] = None
) -> None:
    """
    Convert directory structure data to a Flame bookmarks JSON file.

    Args:
        data_file: Input file with directory structure data
        output_file: Output JSON file path
        original_path: Original path of the directory (optional, for compatibility)
        project_nickname: Nickname for the project (optional)

    Raises:
        IOError: If file operations fail
        ValueError: If data format is invalid
    """
    logging.info(f"Converting directory structure to bookmarks: {data_file} -> {output_file}")
  
    # Create generator instance
    generator = FlameBookmarksGenerator(project_nickname)
  
    # Parse the data file
    parsed_data = generator.parse_data_file(data_file)
  
    # Generate bookmarks structure
    json_data = generator.generate_flame_bookmarks(parsed_data)
  
    # Write to file
    generator.write_bookmarks_file(json_data, output_file)
  
    # Log summary
    expected = parsed_data["expected_count"]
    processed = parsed_data["processed_count"]
    if processed != expected:
        logging.warning(f"Expected {expected} directories, processed {processed}")


def validate_bookmarks_file(bookmarks_file: str) -> bool:
    """
    Validate the generated bookmarks JSON file.
  
    Args:
        bookmarks_file: Path to the bookmarks file
      
    Returns:
        True if valid, False otherwise
    """
    try:
        with open(bookmarks_file, 'r', encoding='utf-8') as f:
            data = json.load(f)
      
        # Check top-level structure
        if "DlBookmark" not in data:
            logging.error("Missing DlBookmark root element")
            return False
      
        dl_bookmark = data["DlBookmark"]
      
        # Check required fields
        if "Version" not in dl_bookmark or "Sections" not in dl_bookmark:
            logging.error("Missing required DlBookmark fields")
            return False
      
        # Check sections structure
        sections = dl_bookmark["Sections"]
        if not isinstance(sections, list) or len(sections) == 0:
            logging.error("Invalid or empty Sections array")
            return False
      
        # Check first section
        section = sections[0]
        if "Section" not in section or "Bookmarks" not in section:
            logging.error("Invalid section structure")
            return False
      
        logging.info("Bookmarks file validation passed")
        return True
      
    except (json.JSONDecodeError, IOError) as e:
        logging.error(f"Bookmarks validation failed: {e}")
        return False


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, format='%(levelname)s: %(message)s')
  
    if len(sys.argv) < 3:
        print("Usage: python directory_structure_to_bookmarks.py <data_file> <output_file> [original_path] [project_nickname]")
        sys.exit(1)

    data_file = sys.argv[1]
    output_file = sys.argv[2]
    original_path = sys.argv[3] if len(sys.argv) > 3 else None
    project_nickname = sys.argv[4] if len(sys.argv) > 4 else None

    try:
        directory_structure_to_bookmarks(data_file, output_file, original_path, project_nickname)
      
        # Validate output
        if not validate_bookmarks_file(output_file):
            sys.exit(1)
          
    except (IOError, ValueError) as e:
        logging.error(f"Error: {e}")
        sys.exit(1)


# -------------------------------------------------------------------------- #

# DISCLAIMER:   This file is part of LOGIK-PROJEKT.

#               Copyright © 2025 STRENGTH IN NUMBERS

#               LOGIK-PROJEKT creates directories, files, scripts & tools
#               for use with Autodesk Flame and other software.

#               LOGIK-PROJEKT is free software.

#               You can redistribute it and/or modify it under the terms
#               of the GNU General Public License as published by the
#               Free Software Foundation, either version 3 of the License,
#               or any later version.

#               This program is distributed in the hope that it will be
#               useful, but WITHOUT ANY WARRANTY; without even the
#               implied warranty of MERCHANTABILITY or
#               FITNESS FOR A PARTICULAR PURPOSE.

#               See the GNU General Public License for more details.
#               You should have received a copy of the GNU General
#               Public License along with this program.

#               If not, see <https://www.gnu.org/licenses/gpl-3.0.en.html>.

#               Contact: phil_man@mac.com

# -------------------------------------------------------------------------- #
# C2 A9 32 30 32 35 53 54 52 45 4E 47 54 48 2D 49 4E 2D 4E 55 4D 42 45 52 53 #
# -------------------------------------------------------------------------- #
# Changelog:
# -------------------------------------------------------------------------- #
