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

# File Name:        add_backup_script_to_crontab.py
# Version:          1.0.0
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

from PySide6.QtGui import QGuiApplication
from PySide6.QtWidgets import QApplication, QFileDialog, QVBoxLayout, QLineEdit, QLabel, QPushButton, QWidget

# ========================================================================== #
# This section defines the primary functions for the script.
# ========================================================================== #

# Hardcode the path to your shell script here
backup_script_path = "/path/to/your/script.sh"

class CronJobApp(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('Schedule Cron Job')

        layout = QVBoxLayout()

        self.script_label = QLabel(f"Shell script to be scheduled: {backup_script_path}")
        layout.addWidget(self.script_label)


        self.cron_label = QLabel(
            '\n'

            '# ---------------------------------------------------------------- #\n\n'

            '  Cron is a utility that allows you to schedule tasks.\n\n'

            '# ---------------------------------------------------------------- #\n\n'

            '  It is useful for automating repetitive tasks, such as backups,\n'
            '  maintenance, and other system tasks.\n\n'


            '  Crontab defines the schedule using five fields:\n'
            '  minute, hour, day of the month, month, and day of the week.\n\n'

            '  Each field can be a value, a range of values, or a wildcard (*).\n\n'

            '# ---------------------------------------------------------------- #\n\n'

            '  Here is the format of a crontab entry:\n\n'

                '  *     *     *     *     *      command/script.sh >> logfile.log\n'
                '  │     │     │     │     │\n'
                '  │     │     │     │     └────  Day of the Week (0-6)\n'
                '  │     │     │     │\n'
                '  │     │     │     └──────────  Month of the Year (1-12)\n'
                '  │     │     │\n'
                '  │     │     └────────────────  Day of the Month (1-31)\n'
                '  │     │\n'
                '  │     └──────────────────────  Hour (0-23)\n'
                '  │\n'
                '  └────────────────────────────  Minute (0-59)\n\n'

            '# ---------------------------------------------------------------- #\n\n'

            '  Here are some example values:\n\n'

            '  Field                    Value         Description\n'
            '# ---------------------------------------------------------------- #\n'
            '  Day of the Week          0,6           Sunday, Saturday\n'
            '  Month of the Year        */2           Every even numbered month\n'
            '  Day of the Month         1-31          Every day of the month\n'
            '  Hour                     3-6           3 AM to 6 AM\n'
            '  Minute                   */5           Every 5 minutes\n\n'

            '# ---------------------------------------------------------------- #\n\n'

            '  Examples:\n\n'

            '   */5 * * * *  - Every 5 minutes\n'
            '  */30 * * * *  - Every 30 minutes\n'
            '     0 * * * *  - Once per hour\n'
            '     0 0 * * *  - Every day at midnight\n'
            '     0 6 * * 0  - Every Sunday at 06:00\n\n'

            '  Enter your values separated by spaces.\n\n'

            '# ---------------------------------------------------------------- #\n\n'

        )
        layout.addWidget(self.cron_label)

        self.cron_input = QLineEdit()
        layout.addWidget(self.cron_input)

        self.submit_button = QPushButton('Schedule Job')
        self.submit_button.clicked.connect(self.submit_cron_job)
        layout.addWidget(self.submit_button)

        self.setLayout(layout)
        self.center()

    def center(self):
        screen = QGuiApplication.primaryScreen()
        screen_geometry = screen.availableGeometry()
        widget_geometry = self.frameGeometry()
        widget_geometry.moveCenter(screen_geometry.center())
        self.move(widget_geometry.topLeft())

    def submit_cron_job(self):
        cron_time = self.cron_input.text()
        if cron_time:
            create_crontab_entry(backup_script_path, cron_time)
        else:
            print("Please enter a valid cron schedule.")

def create_crontab_entry(script_path, cron_time):
    """Adds a crontab entry to run the specified script at the specified time."""
    cron_command = f"{cron_time} {script_path}"
    subprocess.run(f'(crontab -l; echo "{cron_command}") | crontab -', shell=True, check=True)
    print(f"Crontab entry for {script_path} created successfully.")
    user = os.getlogin()
    cron_file_location = f"/var/spool/cron/crontabs/{user}" if os.name != 'darwin' else f"/var/cron/tabs/{user}"
    print(f"Crontab file location: {cron_file_location}")


# ========================================================================== #
# This section defines the stylesheet.
# ========================================================================== #

# Reduced stylesheet
ProjektStyleSheet = """
/* Set the background color */
QWidget {
    background-color: #242424; /* Replace with your desired color */
}

/* Text color (white) */
QPushButton, QLineEdit, QComboBox {
    color: #ffffff; /* White color */
    font: 14px "monospace Bold"; /* Replace with the actual font name */
}

/* Label text color */
QLabel {
    color: #9F9F9F; /* Label color */
}

/* Font (monospace 14 px) */
QLabel, QPushButton, QLineEdit, QComboBox {
    font: 14px "monospace"; /* Replace with the actual font name */
}

/* Disabled Button color */
QPushButton:disabled {
    background-color: #4D0000; /* Red: #4D0000, Amber: #7F3F00, Green: #2F5F00 */
}

/* Enabled Button Color */
QPushButton {
    background-color: #2F5F00; /* Replace with your desired color */
}

/* Lineedit Text Entry Background */
QLineEdit {
    background-color: #37414b; /* Replace with your desired color */
    padding: 4px;
}

/* Reset QFileDialog to default values */
QFileDialog {
    background-color: #2E2E2E; /* Dark grey background */
    color: #CCCCCC; /* Light grey text */
}

QFileDialog QFrame {
    background-color: #2E2E2E;
    border: 1px solid #444444; /* Slightly lighter grey border */
}

QFileDialog QLabel {
    color: #CCCCCC;
}

QFileDialog QPushButton {
    background-color: #3A3A3A; /* Slightly lighter grey for buttons */
    color: #CCCCCC;
    border: 1px solid #444444;
    padding: 5px;
}

QFileDialog QPushButton:hover {
    background-color: #4A4A4A; /* Slightly lighter on hover */
}

QFileDialog QLineEdit {
    background-color: #3A3A3A;
    color: #CCCCCC;
    border: 1px solid #444444;
}

QFileDialog QListView, QFileDialog QTreeView {
    background-color: #2E2E2E;
    color: #CCCCCC;
    border: 1px solid #444444;
}

QFileDialog QComboBox {
    background-color: #3A3A3A;
    color: #CCCCCC;
    border: 1px solid #444444;
}

QFileDialog QToolButton {
    background-color: #3A3A3A;
    color: #CCCCCC;
    border: 1px solid #444444;
}
"""

# ========================================================================== #
# This section defines how to handle the main script function.
# ========================================================================== #

def apply_stylesheet(app, stylesheet):
    app.setStyleSheet(stylesheet)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    apply_stylesheet(app, ProjektStyleSheet)  # Assuming ProjektStyleSheet is defined
    cron_job_app = CronJobApp()
    cron_job_app.show()
    sys.exit(app.exec())

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
# version:          1.0.0
# created:          2024-09-07 - 18:38:56
# comments:         created GUI and reverted to cron.
# -------------------------------------------------------------------------- #






































# -------------------------------------------------------------------------- #

# File Name:        add_archive_script_to_crontab.py
# Version:          1.0.0
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

from PySide6.QtGui import QGuiApplication
from PySide6.QtWidgets import QApplication, QFileDialog, QVBoxLayout, QLineEdit, QLabel, QPushButton, QWidget

# ========================================================================== #
# This section defines script info, job info & software details.
# ========================================================================== #

# Backup Script Name:  BackupScriptName
# Backup Script for:   BackupScriptProjekt
# Script Creation Date: ScriptCreationDate

the_projekt_name="LogikProjektName"

the_projekt_flame_name="LogikProjektFlameName"

flame_workstation_name="FlameWorkstationName"

# Hardcode the path to your shell script here
backup_script_path = "LogikProjektDirectories/LogikProjektDirectory/flame/backup/backup_scripts/FlameWorkstationName/BackupScriptName"  # TESTING

# Define the path for the cron log file
backup_script_cron_log_path = "LogikProjektDirectories/LogikProjektDirectory/flame/backup/backup_scripts/FlameWorkstationName/cron_log/LogikProjektName_cron_log.log"  # TESTING

# ========================================================================== #
# This section defines the primary functions for the script.
# ========================================================================== #

class CronJobApp(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('Schedule Backup Script Cron Job')

        layout = QVBoxLayout()

        self.script_label = QLabel(
            '  Shell script to be scheduled:\n\n'
            f'  {backup_script_path}\n\n')
        layout.addWidget(self.script_label)

        self.log_label = QLabel(
            '  Cron activity will be logged to:\n\n'
            f'  {backup_script_cron_log_path}\n\n')
        layout.addWidget(self.log_label)

        self.cron_label = QLabel(
            '\n'

            '# ---------------------------------------------------------------- #\n\n'

            '  Cron is a utility that allows you to schedule tasks.\n\n'

            '# ---------------------------------------------------------------- #\n\n'

            '  It is useful for automating repetitive tasks, such as backups,\n'
            '  maintenance, and other system tasks.\n\n'


            '  Crontab defines the schedule using five fields:\n'
            '  minute, hour, day of the month, month, and day of the week.\n\n'

            '  Each field can be a value, a range of values, or a wildcard (*).\n\n'

            '# ---------------------------------------------------------------- #\n\n'

            '  Here is the format of a crontab entry:\n\n'

                '  *     *     *     *     *      command/script.sh >> logfile.log\n'
                '  │     │     │     │     │\n'
                '  │     │     │     │     └────  Day of the Week (0-6)\n'
                '  │     │     │     │\n'
                '  │     │     │     └──────────  Month of the Year (1-12)\n'
                '  │     │     │\n'
                '  │     │     └────────────────  Day of the Month (1-31)\n'
                '  │     │\n'
                '  │     └──────────────────────  Hour (0-23)\n'
                '  │\n'
                '  └────────────────────────────  Minute (0-59)\n\n'

            '# ---------------------------------------------------------------- #\n\n'

            '  Here are some example values:\n\n'

            '  Field                    Value         Description\n'
            '# ---------------------------------------------------------------- #\n'
            '  Day of the Week          0,6           Sunday, Saturday\n'
            '  Month of the Year        */2           Every even numbered month\n'
            '  Day of the Month         1-31          Every day of the month\n'
            '  Hour                     3-6           3 AM to 6 AM\n'
            '  Minute                   */5           Every 5 minutes\n\n'

            '# ---------------------------------------------------------------- #\n\n'

            '  Examples:\n\n'

            '   */5 * * * *  - Every 5 minutes\n'
            '  */30 * * * *  - Every 30 minutes\n'
            '     0 * * * *  - Once per hour\n'
            '     0 0 * * *  - Every day at midnight\n'
            '     0 6 * * 0  - Every Sunday at 06:00\n\n'

            '  Enter your values separated by spaces.\n\n'

            '# ---------------------------------------------------------------- #\n\n'

        )
        layout.addWidget(self.cron_label)

        self.cron_input = QLineEdit()
        self.cron_input.setText("0 * * * *")
        layout.addWidget(self.cron_input)

        self.submit_button = QPushButton('Schedule Backup Script Job')
        self.submit_button.clicked.connect(self.submit_cron_job)
        layout.addWidget(self.submit_button)

        self.setLayout(layout)
        self.center()

    def center(self):
        screen = QGuiApplication.primaryScreen()
        screen_geometry = screen.availableGeometry()
        widget_geometry = self.frameGeometry()
        widget_geometry.moveCenter(screen_geometry.center())
        self.move(widget_geometry.topLeft())

    def submit_cron_job(self):
        cron_time = self.cron_input.text()
        if cron_time:
            create_crontab_entry(backup_script_path, cron_time)
        else:
            print("  Please enter a valid cron schedule.")

def create_crontab_entry(script_path, cron_time):
    """Adds a crontab entry to run the specified script at the specified time and log the activity."""
    # Construct the command to run the script and append output to the log file
    cron_command = f"{cron_time} {script_path} >> {backup_script_cron_log_path} 2>&1"
    
    try:
        # Get existing crontab
        existing_crontab = subprocess.check_output("crontab -l", shell=True, universal_newlines=True)
    except subprocess.CalledProcessError:
        # If there's no existing crontab, start with an empty one
        existing_crontab = ""

    # Append the new command to the existing crontab
    new_crontab = f"{existing_crontab.strip()}\n{cron_command}\n"

    # Write the new crontab
    subprocess.run("crontab -", input=new_crontab, shell=True, check=True, text=True)

    print(f"Crontab entry for {script_path} created successfully.")
    print(f"Cron activity will be logged to: {backup_script_cron_log_path}")
    
    user = os.getlogin()
    cron_file_location = f"/var/spool/cron/{user}" if os.name != 'darwin' else f"/var/cron/tabs/{user}"
    print(f"Crontab file location: {cron_file_location}")

# ========================================================================== #
# This section defines the stylesheet.
# ========================================================================== #

# Reduced stylesheet
ProjektStyleSheet = """
/* Set the background color */
QWidget {
    background-color: #242424; /* Replace with your desired color */
}

/* Text color (white) */
QPushButton, QLineEdit, QComboBox {
    color: #ffffff; /* White color */
    font: 14px "monospace Bold"; /* Replace with the actual font name */
}

/* Label text color */
QLabel {
    color: #9F9F9F; /* Label color */
}

/* Font (monospace 14 px) */
QLabel, QPushButton, QLineEdit, QComboBox {
    font: 14px "monospace"; /* Replace with the actual font name */
}

/* Disabled Button color */
QPushButton:disabled {
    background-color: #4D0000; /* Red: #4D0000, Amber: #7F3F00, Green: #2F5F00 */
}

/* Enabled Button Color */
QPushButton {
    background-color: #2F5F00; /* Replace with your desired color */
}

/* Lineedit Text Entry Background */
QLineEdit {
    background-color: #37414b; /* Replace with your desired color */
    padding: 4px;
}

/* Reset QFileDialog to default values */
QFileDialog {
    background-color: #2E2E2E; /* Dark grey background */
    color: #CCCCCC; /* Light grey text */
}

QFileDialog QFrame {
    background-color: #2E2E2E;
    border: 1px solid #444444; /* Slightly lighter grey border */
}

QFileDialog QLabel {
    color: #CCCCCC;
}

QFileDialog QPushButton {
    background-color: #3A3A3A; /* Slightly lighter grey for buttons */
    color: #CCCCCC;
    border: 1px solid #444444;
    padding: 5px;
}

QFileDialog QPushButton:hover {
    background-color: #4A4A4A; /* Slightly lighter on hover */
}

QFileDialog QLineEdit {
    background-color: #3A3A3A;
    color: #CCCCCC;
    border: 1px solid #444444;
}

QFileDialog QListView, QFileDialog QTreeView {
    background-color: #2E2E2E;
    color: #CCCCCC;
    border: 1px solid #444444;
}

QFileDialog QComboBox {
    background-color: #3A3A3A;
    color: #CCCCCC;
    border: 1px solid #444444;
}

QFileDialog QToolButton {
    background-color: #3A3A3A;
    color: #CCCCCC;
    border: 1px solid #444444;
}
"""

# ========================================================================== #
# This section defines how to handle the main script function.
# ========================================================================== #

def apply_stylesheet(app, stylesheet):
    app.setStyleSheet(stylesheet)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    apply_stylesheet(app, ProjektStyleSheet)  # Assuming ProjektStyleSheet is defined
    cron_job_app = CronJobApp()
    cron_job_app.show()
    sys.exit(app.exec())

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
# version:          1.0.0
# created:          2024-09-07 - 18:38:56
# comments:         created GUI and reverted to cron.
# -------------------------------------------------------------------------- #
