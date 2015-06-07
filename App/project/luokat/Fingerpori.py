# -*- coding: utf-8 -*-
from project import db
from bs4 import BeautifulSoup
import datetime, urllib, os, requests, hashlib
from project.luokat.Sarjis import Sarjis

class Fingerpori(Sarjis):

	def __init__(self, sarjakuva, urli=None ):
		Sarjis.__init__(self, sarjakuva, urli)
	
	def Kuva(self):

		img = self.soup.find(id="full-comic")
		img = img.find("img")

		tmp = self.urli.split("/")
		kuvan_nimi = tmp[len(tmp)-1]+".jpg" # muodostetaan nimi
		
		return dict(nimi=kuvan_nimi, src=img["src"])


	def Next(self):
		next = self.soup.find("a", { "class" : "next-cm" })

		if next is not None and not "next-cm-disabled" in next["class"]:
			return u"{}{}".format("http://www.hs.fi", next["href"])

		return None

