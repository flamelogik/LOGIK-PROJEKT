################################################################################
# Filename: sync_assets.py
# Relative Path: hooks/sync_assets.py
#
# Purpose: Main orchestrator for automatic filesystem → Flame asset import.
#          Reads bookmarks, monitors watched folders, and imports new files
#          during Flame idle time.
#
# Author: phil_man@mac.com
# Copyright: Copyright (c) 2026
#
################################################################################

from __future__ import annotations

import logging
import os
import sys
import importlib.util
from datetime import datetime
from pathlib import Path
from typing import Optional, Set, List

# Print module initialization debug message
print("\n" + "="*80)
print("[sync_assets] MODULE INITIALIZATION")
print("="*80)

# Get paths relative to this hook file
hook_file = os.path.abspath(__file__)
hook_dir = os.path.dirname(hook_file)
logik_projekt_root = os.path.dirname(hook_dir)
io_functions_dir = os.path.join(logik_projekt_root, 'src', 'core', 'functions', 'io')

print(f"[sync_assets] hook_file: {hook_file}")
print(f"[sync_assets] hook_dir: {hook_dir}")
print(f"[sync_assets] logik_projekt_root: {logik_projekt_root}")
print(f"[sync_assets] io_functions_dir: {io_functions_dir}")

# Import supporting modules by loading them directly from disk
print("[sync_assets] Loading supporting modules...")

def load_module(module_name: str, file_path: str):
    """Load a Python module directly from a file path."""
    try:
        spec = importlib.util.spec_from_file_location(module_name, file_path)
        if spec and spec.loader:
            module = importlib.util.module_from_spec(spec)
            sys.modules[module_name] = module
            spec.loader.exec_module(module)
            print(f"  ✓ {module_name} loaded from {file_path}")
            return module
        else:
            print(f"  ✗ {module_name}: Could not create spec for {file_path}")
            return None
    except Exception as e:
        import traceback
        print(f"  ✗ {module_name}: {e}")
        print(traceback.format_exc())
        return None

# Load the three supporting modules
bookmark_manager = load_module(
    'bookmark_manager',
    os.path.join(io_functions_dir, 'bookmark_manager.py')
)
manifest_tracker = load_module(
    'manifest_tracker',
    os.path.join(io_functions_dir, 'manifest_tracker.py')
)
flame_importer = load_module(
    'flame_importer',
    os.path.join(io_functions_dir, 'flame_importer.py')
)

if all([bookmark_manager, manifest_tracker, flame_importer]):
    print("[sync_assets] All supporting modules loaded successfully")
else:
    print("[sync_assets] ERROR: Some modules failed to load!")

print("="*80 + "\n")

# --- Configuration ---
DEFAULT_MAX_IMPORTS_PER_CYCLE = 1
DEFAULT_USE_HASH = False
DEFAULT_MIRROR_SUBDIRS = True
DEFAULT_INCLUDE_EXTENSIONS: Optional[List[str]] = None  # e.g. ['.mov', '.mp4']

# Debugging output
DEBUG: bool = True

# Only sync bookmarks whose flame folder path begins with this root
SYNC_ROOT: str = 'assets'

# --- Global State ---
processed_folders_this_cycle: Set[Path] = set()
auto_sync_enabled: bool = True


