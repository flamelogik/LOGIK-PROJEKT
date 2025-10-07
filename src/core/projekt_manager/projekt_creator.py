#!/usr/bin/env python3
# -------------------------------------------------------------------------- #
# Filename:     projekt_creator.py
# Purpose:      Create Autodesk Flame projects and associated file structures.
# Description:  This script handles the creation of a new Autodesk Flame
#               project, including setting up its directory structure,
#               copying necessary files, creating symbolic links, and
#               generating various scripts for project management and backup.

# Author:       phil_man@mac.com
# Copyright:    Copyright (c) 2025
# Disclaimer:   Disclaimer at bottom of script.
# License:      GNU General Public License v3.0 (GPL-3.0).
#               https://www.gnu.org/licenses/gpl-3.0.en.html

# Version:      2026.1.0
# Status:       Production
# Type:         Module
# Created:      2025-07-01
# Modified:     2025-08-03

# Changelog:    Changelog at bottom of script.
# -------------------------------------------------------------------------- #

import os
import logging
import subprocess

from src.core.utils import (
    path_utils
)
from src.core.projekt_manager.projekt_models import (
    ProjektParameters
)
from src.core.functions.io.export_session_variables import (
    export_session_variables
)
from src.core.functions.io.export_session_adsk_json import (
    export_session_adsk_json
)
from src.core.functions.create.create_projekt_filesystem_dirs import (
    create_projekt_filesystem_dirs
)
from src.core.functions.io.export_session_xml import (
    export_session_xml
)
from src.core.functions.create.create_flame_wiretap_node import (
    create_flame_wiretap_node
)
from src.core.functions.create.create_flame_setup_dirs import (
    create_flame_setup_dirs
)
from src.core.functions.create.create_flame_symbolic_links import (
    create_flame_symbolic_links
)
from src.core.functions.copy.copy_flame_presets import (
    copy_flame_presets
)
from src.core.functions.copy.copy_flame_python_scripts import (
    copy_flame_python_scripts
)
from src.core.functions.get.get_flame_bookmarks_path import (
    get_flame_bookmarks_path
)
from src.core.functions.copy.copy_flame_bookmarks import (
    copy_flame_bookmarks
)
from src.core.functions.copy.copy_init_config import (
    copy_init_config
)
from src.core.functions.create.create_flame_archive_script import (
    create_flame_archive_script
)
from src.core.functions.create.create_projekt_backup_script import (
    create_projekt_backup_script
)
from src.core.functions.create.create_flame_startup_script import (
    create_flame_startup_script
)
from src.core.functions.create.create_flame_launcher_script import (
    create_flame_launcher_script
)
from src.core.functions.create.create_projekt_launcher_alias import (
    create_projekt_launcher_alias
)
from src.core.functions.create.create_projekt_pgsql_db import (
    create_projekt_pgsql_db
)
from src.core.functions.copy.copy_current_session_files import (
    copy_current_session_files
)
from src.core.utils.system_info_utils import get_short_hostname

logger = logging.getLogger(__name__)


