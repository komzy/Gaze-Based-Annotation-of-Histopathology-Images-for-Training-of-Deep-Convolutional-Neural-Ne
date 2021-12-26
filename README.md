# Gaze Based Annotation of Histopathology Images for Training of Deep Convolutional Neural Networks
This repo contains the code and data used for our work on Gaze-based annotation of histopathology images. Table of contents is given below
* [Requirements](#requirements)
* [Setting up Python Environment](#setting-up-python-environment)
* [Dataset](#dataset)
   * Gaze
   * Hand
   * Masks
   * Raw Gaze Data
* [Models](#models)
* [Training](#training)
* [Evaluation](#evaluation)
* [Reference](#reference)

# Requirements
- Tensorflow 1.15
- Python 3.7
- Anaconda
- Qupath (for viewing Whole Slide Image (WSI) file)
- MATLAB (masks to bounding box conversion)
- Google Colab or Jupyter Notebook

# Setting up Python Environment
1) Create a conda environment and install Tensorflow:
```
conda create -n tensorflow1.15 python=3.7
conda activate tensorflow1.15
conda install cudatoolkit=10.0
conda install cudnn=7.6.5
pip install tensorflow-gpu==1.15
```
2) Install dependencies
```
pip install numpy==1.19.5 lxml pillow matplotlib jupyter contextlib2 cython tf_slim pycocotools
```
(For windows change `pycocotools` to `pycocotools-windows`)


3) Install the [TensorFlow Object Detection API ](https://github.com/tensorflow/models/blob/master/research/object_detection/g3doc/tf1.md).
## Dataset
Follow the steps in `\Generate_Annotations` to create your own dataset from gaze and hand annotations. 
Or simply download our dataset from the links below.

**- Gaze:** Images used for training and testing of gaze-based object detectors can be downloaded from [here](https://1drv.ms/u/s!As_geBXhgCy1qjOElYHo5oWX_OQ0?e=L38qQ6). The labels corresponding to each file in the training and test dataset can be found in "Gaze_Data/labels/train" and "Gaze_Data/labels/test" respectively. 

**- Hand:** Images used for training and testing of object detectors on hand-labelled data can be downloaded from [here](https://1drv.ms/u/s!As_geBXhgCy1qwa3-NdukNHbLRsb?e=NT3Abi). The labels corresponding to each file in the training and test dataset can be found in "Hand_Data/labels/train" and "Hand_Data/labels/test" respectively. `NOTE:` Hand generated labels were used for performance evaluation of both gaze-based and hand-labelled object detectors. Therefore, the contents of both the "Gaze_Data/labels/test" and the "Hand_Data/labels/test" folders are identical. 

**- Masks:** The binary masks used for generating labels for hand and gaze-based object detectors can be downloaded from [here](https://1drv.ms/u/s!As_geBXhgCy1rBzg_A3ssuabn6TF?e=MD21iT)

**- Raw Gaze Data:** 
The raw gaze data is available [here](https://1drv.ms/u/s!As_geBXhgCy1rkleyurgCn5g3RdX?e=f2OkBb). This data needs to be converted into binary masks before it can be used to train an object detector.
   1) Every eye gaze data collection session (lasted about 5-10 minutes on average) is contained in a folder named according to the date and time. 
   2) "all_sessions_merged" folder contains all levels from every gaze data collection session merged together.
   3) "all_annotations_on_max_level" contains one csv file of the maximum resolution containing all gaze data points from all levels scaled to the highest resolution of the .svs image.
   4) ".svs" files are the corresponding WSI file.



## Models
- Our pre-trained Faster RCNN models are available [here](https://1drv.ms/u/s!As_geBXhgCy1rSjYGEV7aMdLiYnr?e=qLZOUz).
- Raw [Faster RCNN Inception V2 weights](http://download.tensorflow.org/models/object_detection/faster_rcnn_inception_v2_coco_2018_01_28.tar.gz) 
- YOLOv3 and YOLOv5 models were trained using PyTorch and can be downloaded from [here](https://github.com/OAfzal/GazeYoloModels)

## Training
1. Download raw Faster RCNN Inception V2 Weights from the above link and into the `/training` directory.
2. From utils use the appropriate `generate_tfrecord` script to generate 'train.record' and 'test.record' from your train and test sets.
3. Paste 'train.record' and 'test.record' into the `/training` directory.
4. Set the appropriate paths in `training_pipeline.config`
5. Now initiate a training job by opening a new Terminal, cd inside the `models/research/object_detection` and run the following command:
```
python model_main.py  --logtostderr --model_dir=PATH_TO_BE_CONFIGURED\models\research\object_detection\training\faster_rcnn_inception_v2_coco_2018_01_28 --pipeline_config_path=PATH_TO_BE_CONFIGURED\models\research\object_detection\training\training_pipeline.config           
```
6. After training has completed, export the inference graph using `export_inference_graph.py` in the `models\research\object_detection` directory

## Evaluation
The Faster RCNN model was implemented in tensorflow. `Evaluation.ipynb` can be used to test the Faster RCNN model on the test data.
1. Download and extract our [Gaze-based and Hand-Annotated trained models](https://1drv.ms/u/s!As_geBXhgCy1rSjYGEV7aMdLiYnr?e=qLZOUz). If you prefer to train your own model then you can do so by following the instructions provided in the Training section above.
3. Paste `Evaluation.ipynb` and `/images` into `models/research/object_detection/`
4. Open terminal and cd `models/research/object_detection/` 
5. Run `Evaluation.ipynb` notebook via Jupyter Notebook

The YOLO models were implemented in PyTorch and can be found in this [repo](https://github.com/OAfzal/GazeYoloModels).

## Results
Results for all detectors can be found [here](https://1drv.ms/u/s!As_geBXhgCy1rz2y3zLqQZ5a_PQ3?e=2n7O1W). Corresponding metrics are generated by this [repo](https://github.com/Cartucho/mAP) using the detection results in `/Text_Format` directory.

## Reference
This repo was used to generate the results for the following paper on Gaze-based labelling of Pathology data. 
   
   Komal Mariam, Osama Mohammed Afzal, Wajahat Hussain, Muhammad Umar Javed, Amber Kiyani, Nasir Rajpoot, Syed Ali Khurram and Hassan Aqeel Khan, **"On Smart Gaze based Annotation of Histopathology Images for Training of Deep Convolutional Neural Networks",** *submitted to IEEE Journal of Biomedical and Health Informatics.*


**BibTex Reference:** Available after acceptance.
