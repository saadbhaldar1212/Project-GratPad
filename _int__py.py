from flask import Flask, render_template, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin, login_user, LoginManager, login_required, logout_user, current_user
from datetime import datetime
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import InputRequired, Length, ValidationError
from flask_bcrypt import bcrypt

app = Flask(__name__, template_folder='template')

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
app.config['SECRET_KEY'] = '1234'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = "mainPage"


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


class User(db.Model, UserMixin):
    u_id = db.Column(db.Integer, primary_key=True)
    u_uname = db.Column(db.String(length=100), nullable=False)
    u_email = db.Column(db.String(length=100), nullable=False, unique=True)
    u_pass = db.Column(db.String(length=100), nullable=False)
    u_repass = db.Column(db.String(length=100), nullable=False)


def validate_username(username):
    existing_user_username = User.query.filter_by(
        username=username.data).first()

    if existing_user_username:
        raise ValidationError(
            'Username already exists. Please chose a different username'
        )


class RegisterForm(FlaskForm):
    u_name = StringField('Name', validators=[InputRequired(), Length(
        min=4, max=20)], render_kw={"placeholder": "Username"})
    u_email = StringField('Email', validators=[InputRequired(), Length(
        min=4, max=20)], render_kw={"placeholder": "Email"})
    u_pass = PasswordField('Password', validators=[InputRequired(), Length(
        min=4, max=20)], render_kw={"placeholder": "Password"})
    u_repass = PasswordField('Re-enter Password', validators=[InputRequired(), Length(
        min=4, max=20)], render_kw={"placeholder": "Re-enter Password"})
    submit = SubmitField("Register")


class LoginForm(FlaskForm):
    u_email = StringField('Email', validators=[InputRequired(), Length(
        min=4, max=20)], render_kw={"placeholder": "Email"})
    u_pass = PasswordField(validators=[InputRequired(), Length(
        min=4, max=20)], render_kw={"placeholder": "Password"})
    submit = SubmitField("Login")


'''
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

'''
with app.app_context():
    db.create_all()


@app.route("/", methods=['GET', 'POST'])
def index():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(u_email=form.u_email.data).first()
        if user:
            if bcrypt.check_password_hash(user.u_pass, form.u_pass.data):
                logout_user(user)
                return redirect(url_for('mainPage'))
    return render_template('userSignIn.html', form=form)

    form = RegisterForm()

    if form.validate_on_submit():
        hashed_password = bcrypt.generate_password_hash(form.password.data)
        new_user = User(u_email=form.u_email.data, u_pass=hashed_password)
        db.session.add(new_user)
        db.session.commit()
        return redirect(url_for('userSignIn'))

    return render_template('userHomePage.html')


@app.route("/contactus")
def contact():
    return render_template('userContactPage.html')


@app.route("/about")
def about():
    return 'About us'


@app.route("/welcomePage", methods=['GET', 'POST'])
@login_required
def mainPage():
    return render_template('userMainPage.html')


@app.route("/userSignIn", methods=['GET', 'POST'])
def userSignIn():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(u_email=form.u_email.data).first()
        if user:
            if bcrypt.check_password_hash(user.u_pass, form.u_pass.data):
                logout_user(user)
                return redirect(url_for('mainPage'))
    return render_template('userSignIn.html', form=form)


@app.route("/thank_you", methods=['GET', 'POST'])
@login_required
def thankyou():
    logout_user()
    return render_template('/components/thank_you.html')


@app.route("/userSignUp", methods=['GET', 'POST'])
def userSignUp():
    form = RegisterForm()

    if form.validate_on_submit():
        hashed_password = bcrypt.generate_password_hash(form.password.data)
        new_user = User(u_email=form.u_email.data, u_pass=hashed_password)
        db.session.add(new_user)
        db.session.commit()
        return redirect(url_for('userSignIn'))

    return render_template('userSignUp.html', form=form)


@app.route("/journal")
def journal():
    return render_template('journal.html')


@app.route("/merchandise")
def merchandise():
    return render_template('merchandise.html')


@app.route("/user/<username>")
def dynamic(username):
    return f"<h1> Welcome {username} </h1>"


if __name__ == '__main__':
    app.run(debug=True)
