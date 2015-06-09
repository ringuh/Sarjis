# -*- coding: utf-8 -*-
from project import db, app
from bs4 import BeautifulSoup
from project.models import Sarjakuva as SK, Strippi
import datetime, urllib, os, requests, hashlib
from project.luokat import *
import sys


def run():
	sarjakuvat = db.session.query(SK).all()

	for i in sarjakuvat:
		print i.nimi
		now = datetime.datetime.now()
		if i.last_parse is None or i.last_parse+datetime.timedelta(hours=i.interval) < now:
			try:
				Looper(i)
			except Exception, e:
				print i.nimi, e
				raise e
			
		print "----\n"
	print "End"
	return "JOU"


def Looper(comic):

	if "nr" in sys.argv:
		if comic.parseri != int(sys.argv[3]):
			return
	olio = None
	if comic.parseri == 1:
		olio = Oglaf(comic)
	elif comic.parseri == 2:
		olio = Fingerpori(comic)
	elif comic.parseri == 3:
		olio = OOTS(comic)
	elif comic.parseri == 4:
		olio = Toonhole(comic)
	elif comic.parseri == 5:
		olio = Satw(comic)
	elif comic.parseri == 6:
		olio = CtrlAltDel(comic)
	elif comic.parseri == 7:
		olio = Explosm(comic)
	elif comic.parseri == 8:
		olio = Dragonarte(comic)
	elif comic.parseri == 9:
		olio = PainTrain(comic)
	elif comic.parseri == 10:
		olio = HappleTea(comic)


	else:
		olio = Sarjis(comic)
	#try:
	loop = comic.last_url
	 
	while loop is not None:
		loop = olio.Loop(comic, loop)
		if "short" in sys.argv:
			return True
	#except Exception, e:
		#raise e

	return True

