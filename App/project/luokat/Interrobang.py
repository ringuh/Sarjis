# -*- coding: utf-8 -*-
from project import db
from bs4 import BeautifulSoup
import datetime, urllib, os, requests, hashlib
from project.luokat.Sarjis import Sarjis

class Interrobang(Sarjis):
	# SARJIS.info parseri, koska ctrlaltdel jotenkin suojattu?

	def __init__(self, sarjakuva, urli=None ):
		Sarjis.__init__(self, sarjakuva, urli)
	
	def Kuva(self):
		kuvan_nimi = None
		src = None
		
		div = self.soup.find(id="comic01")
		img = div.find("img")
		kuva = img["src"].split("/")
		kuvan_nimi = kuva[len(kuva)-1] # haetaan nimi
		src = img["src"]
		
		
		return dict(nimi=kuvan_nimi, src=src)

		
		

	def Next(self):
		div = self.soup.find(id="comic-nav01")
		links = div.find_all("a")
		for link in links:
			img = link.find("img")
			if img is not None and "nav_next.png" in img["src"]:
				if link["href"] != "#":
					if "http:" in link["href"]:
						return link["href"]
					else:
						return u"{}{}".format(self.sarjakuva.url, link["href"])

		
		return None


	