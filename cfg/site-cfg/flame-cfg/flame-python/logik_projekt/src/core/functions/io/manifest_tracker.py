################################################################################
# Filename: manifest_tracker.py
# Relative Path: src/core/functions/io/manifest_tracker.py
#
# Purpose: Manage import manifests: load, update, and persist per-folder
#          tracking of which files have been imported.
#
# Author: phil_man@mac.com
# Copyright: Copyright (c) 2026
#
################################################################################

from __future__ import annotations

import json
import logging
import os
import hashlib
import tempfile
from datetime import datetime
from pathlib import Path
from typing import Dict, Any, Optional


MANIFEST_FILE_NAME = ".import_manifest"


def read_json_file(path: Path) -> Optional[Dict[str, Any]]:
    """Read and parse a JSON file safely."""
    try:
        with path.open('r', encoding='utf-8') as fh:
            return json.load(fh)
    except FileNotFoundError:
        return None
    except Exception as e:
        logging.warning(f"Failed to read JSON {path}: {e}")
        return None


def atomic_write_json(path: Path, data: Dict[str, Any]) -> None:
    """Write JSON atomically using temp file and rename.
    
    Ensures data integrity even if process crashes mid-write.
    """
    tmp_suffix = path.suffix + '.tmp' if path.suffix else '.tmp'
    try:
        with tempfile.NamedTemporaryFile('w', 
                                         delete=False, 
                                         dir=str(path.parent), 
                                         encoding='utf-8',
                                         suffix=tmp_suffix) as tf:
            json.dump(data, tf, indent=4)
            tf.flush()
            os.fsync(tf.fileno())
        os.replace(tf.name, str(path))
    except Exception as e:
        logging.error(f"Failed to write manifest {path}: {e}")
        try:
            if os.path.exists(tf.name):
                os.remove(tf.name)
        except Exception:
            pass


def compute_sha256(path: Path, block_size: int = 65536) -> str:
    """Compute SHA256 hash of a file."""
    h = hashlib.sha256()
    with path.open('rb') as fh:
        for block in iter(lambda: fh.read(block_size), b''):
            h.update(block)
    return h.hexdigest()


class ManifestTracker:
    """Manages per-folder import manifests.
    
    Each watched folder gets a .import_manifest file that tracks:
      - Which files have been imported
      - File metadata (size, mtime, hash)
      - Import status and timestamps
    """
    
    def __init__(self, watched_root: Path):
        """Initialize tracker for a watched folder.
        
        Args:
            watched_root: Path to the watched folder
        """
        self.watched_root = Path(watched_root)
        self.manifest_path = self.watched_root / MANIFEST_FILE_NAME
        self.manifest = self._load_or_create_manifest()
    
    def _load_or_create_manifest(self) -> Dict[str, Any]:
        """Load existing manifest or create new one."""
        manifest = read_json_file(self.manifest_path)
        if manifest:
            return manifest
        
        # Create new manifest with default structure
        return {
            "version": 1,
            "watched_root": str(self.watched_root),
            "entries": {}
        }
    
    def save(self) -> None:
        """Persist manifest to disk."""
        atomic_write_json(self.manifest_path, self.manifest)
    
    def has_entry(self, rel_key: str) -> bool:
        """Check if manifest has an entry for a file."""
        entries = self.manifest.setdefault('entries', {})
        return rel_key in entries
    
    def get_entry(self, rel_key: str) -> Optional[Dict[str, Any]]:
        """Get manifest entry for a file."""
        entries = self.manifest.setdefault('entries', {})
        return entries.get(rel_key)
    
    def is_file_imported(self, rel_key: str, 
                        file_path: Path,
                        use_hash: bool = False) -> bool:
        """Check if file has already been imported.
        
        Compares file metadata (size, mtime, or hash) against manifest entry.
        
        Args:
            rel_key: Relative path key in manifest
            file_path: Actual filesystem path to file
            use_hash: If True, compare SHA256 hash; otherwise use size+mtime
        
        Returns:
            True if file was already imported and hasn't changed
        """
        entry = self.get_entry(rel_key)
        if not entry:
            return False
        
        if not entry.get('imported'):
            return False
        
        try:
            stat = file_path.stat()
            size = stat.st_size
            mtime = stat.st_mtime
        except Exception as e:
            logging.warning(f"Cannot stat file {file_path}: {e}")
            return False
        
        # Compare using hash if configured
        if use_hash:
            try:
                sha = compute_sha256(file_path)
                return entry.get('sha256') == sha
            except Exception as e:
                logging.warning(f"Failed to hash {file_path}: {e}")
                return False
        
        # Compare using size and mtime
        return (entry.get('size') == size and 
                entry.get('mtime') == mtime)
    
    def record_import_success(self, rel_key: str,
                             file_path: Path,
                             flame_folder: str,
                             use_hash: bool = False) -> None:
        """Record successful import in manifest.
        
        Args:
            rel_key: Relative path key in manifest
            file_path: Actual filesystem path to file
            flame_folder: Destination Flame folder path
            use_hash: If True, also compute and store SHA256
        """
        entries = self.manifest.setdefault('entries', {})
        entry = entries.setdefault(rel_key, {})
        
        try:
            stat = file_path.stat()
            sha = compute_sha256(file_path) if use_hash else None
            
            entry.update({
                'size': stat.st_size,
                'mtime': stat.st_mtime,
                'sha256': sha,
                'imported': True,
                'imported_at': datetime.utcnow().isoformat() + 'Z',
                'flame_path': flame_folder,
                'status': 'ok',
                'last_error': None
            })
        except Exception as e:
            logging.error(f"Failed to record import for {file_path}: {e}")
            entry.update({
                'imported': False,
                'status': 'failed',
                'last_error': str(e)
            })
    
    def record_import_failure(self, rel_key: str, 
                             error: str) -> None:
        """Record failed import attempt in manifest.
        
        Args:
            rel_key: Relative path key in manifest
            error: Error message or description
        """
        entries = self.manifest.setdefault('entries', {})
        entry = entries.setdefault(rel_key, {})
        
        entry.update({
            'imported': False,
            'status': 'failed',
            'last_error': error
        })


# End of file
