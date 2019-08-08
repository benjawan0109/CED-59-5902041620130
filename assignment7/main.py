from flask import Flask,render_template
from flask_wtf import FlaskForm
from wtforms import StringField
from wtforms.validators import DataRequired

app = Flask(__name__)


@app.route('/')
def hello_world():
    return render_template('form.html')

@app.route('/', methods=["POST"])
def chack():
    return 'Welcome to page...'

@app.route('/', methods=["POST"])
def login():
    return 'ok'

if __name__ == '__main__':
    app.run()