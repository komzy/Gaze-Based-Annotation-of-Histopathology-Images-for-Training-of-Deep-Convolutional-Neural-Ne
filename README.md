# Gaze Based Annotation of Histopathology Images for Training of Deep Convolutional Neural Networks
(under construction)

## Requirements
- Tensorflow 2.x
- Python 3.x
- Qupath
- MATLAB (masks to bounding box conversion)
- Google Colab or Jupyter Notebook

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

(under construction)

## Evaluation
Download and extract Gaze-based and Hand-Annotated trained models to 'saved_models' directory. <add link>

  Run Evaluation.ipynb notebook.
