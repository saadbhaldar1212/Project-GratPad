from flask import Flask

app = Flask(__name__)


@app.route("/")
def hello_world():
    return "<p>Hello, Saad!</p>"


@app.route("/harry")
def hello_world1():
    return "<p>Hello, Harry!</p>"


app.run(debug=True)
