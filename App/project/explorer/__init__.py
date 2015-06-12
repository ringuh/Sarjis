# -*- coding: utf-8 -*-
from flask import flash, redirect, render_template, request, url_for, Blueprint
from project import db
from flask.ext.login import current_user, login_required, login_user, logout_user
from sqlalchemy import desc, func, and_, or_
from project.models import Sarjakuva as SK, Strippi, User, Brute_force, Event_log
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
					Strippi.sarjakuva_id == kwargs["comic"].id,
					Strippi.order == kwargs["strip"]
				).first()
			if n is None:
				n = db.session.query(Strippi).filter(
					Strippi.sarjakuva_id == kwargs["comic"].id
				).first()
		if n is None:
			flash(u"Strippi puuttuu")
			return redirect(url_for("explorer.comic", comic=kwargs["comic"].nimi))
		kwargs["strip"] = n
		return f(*args, **kwargs)
	return decorated_function




#def index():
#	return pvm(None)

	
@explorer_blueprint.route('/')
@explorer_blueprint.route('/d/<pvm>/')
def index(pvm=None):
	try:
		now = datetime.datetime.strptime(pvm, "%Y-%m-%d")
	except Exception, e:
		now = datetime.datetime.now()
	
	today = datetime.datetime(now.year, now.month, now.day)
	
	yesterday = today - datetime.timedelta(days=1)
	tomorrow = today + datetime.timedelta(days=1)
	dates = dict(	yesterday=yesterday.strftime("%Y-%m-%d"),
					day=today.strftime("%Y-%m-%d"),
					tomorrow=tomorrow.strftime("%Y-%m-%d"),
					next_day=datetime.datetime.now() > tomorrow
				)
	stripit = db.session.query(Strippi).filter(
				Strippi.date_created >= today, 
				Strippi.date_created < tomorrow ).limit(100).all()
	
	return render_template("portal.html", page="index", 
		dates=dates, stripit=stripit, user=current_user)


@explorer_blueprint.route('/<comic>/')
@login_required
@Comic
def comic(comic):
	return redirect(url_for("explorer.comic_strip", page="comic", comic=comic.nimi, strip=1))

@explorer_blueprint.route('/<comic>/<int:strip>/')
@Comic
@Strip
def comic_strip(comic, strip):
	return render_template("strip.html", page=None, comic=comic, strip=strip, user=current_user)

@explorer_blueprint.route('/list/')
@login_required
def list():
	n = db.session.query(SK).order_by(SK.id).all()
	return render_template("list.html", page="list", comics=n, user=current_user)

@explorer_blueprint.route('/login/', methods=["POST"])
def login():
	from project.models import User
	json = request.get_json(True)
	try:
		account = json["account"].strip().lower()
		passwd = json["password"].strip()
		ip = request.environ['REMOTE_ADDR']
		db.session.add(Event_log(u"Kirjautumisyritys", 
									u"{}//{}".format(account, len(passwd)), 
									ip))
		
		db.session.commit()
		n = Brute_force(ip)
		
		if n.count() > 15:
			flash(u"IP väliaikaisesti estetty. Koita myöhemmin uudestaan.")
			db.session.add(Event_log(u"Kirjautuminen estetty", 
									u"{}//{}".format(account, len(passwd)), 
									ip))
		
		user = User.query.filter(func.lower(User.account)==func.lower(account)).first()
		if user is not None and user.verify_pass(passwd):
				print user.account
				login_user(user, True) # kirjataan käyttäjä current_useriksi
				
				if user.last_login_date is not None and user.account != "vieras":
					flash(u"Last login {} from ip {}"\
						.format(user.last_login_date, user.last_login_ip ))
				user.last_login_date = datetime.datetime.now()
				user.last_login_ip = ip
				
				db.session.add(Event_log(u"Kirjautumisyritys", 
									u"{}//{}".format(account, len(passwd)), 
									ip, user.id))
				db.session.commit()
				flash(u"Kirjauduit sisään")
		else:
			flash(u"Virheellinen kirjautuminen nro: {}".format(n.count()+1))
			db.session.add(n)
			db.session.commit()

	except Exception, e:
		flash(u"{}".format(e.message))
		return "0"
	
	return "1"
	

@explorer_blueprint.route('/logout/')
@login_required
def logout():
	logout_user()
	flash(u"Kirjauduit ulos")

	return redirect(url_for("explorer.index"))