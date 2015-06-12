# -*- coding: utf-8 -*-
from project import db
from bs4 import BeautifulSoup
import datetime, urllib, os, requests, hashlib
from project.luokat.Sarjis import Sarjis

class Wulffmorgenthaler(Sarjis):

	def __init__(self, sarjakuva, urli=None ):
		Sarjis.__init__(self, sarjakuva, urli)
	
	def Kuva(self):
		kuvan_nimi = None
		src = None

		
		
		return dict(nimi=kuvan_nimi, src=src)

		
		

	def Next(self):
		#link = self.soup.find("a", {"class": "comic-arrow-right"})
		#if link is not None and link["href"] != "#":
		#	return link["href"]
		
		return None

