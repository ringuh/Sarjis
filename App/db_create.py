# -*- coding: utf-8 -*-
from project import db
import random
import datetime
from project.models import *

db.drop_all()
#luo db
db.create_all()
db.session.flush()

# 
u = User(u"ringuh", u"zerg", True)
db.session.add(u)

# sarjikset
db.session.add(Sarjakuva(u"Oglaf", 
				u"http://oglaf.com", 
				u"Trydy Cooper, Doub Bayne", 
				1,
				u"http://oglaf.com/cumsprite/" ))

db.session.add(Sarjakuva(u"Fingerpori", 
				u"http://www.hs.fi/fingerpori", 
				u"Pertti Jarla", 
				2,
				u"http://www.hs.fi/fingerpori/s1349775187323" ))

db.session.add(Sarjakuva(u"Viivi ja Wagner", 
				u"http://www.hs.fi/viivijawagner", 
				u"Juba Tuomola", 
				2,
				u"http://www.hs.fi/viivijawagner/s1349773144978" ))

db.session.add(Sarjakuva(u"The Order of the Stick", 
				u"http://www.giantitp.com", 
				u"Giantitp", 
				3,
				u"http://www.giantitp.com/comics/oots0001.html" ))

db.session.add(Sarjakuva(u"Toonhole", 
				u"http://toonhole.com", 
				u"Toonhole", 
				4,
				u"http://toonhole.com/2010/01/smart-questions-get-smart-answers/" ))

db.session.add(Sarjakuva(u"Scandinavia and the World", 
				u"http://satwcomic.com/", 
				u"SatW", 
				5,
				u"http://satwcomic.com/sweden-denmark-and-norway" ))
db.session.add(Sarjakuva(u"Ctrl+Alt+Del", 
				u"http://www.cad-comic.com", 
				u"Tim Buckley", 
				6,
				u"http://www.sarjis.info/sarjakuvat/ctrl-alt-del/1/" ))
db.session.add(Sarjakuva(u"Cyanide and Happiness", 
				u"http://explosm.net", 
				u"Explosm", 
				7,
				u"http://explosm.net/comics/15" ))
db.session.add(Sarjakuva(u"Dragonarte", 
				u"http://dragonarte.com.br/", 
				u"Dragonarte", 
				8,
				u"http://dragonarte.com.br/admin/tirinhas" ))
db.session.add(Sarjakuva(u"Paintrain", 
				u"http://paintraincomic.com/", 
				u"Mark Pain", 
				9,
				u"http://paintraincomic.com/comic/romance/" ))
db.session.add(Sarjakuva(u"HappleTea", 
				u"http://www.happletea.com", 
				u"Scott Maynard", 
				10,
				u"http://www.happletea.com/comic/fallacies/" ))
db.session.add(Sarjakuva(u"Skadi", 
				u"http://skadicomic.com", 
				u"Katie Rice, Luke Cormican", 
				11,
				u"http://skadicomic.com/2008/05/07/ballad-of-skadi-pt-1-2/" ))


db.session.commit()