# -*- coding: utf-8 -*-
from project import db
from bs4 import BeautifulSoup
import datetime, urllib, os, requests, hashlib
from project.luokat.Sarjis import Sarjis

class Sinfest(Sarjis):

	def __init__(self, sarjakuva, urli=None ):
		Sarjis.__init__(self, sarjakuva, urli)
	
	def Kuva(self):
		kuvan_nimi = None
		src = None
		print "kuva"
		images = self.soup.find_all("img")
		for i in images:
			if "btphp/comics/" in i["src"]:
				kuva = i["src"].split("/")
				kuvan_nimi = kuva[len(kuva)-1] # haetaan nimi
				src = u"{}{}".format(self.sarjakuva.url, i["src"])
				break
		
		return dict(nimi=kuvan_nimi, src=src)

	def Next(self):
		link = self.soup.find_all("a")
		for l in link:
			tmp = l.find("img")
			if tmp is not None and l["href"] != "view.php?date=" and tmp["src"] == "../images/next.gif":
				return u"{}{}".format(self.sarjakuva.url, l["href"])
		
		return None

