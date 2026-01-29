# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [2026.2.0] - 2025-10-31

### Added
- New SSH key generator utility with encryption and backup functionality.

### Fixed
- Security vulnerabilities in `create_ssh_keys_linux.py` (CWE-1333, CWE-400, CWE-730).
- Incomplete URL substring sanitization in `nuke_download_tools`.

### Changed
- Updated all version references to `2026.2.0` for Autodesk Flame 2026.2.0 compatibility.
- Updated press release for version `2026.2.0`.

## [2026.1.0] - 2025-10-11

### Added
- Scripts to validate downloads by comparing files to MD5 hashes.
- Feature to export preset ideas and templates.
- Script to convert custom directory structures to Flame workspaces.
- Scripts to create and install a Flame ColorToolkit.
- Script to copy Flame `init.cfg` to project setups directory.
- Enabled 'expanded' attribute of PyObjects on startup for better UI state persistence.

### Fixed
- Updated output paths and logging for OCIO scripts.
- Initialized `replacements` dictionary in `flame_launcher` to prevent `NameError`.
- Resolved `SyntaxError` and `SyntaxWarning` in core create functions.
- Fixed a bug in the template saving process.
- Addressed a performance issue on macOS 15 by setting `QT_QUICK_BACKEND`.
- Corrected various minor bugs in the template export process.

### Changed
- Updated `.gitignore` to exclude more files.
- Updated VERSION file to `2026.1.0`.
- Updated directory tree documentation in `docs/insights`.
- Restored session template JSON.

### Refactored
- Converted the color toolkit installer to a shell script and improved logging.
- Aligned workspace configuration with the filesystem and corrected paths.
- Applied PEP-8 formatting to core functions and other scripts.
- Refactored the main window and fixed an exit error.
- Refactored preset export functionality.

### Removed
- Unused or empty files.

## [2026.0.0] - 2025-08-10

### Added
- Updated `wiretap_IFFFS_project_EXAMPLE.xml` with more detailed examples.

### Fixed
- Corrected cache descriptions in Wiretap XML generation.
- Rearranged mistakenly nested installer files.
- Handled internet connection failures gracefully.

### Changed
- Made modifications to improve compatibility with macOS.

## [0.1.0] - 2025-07-08

### Added
- Initial project structure and core application files.
- Separated UI from business logic.
- Centralized template handling.
- Implemented basic linting and formatting with Ruff.