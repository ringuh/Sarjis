# -*- coding: utf-8 -*-
from project import db
from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship
import datetime

class Sarjakuva_user(db.Model):

	__tablename__ = "sarjakuva_user"

	id = db.Column(db.Integer, primary_key=True)
	sarjakuva_id = db.Column(db.Integer, ForeignKey('sarjakuva.id'), nullable=True)
	user_id = db.Column(db.Integer, ForeignKey('user.id'), nullable=True)
	visibility = db.Column(db.Boolean, default=True)
	date_created = db.Column(db.DateTime, default=datetime.datetime.now)
	


	def __init__(self, sarjakuva_id, user_id, visibility ):
		self.sarjakuva_id = sarjakuva_id
		self.user_id = user_id
		self.visibility = visibility
		

	def __repr__(self):	
		return self.toJson()

	def toJson(self):
		ret = {c.name: getattr(self, c.name) for c in self.__table__.columns}
		ret["date_created"] = str(self.date_created)
		return ret





