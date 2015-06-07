# -*- coding: utf-8 -*-
from flask import flash, redirect, render_template, request, url_for, Blueprint
from project import db
from sqlalchemy import desc, func, and_, or_
from project.models import Sarjakuva as SK, Strippi
import datetime
explorer_blueprint = Blueprint('explorer', __name__, 
					template_folder='templates',
					static_url_path='/explorer/static',
					static_folder='static' )

def Comic(f):
	from functools import wraps
	@wraps(f)
	def decorated_function(*args, **kwargs):
		n = db.session.query(SK).filter(
				func.lower(SK.nimi) == func.lower(kwargs["comic"])
			).first()
		if n is None:
			flash(u"Tuntematon sarjakuva")
			return redirect(url_for("explorer.index"))
		kwargs["comic"] = n
		return f(*args, **kwargs)
	return decorated_function

def Strip(f):
	from functools import wraps
	@wraps(f)
	def decorated_function(*args, **kwargs):
		n = None
		if kwargs["strip"] > 0:
			n = db.session.query(Strippi).filter(
					Strippi.sarjakuva_id == kwargs["comic"].id
				).offset(kwargs["strip"]-1).first()
		if n is None:
			flash(u"Strippi puuttuu")
			return redirect(url_for("explorer.comic", comic=kwargs["comic"].nimi))
		kwargs["strip"] = n
		return f(*args, **kwargs)
	return decorated_function

@explorer_blueprint.route('/')
def index():
	now = datetime.datetime.now()
	today = datetime.datetime(now.year, now.month, now.day)
	stripit = db.session.query(Strippi).filter(Strippi.date_created >= today ).all()
	return render_template("portal.html", stripit=stripit, user=None)

@explorer_blueprint.route('/<comic>/')
@Comic
def comic(comic):
	return redirect(url_for("explorer.comic_strip", comic=comic.nimi, strip=1))

@explorer_blueprint.route('/<comic>/<int:strip>/')
@Comic
@Strip
def comic_strip(comic, strip):
	return render_template("strip.html", comic=comic, strip=strip, user=None)

@explorer_blueprint.route('/list/')
def list():
	n = db.session.query(SK).order_by(SK.nimi).all()
	return render_template("list.html", comics=n, user=None)
