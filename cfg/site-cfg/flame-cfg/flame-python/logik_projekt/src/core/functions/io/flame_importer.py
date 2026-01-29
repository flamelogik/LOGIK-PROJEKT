################################################################################
# Filename: flame_importer.py
# Relative Path: src/core/functions/io/flame_importer.py
#
# Purpose: Encapsulate all Flame API interactions for importing clips and
#          managing workspace hierarchy.
#
# Author: phil_man@mac.com
# Copyright: Copyright (c) 2026
#
################################################################################

from __future__ import annotations

import logging
from typing import Optional, Any


def get_flame_module():
    """Get the Flame module, handling import errors gracefully."""
    try:
        import flame  # type: ignore
        return flame
    except ImportError:
        logging.error("Flame module not available")
        return None


class FlameImporter:
    """Handles all Flame API interactions for importing media.
    
    Isolates Flame-specific code to make testing and refactoring easier.
    """
    
    def __init__(self):
        """Initialize the importer."""
        self.flame = get_flame_module()
    
    def is_available(self) -> bool:
        """Check if Flame API is available."""
        return self.flame is not None
    
    def get_current_project(self) -> Optional[Any]:
        """Get the current Flame project object."""
        if not self.flame:
            return None
        try:
            proj = self.flame.projects.current_project
            import sys
            print(f"\n[flame_importer] Current project: {proj}", file=sys.stdout)
            print(f"[flame_importer] Project type: {type(proj)}", file=sys.stdout)
            # Print available attributes
            attrs = [a for a in dir(proj) if not a.startswith('_')]
            print(f"[flame_importer] Project attributes: {', '.join(attrs[:20])}", file=sys.stdout)
            sys.stdout.flush()
            return proj
        except Exception as e:
            import sys
            logging.error(f"Could not get current project: {e}")
            print(f"[flame_importer] ERROR getting project: {e}", file=sys.stdout)
            sys.stdout.flush()
            return None
    
    def get_project_attribute(self, proj: Any, attr: str) -> Optional[str]:
        """Safely get an attribute from a project object.
        
        Args:
            proj: Flame project object
            attr: Attribute name (e.g., 'name', 'nickname', 'project_path')
        
        Returns:
            Attribute value or None if not found/error
        """
        import sys
        if not proj:
            return None
        try:
            # First try the direct attribute
            value = getattr(proj, attr, None)

            # If project_path is missing, attempt sensible fallbacks
            if value is None and attr == 'project_path':
                # Common alternative attribute names to try
                for alt in ('project_folder', 'projectFolder', 'folder', 'path', 'project_dir', 'projectDirectory'):
                    alt_val = getattr(proj, alt, None)
                    if alt_val:
                        print(f"[flame_importer] get_project_attribute('{attr}') derived from '{alt}' = {alt_val}", file=sys.stdout)
                        sys.stdout.flush()
                        return alt_val

                # Try constructing a candidate path from the project name using Flame's typical projects root
                proj_name = getattr(proj, 'name', None) or getattr(proj, 'project_name', None)
                if proj_name:
                    candidate = f"/var/opt/Autodesk/flame/projects/{proj_name}"
                    try:
                        import os
                        if os.path.exists(candidate):
                            print(f"[flame_importer] get_project_attribute('{attr}') = {candidate} (validated)", file=sys.stdout)
                            sys.stdout.flush()
                            return candidate
                        else:
                            # Return candidate anyway as a best-effort fallback
                            print(f"[flame_importer] get_project_attribute('{attr}') = {candidate} (constructed, not validated)", file=sys.stdout)
                            sys.stdout.flush()
                            return candidate
                    except Exception:
                        # If os fails for any reason, fall through to returning None
                        pass

            # Otherwise return what we found (may be None)
            print(f"[flame_importer] get_project_attribute('{attr}') = {value}", file=sys.stdout)
            sys.stdout.flush()
            return value
        except Exception as e:
            print(f"[flame_importer] get_project_attribute('{attr}') failed: {e}", file=sys.stdout)
            sys.stdout.flush()
            return None
    
    def resolve_destination(self, flame_folder_path: str, 
                           create_missing: bool = True) -> Optional[Any]:
        """Walk workspace hierarchy to find or create destination object.
        
        Navigates through libraries and folders, creating them as needed.
        
        Args:
            flame_folder_path: Path like 'assets/video/footage/raw'
            create_missing: If True, create missing intermediate folders
        
        Returns:
            Flame object (library/folder) or None on failure
        """
        if not self.flame:
            logging.error("Flame not available")
            return None
        
        try:
            proj = self.flame.projects.current_project
            if not proj:
                logging.error("No current project")
                return None
            
            destination = proj.current_workspace
            if not destination:
                logging.error("Could not get workspace")
                return None
            
            # Parse path and navigate/create hierarchy
            path_parts = [p for p in flame_folder_path.split('/') if p]
            
            for idx, part in enumerate(path_parts):
                found = False

                # Try to find existing child with matching name
                children = getattr(destination, 'children', None)
                if children:
                    try:
                        for child in list(children):
                            if getattr(child, 'name', None) == part:
                                destination = child
                                found = True
                                break
                    except Exception as e:
                        logging.warning(f"Error iterating children: {e}")

                # If not found, try a recursive search from the workspace root for top-level segments
                if not found and idx == 0:
                    try:
                        root = proj.current_workspace
                        # shallow recursive search for a child with the same name anywhere beneath root
                        candidate = self._recursive_find(root, part)
                        if candidate:
                            destination = candidate
                            found = True
                            logging.info(f"Resolved top-level '{part}' by recursive search")
                    except Exception as e:
                        logging.warning(f"Recursive search failed: {e}")

                if not found:
                    if not create_missing:
                        raise ValueError(f"Cannot find '{part}' under "
                                         f"'{getattr(destination, 'name', 'root')}'")

                    # Try to create missing folder (defensive)
                    new_dest = self._create_folder(destination, part)
                    if not new_dest:
                        raise RuntimeError(f"Failed to create folder '{part}'")
                    destination = new_dest

            return destination
        
        except Exception as e:
            logging.error(f"Could not resolve destination '{flame_folder_path}': {e}")
            return None
    
    def _recursive_find(self, parent: Any, name: str) -> Optional[Any]:
        """Recursively search for a child object with a given name under parent.

        This is a best-effort, shallow recursion to locate an existing library or
        folder with the same name to avoid creating duplicate top-level objects.
        """
        try:
            children = getattr(parent, 'children', None)
            if not children:
                return None

            for child in list(children):
                if getattr(child, 'name', None) == name:
                    return child
                # Recurse one level deep
                grand_children = getattr(child, 'children', None)
                if grand_children:
                    for gc in list(grand_children):
                        if getattr(gc, 'name', None) == name:
                            return gc
            return None
        except Exception as e:
            logging.warning(f"_recursive_find failed: {e}")
            return None


    def _create_folder(self, parent: Any, folder_name: str) -> Optional[Any]:
        """Create a folder under a parent object.

        Tries multiple methods depending on parent type. This implementation is
        defensive: it ensures the attribute exists and is callable before
        invoking it, and logs detailed information on failure.

        Args:
            parent: Parent Flame object
            folder_name: Name for new folder

        Returns:
            New folder object or None on failure
        """
        methods = [
            ('create_library', 'library'),
            ('create_folder', 'folder'),
            ('create_reel_group', 'reel_group')
        ]

        for method_name, type_name in methods:
            if hasattr(parent, method_name):
                method = getattr(parent, method_name)
                if not callable(method):
                    logging.warning(f"Attribute '{method_name}' exists but is not callable on '{getattr(parent, 'name', 'parent')}'")
                    continue

                try:
                    new_obj = method(folder_name)
                    if new_obj is None:
                        logging.warning(f"{type_name} creation returned None for '{folder_name}'")
                        continue
                    logging.info(f"Created {type_name} '{folder_name}'")
                    return new_obj
                except Exception as e:
                    logging.warning(f"Failed to create {type_name}: {e}")

        logging.error(f"Don't know how to create '{folder_name}' under "
                      f"'{getattr(parent, 'name', 'root')}'")
        return None
    
    def import_clip(self, file_path: str, destination: Any) -> bool:
        """Import a clip into the specified destination.
        
        Args:
            file_path: Full path to media file
            destination: Flame destination object (library/folder)
        
        Returns:
            True if import succeeded, False otherwise
        """
        if not self.flame:
            logging.error("Flame not available")
            return False
        
        if not destination:
            logging.error("No destination object provided")
            return False
        
        try:
            self.flame.import_clips(file_path, destination)
            logging.info(f"Successfully imported {file_path}")
            return True
        except Exception as e:
            logging.error(f"Failed to import {file_path}: {e}")
            return False
    
    def schedule_idle_event(self, callback, delay: int = 1) -> bool:
        """Schedule a callback to run during Flame idle time.
        
        Args:
            callback: Function to call
            delay: Delay in seconds before execution
        
        Returns:
            True if scheduled successfully, False otherwise
        """
        if not self.flame:
            logging.error("Flame not available")
            return False
        
        try:
            self.flame.schedule_idle_event(callback, delay=delay)
            return True
        except Exception as e:
            logging.error(f"Failed to schedule idle event: {e}")
            return False


# End of file
