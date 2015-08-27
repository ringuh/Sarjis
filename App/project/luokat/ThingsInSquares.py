# -*- coding: utf-8 -*-
from project import db
from bs4 import BeautifulSoup
import datetime, urllib, os, requests, hashlib
from project.luokat.Sarjis import Sarjis

class ThingsInSquares(Sarjis):

	def __init__(self, sarjakuva, urli=None ):
		Sarjis.__init__(self, sarjakuva, urli)
	
	def Kuva(self):
		kuvan_nimi = None
		src = None
		
		div = self.soup.find(id="content")
		article = div.find("article")
		div = article.find("div", {"class": "entry-content"})
		img = div.find("img")
		kuva = img["src"].split("/")
		kuvan_nimi = kuva[len(kuva)-1] # haetaan nimi
		src = img["src"]
		
		
		return dict(nimi=kuvan_nimi, src=src)

		
		

	def Next(self):
		div = self.soup.find("div", {"class": "nav-links"})
		links = div.find_all("a")
		for link in links:
			rel = link.get("rel")
			if rel is not None and "next" in rel:
				if link["href"] is not None:
					return link["href"]
		
		return None
