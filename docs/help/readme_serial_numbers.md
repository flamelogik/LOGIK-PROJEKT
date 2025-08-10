# Automated Serial Number Generation

This guide explains how to activate the automated serial number feature for LOGIK-PROJEKT. By default, this feature is **disabled**, and serial numbers must be typed in manually.

Following these steps will change the UI to have a "Get Next Serial" button and will automate the number generation based on a configuration file you can control.

## Activation Guide

### Step 1: Create New Files

You will need to create three new files. Copy the contents provided below into the correct locations.

**File 1: The Serial Number Engine**
- **Location:** `src/core/utils/serial_number_generator.py`
- **Content:**
  ```python
  """
  Serial Number Engine for LOGIK-PROJEKT.

  Reads a configuration file to determine how to generate the next
  available serial number.
  """
  import json
  import os
  from datetime import datetime

  CONFIG_PATH = "cfg/site-cfg/logik-projekt-cfg/serial_number_config.json"

  def get_next_serial() -> str:
      """
      Generates the next serial number based on the mode in the config file.

      Returns:
          str: The next serial number.

      Raises:
          Exception: If the mode is invalid or files cannot be read/written.
      """
      if not os.path.exists(CONFIG_PATH):
          raise FileNotFoundError(f"Configuration file not found at: {CONFIG_PATH}")

      with open(CONFIG_PATH, 'r') as f:
          config = json.load(f)

      mode = config.get("mode", "manual")

      if mode == "manual":
          raise ValueError("System is in 'manual' mode. Cannot generate a serial.")

      elif mode == "file":
          settings = config["file_mode_settings"]
          path = settings["path"]
          padding = settings.get("padding", 4)
          prefix = settings.get("prefix", "")

          if not os.path.exists(path):
              raise FileNotFoundError(f"Serial number file not found at: {path}")

          with open(path, 'r+') as f:
              data = json.load(f)
              last_used = int(data["last_used"])
              next_serial_num = last_used + 1
              data["last_used"] = next_serial_num
              f.seek(0)
              json.dump(data, f, indent=2)
              f.truncate()

          return f"{prefix}{str(next_serial_num).zfill(padding)}"

      elif mode == "date":
          settings = config["date_mode_settings"]
          date_format = settings.get("format", "%Y%m%d")
          return datetime.now().strftime(date_format)

      else:
          raise ValueError(f"Invalid mode '{mode}' in {CONFIG_PATH}")

  ```

**File 2: The Configuration File**
- **Location:** `cfg/site-cfg/logik-projekt-cfg/serial_number_config.json`
- **Content:**
  ```json
  {
    "//": "--- SERIAL NUMBER SETTINGS ---",
    "//": "To enable automation, change 'mode' to 'file' or 'date'.",
    "mode": "manual",

    "file_mode_settings": {
      "//": "Settings for when 'mode' is 'file'.",
      "path": "pref/site-prefs/logik-projekt-site-prefs/last_serial.json",
      "padding": 4,
      "prefix": "PROJ_"
    },

    "date_mode_settings": {
      "//": "Settings for when 'mode' is 'date'.",
      "//": "Use standard date formatting codes (e.g., %Y-%m-%d, %y%m%d).",
      "format": "%y%m%d"
    }
  }
  ```

**File 3: The Last Used Serial Number Tracker**
- **Location:** `pref/site-prefs/logik-projekt-site-prefs/last_serial.json`
- **Content:**
  ```json
  {
    "last_used": 0
  }
  ```

### Step 2: Modify the UI Panel

You need to edit one existing Python file to add the button and connect it to the engine.

- **File to Edit:** `src/ui/panels/template_info_panel.py`

**1. Add Imports:**
At the top of the file, add these new import statements:
```python
from PySide6.QtWidgets import QPushButton, QMessageBox
from src.core.utils import serial_number_generator
```

**2. Modify `_create_widgets`:**
Find the `_create_widgets` method. Change the line where `self.serial_number_widget` is created and add a new button.
- **REMOVE THIS LINE:**
  ```python
  self.layout.addWidget(self.serial_number_widget.entry, row, 1)
  ```
- **ADD THESE LINES in its place:**
  ```python
  self.serial_number_widget.entry.setReadOnly(True)
  serial_layout = QHBoxLayout()
  self.get_serial_button = QPushButton("Get Next Serial")
  serial_layout.addWidget(self.serial_number_widget.entry)
  serial_layout.addWidget(self.get_serial_button)
  self.layout.addLayout(serial_layout, row, 1)
  ```

**3. Modify `_connect_signals`:**
Find the `_connect_signals` method and add this new line to connect the button's click action:
```python
self.get_serial_button.clicked.connect(self._get_next_serial_number)
```

**4. Add New Method:**
At the end of the file (before `get_template_info`), add this new method to handle the button click:
```python
def _get_next_serial_number(self):
    """Fetch the next serial number from the engine and update the UI."""
    try:
        next_serial = serial_number_generator.get_next_serial()
        self.serial_number_widget.set(next_serial)
    except Exception as e:
        QMessageBox.warning(self, "Serial Number Error", str(e))
```

### Step 3: Activate a Mode

To turn the automation on, edit `cfg/site-cfg/logik-projekt-cfg/serial_number_config.json` and change the `"mode"` from `"manual"` to either `"file"` or `"date"`.

Once you restart the application, the "Get Next Serial" button will be active and will populate the serial number field automatically.
