from ultralytics import YOLO
import os

model = YOLO("yolov8sp2.pt")

def predict_people():
    image_files = [os.path.join("video/frames", f) for f in os.listdir("video/frames")]
    # counter for number of people
    num_people = 0

    for image in image_files:
        results = model.predict(image, imgsz=1280, conf=0.25)
        num_people += results[0].boxes.data.size()[0]
    
    return num_people
    