## Generate Binary Masks from Gaze Annotations

1) Run 1_Gaze_to_BinaryMask.py. Download the 'Raw_Gaze_Data' folder from [here](https://1drv.ms/u/s!As_geBXhgCy1rkleyurgCn5g3RdX?e=f2OkBb). Set the input_path to the raw Gaze Annotation directory containing 'info.json' (preferably the `Raw_Gaze_Data/Case_Number/all_sessions_merged` folder). Kernel width of the KDE algorithm can be varied via the `ngaussian` parameter. Thresholding can be controlled via the `multiple` parameter. Output should be binary mask image files and their corresponding RGB tiles.

2) Run 3_BinaryMask_to_BoundingBox.m in MATLAB. The script converts white 'blobs' in binary mask image files to bounding boxes. Output should be a CSV containing BBox coordinates. 

## Generate Binary Masks from Hand Annotations

1) Run 2_QuPath_to_BinaryMask.groovy in Qupath to convert annotations to binary masks. Ouput are binary masks and their corresponding RGB tiles.

2) Run 3_BinaryMask_to_BoundingBox.m in MATLAB. The script converts white 'blobs' in binary mask image files to bounding boxes. Output should be a CSV containing BBox coordinates. The csvs can be used to generate the the required xmls Faster R-CNN.

## Visualize Gaze based Annotations in Qupath
1) Open the `.svs` file in the Raw_Gaze data in Qupath. 
 
2) Open 'utils/CSV_to_Qupath.groovy`in Qupath.
 
3) Set `maxLevel` to the highest zoom level contined in 'info.json' associated with the Raw_Gaze data

4) Run the script and input the path of the directory containing the gaze csvs ('Level xx') when prompted. 
