from run_inference import predict_people
from flask import Flask, render_template, redirect

# num_people = predict_people()
num_people = 2

app = Flask(__name__)

@app.route('/', methods=['GET'])
def index():    
    return render_template('./index.html', num_people=num_people)


if __name__ == '__main__':
    app.run()
    