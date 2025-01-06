"""
Script Name: uc projekt starter
Script Version: 0.1
Flame Version: 2025.1
Written by: John Geehreng
Creation Date: 01.06.25
Update Date: 

Custom Action Type: Projekt Launch

Description:

    Configure Projekt on Launch


Updates:

    v0.1 01.06.25

        Repurpose UC Project Starter for Logik Projekt
"""

#-------------------------------------#
# Imports

import os
import flame
import datetime

#-------------------------------------#
# Main Script

SCRIPT_NAME = 'UC Projekt Starter'
SCRIPT_VERSION = 'v0.1'
SCRIPT_PATH = os.path.abspath(os.path.dirname(__file__))

class ProjectStarter():

    def __init__(self, selection) -> None:

        # Define common variables
        self.project_name = flame.project.current_project.name
        self.project_nickname = flame.project.current_project.nickname
        self.project_file = f"/opt/Autodesk/project/{self.project_name}/setups/tmp/project_starter.txt"
        self.wks = flame.project.current_project.current_workspace
        self.libs = flame.project.current_project.current_workspace.libraries
        self.dsk = flame.project.current_project.current_workspace.desktop
        dateandtime = datetime.datetime.now()
        self.today = (dateandtime.strftime("%Y-%m-%d"))
        self.time = (dateandtime.strftime("%H%M"))

        # Create project file so UC Proect Starter does not run again.
        message = f"{SCRIPT_NAME} was not used for {self.project_name}."
        self.create_project_file(message)

        # Set Default MediaHub Options
        self.set_mediahub_options()

        # Create Desktop, Libraries, Shared Libraries, and Subfolders
        self.create_libraries()
        self.new_conform_desktop()

        
    
    def create_project_file(self,message):
            print ("Creating Project File.")
            # Create this file so the prompt does not show up again.
            f = open(self.project_file, "w")
            f.write(message + '\n')
            f.close()

    def set_mediahub_options(self):
        print("Setting MediaHub Options")
        flame.mediahub.files.options.set_tagged_colour_space("From File or Rules")
        flame.mediahub.files.options.sequence_mode = True
        flame.mediahub.files.options.cache_mode = True
        flame.mediahub.files.options.cache_and_proxies_all_versions = True

    def create_libraries(self):
        # Create Libraries and subfolders
        print ("Creating Libraries.")
        master_lib = self.wks.create_library('MASTERS')
        master_lib.colour = (0.3764706254005432, 0.0470588281750679, 0.0470588281750679)
        
        self.wips_lib = self.wks.create_library('WIPS')
        
        vfx_shots_lib = self.wks.create_library('VFX_SHOTS')
        vfx_shots_lib.colour = (0.26274511218070984, 0.4078431725502014, 0.501960813999176)
        
        audio_lib = self.wks.create_library('AUDIO')
        audio_lib.create_folder(self.today)
        audio_lib.expanded = False

        gfx_lib = self.wks.create_library('GFX')
        gfx_lib.create_folder(self.today)
        gfx_lib.expanded = False
        
        self.slates_lib = self.wks.create_library('SLATES')
        # Wondering if we need shorter slates in a different folder
        slates_folder = '/Volumes/vfx/UC_Jobs/UPPERCUT/FOOTAGE/SLATES/'
        if os.path.isdir(slates_folder):
            slates_list = os.listdir(slates_folder)
            for item in slates_list:
                slate = f"{slates_folder}/{item}"
                flame.import_clips(slate, self.slates_lib)

            # Cache Slates
            for item in self.slates_lib.children:
                try:
                    item.cache_media(mode='current')
                except:
                    print (f"Cannot Cache {item.name}.")
        
        shipping_kit_lib = self.wks.create_library('SHIPPING_KIT')
        shipping_kit_folder = '/Volumes/vfx/UC_Jobs/UPPERCUT/FOOTAGE/SHIPPING_KIT/'
        if os.path.isdir(shipping_kit_folder):
            shipping_kit_list = os.listdir(shipping_kit_folder)
            for guide in shipping_kit_list:
                guide_path = f"{shipping_kit_folder}/{guide}"
                flame.import_clips(guide_path, shipping_kit_lib)

            # Cache Guides
            for item in shipping_kit_lib.children:
                try:
                    item.cache_media(mode='current')
                except:
                    print (f"Cannot Cache {item.name}.")

        vendors_lib = self.wks.create_library('VENDORS')
        vendors_lib.create_folder('OUT').create_folder(self.today)
        vendors_lib.create_folder('IN').create_folder(self.today)
        vendors_lib.expanded = False
        
        footage_lib = self.wks.create_library('FOOTAGE')
        footage_lib.create_folder('GRADE').create_folder(self.today)
        footage_lib.create_folder('RAW').create_folder(self.today)
        footage_lib.create_folder('STOCK').create_folder(self.today)
        footage_lib.create_folder('PREVIOUS_MASTERS').create_folder(self.today)
        footage_lib.create_folder('REFERENCES').create_folder(self.today)
        footage_lib.create_folder('ELEMENTS').create_folder(self.today)
        safety_guides_folder = '/Volumes/vfx/UC_ELEMENTS/SafetyGuides/flame_auto_imports'
        if os.path.isdir(safety_guides_folder):
            safety_guides = footage_lib.create_folder('SAFETY_GUIDES')#.create_folder(self.today)
            
            safety_guides_list = os.listdir(safety_guides_folder)
            for guide in safety_guides_list:
                guide_path = f"{safety_guides_folder}/{guide}"
                flame.import_clips(guide_path, safety_guides)
            # Cache Safety Guides
            for item in safety_guides.children:
                try:
                    item.cache_media(mode='current')
                except:
                    print (f"Cannot Cache {item.name}.")
        footage_lib.expanded = False

        archive_status_lib = self.wks.create_library('NOT_ARCHIVED')
        archive_status_lib.colour = (0.38823533058166504, 0.3176470696926117, 0.5411764979362488)
        archive_status_lib.expanded = False

        # Create Share Libraries
        print ("Creating Shared Libraries.")
        shared_libary_list = ['FROM_FLAME', 'SUPPORT_OUT', "SUPPORT_IN"]
        for item in shared_libary_list:
            shared_lib = flame.project.current_project.create_shared_library(item)
            shared_lib.acquire_exclusive_access()
            shared_lib.create_folder(self.today)
            shared_lib.expanded = False
            shared_lib.release_exclusive_access()

        # Deletes the Default Library:
        for library in self.libs:
            if library.name == "Default Library":
                flame.delete(library)
                print ("Deleted Default Library")

    def new_conform_desktop(self):

        #rename desktop
        self.dsk.name = (f'WIPS_{self.today}')
        
        #create/name schematic reels
        schematicReels = [ 'Plates', 'Elements', 'Ref', 'Pre-Renders']
        #create/name shelf reels
        shelfReels = [ 'Renders']

        #Create batch group with name, start_frame value, duration value, set of schematic reel names, set of shelf reel names
        flame.batch.create_batch_group('QC',
        start_frame = 1001,
        duration = 108,
        reels =  schematicReels,
        shelf_reels = shelfReels )

        #Deletes default batch and reels
        flame.delete(self.dsk.batch_groups[0])

        #Rename Reels
        new_reels = self.dsk.reel_groups[0]
        new_reels.name = 'CONFORMS'
        for reel in new_reels.reels:
            reel_name = str(reel.name)[(1):-(1)]
            reel_name = reel_name.replace("Reel 1", "Temp")
            reel_name = reel_name.replace("Reel 2", "Breakout")
            reel_name = reel_name.replace("Reel 3", "Offlines")
            reel_name = reel_name.replace("Sequences", "CONFORMS")
            reel.name = reel_name
            # Delete the Extra Reels if Preferences aren't set to Reel Group 3
            if reel_name in ['Reel 4', 'Reel 5', 'Reel 6', 'Reel 7', 'Reel 8', 'Reel 9', 'Temp0', 'Temp1', 'Temp2', 'Temp3', 'Temp4', 'Temp5', 'Temp6']:
                flame.delete(reel)
                continue

        #Set View and Current Desktop
        self.wks.set_desktop_reels(self.dsk.reel_groups[0])
        self.wks.current_reel_group = self.dsk.reel_groups[0]

        # Find the WIPS library and set that as the save destination.
        try:
            self.dsk.destination = self.wips_lib
        except:
            print ('Cannot Find WIPS Libray')

            
#-------------------------------------#
# Flame Menus

def app_initialized(selection):
        ProjectStarter(selection)