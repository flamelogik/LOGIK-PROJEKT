"""
Script Name: uc projekt metadata
Script Version: 0.0.1
Flame Version: 2025.1
Written by: John Geehreng
Creation Date: 01.13.25
Update Date: 

Custom Action Type: Flame Main Menu

Description:

    Configure Projekt on Launch

Updates:
    01.06.25 - v0.0.1 - Quickly create metadata files for a existing projects.
"""

#-------------------------------------#
# Imports

import os
import flame
import subprocess
from xml.dom.minidom import parse
import xml.etree.ElementTree as ET
import json
import platform
#-------------------------------------#
# Main Script

SCRIPT_NAME = 'UC Projekt Starter'
SCRIPT_VERSION = 'v0.3'
SCRIPT_PATH = os.path.abspath(os.path.dirname(__file__))

class ProjektMetadata():

    def __init__(self, selection) -> None:

        # Define common variables
        # self.simple_flame_version = flame.get_version().split('.')[0]
        # self.full_flame_version = flame.get_version()
        self.project_name = flame.project.current_project.name
        self.project_nickname = flame.project.current_project.nickname
        self.user_name = flame.users.current_user.name
        self.user_nickname = flame.users.current_user.nickname
        self.workstation = platform.node().casefold()
        self.archive_path = f"/PROJEKTS/{self.project_nickname}/DOCS/FLAME_ARCHIVE/{self.workstation}"
        # self.flame_version = flame.get_version()            
        # self.segment_size = 25
        # self.wks = flame.project.current_project.current_workspace
        # self.libs = flame.project.current_project.current_workspace.libraries
        # self.dsk = flame.project.current_project.current_workspace.desktop
        # dateandtime = datetime.datetime.now()
        # self.today = (dateandtime.strftime("%Y-%m-%d"))
        # self.time = (dateandtime.strftime("%H%M"))

        # Define Project File
        self.project_file = f"/PROJEKTS/{self.project_nickname}/DOCS/FLAME_ARCHIVE/flame_project_metadata_{self.workstation}.json"

        # Create Project Metadata Files
        self.create_project_metadata_files()

    def create_project_metadata_files(self):

        temp_xml = "/tmp/temp_output.xml"
        clean_xml = f"/PROJEKTS/{self.project_nickname}/DOCS/FLAME_ARCHIVE/flame_project_metadata_{self.workstation}.xml"
        project_metadata_json = f"/PROJEKTS/{self.project_nickname}/DOCS/FLAME_ARCHIVE/flame_project_metadata_{self.workstation}.json"

        command = [
            "/opt/Autodesk/wiretap/tools/current/wiretap_get_metadata",
            "--host", "127.0.0.1:IFFFS",
            "--nodeid", f"/projects/{self.project_name}",
            "--stream", "xml",
            "--output", temp_xml
        ]

        try:
            # Run the command
            result = subprocess.run(command, check=True, text=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            
            # Print standard error if any
            if result.stderr:
                print("Command Error:")
                print(result.stderr)
                
        except subprocess.CalledProcessError as e:
            print(f"Command failed with return code {e.returncode}")
            print(e.stderr)
            
        # XML Section
        # Parse and pretty-print the XML
        with open(temp_xml, "r") as file:
            dom = parse(file)
            pretty_xml = dom.toprettyxml(indent="  ")

        # Write the formatted XML to a file
        with open(clean_xml, "w") as file:
            file.write(pretty_xml)

        print(f"Formatted XML saved to {clean_xml}")

        # Give the option to Auto Archive or not
        auto_archive_dialogue = flame.messages.show_in_dialog(
        title = f"{SCRIPT_NAME} - {SCRIPT_VERSION}",
        message = 'Would you like to have this project automatically archive?',
        type = "info",
        buttons = ["Yes"],
        cancel_button = "No")

        if auto_archive_dialogue == "Yes":
            self.auto_archive = True
        else:
            self.auto_archive = False

        # JSON Section
        # Parse the XML file
        tree = ET.parse(clean_xml)  # Parses the XML file into an ElementTree object
        root = tree.getroot()      # Gets the root element of the XML tree

        # Extract the desired fields
        json_data = {
            "Name": root.find("Name").text,
            "Nickname": root.find("Nickname").text,
            "CreationDate": root.find("CreationDate").text,
            "ProjectDir": root.find("ProjectDir").text,
            "SetupDir": root.find("SetupDir").text,
            "MediaDir": root.find("MediaDir").text,
            "Version": root.find("Version").text,
        }
        print(f"JSON data extracted from {clean_xml}, {json_data}")
        # Add new fields
        json_data["ProjectDir"] = f"/opt/Autodesk/project/{self.project_name}"
        json_data["AutoArchive"] = self.auto_archive
        json_data["Workstation"] = self.workstation
        json_data["UserName"] = self.user_name
        json_data["UserNickname"] = self.user_nickname
        # print(f"Updated JSON data: {json_data}")

        # Write the JSON to a file
        with open(project_metadata_json, "w") as json_file:
            json.dump(json_data, json_file, indent=4)
            
        print(f"JSON output saved to {project_metadata_json}")

        # Load and check JSON data
        with open(project_metadata_json, "r") as json_file:
            json_data = json.load(json_file)
        # print(json_data)

        # Access specific fields
        name = json_data.get("Name")
        nickname = json_data.get("Nickname")
        flame_version = json_data.get("Version")
        creation_date = json_data.get("CreationDate")
        project_dir = json_data.get("ProjectDir")
        auto_archive = json_data.get("AutoArchive")
        workstation = json_data.get("Workstation")
        user_name = json_data.get("UserName")
        user_nickname = json_data.get("UserNickname")

        # Print the retrieved information
        print('\n')
        print(f"Name: {name}")
        print(f"Nickname: {nickname}")
        print(f"Flame Version: {flame_version}")
        print(f"Creation Date: {creation_date}")
        print(f"Project Directory: {project_dir}")
        print(f"AutoArchive Enabled: {auto_archive}")
        print(f"Workstation: {workstation}")
        print(f"User Name: {user_name}")
        print(f"User Nickname: {user_nickname}", '\n')

#-------------------------------------#
# Scope
def scope_project_metadata_file(selection):
   
    project_nickname = flame.project.current_project.nickname
    workstation = platform.node().casefold()
    project_file = f"/PROJEKTS/{project_nickname}/DOCS/FLAME_ARCHIVE/flame_project_metadata_{workstation}.json"

    # If the file exists, don't show this script
    if os.path.isfile(project_file): 
        return False
    else:
        return True

#-------------------------------------#
# Flame Menus
def get_main_menu_custom_ui_actions():

    return [
        {
            'name': 'UC Job Folder',
            'hierarchy': [],
            'actions': [
                {
                    'name': 'Create Auto Archive Metadata',
                    'execute': ProjektMetadata,
                    'isVisible': scope_project_metadata_file,
                    'minimumVersion': '2025.2',
                    'maximumVersion': '2026'
                }
            ]
        }
    ]