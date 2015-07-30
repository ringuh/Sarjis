# -*- coding: utf-8 -*-
from project import db
from bs4 import BeautifulSoup
import datetime, urllib, os, requests, hashlib
from project.luokat.Sarjis import Sarjis

class ItsTheTie(Sarjis):

	def __init__(self, sarjakuva, urli=None ):
		Sarjis.__init__(self, sarjakuva, urli)
	
	def Kuva(self):
		kuvan_nimi = None
		src = None

		img = self.soup.find("img", { "class": "alignnone"})
		kuva = img["src"].split("/")
		kuvan_nimi = kuva[len(kuva)-1] # haetaan nimi
		src = img["src"]
		
		return dict(nimi=kuvan_nimi, src=src)

	def Next(self):
		nav = self.soup.find("div", {"class":"nav-next"})
	
		link = nav.find("a")
		if link is not None:
			return link["href"]
		
		return None

