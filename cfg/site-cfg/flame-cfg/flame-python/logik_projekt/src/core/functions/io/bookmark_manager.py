################################################################################
# Filename: bookmark_manager.py
# Relative Path: src/core/functions/io/bookmark_manager.py
#
# Purpose: Parse and manage bookmarks from cf_bookmarks.json, handling
#          placeholder substitution and filtering by sync root.
#
# Author: phil_man@mac.com
# Copyright: Copyright (c) 2026
#
################################################################################

from __future__ import annotations

import json
import logging
from pathlib import Path
from typing import Dict, Any, Optional, List


def read_json_file(path: Path) -> Optional[Dict[str, Any]]:
    """Read and parse a JSON file safely.
    
    Returns None if file not found or parse fails.
    """
    try:
        with path.open('r', encoding='utf-8') as fh:
            return json.load(fh)
    except FileNotFoundError:
        return None
    except Exception as e:
        logging.warning(f"Failed to read JSON {path}: {e}")
        return None


def _extract_paths_from_cf_structure(obj: Any, collected: List[str]) -> None:
    """Recursively walk cf_bookmarks structure and collect all Path values."""
    if isinstance(obj, dict):
        for k, v in obj.items():
            if k == 'Path' and isinstance(v, str):
                collected.append(v)
            else:
                _extract_paths_from_cf_structure(v, collected)
    elif isinstance(obj, list):
        for item in obj:
            _extract_paths_from_cf_structure(item, collected)


def parse_cf_bookmarks(cf_path: Path, 
                       project_nickname: Optional[str] = None,
                       setups_path: Optional[Path] = None) -> List[Dict[str, str]]:
    """Parse cf_bookmarks.json and return normalized bookmark dictionaries.
    
    Substitutes placeholders:
      - <project setups> → setups_path
      - <project nickname> → searches /PROJEKTS/*/... pattern
    
    For each path, derives flame_folder as the relative path from /PROJEKTS/<nickname>/
    (or the last two path segments as fallback).
    
    Args:
        cf_path: Path to cf_bookmarks.json
        project_nickname: Project nickname for placeholder substitution
        setups_path: Project setups path for <project setups> substitution
    
    Returns:
        List of dicts with 'filesystem_path' and 'flame_folder' keys
    """
    data = read_json_file(cf_path)
    if not data:
        return []

    collected_paths: List[str] = []
    _extract_paths_from_cf_structure(data, collected_paths)

    bookmarks: List[Dict[str, str]] = []
    for p in collected_paths:
        fs_path = p

        # Substitute <project setups> placeholder
        if '<project setups>' in fs_path and setups_path:
            fs_path = fs_path.replace('<project setups>', str(setups_path))

        # Handle <project nickname> placeholder
        if '<project nickname>' in fs_path:
            prefix, _, suffix = fs_path.partition('<project nickname>')
            suffix = suffix.lstrip('/')
            candidate = None
            projekts_root = Path('/PROJEKTS')
            try:
                for p in projekts_root.glob(f"*/{suffix}"):
                    if p.exists():
                        candidate = p
                        break
            except Exception as e:
                logging.warning(f"Error globbing for project nickname: {e}")

            if candidate:
                fs_path = str(candidate)
                logging.info(f"Resolved '<project nickname>' to {fs_path}")
            else:
                logging.info(f"Could not resolve '<project nickname>' for {fs_path}; skipping")
                continue

        # Skip unresolved placeholders
        if '<' in fs_path or '>' in fs_path:
            logging.info(f"Skipping unresolved placeholder: {fs_path}")
            continue

        # Skip setups references (not media folders)
        if '/setups' in fs_path:
            logging.info(f"Skipping setups reference: {fs_path}")
            continue

        # Must be absolute path
        if not fs_path.startswith('/'):
            logging.info(f"Skipping non-absolute path: {fs_path}")
            continue

        # Derive flame_folder from filesystem path
        flame_folder = None
        try:
            parts = Path(fs_path).parts
            # Look for PROJEKTS marker and extract path after project nickname
            if 'PROJEKTS' in parts:
                i = parts.index('PROJEKTS')
                if len(parts) > i + 2:
                    flame_folder = '/'.join(parts[i + 2:])
                else:
                    logging.info(f"Path missing project subpath: {fs_path}")
                    continue
            else:
                # Fallback: use last two segments
                if len(parts) >= 2:
                    flame_folder = '/'.join(parts[-2:])
        except Exception as e:
            logging.warning(f"Failed to parse path {fs_path}: {e}")
            continue

        # Sanity check
        if not flame_folder or '<' in flame_folder or '>' in flame_folder:
            logging.info(f"Skipping invalid derived flame_folder: {fs_path}")
            continue

        bookmarks.append({
            'filesystem_path': fs_path,
            'flame_folder': flame_folder
        })
        logging.info(f"Parsed bookmark: fs={fs_path} flame={flame_folder}")

    logging.info(f"Parsed {len(bookmarks)} usable bookmarks from {cf_path}")
    return bookmarks


