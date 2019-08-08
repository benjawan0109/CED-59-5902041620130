from flask import Flask,render_template

app = Flask(__name__)


@app.route('/')
<<<<<<< HEAD
def hello_world():
    return render_template('form.html')
@app.route('/', methods=["POST"])

def chack():
    return 'Welcome to page...'
@app.route('/', methods=["POST"])

def h2():
    return 'xyz';

if __name__ == '__main__':
    app.run()
=======
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
>>>>>>> 526d60a24d2ca9a9942ada914bc2b93e5d96ab13
