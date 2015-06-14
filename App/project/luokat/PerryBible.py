# -*- coding: utf-8 -*-
from project import db
from bs4 import BeautifulSoup
import datetime, urllib, os, requests, hashlib
from project.luokat.Sarjis import Sarjis

class PerryBible(Sarjis):

	def __init__(self, sarjakuva, urli=None ):
		Sarjis.__init__(self, sarjakuva, urli)
	
	def Kuva(self):
		kuvan_nimi = None
		src = None
		
		img = self.soup.find(id="topimg")
		kuva = img["src"].split("/")
		kuvan_nimi = kuva[len(kuva)-1] # haetaan nimi
		img["src"] = img["src"].replace("./", "")
		src = u"{}{}".format(self.sarjakuva.url, img["src"])
		
		
		return dict(nimi=kuvan_nimi, src=src)

		
		

	def Next(self):
		
		link = self.soup.find_all("a")
		for i in link:
			img = i.find("img")
			
			if img is not None and "newer" in img["src"].lower():
				if i["href"] != "#":
					return u"{}{}".format(self.sarjakuva.url, i["href"])
		
		return None

