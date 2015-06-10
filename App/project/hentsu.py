# -*- coding: utf-8 -*-
from bs4 import BeautifulSoup
import datetime, urllib2, os, requests, hashlib
from werkzeug.urls import url_fix

url = "http://amt.fi/fi/publication/42/alihankinta-2015-messuopas/"
r = requests.get(url_fix(url))
soup = BeautifulSoup(r.text)

companies = soup.find_all("tr", {"class":"company"})
base_url = "http://amt.fi"
csv = "";
fo = open("hentsu.csv", 'w')
fo.write(u"nimi, www, to_go, maa, koodi".encode('utf-8'))
fo.close()

count = 0
for i in companies:
	count += 1
	maa = None
	koodi = None
	nimi = None
	urli = None
	www = None
	try:
		nimi_arr = i.find("td", {"class":"company-name"})
		comp_link = nimi_arr.find("a")
		nimi = unicode(comp_link.text).strip()
		maa = i.find("td", {"class":"company-country"}).text.strip()
		koodi = i.find("td", {"class":"company-stand-list"}).text.strip()
		urli = comp_link["href"].strip()
		#print u"{}{}".format(base_url, urli)
		to_go = url_fix(u"{}{}".format(base_url, urli))
		try:
			print count, len(companies), to_go
			tr = requests.get(to_go)
			tsoup = BeautifulSoup(tr.text)
			#print tsoup
			www = tsoup.find("p", { "class": "company-website"}).text.strip()
		except Exception, e:
			www = None
			raise e
		
			
			#print "---"
			#print nimi, maa, koodi, urli,www
		csv = u"\n{},{},{},{},{}".format(nimi, www, to_go, maa, koodi).encode('utf-8')
		fo = open('hentsu.csv','a')
		fo.write(csv)
		fo.close()
		#print csv
	except Exception, e:
	#	#csv += u"{}, {}, {}, {} ,{};".format(nimi, comp_link, to_go, maa, koodi)
		print i
		raise e
		
#print csv


#print companies[0]
	