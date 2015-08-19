# -*- coding: utf-8 -*-
from project import db, app
from bs4 import BeautifulSoup
from project.models import Sarjakuva as SK, Strippi
import datetime, urllib, os, requests, hashlib
from project.luokat import *
import sys


def run():
	sarjakuvat = db.session.query(SK).order_by(SK.id).all()

	for i in sarjakuvat:
		print i.nimi
		now = datetime.datetime.now()
		if i.last_parse is None or i.last_parse+datetime.timedelta(hours=i.interval) < now:
			try:
				Looper(i)
			except Exception, e:
				print i.nimi, e
				#raise e
			
		print "----\n"
	#print "End"
	return "JOU"


def Looper(comic):
	#print "\n"+comic.nimi
	#return None
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
		olio = Gunshow(comic)
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
		olio = JohnnyWander(comic)
	elif comic.parseri == 23:
		olio = Floabc(comic)
	elif comic.parseri == 24:
		olio = Cheerup(comic)
	elif comic.parseri == 25:
		olio = LoveMeNice(comic)
	elif comic.parseri == 26:
		olio = HamletsDanish(comic)
	elif comic.parseri == 27 and not "short" in sys.argv:
		olio = AvasDemon(comic)
	elif comic.parseri == 28:
		olio = Machismo(comic)
	elif comic.parseri == 29:
		olio = Interrobang(comic)
	elif comic.parseri == 30:
		olio = Unsounded(comic)
	elif comic.parseri == 31:
		olio = Catsu(comic)
	elif comic.parseri == 32:
		olio = PerryBible(comic)
	elif comic.parseri == 33:
		olio = Dilbert(comic)
	elif comic.parseri == 34:
		olio = PepperCarrot(comic)
	elif comic.parseri == 35:
		olio = Rational(comic)
	elif comic.parseri == 36:
		olio = LoadingArtist(comic)
	elif comic.parseri == 37:
		olio = SMBC(comic)
	elif comic.parseri == 38:
		olio = ItsTheTie(comic)
	elif comic.parseri == 39:
		olio = AwkwardZombie(comic)
	elif comic.parseri == 40:
		olio = PowerNap(comic)
	elif comic.parseri == 41:
		olio = ExtraLife(comic)
	elif comic.parseri == 42:
		olio = PlayerVSPlayer(comic)
	elif comic.parseri == 43:
		olio = Abominable(comic)
	elif comic.parseri == 44:
		olio = Existential(comic)
	elif comic.parseri == 45:
		olio = JuniorLeague8(comic)
	elif comic.parseri == 46:
		olio = UserFriendly(comic)
	elif comic.parseri == 47:
		olio = DeathBulge(comic)
	elif comic.parseri == 48:
		olio = PoorlyDrawn(comic)
	elif comic.parseri == 49:
		olio = Ma3(comic)
	elif comic.parseri == 50:
		olio = Blastwave(comic)
	elif comic.parseri == 51:
		olio = StandStill(comic)
	elif comic.parseri == 52:
		olio = DarkLegacy(comic)
	elif comic.parseri == 53:
		olio = CompletelyNormalPeople(comic)


	

	else:
		olio = Sarjis(comic)
	#try:
	loop = comic.last_url
	count = 0
	while loop is not None:
		loop = olio.Loop(comic, loop)
		count += 1
		if "short" in sys.argv and count > 2:
			return True

		if count > 2000: 
		# ladataan korkeintaan 200 strippiä per sarjis per ajo
		# estää bugi ikiloopit
			return True
	#except Exception, e:
		#raise e

	return True

