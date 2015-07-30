# -*- coding: utf-8 -*-
from project import db
from bs4 import BeautifulSoup
import datetime, urllib, os, requests, hashlib
from project.luokat.Sarjis import Sarjis

class AwkwardZombie(Sarjis):

	def __init__(self, sarjakuva, urli=None ):
		Sarjis.__init__(self, sarjakuva, urli)
	
	def Kuva(self):
		kuvan_nimi = None
		src = None

		div = self.soup.find(id="comic")
		img = div.find("img")
		kuva = img["src"].split("/")
		kuvan_nimi = kuva[len(kuva)-1] # haetaan nimi
		src = img["src"]
		
		return dict(nimi=kuvan_nimi, src=src)

		
		

	def Next(self):
		links = self.soup.find_all("a")

		for link in links:
			img = link.find("img")

			if img is not None and img.get("alt") is not None and img.get("alt").lower() == "next comic":
				if link["href"] != "#":
					return u"{}{}".format(self.sarjakuva.url, link["href"])
		
		return None

