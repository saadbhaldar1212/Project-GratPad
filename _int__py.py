from flask import Flask, render_template, url_for
'''from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin
'''
app = Flask(__name__, template_folder='template')
'''db = SQLAlchemy(app)
app.config['SQLACHEMY_DATABASE_URI'] = 'sqlite///database.db'
app.config['SECRET_KEY'] = '1234'

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), nullable=False)
    password = db.Column(db.String(80), nullable=False)
'''
@app.route("/")
def index():    
    return render_template('userHomePage.html')

@app.route("/contactus")
def contact():
    return render_template('userContactPage.html')

@app.route("/userSignIn")
def userSignIn():
    return render_template('userSignIn.html')

@app.route("/userSignUp")
def userSignUp():
    return render_template('userSignUp.html')

if __name__ == '__main__':
    app.run(debug=True)
