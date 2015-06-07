# -*- coding: utf-8 -*-
from project import db
from bs4 import BeautifulSoup
import datetime, urllib, os, requests, hashlib
from project.luokat.Sarjis import Sarjis

class CtrlAltDel(Sarjis):

	def __init__(self, sarjakuva, urli=None ):
		Sarjis.__init__(self, sarjakuva, urli)
	
	def Kuva(self):
		src = None
		kuvan_nimi = None

		div = self.soup.find(id="content")
		img = div.find("img")
		src = img["src"]
		kuva = img["src"].split("/")
		kuvan_nimi = kuva[len(kuva)-1] # haetaan nimi
			
		#print kuvan_nimi, src
		return dict(nimi=kuvan_nimi, src=src)

		
		

	def Next(self):
		div = self.soup.find(id="content")
		nav = div.find("div", { "class": "navigation" })
		link = nav.find("a", {"class":"nav-next"})
			
		
		if link is not None and len(link["href"]) > 5:
			return u"{}{}".format(self.sarjakuva.url, link["href"])
		
		
		return None