class ProjektCreator:
    def create_projekt(self, config: ProjektParameters):
        # 1. Start Logging
        logger.info(
            f"Creating PROJEKT: "
            f"{config.flame_projekt_name}"
        )
        logger.info(
            f"Launch Flame after creation: "
            f"{config.launch_flame_after_creation}"
        )

        # 2. Export Session Variables
        export_session_variables(config.__dict__)

        # 3. Export Session ADSK JSON
        export_session_adsk_json(config.__dict__)

        # 4. Create Filesystem Directories
        json_filepath = config.logik_projekt_config_tree
        target_root_dir = config.logik_projekt_path
        path_utils.create_directory(
            os.path.dirname(
                target_root_dir
            )
        )
        create_projekt_filesystem_dirs(
            json_filepath,
            os.path.dirname(target_root_dir),
            os.path.basename(target_root_dir)
        )
        iterations_dir = (
            os.path.join(
                config.logik_projekt_path,
                "flame",
                "iterations"
            )
        )
        path_utils.create_directory(iterations_dir)

        # 5. Generate Flame Project XML
        xml_template_path = (
            "cfg/"
            "site-cfg/"
            "flame-cfg/"
            "flame-templates/"
            "wiretap-templates/"
            "wiretap_IFFFS_project_EXAMPLE.xml"
        )
        output_xml_path = (
            "pref/"
            "session-preferences/"
            "current_session-wiretap_template.xml"
        )
        export_session_xml(
            config.__dict__,
            xml_template_path,
            output_xml_path
        )

        # 6. Create Flame Project via Wiretap
        create_flame_wiretap_node(
            config.flame_projekt_name,
            output_xml_path
        )

        # 7. Create Flame Project Setup Directories
        create_flame_setup_dirs(
            config.flame_projekt_setups_dir
        )

        # 8. Create Symbolic Links
        create_flame_symbolic_links(
            config.logik_projekt_path,
            config.flame_projekt_setups_dir,
            config.current_workstation
        )

        # 9. Copy Site Presets
        copy_flame_presets(
            config.logik_projekt_path,
            config.flame_projekt_setups_dir
        )

        # 10. Copy Flame Python Scripts
        copy_flame_python_scripts(
            config.flame_projekt_setups_dir
        )

        # 11. Copy Flame Bookmarks
        try:
            flame_bookmarks_source_path = get_flame_bookmarks_path(
                config.logik_projekt_config_name
            )
            flame_bookmarks_destination_dir = os.path.join(
                config.flame_projekt_setups_dir,
                "status"
            )
            copy_flame_bookmarks(
                flame_bookmarks_source_path,
                flame_bookmarks_destination_dir
            )
        except Exception as e:
            logger.error(f"Failed to copy Flame bookmarks: {e}")

        # 12. Copy Flame Init Config
        if config.flame_projekt_init:
            try:
                copy_init_config(
                    os.path.basename(config.flame_projekt_init),
                    config.flame_projekt_setups_dir,
                    config.flame_projekt_name
                )
            except Exception as e:
                logger.error(f"Failed to copy Flame init config: {e}")
        else:
            logger.info("No Flame init config file specified. Skipping copy.")

        # 13. Create Archive Script
        create_flame_archive_script(config.__dict__)

        # 14. Create Backup Script
        template_dir = os.path.join(
            path_utils.get_repository_root_dir(),
            "cfg",
            "site-cfg",
            "logik-projekt-cfg",
            "logik-projekt-templates"
        )
        backup_template_path = os.path.join(
            template_dir,
            "rsync-backup-templates",
            "backup_template"
        )
        backup_script_dir = os.path.join(
            config.logik_projekt_path,
            "backup",
            "backup-scripts",
            config.current_workstation
        )
        path_utils.create_directory(backup_script_dir)
        create_projekt_backup_script(
            config.__dict__,
            backup_template_path,
            backup_script_dir
        )

        # 15. Create Flame Startup Script
        create_flame_startup_script(
            config.flame_projekt_setups_dir,
            config.logik_projekt_config_workspace
        )

        # 16. Create Flame Launcher Script
        launcher_script_path = create_flame_launcher_script(
            repository_root_dir=path_utils.get_repository_root_dir(),
            logik_projekt_path=config.logik_projekt_path,
            current_workstation=config.current_workstation,
            current_os=config.current_os,
            the_projekts_dir=config.logik_projekt_path.rsplit('/', 1)[0],
            the_projekt_flame_dirs=config.flame_projekt_home.rsplit('/', 1)[0],
            the_adsk_dir="/opt/Autodesk",
            the_adsk_dir_linux="/opt/Autodesk",
            the_adsk_dir_macos="/Applications/Autodesk",
            logik_projekt_name=config.logik_projekt_name,
            the_projekt_flame_name=config.flame_projekt_name,
            flame_software_sanitized_version=config.flame_software_sanitized_version,
            flame_software_choice=config.flame_software_choice,
            flame_projekt_setups_dir=config.flame_projekt_setups_dir,
        )

        # 17. Create Project Launcher Alias
        create_projekt_launcher_alias(
            config.logik_projekt_name,
            launcher_script_path
        )

        # 18. Create PostgreSQL Database
        create_projekt_pgsql_db(
            config.logik_projekt_name,
            config.logik_projekt_path
        )

        # 19. Launch Flame (Optional)
        if config.launch_flame_after_creation:
            logger.info(
                f"Launching Flame with script: "
                f"{launcher_script_path}"
            )
            try:
                os.chmod(launcher_script_path, 0o755)
                process = subprocess.Popen(
                    [launcher_script_path],
                    stdout=subprocess.PIPE,
                    stderr=subprocess.STDOUT,
                    text=True,
                    bufsize=1,
                    universal_newlines=True
                )
                for line in iter(process.stdout.readline, ''):
                    logger.info(line.strip())
                process.stdout.close()
                return_code = process.wait()
                if return_code:
                    raise subprocess.CalledProcessError(
                        return_code,
                        launcher_script_path
                    )
                logger.info("Flame launched successfully.")
            except (subprocess.CalledProcessError, FileNotFoundError) as e:
                logger.error(f"Failed to launch Flame: {e}")

        # 20. Copy Current Session Files
        copy_current_session_files(
            config.logik_projekt_path,
            config.current_workstation
        )

        logger.info("PROJEKT creation logic executed.")


