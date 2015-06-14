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
	elif comic.parseri == 8 and not "short" in sys.argv:
		olio = Dragonarte(comic)
	elif comic.parseri == 9:
		olio = PainTrain(comic)
	elif comic.parseri == 10:
		olio = HappleTea(comic)
	elif comic.parseri == 11:
		olio = HappleTea(comic)
	elif comic.parseri == 12:
		olio = VGCats(comic)
	elif comic.parseri == 13:
		olio = NerfNow(comic)
	elif comic.parseri == 14:
		olio = Sinfest(comic)
	elif comic.parseri == 15:
		olio = Camp(comic)
	elif comic.parseri == 16:
		olio = Pidjin(comic)
	elif comic.parseri == 17:
		olio = Garfield(comic)
	elif comic.parseri == 18:
		olio = LeastICouldDo(comic)
	elif comic.parseri == 19:
		olio = GC(comic)
	elif comic.parseri == 20:
		olio = LassiLeevi(comic)
	elif comic.parseri == 21:
		olio = PennyArcade(comic)
	elif comic.parseri == 22:
		olio = Gunshow(comic)
	#elif comic.parseri == 20:
	#	olio = Wulfmorgenthaler(comic)


	else:
		olio = Sarjis(comic)
	#try:
	loop = comic.last_url
	count = 0
	while loop is not None:
		loop = olio.Loop(comic, loop)
		count += 1
		if "short" in sys.argv and count > 5:
			return True

		if count > 2000: 
		# ladataan korkeintaan 2000 strippiä per sarjis per ajo
		# estää bugi ikiloopit
			return True
	#except Exception, e:
		#raise e

	return True

