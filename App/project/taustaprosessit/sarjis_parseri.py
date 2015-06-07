# -*- coding: utf-8 -*-
from project import db, app
from bs4 import BeautifulSoup
from project.models import Sarjakuva as SK, Strippi
import datetime, urllib, os, requests, hashlib
from project.luokat import *



def run():
	sarjakuvat = db.session.query(SK).all()

	for i in sarjakuvat:
		print i.nimi
		now = datetime.datetime.now()
		if i.last_parse is None or i.last_parse+datetime.timedelta(hours=i.interval) < now:
			Looper(i)
			#elif i.parseri == 2:
			#	Fingerpori(i)
			#elif i.parseri == 3:
			#	Giantitp(i)
			
		print "----\n"
	print "End"
	return "JOU"


def Looper(comic):
	olio = Sarjis(comic)
	if comic.parseri == -1:
		olio = Oglaf(comic)
	elif comic.parseri == -2:
		olio = Fingerpori(comic)
	elif comic.parseri == -3:
		olio = OOTS(comic)
	elif comic.parseri == 4:
		olio = Toonhole(comic)

	#try:
	loop = comic.last_url
	while loop is not None:
		loop = olio.Loop(comic, loop)
	#except Exception, e:
		#raise e

	return True

