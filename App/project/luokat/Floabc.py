# -*- coding: utf-8 -*-
from project import db
from bs4 import BeautifulSoup
import datetime, urllib, os, requests, hashlib
from project.luokat.Sarjis import Sarjis

class Floabc(Sarjis):

	def __init__(self, sarjakuva, urli=None ):
		Sarjis.__init__(self, sarjakuva, urli)
	
	def Kuva(self):
		kuvan_nimi = None
		src = None
		
		img = self.soup.find(id="comicimg")
		kuva = img["src"].split("/")
		kuvan_nimi = kuva[len(kuva)-1] # haetaan nimi
		img["src"] = img["src"].replace("./", "")
		src = u"{}".format(img["src"])
		
		
		return dict(nimi=kuvan_nimi, src=src)

		
		

	def Next(self):
		div = self.soup.find("div", { "class": "navbar" })
		links = div.find_all("a")
		for link in links:
			if link.text.strip() == "Next" and link["href"] != "#":
				return u"{}".format(link["href"])
		
		
		return None

