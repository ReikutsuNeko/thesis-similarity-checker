import os

from flask import Flask, redirect
from flask_sqlalchemy import SQLAlchemy

# create and configure the app
app = Flask(__name__, instance_relative_config=True)

app.config.from_mapping(
    SECRET_KEY='changeme',
    # DATABASE=os.path.join(app.instance_path, 'flaskr.sqlite'),
)

# if test_config is None:
#     # load the instance config, if it exists, when not testing
#     app.config.from_pyfile('config.py', silent=True)
# else:
#     # load the test config if passed in
#     app.config.from_mapping(test_config)

# ensure the instance folder exists
try:
    os.makedirs(app.instance_path)
except OSError:
    pass

app.config['SQLALCHEMY_DATABASE_URI'] = 'changeme'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

import models

# a simple page that says hello
@app.route('/')
def index():
    return redirect("/home")

import auth
import home
app.register_blueprint(auth.bp)
app.register_blueprint(home.bp)

# def __init__(test_config=None):

    

#     # return app