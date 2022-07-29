# YOLOV5 training

 we are using yolov5s model for our project. So we will finetune it on our datasets.

 Steps
 1) clone yolov5s in your project root dir
```
git clone https://github.com/ultralytics/yolov5.git
``` 
 2) Now take a copy of coco.yaml(yolov5/data/coco.yaml) and rename it custom_data.yaml. And provide your data path and no of class e.g:
```
path: ../data/  # dataset root dir
train: ../data/train/images  # train images (relative to 'path') 118287 images
val: ../data/test/  # val images (relative to 'path') 5000 images
test: ../data/test/  # 20288 of 40670 images, submit to https://competitions.codalab.org/competitions/20794

# Classes
nc: 6  # number of classes
names: ['Hello', 'IloveYou', 'No', 'Please', 'Thanks', 'Yes'] 
```  
 3) Take the copy of yolov5s.yaml (yolov5/models/yolos.yaml) and rename it custom_yolos.yaml. And change no of class as per your requirements e.g:
```
nc: 6  
```
