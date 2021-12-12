import os
import csv
import numpy as np
import matplotlib
from matplotlib import image
import glob
import re
import json
import openslide

"""
1_Gaze_to_BinaryMask.py: Script to generate binary masks for fixation regions and correspoinding RGB 
image. Python equivalent to 2_QuPath_to_BinaryMask.groovy with additional support for fixation regions and thresholding
Generates masks + RGB tiles for regions containing atleast 1 white pixel.

Uncomment lines 85-88 and if conditions on lines 187-190, 220-223 to generate corresponding RGB tiles.
WARNING: This will slow down execution
"""

def merged_levels(file_path, max_level):
    max_level_merged = []
    count = 0;

    # bring level points to maxlevel
    os.chdir(file_path)
    result = [i for i in glob.glob('Level *[0-9].csv')]
    for file in result:
        level = int(re.findall(r'\d+', file)[0])
        scaling_factor = 2 ** (max_level - level)
        with open(file) as csv_file:
            reader = csv.reader(csv_file)
            for row in reader:
                x = int(row[0]) * scaling_factor
                y = int(row[1]) * scaling_factor
                max_level_merged.append((x, y))
                count = count + 1

    return max_level_merged


def gaussian(x, sx, y=None, sy=None):
    """Returns an array of numpy arrays (a matrix) containing values between
    1 and 0 in a 2D Gaussian distribution

    arguments
    x		-- width in pixels
    sx		-- width standard deviation

    keyword argments
    y		-- height in pixels (default = x)
    sy		-- height standard deviation (default = sx)
    """

    # square Gaussian if only x values are passed
    if y == None:
        y = x
    if sy == None:
        sy = sx
    # centers
    xo = x / 2
    yo = y / 2
    # matrix of zeros
    M = np.zeros([y, x], dtype=float)
    # gaussian matrix
    for i in range(x):
        for j in range(y):
            M[j, i] = np.exp(
                -1.0 * (((float(i) - xo) ** 2 / (2 * sx * sx)) + ((float(j) - yo) ** 2 / (2 * sy * sy))))

    return M


