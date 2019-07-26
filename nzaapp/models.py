from flask_sqlalchemy import SQLAlchemy
from nzaapp import app
from werkzeug.security import generate_password_hash, check_password_hash


db=SQLAlchemy(app)


class Username (db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)  
    password= db.Column(db.String(256), nullable=False)

    def __init__ (self,username, email,password):
        self.username=usernameself
        self.email=email
        self.password=passwords

    def __repr__(self):
        return "{} has been created".format(self.username)
    
    def set_password(self, password):
        self.pw_hash= generate_password_hash(password)
        return self.pw_hash
    
    def check_password(self,password):
        return check_password_hash(self.pw_hash. password)

class Review (db.Model):
    id=db.Column(db.Integer, primary_key=True)
    email_address= db.Column(db.String(100))
    name=db.Column(db.String(100))
    review=db.Column(db.String(250))

class Comment (db.Model):
    id=db.Column(db.Integer, primary_key=True)
    email_address= db.Column(db.String(100))
    first_name=db.Column(db.String(100))
    last_name=db.Column(db.String(100))
    comment=db.Column(db.String(250))
    phone_number=db.Column(db.String(100))

