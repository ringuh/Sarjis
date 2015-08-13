# -*- coding: utf-8 -*-
from project import db
from bs4 import BeautifulSoup
import datetime, urllib, os, requests, hashlib
from project.luokat.Sarjis import Sarjis

class DarkLegacy(Sarjis):

	def __init__(self, sarjakuva, urli=None ):
		Sarjis.__init__(self, sarjakuva, urli)
	
	def Kuva(self):
		kuvan_nimi = None
		src = None
		img = self.soup.find("div", { "class": "comic" })

		img = img.find("img")
		src = img["src"]
		if "?" in src:
			src = src[0:src.index("?")]
		tmp = src.split("/")
		kuvan_nimi = tmp[len(tmp)-1] # muodostetaan nimi

		if not "http:" in src:
			src = u"{}{}".format(self.sarjakuva.url, src.strip())
		#print kuvan_nimi, src
		return dict(nimi=kuvan_nimi, src=src)


	def Next(self):
		next = self.soup.find("a", { "class" : "nextLink" })
	
		if next is not None:
			return u"{}{}".format(self.sarjakuva.url, next["href"])
			

		return None

