# -*- coding: utf-8 -*-
from project import db
from bs4 import BeautifulSoup
import datetime, urllib, os, requests, hashlib
from project.luokat.Sarjis import Sarjis

class Toonhole(Sarjis):

	def __init__(self, sarjakuva, urli=None ):
		Sarjis.__init__(self, sarjakuva, urli)
	
	def Kuva(self):
		src = None
		kuvan_nimi = None

		div = self.soup.find(id="comic")
		img = div.find("img")
		src = img["src"]
		kuva = img["src"].split("/")
		kuvan_nimi = kuva[len(kuva)-1] # haetaan nimi
		#print kuvan_nimi, src
		return dict(nimi=kuvan_nimi, src=src)

		
		

	def Next(self):
		#print "in next"
		links = self.soup.find_all("a")
		for link in links:

			rel = link.get("rel")
			#print rel, link["href"]
			if rel is not None and "next" in rel:
				#print link["href"]
				return link["href"]
		
		
		return None

