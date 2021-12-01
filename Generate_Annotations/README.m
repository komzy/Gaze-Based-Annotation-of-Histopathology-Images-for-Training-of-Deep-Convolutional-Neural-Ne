# Generate Binary Masks from Gaze Annotations:

1) Run 1_Gaze_to_BinaryMask.py. Set the input_path to the raw Gaze Annotation directory containing 'info.json' (preferably the 'all_sessions_merged' folder). Vary kernel width of KDE via ngaussian and threshold by multiple parameters. Output should be binary mask image files and their corresponding RGB tiles.
2) Run 3_BinaryMask_to_BoundingBox.m in MATLAB. The script converts white 'blobs' in binary mask image files to bounding boxes. Output should be a CSV containing BBox coordinates. 

# Generate Binary Masks from Hand Annotations:

1) Run 2_QuPath_to_BinaryMask.groovy in Qupath to convert annotations to binary masks. Ouput are binary masks and their corresponding RGB tiles.
2) Run 3_BinaryMask_to_BoundingBox.m in MATLAB. The script converts white 'blobs' in binary mask image files to bounding boxes. Output should be a CSV containing BBox coordinates. 

# Visulaise Gaze based Annotations in Qupath:
1. Open the `.svs` file in the Raw_Gaze data in Qupath. 
2. Open 'utils/CSV_to_Qupath.groovy`in Qupath.
3. Set `maxLevel` to the highest zoom level contined in 'info.json' associated with the Raw_Gaze data 
4. Run the script and input the path of the directory containing the gaze csvs ('Level xx') when prompted. 
