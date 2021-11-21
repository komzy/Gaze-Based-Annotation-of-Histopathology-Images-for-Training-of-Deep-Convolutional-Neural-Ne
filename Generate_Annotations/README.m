Generate Binary Masks from Gaze Annotations:

1) Run 1_Gaze_to_BinaryMask.py. Set the input_path to the Gaze Annotation folder containing 'info.json'. Vary kernel width of KDE via ngaussian and threshold by multiple parameters. Output should be binary mask image files and their corresponding RGB tiles.
2) Run 3_BinaryMask_to_BoundingBox.m in MATLAB. The script converts white 'blobs' in binary mask image files to bounding boxes. Output should be a CSV containing BBox coordinates. 

Generate Binary Masks from Hand Annotations:

1) Run 2_QuPath_to_BinaryMask.groovy in Qupath to convert annotations to binary masks. Ouput are binary masks and their corresponding RGB tiles.
2) Run 3_BinaryMask_to_BoundingBox.m in MATLAB. The script converts white 'blobs' in binary mask image files to bounding boxes. Output should be a CSV containing BBox coordinates. 

