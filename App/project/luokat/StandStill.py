# -*- coding: utf-8 -*-
from project import db
from bs4 import BeautifulSoup
import datetime, urllib, os, requests, hashlib
from project.luokat.Sarjis import Sarjis

class StandStill(Sarjis):

	def __init__(self, sarjakuva, urli=None ):
		Sarjis.__init__(self, sarjakuva, urli)
	
	def Kuva(self):
		src = None
		kuvan_nimi = None
		
		div = self.soup.find(id="wrapper2")
		img = div.find("img")
		src = img["src"]
		kuva = img["src"].split("/")
		kuvan_nimi = kuva[len(kuva)-1] # haetaan nimi
		
		src = u"{}{}".format(self.sarjakuva.url, src.strip())
		# if src.index("//") == 0:
		# 	src = u"http:{}".format(src)

		
		return dict(nimi=kuvan_nimi, src=src)

		
		

	def Next(self):
		#print "in next"
		div = self.soup.find(id="navtop")
		links = div.find_all("a")
		for link in links:
			btn = link.find(id="navnext")
			if btn is not None:
				return u"{}comic.php{}".format(self.sarjakuva.url, link["href"])
		
		return None

