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
		count = 0
		for i in self.stripit:
			count += 1

		return count

	def Last(self):
		ret = None
		for i in self.stripit:
			ret = i
		return ret





