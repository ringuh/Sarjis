# -*- coding: utf-8 -*-
from project import db
from bs4 import BeautifulSoup
import datetime, urllib, os, requests, hashlib
from project.luokat.Sarjis import Sarjis, Strippi

class NerdRage(Sarjis):

	def __init__(self, sarjakuva, urli=None ):
		Sarjis.__init__(self, sarjakuva, urli)
	
	def Kuva(self):
		ret = []

		table = self.soup.find("table", { "class": "shadow"} )

		images = table.find_all("img")
		for img in images:
			kuvan_nimi = None
			src = None
	
			kuva = img["src"].split("/")
			kuvan_nimi = kuva[len(kuva)-1] # haetaan nimi
			src = u"{}{}".format(self.sarjakuva.url, img["src"])
			ret.append(dict(nimi=kuvan_nimi, src=src))
		
		return ret

		
		

	def Next(self):
		try:
			links = self.soup.find_all("a")
			for link in links:
				img = link.find("img")
				if img is not None:
					alt = img.get("alt")
					if alt is not None and "next comic" in alt.lower():
						return u"{}{}".format(self.sarjakuva.url, link["href"])

		except Exception, e:
			return None
		

		return None


	def Loop(self, sarjakuva=None, url=None): # ylikirjoitetaan looppi
		if sarjakuva is not None: # initoidaan uudella urlilla
			self.Init(sarjakuva, url)
		
		images = self.Kuva()
		for img in images:
			self.Save(img["nimi"], img["src"])
					
		return self.Next()