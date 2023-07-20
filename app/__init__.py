from flask import Flask, render_template
from flask_socketio import SocketIO, emit
from run_inference import predict_people
import random

# Initialize the app
app = Flask(__name__, instance_relative_config = True)
app.config.from_object('config')

# Making a socketio object
socketio = SocketIO(app)

# num_people = predict_people()
# num_people = random.randint(1,100)

@app.route('/', methods=['GET'])
def index():
    return render_template("index.html")

@socketio.on('connect', namespace='/')
def test_connect():
    emit('after connect', {'data':'Connection successful!'})
    print('Client connected')

@socketio.on('Update histogram', namespace='/')
def update_num_people(data):
    print(data)
    num_people = predict_people()
    emit('update count of people', {'count': num_people}, broadcast=True)

@socketio.on('disconnect', namespace='/')
def test_disconnect():
    print('Client disconnected')

# load the views
# from app import views

# load the config file

# Include SocketIO
