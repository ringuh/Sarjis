# -*- coding: utf-8 -*-
from project import db
from bs4 import BeautifulSoup
import datetime, urllib, os, requests, hashlib
from project.luokat.Sarjis import Sarjis

class FoxTrot(Sarjis):

	def __init__(self, sarjakuva, urli=None ):
		Sarjis.__init__(self, sarjakuva, urli)
	
	def Kuva(self):
		src = None
		kuvan_nimi = None
		
		div = self.soup.find("article")
		div = div.find("div", { "class" : "entry-content" })
		
		img = div.find("img")
		src = img["src"]
	
		kuva = img["src"].split("/")
		kuvan_nimi = kuva[len(kuva)-1] # haetaan nimi
		
		# if src.index("./") == 0:
		#  	src = u"{}{}".format(self.sarjakuva.url, src[2:])

		
		return dict(nimi=kuvan_nimi, src=src)

		
		

	def Next(self):
		#print "in next"
		div = self.soup.find("div", { "class" : "entry-navarrows" })
		links = div.find_all("a")
		for link in links:
			rel = link.get("rel")
			
			if rel is not None and "next" in rel:
				return link["href"]
		
		
		return None

