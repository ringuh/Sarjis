# -*- coding: utf-8 -*-
from project import db
from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship
import datetime

class Sarjakuva(db.Model):

	__tablename__ = "sarjakuva"

	id = db.Column(db.Integer, primary_key=True)
	nimi = db.Column(db.UnicodeText)
	author = db.Column(db.UnicodeText)
	url = db.Column(db.UnicodeText)
	last_url = db.Column(db.UnicodeText)
	parseri = db.Column(db.Integer)
	interval = db.Column(db.Integer, default=6) # tunteja
	last_parse = db.Column(db.DateTime)
	date_created = db.Column(db.DateTime, default=datetime.datetime.now)
	#joukkue_id = db.Column(db.Integer, ForeignKey('joukkue.id'), nullable=True)
	
	#parents = relationship("User_has_child", foreign_keys="User_has_child.child_id", lazy="dynamic", backref="child")
	#fh_players = relationship("Fh_pelaaja_seuranta", lazy="dynamic", backref="user")

	# relationships
	stripit = relationship("Strippi", lazy="dynamic", backref="sarjakuva")


	def __init__(self, nimi, url=None, author=None, parseri=None, last_url=None ):
		self.nimi = nimi
		self.url = url
		self.author = author
		self.parseri = parseri
		self.last_url = last_url


	def __repr__(self):	
		return self.toJson()

	def toJson(self):
		ret = {c.name: getattr(self, c.name) for c in self.__table__.columns}
		ret["date_created"] = str(self.date_created)
		ret["last_parse"] = str(self.last_parse)
		return ret

	def Max(self):
		from project.models import Strippi
		count = db.session.query(Strippi).filter(
			Strippi.sarjakuva_id == self.id).count()

		return count

	def Last(self):
		from project.models import Strippi
		ret = None
		ret = db.session.query(Strippi).filter(
			Strippi.sarjakuva_id == self.id).order_by(
					Strippi.id.desc()).first()
		return ret

	def UserStatus(self, id):
		from project.models import Sarjakuva_user as SKU
		ret = True

		n = db.session.query(SKU).filter(
				SKU.sarjakuva_id == self.id,
				SKU.user_id == id ).first()
		if n is not None:
			ret = n.visibility

		return ret

	def StatusJson(self, id):
		ret = self.toJson()
		ret["visibility"] = self.UserStatus(id)

		return ret




