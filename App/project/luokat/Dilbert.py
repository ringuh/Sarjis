# -*- coding: utf-8 -*-
from project import db
from bs4 import BeautifulSoup
import datetime, urllib, os, requests, hashlib
from project.luokat.Sarjis import Sarjis

class Dilbert(Sarjis):

	def __init__(self, sarjakuva, urli=None ):
		Sarjis.__init__(self, sarjakuva, urli)
	
	def Kuva(self):
		kuvan_nimi = None
		src = None

		img = self.soup.find("img", { "class": "img-comic"})
		#img = div.find("img", {"class": "center-block"})
		kuva = img["src"].split("/")
		kuvan_nimi = kuva[len(kuva)-1]+".jpg" # haetaan nimi
		src = img["src"]
		
		return dict(nimi=kuvan_nimi, src=src)

		
		

	def Next(self):
		links = self.soup.find_all("a")
		for link in links:
			alt = link.get("alt")
			if alt is not None and alt.lower() == "newer strip":
				return u"{}{}".format(self.sarjakuva.url, link["href"])
		
			
		
		return None

