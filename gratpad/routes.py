from flask import render_template, flash, redirect, url_for
from flask import app
from gratpad.models import User, Journal
from gratpad.forms import RegisterForm, LoginForm

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


with app.app_context():
    db.create_all()


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