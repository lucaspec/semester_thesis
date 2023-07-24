# Semester Thesis

This repository is part of my semester thesis called "Hand-Detection for Sign Language Aid on Android-Based Smart Glasses" which inlcudes the following work: 
1. Training of various YOLOv5 and YOLOv7 models for the task of hand detection using the HaGRID dataset
2. Conversion process from PyTorch to TensofFlow Lite with the help of OpenVino and also Quantization
3. Development of an Android app which is capable of running inference on the CPU and GPU via NNAPI
4. Evaluation of accuracy and inference time of different models

## Navigation

An overview of each folder and its contents:
- ```/deliverables``` includes the report, the final presentation, the declaration of originality and project assignment
- ```/models``` contains all the model configurations that were trained on the ETH server using pytorch
- ```/related-work``` is a compilation of papers that were relevant to this project
- ```/results``` comprises all results compiled into an excel file with numerous plots
- ```/software``` contains the source code and external repos which were modified to fit the needs of this project:
    - ```./yolov5``` and ```./yolov7``` are the official YOLO repositories used for training, exportation (to ONNX) and evaluation
    - ```./hagrid``` is the official HaGRID repo (the hand dataset used for this project) and includes annotation conversion scripts amongst other things
    - ```./android``` contains a simple Android test app, a PyTorch based Hand Detection App (for YOLOv7) and a TensorFlow Lite based Hand Detection App (for YOLOv5). It also includes the OpenVino conversion and quantization scripts.

## Results

Following plots summarize the most important results: 
![Alt Text](https://git.ee.ethz.ch/pbl/fs2023/luca-specht/-/tree/main/report/images/results_table.png?raw=true)
![Alt Text](https://git.ee.ethz.ch/pbl/fs2023/luca-specht/-/tree/main/report/images/results_pareto.png?raw=true)