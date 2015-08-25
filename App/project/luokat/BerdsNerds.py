# -*- coding: utf-8 -*-
from project import db, app
from bs4 import BeautifulSoup
import datetime, urllib, os, requests, hashlib, urllib2
from project.luokat.Sarjis import Sarjis, Strippi

class BerdsNerds(Sarjis):

	def __init__(self, sarjakuva, urli=None ):
		Sarjis.__init__(self, sarjakuva, urli)


	def Loop(self, sarjakuva=None, url=None): # ylikirjoitetaan looppi
		if sarjakuva is not None: # initoidaan uudella urlilla
			self.Init(sarjakuva, url)

		
		ol = self.soup.find("ol")
	
		for li in ol:
			link = li.find("a")
			print link["href"]
			
			url_used = db.session.query(Strippi).filter(
					Strippi.sarjakuva_id == self.sarjakuva.id,
					Strippi.url == link["href"],
				).first()

			if url_used is not None:
				continue

			src = None
			kuvan_nimi = None
				
			
			r = requests.get(link["href"], headers=app.config["REQUEST_HEADER"] )
			page = BeautifulSoup(r.text)
			
			div = page.find("noscript")
			img = div.find("img")
			src = img["src"]
			#print src
			kuva = img["src"].split("/")
			
			kuvan_nimi = kuva[len(kuva)-1] # haetaan nimi
			final_nimi = u"{}{}_{}".format(self.sarjakuva.lyhenne, self.sarjakuva.Max()+1, kuvan_nimi)
			#print final_nimi
			#print url, nimi
			polku = os.path.join(app.config["SARJAKUVA_FOLDER"], self.sarjakuva.lyhenne)
			polku = os.path.join(polku, final_nimi)

			# luodaan kansio if needed
			dir = os.path.dirname(polku) 
			try:
				os.stat(dir)
			except:
				os.mkdir(dir)

			# katsotaan oliko kyseisestä sarjasta jo kyseinen kuva
			found = db.session.query(Strippi).filter(
				Strippi.sarjakuva_id == self.sarjakuva.id,
				Strippi.url == link["href"],
				Strippi.rname == kuvan_nimi).first()

			if found is None: # kuvaa ei löytynyt, tallennetaan
				print "Tallennetaan", kuvan_nimi
	
				req = urllib2.Request(src, None, app.config["REQUEST_HEADER"])
				try:
					f = open(polku,'wb')
					f.write(urllib2.urlopen(req).read())
					f.close()
				except Exception, e:
					try:
						f.close()
						f = open(polku,'wb')
						f.write(urllib2.urlopen(src).read())
						f.close()
					except Exception, e:
						print "tallennus epäonnistui"
						#return self.Next()

				# lisätään kantaan tieto, että kuva on haettu
				order = db.session.query(Strippi).filter(
						Strippi.sarjakuva_id == self.sarjakuva.id).count()+1
				tmp = Strippi(self.sarjakuva.id, link["href"], final_nimi, order, kuvan_nimi)
				db.session.add(tmp)
				#self.sarjakuva.last_url = self.urli

				db.session.commit()

		return None
	
	# def Kuva(self):
	# 	src = None
	# 	kuvan_nimi = None
		
	# 	div = self.soup.find("noscript")
	# 	#div = self.soup.find(id="comic")
	# 	img = div.find("img")
	# 	src = img["src"]
	# 	kuva = img["src"].split("/")
	# 	kuvan_nimi = kuva[len(kuva)-1] # haetaan nimi
	# 	#print src
	# 	if src.index("//") == 0:
	# 		src = u"http:{}".format(src)

	# 	return dict(nimi=kuvan_nimi, src=src)

		
		

	# def Next(self):
	# 	#print "in next"
	# 	div = self.soup.find("div", { "class": "intrinsic" })
	# 	link = div.find("a")
		
	# 	if link is not None and "berdsandnerds.com/comic/" in link["href"]:
	# 		return link["href"]
			
		
		
	# 	return None

