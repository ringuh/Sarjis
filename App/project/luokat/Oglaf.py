# -*- coding: utf-8 -*-
from project import db
from bs4 import BeautifulSoup
import datetime, urllib, os, requests, hashlib
from project.luokat.Sarjis import Sarjis

class Oglaf(Sarjis):

	def __init__(self, sarjakuva, urli=None ):
		Sarjis.__init__(self, sarjakuva, urli)
	
	def Kuva(self):
		img = self.soup.find(id="strip")
		img_url = img["src"]
		kuva = img["src"].split("/")
		kuva = kuva[len(kuva)-1] # haetaan nimi

		return dict(nimi=kuva, src=img_url)


	def Next(self):
		nav = self.soup.find(id="nav")
		nav_links = nav.find_all('a')
		for nn in nav_links:
			next = nn.find(id="nx")
			if next is not None and nn["href"] is not None:
				return u"{}{}".format(u"http://oglaf.com", nn["href"])

		return None

