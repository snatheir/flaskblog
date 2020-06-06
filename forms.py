from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField
from wtforms import InputRequired, Length, Email, EqualTo

class RegistrationForm(FlaskForm):
    username = StringField('Username', validators=[InputRequired(), Length(min=2, max=20)]) 

    email = StringField('Email', validators=[InputRequired(), Email()])

    password = PasswordField('Password', validators=[InputRequired()])
    confirm_password = PasswordField('Confirm Password', validators=[InputRequired(), EqualTo('password')])

    submit = SubmitField('Sign Up')


class LoginForm(FlaskForm):
    email = StringField('Email', validators=[InputRequired(), Email()])

    password = PasswordField('Password', validators=[InputRequired()])
    remember = BooleanField('Remember Me')

    submit = SubmitField('Login')