# -*- coding: utf-8 -*-
from project import db
from bs4 import BeautifulSoup
import datetime, urllib, os, requests, hashlib
from project.luokat.Sarjis import Sarjis

class Blastwave(Sarjis):

	def __init__(self, sarjakuva, urli=None ):
		Sarjis.__init__(self, sarjakuva, urli)
	
	def Kuva(self):
		src = None
		kuvan_nimi = None
		
		div = self.soup.find(id="comic_ruutu")
		img = div.find("img")
		src = img["src"]
		kuva = img["src"].split("/")
		kuvan_nimi = kuva[len(kuva)-1] # haetaan nimi
		
		if src.index("./") == 0:
		 	src = u"{}{}".format(self.sarjakuva.url, src[2:])

		
		return dict(nimi=kuvan_nimi, src=src)

		
		

	def Next(self):
		#print "in next"
		links = self.soup.find_all("a")
		for link in links:
			img = link.find("img")
			if img is not None and "next.jpg" in img["src"]:
				return u"{}{}".format(self.sarjakuva.url, link["href"])
		
		
		return None

