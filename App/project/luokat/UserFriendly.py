# -*- coding: utf-8 -*-
from project import db, app
from bs4 import BeautifulSoup
import datetime, urllib, urllib2, os, requests, hashlib
from project.luokat.Sarjis import Sarjis
from project.models import Strippi

class UserFriendly(Sarjis):

	def __init__(self, sarjakuva, urli=None ):
		Sarjis.__init__(self, sarjakuva, urli)
	
	def Kuva(self):
		kuvan_nimi = None
		src = None
		imgs = self.soup.find_all("img")
		for img in imgs:
			x = img.get("alt")
			if x is None or not "strip" in x.lower():
				continue

			src = img["src"]
			if "?" in src:
				src = src[0:src.index("?")]
			tmp = src.split("/")
			kuvan_nimi = tmp[len(tmp)-1] # muodostetaan nimi

			if not "http:" in src:
				src = "http:"+src
			
			break

		return dict(nimi=kuvan_nimi, src=src)
		

	def Next(self):
		areas = self.soup.find_all("area")
		for area in areas:
			x = area.get("alt")
	
			if x is not None and "next" in x.lower():
				if area["href"][0] == "/":
					area["href"] = area["href"][1:]
				
				return u"{}{}".format(self.sarjakuva.url, area["href"])

		return None



