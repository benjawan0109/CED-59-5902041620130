<<<<<<< HEAD
from flask import Flask,render_template

app = Flask(__name__)

@app.route('/')
def login():
    return render_template('login1.html')

@app.route('/',methods=["post"])
def register():
    return 'xyz'

if __name__ == '__main__':
    app.run()
=======
from flask import Flask
from flask import render_template


app = Flask(__name__)



@app.route("/")
def login(): 
    return render_template('login.html')



if __name__ == '__main__':
    app.run(debug=True)
>>>>>>> 526d60a24d2ca9a9942ada914bc2b93e5d96ab13
