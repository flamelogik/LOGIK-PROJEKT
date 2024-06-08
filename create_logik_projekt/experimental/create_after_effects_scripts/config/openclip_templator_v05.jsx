{
    // folder_import.jsx

    function SmartImport() {
        var scriptName = "Smart Import";

        // Define the source folder
        var source_folder = "/Users/Shared/JOBS/my_job/shots/shot_0010/media/sources/shot_0010_layer_001/";

        // If no project open, create a new project to import the files into.
        if (!app.project) {
            app.newProject();
        }

        function processFile(theFile) {
            try {
                // Create a variable containing ImportOptions.
                var importOptions = new ImportOptions(theFile);
                var importedFootage = app.project.importFile(importOptions);

                // Create a new composition
                var compName = "shot_0010_layer_001_ae_comp_v0001";
                var compWidth = importedFootage.width;
                var compHeight = importedFootage.height;
                var compFrameRate = importedFootage.frameRate;
                var compDuration = importedFootage.duration;
                var compStartFrame = "1001";
                var newComp = app.project.items.addComp(compName, compWidth, compHeight, 1, compDuration, compFrameRate);
                newComp.displayStartTime = compStartFrame;

                // Add the imported footage to the composition
                var footageLayer = newComp.layers.add(importedFootage);

                // Add the composition to the render queue
                var renderQueueItem = app.project.renderQueue.items.add(newComp);

                // Set render output settings
                renderQueueItem.outputModule(1).file = new File("/Users/Shared/JOBS/my_job/shots/shot_0010/media/renders/shot_0010_layer_001_ae_comp_v0001/shot_0010_layer_001_ae_comp_v0001.[########].exr");
                renderQueueItem.outputModule(1).applyTemplate("OpenEXR-PIZ");

                // Save the After Effects project
                app.project.save(new File("/Users/Shared/JOBS/my_job/shots/shot_0010/scripts/after_effects/shot_0010_layer_001_ae_comp_v0001.aep"));
            } catch (error) {
                alert(error.toString(), scriptName);
            }
        }

        function testForSequence(files) {
            var searcher = new RegExp("[0-9]+");
            var movieFileSearcher = new RegExp("(mov|avi|mpg)$", "i");
            var parseResults = new Array;

            // Test that we have a sequence. Stop parsing after 10 files.
            for (x = 0; (x < files.length) & x < 10; x++) {
                var movieFileResult = movieFileSearcher.exec(files[x].name);
                if (!movieFileResult) {
                    var currentResult = searcher.exec(files[x].name);
                    // Regular expressions return null if no match was found.
                    // Otherwise, they return an array with the following information:
                    // array[0] = the matched string.
                    // array[1..n] = the matched capturing parentheses.

                    if (currentResult) { // We have a match -- the string contains numbers.
                        // The match of those numbers is stored in the array[1].
                        // Take that number and save it into parseResults.
                        parseResults[parseResults.length] = currentResult[0];
                    } else {
                        parseResults[parseResults.length] = null;
                    }
                } else {
                    parseResults[parseResults.length] = null;
                }
            }

            // If all the files we just went through have a number in their file names,
            // assume they are part of a sequence and return the first file.

            var result = null;
            for (i = 0; i < parseResults.length; ++i) {
                if (parseResults[i]) {
                    if (!result) {
                        result = files[i];
                    }
                } else {
                    // In this case, a file name did not contain a number.
                    result = null;
                    break;
                }
            }

            return result;
        }

        function processFolder(theFolder) {
            // Get an array of files in the target folder.
            var files = theFolder.getFiles();

            // Test whether theFolder contains a sequence.
            var sequenceStartFile = testForSequence(files);

            // If it does contain a sequence, import the sequence,
            if (sequenceStartFile) {
                try {
                    // Create a variable containing ImportOptions.
                    var importOptions = new ImportOptions(sequenceStartFile);

                    importOptions.sequence = true;
                    // importOptions.forceAlphabetical = true;        // Un-comment this if you want to force alpha order by default.
                    var importedFootage = app.project.importFile(importOptions);

                    // Create a new composition
                    var compName = "shot_0010_layer_001_ae_comp_v0001";
                    var compWidth = importedFootage.width;
                    var compHeight = importedFootage.height;
                    var compFrameRate = importedFootage.frameRate;
                    var compDuration = importedFootage.duration;
                    var compStartFrame = "1001";
                    var newComp = app.project.items.addComp(compName, compWidth, compHeight, 1, compDuration, compFrameRate);
                    newComp.displayStartTime = compStartFrame;

                    // Add the imported footage to the composition
                    var footageLayer = newComp.layers.add(importedFootage);

                    // Add the composition to the render queue
                    var renderQueueItem = app.project.renderQueue.items.add(newComp);

                    // Set render output settings
                    renderQueueItem.outputModule(1).file = new File("/Users/Shared/JOBS/my_job/shots/shot_0010/media/renders/shot_0010_layer_001_ae_comp_v0001/shot_0010_layer_001_ae_comp_v0001.[########].exr");
                    renderQueueItem.outputModule(1).applyTemplate("OpenEXR-PIZ");

                    // Save the After Effects project
                    app.project.save(new File("/Users/Shared/JOBS/my_job/shots/shot_0010/scripts/after_effects/shot_0010_layer_001_ae_comp_v0001.aep"));
                } catch (error) {
                }
            }

            // Otherwise, import the files and recurse.

            for (index in files) { // Go through the array and set each element to singleFile, then run the following.
                if (files[index] instanceof File) {
                    if (!sequenceStartFile) { // If file is already part of a sequence, don't import it individually.
                        processFile(files[index]); // Calls the processFile function above.
                    }
                }
                if (files[index] instanceof Folder) {
                    processFolder(files[index]); // recursion
                }
            }
        }

        // Recursively examine the source folder.
        processFolder(new Folder(source_folder));
    }

    SmartImport();
}
