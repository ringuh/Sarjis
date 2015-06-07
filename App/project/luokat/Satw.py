# -*- coding: utf-8 -*-
from project import db
from bs4 import BeautifulSoup
import datetime, urllib, os, requests, hashlib
from project.luokat.Sarjis import Sarjis

class Satw(Sarjis):

	def __init__(self, sarjakuva, urli=None ):
		Sarjis.__init__(self, sarjakuva, urli)
	
	def Kuva(self):
		src = None
		kuvan_nimi = None

		divs = self.soup.find_all("center")
		for div in divs:
			img = div.find("img")
			#print img
			if img is not None and "/art/" in img["src"]:
				src = img["src"]
				kuva = img["src"].split("/")
				kuvan_nimi = kuva[len(kuva)-1] # haetaan nimi
				break
		#print kuvan_nimi, src
		return dict(nimi=kuvan_nimi, src=src)

		
		

	def Next(self):
		links = self.soup.find_all("a")
		for link in links:
			rel = link.get("accesskey")
		
			if rel is not None and "n" in rel:
				return link["href"]
		
		
		return None

