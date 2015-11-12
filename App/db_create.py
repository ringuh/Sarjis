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

db.session.add(User(u"vieras", u"vieras"))
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
		u"http://wumo.com/", 
		u"Wumo", 
		64, # vaihda in future
		u"http://wumo.com/wumo/2015/09/08"
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

	Sarjakuva(
		u"Player vs. Player", 
		u"pvponline",
		u"http://www.pvponline.com/", 
		u"Scott R. Kurtz", 
		42,
		u"http://www.pvponline.com/comic/2015/06/01/birds-of-a-feather1"
	),

	Sarjakuva(
		u"Evil Inc.", 
		u"evilinc",
		u"http://evil-inc.com/", 
		u"Brad J. Guigar", 
		9,
		u"http://evil-inc.com/comic/santa-villain-poem-1/"
	),

	Sarjakuva(
		u"The Abominable", 
		u"abominable",
		u"http://abominable.cc/", 
		u"Charles Christopher", 
		43,
		u"http://abominable.cc/post/44164796353/episode-one"
	),

	Sarjakuva(
		u"Girls with Slingshots", 
		u"girlswithslingshots",
		u"http://www.girlswithslingshots.com/", 
		u"Danielle Corsetto", 
		37,
		u"http://www.girlswithslingshots.com/comic/gws-chaser-99/"
	),


	Sarjakuva(
			u"Lets Speak English", 
			u"letsspeakenglish",
			u"http://www.marycagle.com/", 
			u"Mary Cagle", 
			22,
			u"http://www.marycagle.com/letsspeakenglish/1-shingeki-no-kodomo"
		),

	Sarjakuva(
			u"Amazing Super Powers", 
			u"amazingsuperpowers",
			u"http://www.amazingsuperpowers.com/", 
			u"Wes & Tony", 
			11,
			u"http://www.amazingsuperpowers.com/2007/09/heredity/"
		),

	Sarjakuva(
			u"Zen Pencils", 
			u"zenpencils",
			u"http://zenpencils.com/", 
			u"Wes & Tony", 
			11,
			u"http://zenpencils.com/comic/1-ralph-waldo-emerson-make-them-cry/"
		),

	Sarjakuva(
			u"Last Place", 
			u"lastplace",
			u"http://lastplacecomics.com/", 
			u"LastPlace", 
			9,
			u"http://lastplacecomics.com/comic/wide-range-of-super-powers/"
		),

	Sarjakuva(
			u"Existential Comics", 
			u"existential",
			u"http://existentialcomics.com/", 
			u"unknown", 
			44,
			u"http://existentialcomics.com/comic/1"
		),

	Sarjakuva(
			u"Justice League 8", 
			u"jl8",
			u"http://jl8comic.tumblr.com/", 
			u"Yale Stewart", 
			45,
			u"http://jl8comic.tumblr.com/post/13372482444/jl8-1-by-yale-stewart-based-on-characters-in-dc"
		),

	Sarjakuva(
			u"Fowl Language", 
			u"fowllanguage",
			u"http://www.fowllanguagecomics.com/", 
			u"Brian Gordon", 
			9,
			u"http://www.fowllanguagecomics.com/comic/part-of-the-process/"
		),

	Sarjakuva(
			u"Over the Hedge", 
			u"overthehedge",
			u"http://www.gocomics.com/overthehedge/", 
			u"T Lewis and Michael Fry", 
			20,
			u"http://www.gocomics.com/overthehedge/2015/07/30"
		),

	Sarjakuva(
			u"User Friendly", 
			u"userfriendly",
			u"http://ars.userfriendly.org/", 
			u"J.D Frazer", 
			46,
			u"http://ars.userfriendly.org/cartoons/?id=20150731"
		),

	Sarjakuva(
		u"Karlsson", 
		u"karlsson",
		u"http://www.hs.fi/karlsson", 
		u"Karlsson", 
		2,
		u"http://www.hs.fi/karlsson/s1305951536460" 
	),

	Sarjakuva(
			u"Poorly Drawn Lines", 
			u"poorlydrawnlines",
			u"http://poorlydrawnlines.com/", 
			u"Reza Farazmand", 
			48,
			u"http://poorlydrawnlines.com/comic/campus-characters/"
		),

	Sarjakuva(
			u"xkcd", 
			u"xkcd",
			u"http://xkcd.com/", 
			u"Randall", 
			4,
			u"http://xkcd.com/1500/"
		),

	Sarjakuva(
			u"Menage a 3", 
			u"ma3",
			u"http://www.ma3comic.com/", 
			u"Giz / Dave Zero", 
			49,
			u"http://www.ma3comic.com/strips-ma3/for_new_readers"
		),
	Sarjakuva(
			u"Gone With the Blastwave", 
			u"blastwave",
			u"http://www.blastwave-comic.com/", 
			u"Kimmo Lemetti", 
			50,
			u"http://www.blastwave-comic.com/index.php?p=comic&nro=1"
		),

	Sarjakuva(
			u"The Rock Cocks", 
			u"rockcocks",
			u"http://www.therockcocks.com/", 
			u"Unknown", 
			22,
			u"http://www.therockcocks.com/comic/page-1"
		),

	

	Sarjakuva(
			u"The Noob", 
			u"noob",
			u"http://thenoobcomic.com/", 
			u"Gianna", 
			11,
			u"http://thenoobcomic.com/comic/1/"
		),

	Sarjakuva(
			u"Looking For Group", 
			u"lfg",
			u"http://www.lfg.co/", 
			u"Ryan Sohmer and Lar Desouza", 
			9,
			u"http://www.lfg.co/page/1/"
		),

	Sarjakuva(
			u"Non-Player Character", 
			u"npc",
			u"http://www.lfg.co/", 
			u"Ryan Sohmer and Lar Desouza", 
			9,
			u"http://www.lfg.co/npc/tale/1-1/"
		),

	Sarjakuva(
			u"Tiny Dick Adventures", 
			u"tinydickadventures",
			u"http://www.lfg.co/", 
			u"Ryan Sohmer and Lar Desouza", 
			9,
			u"http://www.lfg.co/tda/strip/1/"
		),

	Sarjakuva(
			u"Dark Legacy", 
			u"darklegacy",
			u"http://www.darklegacycomics.com/", 
			u"Arad Kedar", 
			52,
			u"http://www.darklegacycomics.com/1"
		),

	Sarjakuva(
			u"Stand Still Stay Silent", 
			u"standstillstaysilent",
			u"http://www.sssscomic.com/", 
			u"Minna Sundberg", 
			51,
			u"http://www.sssscomic.com/comic.php?page=1"
		),

	Sarjakuva(
			u"Completely Normal People", 
			u"completelynormal",
			u"http://completelynormalpeople.com/", 
			u"Unknown", 
			53,
			u"http://completelynormalpeople.com/images/toons/"
		),

	Sarjakuva(
			u"Safely Endangered", 
			u"safelyendangered",
			u"http://www.safelyendangered.com/", 
			u"Chris", 
			11,
			u"http://www.safelyendangered.com/comic/ignored/"
		),

	Sarjakuva(
			u"Nedroid", 
			u"nedroid",
			u"http://nedroid.com/", 
			u"Unknown", 
			4,
			u"http://nedroid.com/2015/04/gobs/"
		),

	Sarjakuva(
			u"Romantically Apocalyptic", 
			u"romanticallyapocalyptic",
			u"http://romanticallyapocalyptic.com/", 
			u"Unknown", 
			54,
			u"http://romanticallyapocalyptic.com/0"
		),

	Sarjakuva(
			u"The Fox Sisters", 
			u"foxsisters",
			u"http://www.thefoxsister.com/", 
			u"Unknown", 
			9,
			u"http://www.thefoxsister.com/index.php?id=1"
		),

	Sarjakuva(
			u"The Odd 1s Out", 
			u"theodd1sout",
			u"http://theodd1sout.com/", 
			u"Unknown", 
			9,
			u"http://theodd1sout.com/comic/god-its-awful/"
		),

	Sarjakuva(
			u"Berds and Nerds", 
			u"berdsandnerds",
			u"http://berdsandnerds.com/", 
			u"Unknown", 
			55,
			u"http://berdsandnerds.com/thearchive/"
		),

	Sarjakuva(
			u"FoxTrot", 
			u"foxtrot",
			u"http://www.foxtrot.com/", 
			u"Bill Amend", 
			56,
			u"http://www.foxtrot.com/2015/08/16/no-worries/"
		),

	Sarjakuva(
			u"Sunny Street", 
			u"sunnystreet",
			u"http://www.gocomics.com/sunny-street/", 
			u"Max Garcia and Sandra Barthauer", 
			20,
			u"http://www.gocomics.com/sunny-street/2013/06/03"
		),

	Sarjakuva(
			u"Exploding Dinosaur", 
			u"explodingdinosaur",
			u"http://explodingdinosaur.com/", 
			u"Josh Walthall", 
			11,
			u"http://explodingdinosaur.com/comic/seriously-stop-it/"
		),

	Sarjakuva(
			u"Things In Squares", 
			u"thingsinsquares",
			u"http://www.thingsinsquares.com/", 
			u"Unknown", 
			57,
			u"http://www.thingsinsquares.com/comics/lame-joke/"
		),

	Sarjakuva(
			u"Down the Upward Spiral", 
			u"downtheupwardspiral",
			u"http://www.downtheupwardspiral.com/", 
			u"Corey Giacco", 
			58,
			u"http://www.downtheupwardspiral.com/gallery.html"
		),

	Sarjakuva(
			u"Strong Female Protagonist", 
			u"strongfemaleprotagonist",
			u"http://strongfemaleprotagonist.com/", 
			u"unknown", 
			38,
			u"http://strongfemaleprotagonist.com/issue-1/page-0/"
		),

	Sarjakuva(
			u"Vattu", 
			u"vattu",
			u"http://www.rice-boy.com/vattu/", 
			u"unknown", 
			59,
			u"http://www.rice-boy.com/vattu/index.php?c=001"
		),

	Sarjakuva(
			u"nellucnhoj", 
			u"nellucnhoj",
			u"http://nellucnhoj.com/", 
			u"unknown", 
			45,
			u"http://nellucnhoj.com/post/72259187580/back-in-2010-i-decided-to-punish-myself-by-doing"
		),

	Sarjakuva(
		u"Jim Benton", 
		u"jimbenton",
		u"http://www.gocomics.com/jim-benton-cartoons/", 
		u"Jim Benton", 
		20, # vaihda in future
		u"http://www.gocomics.com/jim-benton-cartoons/2014/10/27",
	),

	Sarjakuva(
		u"Veritable Hokum", 
		u"veritablehokum",
		u"http://www.veritablehokum.com/", 
		u"Korwin Briggs", 
		11,
		u"http://www.veritablehokum.com/comic/headless-folks-of-the-french-revolution/",
	),

	Sarjakuva(
		u"Hijinks Ensue", 
		u"hijinksensue",
		u"http://hijinksensue.com/", 
		u"Joel Watson", 
		11,
		u"http://hijinksensue.com/comic/who-is-your-daddy-and-what-does-he-do/",
	),


	Sarjakuva(
		u"Sharksplode", 
		u"sharksplode",
		u"http://sharksplode.com/", 
		u"Joel Watson", 
		11,
		u"http://sharksplode.com/comic/is-it-the-word-is-it-really/",
	),

	Sarjakuva(
		u"Grog", 
		u"grog",
		u"http://www.grogcomics.com/", 
		u"Joel Watson", 
		60,
		u"http://www.grogcomics.com/post/31903734556/my-first-posted-comic",
	),

	Sarjakuva(
		u"Legacy Control", 
		u"legacy-control",
		u"http://legacy-control.com/", 
		u"Javis Ray", 
		11,
		u"http://legacy-control.com/comic/advent-boner-3/",
	),
	Sarjakuva(
		u"The Adventures of Businesscat", 
		u"businesscat",
		u"http://www.businesscat.happyjar.com/", 
		u"Javis Ray", 
		11,
		u"http://www.businesscat.happyjar.com/comic/coffee/",
	),

	Sarjakuva(
		u"Hejibits", 
		u"hejibits",
		u"http://www.hejibits.com/", 
		u"John", 
		11,
		u"http://www.hejibits.com/comics/roommate-comics-1/"
	),

	Sarjakuva(
		u"Dire Circumstances", 
		u"dire",
		u"http://fruitscs.tumblr.com/", 
		u"Jasper Huang", 
		45,
		u"http://fruitscs.tumblr.com/post/117225884584"
	),

	Sarjakuva(
		u"Dorkly", 
		u"dorkly",
		u"http://www.dorkly.com/", 
		u"Unknown", 
		61,
		u"http://www.dorkly.com/post/1419/why-you-should-only-use-round-pokemon?ref=comics",
	),

	Sarjakuva(
		u"Tubey toons", 
		u"tubey",
		u"http://tubeytoons.com/", 
		u"Tubey", 
		62,
		u"http://tubeytoons.com/comic/stay-put",
	),

	Sarjakuva(
		u"The Awkward Yeti", 
		u"awkwardyeti",
		u"http://theawkwardyeti.com/", 
		u"Nick Seluk", 
		11,
		u"http://theawkwardyeti.com/comic/0912-reading/",
	),

	Sarjakuva(
		u"Big Foot Justice", 
		u"bigfootjustice",
		u"http://bigfootjustice.com/", 
		u"Mike Salcedo", 
		11,
		u"http://bigfootjustice.com/comic/iscale-2/",
	),

	Sarjakuva(
		u"Nerd Rage", 
		u"nerdrage",
		u"http://nerdragecomic.com/", 
		u"Unknown", 
		63,
		u"http://nerdragecomic.com/index.php?date=2010-09-28",
	),

	Sarjakuva(
		u"Whomp", 
		u"whomp",
		u"http://www.whompcomic.com/", 
		u"Unknown", 
		22,
		u"http://www.whompcomic.com/comic/06152010",
	),


	Sarjakuva(
		u"Commit Strip", 
		u"commitstrip",
		u"http://www.commitstrip.com/", 
		u"ItstheTie", 
		38,
		u"http://www.commitstrip.com/en/2012/02/22/interview/"
	),

	# Sarjakuva(
	# 		u"Death Bulge", 
	# 		u"deathbulge",
	# 		u"http://deathbulge.com/", 
	# 		u"Rory", 
	# 		47,
	# 		u"http://deathbulge.com/comics/1"
	# 	),
	
]
# sarjikset
for i in coms:
	db.session.add(i)

db.session.commit()