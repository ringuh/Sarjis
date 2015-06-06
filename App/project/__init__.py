# -*- coding: utf-8 -*-
from flask import Flask, request, g, session
from flask.ext.sqlalchemy import SQLAlchemy
from flask.ext.login import LoginManager, current_user
from flask.ext.triangle import Triangle

app = Flask(__name__)
app.config.from_object('config.BaseConfig')

db = SQLAlchemy(app)
Triangle(app)

#from project.users.views import user_blueprint
#app.register_blueprint(user_blueprint)

from project.explorer import explorer_blueprint
app.register_blueprint(explorer_blueprint)