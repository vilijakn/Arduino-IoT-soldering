from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField
from wtforms.validators import DataRequired, Length, Email, EqualTo

class Registration(FlaskForm):
    username = StringField('username:', validators=[DataRequired(), Length(min=4, max=20)])
    email = StringField('email:', validators=[DataRequired(), Email()])
    password = PasswordField('password:', validators=[DataRequired()])
    password_confirmation = PasswordField('password confirmation:', validators=[DataRequired(),EqualTo('password')])
    submit = SubmitField('Sign up!')

class Login(FlaskForm):
    username = StringField('username:', validators=[DataRequired(), Length(min=4, max=20)])
    password = PasswordField('password:', validators=[DataRequired()])
    #remember = BooleanField('remember login')
    submit = SubmitField('Login')
