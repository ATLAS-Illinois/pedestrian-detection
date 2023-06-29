from flask import Flask, render_template
from ultralytics import YOLO
import os

app = Flask(__name__)

@app.route('/')
def home():
    model = YOLO("yolov8n.pt")
    image_files = [os.path.join("./data/video/frames/", f) for f in os.listdir("./data/video/frames/")]

    # counter for number of people
    num_people = 0

    for image in image_files:
        results = model(image, classes=0, imgsz=1280)
        num_people += results[0].boxes.data.size()[0]
    
    return render_template('./index.html', num_people=num_people)

if __name__ == '__main__':
    app.run()
    