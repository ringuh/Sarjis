# -*- coding: utf-8 -*-
from project import db, app
from bs4 import BeautifulSoup
from project.models import Sarjakuva as SK, Strippi as ST
import datetime, urllib, os, requests, hashlib
from project.luokat import *
import sys


def run():
	nr = int(sys.argv[2])

	n = db.session.query(ST).filter(
			ST.sarjakuva_id == nr
		).order_by(ST.id).all()

	offset = len(n)

	for i in n:
		offset -= 1
		i.date_created = i.date_created - datetime.timedelta(days=offset)

	db.session.commit()