def _process_single_folder(fs_path_str: str, 
                          flame_folder_str: str,
                          flame_importer_instance,
                          *,
                          use_hash: bool = DEFAULT_USE_HASH,
                          mirror_subdirs: bool = DEFAULT_MIRROR_SUBDIRS,
                          include_extensions: Optional[List[str]] = DEFAULT_INCLUDE_EXTENSIONS,
                          max_imports: int = DEFAULT_MAX_IMPORTS_PER_CYCLE) -> None:
    """Process a single watched folder: scan for new files and import them.
    
    Args:
        fs_path_str: Filesystem path to watched folder
        flame_folder_str: Destination Flame folder path
        flame_importer_instance: FlameImporter instance
        use_hash: Use SHA256 for change detection
        mirror_subdirs: Recreate subdirs under Flame destination
        include_extensions: Filter by file extension if provided
        max_imports: Max files to import per cycle
    """
    fs_path = Path(fs_path_str)
    
    if DEBUG:
        print(f"[sync_assets] process_single_folder: {fs_path} -> {flame_folder_str}")
    
    # Validate folder exists
    if not fs_path.exists() or not fs_path.is_dir():
        logging.warning(f"Watch folder invalid: {fs_path}")
        if DEBUG:
            print(f"[sync_assets] abort: folder not found: {fs_path}")
        return
    
    # Prevent re-processing same folder in one cycle
    if fs_path in processed_folders_this_cycle:
        if DEBUG:
            print(f"[sync_assets] already processed this cycle: {fs_path}")
        return
    
    # Load or create manifest
    tracker = manifest_tracker.ManifestTracker(fs_path)
    
    # Scan for new files
    files_to_import: List[Path] = []
    for root, dirs, files in os.walk(fs_path):
        root_path = Path(root)
        rel_root = root_path.relative_to(fs_path)
        
        for fname in sorted(files):
            # Skip hidden files
            if fname.startswith('.'):
                continue
            
            file_path = root_path / fname
            rel_key = str((rel_root / fname).as_posix()) if rel_root.parts else fname
            
            # Filter by extension if configured
            if include_extensions is not None:
                if file_path.suffix.lower() not in [e.lower() for e in include_extensions]:
                    continue
            
            # Check if already imported
            if tracker.is_file_imported(rel_key, file_path, use_hash=use_hash):
                if DEBUG:
                    print(f"[sync_assets] already imported: {rel_key}")
                continue
            
            files_to_import.append(file_path)
            if len(files_to_import) >= max_imports:
                break
        
        if len(files_to_import) >= max_imports:
            break
    
    if DEBUG:
        print(f"[sync_assets] candidates: {[str(p) for p in files_to_import]}")
    
    if not files_to_import:
        if DEBUG:
            print(f"[sync_assets] no new files in {fs_path}")
        processed_folders_this_cycle.add(fs_path)
        tracker.save()
        return
    
    # Resolve destination without creating new top-level libraries/folders
    dest_obj = flame_importer_instance.resolve_destination(flame_folder_str, create_missing=False)
    print(f"[sync_assets] resolve_destination(create_missing=False) for '{flame_folder_str}' -> {dest_obj}")
    if not dest_obj:
        logging.error(f"Could not resolve destination '{flame_folder_str}' (create_missing=False)")
        # Mark all files as failed (destination missing in Flame workspace)
        for file_path in files_to_import:
            rel_key = str(file_path.relative_to(fs_path).as_posix())
            tracker.record_import_failure(rel_key, 'Destination resolution failed (missing in Flame workspace)')
        tracker.save()
        processed_folders_this_cycle.add(fs_path)
        return
    
    # Import files one by one
    for file_path in files_to_import:
        rel_key = str(file_path.relative_to(fs_path).as_posix())
        
        try:
            # Determine target folder (with optional subdirectory mirroring)
            target_flame_folder = flame_folder_str
            if mirror_subdirs:
                rel_parent = file_path.parent.relative_to(fs_path)
                if rel_parent.parts:
                    target_flame_folder = f"{flame_folder_str}/{rel_parent.as_posix()}"
            
            print(f"[sync_assets] importing: {file_path} -> {target_flame_folder}")
            
            # Resolve target without creating new top-level folders
            target_obj = flame_importer_instance.resolve_destination(target_flame_folder, create_missing=False)
            print(f"[sync_assets] resolve_destination(create_missing=False) for target '{target_flame_folder}' -> {target_obj}")
            if not target_obj:
                raise RuntimeError(f"Could not resolve '{target_flame_folder}' in Flame workspace (create_missing=False)")

            success = flame_importer_instance.import_clip(str(file_path), target_obj)
            if not success:
                raise RuntimeError("Import clip call failed")
            
            # Record success
            tracker.record_import_success(rel_key, file_path, target_flame_folder, 
                                         use_hash=use_hash)
            logging.info(f"Imported {file_path}")
            tracker.save()
            
            # Schedule next iteration to keep UI responsive
            importer = flame_importer_instance
            importer.schedule_idle_event(
                lambda fp=fs_path_str, ff=flame_folder_str: _process_single_folder(
                    fp, ff, importer,
                    use_hash=use_hash,
                    mirror_subdirs=mirror_subdirs,
                    include_extensions=include_extensions,
                    max_imports=max_imports
                ),
                delay=1
            )
            processed_folders_this_cycle.add(fs_path)
            return
        
        except Exception as e:
            import traceback
            print(f"[sync_assets] import failed: {file_path}")
            print(traceback.format_exc())
            logging.error(f"Failed to import {file_path}: {e}")
            tracker.record_import_failure(rel_key, str(e))
            tracker.save()
            continue
    
    processed_folders_this_cycle.add(fs_path)
    tracker.save()


