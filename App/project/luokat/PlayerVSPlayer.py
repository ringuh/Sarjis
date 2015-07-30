# -*- coding: utf-8 -*-
from project import db
from bs4 import BeautifulSoup
import datetime, urllib, os, requests, hashlib
from project.luokat.Sarjis import Sarjis

class PlayerVSPlayer(Sarjis):

	def __init__(self, sarjakuva, urli=None ):
		Sarjis.__init__(self, sarjakuva, urli)
	
	def Kuva(self):
		kuvan_nimi = None
		src = None

		div = self.soup.find("section", { "class": "comic-art"})
		img = div.find("img")
		kuva = img["src"].split("/")
		kuvan_nimi = kuva[len(kuva)-1] # haetaan nimi
		src = img["src"]
		
		return dict(nimi=kuvan_nimi, src=src)

	def Next(self):
		nav = self.soup.find("div", {"class":"comic-nav"})
	
		links = nav.find_all("a")
		for link in links:
			if link is not None and "next" in link.text.lower():
				return u"{}{}".format(self.sarjakuva.url[:-1], link["href"])
		
		return None

