{
    // ANIMALS_0010_layer_01_after_effects_roto_v0000.jsx

    function SmartImport() {
        var scriptName = "ANIMALS_0010_layer_01_after_effects_roto_v0000.jsx";

        // Define the source folder
        var source_folder = "/Users/shared/JOBS/alpha_bravo_charlie/shots/ANIMALS_0010/media/sources/v0000";

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
                var compName = "ANIMALS_0010_layer_01_after_effects_roto_v0000";
                var compWidth = importedFootage.width;
                var compHeight = importedFootage.height;
                var compFrameRate = importedFootage.frameRate;
                var compDuration = importedFootage.duration;
                var compStartFrame = 1001;
                var newComp = app.project.items.addComp(compName, compWidth, compHeight, 1, compDuration, compFrameRate);
                newComp.displayStartFrame = compStartFrame;

                // Add the imported footage to the composition
                var footageLayer = newComp.layers.add(importedFootage);

                // Set the target directory for the render output (including the subfolder)
                var targetDirectory = new Folder("/Users/shared/JOBS/alpha_bravo_charlie/shots/ANIMALS_0010/media/sources/ANIMALS_0010_layer_01_after_effects_roto_v0000");

                // Check if the target directory exists, and create it if it doesn't
                if (!targetDirectory.exists) {
                    targetDirectory.create();
                }

                // Add the composition to the render queue
                var renderQueueItem = app.project.renderQueue.items.add(newComp);

                // Set render output settings
                renderQueueItem.outputModule(1).file = new File("/Users/shared/JOBS/alpha_bravo_charlie/shots/ANIMALS_0010/media/sources/ANIMALS_0010_layer_01_after_effects_roto_v0000.[########].exr");
                renderQueueItem.outputModule(1).applyTemplate("OpenEXR-PIZ");

                // Save the After Effects project
                app.project.save(new File("/Users/shared/JOBS/alpha_bravo_charlie/shots/ANIMALS_0010/scripts/after_effects/sources/roto/ANIMALS_0010_layer_01_after_effects_roto_v0000.aep"));
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
            // Get an array of files in the target folder, excluding .DS_Store files.
            var files = theFolder.getFiles(function(file) {
                return !file.name.match(/^\..*$/); // Exclude files starting with a dot (hidden files)
            });

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
                    var compName = "ANIMALS_0010_layer_01_after_effects_roto_v0000";
                    var compWidth = importedFootage.width;
                    var compHeight = importedFootage.height;
                    var compFrameRate = importedFootage.frameRate;
                    var compDuration = importedFootage.duration;
                    var compStartFrame = 1001;
                    var newComp = app.project.items.addComp(compName, compWidth, compHeight, 1, compDuration, compFrameRate);
                    newComp.displayStartFrame = compStartFrame;

                    // Add the imported footage to the composition
                    var footageLayer = newComp.layers.add(importedFootage);


                    // Set the target directory for the render output (including the subfolder)
                    var targetDirectory = new Folder("/Users/shared/JOBS/alpha_bravo_charlie/shots/ANIMALS_0010/media/sources/ANIMALS_0010_layer_01_after_effects_roto_v0000");

                    // Check if the target directory exists, and create it if it doesn't
                    if (!targetDirectory.exists) {
                        targetDirectory.create();
                    }

                    // Add the composition to the render queue
                    var renderQueueItem = app.project.renderQueue.items.add(newComp);

                    // Set render output settings
                    renderQueueItem.outputModule(1).file = new File("/Users/shared/JOBS/alpha_bravo_charlie/shots/ANIMALS_0010/media/sources/ANIMALS_0010_layer_01_after_effects_roto_v0000.[########].exr");
                    renderQueueItem.outputModule(1).applyTemplate("OpenEXR-PIZ");

                    // Save the After Effects project
                    app.project.save(new File("/Users/shared/JOBS/alpha_bravo_charlie/shots/ANIMALS_0010/scripts/after_effects/sources/roto/ANIMALS_0010_layer_01_after_effects_roto_v0000.aep"));
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