def sync_watched_folders(project_name: str,
                        force: bool = False,
                        *,
                        use_hash: bool = DEFAULT_USE_HASH,
                        mirror_subdirs: bool = DEFAULT_MIRROR_SUBDIRS,
                        include_extensions: Optional[List[str]] = DEFAULT_INCLUDE_EXTENSIONS,
                        max_imports: int = DEFAULT_MAX_IMPORTS_PER_CYCLE) -> None:
    """Main sync loop: read bookmarks and schedule folder processing.
    
    Args:
        project_name: Flame project name
        force: Ignore auto_sync_enabled setting
        use_hash: Use SHA256 for change detection
        mirror_subdirs: Recreate subdirs in Flame
        include_extensions: File extension filter
        max_imports: Max files per cycle
    """
    logging.info("Starting assets sync cycle")
    
    # Check if we should run
    if not force and not auto_sync_enabled:
        logging.info("Auto-sync disabled; skipping")
        return
    
    # Reset processed set for this cycle
    global processed_folders_this_cycle
    processed_folders_this_cycle.clear()
    
    # Initialize Flame importer
    importer = flame_importer.FlameImporter()
    if not importer.is_available():
        logging.error("Flame not available; aborting")
        return
    
    # Get project path
    try:
        proj = importer.get_current_project()
        if not proj:
            logging.error("Could not get current project")
            return
        
        project_path_str = importer.get_project_attribute(proj, 'project_path')
        project_nickname = importer.get_project_attribute(proj, 'nickname') or project_name
        
        if not project_path_str:
            logging.error("Could not determine project path")
            return
        
        project_path = Path(project_path_str)
    except Exception as e:
        logging.error(f"Error getting project info: {e}")
        return
    
    # Load bookmarks
    bookmarks = bookmark_manager.load_bookmarks_for_project(project_path, project_nickname)
    if not bookmarks:
        logging.error("No bookmarks found; aborting")
        if auto_sync_enabled:
            importer.schedule_idle_event(
                lambda pn=project_name: sync_watched_folders(pn,
                                                            use_hash=use_hash,
                                                            mirror_subdirs=mirror_subdirs,
                                                            include_extensions=include_extensions,
                                                            max_imports=max_imports),
                delay=30
            )
        return
    
    # Filter by sync root
    original_count = len(bookmarks)
    bookmarks = bookmark_manager.filter_bookmarks_by_sync_root(bookmarks, SYNC_ROOT)
    if DEBUG:
        print(f"[sync_assets] bookmarks: original={original_count} filtered={len(bookmarks)}")

    # Further restrict to bookmarks inside this project's assets root to avoid
    # importing assets from other projects. This is a safety measure and can be
    # made configurable later.
    try:
        project_assets_root = (Path('/PROJEKTS') / project_nickname / 'assets').resolve()
    except Exception:
        project_assets_root = Path('/PROJEKTS') / project_nickname / 'assets'

    if DEBUG:
        print(f"[sync_assets] Project assets root: {project_assets_root}")

    allowed_bookmarks = []
    for b in bookmarks:
        fs_path = b.get('filesystem_path')
        if not fs_path:
            continue
        try:
            p = Path(fs_path).resolve()
            if p.is_relative_to(project_assets_root):
                allowed_bookmarks.append(b)
            else:
                logging.info(f"Skipping bookmark outside project assets: {fs_path}")
                print(f"[sync_assets] Skipping outside-project bookmark: {fs_path}")
        except Exception:
            # If resolving fails, skip the bookmark for safety
            logging.warning(f"Skipping bookmark with unresolvable path: {fs_path}")
            print(f"[sync_assets] Skipping unresolvable bookmark: {fs_path}")

    if DEBUG:
        print(f"[sync_assets] bookmarks after project filter: {len(allowed_bookmarks)}")

    bookmarks = allowed_bookmarks

    if not bookmarks:
        logging.info("No bookmarks under sync root and project assets")
        if auto_sync_enabled:
            importer.schedule_idle_event(
                lambda pn=project_name: sync_watched_folders(pn,
                                                            use_hash=use_hash,
                                                            mirror_subdirs=mirror_subdirs,
                                                            include_extensions=include_extensions,
                                                            max_imports=max_imports),
                delay=30
            )
        return
    
    # Process each bookmark
    for bookmark in bookmarks:
        fs_path_str = bookmark.get('filesystem_path')
        flame_folder_str = bookmark.get('flame_folder')

        if not fs_path_str or not flame_folder_str:
            logging.warning(f"Invalid bookmark: {bookmark}")
            continue

        # Enforce that the filesystem path is under this project's assets root
        try:
            p = Path(fs_path_str).resolve()
            if not p.is_relative_to(project_assets_root):
                logging.info(f"Skipping scheduling for bookmark outside project assets: {fs_path_str}")
                print(f"[sync_assets] Skipping scheduling for outside-project bookmark: {fs_path_str}")
                continue
        except Exception as e:
            logging.warning(f"Error resolving bookmark path {fs_path_str}: {e}")
            print(f"[sync_assets] Error resolving bookmark path {fs_path_str}: {e}")
            continue

        # Schedule processing
        try:
            importer.schedule_idle_event(
                lambda fp=fs_path_str, ff=flame_folder_str: _process_single_folder(
                    fp, ff, importer,
                    use_hash=use_hash,
                    mirror_subdirs=mirror_subdirs,
                    include_extensions=include_extensions,
                    max_imports=max_imports
                ),
                delay=2
            )
        except Exception as e:
            logging.warning(f"Failed to schedule {fs_path_str}: {e}")
    
    # Schedule next full pass
    if auto_sync_enabled:
        try:
            importer.schedule_idle_event(
                lambda pn=project_name: sync_watched_folders(pn,
                                                            use_hash=use_hash,
                                                            mirror_subdirs=mirror_subdirs,
                                                            include_extensions=include_extensions,
                                                            max_imports=max_imports),
                delay=30
            )
        except Exception:
            pass


