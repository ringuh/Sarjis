# -*- coding: utf-8 -*-
from project import db
from bs4 import BeautifulSoup
import datetime, urllib, os, requests, hashlib
from project.luokat.Sarjis import Sarjis

class OOTS(Sarjis):

	def __init__(self, sarjakuva, urli=None ):
		Sarjis.__init__(self, sarjakuva, urli)
	
	def Kuva(self):
		imgs = self.soup.find_all("img")
		kuvan_nimi = None
		src = None
		for img in imgs:
			#print img["src"]
			if "/comics/images/" in img["src"]:
				kuva = img["src"].split("/")
				kuvan_nimi = kuva[len(kuva)-1] # haetaan nimi
				src = img["src"]
				if not "http:" in src:
					src = u"{}{}".format(self.sarjakuva.url, img["src"])
				#print kuvan_nimi, src
				break
		
		
		return dict(nimi=kuvan_nimi, src=src)

		
		

	def Next(self):
		links = self.soup.find_all("a")

		for link in links:
			img = link.find("img")

			if img is not None and img.get("title") is not None and img.get("title").lower() == "next comic":
				if link["href"] != "#":
					return u"{}{}".format(self.sarjakuva.url, link["href"])
		
		return None

