# Gaze Based Annotation of Histopathology Images for Training of Deep Convolutional Neural Networks
(under construction)

## Requirements
- Tensorflow 1.15
- Python 3.7
- Anaconda
- Qupath
- MATLAB (masks to bounding box conversion)
- Google Colab or Jupyter Notebook

## Setting up Python Environment
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
Follow the steps in \Generate_Annotations to create your own dataset from gaze and hand annotations. **@komal:** *I don't see the raw gaze files. Have we provided a link to those somewhere? That link should be visible here and/or in the readme file in \Generate_Annotations.*

Or simply download our dataset here:

**- Gaze:** Images used for training and testing of gaze-based object detectors can be downloaded from the following link: https://1drv.ms/u/s!As_geBXhgCy1qjOElYHo5oWX_OQ0?e=L38qQ6. The labels corresponding to each file in the training and test dataset can be found in "train.xls" and "test.xlx" respectively.

**- Hand:** Images used for training and testing of gaze-based object detectors can be downloaded from the following link: https://1drv.ms/u/s!As_geBXhgCy1qwa3-NdukNHbLRsb?e=NT3Abi. The labels corresponding to each file in the training dataset can be found in the "train.xls" file. Object detectors trained on hand-labelled data were tested on the same images as the gaze-trained classifier. Therefore, the label file: *Gaze_Data/test.xlx* and the images in the *Gaze_Data/images/test_png* directory should be used for testing purposes.

**@komal:** *Please verify that the preceding statement is correct? I recommend putting Test images in the HAND data instead of the GAZE data to avoid confusion. We're testing both detectors on Hand labels so it makes more sense to have the test data in the Hand Data director.*

**@Dr.Hassan**: Please have a look now. test set in both folders is identical and created via hand labels. (Should I onlt have the test labels in hand-data directory?). Also updated the labels to PASCAL VOC format since its more standardized than csvs. 

**- Masks:** The binary masks used for generating labels for hand and gaze-based object detectors can be downloaded from the following links: https://1drv.ms/u/s!As_geBXhgCy1rBzg_A3ssuabn6TF?e=MD21iT


## Models
- Pre-trained models: https://1drv.ms/u/s!As_geBXhgCy1rSjYGEV7aMdLiYnr?e=qLZOUz
- Raw [Faster RCNN Inception V2 weights](http://download.tensorflow.org/models/object_detection/faster_rcnn_inception_v2_coco_2018_01_28.tar.gz) 

## Training
1. Download raw Faster RCNN Inception V2 Weights from the above link and into the `/training` directory.
2. Generate 'train.record' and 'test.record'. Please refer to `/Generate_Annotations` on steps to create these files.
3. Paste 'train.record' and 'test.record' into the `/training` directory.
4. Set the appropriate paths in `training_pipeline.config`
5. Now initiate a training job by opening a new Terminal, cd inside the `models/research/object_detection` and run the following command:
```
python model_main.py  --logtostderr --model_dir=PATH_TO_BE_CONFIGURED\models\research\object_detection\training\faster_rcnn_inception_v2_coco_2018_01_28 --pipeline_config_path=PATH_TO_BE_CONFIGURED\models\research\object_detection\training\training_pipeline.config           
```
6. After training has completed, export the inference graph using `export_inference_graph.py` in the models/research/object_detection directory

## Evaluation
1. Download and extract Gaze-based and Hand-Annotated trained models. You can also use your own trained model from the 'Training' step.
2. Paste `Evaluation.ipynb` and `/images` into `models/research/object_detection/`
3. Open terminal and cd `models/research/object_detection/` 
4. Run `Evaluation.ipynb` notebook via Jupyter Notebook

## Reference
This repo was used to generate the results for the following paper on Gaze-based labelling of Pathology data. 
   
   Komal Mariam, Osama Mohammed Afzal, Wajahat Hussain, Muhammad Umar Javed, Amber Kiyani, Nasir Rajpoot, Syed Ali Khurram and Hassan Aqeel Khan, **"On Smart Gaze based Annotation of Histopathology Images for Training of Deep Convolutional Neural Networks",** *submitted to IEEE Journal of Biomedical and Health Informatics.*


**BibTex Reference:** Available after acceptance.
