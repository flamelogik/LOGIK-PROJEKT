// Define the file path for the OpenEXR sequence
var exrPath = "/JOBS/my_job/shots/shot_0010/media/sources/shot_0010_layer_001/shot_0010_layer_001.00001001-00001050.exr";
var outputPath = "/JOBS/my_job/shots/shot_0010/media/renders/shot_0010_layer_001_ae_comp/shot_0010_layer_001_ae_comp.00001001-00001050.exr";

// Add the FootageItem (OpenEXR sequence)
var importOptions = new ImportOptions(File(exrPath));
importOptions.sequence = true;
var footageItem = app.project.importFile(importOptions);

// Create a new composition at the native resolution, color depth, aspect ratio, and frame rate of the FootageItem
var compName = "shot_0010_layer_001_ae_comp";
var comp = app.project.items.addComp(
    compName,
    footageItem.width,
    footageItem.height,
    footageItem.pixelAspect,
    footageItem.duration,
    footageItem.frameRate
);

// Add the FootageItem to the new composition
var footageLayer = comp.layers.add(footageItem);

// Add the CompItem to the RenderQueue
var renderQueueItem = app.project.renderQueue.items.add(comp);

// Set the output module for the render queue item
var outputModule = renderQueueItem.outputModule(1);
outputModule.file = File(outputPath);
outputModule.applyTemplate("OpenEXR");
outputModule.setSetting("OpenEXR Compression", "PIZ");
outputModule.setSetting("OpenEXR Bit Depth", "16 bit");

// Save the project
var projectFile = File("/JOBS/my_job/shots/shot_0010/media/renders/shot_0010_layer_001_ae_comp/shot_0010_layer_001_ae_comp.aep");
app.project.save(projectFile);

alert("Script completed successfully.");
