# -*- coding: utf-8 -*-
from project import db
from bs4 import BeautifulSoup
import datetime, urllib, os, requests, hashlib
from project.luokat.Sarjis import Sarjis, Strippi

class Dorkly(Sarjis):

	def __init__(self, sarjakuva, urli=None ):
		Sarjis.__init__(self, sarjakuva, urli)
	
	def Kuva(self):
		kuvan_nimi = None
		src = None

		div = self.soup.find("div", { "class": "post-content"})
		img = self.soup.find("img", { "class": "img-comic"})
		#img = div.find("img", {"class": "center-block"})
		kuva = img["src"].split("/")
		kuvan_nimi = kuva[len(kuva)-1]+".jpg" # haetaan nimi
		src = img["src"]
		
		return dict(nimi=kuvan_nimi, src=src)

		
		

	def Next(self):
		print "next"
		#nav = self.soup.find("nav", { "class": "arrow-next"})
		#link = nav.find("a", { "class": "anchor_next"})
		try:
			nav = self.soup.find("div", { "class": "pagination"})
			link = nav.find("a", { "class": "next"})
			
			if link is not None and link["href"] != "#":
				tmp = u"{}{}".format(self.sarjakuva.url[:-1], link["href"])
				n = db.session.query(Strippi).filter(
						Strippi.url == tmp ).first()
				if n is None:
					return u"{}{}".format(self.sarjakuva.url[:-1], link["href"])
			
		except:
			return self.AltCheck()
		
		return None


	def Loop(self, sarjakuva=None, url=None): # ylikirjoitetaan looppi
		if sarjakuva is not None: # initoidaan uudella urlilla
			self.Init(sarjakuva, url)

		div = self.soup.find("div", { "class": "post-content"})

		images = div.find_all("img")
		for img in images:
			url = img["src"]
			if url is None or "download.jpg" in url:
				continue
			nimi =  url.split("/")[-1] # haetaan nimi
			
			self.Save(nimi, url)
					
		return self.Next()



	def AltCheck(self):
		r = requests.get("http://www.dorkly.com/comics")
		soup = BeautifulSoup(r.text)

		div = soup.find("div", { "class": "content"})

		links = div.find_all("a", {"class": "thumb"})

		prev_url = None
		for link in links:
			url = link["href"]
			if "ref=comics" in url:
				tmp = u"{}{}".format(self.sarjakuva.url[:-1], url)
				n = db.session.query(Strippi).filter(
					Strippi.url == tmp ).first()

				if n is None:
					prev_url = tmp
				else:
					break
		return prev_url 