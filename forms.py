from operator import length_hint
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField
from wtforms.validators import *

class registrationform(FlaskForm):
    username = StringField('username', validators=[DataRequired(), Length(min=2, max=20)])
    email = StringField("email", validators=[DataRequired(), Email()])
    password = PasswordField("password", validators=[DataRequired(), Length(min=8, max=100)])
    confirm_password = PasswordField("confirm_password", validators=[DataRequired(), EqualTo("password")])

    submit = SubmitField("Sign Up")


class Loginform(FlaskForm):
    email = StringField("email", validators=[DataRequired(), Email()])
    password = PasswordField("password", validators=[DataRequired(), Length(min=8, max=100)])
    remember = BooleanField("remember me")

    submit = SubmitField("Login")