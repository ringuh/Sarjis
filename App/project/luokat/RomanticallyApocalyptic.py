# -*- coding: utf-8 -*-
from project import db
from bs4 import BeautifulSoup
import datetime, urllib, os, requests, hashlib
from project.luokat.Sarjis import Sarjis

class RomanticallyApocalyptic(Sarjis):

	def __init__(self, sarjakuva, urli=None ):
		Sarjis.__init__(self, sarjakuva, urli)
	
	def Kuva(self):
		kuvan_nimi = None
		src = None
		div = self.soup.find("div", { "class": "comicpanel"})
		div = div.find("center")
		img = div.find("img")
		kuva = img["src"].split("/")
		kuvan_nimi = kuva[len(kuva)-1] # haetaan nimi
		src = img["src"]
		
		return dict(nimi=kuvan_nimi, src=src)

	def Next(self):
		div = self.soup.find("div", { "class": "comicpanel"})
		links = div.find_all("a")
		
		for link in links:
			access = link.get("accesskey")
			if access is not None and "n" in access:
				return link["href"]
		
		return None

