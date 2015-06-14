# -*- coding: utf-8 -*-
from project import db
from bs4 import BeautifulSoup
import datetime, urllib, os, requests, hashlib
from project.luokat.Sarjis import Sarjis

class CSection(Sarjis):
	# SARJIS.info parseri, koska ctrlaltdel jotenkin suojattu?

	def __init__(self, sarjakuva, urli=None ):
		Sarjis.__init__(self, sarjakuva, urli)
	
	def Kuva(self):
		kuvan_nimi = None
		src = None
		
		div = self.soup.find(id="comic")
		img = div.find("img")
		kuva = img["src"].split("/")
		kuvan_nimi = kuva[len(kuva)-1] # haetaan nimi
		src = img["src"]

		url = self.urli.split("/")
		url.pop()
		self.t_url = "/".join(url)
		src = u"{}/{}".format(self.t_url, src)
		
		
		return dict(nimi=kuvan_nimi, src=src)

		
		

	def Next(self):
		link = self.soup.find("a", {"class": "forward"})
		if ".html" in link["href"]:
			
			return u"{}/{}".format(self.t_url, link["href"])

		
		return None


	