___
# [LOGIK-PROJEKT](https://github.com/flamelogik/LOGIK-PROJEKT)
Projekt Creation, Workflow & LifeCycle Management for Autodesk Flame.
___
LOGIK-PROJEKT was developed with Autodesk Flame 2025, Python 3.11, and PySide 6.
___
### Requirements:
* [Autodesk Flame 2025](https://help.autodesk.com/view/FLAME/2025/ENU/)
* /PROJEKTS - (root level symbolic link to storage)
___
### Useful Software:
* [Microsoft VisualStudio Code](https://code.visualstudio.com/Download)
* [GitHub Desktop](https://desktop.github.com/download/)
___
### Installation Checklist:

Setting up the /PROJEKTS directory:
1. check flame installation
2. check “stonefs” (Autodesk setup app) existence - the stone NEEDS to be called stonefs (for now)
3. symlink ‘/PROJEKTS’ to your storagepico (or vi or vim) /etc/synthetic.conf (as root) and reboot
4. mkdir -p -m 777 /PROJEKTS/test (this may not show up as drwxrwxrwx depending on underlying infrastructure)

Mac OS Pre-Start checklist:
Make sure the following are all enabled in the System Preferences/Privacy & Security/Full Disk Access/

- [ ] wiretapgateway 
- [ ] ifffsWiretapServer 
- [ ] Visual Code
- [ ] swdb
- [ ] sw_dbd
- [ ] sw_serverd
- [ ] DLmpd
- [ ] Flame

Set Flame Preferences:
User Tokens tab
Make sure the username and nickname are there

Timeline tab
Default Shot Name
<name>_<background segment###>0

Batch&BFX Tab
Default batch iteration name
<batch name>_v<iteration####>_<workstation>_<user nickname>

Media Panel Tab
Batch shelf 1
Reel Group 2
Show Batch iterations (first column) 
Desktop Column: Set to “Copy From/To Batch”




Creating a PROJEKT for the first time (no UI)
1. download your repo form GitHub.
2. check your repo in vscode or pycharm
3. run /create_logik_projekt/create_logik_projekt.sh
4. on first run answer ’N’ to say you don’t have a projekt template
5. assign ‘test’ to client name
6. assign ‘test’ to campaign name
7. choose resolution
8. choose frame rate
9. choose bit depth
10. choose color science
11. press enter to launch flame or escape to cancel
12. if you press enter, flame will launch with the newly defined project (-J option)
13. it will create a workspace with the name of your workstation
14. it will create the library layout with the create_layout python script
15. save flame
16. quit flame
17. create the first archive:/PROJEKTS/test_test/flame/archives/test_test_2025_my_workstation.sh
18. create the first rsync backup:/PROJEKTS/test_test/backup_scripts/test_test_*.sh
19. you can exclude directories from the rsync by modifying the exclusion_list file
20. When you are RESTORING ARCHIVEs make sure you’re using the “Convert to Local” Path






Conform

What’s going to happen:
Tell Flame what the sequence is going to be (bring in the metadata - XML, AAF, EDL, etc)
Tell Flame where the footage is - start with the camera raw preferably to get the most metadata
Organize the footage in the timeline by setting the resolution, color science and naming things
Make governing timelines - Sources Sequence then Shots Sequence
Link the footage to the timeline
Export to create media for use in the job (never Original Camera footage!)
Reformat the exported footage and create the first versions to enable deeper links with the publish metadata and the project
(2 archives are created - one is shared one is for your box)



Start the Conform
Add footage to Libraries/assets/footage_xxx - preferable to start with raw at full res
Add graphics
Import (XML, AAF, EDL, etc) to Sequences reel on desktop
Consolidate all handles to Zero (0)
Make sources sequences - do not limit handles (it doesn’t have shot names) (the purpose is apply a color pipeline to each track - different source cameras)
make shots sequence (
Name (rename) the track(s)
rename shots (Name of the spot)_<background segment###>0
rename segments <shot name>_<track name>
rename comments <tape reel source>/<source name>
Make sure “Save Sources” is enabled (these become their own sources (separate from the soft linked raw folder in footage_raw)
Set the “Conform Search Location” directory


Set the resolution
In the Sources sequence, separate different camera type sources by layer
Select the first clip on the first layer
Set the format/resize and once you’ve got the option you want for the clip, exit the format
select all the clips on that track
drag the format to the rest of the clips and the resizing will be applied

Set the color space
Select the first clip on each track in the Sources Sequence
Select the PreProcessing Options TLFX and edit
Select the Colour Mgmt button
Select Colour transform 16bit
Hit the Import
Go to bookmark/job directories/utilities/flame color toolkit (your OS)
Select the camera (with the science you want)
Select the appropriate color tagging (if the last color science thing says xxx to ACES then select ACES) and exit the Format editor
Drag the format to the rest of the clips in the track
Check the sources reel and validate that your sources have changed accordingly (make sure the tagging is what you intended)

Publish the OpenClip SOURCE shot (sequence publish)
Highlight the Desktop/(reel group)/Shots Sequence and navigate the media hub to the “job home” bookmark
Select Export/Sequence Publish 
Select the Format Preset/Project/Shots_Publish_(desired option)
Enable the Show Advanced Options button
Select the Sequence Options/Include Handles desired amount of handles
Export

Publish the OpenClip COMP shot for the timeline
Copy the top layer from the Shots Sequence to the Shots Sequence_publish timeline
Select the first Batch Group (SPOTNAME_shot number) 
Delete the auto generated nodes - resize, mux, writefile
Right click the media and from the context menu, select logik-project/create-openclip/projekt_comp selected clips to create comp open clip
Iterate
Render
Repeat for all Batch Groups created by the publish activities.

Connected conform
Copy the published shots
Paste shots in the shots sequence publish
From the desktop drag the shots sequence publish into the published sequence reel
Drag the top layer of the OpenClip COMP shots from the conformed sequence top layer into the Published versions reel
In the media panel, choose the clips and right-click-export as movie preset work in progress (WIP)
Export
Go the Media hub/job home
from pattern browsing tab - go to preset for WIP postings
Drag all into the postings reel (blue)
In the sequence reel - shots sequence - duplicate and rename shots sequence graded
Open and delete the top track and the movie file at the end and select the clips
Right click and “remove segment connection”
Right click k and dup source
Right click and Media unlink
Media hub - assets footage graded and drag into the footage graded library
Go back to conform and set as the conform search location
Go back to reels view - select the first clip on the timeline and color transform 16b import the correct science tag properly as well
Drag the processing to all the other clips on the timeline.
Right click on shots sequence graded on the sequences reel - export.  
Make sure you’re in JobHome
Export as publish graded preset
Export and the grade shows up in the source

Go to the desktop and go into the batchgroups.  

Gather an Archive


Usage Notes:
To create a dated desktop - Make sure the desktop is cleared first

To create a conforms reel - it creates it in the editorial library


Troubleshooting:


Please see the Preference section to make sure the expected Prefs are set



Problem:
Not being able to fire up the project on a Mac

Info:
When the computer name has a space or a hyphen
<workstation name> is required for project connection
Mac has a Pretty Name, a host name and a bonjour name

To Fix:
Set HostName
Set ComputerName
Set LocalHostName


Questions for Phil:
what is the tmp bookmark for?
why four pad in version name?  Possible 2?


What’s the difference between Format Options and Preprocessing options?
Format has to do with the format of the files coming in
Pre-Processing has to do with Color Management


What should I ask for from Color?
AP0 [ACES 2065-1] or ACEScg [AP1]
OpenEXR 16bfp PIZ

Why no access to the hooks from the keyboard shortcuts?

Write File:
Pattern:
Original:
                                   shots/<shot name>/media/renders/<shot name>_v<version>/<shot name>_v<version>.<frame><ext>
Comp
<project nickname>/shots/<shot name>/media/renders/<name>_<version name>/<name>_<version name><frame><ext>


Open Clip:
Original
                                   shots/<shot name>/openclip/output_clips/flame/<shot name>_publish<ext>
Comp:
<project nickname>/shots/<shot name>/openclip/output_clips/flame/<name><ext>



Guidance:
shared in the project








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
