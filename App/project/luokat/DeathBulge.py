# -*- coding: utf-8 -*-
from project import db
from bs4 import BeautifulSoup
import datetime, urllib, os, requests, hashlib
from project.luokat.Sarjis import Sarjis

class DeathBulge(Sarjis):

	def __init__(self, sarjakuva, urli=None ):
		Sarjis.__init__(self, sarjakuva, urli)
	
	def Kuva(self):

		images = self.soup.find_all("img")
		for i in images:
			print i

		kuvan_nimi = None
		src = None
		div = self.soup.find(id="comic")
		#print self.soup
		img = div.find(id="comic-image")
		#img = div.find("img", {"class": "center-block"})
		kuva = img["src"].split("/")
		kuvan_nimi = kuva[len(kuva)-1]+".jpg" # haetaan nimi
		src = img["src"]
		if src[0] == "/":
			src = src[1:]

		src = u"{}{}".format(self.sarjakuva.url, src)
		
		return dict(nimi=kuvan_nimi, src=src)

		
		

	def Next(self):
		link = self.soup.find_all(id="next-button")
		link["href"] = link["href"].replace("#/", "")

		url = u"{}{}".format(self.sarjakuva.url, link["href"])
		if url != self.sarjakuva.last_url:
			return url
		
		return None

