from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
@app.route('/bday.html')
@app.route('/start.html')
@app.route('/dinesh.html')
@app.route('/Birthday.html')
@app.route('/about.html')
def index():
    return render_template('index.html')


def dinesh():
    return render_template('dinesh.html')


def start():
    return render_template('start.html')


def Birthday():
    return render_template('Birthday.html')


def about():
    return render_template('about.html')

def bday():
    return render_template('bday.html')