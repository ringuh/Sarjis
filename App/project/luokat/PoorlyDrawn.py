# -*- coding: utf-8 -*-
from project import db
from bs4 import BeautifulSoup
import datetime, urllib, os, requests, hashlib
from project.luokat.Sarjis import Sarjis

class PoorlyDrawn(Sarjis):

	def __init__(self, sarjakuva, urli=None ):
		Sarjis.__init__(self, sarjakuva, urli)
	
	def Kuva(self):

		kuvan_nimi = None
		src = None
		div = self.soup.find("div", { "class":"comic"})
		div = div.find("div", { "class":"post"})
		
		img = div.find("img")
		
		kuva = img["src"].split("/")
		kuvan_nimi = kuva[len(kuva)-1]+".jpg" # haetaan nimi
		src = img["src"]
		
		
		return dict(nimi=kuvan_nimi, src=src)

		
		

	def Next(self):
		ul = self.soup.find("ul", { "class":"post-nav"})
		li = ul.find("li", { "class":"next"})
		link = li.find("a")
		
		if link is not None:
			return link["href"]		

		
		return None

