# Training on custom data

Go inside yolov5 and use below cmd.(if GPU not available then use device as CPU)
```
python train.py --img 400 --batch 16 --epochs 3 --data data/custom_data.yaml --weights yolov5s.pt --cfg custom_yolov5s.yaml --device 0

```