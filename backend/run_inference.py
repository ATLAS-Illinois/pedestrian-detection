from ultralytics import YOLO
import os

model = YOLO("yolov8n.pt")

def predict_people():
    image_files = [os.path.join("./data/video/frames/", f) for f in os.listdir("./data/video/frames/")]
    # counter for number of people
    num_people = 0

    for image in image_files:
        results = model(image, classes=0, imgsz=1280)
        num_people += results[0].boxes.data.size()[0]
    
    return num_people