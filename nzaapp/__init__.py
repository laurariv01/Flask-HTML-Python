from flask import Flask
app = Flask(__name__)
import os
from flask_login import LoginManager

# Creating relative base directory
basedir = os.path.abspath(os.path.dirname(__file__))


login_manager= LoginManager(app)
login_manager.login_view= 'login'

app.config['SECRET_KEY']="Hello"

app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///" + os.path.join(basedir, 'data.db')
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
