# -*- coding: utf-8 -*-
from project import db
import datetime


class Brute_force(db.Model):

	__tablename__ = "brute_force"

	id = db.Column(db.Integer, primary_key=True)
	ip = db.Column(db.UnicodeText, nullable=False)
	date_created = db.Column(db.DateTime, default=datetime.datetime.now)

	def __init__(self, ip ):
		self.ip = ip 
		

	def __repr__(self):	
		return '{}:bruteforce'.format(self.id)	

	def count(self):
		vrt = datetime.datetime.now() - datetime.timedelta(hours=2)
		n = db.session.query(Brute_force).filter(
			Brute_force.ip == self.ip, Brute_force.date_created > vrt ).count()
		return n