from ultralytics import YOLO
from datetime import datetime
from random import randint
import os

model = YOLO("yolov8sp2.pt")

def predict_people():
    # grabbing all image files
    image_files = [os.path.join("video/frames", f) for f in os.listdir("video/frames") if f.endswith(".png")]
    
    # grabbing current time
    current_time = datetime.now()
    
    # counter for number of people
    num_people = 0
    num_frames = len(image_files) if len(image_files) > 0 else 1
    # num_people = randint(1,100)
    
    for image in image_files:
        results = model.predict(image, imgsz=1280, conf=0.25)
        num_people += results[0].boxes.data.size()[0]
        os.remove(image)
    
    result = {
        'count': int(num_people/num_frames),
        'timestamp': current_time.strftime("%a %x %X") # day + date + time -> Mon, 09/30/13 07:06:05
    }
    return result
    