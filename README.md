# Gaze Based Annotation of Histopathology Images for Training of Deep Convolutional Neural Networks
(under construction)

## Requirements
- Tensorflow 1.15
- Python 3.7
- Qupath
- MATLAB (masks to bounding box conversion)
- Google Colab or Jupyter Notebook

## Setting up Python Environment
Create virtual environment and install Tensorflow:
```
conda create -n tensorflow1.15 python=3.7
conda activate tensorflow1.15
conda install cudatoolkit=10.0
conda install cudnn=7.6.5
pip install tensorflow-gpu==1.15
```
Install dependenies
```
pip install lxml pillow matplotlib jupyter contextlib2 cython tf_slim pycocotools-windows 
```
Install the [TensorFlow Object Detection API ](https://github.com/tensorflow/models/blob/master/research/object_detection/g3doc/tf1.md).
## Dataset
Follow the steps in \Generate_Annotations to create your own dataset from gaze and hand annotations. **@komal:** *I don't see the raw gaze files. Have we provided a link to those somewhere? That link should be visible here and/or in the readme file in \Generate_Annotations.*

Or simply download our dataset here:

**- Gaze:** Images used for training and testing of gaze-based object detectors can be downloaded from the following link: https://1drv.ms/u/s!As_geBXhgCy1qjOElYHo5oWX_OQ0?e=L38qQ6. The labels corresponding to each file in the training and test dataset can be found in "train.xls" and "test.xlx" respectively.

**- Hand:** Images used for training and testing of gaze-based object detectors can be downloaded from the following link: https://1drv.ms/u/s!As_geBXhgCy1qwa3-NdukNHbLRsb?e=NT3Abi. The labels corresponding to each file in the training dataset can be found in the "train.xls" file. Object detectors trained on hand-labelled data were tested on the same images as the gaze-trained classifier. Therefore, the label file: *Gaze_Data/test.xlx* and the images in the *Gaze_Data/images/test_png* directory should be used for testing purposes. **@komal:** *Please verify that the preceding statement is correct? I recommend putting Test images in the HAND data instead of the GAZE data to avoid confusion. We're testing both detectors on Hand labels so it makes more sense to have the test data in the Hand Data director.*

**- Masks:** The binary masks used for generating labels for hand and gaze-based object detectors can be downloaded from the following links: https://1drv.ms/u/s!As_geBXhgCy1rBzg_A3ssuabn6TF?e=MD21iT

## Models
- Pre-trained models: https://1drv.ms/u/s!As_geBXhgCy1rSjYGEV7aMdLiYnr?e=qLZOUz
- Raw [Faster RCNN Inception V2 weights](http://download.tensorflow.org/models/object_detection/faster_rcnn_inception_v2_coco_2018_01_28.tar.gz) 

## Training
(under construction)

Download raw Faster RCNN Inception V2 Weight.

Now, to initiate a new training job, open a new Terminal, cd inside the models/research/object_detection folder and run the following command:
```
python model_main_tf2.py --model_dir=models/my_ssd_resnet50_v1_fpn --pipeline_config_path=models/my_ssd_resnet50_v1_fpn/pipeline.config
```
```
python model_main.py --model_dir=C:\Thesis\tensorflow1\models\research\object_detection\training\faster_rcnn_inception_v2_coco_2018_01_28 --pipeline_config_path=C:\Thesis\tensorflow1\models\research\object_detection\training\training_pipeline.config 
```
## Evaluation
Download and extract Gaze-based and Hand-Annotated trained models to 'saved_models' directory. <add link>

  Run Evaluation.ipynb notebook.

## Reference
This repo was used to generate the results for the following paper on Gaze-based labelling of Pathology data. 
   
   Komal Mariam, Osama Mohammed Afzal, Wajahat Hussain, Muhammad Umar Javed, Amber Kiyani, Nasir Rajpoot, Syed Ali Khurram and Hassan Aqeel Khan, **"On Smart Gaze based Annotation of Histopathology Images for Training of Deep Convolutional Neural Networks",** *submitted to IEEE Journal of Biomedical and Health Informatics.*


**BibTex Reference:** Available after acceptance.
