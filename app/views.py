from run_inference import predict_people
from flask import render_template
from app import app, socketio

num_people = predict_people()

@app.route('/', methods=['GET'])
def index():
    return render_template("index.html", num_people=num_people)

@socketio.on('connect', namespace='/')
def test_connect():
    print('Client connected')

@socketio.on('disconnect', namespace='/')
def test_disconnect():
    print('Client disconnected')

# @app.route('/about')
# def about():
#     return render_template("about.html")