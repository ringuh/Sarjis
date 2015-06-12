# -*- coding: utf-8 -*-
from project import db
from bs4 import BeautifulSoup
import datetime, urllib, os, requests, hashlib
from project.luokat.Sarjis import Sarjis

class Garfield(Sarjis):

	def __init__(self, sarjakuva, urli=None ):
		Sarjis.__init__(self, sarjakuva, urli)
	
	def Kuva(self):
		kuvan_nimi = None
		src = None

		div = self.soup.find(id="comic_wrap")
		img = div.find("img", {"class": "center-block"})
		kuva = img["src"].split("/")
		kuvan_nimi = kuva[len(kuva)-1] # haetaan nimi
		src = img["src"]
		
		
		return dict(nimi=kuvan_nimi, src=src)

		
		

	def Next(self):
		link = self.soup.find("a", {"class": "comic-arrow-right"})
		if link is not None and link["href"] != "#":
			return link["href"]
		
		return None

