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

# File Name:        create_after_effects_shot_script.py
# Version:          2.2.7
# Created:          2024-01-19
# Modified:         2024-08-31

# ========================================================================== #
# This section imports the necessary modules.
# ========================================================================== #

# import flame
import os
# import pdb; pdb.set_trace()
import re
import fileinput
# import logging
# from datetime import datetime

# ========================================================================== #
# This section defines functions to create after effects scripts.
# ========================================================================== #

# Define function to create a shot script for after effects based on task
def create_after_effects_shot_script(shot_name, 
                       app_name, 
                       task_type, 
                       version_name,
                       shots_dir, 
                       shot_renders_dir, 
                       shot_scripts_dir):
    """
    Create a shot script for after effects based on task.

    Parameters:
        shot_name (str): The name of the shot.
        shots_dir (str): The directory where shots are stored.
        shot_sources_dir (str): The directory for shot sources.
        shot_source_dir (str): The directory for shot source.
        app_name (str): The name of the application.
        task_type (str): The type of task.
        version_name (str): The name of the version.
        shot_scripts_dir (str): The directory for shot scripts.
        shot_source_version_openexr_sequences_info (list): Information about OpenEXR sequences.
        shot_source_version_start_frame (int): Start frame number of the source version.
        shot_source_version_end_frame (int): End frame number of the source version.

    Returns:
    None
    """

    # Define the directory for the specific app and task type
    shot_scripts_app_task_dir = os.path.join(shots_dir,
                                             shot_scripts_dir,
                                             app_name,
                                             'shot',
                                             task_type)

    # Create the directory if it doesn't exist
    os.makedirs(shot_scripts_app_task_dir, exist_ok=True)

    # Define the file path for the script
    shot_scripts_app_task_file = f"{shot_name}_{app_name}_{task_type}_{version_name}.aep"
    shot_scripts_app_task_file_path = os.path.join(shot_scripts_app_task_dir,
                                              shot_scripts_app_task_file)
    
    # Define the script path for the script
    shot_scripts_app_task_script = f"{shot_name}_{app_name}_{task_type}_{version_name}.jsx"
    shot_scripts_app_task_script_path = os.path.join(shot_scripts_app_task_dir,
                                              shot_scripts_app_task_script)

    # Write the After Effects script content to the file
    with open(shot_scripts_app_task_script_path, 'w') as shot_scripts_app_task_script:
        shot_scripts_app_task_script.write(f"""{{
    // {shot_scripts_app_task_script}

    function SmartImport() {{
        var scriptName = "{shot_scripts_app_task_script}";

        // Define the source folder
        var source_folder = "{shot_sources_dir}/{shot_source_dir}";

        // If no project open, create a new project to import the files into.
        if (!app.project) {{
            app.newProject();
        }}

        function processFile(theFile) {{
            try {{
                // Create a variable containing ImportOptions.
                var importOptions = new ImportOptions(theFile);
                var importedFootage = app.project.importFile(importOptions);

                // Create a new composition
                var compName = "{shot_name}_{app_name}_{task_type}_{version_name}";
                var compWidth = importedFootage.width;
                var compHeight = importedFootage.height;
                var compFrameRate = importedFootage.frameRate;
                var compDuration = importedFootage.duration;
                var compStartFrame = {shot_source_version_start_frame};
                var newComp = app.project.items.addComp(compName, compWidth, compHeight, 1, compDuration, compFrameRate);
                newComp.displayStartFrame = compStartFrame;

                // Add the imported footage to the composition
                var footageLayer = newComp.layers.add(importedFootage);

                // Set the target directory for the render output (including the subfolder)
                var targetDirectory = new Folder("{shot_renders_dir}/{shot_name}_{app_name}_{task_type}_{version_name}");

                // Check if the target directory exists, and create it if it doesn't
                if (!targetDirectory.exists) {{
                    targetDirectory.create();
                }}

                // Add the composition to the render queue
                var renderQueueItem = app.project.renderQueue.items.add(newComp);

                // Set render output settings
                renderQueueItem.outputModule(1).file = new File("{shot_renders_dir}/{shot_name}_{app_name}_{task_type}_{version_name}/{shot_name}_{app_name}_{task_type}_{version_name}.[########].exr");
                renderQueueItem.outputModule(1).applyTemplate("OpenEXR-PIZ");

                // Save the After Effects project
                app.project.save(new File("{shot_scripts_app_task_file_path}"));
            }} catch (error) {{
                alert(error.toString(), scriptName);
            }}
        }}

        function testForSequence(files) {{
            var searcher = new RegExp("[0-9]+");
            var movieFileSearcher = new RegExp("(mov|avi|mpg)$", "i");
            var parseResults = new Array;

            // Test that we have a sequence. Stop parsing after 10 files.
            for (x = 0; (x < files.length) & x < 10; x++) {{
                var movieFileResult = movieFileSearcher.exec(files[x].name);
                if (!movieFileResult) {{
                    var currentResult = searcher.exec(files[x].name);
                    // Regular expressions return null if no match was found.
                    // Otherwise, they return an array with the following information:
                    // array[0] = the matched string.
                    // array[1..n] = the matched capturing parentheses.

                    if (currentResult) {{ // We have a match -- the string contains numbers.
                        // The match of those numbers is stored in the array[1].
                        // Take that number and save it into parseResults.
                        parseResults[parseResults.length] = currentResult[0];
                    }} else {{
                        parseResults[parseResults.length] = null;
                    }}
                }} else {{
                    parseResults[parseResults.length] = null;
                }}
            }}

            // If all the files we just went through have a number in their file names,
            // assume they are part of a sequence and return the first file.

            var result = null;
            for (i = 0; i < parseResults.length; ++i) {{
                if (parseResults[i]) {{
                    if (!result) {{
                        result = files[i];
                    }}
                }} else {{
                    // In this case, a file name did not contain a number.
                    result = null;
                    break;
                }}
            }}

            return result;
        }}

        function processFolder(theFolder) {{
            // Get an array of files in the target folder, excluding .DS_Store files.
            var files = theFolder.getFiles(function(file) {{
                return !file.name.match(/^\..*$/); // Exclude files starting with a dot (hidden files)
            }});

            // Test whether theFolder contains a sequence.
            var sequenceStartFile = testForSequence(files);

            // If it does contain a sequence, import the sequence,
            if (sequenceStartFile) {{
                try {{
                    // Create a variable containing ImportOptions.
                    var importOptions = new ImportOptions(sequenceStartFile);

                    importOptions.sequence = true;
                    // importOptions.forceAlphabetical = true;        // Un-comment this if you want to force alpha order by default.
                    var importedFootage = app.project.importFile(importOptions);

                    // Create a new composition
                    var compName = "{shot_name}_{app_name}_{task_type}_{version_name}";
                    var compWidth = importedFootage.width;
                    var compHeight = importedFootage.height;
                    var compFrameRate = importedFootage.frameRate;
                    var compDuration = importedFootage.duration;
                    var compStartFrame = {shot_source_version_start_frame};
                    var newComp = app.project.items.addComp(compName, compWidth, compHeight, 1, compDuration, compFrameRate);
                    newComp.displayStartFrame = compStartFrame;

                    // Add the imported footage to the composition
                    var footageLayer = newComp.layers.add(importedFootage);

                    // Set the target directory for the render output (including the subfolder)
                    var targetDirectory = new Folder("{shot_renders_dir}/{shot_name}_{app_name}_{task_type}_{version_name}");

                    // Check if the target directory exists, and create it if it doesn't
                    if (!targetDirectory.exists) {{
                        targetDirectory.create();
                    }}

                    // Add the composition to the render queue
                    var renderQueueItem = app.project.renderQueue.items.add(newComp);

                    // Set render output settings
                    renderQueueItem.outputModule(1).file = new File("{shot_renders_dir}/{shot_name}_{app_name}_{task_type}_{version_name}/{shot_name}_{app_name}_{task_type}_{version_name}.[########].exr");
                    renderQueueItem.outputModule(1).applyTemplate("OpenEXR-PIZ");

                    // Save the After Effects project
                    app.project.save(new File("{shot_scripts_app_task_file_path}"));
                }} catch (error) {{
                }}
            }}

            // Otherwise, import the files and recurse.

            for (index in files) {{ // Go through the array and set each element to singleFile, then run the following.
                if (files[index] instanceof File) {{
                    if (!sequenceStartFile) {{ // If file is already part of a sequence, don't import it individually.
                        processFile(files[index]); // Calls the processFile function above.
                    }}
                }}
                if (files[index] instanceof Folder) {{
                    processFolder(files[index]); // recursion
                }}
            }}
        }}

        // Recursively examine the source folder.
        processFolder(new Folder(source_folder));
    }}

    SmartImport();
}}""")

        # # This section is for logging purposes
        # logging.debug(f"After Effects script created for:  {shot_name}_{app_name}_{task_type}_{version_name}")

        print(f"After Effects Shot script created:    {shot_scripts_app_task_script}\n")