def find_cf_bookmarks(project_path: Path) -> Optional[Path]:
    """Locate cf_bookmarks.json in standard locations.
    
    Checks:
      1. <project_path>/setups/status/cf_bookmarks.json
      2. <project_path>/setups/status/<project_name>/cf_bookmarks.json
    
    Args:
        project_path: Path to Flame project root
    
    Returns:
        Path to cf_bookmarks.json if found, None otherwise
    """
    import sys
    print(f"\n[bookmark_manager] find_cf_bookmarks() called", file=sys.stdout)
    print(f"  project_path: {project_path}", file=sys.stdout)
    sys.stdout.flush()
    
    setups_path = project_path / 'setups'
    print(f"  setups_path: {setups_path}", file=sys.stdout)
    print(f"  setups_path exists: {setups_path.exists()}", file=sys.stdout)
    sys.stdout.flush()
    
    candidate1 = setups_path / 'status' / 'cf_bookmarks.json'
    print(f"  candidate1: {candidate1}", file=sys.stdout)
    print(f"  candidate1 exists: {candidate1.exists()}", file=sys.stdout)
    sys.stdout.flush()
    
    if candidate1.exists():
        logging.info(f"Found cf_bookmarks at {candidate1}")
        print(f"[bookmark_manager] Found cf_bookmarks at {candidate1}", file=sys.stdout)
        sys.stdout.flush()
        return candidate1
    
    project_name = project_path.name
    candidate2 = setups_path / 'status' / project_name / 'cf_bookmarks.json'
    print(f"  candidate2: {candidate2}", file=sys.stdout)
    print(f"  candidate2 exists: {candidate2.exists()}", file=sys.stdout)
    sys.stdout.flush()
    
    if candidate2.exists():
        logging.info(f"Found cf_bookmarks at {candidate2}")
        print(f"[bookmark_manager] Found cf_bookmarks at {candidate2}", file=sys.stdout)
        sys.stdout.flush()
        return candidate2
    
    logging.warning(f"No cf_bookmarks.json found in {project_path}")
    print(f"[bookmark_manager] ERROR: No cf_bookmarks.json found!", file=sys.stdout)
    sys.stdout.flush()
    return None


def load_bookmarks_for_project(project_path: Path, 
                               project_nickname: Optional[str] = None) -> List[Dict[str, str]]:
    """Load and parse bookmarks from a Flame project.
    
    Args:
        project_path: Path to Flame project root
        project_nickname: Optional nickname for placeholder substitution
    
    Returns:
        List of bookmark dicts with filesystem_path and flame_folder
    """
    import sys
    print(f"\n[bookmark_manager] load_bookmarks_for_project() called", file=sys.stdout)
    print(f"  project_path: {project_path}", file=sys.stdout)
    print(f"  project_nickname: {project_nickname}", file=sys.stdout)
    sys.stdout.flush()
    
    setups_path = project_path / 'setups'
    
    cf_path = find_cf_bookmarks(project_path)
    if not cf_path:
        logging.warning("Could not find cf_bookmarks.json")
        print(f"[bookmark_manager] ERROR: Could not find cf_bookmarks.json", file=sys.stdout)
        sys.stdout.flush()
        return []
    
    nickname = project_nickname or project_path.name
    print(f"[bookmark_manager] Parsing cf_bookmarks.json with nickname={nickname}", file=sys.stdout)
    sys.stdout.flush()
    
    bookmarks = parse_cf_bookmarks(cf_path, project_nickname=nickname, setups_path=setups_path)
    print(f"[bookmark_manager] Parsed {len(bookmarks)} bookmarks", file=sys.stdout)
    sys.stdout.flush()
    
    return bookmarks


def filter_bookmarks_by_sync_root(bookmarks: List[Dict[str, str]], 
                                   sync_root: str) -> List[Dict[str, str]]:
    """Filter bookmarks to only those under the specified sync root.
    
    A bookmark matches if its flame_folder:
      - Starts with '<sync_root>/'
      - Equals '<sync_root>'
      - Has '/<sync_root>/' anywhere in the filesystem_path
    
    Args:
        bookmarks: List of bookmark dicts
        sync_root: Root directory name to filter by (e.g., 'assets')
    
    Returns:
        Filtered list of bookmarks
    """
    filtered = []
    for b in bookmarks:
        flame_folder = b.get('flame_folder') or ''
        fs_path = b.get('filesystem_path') or ''
        
        if (flame_folder.startswith(sync_root + '/') or 
            flame_folder == sync_root or 
            ('/' + sync_root + '/') in fs_path):
            filtered.append(b)
    
    return filtered


# End of file
