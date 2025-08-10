# Flame Options Data Map

This document analyzes the data fields in the **Flame Options** panel (`RightSubPanelFlameOptions`).

## Overview

This panel allows the user to specify various Flame-related settings, including the software version and key project directory paths. These settings directly influence the environment in which the LOGIK-PROJEKT will be created.

## Related Scripts

* [`src/ui/panels/flame_options_panel.py`](<../src/ui/panels/flame_options_panel.py>)

    * [`src/ui/widgets/combobox/flame_software_choice_widget.py`](<../src/ui/widgets/combobox/flame_software_choice_widget.py>)
    * [`src/ui/widgets/buttons/flame_home_dir_widget.py`](<../src/ui/widgets/buttons/flame_home_dir_widget.py>)
    * [`src/ui/widgets/buttons/flame_setups_dir_widget.py`](<../src/ui/widgets/buttons/flame_setups_dir_widget.py>)
    * [`src/ui/widgets/buttons/flame_media_dir_widget.py`](<../src/ui/widgets/buttons/flame_media_dir_widget.py>)
    * [`src/ui/widgets/buttons/flame_catalog_dir_widget.py`](<../src/ui/widgets/buttons/flame_catalog_dir_widget.py>)
    * [`src/ui/widgets/combobox/projekt_config_widget.py`](<../src/ui/widgets/combobox/projekt_config_widget.py>)

| Field Name / Displayed Field / Label | Widget Class | Variable Name / Key | Is Displayed? | Data Source (Panel & Widget) | JSON Key | Notes |
|---|---|---|---|---|---|---|
| `Software Version:` | `FlameSoftwareChoiceWidget` | `flame_software_choice` | Yes | User Input | Internal Use | Combobox selection for the Flame software version. Data flows to `projekt_summary_data_map.md`. |
| `Flame Home Dir:` | `FlameHomeDirWidget` | `flame_home_directory` | Yes | User Input | Internal Use | Button that opens a directory selection dialog for the Flame project root. Data flows to `projekt_summary_data_map.md`. |
| `Flame Setups Dir:` | `FlameSetupsDirWidget` | `flame_setups_directory` | Yes | User Input / Default from `sysconfig.cfg` | Internal Use | Button that opens a directory selection dialog for the Flame project setups directory. Default value is loaded from `sysconfig.cfg`. |
| `Flame Media Dir:` | `FlameMediaDirWidget` | `flame_media_directory` | Yes | User Input / Default from `sysconfig.cfg` | Internal Use | Button that opens a directory selection dialog for the Flame project media directory. Default value is loaded from `sysconfig.cfg`. |
| `Flame Catalog Dir:` | `FlameCatalogDirWidget` | `flame_catalog_directory` | Yes | User Input / Default from `sysconfig.cfg` | Internal Use | Button that opens a directory selection dialog for the Flame project catalog directory. Default value is loaded from `sysconfig.cfg`. |
| `PROJEKT Config:` | `ProjektConfigWidget` | `logik_projekt_config` | Yes | User Input | Internal Use | Combobox selection for the LOGIK-PROJEKT configuration. Data flows to `projekt_summary_data_map.md`. |