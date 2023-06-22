from ultralytics import YOLO
import os


model = YOLO("yolov8n.pt")
image_files = [os.path.join("./data/video/frames/", f) for f in os.listdir("./data/video/frames/")]

# counter for number of people
num_people = 0

for image in image_files:
    results = model(image, classes=0)
    num_people = results[0].boxes.data.size()[0]

print(f"In a 20 second clip of the livestream, YOLOv8 found {num_people} people!")
    