# -*- coding: utf-8 -*-
from project import db
from bs4 import BeautifulSoup
import datetime, urllib, os, requests, hashlib
from project.luokat.Sarjis import Sarjis

class CtrlAltDel(Sarjis):
	# SARJIS.info parseri, koska ctrlaltdel jotenkin suojattu?

	def __init__(self, sarjakuva, urli=None ):
		Sarjis.__init__(self, sarjakuva, urli)
	
	def Kuva(self):
		src = None
		kuvan_nimi = None

		div = self.soup.find(id="sisalto")
		div = div.find("div", { "class": "sarjakuva_vasen"})
		img = div.find("img")
		src = img["src"]
		kuva = img["src"].split("/")
		kuvan_nimi = kuva[len(kuva)-1] # haetaan nimi
			
		#print kuvan_nimi, src
		return dict(nimi=kuvan_nimi, src=src)

		
		

	def Next(self):
		div = self.soup.find(id="seuraava")
		
		if div is not None:
			return div["href"]
		
		return None


	