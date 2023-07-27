from flask import Flask, render_template
from flask_socketio import SocketIO, emit
from run_inference import predict_people
import csv

# Initialize the app
app = Flask(__name__, instance_relative_config = True)
app.config.from_object('config')

# Making a socketio object
socketio = SocketIO(app)

# num_people = predict_people()
last_line_read = 0

@app.route('/', methods=['GET'])
def index():
    return render_template("index.html")

@socketio.on('connect', namespace='/')
def test_connect():
    emit('after connect', {'data':'Connection successful!'})
    print('Client connected')

@socketio.on('Run inference', namespace='/')
def predict(data):
    print(data)
    num_people_and_time = predict_people()
    csv_file = open('people_time_data.csv', 'a')
    csv_file.write(f'{num_people_and_time["count"]}, {num_people_and_time["timestamp"]}\n')
    csv_file.close()

@socketio.on('Update histogram', namespace='/')
def update_num_people(data):
    print(data)
    # declare local and global variables
    global last_line_read
    count = 0
    
    with open('people_time_data.csv', 'r') as csvfile:
        csv_reader = csv.reader(csvfile, delimiter=',')
        total_lines = 0
        for _ in range(last_line_read):
            next(csv_reader)
        for row in csv_reader:
            total_lines += 1
            if len(row) > 0:
                try:
                    count += int(row[0]) # adding the first column
                except ValueError:
                    print(f"Skipping invalid entry: {row[0]}")
        last_line_read = total_lines
    
    emit('update count of people', {'num_people': count}, broadcast=True)

@socketio.on('disconnect', namespace='/')
def test_disconnect():
    print('Client disconnected')

# load the views
# from app import views

# load the config file

# Include SocketIO
