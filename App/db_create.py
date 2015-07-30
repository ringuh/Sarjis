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

coms = [
	Sarjakuva( 	
		u"Oglaf", 
		u"oglaf", 
		u"http://oglaf.com", 
		u"Trydy Cooper, Doub Bayne", 
		1,
		u"http://oglaf.com/cumsprite/"
	),
	Sarjakuva(
		u"Fingerpori", 
		u"fingerpori",
		u"http://www.hs.fi/fingerpori", 
		u"Pertti Jarla", 
		2,
		u"http://www.hs.fi/fingerpori/s1349775187323" 
	),
	Sarjakuva(
		u"Viivi ja Wagner", 
		u"viivijawagner",
		u"http://www.hs.fi/viivijawagner", 
		u"Juba Tuomola", 
		2,
		u"http://www.hs.fi/viivijawagner/s1349773144978" 
	),
	Sarjakuva(
		u"The Order of the Stick", 
		u"oots",
		u"http://www.giantitp.com", 
		u"Giantitp", 
		3,
		u"http://www.giantitp.com/comics/oots0001.html" 
	),
	Sarjakuva(
		u"Toonhole", 
		u"toonhole",	
		u"http://toonhole.com", 	
		u"Toonhole", 		
		4,
		u"http://toonhole.com/2010/01/smart-questions-get-smart-answers/" 
	),
	Sarjakuva(
		u"Scandinavia and the World", 
		u"satw",
		u"http://satwcomic.com/", 
		u"SatW", 
		5,
		u"http://satwcomic.com/sweden-denmark-and-norway" 
	),
	Sarjakuva(
		u"Ctrl+Alt+Del", 
		u"cad",
		u"http://www.cad-comic.com", 
		u"Tim Buckley", 
		6,
		u"http://www.sarjis.info/sarjakuvat/ctrl-alt-del/1/" 
	),
	Sarjakuva(
		u"Cyanide and Happiness", 
		u"explosm",
		u"http://explosm.net", 
		u"Explosm", 
		7,
		u"http://explosm.net/comics/15"
	),
	Sarjakuva(
		u"Dragonarte", 
		u"dragonarte",
		u"http://dragonarte.com.br/", 
		u"Dragonarte", 
		8,
		u"http://dragonarte.com.br/admin/tirinhas"
	),
	Sarjakuva(
		u"Paintrain", 
		u"paintrain",
		u"http://paintraincomic.com/", 
		u"Mark Pain", 
		9,
		u"http://paintraincomic.com/comic/romance/"
	),
	Sarjakuva(
		u"Gunshow", 
		u"gunshow",
		u"http://www.gunshowcomic.com/", 
		u"KC Green", 
		10,
		u"http://www.gunshowcomic.com/1"
	),
	Sarjakuva(
		u"HappleTea", 
		u"happletea",
		u"http://www.happletea.com", 
		u"Scott Maynard", 
		11,
		u"http://www.happletea.com/comic/fallacies/"
	),
	Sarjakuva(
		u"Skadi", 
		u"skadi",
		u"http://skadicomic.com", 
		u"Katie Rice, Luke Cormican", 
		11,
		u"http://skadicomic.com/2008/05/07/ballad-of-skadi-pt-1-2/"
	),
	Sarjakuva(
		u"VGCats", 
		u"vgcats",
		u"http://www.vgcats.com/comics/", 
		u"Scott Ramsoomair", 
		12,
		u"http://www.vgcats.com/comics/?strip_id=1"
	),
	Sarjakuva(
		u"Nerf Now", 
		u"nerfnow",
		u"http://www.nerfnow.com/", 
		u"Josué Pereira", 
		13,
		u"http://www.nerfnow.com/comic/4"
	),
	Sarjakuva(
		u"Sinfest", 
		u"sinfest",
		u"http://www.sinfest.net/", 
		u"Tatsuya Ishida", 
		14,
		u"http://www.sinfest.net/view.php?date=2000-01-17",
		True
	),
	Sarjakuva(
		u"Camp", 
		u"camp",
		u"http://campcomic.com/", 
		u"Dani", 
		15,
		u"http://campcomic.com/comic/dear-mom"
	),
	Sarjakuva(
		u"Fredo & Pidjin", 
		u"fredo_pidjin",
		u"http://www.pidjin.net/", 
		u"Dani", 
		16,
		u"http://www.pidjin.net/2005/05/30/tricks-to-getting-delayed/"
	),
	Sarjakuva(
		u"U.S. Acres", 
		u"usacres",
		u"http://garfield.com/us-acres", 
		u"Jim Davis", 
		17,
		u"http://garfield.com/us-acres/2012-06-01",
		True
	),
	Sarjakuva(
		u"Garfield", 
		u"garfield",
		u"http://garfield.com/comic", 
		u"Jim Davis", 
		17,
		u"http://garfield.com/comic/2012-06-01",
		True
	),

	Sarjakuva(
		u"Least I could do", 
		u"licd",
		u"http://www.leasticoulddo.com/comic/", 
		u"Ryan Sohmer & Trevor Adams", 
		18,
		u"http://www.leasticoulddo.com/comic/20030210/"
	),
	Sarjakuva(
		u"Questionable Content", 
		u"qc",
		u"http://questionablecontent.net/", 
		u"Jeph Jacques", 
		19,
		u"http://questionablecontent.net/view.php?comic=1"
	),

	Sarjakuva(
		u"Wulffmorgenthaler", 
		u"wumo",
		u"http://kindofnormal.com/wumo/", 
		u"Wumo", 
		6, # vaihda in future
		u"http://www.sarjis.info/sarjakuvat/wulffmorgenthaler/95/"
	),
	# GO COMICS
	Sarjakuva(
		u"Lassi ja Leevi", 
		u"lassi",
		u"http://www.gocomics.com/calvinandhobbes/", 
		u"Bill Watterson", 
		20, # vaihda in future
		u"http://www.gocomics.com/calvinandhobbes/2014/06/13",
		True
	),
	Sarjakuva(
		u"The Flying MCCoys", 
		u"mccoys",
		u"http://www.gocomics.com/theflyingmccoys/", 
		u"Glenn and Gary McCoy", 
		20, # vaihda in future
		u"http://www.gocomics.com/theflyingmccoys/2012/06/01",
		True
	),
	Sarjakuva(
		u"Pearls Before Swine", 
		u"pearls",
		u"http://www.gocomics.com/pearlsbeforeswine/", 
		u"Stephan Pastis", 
		20, # vaihda in future
		u"http://www.gocomics.com/pearlsbeforeswine/2012/06/01",
		True
	),
	Sarjakuva(
		u"9 Chickweed Lane", 
		u"9chickweedlane",
		u"http://www.gocomics.com/9chickweedlane", 
		u"Brooke McEldowney", 
		20, # vaihda in future
		u"http://www.gocomics.com/9chickweedlane/2012/06/01",
		True
	),

	# END OF GO COMICS
	Sarjakuva(
		u"Penny Arcade", 
		u"pennyarcade",
		u"http://www.penny-arcade.com/", 
		u"Mike Krahulik & Jerry Holkins", 
		21,
		u"http://www.penny-arcade.com/comic/1998/11/18"
	),
	Sarjakuva(
		u"Tales of Valoran", 
		u"valoran",
		u"http://www.talesofvaloran.com/", 
		u"lendokhar", 
		11,
		u"http://www.talesofvaloran.com/?p=21"
	),
	Sarjakuva(
		u"Johnny Wander Fiction", 
		u"jwfiction",
		u"http://www.johnnywander.com/fiction", 
		u"Ananth Panagariya & Yoko Ota", 
		22,
		u"http://www.johnnywander.com/fiction/girl-with-the-skeleton-hand-1"
	),
	Sarjakuva(
		u"Lucky Penny", 
		u"luckypenny",
		u"http://www.johnnywander.com/luckypenny", 
		u"Ananth Hirsh & Yoko Ota", 
		22,
		u"http://www.johnnywander.com/luckypenny/lucky-penny-001"
	),
	Sarjakuva(
		u"Autobio", 
		u"autobio",
		u"http://www.johnnywander.com/autobio", 
		u"Ananth Hirsh & Yoko Ota", 
		22,
		u"http://www.johnnywander.com/autobio/i"
	),
	Sarjakuva(
		u"For lack of a better comic", 
		u"floabc",
		u"http://www.forlackofabettercomic.com/", 
		u"Jacob Andrews", 
		23,
		u"http://forlackofabettercomic.com/?id=1"
	),
	Sarjakuva(
		u"Cheer Up, Emo Kid", 
		u"cheerup",
		u"http://www.cheerupemokid.com/", 
		u"Enzo", 
		24,
		u"http://www.cheerupemokid.com/comic/truth"
	),
	Sarjakuva(
		u"Love Me Nice", 
		u"lovemenice",
		u"http://lovemenicecomic.com/comic/", 
		u"Amanda Lafrenais", 
		25,
		u"http://lovemenicecomic.com/comic/001.php"
	),
	Sarjakuva(
		u"Hamlet's Danish", 
		u"hamlet",
		u"http://clayyount.com/hamlets-danish", 
		u"Clay Yount", 
		26,
		u"http://clayyount.com/hamlets-danish-comic/2014/4/7/one-question"
	),
	Sarjakuva(
		u"Avas Demon", 
		u"avasdemon",
		u"http://www.avasdemon.com/", 
		u"Michelle Czajkowski", 
		27,
		u"http://www.avasdemon.com/chapters.php"
	),
	Sarjakuva(
		u"Manly Guys Doing Manly Things", 
		u"machismo",
		u"http://thepunchlineismachismo.com/", 
		u"", 
		28,
		u"http://thepunchlineismachismo.com/archives/comic/02222010"
	),
	Sarjakuva(
		u"Im my own Mascot", 
		u"imomascot",
		u"http://www.interrobangstudios.com/comics-display.php?comic_id=9", 
		u"", 
		29,
		u"http://interrobangstudios.com/comics-display.php?strip_id=141"
	),
	Sarjakuva(
		u"Wookie-ookies", 
		u"wookie",
		u"http://www.interrobangstudios.com/comics-display.php?comic_id=18", 
		u"", 
		29,
		u"http://interrobangstudios.com/comics-display.php?strip_id=929"
	),
	Sarjakuva(
		u"Things Which Defy Categorization", 
		u"twdc",
		u"http://www.interrobangstudios.com/comics-display.php?comic_id=17", 
		u"", 
		29,
		u"http://interrobangstudios.com/comics-display.php?strip_id=49"
	),
	Sarjakuva(
		u"Fair-Haired Adventure Seekers", 
		u"adventureseekers",
		u"http://www.interrobangstudios.com/comics-display.php?comic_id=6", 
		u"", 
		29,
		u"http://interrobangstudios.com/comics-display.php?strip_id=930"
	),
	Sarjakuva(
		u"It sucks to be Weegie", 
		u"weegie",
		u"http://www.interrobangstudios.com/comics-display.php?comic_id=11", 
		u"", 
		29,
		u"http://interrobangstudios.com/comics-display.php?strip_id=941"
	),
	Sarjakuva(
		u"WatchBabies", 
		u"watchbabies",
		u"http://www.interrobangstudios.com/comics-display.php?comic_id=7", 
		u"", 
		29,
		u"http://interrobangstudios.com/comics-display.php?strip_id=959"
	),
	Sarjakuva(
		u"Ensign3 Crisis of Infinite Sues", 
		u"ensign3",
		u"http://www.interrobangstudios.com/comics-display.php?comic_id=10", 
		u"", 
		29,
		u"http://interrobangstudios.com/comics-display.php?strip_id=989"
	),
	Sarjakuva(
		u"Spinks", 
		u"spinks",
		u"http://www.spinkspink.com/", 
		u"", 
		29,
		u"http://www.spinkspink.com/index.php?strip_id=78"
	),
	Sarjakuva(
		u"Trigger Star", 
		u"triggerstar",
		u"http://www.triggerstar.com/", 
		u"", 
		29,
		u"http://www.triggerstar.com/index.php?strip_id=60"
	),
	Sarjakuva(
		u"The Dark Intruder", 
		u"darkintruder",
		u"http://www.interrobangstudios.com/comics-display.php?comic_id=1", 
		u"", 
		29,
		u"http://interrobangstudios.com/comics-display.php?strip_id=1"
	),
	Sarjakuva(
		u"A Girl Named Bob", 
		u"girlbob",
		u"http://www.interrobangstudios.com/comics-display.php?comic_id=3", 
		u"", 
		29,
		u"http://interrobangstudios.com/comics-display.php?strip_id=31"
	),
	Sarjakuva(
		u"This is Visas", 
		u"visas",
		u"http://www.interrobangstudios.com/comics-display.php?comic_id=13", 
		u"", 
		29,
		u"http://interrobangstudios.com/comics-display.php?strip_id=357"
	),
	Sarjakuva(
		u"Heeere's Satan", 
		u"heresatan",
		u"http://www.interrobangstudios.com/comics-display.php?comic_id=15", 
		u"", 
		29,
		u"http://interrobangstudios.com/comics-display.php?strip_id=146"
	),
	Sarjakuva(
		u"Punker Darren", 
		u"punkerdarren",
		u"http://www.interrobangstudios.com/comics-display.php?comic_id=2", 
		u"", 
		29,
		u"http://interrobangstudios.com/comics-display.php?strip_id=16"
	),
	Sarjakuva(
		u"Space is really big!", 
		u"bigspace",
		u"http://www.interrobangstudios.com/comics-display.php?comic_id=12", 
		u"", 
		29,
		u"http://interrobangstudios.com/comics-display.php?strip_id=55"
	),

	Sarjakuva(
		u"Unsounded", 
		u"unsounded",
		u"http://www.casualvillain.com/Unsounded/comic+index", 
		u"Ashley Cope", 
		30,
		u"http://www.casualvillain.com/Unsounded/comic/ch01/ch01_01.html"
	),

	Sarjakuva(
		u"C-Section", 
		u"csection",
		u"http://www.csectioncomics.com/", 
		u"", 
		11,
		u"http://www.csectioncomics.com/2010/04/one-day-in-country.html"
	),

	Sarjakuva(
		u"Merkworks", 
		u"merkworks",
		u"http://mercworks.net/", 
		u"Dave Mercier", 
		9,
		u"http://mercworks.net/comicland/a-comic/"
	),

	Sarjakuva(
		u"Extra Fabulous", 
		u"extrafabulouscomics",
		u"http://extrafabulouscomics.com/", 
		u"ZMS", 
		11,
		u"http://extrafabulouscomics.com/comic/buttfly/"
	),
	Sarjakuva(
		u"Catsu The Cat", 
		u"catsu",
		u"http://www.catsuthecat.com/blogs/comics/", 
		u"Daria", 
		31,
		u"http://www.catsuthecat.com/blogs/comics/"
	),

	Sarjakuva(
		u"The Perry Bible Fellowship", 
		u"pbf",
		u"http://pbfcomics.com", 
		u"Daria", 
		32,
		u"http://pbfcomics.com/1/"
	),

	Sarjakuva(
		u"Dilbert", 
		u"dilbert",
		u"http://dilbert.com", 
		u"Scott Adams", 
		33,
		u"http://dilbert.com/strip/2015-01-11"
	),
	Sarjakuva(
		u"Pepper and Carrot", 
		u"peppercarrot",
		u"http://www.peppercarrot.com/", 
		u"David Revoy", 
		34,
		u"http://www.peppercarrot.com/en/static6/sources"
	),

	Sarjakuva(
		u"Berkeley Mews", 
		u"berkeleymews",
		u"http://www.berkeleymews.com/", 
		u"benzaehringer at gmail.com", 
		11,
		u"http://www.berkeleymews.com/?p=19"
	),
	Sarjakuva(
		u"Completely Serious Comics", 
		u"completelyseriouscomics",
		u"http://completelyseriouscomics.com/", 
		u"completelyseriouscomics", 
		11,
		u"http://completelyseriouscomics.com/?p=6"
	),
	Sarjakuva(
		u"Pictures in Boxes", 
		u"picturesinboxes",
		u"http://www.picturesinboxes.com/", 
		u"picturesinboxes", 
		11,
		u"http://www.picturesinboxes.com/2013/10/26/tetris/"
	),

	Sarjakuva(
		u"Rational Comics", 
		u"rational",
		u"http://www.rationalcomics.com/", 
		u"Joshua Sim", 
		35,
		u"http://www.rationalcomics.com/001-mountain-moving-man/"
	),

	Sarjakuva(
		u"Loading Artist", 
		u"loadingartist",
		u"http://www.loadingartist.com/", 
		u"GREGOR CZAYKOWSK", 
		36,
		u"http://www.loadingartist.com/comic/born/"
	),

	Sarjakuva(
		u"Channelate", 
		u"channelate",
		u"http://www.channelate.com/", 
		u"Ryan Hudson", 
		11,
		u"http://www.channelate.com/2008/02/13/wear-a-clean-shirt/"
	),

	Sarjakuva(
		u"Saturday Morning Breakfast Cereal", 
		u"smbc",
		u"http://www.smbc-comics.com/", 
		u"Zach Weiner", 
		37,
		u"http://www.smbc-comics.com/index.php?id=3768"
	),

	Sarjakuva(
		u"Its the Tie", 
		u"itsthetie",
		u"http://itsthetie.com/", 
		u"ItstheTie", 
		38,
		u"http://itsthetie.com/?comic=no-world-for-a-squirrel-4"
	),

	Sarjakuva(
		u"Awkward Zombie", 
		u"awkwardzombie",
		u"http://www.awkwardzombie.com/", 
		u"Katie Tiedrich", 
		39,
		u"http://www.awkwardzombie.com/index.php?page=0&comic=092006"
	),

	Sarjakuva(
		u"Power Nap", 
		u"powernap",
		u"http://www.powernapcomic.com/", 
		u"Maritza Campos + Bachan", 
		40,
		u"http://www.powernapcomic.com/d/20110617.html"
	),

	Sarjakuva(
		u"Extra Life", 
		u"extralife",
		u"http://www.myextralife.com/", 
		u"Scott Johnson", 
		41,
		u"http://www.myextralife.com/comic/06172001/"
	),




]
# sarjikset
for i in coms:
	db.session.add(i)

db.session.commit()