def manual_sync(selection=None, project_name: Optional[str] = None) -> None:
    """Manual sync action callable from Flame menus."""
    import sys
    print("\n" + "="*80, file=sys.stdout)
    print("[sync_assets] manual_sync() called", file=sys.stdout)
    print(f"  selection: {selection}", file=sys.stdout)
    print(f"  project_name: {project_name}", file=sys.stdout)
    sys.stdout.flush()
    
    try:
        importer = flame_importer.FlameImporter()
        print(f"[sync_assets] importer created, is_available={importer.is_available()}", file=sys.stdout)
        sys.stdout.flush()
        
        if project_name is None and importer.is_available():
            proj = importer.get_current_project()
            print(f"[sync_assets] proj: {proj}", file=sys.stdout)
            sys.stdout.flush()
            
            project_name = importer.get_project_attribute(proj, 'name')
            print(f"[sync_assets] got project_name: {project_name}", file=sys.stdout)
            sys.stdout.flush()
    except Exception as e:
        import traceback
        print(f"[sync_assets] ERROR in manual_sync setup: {e}", file=sys.stdout)
        print(traceback.format_exc(), file=sys.stdout)
        sys.stdout.flush()
    
    project_name = project_name or 'unknown'
    print(f"[sync_assets] Calling sync_watched_folders with project_name={project_name}", file=sys.stdout)
    sys.stdout.flush()
    
    logging.info(f"Manual sync requested for {project_name}")
    sync_watched_folders(project_name, force=True)


def toggle_auto_sync(selection=None) -> None:
    """Toggle automatic background syncing."""
    global auto_sync_enabled
    auto_sync_enabled = not auto_sync_enabled
    logging.info(f"Auto-sync enabled: {auto_sync_enabled}")


def get_main_menu_custom_ui_actions():
    """Provide menu actions for manual control."""
    import sys
    print("\n" + "="*80, file=sys.stdout)
    print("DEBUG: get_main_menu_custom_ui_actions() called", file=sys.stdout)
    print("="*80, file=sys.stdout)
    sys.stdout.flush()
    
    logging.info("get_main_menu_custom_ui_actions() called")
    
    # Define wrapper functions that will be called by Flame
    def sync_now_action(selection):
        """Wrapper for manual sync."""
        import sys
        print("\n[sync_assets] sync_now_action() called!", file=sys.stdout)
        sys.stdout.flush()
        manual_sync(selection=selection)
    
    def toggle_sync_action(selection):
        """Wrapper for toggle auto sync."""
        import sys
        print("\n[sync_assets] toggle_sync_action() called!", file=sys.stdout)
        sys.stdout.flush()
        toggle_auto_sync(selection=selection)
    
    menu_structure = [
        {
            "name": "logik-projekt",
            "hierarchy": [],
            "actions": []
        },
        {
            "name": "sync",
            "hierarchy": ["logik-projekt"],
            "order": 10,
            "actions": [
                {
                    "name": "Sync Now",
                    "order": 0,
                    "execute": sync_now_action,
                    "minimumVersion": "2025"
                },
                {
                    "name": "Toggle Auto Sync",
                    "order": 1,
                    "execute": toggle_sync_action,
                    "minimumVersion": "2025"
                }
            ]
        }
    ]
    
    print("DEBUG: Menu structure created")
    for i, item in enumerate(menu_structure):
        print(
            f"  [{i}] name='{item.get('name')}', "
            f"hierarchy={item.get('hierarchy', 'N/A')}, "
            f"actions count={len(item.get('actions', []))}"
        )
    print(f"DEBUG: Returning menu with {len(menu_structure)} items")
    print("="*80 + "\n")
    
    return menu_structure


