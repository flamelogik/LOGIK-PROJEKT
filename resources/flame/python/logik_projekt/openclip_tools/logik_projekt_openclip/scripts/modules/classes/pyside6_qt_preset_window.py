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

# File Name:        pyside6_qt_preset_window.py
# Version:          0.5.0
# Created:          2024-01-19
# Modified:         2024-08-31

# ========================================================================== #
# This section imports the necessary modules.
# ========================================================================== #

# Standard library imports
import ast
import datetime
import functools
import importlib.util
import os
import re
import shutil
import subprocess
import typing
from typing import (
    Union,
    List,
    Dict,
    Optional,
    Callable
)
import xml
import xml.etree.ElementTree as ET

# Third Party library imports
from PySide6 import (
    QtWidgets,
    QtCore,
    QtGui
)

from pyside6_qt_button import pyside6_qt_button
from pyside6_qt_label import pyside6_qt_label
from pyside6_qt_message_window import pyside6_qt_message_window
from pyside6_qt_push_button_menu import pyside6_qt_push_button_menu
from pyside6_qt_window import pyside6_qt_window

# from ..functions.pyside6_qt_print import pyside6_qt_print

class pyside6_qt_preset_window():
    '''
    Custom Qt Flame Preset Window

    pyside6_qt_preset_window(script_name, script_path, setup_window)

    window_title: Text shown in top left of window [str]
    script_name: Name of script [str]
    script_path: Path to script [str]
    setup_window: Setup window to open

    When creating a new preset, 'new_preset' is sent to the setup_window.
    When editing a preset, the path of the selected preset is sent to the setup window.

    The Save button in the setup window should return the name of the preset as a string.
    The Cancel button in the setup window should return the string 'cancel'

    Preset set as default will show an asterisk (*) next to the preset name.

    Example:

    return pyside6_qt_preset_window(f'{SCRIPT_NAME}: Presets <small>{VERSION}', SCRIPT_NAME, SCRIPT_PATH, UberSaveSetup)
    '''

    def __init__(self, window_title: str, script_name: str, script_path: str, setup_window):
        import flame

        # Check argument types

        if not isinstance(window_title, str):
            raise TypeError('pyside6_qt_preset_window: window_title must be a string')
        if not isinstance(script_name, str):
            raise TypeError('pyside6_qt_preset_window: script_name must be a string')
        elif not isinstance(script_path, str):
            raise TypeError('pyside6_qt_preset_window: script_path must be a string')

        # Set misc variables

        self.default_preset = ''
        self.script_name = script_name
        self.script_path = script_path
        self.setup_window = setup_window

        self.flame_prj_name = flame.project.current_project.project_name
        #print('flame_prj_name:', self.flame_prj_name)

        self.preset_settings_name = self.script_name.lower().replace(' ', '_') + '_preset_settings'
        #print('preset_settings_name:', self.preset_settings_name, '\n')

        # Set paths

        self.preset_config_xml = os.path.join(self.script_path, 'config', 'preset_config.xml')
        self.preset_path = os.path.join(self.script_path, 'config', 'preset')
        self.project_config_path = os.path.join(self.script_path, 'config', 'project')

        # Build window

        grid_layout = QtWidgets.QGridLayout()
        self.preset_window = pyside6_qt_window(window_title, grid_layout, 670, 300)

        # Labels

        self.preset_label = pyside6_qt_label('Current Project Preset', label_type='underline')

        # Shot Name Type Push Button Menu

        preset_list = self.build_preset_list()
        self.current_preset_push_btn = pyside6_qt_push_button_menu('', preset_list)

        #  Buttons
        self.new_btn = pyside6_qt_button('New', self.new_preset, button_width=100)
        self.make_default_btn = pyside6_qt_button('Make Default', self.make_default, button_width=100)
        self.edit_btn = pyside6_qt_button('Edit', self.edit_preset, button_width=100)
        self.rename_btn = pyside6_qt_button('Rename', self.edit_preset, button_width=100)
        self.delete_btn = pyside6_qt_button('Delete', self.delete_preset, button_width=100)
        self.duplicate_btn = pyside6_qt_button('Duplicate', self.duplicate_preset, button_width=100)
        self.set_btn = pyside6_qt_button('Set', self.set, button_width=100)
        self.done_btn = pyside6_qt_button('Done', self.done, button_width=100)

        self.load_current_preset()

        # Preset Window layout

        grid_layout.setContentsMargins(10, 10, 10, 10) # grid_layout.setMargin(10) # Fix for flame 2025

        grid_layout.setRowMinimumHeight(1, 30)

        grid_layout.addWidget(self.preset_label, 4, 0, 1, 4)
        grid_layout.addWidget(self.current_preset_push_btn, 5, 0, 1, 4)

        grid_layout.addWidget(self.new_btn, 5, 5)
        grid_layout.addWidget(self.edit_btn, 6, 5)
        grid_layout.addWidget(self.set_btn, 7, 5)
        grid_layout.addWidget(self.make_default_btn, 5, 6)
        grid_layout.addWidget(self.duplicate_btn, 6, 6)
        grid_layout.addWidget(self.delete_btn, 7, 6)

        grid_layout.setRowMinimumHeight(8, 28)

        grid_layout.addWidget(self.done_btn, 9, 6)

        self.preset_window.setLayout(grid_layout)
        self.preset_window.show()

    def paintEvent(self, event):
        '''
        Add title bar line and side color lines to window
        '''

        painter = QtGui.QPainter(self)

        # Vertical line

        painter.setPen(QtGui.QPen(QtGui.QColor(0, 110, 176), 6, QtCore.Qt.SolidLine))
        painter.drawLine(0, 0, 0, 330)

        # Horizontal line

        painter.setPen(QtGui.QPen(QtGui.QColor(71, 71, 71), .5, QtCore.Qt.SolidLine))
        painter.drawLine(0, 40, 650, 40)

    # For moving frameless window

    def mousePressEvent(self, event):
        self.oldPosition = event.globalPos()

    def mouseMoveEvent(self, event):

        try:
            delta = QtCore.QPoint(event.globalPos() - self.oldPosition)
            self.move(self.x() + delta.x(), self.y() + delta.y())
            self.oldPosition = event.globalPos()
        except:
            pass

    # ----------------------------------------------------------------------------------------------------------------------

    def preset_config(self):
        '''
        Check for default config file and create if it doesn't exist
        '''

        def get_config_values():

            xml_tree = ET.parse(self.preset_config_xml)
            root = xml_tree.getroot()

            # Get Settings

            for setting in root.iter(self.preset_settings_name):
                self.default_preset = setting.find('default_preset').text

            print('default_preset:', self.default_preset, '\n')

            pyside6_qt_print(self.script_name, 'Preset config loaded.')

        def create_config_file():

            if not os.path.exists(self.preset_path):
                try:
                    os.makedirs(self.preset_path)
                    os.makedirs(self.project_config_path)
                except:
                    pyside6_qt_message_window('error', f'{self.script_name}: Error', f'Unable to create folder: {self.preset_path}<br>Check folder permissions')

            if not os.path.isfile(self.preset_config_xml):
                pyside6_qt_print(self.script_name, 'Preset config file not found. Creating new preset config file.')

                config = f"""
<settings>
    <{self.preset_settings_name}>
        <default_preset></default_preset>
    </{self.preset_settings_name}>
</settings>"""

                with open(self.preset_config_xml, 'a') as config_file:
                    config_file.write(config)
                    config_file.close()

        if os.path.isfile(self.preset_config_xml):
            get_config_values()
        else:
            create_config_file()
            if os.path.isfile(self.preset_config_xml):
                get_config_values()

    def load_current_preset(self):
        '''
        Set current preset push button text to default preset unless a project preset is set
        '''

        xml_tree = ET.parse(self.preset_config_xml)
        root = xml_tree.getroot()

        # Get Settings

        for setting in root.iter(self.preset_settings_name):
            self.default_preset = setting.find('default_preset').text

        # If default preset is None and no presets exist in preset folder, set current preset to ''

        if not self.default_preset and len(os.listdir(self.preset_path)) == 0:
            return self.current_preset_push_btn.setText('')

        # If default preset is None and one or more presets exists in preset folder, set current preset to first preset and make that preset the default preset

        if not self.default_preset and len(os.listdir(self.preset_path)) > 0:
            preset_file = os.listdir(self.preset_path)[0]
            preset_file_name = self.get_project_preset_name_xml(os.path.join(self.preset_path, preset_file))
            self.update_default_preset_xml(preset_file_name)
            self.default_preset = preset_file_name

        # Check for existing project preset

        try:
            project_preset = [f[:-4] for f in os.listdir(self.project_config_path) if f[:-4] == self.flame_prj_name][0]
        except:
            project_preset = False

        if project_preset:

            # Get current project preset name from project file

            preset_name = self.get_project_preset_name_xml(os.path.join(self.project_config_path, project_preset + '.xml'))

            if preset_name == self.default_preset:
                preset_name = preset_name + '*'

            self.current_preset_push_btn.setText(preset_name)
        else:
            if os.listdir(self.preset_path):
                self.current_preset_push_btn.setText(self.default_preset + '*')
            else:
                self.current_preset_push_btn.setText('')

        if not os.listdir(self.preset_path):
            return print('No saved presets found.')

        # If preset current project is set to is not found, switch to the default preset and delete the project preset

        if not os.path.isfile(os.path.join(self.preset_path, self.get_current_preset_button() + '.xml')):
            pyside6_qt_message_window('error', f'{self.script_name}: Error', f'Preset file not found: {self.current_preset_push_btn.text()}<br><br>Switching to default preset.')
            self.current_preset_push_btn.setText(self.default_preset + '*')
            os.remove(os.path.join(self.project_config_path, project_preset + '.xml'))

    def build_preset_list(self) -> List[str]:
        '''
        Builds list of presets from preset folder
        '''

        self.preset_config()

        preset_list = []

        for preset in os.listdir(self.preset_path):
            preset = preset[:-4]
            if preset == self.default_preset or len(os.listdir(self.preset_path)) == 1:
                preset = preset + '*'
            preset_list.append(preset)

        preset_list.sort()

        print('preset_list:', preset_list, '\n')

        return preset_list

    def get_current_preset_button(self) -> str:
        '''
        Get current preset button text. Remove '*' if it exists in name.
        '''

        current_preset = self.current_preset_push_btn.text()
        if current_preset.endswith('*'):
            current_preset = current_preset[:-1]

        return current_preset

    def update_current_preset_button(self, preset_name: str=None, preset_is_default: bool=False):
        '''
        Update current preset button text and menu

        preset_name: Preset name that will be shown on Curren Project Preset button. If none is given, first preset in list will be shown.
        preset_is_default: Preset being passed is the default preset. If true, preset will be shown as default preset with an asterisk.
        '''

        preset_list = self.build_preset_list()

        # If preset list is empty, set current preset to empty string and return

        if not preset_list:
            return self.current_preset_push_btn.update_menu('', [])

        # Update Current Project Preset button and menu

        # If preset name is not given, set to first preset in list - for deleting presets
        if not preset_name:
            return self.current_preset_push_btn.update_menu(preset_list[0], preset_list)
        # If preset name returned is cancel, don't update the Current Preset push button
        elif preset_name == 'cancel':
            return
        # If the returned preset name is the same as the default preset add asterisk to the preset name
        elif preset_name == self.default_preset:
            return self.current_preset_push_btn.update_menu(preset_name + '*', preset_list)
        # If only one preset exists in the preset list, that preset is the default. Add asterisk the the name.
        elif preset_name and len(preset_list) == 1:
            return self.current_preset_push_btn.update_menu(preset_name + '*', preset_list)
        elif preset_is_default and not preset_name.endswith('*'):
            return self.current_preset_push_btn.update_menu(preset_name + '*', preset_list)
        return self.current_preset_push_btn.update_menu(preset_name, preset_list)

    def update_default_preset_xml(self, new_default_preset: str):
        '''
        Write new default preset to config file
        '''

        if new_default_preset.endswith('*'):
            new_default_preset = new_default_preset[:-1]

        #print('new_default_preset:', new_default_preset, '\n')

        xml_tree = ET.parse(self.preset_config_xml)
        root = xml_tree.getroot()

        for setting in root.iter(self.preset_settings_name):
            setting.find('default_preset').text = new_default_preset

        xml_tree.write(self.preset_config_xml)

    def save_project_preset_xml(self, preset_path: str, preset_name: str):
        '''
        Update and save project preset xml file with passed preset name
        '''

        # Bypass saving if preset name is 'cancel'. 'cancel' gets passed when the user clicks the cancel button in the setup window.

        if preset_name != 'cancel':

            xml_tree = ET.parse(preset_path)
            root = xml_tree.getroot()

            preset = root.find('.//preset_name')
            preset.text = preset_name

            xml_tree.write(preset_path)

    def create_project_preset_xml(self, preset_name: str, preset_path: str):
            '''
            Create and write new default preset xml file
            '''

            # Create project preset

            preset = f"""
<settings>
    <{self.preset_settings_name}>
        <preset_name></preset_name>
    </{self.preset_settings_name}>
</settings>"""

            with open(preset_path, 'a') as xml_file:
                xml_file.write(preset)
                xml_file.close()

            # Update and save new preset file with current preset name

            self.save_project_preset_xml(preset_path, preset_name)

    def get_project_preset_name_xml(self, project_preset_path: str) -> str:
        '''
        Get name of preset from preset xml
        '''

        script_name = self.script_name.lower().replace(' ', '_')

        # Load settings from project file

        xml_tree = ET.parse(project_preset_path)
        root = xml_tree.getroot()

        # Assign values from config file to variables

        for setting in root.iter(f'{script_name}_preset_settings'):
            preset_name = setting.find('preset_name').text

        return preset_name

    def update_project_presets(self, old_preset_name: str, new_preset_name: str):
        '''
        When changing the name of an existing preset, check all project presets for old preset name. If found, update to new preset name.
        '''

        for project_preset_xml in os.listdir(self.project_config_path):
            project_preset_xml_path = os.path.join(self.project_config_path, project_preset_xml)
            project_preset_name = self.get_project_preset_name_xml(project_preset_xml_path)
            if project_preset_name == old_preset_name:
                self.save_project_preset_xml(project_preset_xml_path, new_preset_name)

        pyside6_qt_print(self.script_name, f'Updated project presets to new preset name: {new_preset_name}')

    # Button actions

    def new_preset(self):
        '''
        Open Setup window with default values.
        Sends string 'new preset' to Setup window.
        Setup window should return preset name as string.
        Setup window cancel button should return 'cancel'.
        Current Project Preset button will be updated with new preset name.
        '''

        pyside6_qt_print(self.script_name, 'Creating new preset.')

        # Hide preset window while creating new preset

        self.preset_window.hide()
        print('preset_window hidden')
        # Load Setup window passing 'new preset' as string

        preset_name = str(self.setup_window('new_preset'))

        # Restore preset window after creating new preset

        self.preset_window.show()
        print('preset_window shown')
        # Refresh current preset button and menu

        self.update_current_preset_button(preset_name)

    def edit_preset(self):
        '''
        Open Setup window with selected preset loaded.
        Sends selected preset xml path to Setup window.
        Setup window should return preset name as string.
        Setup window cancel button should return 'cancel'.
        '''

        # Edit preset returns preset path

        if self.current_preset_push_btn.text():

            preset = self.get_current_preset_button()

            full_preset_path = os.path.join(self.preset_path, preset + '.xml')

            pyside6_qt_print(self.script_name, f'Editing preset: {preset}')

            # Hide preset window while creating new preset

            self.preset_window.hide()

            preset_name = str(self.setup_window(full_preset_path))

            # Restore preset window after creating new preset

            self.preset_window.show()

            # If preset name is changed during edit, update all project presets using preset with new preset name

            if preset != preset_name:
                self.update_project_presets(preset, preset_name)

            self.update_current_preset_button(preset_name)

    def make_default(self):
        '''
        Set current preset as default preset.
        Default preset is shown with an asterisk.
        '''

        if self.current_preset_push_btn.text():

            # Set default preset in preset config xml

            self.update_default_preset_xml(self.current_preset_push_btn.text())

            # Update push button text and list

            self.update_current_preset_button(self.current_preset_push_btn.text(), preset_is_default=True)

            pyside6_qt_print(self.script_name, f'Default preset set to: {self.current_preset_push_btn.text()}')

    def duplicate_preset(self):
        '''
        Create duplicate of currently selected preset. Add copy to end of preset name.
        '''

        if self.current_preset_push_btn.text():

            current_preset = self.get_current_preset_button()

            # Add 'copy' to the end of the new file being created.

            existing_presets = [f[:-4] for f in os.listdir(self.preset_path)]

            new_preset_name = current_preset

            while new_preset_name in existing_presets:
                new_preset_name = new_preset_name  + ' copy'

            # Duplicate preset

            source_file = os.path.join(self.preset_path, current_preset + '.xml')
            dest_file = os.path.join(self.preset_path, new_preset_name + '.xml')
            shutil.copyfile(source_file, dest_file)

            # Save new preset name to duplicate preset xml file

            xml_tree = ET.parse(dest_file)
            root = xml_tree.getroot()

            preset_name = root.find('.//preset_name')
            preset_name.text = new_preset_name

            xml_tree.write(dest_file)

            # Update current preset push button

            self.update_current_preset_button(new_preset_name)

            pyside6_qt_print(self.script_name, f'Preset duplicate created: {new_preset_name}')

    def delete_preset(self):
        '''
        Delete curretly selected preset
        '''

        if self.current_preset_push_btn.text():

            preset_name = self.current_preset_push_btn.text()
            preset_path = os.path.join(self.preset_path, preset_name + '.xml')

            # If selected preset it the default preset, confirm that the user wants to delete it.
            # If confirmed, the default preset is set to the first preset in the list.

            if preset_name.endswith('*'):
                if pyside6_qt_message_window('warning', f'{self.script_name}: Confirm Operation', 'Selected preset is currently the default preset.<br><br>Deleting this preset will set the default preset to the next preset in the list.<br><br>Are you sure you want to delete this preset?'):

                    # If confirmed, delete preset

                    os.remove(os.path.join(self.preset_path, self.get_current_preset_button() + '.xml'))

                    # Update preset config xml with new default preset

                    if os.listdir(self.preset_path):
                        new_preset = str(os.listdir(self.preset_path)[0])[:-4]
                    else:
                        new_preset = ''
                    print(f'new_preset: {new_preset}')
                    self.update_default_preset_xml(new_preset)

                    # Update current preset push button

                    return self.update_current_preset_button(preset_is_default=True)
                else:
                    return

            # Check all project config files for current preset before deleting.
            # If the preset exists in other project files, delete project files. Confirm first.

            def check_for_project_files():

                preset_names = []

                if os.listdir(self.project_config_path):
                    for n in os.listdir(self.project_config_path):
                        saved_preset_name = self.get_project_preset_name_xml(os.path.join(self.project_config_path, n))
                        preset_names.append(saved_preset_name)

                return preset_names

            # Check for project preset files, if they exitst, get names of presets in project files.

            preset_names = check_for_project_files()

            # If project presets exist, check preset names for preset being deleted.

            if preset_names:

                # If preset exists in other project configs, confirm deletion

                if preset_name in preset_names:
                    if pyside6_qt_message_window('warning', f'{self.script_name}: Confirm Operation', 'Selected preset is used by other projects. Deleting this preset will delete it for the other projects and set those projects to the Default preset. Continue?'):
                        os.remove(preset_path)
                    else:
                        return
                else:
                    # If preset is not found in any projects, delete. Confirm first.

                    if pyside6_qt_message_window('warning', f'{self.script_name}: Confirm Operation', f'Delete Preset: <b>{preset_name}'):
                        os.remove(preset_path)
                    else:
                        return

            else:
                # If no project configs exist, delete preset. Confirm first.

                if pyside6_qt_message_window('warning', f'{self.script_name}: Confirm Operation', f'Delete Preset: <b>{preset_name}'):
                    os.remove(preset_path)
                else:
                    return

            # Update push button text and list
            print('lfkdflkl666')
            self.update_current_preset_button()

            pyside6_qt_print(self.script_name, f'Preset deleted: {preset_name}')

    def set(self):
        '''
        Set current preset as current project preset.
        Creates a new project preset file.
        '''

        if self.current_preset_push_btn.text():

            # Get current preset button name

            preset_name_text = self.get_current_preset_button()

            # Create new preset xml path

            preset_path = os.path.join(self.project_config_path, self.flame_prj_name + '.xml')

            if preset_name_text != self.default_preset:

                # If project preset already exists, delete it before creating new one.

                if os.path.isfile(preset_path):
                    os.remove(preset_path)

                # Create project preset

                self.create_project_preset_xml(preset_name_text, preset_path)

            else:
                try:
                    os.remove(preset_path)
                except:
                    pass

            pyside6_qt_message_window('message', f'{self.script_name}: Preset Set', f'Uber Save preset set for this project: {preset_name_text}')

    def done(self):
        '''
        Close preset window
        '''

        # Save default preset to default preset xml file

        preset_list = self.build_preset_list()
        for preset in preset_list:
            if preset.endswith('*'):
                self.update_default_preset_xml(preset)

        # Close preset window

        self.preset_window.close()

        pyside6_qt_print(self.script_name, 'Done.')

