# -*- coding: utf-8 -*-
from project import db
from bs4 import BeautifulSoup
import datetime, urllib, os, requests, hashlib
from project.luokat.Sarjis import Sarjis

class Grog(Sarjis):

	def __init__(self, sarjakuva, urli=None ):
		Sarjis.__init__(self, sarjakuva, urli)
	
	def Kuva(self):
		kuvan_nimi = None
		src = None
		
		#print self.soup
		div = self.soup.find("div", {"class": "photo-panel"})

		img = div.find("img")
		kuva = img["src"].split("/")
		kuvan_nimi = kuva[len(kuva)-1] # haetaan nimi
		src = img["src"]
		
		
		return dict(nimi=kuvan_nimi, src=src)

		
		

	def Next(self):
		link = self.soup.find("a", {"class": "prev"})
	
		
		if link is not None:
			return link["href"]
		
		return None

