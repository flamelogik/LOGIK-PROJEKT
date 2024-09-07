#

# -------------------------------------------------------------------------- #

# DISCLAIMER:       This file is part of LOGIK-PROJEKT.
#                   Copyright © 2024 man-made-mekanyzms
                
#                   LOGIK-PROJEKT creates directories, files, scripts & tools
#                   for use with Autodesk Flame and other software.

#                   LOGIK-PROJEKT is free software.

#                   You can redistribute it and/or modify it under the terms
#                   of the GNU General Public License as published by the
#                   Free Software Foundation, either version 3 of the License,
#                   or any later version.
 
#                   This program is distributed in the hope that it will be
#                   useful, but WITHOUT ANY WARRANTY; without even the
#                   implied warranty of MERCHANTABILITY or FITNESS FOR A
#                   PARTICULAR PURPOSE.

#                   See the GNU General Public License for more details.

#                   You should have received a copy of the GNU General
#                   Public License along with this program.

#                   If not, see <https://www.gnu.org/licenses/>.
                
#                   Contact: phil_man@mac.com

# -------------------------------------------------------------------------- #

# File Name:        add_scripts_to_crontab.py
# Version:          0.9.9
# Created:          2024-01-19
# Modified:         2024-09-07

# ========================================================================== #
# This section defines the import statements and path setup.
# ========================================================================== #

# Standard library imports
import os
import subprocess
import sys

# -------------------------------------------------------------------------- #

from PySide6.QtWidgets import QApplication, QFileDialog, QVBoxLayout, QLineEdit, QLabel, QPushButton, QWidget

# ========================================================================== #
# This section defines the primary functions for the script.
# ========================================================================== #

