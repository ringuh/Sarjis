# -*- coding: utf-8 -*-
from project import db, app
from bs4 import BeautifulSoup
from project.models import Sarjakuva as SK, Strippi
import datetime, urllib, os, requests, hashlib



def run():
	sarjakuvat = db.session.query(SK).all()

	for i in sarjakuvat:
		print i.nimi
		now = datetime.datetime.now()
		if i.last_parse is None or i.last_parse+datetime.timedelta(hours=i.interval) < now:
			if i.parseri == 1:
				Oglaf(i)
			else:
				print u"Parseri puuttuu"
		print "----\n"
	print "End"
	return "JOU"



def Oglaf(sarjis):
	print "Haetaan oglaf"

	
	def Loop(urli):
		print u"\nfinding url", urli
		r  = requests.get(urli)
		soup = BeautifulSoup(r.text)
		#print soup
		img = soup.find(id="strip") # haetaan elementti, jossa kuva
		#print img["src"]
		kuva = img["src"].split("/")
		kuva = kuva[len(kuva)-1] # haetaan nimi
		
		polku = os.path.join(app.config["SARJAKUVA_FOLDER"], sarjis.nimi)
		polku = os.path.join(polku, kuva)

		# luodaan kansio if needed
		dir = os.path.dirname(polku) 
		try:
			os.stat(dir)
		except:
			os.mkdir(dir)

		found = db.session.query(Strippi).filter(
				Strippi.sarjakuva_id == sarjis.id,
				Strippi.url == urli,
				Strippi.filename == kuva).first()
		if found is None:
			print "Tallennetaan", kuva
			f = open(polku,'wb')
			f.write(urllib.urlopen(img["src"]).read())
			f.close()
			
			# lisätään kantaan tieto, että kuva on haettu
			tmp = Strippi(sarjis.id, urli, kuva)
			db.session.add(tmp)
			sarjis.last_url = urli

			db.session.commit()

		# tarkistetaan löytyykö "seuraavaa sivua"


		nav = soup.find(id="nav")
		nav_links = nav.find_all('a')
		for nn in nav_links:
			next = nn.find(id="nx")
			if next is not None and nn["href"] is not None:
				Loop(u"{}{}".format(sarjis.url, nn["href"]))
				break


		
	#try:
	Loop(sarjis.last_url)
	#except Exception, e:
		#raise e

	return True