def get_media_panel_custom_ui_actions():
    """Expose sync controls in media panel context menus."""
    import sys
    print("\n" + "="*80, file=sys.stdout)
    print("DEBUG: get_media_panel_custom_ui_actions() called", file=sys.stdout)
    print("="*80, file=sys.stdout)
    sys.stdout.flush()
    
    logging.info("get_media_panel_custom_ui_actions() called")
    
    # Define wrapper functions that will be called by Flame
    def sync_now_action(selection):
        """Wrapper for manual sync."""
        import sys
        print("\n[sync_assets] sync_now_action() called!", file=sys.stdout)
        sys.stdout.flush()
        manual_sync(selection=selection)
    
    def toggle_sync_action(selection):
        """Wrapper for toggle auto sync."""
        import sys
        print("\n[sync_assets] toggle_sync_action() called!", file=sys.stdout)
        sys.stdout.flush()
        toggle_auto_sync(selection=selection)
    
    menu_structure = [
        {
            "name": "logik-projekt",
            "hierarchy": [],
            "actions": []
        },
        {
            "name": "sync",
            "hierarchy": ["logik-projekt"],
            "order": 10,
            "actions": [
                {
                    "name": "Sync Now",
                    "order": 0,
                    "execute": sync_now_action,
                    "minimumVersion": "2025"
                },
                {
                    "name": "Toggle Auto Sync",
                    "order": 1,
                    "execute": toggle_sync_action,
                    "minimumVersion": "2025"
                }
            ]
        }
    ]
    
    print("DEBUG: Menu structure created")
    for i, item in enumerate(menu_structure):
        print(
            f"  [{i}] name='{item.get('name')}', "
            f"hierarchy={item.get('hierarchy', 'N/A')}, "
            f"actions count={len(item.get('actions', []))}"
        )
    print(f"DEBUG: Returning menu with {len(menu_structure)} items")
    print("="*80 + "\n")
    
    return menu_structure


def app_initialized(project_name: str) -> None:
    """Entry point called by Flame when project loads.
    
    Args:
        project_name: Name of the loaded project
    """
    import sys
    print("\n" + "="*80, file=sys.stdout)
    print(f"[sync_assets] app_initialized called for project: {project_name}", file=sys.stdout)
    print("="*80 + "\n", file=sys.stdout)
    sys.stdout.flush()
    
    # Set up logging
    logging.basicConfig(
        level=logging.INFO,
        format='%(asctime)s - %(levelname)s - [sync_assets] %(message)s'
    )
    logging.info(f"sync_assets hook initialized for project: {project_name}")
    
    # Log that we're about to try to initialize Flame importer
    logging.info("Attempting to initialize Flame importer...")
    print("[sync_assets] Attempting to initialize Flame importer...")
    
    # Start sync after brief delay
    importer = flame_importer.FlameImporter()
    if importer.is_available():
        logging.info("Flame importer initialized successfully")
        print("[sync_assets] Flame importer initialized successfully")
        try:
            importer.schedule_idle_event(
                lambda pn=project_name: sync_watched_folders(pn),
                delay=5
            )
            logging.info("Initial sync scheduled for 5 seconds delay")
            print("[sync_assets] Initial sync scheduled for 5 seconds delay")
        except Exception as e:
            logging.error(f"Could not schedule initial sync: {e}")
            print(f"[sync_assets] ERROR: Could not schedule initial sync: {e}")
    else:
        logging.error("Flame not available at initialization")
        print("[sync_assets] ERROR: Flame not available at initialization")


# End of file
