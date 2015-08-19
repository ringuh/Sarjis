# -*- coding: utf-8 -*-
from project import db, app
from bs4 import BeautifulSoup
import datetime, urllib, os, requests, hashlib, urllib2
from project.luokat.Sarjis import Sarjis
from project.models import Strippi

class CompletelyNormalPeople(Sarjis):
	# SARJIS.info parseri, koska ctrlaltdel jotenkin suojattu?

	def __init__(self, sarjakuva, urli=None ):
		Sarjis.__init__(self, sarjakuva, urli)
	
	def Kuva(self):
		src = None
		kuvan_nimi = None

		return dict(nimi=kuvan_nimi, src=src)
		

	def Next(self):		
		return None


	def Loop(self, sarjakuva=None, url=None): # ylikirjoitetaan looppi
		if sarjakuva is not None: # initoidaan uudella urlilla
			self.Init(sarjakuva, url)

		kuvat = [".jpg", ".jpeg", ".gif", ".png", ".svg"]

		links = self.soup.find_all("a")
		
		arr = []
		for link in links:
			if ".png" in link["href"]:
				arr.append(link["href"])
		arr.sort()
		
		for n in arr:
			url = u"{}images/toons/{}".format(self.sarjakuva.url, n)
			nimi = n
			#print url, nimi
			polku = os.path.join(app.config["SARJAKUVA_FOLDER"], self.sarjakuva.lyhenne)
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
				Strippi.rname == nimi).first()

			if found is None: # kuvaa ei löytynyt, tallennetaan
				print "Tallennetaan", nimi
	
				headers = { 'User-Agent' : 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/43.0.2357.124 Safari/537.36' }
				req = urllib2.Request(url, None, headers)
				try:
					f = open(polku,'wb')
					f.write(urllib2.urlopen(req).read())
					f.close()
				except Exception, e:
					try:
						f.close()
						f = open(polku,'wb')
						f.write(urllib2.urlopen(url).read())
						f.close()
					except Exception, e:
						print "tallennus epäonnistui"
						#return self.Next()

				# lisätään kantaan tieto, että kuva on haettu
				order = db.session.query(Strippi).filter(
						Strippi.sarjakuva_id == self.sarjakuva.id).count()+1
				tmp = Strippi(self.sarjakuva.id, self.urli, nimi, order, nimi)
				db.session.add(tmp)
				self.sarjakuva.last_url = self.urli

				db.session.commit()

		return None

	