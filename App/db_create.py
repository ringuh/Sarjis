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
db.session.add(Sarjakuva(u"VGCats", 
				u"http://www.vgcats.com/comics/", 
				u"Scott Ramsoomair", 
				12,
				u"http://www.vgcats.com/comics/?strip_id=1" ))
db.session.add(Sarjakuva(u"Nerf Now", 
				u"http://www.nerfnow.com/", 
				u"Josué Pereira", 
				13,
				u"http://www.nerfnow.com/comic/4" ))
db.session.add(Sarjakuva(u"Sinfest", 
				u"http://www.sinfest.net/", 
				u"Tatsuya Ishida", 
				14,
				u"http://www.sinfest.net/view.php?date=2000-01-17" ))
db.session.add(Sarjakuva(u"Camp Comic", 
				u"http://campcomic.com/", 
				u"Dani", 
				15,
				u"http://campcomic.com/comic/dear-mom" ))
db.session.add(Sarjakuva(u"Fredo & Pidjin", 
				u"http://www.pidjin.net/", 
				u"Dani", 
				16,
				u"http://www.pidjin.net/2005/05/30/tricks-to-getting-delayed/" ))
db.session.add(Sarjakuva(u"U.S. Acres", 
				u"http://garfield.com/us-acres", 
				u"Jim Davis", 
				17,
				u"http://garfield.com/us-acres/2012-06-01" ))
db.session.add(Sarjakuva(u"Garfield", 
				u"http://garfield.com/comic", 
				u"Jim Davis", 
				17,
				u"http://garfield.com/comic/2012-06-01" ))

db.session.add(Sarjakuva(u"Least I could do", 
				u"http://www.leasticoulddo.com/comic/", 
				u"Ryan Sohmer & Trevor Adams", 
				18,
				u"http://www.leasticoulddo.com/comic/20030210/" ))
db.session.add(Sarjakuva(u"Questionable Content", 
				u"http://questionablecontent.net/", 
				u"Jeph Jacques", 
				19,
				u"http://questionablecontent.net/view.php?comic=1" ))

db.session.add(Sarjakuva(u"Wulffmorgenthaler", 
				u"http://kindofnormal.com/wumo/", 
				u"Wumo", 
				6, # vaihda in future
				u"http://www.sarjis.info/sarjakuvat/wulffmorgenthaler/95/" ))

db.session.add(Sarjakuva(u"Lassi ja Leevi", 
				u"http://www.gocomics.com/calvinandhobbes/", 
				u"Bill Watterson", 
				20, # vaihda in future
				u"http://www.gocomics.com/calvinandhobbes/2014/06/13" ))
db.session.add(Sarjakuva(u"Penny Arcade", 
				u"http://www.penny-arcade.com/", 
				u"Mike Krahulik & Jerry Holkins", 
				21,
				u"http://www.penny-arcade.com/comic/1998/11/18" ))

#db.session.add(Sarjakuva(u"Gunshow", 
#				u"http://www.gunshowcomic.com/", 
#				u"KC Green", 
#				22,
#				u"http://www.gunshowcomic.com/1" ))

db.session.commit()