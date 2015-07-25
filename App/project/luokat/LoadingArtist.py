# -*- coding: utf-8 -*-
from project import db
from bs4 import BeautifulSoup
import datetime, urllib, os, requests, hashlib
from project.luokat.Sarjis import Sarjis

class LoadingArtist(Sarjis):

	def __init__(self, sarjakuva, urli=None ):
		Sarjis.__init__(self, sarjakuva, urli)
	
	def Kuva(self):
		kuvan_nimi = None
		src = None
		
		div = self.soup.find("div", { "class": "comic"})
		div = div.find("div", { "class": "comic"})
		img = div.find("img")
		kuva = img["src"].split("/")
		kuvan_nimi = kuva[len(kuva)-1] # haetaan nimi
		img["src"] = img["src"].replace("./", "")
		src = u"{}".format(img["src"])
		
		
		return dict(nimi=kuvan_nimi, src=src)

		
		

	def Next(self):
		div = self.soup.find("div", { "class": "comic"})
		div = div.find("div", { "class": "comic"})
		
		link = div.find("a")
		
		if link is not None:
			return u"{}".format(link["href"])
		
		
		return None

