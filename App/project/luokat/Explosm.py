# -*- coding: utf-8 -*-
from project import db
from bs4 import BeautifulSoup
import datetime, urllib, os, requests, hashlib
from project.luokat.Sarjis import Sarjis

class Explosm(Sarjis):
	# SARJIS.info parseri, koska ctrlaltdel jotenkin suojattu?

	def __init__(self, sarjakuva, urli=None ):
		Sarjis.__init__(self, sarjakuva, urli)
	
	def Kuva(self):
		src = None
		kuvan_nimi = None

		img = self.soup.find(id="main-comic")
		src = u"http:{}".format(img["src"])
		kuva = img["src"].split("/")
		kuvan_nimi = kuva[len(kuva)-1] # haetaan nimi
			
		#print kuvan_nimi, src
		return dict(nimi=kuvan_nimi, src=src)
		

	def Next(self):
		div = self.soup.find("a", { "class": "next-comic" })
		
		if div is not None and len(div["href"]) > 1:
			return u"{}{}".format(self.sarjakuva.url, div["href"])
		
		return None


	