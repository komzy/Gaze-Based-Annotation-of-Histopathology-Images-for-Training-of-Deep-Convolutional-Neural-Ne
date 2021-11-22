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
pip install lxml pillow matplotlib jupyter contextlib2 cython tf_slim
```

## Dataset
Follow the steps in \Generate_Annotations to create your own dataset from gaze and hand annotations.

Or simply download our dataset here:

- Gaze: https://1drv.ms/u/s!As_geBXhgCy1qjOElYHo5oWX_OQ0?e=L38qQ6
- Hand: https://1drv.ms/u/s!As_geBXhgCy1qwa3-NdukNHbLRsb?e=NT3Abi
- Masks: https://1drv.ms/u/s!As_geBXhgCy1rBzg_A3ssuabn6TF?e=MD21iT

## Models
Download pre-trained models: https://1drv.ms/u/s!As_geBXhgCy1rSjYGEV7aMdLiYnr?e=qLZOUz

Or train on your own dataset by downloading [Faster RCNN Inception V2 weights](http://download.tensorflow.org/models/object_detection/faster_rcnn_inception_v2_coco_2018_01_28.tar.gz) from Tensorflow model zoo. 

## Training


## Evaluation
Download and extract Gaze-based and Hand-Annotated trained models to 'saved_models' directory. <add link>

  Run Evaluation.ipynb notebook.
