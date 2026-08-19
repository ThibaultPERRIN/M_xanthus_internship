inputDir = getDirectory("Choose a folder with hyperstack images");
outputDir = getDirectory("Choose a folder to save split channels");

list = getFileList(inputDir);

for (i = 0; i < list.length; i++) {
	run("Bio-Formats Importer", "open=[" + inputDir + list[i] + "] autoscale color_mode=Default rois_import=[ROI manager] view=Hyperstack stack_order=XYCZT");
	imgTitle = getTitle();
	run("Split Channels");
	
	dotIndex = lastIndexOf(list[i], ".");
	if (dotIndex > 0)
		baseName = substring(list[i], 0, dotIndex);
    else
    	baseName = list[i];
    
    for (c = 2; c <= nImages; c++) {
    	selectImage(c);
        saveAs("Tiff", outputDir + baseName + "_C" + c + ".tif");
        close();
    }

    close("*");
}

