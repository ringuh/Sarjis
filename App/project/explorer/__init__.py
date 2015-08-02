# -*- coding: utf-8 -*-
from flask import flash, redirect, render_template, request, url_for, Blueprint, jsonify
from project import db
from flask.ext.login import current_user, login_required, login_user, logout_user
from sqlalchemy import desc, func, and_, or_
from project.models import Sarjakuva as SK, Strippi, User, Brute_force, Event_log,\
Sarjakuva_user as SKU
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
				func.lower(SK.lyhenne) == func.lower(kwargs["comic"])
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
	if current_user.is_anonymous():
		return render_template("portal.html", page="index", 
			dates=None, stripit=None, user=current_user)
	today = datetime.datetime(now.year, now.month, now.day)
	
	yesterday = today - datetime.timedelta(days=1)
	tomorrow = today + datetime.timedelta(days=1)
	dates = dict(	yesterday=yesterday.strftime("%Y-%m-%d"),
					day=today.strftime("%Y-%m-%d"),
					tomorrow=tomorrow.strftime("%Y-%m-%d"),
					next_day=datetime.datetime.now() > tomorrow
				)
	karsitut = current_user.getKarsitut()

	stripit = db.session.query(Strippi).filter(
				Strippi.date_created >= today, 
				Strippi.date_created < tomorrow,
				~Strippi.sarjakuva_id.in_(karsitut) ).limit(100).all()

	return render_template("portal.html", page="index", 
		dates=dates, stripit=stripit, user=current_user)

@explorer_blueprint.route('/list/')
@login_required
def list():
	n = db.session.query(SK).filter(
			~SK.id.in_(current_user.getKarsitut())).order_by(SK.id).all()
	return render_template("list.html", page="list", comics=n, user=current_user)


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




@explorer_blueprint.route('/options/')
@login_required
def options():
	n = db.session.query(SK).order_by(SK.id).all()
	comics = [i.toJson() for i in n]

	users = None
	if current_user.admin:
		users = db.session.query(User).all()

	return render_template("options.html", page="options", comics=comics, users=users, user=current_user)

@explorer_blueprint.route('/options/change_pass/', methods=["POST"])
@login_required
def change_pass():
	json = request.get_json(True)
	msg = None
	#print json
	msg = u"Ei tehty mitään"
	try:
		u = db.session.query(User).get(json["id"])
		if u.id == current_user.id and "old_pass" in json and u.verify_pass(json["old_pass"]):
			u.set_password(json["new_pass"])
			db.session.commit()
			msg = u"Vaihdettiin salasana"
		else:
			msg = u"Virheellinen salasana"
			if current_user.admin:
				try:
					u = db.session.query(User).get(json["id"])
					u.set_password(json["new_pass"])
					db.session.commit()
					msg = u"Salasanaksi asetettiin "+json["new_pass"]

				except Exception, e:
					msg = u"Salasanan asetus epäonnistui"

	except Exception, e:
		msg = u"Salasanan asetus epäonnistui"

	return jsonify(msg=msg)

@explorer_blueprint.route('/options/my_comics/', methods=["POST"])
@login_required
def my_comics():
	json = request.get_json(True)
	msg = None
	#print json
	if "id" in json and "visibility" in json:
		n = db.session.query(SKU).filter(
				SKU.sarjakuva_id == json["id"],
				SKU.user_id == current_user.id ).first()
		if n is None:
			db.session.add(SKU(json["id"], current_user.id, json["visibility"]))
			
		else:
			n.visibility = json["visibility"]
		db.session.commit()
		msg = u"Tallennettiin"

	tmp = db.session.query(SK).order_by(SK.nimi).all()
	comics = []
	for i in tmp:
		comics.append(i.StatusJson(current_user.id))

	return jsonify(comics=comics, msg=msg)

@explorer_blueprint.route('/options/users/', methods=["POST"])
@login_required
def users():
	json = request.get_json(True)
	msg = None
	#print json

	if not current_user.admin:
		return "error", 400

	tmp = db.session.query(User).order_by(User.id).all()
	users = [i.toJson() for i in tmp]

	return jsonify(users=users, msg=msg)

@explorer_blueprint.route('/options/users/take_over/', methods=["POST"])
@login_required
def take_over():
	json = request.get_json(True)
	msg = None

	if not current_user.admin:
		return "error", 400
	try:
		tmp = db.session.query(User).get(json["id"])
		logout_user()
		login_user(tmp)			
	except Exception, e:
		msg = u"Epäonnistui"
	
	

	return jsonify(msg=msg)

@explorer_blueprint.route('/options/users/register/', methods=["POST"])
@login_required
def register():
	json = request.get_json(True)
	msg = None
	#print json

	if not current_user.admin:
		return "error", 400
	try:
		db.session.add(User(json["account"].strip().lower(), json["password"].strip()))
		db.session.commit()
	except Exception, e:
		msg = u"Epäonnistui"
	
	

	return jsonify(msg=msg)


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


@explorer_blueprint.route('/add/', methods=["POST", "GET"])
@login_required
def add():
	from project.models import Sarjakuva as SK
	if not current_user.admin:
		return "loser";

	if request.method == "GET":
		sarjikset = db.session.query(SK).order_by(desc(SK.id)).all()
		return render_template("add.html", user=current_user, sarjikset=sarjikset)
	else:
		json = request.get_json(True)

		tmp = json["text"].strip()
		tmp = tmp.split("\n")

		add = []
		for i in tmp:
			i = i.strip();
			if i[0] == "u":
				i = i[1:]

			if i[-1] == ",":
				i = i[:-1]

			i = i.strip('"')

			if not i[0] in [")", "S"] and i != "":
				add.append(i)
			
		if len(add) == 6:
			db.session.add(SK(add[0], add[1], add[2], add[3], add[4], add[5]))
			db.session.commit()
			
		return jsonify(ret=add)