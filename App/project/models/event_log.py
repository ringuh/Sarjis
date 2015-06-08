# -*- coding: utf-8 -*-
from project import db
from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship
import datetime

class Event_log(db.Model):

	__tablename__ = "event_log"

	id = db.Column(db.Integer, primary_key=True)
	user_id = db.Column(db.Integer, 
		ForeignKey('user.id'), nullable=True)
	ip = db.Column(db.UnicodeText)
	kategoria = db.Column(db.UnicodeText)
	viesti = db.Column(db.UnicodeText)
	
	date_created = db.Column(db.DateTime, default=datetime.datetime.now)
	#master_id = db.Column(db.Integer, ForeignKey('user.id'))
	#joukkueet = relationship("Joukkue", lazy="dynamic", backref="organisaatio")
	#testitulokset = relationship("Testitulos", backref="Orgatestitulokset")



	def __init__(self, kategoria, viesti, ip, user_id=None):
		self.user_id = user_id
		self.kategoria = kategoria
		self.viesti = viesti
		self.ip = ip
		
	def __repr__(self):	
		return '{}:google_reg_id'.format(self.id)	

	def toJson(self):
		ret = {c.name: getattr(self, c.name) for c in self.__table__.columns}
		ret["date_created"] = str(self.date_created)[0:22]
		if self.user_id is not None:
			ret["user"] = self.user.email
		return ret