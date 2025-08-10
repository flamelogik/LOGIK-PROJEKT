#!/usr/bin/env python3
# -------------------------------------------------------------------------- #
# Filename:     directory_structure_to_json.py
# Purpose:      Converts directory structure data to a structured JSON file.
# Description:  This script processes a data file representing a directory
#               structure and generates a JSON file containing detailed
#               information about each subdirectory, including its path, name,
#               depth, and parent.

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
Directory structure to JSON converter.
Converts directory structure data to a structured JSON file.
"""

import json
import os
import sys
import logging
from datetime import datetime
from pathlib import Path
from typing import Dict, List, Any, Optional


def directory_structure_to_json(
    data_file: str,
    output_file: str,
    original_path: Optional[str] = None
) -> None:
    """
    Convert directory structure data to a JSON file.

    Args:
        data_file: Input file with directory structure data
        output_file: Output JSON file path
        original_path: Original path of the directory (optional)

    Raises:
        IOError: If file operations fail
        ValueError: If data format is invalid
    """
    if not os.path.exists(data_file):
        raise IOError(f"Data file does not exist: {data_file}")
  
    logging.info(f"Converting directory structure to JSON: {data_file} -> {output_file}")
  
    try:
        with open(data_file, 'r', encoding='utf-8') as f:
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

    # Extract metadata from original path
    original_name = ""
    original_depth = 0
    if original_path:
        original_name = os.path.basename(original_path)
        original_depth = str(original_path).count(os.sep)

    timestamp = datetime.now()
  
    # Build JSON structure
    json_data = {
        "metadata": {
            "created_at": timestamp.isoformat(),
            "created_by": "directory_structure_to_json",
            "version": "1.0"
        },
        "source": {
            "original_path": original_path or "",
            "original_name": original_name,
            "original_depth": original_depth,
            "root_directory": root_dir_name
        },
        "analysis": {
            "timestamp": timestamp.strftime("%Y_%m_%d-%H_%M_%S"),
            "total_subdirectories": subdir_count
        },
        "subdirectories": []
    }

    # Process subdirectories
    processed_count = 0
    for i in range(2, min(subdir_count + 2, len(lines))):
        line = lines[i].strip()
        if not line:
            continue
          
        parts = line.split('|')
        if len(parts) < 3:
            logging.warning(f"Skipping malformed line {i}: {line}")
            continue

        subdir = parts[0]
        has_children_flag = parts[1]
        parent_name = parts[2] if len(parts) > 2 else ""

        # Calculate depth and extract directory name
        depth = subdir.count('/') + subdir.count('\\') + 1
        dir_name = os.path.basename(subdir)
        has_children = has_children_flag.lower() == "true"

        # Normalize path separators
        normalized_path = subdir.replace('\\', '/')

        subdir_entry = {
            "path": normalized_path,
            "name": dir_name,
            "depth": depth,
            "hasChildren": has_children,
            "parent": parent_name,
            "type": "directory"
        }

        json_data["subdirectories"].append(subdir_entry)
        processed_count += 1

    # Update actual count
    json_data["analysis"]["processed_subdirectories"] = processed_count
  
    if processed_count != subdir_count:
        logging.warning(f"Expected {subdir_count} subdirectories, processed {processed_count}")

    # Ensure output directory exists
    output_path = Path(output_file)
    output_path.parent.mkdir(parents=True, exist_ok=True)

    # Write JSON file
    try:
        with open(output_file, 'w', encoding='utf-8') as f:
            json.dump(json_data, f, indent=2, ensure_ascii=False, sort_keys=False)
    except IOError as e:
        logging.error(f"Error writing JSON file: {e}")
        raise

    logging.info(f"Successfully created JSON file with {processed_count} subdirectories")


def validate_json_output(json_file: str) -> bool:
    """
    Validate the generated JSON file.
  
    Args:
        json_file: Path to the JSON file to validate
      
    Returns:
        True if valid, False otherwise
    """
    try:
        with open(json_file, 'r', encoding='utf-8') as f:
            data = json.load(f)
      
        # Check required fields
        required_fields = ["metadata", "source", "analysis", "subdirectories"]
        for field in required_fields:
            if field not in data:
                logging.error(f"Missing required field: {field}")
                return False
      
        # Validate subdirectories structure
        for i, subdir in enumerate(data["subdirectories"]):
            required_subdir_fields = ["path", "name", "depth", "hasChildren", "parent"]
            for field in required_subdir_fields:
                if field not in subdir:
                    logging.error(f"Missing field '{field}' in subdirectory {i}")
                    return False
      
        logging.info("JSON file validation passed")
        return True
      
    except (json.JSONDecodeError, IOError) as e:
        logging.error(f"JSON validation failed: {e}")
        return False


def get_directory_tree_summary(json_file: str) -> Dict[str, Any]:
    """
    Generate a summary of the directory tree from JSON file.
  
    Args:
        json_file: Path to the JSON file
      
    Returns:
        Dictionary with tree summary
    """
    try:
        with open(json_file, 'r', encoding='utf-8') as f:
            data = json.load(f)
    except (json.JSONDecodeError, IOError) as e:
        logging.error(f"Error reading JSON file: {e}")
        return {}
  
    subdirs = data.get("subdirectories", [])
  
    summary = {
        "total_directories": len(subdirs),
        "max_depth": max((d.get("depth", 0) for d in subdirs), default=0),
        "directories_with_children": sum(1 for d in subdirs if d.get("hasChildren", False)),
        "leaf_directories": sum(1 for d in subdirs if not d.get("hasChildren", False)),
        "depth_distribution": {}
    }
  
    # Calculate depth distribution
    for subdir in subdirs:
        depth = subdir.get("depth", 0)
        summary["depth_distribution"][depth] = summary["depth_distribution"].get(depth, 0) + 1
  
    return summary


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, format='%(levelname)s: %(message)s')
  
    if len(sys.argv) < 3:
        print("Usage: python directory_structure_to_json.py <data_file> <output_file> [original_path]")
        sys.exit(1)

    data_file = sys.argv[1]
    output_file = sys.argv[2]
    original_path = sys.argv[3] if len(sys.argv) > 3 else None

    try:
        directory_structure_to_json(data_file, output_file, original_path)
      
        # Validate output
        if validate_json_output(output_file):
            # Print summary
            summary = get_directory_tree_summary(output_file)
            if summary:
                logging.info(f"Directory tree summary: {summary}")
        else:
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
