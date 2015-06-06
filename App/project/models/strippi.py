# -*- coding: utf-8 -*-
from project import db
from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship
import datetime

class Strippi(db.Model):

	__tablename__ = "strippi"

	id = db.Column(db.Integer, primary_key=True)
	sarjakuva_id = db.Column(db.Integer, ForeignKey('sarjakuva.id'), nullable=True)
	url = db.Column(db.UnicodeText)
	filename = db.Column(db.UnicodeText)
	date_created = db.Column(db.DateTime, default=datetime.datetime.now)
	#joukkue_id = db.Column(db.Integer, ForeignKey('joukkue.id'), nullable=True)
	

	


	def __init__(self, sarjakuva_id, url, filename  ):
		self.sarjakuva_id = sarjakuva_id
		self.url = url
		self.filename = filename

	def __repr__(self):	
		return self.toJson()

	def toJson(self):
		ret = {c.name: getattr(self, c.name) for c in self.__table__.columns}
		ret["date_created"] = str(self.date_created)
		#ret["last_parse"] = str(self.last_parse)
		return ret
