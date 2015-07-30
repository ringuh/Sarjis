# -*- coding: utf-8 -*-
from project import db
from bs4 import BeautifulSoup
import datetime, urllib, os, requests, hashlib
from project.luokat.Sarjis import Sarjis

class PowerNap(Sarjis):

	def __init__(self, sarjakuva, urli=None ):
		Sarjis.__init__(self, sarjakuva, urli)
	
	def Kuva(self):
		kuvan_nimi = None
		src = None
		img = None
		
		centers = self.soup.find_all("center")
		
		for i in centers:
			center = i.find("center")
			pic = i.find("img")
			br = i.find("br")
			if center is None and pic is not None and br is not None:
				img = pic
		img["src"] = img["src"].replace("\n", "")
		#print "'"+img["src"]+"'"
		kuva = img["src"].split("/")
		kuvan_nimi = kuva[len(kuva)-1] # haetaan nimi
		src = img["src"]
		
		return dict(nimi=kuvan_nimi, src=src)

		
		

	def Next(self):
		links = self.soup.find_all("a")
		
		for link in links:
			img = link.find("img")

			if img is not None and img.get("alt") is not None and img.get("alt").lower() == "the next comic":
				if link["href"] != "#":
					return u"{}".format(link["href"])
		
		return None
