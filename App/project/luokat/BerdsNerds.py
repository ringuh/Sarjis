# -*- coding: utf-8 -*-
from project import db
from bs4 import BeautifulSoup
import datetime, urllib, os, requests, hashlib
from project.luokat.Sarjis import Sarjis

class BerdsNerds(Sarjis):

	def __init__(self, sarjakuva, urli=None ):
		Sarjis.__init__(self, sarjakuva, urli)
	
	def Kuva(self):
		src = None
		kuvan_nimi = None
		
		div = self.soup.find("noscript")
		#div = self.soup.find(id="comic")
		img = div.find("img")
		src = img["src"]
		kuva = img["src"].split("/")
		kuvan_nimi = kuva[len(kuva)-1] # haetaan nimi
		#print src
		if src.index("//") == 0:
			src = u"http:{}".format(src)

		return dict(nimi=kuvan_nimi, src=src)

		
		

	def Next(self):
		#print "in next"
		div = self.soup.find("div", { "class": "intrinsic" })
		link = div.find("a")
		
		if link is not None and "berdsandnerds.com/comic/" in link["href"]:
			return link["href"]
			
		
		
		return None

