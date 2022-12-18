from datetime import datetime

from flask import Flask, render_template, flash, redirect, url_for
from flask_login import UserMixin, LoginManager, login_required, logout_user
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, EmailField
from wtforms.validators import InputRequired, Length, ValidationError, EqualTo, DataRequired, Email


app = Flask(__name__, template_folder='template')

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
app.config['SECRET_KEY'] = '1234'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = "mainPage"

journals = [
    {
        'time': '12',
        'title': 'Fist Journal',
        'desc': 'hello this is my first Blog'
    },
    {
        'time': '6',
        'title': 'Second Journal',
        'desc': 'hello this is my recent Blog'
    },
    {
        'time': '21',
        'title': 'Second Journal',
        'desc': 'hello this is my recent Blog'
    }
]


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


class User(db.Model):
    u_id = db.Column(db.Integer, primary_key=True)
    u_uname = db.Column(db.String(length=100), nullable=False)
    u_email = db.Column(db.String(length=100), nullable=False, unique=True)
    u_pass = db.Column(db.String(length=100), nullable=False)
    u_repass = db.Column(db.String(length=100), nullable=False)
    u_journal = db.relationship(nullable=False, backref='j_author', lazy=True)

    def __repr__(self):
        return f'User("{self.u_uname}","{self.u_email}")'


class Journal(db.Model):
    j_id = db.Column(db.Integer, primary_key=True)
    j_dateTime = db.Column(db.String(50), nullable=True, default=datetime.utcnow)
    j_title = db.Column(db.String(50), nullable=False)
    j_content = db.Column(db.Text, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.u_id'), nullable=False)

    def __repr__(self):
        return f'User("{self.j_dateTime}","{self.j_title}")'


'''
class Contact(db.Model):
    c_id = db.Column(db.Integer, primary_key=True)
    c_fname = db.Column(db.String(100), nullable=False)
    c_lname = db.Column(db.String(100), nullable=False)
    c_email = db.Column(db.String(100), nullable=False)
    c_msg = db.Column(db.String(200), nullable=False)



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


    def validate_username(u_email):
        existing_user_username = User.query.filter_by(
            u_email=u_email.data).first()

        if existing_user_username:
            raise ValidationError(
                'Username already exists. Please chose a different username'
            )


    class RegisterForm(FlaskForm):
        u_name = StringField('Name', validators=[InputRequired(), Length(
            min=4, max=200), DataRequired()], render_kw={"placeholder": "Username"})
        u_email = EmailField('Email', validators=[InputRequired(), Length(
            min=4, max=200), DataRequired(), Email()], render_kw={"placeholder": "Email"})
        u_pass = PasswordField('Password', validators=[InputRequired(), Length(
            min=4, max=200)], render_kw={"placeholder": "Password"})
        u_repass = PasswordField('Re-enter Password', validators=[InputRequired(), Length(
            min=4, max=200), EqualTo('u_pass')], render_kw={"placeholder": "Re-enter Password"})
        submit = SubmitField("Register")


    class LoginForm(FlaskForm):
        u_email = EmailField('Email', validators=[InputRequired(), Length(
            min=4, max=200), DataRequired(), Email()], render_kw={"placeholder": "Email"})
        u_pass = PasswordField(validators=[InputRequired(), Length(
            min=4, max=200)], render_kw={"placeholder": "Password"})
        submit = SubmitField("Login")


@app.route("/", methods=['GET', 'POST'])
def index():
    form1 = RegisterForm()
    if form1.validate_on_submit():
        flash(f'Account created for {form1.u_name.data}!', 'success')
    else:
        flash('Invalid credentials', 'danger')

    return render_template('userHomePage.html', form=form1)


@app.route("/logIn", methods=['GET', 'POST'])
def userSignIn():
    form2 = LoginForm()
    if form2.validate_on_submit():
        if form2.u_email.data == 'saadbhaldar1212@gmail.com' and form2.u_pass.data == 'Saad@1212':
            return redirect(url_for('mainPage'))
        else:
            return redirect(url_for('index'))
            flash('Invalid credentials', 'danger')

    return render_template('userSignIn.html', form=form2)


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


@app.route("/thank_you", methods=['GET', 'POST'])
@login_required
def thankyou():
    logout_user()
    return render_template('/components/thank_you.html')


@app.route("/journal", methods=['GET', 'POST'])
def journal():
    return render_template('journal.html', journals=journals)


@app.route("/merchandise")
def merchandise():
    return render_template('merchandise.html')


@app.route("/user/<username>")
def dynamic(username):
    return f"<h1> Welcome {username} </h1>"


if __name__ == '__main__':
    app.run(debug=True)
