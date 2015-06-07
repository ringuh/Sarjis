# -*- coding: utf-8 -*-
from project import db, app
from bs4 import BeautifulSoup
import datetime, urllib, os, requests, hashlib
from project.luokat.Sarjis import Sarjis
from project.models import Strippi

class Dragonarte(Sarjis):
	# erilainen parseri. parseaa tiedostolistausta

	def __init__(self, sarjakuva, urli=None ):
		Sarjis.__init__(self, sarjakuva, urli)
	
	def Kuva(self):
		src = None
		kuvan_nimi = None

		img = self.soup.find(id="main-comic")
		#src = u"http:{}".format(img["src"])
		#kuva = img["src"].split("/")
		#kuvan_nimi = kuva[len(kuva)-1] # haetaan nimi
			
		#print kuvan_nimi, src
		return dict(nimi=kuvan_nimi, src=src)
		

	def Next(self):
		#div = self.soup.find("a", { "class": "next-comic" })
		
		#if div is not None and len(div["href"]) > 1:
		#	return u"{}{}".format(self.sarjakuva.url, div["href"])
		
		return None


	def Loop(self, sarjakuva=None, url=None): # ylikirjoitetaan looppi
		if sarjakuva is not None: # initoidaan uudella urlilla
			self.Init(sarjakuva, url)

		kuvat = [".jpg", ".jpeg", ".gif", ".png", ".svg"]
		links = self.soup.find_all("a")
		for link in links:
			nimi = link["href"]
			#print nimi
			arr = nimi.split(".")
			if not "."+arr[len(arr)-1] in kuvat: # ei oikeanlainen kuva
				continue
			url = u"{}/{}".format(self.urli, nimi)
			polku = os.path.join(app.config["SARJAKUVA_FOLDER"], self.sarjakuva.nimi)
			polku = os.path.join(polku, nimi)

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
				Strippi.filename == nimi).first()

			if found is None: # kuvaa ei löytynyt, tallennetaan
				print "Tallennetaan", nimi
				f = open(polku,'wb')
				f.write(urllib.urlopen(url).read())
				f.close()

				# lisätään kantaan tieto, että kuva on haettu
				order = db.session.query(Strippi).filter(
						Strippi.sarjakuva_id == self.sarjakuva.id).count()+1
				tmp = Strippi(self.sarjakuva.id, self.urli, nimi, order)
				db.session.add(tmp)
				self.sarjakuva.last_url = self.urli

				db.session.commit()

		return None