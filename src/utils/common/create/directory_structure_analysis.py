#!/usr/bin/env python3
# -------------------------------------------------------------------------- #
# Filename:     directory_structure_analysis.py
# Purpose:      Analyzes directory structure and outputs data to a temporary file.
# Description:  This script recursively traverses a given root directory,
#               identifies subdirectories, and records their relative paths,
#               parent relationships, and whether they contain children.

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
Directory structure analysis module.
Analyzes directory structure and outputs data to a temporary file.
"""

import os
import re
import sys
import logging
from pathlib import Path
from typing import Dict, List, Set, Tuple


def directory_structure_analysis(root_dir: str, tmp_file: str) -> None:
    """
    Analyze directory structure and output data to a temporary file.

    Args:
        root_dir: The root directory to analyze
        tmp_file: Temporary file to write analysis results

    Raises:
        OSError: If directory access fails
        IOError: If file writing fails
    """
    if not os.path.isdir(root_dir):
        raise OSError(f"Root directory does not exist: {root_dir}")
  
    logging.info(f"Analyzing directory structure: {root_dir}")
  
    subdirs: List[str] = []
    has_children: Set[str] = set()
    parents: Dict[str, str] = {}
  
    try:
        for dirpath, dirnames, filenames in os.walk(root_dir):
            # Skip the root directory itself
            if dirpath == root_dir:
                continue

            rel_path = os.path.relpath(dirpath, root_dir)
          
            # Skip hidden directories and their subdirectories
            if any(part.startswith('.') for part in Path(rel_path).parts):
                dirnames.clear()  # Don't recurse into subdirectories
                continue
          
            # Skip common build/cache directories
            skip_dirs = {'.git', '__pycache__', '.pytest_cache', 'node_modules',
                        '.vscode', '.idea', 'build', 'dist', '.tox'}
            if os.path.basename(dirpath) in skip_dirs:
                dirnames.clear()
                continue
          
            subdirs.append(rel_path)
            parent_path = os.path.dirname(rel_path)
            depth = rel_path.count(os.sep)

            # Determine parent name
            if depth == 0:
                parents[rel_path] = "projekt directories"
            elif parent_path and parent_path != ".":
                parents[rel_path] = os.path.basename(parent_path)
            else:
                parents[rel_path] = ""
          
            # Mark parent as having children if it exists
            if parent_path and parent_path != ".":
                has_children.add(parent_path)

    except OSError as e:
        logging.error(f"Error walking directory {root_dir}: {e}")
        raise

    # Natural sort - handles numbers in directory names properly
    def natural_sort_key(text: str) -> List:
        """Generate sort key for natural sorting (handles numbers correctly)."""
        return [int(c) if c.isdigit() else c.lower()
                for c in re.split(r'(\d+)', text)]
  
    subdirs.sort(key=natural_sort_key)
  
    logging.info(f"Found {len(subdirs)} subdirectories")
  
    # Write results to temporary file
    try:
        with open(tmp_file, 'w', encoding='utf-8') as f:
            f.write(f"{os.path.basename(root_dir)}\n")
            f.write(f"{len(subdirs)}\n")

            for subdir in subdirs:
                has_children_flag = "true" if subdir in has_children else "false"
                parent = parents.get(subdir, "")
                f.write(f"{subdir}|{has_children_flag}|{parent}\n")
              
    except IOError as e:
        logging.error(f"Error writing to temporary file {tmp_file}: {e}")
        raise
  
    logging.info(f"Analysis complete. Results written to {tmp_file}")


def get_directory_stats(root_dir: str) -> Dict[str, int]:
    """
    Get basic statistics about the directory structure.
  
    Args:
        root_dir: The root directory to analyze
      
    Returns:
        Dictionary with statistics (total_dirs, max_depth, etc.)
    """
    if not os.path.isdir(root_dir):
        return {}
  
    stats = {
        'total_dirs': 0,
        'max_depth': 0,
        'total_files': 0,
        'hidden_dirs': 0
    }
  
    for dirpath, dirnames, filenames in os.walk(root_dir):
        if dirpath == root_dir:
            continue
          
        rel_path = os.path.relpath(dirpath, root_dir)
        depth = rel_path.count(os.sep) + 1
      
        stats['total_dirs'] += 1
        stats['max_depth'] = max(stats['max_depth'], depth)
        stats['total_files'] += len(filenames)
      
        if os.path.basename(dirpath).startswith('.'):
            stats['hidden_dirs'] += 1
  
    return stats


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, format='%(levelname)s: %(message)s')
  
    if len(sys.argv) != 3:
        print("Usage: python directory_structure_analysis.py <root_dir> <output_file>")
        sys.exit(1)

    root_dir = sys.argv[1]
    tmp_file = sys.argv[2]

    try:
        directory_structure_analysis(root_dir, tmp_file)
      
        # Print statistics
        stats = get_directory_stats(root_dir)
        if stats:
            logging.info(f"Statistics: {stats}")
          
    except (OSError, IOError) as e:
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
