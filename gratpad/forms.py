
from wtforms import StringField, PasswordField, SubmitField, EmailField
from wtforms.validators import InputRequired, Length, ValidationError, EqualTo, DataRequired, Email
from flask_login import login_required, logout_user
from flask_wtf import FlaskForm



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