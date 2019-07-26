from wtforms import StringField,PasswordField,SubmitField
from wtforms.validators import input_required, EqualTo,Email
from flask_wtf import FlaskForm 

class LoginForm(FlaskForm):
    username = StringField("Username", validators=[input_required()])
    password=PasswordField("Password", validators=[input_required()])
    submit = SubmitField() 

class RegisterForm(FlaskForm):
    username= StringField("Username", validators=[input_required()])
    email= StringField("Email", validators=[input_required()])
    password= PasswordField("Password", validators=[input_required()])
    confirm_pass=PasswordField("Confirm Password", validators=[input_required()])
    submit = SubmitField()

class ContactForm (FlaskForm):
    first_name= StringField("First Name", validators=[input_required()])
    last_name= StringField("Last Name", validators=[input_required()])
    phone= StringField("Phone Number", validators=[input_required()])
    email=StringField("Email Address", validators=[input_required()])
    comment=StringField("Comment", validators=[input_required()])
    submit = SubmitField()

class ReviewForm (FlaskForm):
    email= StringField("First Name", validators=[input_required()])
    first_name= StringField("First Name", validators=[input_required()])
    last_name= StringField("Last Name", validators=[input_required()])
    comment=StringField("Leave a Review", validators=[input_required()])
    submit = SubmitField()