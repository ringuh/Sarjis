# -*- coding: utf-8 -*-
from project import db
from bs4 import BeautifulSoup
import datetime, urllib, os, requests, hashlib
from project.luokat.Sarjis import Sarjis

class VGCats(Sarjis):
	# SARJIS.info parseri, koska ctrlaltdel jotenkin suojattu?

	def __init__(self, sarjakuva, urli=None ):
		Sarjis.__init__(self, sarjakuva, urli)
	
	def Kuva(self):
		src = None
		kuvan_nimi = None

	
		found = self.soup.find_all("img")
		img = None
		for i in found:
			table = i.find("table")
			if table is not None:
				img = i

		src = u"{}{}".format(self.sarjakuva.url, img["src"])
		kuva = img["src"].split("/")
		kuvan_nimi = kuva[len(kuva)-1] # haetaan nimi
			
		#print kuvan_nimi, src
		return dict(nimi=kuvan_nimi, src=src)
		

	def Next(self):
		
		linkit = self.soup.find_all("a")
		
		for i in linkit:
			tmp = i.find("img")
			if tmp is not None and tmp["src"] == "next.gif":
				return u"{}{}".format(self.sarjakuva.url, i["href"])
		
		return None


	