from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__, template_folder='template')

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:@localhost/gratpad'
app.config['SECRET_KEY'] = '1234'
db = SQLAlchemy()


class User(db.Model):
    u_id = db.Column(db.Integer, primary_key=True)
    u_uname = db.Column(db.String(100), nullable=False)
    u_email = db.Column(db.String(100), nullable=False)
    u_pass = db.Column(db.String(100), nullable=False)
    u_repass = db.Column(db.String(100), nullable=False)


class Login(db.Model):
    l_id = db.Column(db.Integer, primary_key=True)

    def __init__(self):
        super().__init__()


class Contact(db.Model):
    c_id = db.Column(db.Integer, primary_key=True)
    c_fname = db.Column(db.String(100), nullable=False)
    c_lname = db.Column(db.String(100), nullable=False)
    c_email = db.Column(db.String(100), nullable=False)
    c_msg = db.Column(db.String(200), nullable=False)


class Journal(db.Model):
    j_id = db.Column(db.Integer, primary_key=True)
    j_date = db.Column(db.String(50), nullable=True)
    j_time = db.Column(db.String(50), nullable=True)
    j_content = db.Column(db.String(5000), nullable=False)


class Product(db.Model):
    p_id = db.Column(db.Integer, primary_key=True)
    p_name = db.Column(db.String(100), nullable=False)
    p_desc = db.Column(db.String(100), nullable=False)
    p_price = db.Column(db.Float, nullable=False)
    p_quant = db.Column(db.Integer, nullable=False)
    p_img = db.Column(db.String(100), nullable=False)


class Admin(db.Model):
    a_id = db.Column(db.Integer, primary_key=True)
    a_uname = db.Column(db.String(100), nullable=False)
    a_pass = db.Column(db.String(100), nullable=False)


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


@app.route("/thank_you")
def thankyou():
    return render_template('/components/thank_you.html')


@app.route("/journal")
def journal():
    return render_template('journal.html')


@app.route("/merchandise")
def merchandise():
    return render_template('merchandise.html')


if __name__ == '__main__':
    app.run(debug=True)
