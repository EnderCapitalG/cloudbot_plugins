#Made for cloudbot
#Created by ender.capitalg@gmail.com

from cloudbot import hook
from lxml import etree
import arrow
import requests

tqcache = 0
sisicache = 0
tqtree = ''
sisitree = ''

@hook.command('tq')
@hook.command('eve')
@hook.command('evestatus')
def evestatus():
	global tqcache, tqtree
	now = arrow.utcnow()
	if tqcache is 0 or now > tqcache:
		url_tq = requests.get("https://api.eveonline.com/server/ServerStatus.xml.aspx")
		tree = etree.fromstring(url_tq.content)
		tqcache = arrow.get(tree.find("cachedUntil").text)
		tqtree = tree
		print("Parsing TQ server status. Seconds until cache:", (tqcache - now).seconds)

	if tqtree.find("result/serverOpen").text == "True":
        	online = "Online"
	else:
		pr = "Tranquility server status: Offline."
		return pr

	players = tqtree.find("result/onlinePlayers")
	pr = "Tranquility server status: " + online + "." " Players online: " + players.text
	return pr


@hook.command('sisi')
def sisistatus():
	global sisicache, sisitree
	now = arrow.utcnow()
	if sisicache is 0 or now > sisicache:
		url_si = requests.get("https://api.testeveonline.com/server/ServerStatus.xml.aspx")
		tree = etree.fromstring(url_si.content)
		sisicache = arrow.get(tree.find("cachedUntil").text)
		sisitree = tree
		print("Parsing SiSi server status. Seconds until cache:", (sisicache - now).seconds)

	if tree.find("result/serverOpen").text == "True":
        	online = "Online"
	else:
		pr = "Singularity server status: Offline."
		return pr

	players = tree.find("result/onlinePlayers")
	pr = "Singularity server status: " + online + "." " Players online: " + players.text
	return pr

