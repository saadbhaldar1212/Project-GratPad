from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def hello_world():
    return render_template('userHomePage.html')


@app.route("/harry")
def hello_world1():
    return "<p>Hello, Harry!</p>"


app.run(debug=True)