def draw_heatmap(gazepoints, dispsize, mask_width, mask_height, input_path, slide, imagefile=None, alpha=0.5, savefilename=None, gaussianwh=200, gaussiansd=None):
 
    """----THRESHOLDING INFO-----
    - Set 'multiple' to vary binary mask thresholding parameter
    - lowbound is the mean of non-zero pixel values 
    - lowbound is equal lowbound * multiple to vary thresholding"""

    multiple = 4

    binarymasks_path = os.path.join(input_path, 'masks_'+str(multiple)+'_'+str(gaussianwh))
    if not os.path.exists(binarymasks_path):
        os.makedirs(binarymasks_path)

    ## uncomment to save RGB tiles
    # RGBimage_path = os.path.join(input_path, 'images')
    # if not os.path.exists(RGBimage_path):
    #     os.makedirs(RGBimage_path)

    print("This will take a while...")
    outF_path = os.path.join(binarymasks_path, "kernel_threshold_miou.txt")
    outF = open(outF_path, "a")

    # HEATMAP
    # Gaussian
    gwh = gaussianwh
    gsdwh = gwh / 6 if (gaussiansd is None) else gaussiansd
    gaus = gaussian(gwh, gsdwh)
    # matrix of zeroes
    strt = int(gwh / 2)
    heatmapsize = dispsize[1] + 2 * strt, dispsize[0] + 2 * strt
    heatmap = np.zeros(heatmapsize, dtype=float)
    # create heatmap
    for i in range(0, len(gazepoints)):
        # get x and y coordinates
        x = strt + gazepoints[i][0] - int(gwh / 2)
        y = strt + gazepoints[i][1] - int(gwh / 2)
        # correct Gaussian size if either coordinate falls outside of
        # display boundaries
        if (not 0 < x < dispsize[0]) or (not 0 < y < dispsize[1]):
            hadj = [0, gwh];
            vadj = [0, gwh]
            if 0 > x:
                hadj[0] = abs(x)
                x = 0
            elif dispsize[0] < x:
                hadj[1] = gwh - int(x - dispsize[0])
            if 0 > y:
                vadj[0] = abs(y)
                y = 0
            elif dispsize[1] < y:
                vadj[1] = gwh - int(y - dispsize[1])
            # add adjusted Gaussian to the current heatmap
            try:
                heatmap[y:y + vadj[1], x:x + hadj[1]] += gaus[vadj[0]:vadj[1], hadj[0]:hadj[1]] * gazepoints[i][2]
            except:
                # fixation was probably outside of display
                pass
        else:
            # add Gaussian to the current heatmap
            heatmap[y:y + gwh, x:x + gwh] += gaus * gazepoints[i][2]
    # resize heatmap
    # heatmap = heatmap[strt:dispsize[1] + strt, strt:dispsize[0] + strt]
    # # uncomment if MEMORY_ERROR
    heatmap1 = heatmap[0:int(len(heatmap)/2),:]
    heatmap2 = heatmap[int(len(heatmap)/2):len(heatmap),:]
    lowbound1 = np.mean(heatmap1[heatmap1 > 0])
    lowbound2 = np.mean(heatmap2[heatmap2 > 0])
    lowbound = (lowbound1+lowbound2)/2

    #lowbound = np.mean(heatmap[heatmap > 0])  # comment out if MEMORY_ERROR
    maxValue = np.amax(heatmap)
    minValue = np.amin(heatmap)
    normalize = maxValue - minValue

    print("Magnitude Maxvalue: " + str(maxValue))
    outF.write("Magnitude Maxvalue: " + str(maxValue)+"\n")
    print("Magnitude Minvalue: " + str(minValue))
    outF.write("Magnitude Minvalue: " + str(minValue) + "\n")
    print("Magnitude mean: " + str(lowbound))
    outF.write("Magnitude mean: " + str(lowbound) + "\n")
    lowbound = lowbound * multiple
    print("Thresholding mean_non-normalized: " + str(lowbound))
    outF.write("Thresholding mean_non-normalized: " + str(lowbound)+ "\n")
    print("Thresholding mean_normalized: " + str(lowbound / normalize))
    outF.write("Thresholding mean_normalized: " + str(lowbound / normalize)+"\n")
    heatmap[heatmap < lowbound] = 0
    heatmap[heatmap >= lowbound] = 1

    ## offset correction
    # skew_h = 132
    # skew_v = 45
    # for i in range(len(heatmap)):
    #     for j in range(len(heatmap[i])):
    #         if heatmap[i][j] == 1:
    #             heatmap[i-skew_v][j-skew_h] = 1
    #             heatmap[i][j] = 0;


    print("Working on it..")

    count = 0
    step_size_height = mask_height
    step_size_width = mask_width


    # height #width
    for height in range(0,display_height,step_size_height):
        for width in range(0,display_width,step_size_width):
            binary_tile= heatmap[height:height+step_size_height, width:width+step_size_width]
            count = count + 1
            if 1 in binary_tile:
                # Generate binary mask tiles
                matplotlib.image.imsave(os.path.join(binarymasks_path, savefilename+'_['+str(height)+','+str(width)+','
                +str(step_size_height)+','+str(step_size_width)+']_'+str(count)+'_labels.png'), binary_tile, cmap='gist_gray')

                ## uncomment to save RGB tiles
                # image = slide.read_region((width, height), 0, (step_size_width, step_size_height))
                # image.save(os.path.join(RGBimage_path, savefilename+'_['+str(height)+','+str(width)+','
                # +str(step_size_height)+','+str(step_size_width)+']_'+str(count)+'.png'))


    # tiles for last coloumn
    for height in range(display_height-step_size_height, display_height, step_size_height):
        for width in range(0, display_width, step_size_width):
            binary_tile = heatmap[height:height + step_size_height, width:width + step_size_width]
            count = count + 1
            if 1 in binary_tile:
                # Generate binary mask tiles
                matplotlib.image.imsave(os.path.join(binarymasks_path, savefilename+'_['+str(height)+','+str(width)+','
                +str(step_size_height)+','+str(step_size_width)+']_'+str(count)+'_labels.png'), binary_tile, cmap='gist_gray')

                ## uncomment to save RGB tiles
                # image = slide.read_region((width, height), 0, (step_size_width, step_size_height))
                # image.save(os.path.join(RGBimage_path, savefilename+'_['+str(height)+','+str(width)+','
                # +str(step_size_height)+','+str(step_size_width)+']_'+str(count)+'.png'))



    # tiles for last row
    for height in range(0, display_height, step_size_height):
        for width in range(display_width-step_size_width, display_width, step_size_width):
            binary_tile = heatmap[height:height + step_size_height, width:width + step_size_width]
            count = count + 1
            if 1 in binary_tile:
                # Generate binary mask tiles
                matplotlib.image.imsave(os.path.join(binarymasks_path, savefilename+'_['+str(height)+','+str(width)+','
                +str(step_size_height)+','+str(step_size_width)+']_'+str(count)+'_labels.png'), binary_tile, cmap='gist_gray')

                ## uncomment to save RGB tiles
                # image = slide.read_region((width, height), 0, (step_size_width, step_size_height))
                # image.save(os.path.join(RGBimage_path, savefilename+'_['+str(height)+','+str(width)+','
                # +str(step_size_height)+','+str(step_size_width)+']_'+str(count)+'.png'))


# BEGIN CODE
# SET INPUT ARGUMENTS HERE

input_path = "F:\Data\Career & Studies\Masters\Thesis\DigitPathology\Pycharm_Projects\lsiv-python3\output_2\S-19-126H gaze\\2020-04-09 22-26-37"
mask_width = 4000  #output width
mask_height = 4000  #output width
ngaussian = 400 # "blob size": for gaussian width 200 set to 1600, for width 100 set 800, for 50 set to 400..etc
alpha = 1       #opacity of white regions in binary masks

##TODO: Standard deviation param

with open(input_path + '/info.json') as f:
    data = json.load(f)
    max_level = int(data['Level_Count']) - 1
    display_width = data['Level_Details'][max_level]['Width']
    display_height = data['Level_Details'][max_level]['Height']
    output_name = data['File_Name']
    file_path = data['File_Path']       # manually set if path not found
    #file_path='/media/affan/32CCA87DCCA83D4B/Users/Affan/Desktop/sigma/Gaze Tracking project/Datasets/Whole Slide images/S-19-126H.svs'

slide=openslide.OpenSlide(file_path)
gaze_data_raw= merged_levels(input_path,max_level)
gaze_data = []
if len(gaze_data_raw[0]) == 2:
    gaze_data = list(map(lambda q: (int(float(q[0])), int(float(q[1])), 1), gaze_data_raw))
    print("Running 1")
else:
    gaze_data = list(map(lambda q: (int(float(q[0])), int(float(q[1])), int(float(q[2]))), gaze_data_raw))
    print("Running 2")

draw_heatmap(gaze_data, (display_width, display_height), mask_width, mask_height, input_path, slide, alpha=alpha, savefilename=output_name,
             imagefile=None, gaussianwh=ngaussian, gaussiansd=None)
print("Done!")



