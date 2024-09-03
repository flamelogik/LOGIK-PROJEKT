








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





## Table of Contents
- Introduction
- Chapter 1
  - Section 1.1
  - Section 1.2
- Chapter 2

# Introduction
Welcome to the document.

## Chapter 1
This is the first chapter.

### Section 1.1
Details of section 1.1.

### Section 1.2
Details of section 1.2.

## Chapter 2
This is the second chapter.




