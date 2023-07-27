from flask import Flask, render_template
from flask_socketio import SocketIO, emit
from run_inference import predict_people

# Initialize the app
app = Flask(__name__, instance_relative_config = True)
app.config.from_object('config')

# Making a socketio object
socketio = SocketIO(app)

num_people = predict_people()

@app.route('/', methods=['GET'])
def index():
    return render_template("index.html", num_people=num_people)

@socketio.on('connect', namespace='/')
def test_connect():
    emit('after connect', {'data':'Connection successful!'})
    print('Client connected')

@socketio.on('Update histogram', namespace='/')
def update_num_people(data):
    print(data)
    num_people_and_time = predict_people()
    csv_file = open('people_time_data.csv', 'a')
    csv_file.write(f'{num_people_and_time["count"]}, {num_people_and_time["timestamp"]}\n')
    csv_file.close()
    emit('update count of people', num_people_and_time, broadcast=True)

@socketio.on('disconnect', namespace='/')
def test_disconnect():
    print('Client disconnected')

# load the views
# from app import views

# load the config file

# Include SocketIO
