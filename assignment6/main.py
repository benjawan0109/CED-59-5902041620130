from flask import Flask,render_template

app = Flask(__name__)


@app.route('/')
def login():
    return render_template('login.html')
@app.route('/', methods=["POST"])
def chack():
    return '...login...'
@app.route('/', methods=["POST"])
def test():
    return 'xyz';

if __name__ == '__main__':
    app.run()
