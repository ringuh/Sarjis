# -*- coding: utf-8 -*-
from flask import Flask, request, g, session
from flask.ext.sqlalchemy import SQLAlchemy
from flask.ext.login import LoginManager, current_user
from flask.ext.triangle import Triangle

app = Flask(__name__)
app.config.from_object('config.BaseConfig')

db = SQLAlchemy(app)
Triangle(app)
login_manager = LoginManager()
login_manager.init_app(app)

#from project.users.views import user_blueprint
#app.register_blueprint(user_blueprint)

from project.explorer import explorer_blueprint
app.register_blueprint(explorer_blueprint)


login_manager.login_view = 'explorer.index'

@app.before_request
def before_request():
	"jotain ennen requestia"

@login_manager.user_loader
def load_user(id):
    from project.models import User
    return User.query.get(int(id))


@app.errorhandler(500)
def page_not_found(e):
    return "Sorry. There was some kind of error on our server. :(", 500

@app.errorhandler(404)
def page_not_found(e):
    return "Sorry. No such page on our server. :(", 404
