from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:@localhost/db_name'
app.config['SECRET_KEY'] = '1234'
db = SQLAlchemy()


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), nullable=False)
    password = db.Column(db.String(80), nullable=False)


@app.route("/")
def index():
    return render_template('userHomePage.html')


@app.route("/welcomePage")
def mainPage():
    return render_template('userMainPage.html')


@app.route("/contactus")
def contact():
    return render_template('userContactPage.html')


@app.route("/about")
def about():
    return 'About us'


@app.route("/userSignIn")
def userSignIn():
    return render_template('userSignIn.html')


@app.route("/userSignUp")
def userSignUp():
    return render_template('userSignUp.html')


if __name__ == '__main__':
    app.run(debug=True)
