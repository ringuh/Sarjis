# -*- coding: utf-8 -*-
from project import db
from bs4 import BeautifulSoup
import datetime, urllib, os, requests, hashlib
from project.luokat.Sarjis import Sarjis, Strippi

class Tubey(Sarjis):

	def __init__(self, sarjakuva, urli=None ):
		Sarjis.__init__(self, sarjakuva, urli)
	
	def Kuva(self):
		ret = []
		divs = self.soup.find_all("div", { "class": "comic-image"})
		for div in divs:
			images = self.soup.find_all("img")
			for img in images:
				try:
					if not "/comics/" in img["src"]:
						continue
				except Exception, e:
					continue

				kuvan_nimi = None
				src = None
		
				kuva = img["src"].split("/")
				kuvan_nimi = kuva[len(kuva)-1] # haetaan nimi
				src = img["src"]
				ret.append(dict(nimi=kuvan_nimi, src=src))
		
		return ret

		
		

	def Next(self):
		try:
			span = self.soup.find("span", { "class": "hvr-skew-forward"})
		
			g = span.get("onclick")

			g = g.replace("goCom(", "").replace(")", "")
			id, cmd = g.split(",") 

			url = u"{}{}".format(self.sarjakuva.url, int(id)+1)
		
			return url
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
