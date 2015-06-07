# -*- coding: utf-8 -*-
from project import db, app
from bs4 import BeautifulSoup
import datetime, urllib2, os, requests, hashlib
from project.models import Strippi

class Sarjis(object):
	
	def __init__(self, sarjakuva, url=None ):
		self.sarjakuva = sarjakuva
		if url is None:
			url = sarjakuva.last_url
		self.urli = url
		r = requests.get(url)
		self.soup = BeautifulSoup(r.text)
	
	def Init(self, sarjakuva, url=None):
		self.sarjakuva = sarjakuva
		if url is None:
			url = sarjakuva.last_url
		self.urli = url
		r = requests.get(url)
		self.soup = BeautifulSoup(r.text)
		print u"\nFinding url", url 

	def Loop(self, sarjakuva=None, url=None):
		if sarjakuva is not None: # initoidaan uudella urlilla
			self.Init(sarjakuva, url)

		kuva = self.Kuva()
		if kuva["src"] is None:
			return None

		# päätetään minne tallennettaisiin jos tallennetaan
		polku = os.path.join(app.config["SARJAKUVA_FOLDER"], self.sarjakuva.nimi)
		polku = os.path.join(polku, kuva["nimi"])
		
		# luodaan kansio if needed
		dir = os.path.dirname(polku) 
		try:
			os.stat(dir)
		except:
			os.mkdir(dir)

		# katsotaan oliko kyseisestä sarjasta jo kyseinen kuva
		found = db.session.query(Strippi).filter(
				Strippi.sarjakuva_id == self.sarjakuva.id,
				Strippi.url == self.urli,
				Strippi.filename == kuva["nimi"]).first()

		if found is None: # kuvaa ei löytynyt, tallennetaan
			print "Tallennetaan", kuva["nimi"]

			headers = { 'User-Agent' : 'Mozilla/5.0' }
			req = urllib2.Request(kuva["src"], None, headers)
			f = open(polku,'wb')
			f.write(urllib2.urlopen(req).read())
			f.close()

			# lisätään kantaan tieto, että kuva on haettu
			order = db.session.query(Strippi).filter(
					Strippi.sarjakuva_id == self.sarjakuva.id).count()+1
			tmp = Strippi(self.sarjakuva.id, self.urli, kuva["nimi"], order)
			db.session.add(tmp)
			self.sarjakuva.last_url = self.urli

			db.session.commit()

		# tarkistetaan löytyykö seuraavaa sivua
		return self.Next() # jos None looppi loppuu
		

	def Kuva(self):
		print "SARJIS KUVA"
		return dict(nimi=None, src=None)

	def Next(self):
		print "SARJIS NEXT"
		return None