# ========================================================================== #
# This section defines how to handle the main script function.
# ========================================================================== #

# # If this script is executed as main:
# # Call functions for immediate execution
# if __name__ == "__main__":

# ========================================================================== #
# C2 A9 32 30 32 34 2D 4D 41 4E 5F 4D 41 44 45 2D 4D 45 4B 41 4E 49 53 4D 5A #
# ========================================================================== #

# Changelist:

# -------------------------------------------------------------------------- #
# version:               0.0.1
# modified:              2024-05-07 - 21:48:20
# comments:              Refactored monolithic code to discreet modules
# -------------------------------------------------------------------------- #
# version:               0.0.2
# modified:              2024-05-07 - 21:49:31
# comments:              Added docstrings
# -------------------------------------------------------------------------- #
# version:               0.0.3
# modified:              2024-05-07 - 21:50:00
# comments:              Prep for initial production test
# -------------------------------------------------------------------------- #
# version:               0.0.4
# modified:              2024-05-09 - 13:18:47
# comments:              Refactored code works in flame 2025. Time to tidy up.
# -------------------------------------------------------------------------- #
# version:               0.0.5
# modified:              2024-05-17 - 13:36:42
# comments:              Replaced FlameButton with pyside6_qt_button
# -------------------------------------------------------------------------- #
# version:               0.0.6
# modified:              2024-05-17 - 13:37:49
# comments:              Replaced FlameClickableLineEdit with pyside6_qt_clickable_line_edit
# -------------------------------------------------------------------------- #
# version:               0.0.7
# modified:              2024-05-17 - 13:38:19
# comments:              Replaced FlameLabel with pyside6_qt_label
# -------------------------------------------------------------------------- #
# version:               0.0.8
# modified:              2024-05-17 - 13:38:29
# comments:              Replaced FlameLineEdit with pyside6_qt_line_edit
# -------------------------------------------------------------------------- #
# version:               0.0.9
# modified:              2024-05-17 - 13:39:27
# comments:              Replaced FlameListWidget with pyside6_qt_list_widget
# -------------------------------------------------------------------------- #
# version:               0.1.0
# modified:              2024-05-17 - 13:39:47
# comments:              Replaced FlameMessageWindow with pyside6_qt_message_window
# -------------------------------------------------------------------------- #
# version:               0.1.1
# modified:              2024-05-17 - 13:40:01
# comments:              Replaced FlamePasswordWindow with pyside6_qt_password_window
# -------------------------------------------------------------------------- #
# version:               0.1.2
# modified:              2024-05-17 - 13:40:28
# comments:              Replaced FlamePresetWindow with pyside6_qt_preset_window
# -------------------------------------------------------------------------- #
# version:               0.1.3
# modified:              2024-05-17 - 13:40:37
# comments:              Replaced FlameProgressWindow with pyside6_qt_progress_window
# -------------------------------------------------------------------------- #
# version:               0.1.4
# modified:              2024-05-17 - 13:41:39
# comments:              Replaced FlamePushButton with pyside6_qt_push_button
# -------------------------------------------------------------------------- #
# version:               0.1.5
# modified:              2024-05-17 - 13:41:49
# comments:              Replaced FlamePushButtonMenu with pyside6_qt_push_button_menu
# -------------------------------------------------------------------------- #
# version:               0.1.6
# modified:              2024-05-17 - 13:42:30
# comments:              Replaced FlameQDialog with pyside6_qt_qdialog
# -------------------------------------------------------------------------- #
# version:               0.1.7
# modified:              2024-05-17 - 13:44:20
# comments:              Replaced FlameSlider with pyside6_qt_slider
# -------------------------------------------------------------------------- #
# version:               0.1.8
# modified:              2024-05-17 - 13:44:30
# comments:              Replaced FlameTextEdit with pyside6_qt_text_edit
# -------------------------------------------------------------------------- #
# version:               0.1.9
# modified:              2024-05-17 - 13:44:39
# comments:              Replaced FlameTokenPushButton with pyside6_qt_token_push_button
# -------------------------------------------------------------------------- #
# version:               0.2.0
# modified:              2024-05-17 - 13:45:12
# comments:              Replaced FlameTreeWidget with pyside6_qt_tree_widget
# -------------------------------------------------------------------------- #
# version:               0.2.1
# modified:              2024-05-17 - 13:45:29
# comments:              Replaced FlameWindow with pyside6_qt_window
# -------------------------------------------------------------------------- #
# version:               0.2.2
# modified:              2024-05-17 - 13:45:43
# comments:              Replaced pyflame_file_browser with pyside6_qt_file_browser
# -------------------------------------------------------------------------- #
# version:               0.2.3
# modified:              2024-05-17 - 13:47:07
# comments:              Replaced pyflame_get_flame_version with pyside6_qt_get_flame_version
# -------------------------------------------------------------------------- #
# version:               0.2.4
# modified:              2024-05-17 - 13:47:43
# comments:              Replaced pyflame_get_shot_name with pyside6_qt_get_shot_name
# -------------------------------------------------------------------------- #
# version:               0.2.5
# modified:              2024-05-17 - 13:47:56
# comments:              Replaced pyflame_load_config with pyside6_qt_load_config
# -------------------------------------------------------------------------- #
# version:               0.2.6
# modified:              2024-05-17 - 13:49:42
# comments:              Replaced pyflame_open_in_finder with pyside6_qt_open_in_finder
# -------------------------------------------------------------------------- #
# version:               0.2.7
# modified:              2024-05-17 - 13:49:51
# comments:              Replaced pyflame_print with pyside6_qt_print
# -------------------------------------------------------------------------- #
# version:               0.2.8
# modified:              2024-05-17 - 13:50:00
# comments:              Replaced pyflame_refresh_hooks with pyside6_qt_refresh_hooks
# -------------------------------------------------------------------------- #
# version:               0.2.9
# modified:              2024-05-17 - 13:50:10
# comments:              Replaced pyflame_resolve_path_tokens with pyside6_qt_resolve_path_tokens
# -------------------------------------------------------------------------- #
# version:               0.3.0
# modified:              2024-05-17 - 13:50:21
# comments:              Replaced pyflame_resolve_shot_name with pyside6_qt_resolve_shot_name
# -------------------------------------------------------------------------- #
# version:               0.3.1
# modified:              2024-05-17 - 13:50:32
# comments:              Replaced pyflame_save_config with pyside6_qt_save_config
# -------------------------------------------------------------------------- #
# version:               0.3.2
# modified:              2024-05-17 - 15:16:41
# comments:              Replaced pyside6_qt_textedit with pyside6_qt_text_edit
# -------------------------------------------------------------------------- #
# version:               0.3.3
# modified:              2024-05-17 - 15:48:00
# comments:              Replaced pyside6_qt_push_buttonMenu with pyside6_qt_push_button_menu
# -------------------------------------------------------------------------- #
# version:               0.4.3
# modified:              2024-05-18 - 18:00:39
# comments:              Added GNU GPLv3 Disclaimer.
# -------------------------------------------------------------------------- #
# version:               0.4.4
# modified:              2024-05-18 - 18:46:09
# comments:              Minor modification to Disclaimer.
# -------------------------------------------------------------------------- #
# version:               0.4.5
# modified:              2024-06-04 - 17:38:52
# comments:              Added 'Smart Replace' option for render and write nodes
# -------------------------------------------------------------------------- #
# version:               0.4.6
# modified:              2024-06-05 - 19:30:33
# comments:              Added a new script to create openclip multichannel
# -------------------------------------------------------------------------- #
# version:               0.4.7
# modified:              2024-06-05 - 21:08:34
# comments:              Modified note strings
# -------------------------------------------------------------------------- #
# version:               0.4.8
# modified:              2024-06-26 - 22:31:48
# comments:              Fixed missing import statements for pyside6_qt_label
# -------------------------------------------------------------------------- #
# version:               0.4.8
# modified:              2024-07-11 - 08:39:06
# comments:              Added new schematic reels for batch groups
# -------------------------------------------------------------------------- #
# version:               0.4.9
# modified:              2024-07-11 - 08:41:36
# comments:              Fixed a version bug for the changelist updater script
# -------------------------------------------------------------------------- #
# version:               0.5.0
# modified:              2024-08-31 - 18:26:05
# comments:              prep for release.
# -------------------------------------------------------------------------- #