def create_projekt(projekt_summary_data: dict):
    """
    Create a new project using the provided summary data.
  
    Args:
        projekt_summary_data: Dictionary containing all project config data
    """
    projekt_creator = ProjektCreator()
    projekt_config = ProjektParameters(
        current_user=projekt_summary_data.get(
            "current_user",
            ""
        ),
        current_group=projekt_summary_data.get(
            "current_group",
            ""
        ),
        current_workstation=projekt_summary_data.get(
            "current_workstation",
            ""
        ),
        current_os=projekt_summary_data.get(
            "current_os",
            ""
        ),
        flame_software_choice=projekt_summary_data.get(
            "flame_software_choice",
            ""
        ),
        flame_software_name=projekt_summary_data.get(
            "flame_software_name",
            ""
        ),
        flame_software_version=projekt_summary_data.get(
            "flame_software_version",
            "",
        ),
        flame_software_sanitized_name=projekt_summary_data.get(
            "flame_software_sanitized_name",
            "",
        ),
        flame_software_sanitized_version=projekt_summary_data.get(
            "flame_software_sanitized_version",
            "",
        ),
        flame_projekt_name=projekt_summary_data.get(
            "flame_projekt_name",
            ""
        ),
        flame_projekt_nickname=projekt_summary_data.get(
            "flame_projekt_nickname",
            "",
        ),
        flame_projekt_shotgun_name=projekt_summary_data.get(
            "flame_projekt_shotgun_name",
            "",
        ),
        flame_projekt_description=projekt_summary_data.get(
            "flame_projekt_description",
            "",
        ),
        flame_projekt_home=projekt_summary_data.get(
            "flame_projekt_home",
            "",
        ),
        flame_projekt_setups_dir=projekt_summary_data.get(
            "flame_projekt_setups_dir",
            "",
        ),
        flame_projekt_media_dir=projekt_summary_data.get(
            "flame_projekt_media_dir",
            "",
        ),
        flame_projekt_catalog_dir=projekt_summary_data.get(
            "flame_projekt_catalog_dir",
            "",
        ),
        flame_projekt_width=projekt_summary_data.get(
            "flame_projekt_width",
            "",
        ),
        flame_projekt_height=projekt_summary_data.get(
            "flame_projekt_height",
            "",
        ),
        flame_projekt_ratio=projekt_summary_data.get(
            "flame_projekt_ratio",
            "",
        ),
        flame_projekt_depth=projekt_summary_data.get(
            "flame_projekt_depth",
            "",
        ),
        flame_projekt_rate=projekt_summary_data.get(
            "flame_projekt_rate",
            "",
        ),
        flame_projekt_mode=projekt_summary_data.get(
            "flame_projekt_mode",
            "",
        ),
        flame_projekt_start=projekt_summary_data.get(
            "flame_projekt_start",
            "",
        ),
        flame_projekt_init=projekt_summary_data.get(
            "flame_projekt_init",
            "",
        ),
        flame_projekt_ocio=projekt_summary_data.get(
            "flame_projekt_ocio",
            "",
        ),
        flame_projekt_ocio_path=projekt_summary_data.get(
            "flame_projekt_ocio_path",
            "",
        ),
        flame_projekt_ocio_name=projekt_summary_data.get(
            "flame_projekt_ocio_name",
            "",
        ),
        flame_projekt_cachef=projekt_summary_data.get(
            "flame_projekt_cachef",
            "",
        ),
        flame_projekt_cachef_id=projekt_summary_data.get(
            "flame_projekt_cachef_id",
            "",
        ),
        flame_projekt_cachei=projekt_summary_data.get(
            "flame_projekt_cachei",
            "",
        ),
        flame_projekt_cachei_id=projekt_summary_data.get(
            "flame_projekt_cachei_id",
            "",
        ),
        logik_projekt_name=projekt_summary_data.get(
            "logik_projekt_name",
            "",
        ),
        logik_projekt_path=projekt_summary_data.get(
            "logik_projekt_path",
            "",
        ),
        logik_projekt_config_name=projekt_summary_data.get(
            "logik_projekt_config_name",
            "",
        ),
        logik_projekt_config_tree=projekt_summary_data.get(
            "logik_projekt_config_tree",
            "",
        ),
        logik_projekt_config_bookmarks=projekt_summary_data.get(
            "logik_projekt_config_bookmarks",
            "",
        ),
        logik_projekt_config_workspace=projekt_summary_data.get(
            "logik_projekt_config_workspace",
            ""
        ),
        launch_flame_after_creation=projekt_summary_data.get(
            "launch_flame_after_creation",
            False,
        ),
    )
    projekt_creator.create_projekt(projekt_config)


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