# ========================================================================== #
# C2 A9 32 30 32 34 2D 4D 41 4E 5F 4D 41 44 45 2D 4D 45 4B 41 4E 49 53 4D 5A #
# ========================================================================== #

# Changelist:

# -------------------------------------------------------------------------- #
# version:               0.0.1
# modified:              2024-05-03 - 01:50:36
# comments:              Basic functionality defined and tested
# -------------------------------------------------------------------------- #
# version:               0.0.2
# modified:              2024-05-03 - 02:12:19
# comments:              Fixed some formatting and flame menus
# -------------------------------------------------------------------------- #
# version:               0.0.3
# modified:              2024-05-03 - 11:25:42
# comments:              Changed 'the_current_project' to 'the_current_projekt'
# -------------------------------------------------------------------------- #
# version:               0.0.4
# modified:              2024-05-03 - 11:38:31
# comments:              Standardizd 'logik-projekt' menu entries
# -------------------------------------------------------------------------- #
# version:               0.0.5
# modified:              2024-05-03 - 12:29:29
# comments:              Restored '_{version_name}' in script construction
# -------------------------------------------------------------------------- #
# version:               0.0.6
# modified:              2024-05-03 - 13:37:01
# comments:              Added validation for file existence
# -------------------------------------------------------------------------- #
# version:               1.0.0
# modified:              2024-05-06 - 14:35:57
# comments:              Complete re-write - tested on Lucid Link
# -------------------------------------------------------------------------- #
# version:               1.0.1
# modified:              2024-05-06 - 16:12:00
# comments:              Minor reformatting
# -------------------------------------------------------------------------- #
# version:               1.0.2
# modified:              2024-05-06 - 16:24:36
# comments:              added printf statements at logging.debug points
# -------------------------------------------------------------------------- #
# version:               1.0.3
# modified:              2024-05-06 - 17:02:53
# comments:              Added (*args, **kwargs) to main function
# -------------------------------------------------------------------------- #
# version:               1.0.4
# modified:              2024-05-06 - 21:50:39
# comments:              Updated docstrings, comments and formatting
# -------------------------------------------------------------------------- #
# version:               1.0.5
# modified:              2024-05-06 - 22:14:47
# comments:              Corrected Write node file path for Nuke Shot script.
# -------------------------------------------------------------------------- #
# version:               1.0.6
# modified:              2024-05-10 - 09:39:33
# comments:              Enabled production job_dir and disabled test job_dir
# -------------------------------------------------------------------------- #
# version:               2.0.0
# modified:              2024-05-10 - 21:14:44
# comments:              Refactored monolithic code and tested in flame 2025
# -------------------------------------------------------------------------- #
# version:               2.0.1
# modified:              2024-05-10 - 21:45:10
# comments:              Modified docstrings and formatting.
# -------------------------------------------------------------------------- #
# version:               2.0.2
# modified:              2024-05-14 - 12:53:36
# comments:              Renamed 'classes_and_functions' directory to 'modules'.
# -------------------------------------------------------------------------- #
# version:               2.1.2
# modified:              2024-05-15 - 12:35:57
# comments:              Renamed nuke script functions and started blender tools.
# -------------------------------------------------------------------------- #
# version:               2.2.2
# modified:              2024-05-18 - 18:00:56
# comments:              Added GNU GPLv3 Disclaimer.
# -------------------------------------------------------------------------- #
# version:               2.2.3
# modified:              2024-05-18 - 18:46:27
# comments:              Minor modification to Disclaimer.
# -------------------------------------------------------------------------- #
# version:               2.2.5
# modified:              2024-06-09 - 11:27:00
# comments:              Added After Effects script/openclip generators
# -------------------------------------------------------------------------- #
# version:               2.2.6
# modified:              2024-06-10 - 06:59:38
# comments:              Removed some double quotes from After Effects templates
# -------------------------------------------------------------------------- #
# version:               2.2.7
# modified:              2024-08-31 - 19:04:02
# comments:              prep for release.
# -------------------------------------------------------------------------- #