class CronJobApp(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('Add Scripts to Crontab')

        layout = QVBoxLayout()

        self.script_label = QLabel('Select the shell script:')
        layout.addWidget(self.script_label)

        self.script_button = QPushButton('Browse...')
        self.script_button.clicked.connect(self.select_script)
        layout.addWidget(self.script_button)

        self.cron_label = QLabel('Enter the cron time (Minute Hour Day_of_Month Month Day_of_Week):')
        layout.addWidget(self.cron_label)

        self.cron_input = QLineEdit()
        layout.addWidget(self.cron_input)

        self.submit_button = QPushButton('Add to Crontab')
        self.submit_button.clicked.connect(self.submit_cron_job)
        layout.addWidget(self.submit_button)

        self.setLayout(layout)

    def select_script(self):
        script_path, _ = QFileDialog.getOpenFileName(self, "Select the shell script")
        if script_path:
            self.script_label.setText(f'Selected script: {script_path}')
            self.script_path = script_path

    def submit_cron_job(self):
        cron_time = self.cron_input.text()
        if hasattr(self, 'script_path') and cron_time:
            if sys.platform == "darwin":
                create_launchd_entry(self.script_path, cron_time)
            else:
                create_crontab_entry(self.script_path, cron_time)
        else:
            print("Please select a script and enter a valid cron time.")

def create_crontab_entry(script_path, cron_time):
    """Adds a crontab entry to run the specified script at the specified time.

    Args:
        script_path (str): The path to the script to be run.
        cron_time (str): The cron time expression at which the script should be run.

    Returns:
        None

    Raises:
        subprocess.CalledProcessError: If the crontab command fails.

    Example:
        create_crontab_entry("/path/to/script.sh", "0 0 * * *")
    """
    cron_command = f"{cron_time} {script_path}"
    subprocess.run(f'(crontab -l; echo "{cron_command}") | crontab -', shell=True, check=True)
    print(f"Crontab entry for {script_path} created successfully.")
    user = os.getlogin()
    cron_file_location = f"/var/spool/cron/crontabs/{user}" if os.name != 'darwin' else f"/var/cron/tabs/{user}"
    print(f"Crontab file location: {cron_file_location}")

def create_launchd_entry(script_path, cron_time):
    """Adds a launchd entry to run the specified script at the specified time.

    Args:
        script_path (str): The path to the script to be run.
        cron_time (str): The cron time expression at which the script should be run.

    Returns:
        None
    """
    plist_file = os.path.expanduser(f"~/Library/LaunchAgents/com.example.{os.path.basename(script_path)}.plist")
    start_interval = int(cron_time.split()[0]) * 60  # Assuming cron_time is in the format "*/N * * * *"
    plist_content = f"""
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
    <key>Label</key>
    <string>com.example.{os.path.basename(script_path)}</string>
    <key>ProgramArguments</key>
    <array>
        <string>/bin/bash</string>
        <string>{script_path}</string>
    </array>
    <key>StartInterval</key>
    <integer>{start_interval}</integer>
    <key>StandardOutPath</key>
    <string>{os.path.expanduser('~/Library/Logs/com.example.' + os.path.basename(script_path) + '.log')}</string>
    <key>StandardErrorPath</key>
    <string>{os.path.expanduser('~/Library/Logs/com.example.' + os.path.basename(script_path) + '.log')}</string>
</dict>
</plist>
"""
    with open(plist_file, "w") as f:
        f.write(plist_content)
    subprocess.run(["launchctl", "load", plist_file], check=True)
    print(f"Launchd entry for {script_path} created successfully.")

def add_editor_to_zshrc():
    """Adds 'export EDITOR=pico' to ~/.zshrc if the operating system is Darwin (macOS)."""
    if sys.platform == "darwin":
        zshrc_path = os.path.expanduser("~/.zshrc")
        with open(zshrc_path, "a") as zshrc_file:
            zshrc_file.write("\nexport EDITOR=pico\n")
        print("'export EDITOR=pico' added to ~/.zshrc")

def create_removal_script(script_path, cron_time):
    """Creates a Python script to remove the process from either cron or launchd.

    Args:
        script_path (str): The path to the script to be removed.
        cron_time (str): The cron time expression at which the script is scheduled.

    Returns:
        None
    """
    removal_script_path = os.path.expanduser("~/remove_scheduled_task.py")
    with open(removal_script_path, "w") as f:
        f.write(f"""
import os
import subprocess
import sys

def remove_crontab_entry(script_path):
    cron_command = f"{cron_time} {script_path}"
    subprocess.run(f'(crontab -l | grep -v "{cron_command}") | crontab -', shell=True, check=True)
    print(f"Crontab entry for {script_path} removed successfully.")

def remove_launchd_entry(script_path):
    plist_file = os.path.expanduser(f"~/Library/LaunchAgents/com.example.{os.path.basename(script_path)}.plist")
    subprocess.run(["launchctl", "unload", plist_file], check=True)
    os.remove(plist_file)
    print(f"Launchd entry for {script_path} removed successfully.")

if __name__ == "__main__":
    if sys.platform == "darwin":
        remove_launchd_entry("{script_path}")
    else:
        remove_crontab_entry("{script_path}")
""")
    print(f"Removal script created at {removal_script_path}")

# ========================================================================== #
# This section defines how to handle the main script function.
# ========================================================================== #

if __name__ == "__main__":
    path_to_shell_script = "/path/to/script.sh"
    process_frequency = "*/5 * * * *"

    add_editor_to_zshrc()
    app = QApplication(sys.argv)
    cron_job_app = CronJobApp()
    cron_job_app.show()
    sys.exit(app.exec())

    create_removal_script(path_to_shell_script, process_frequency)

# ========================================================================== #
# C2 A9 32 30 32 34 2D 4D 41 4E 2D 4D 41 44 45 2D 4D 45 4B 41 4E 59 5A 4D 53 #
# ========================================================================== #

# Changelist:       

# -------------------------------------------------------------------------- #
# version:          0.0.1
# created:          2024-01-19 - 12:34:56
# comments:         scripts to create flame projekts, presets & templates.
# -------------------------------------------------------------------------- #
# version:          0.1.0
# modified:         2024-04-20 - 16:20:00
# comments:         refactored monolithic program into separate functions.
# -------------------------------------------------------------------------- #
# version:          0.5.0
# modified:         2024-05-24 - 20:24:00
# comments:         merged flame_colortoolkit with projekt.
# -------------------------------------------------------------------------- #
# version:          0.6.0
# modified:         2024-05-25 - 15:00:03
# comments:         started conversion to python3.
# -------------------------------------------------------------------------- #
# version:          0.7.0
# modified:         2024-06-21 - 18:21:03
# comments:         started gui design with pyside6.
# -------------------------------------------------------------------------- #
# version:          0.9.9
# created:          2024-09-07 - 10:38:56
# comments:         added launchd option and removal script.
# -------------------------------------------------------------------------- #
