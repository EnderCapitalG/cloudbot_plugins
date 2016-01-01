#Made for cloudbot
#Created by ender.capitalg@gmail.com

from cloudbot import hook
from lxml import etree

@hook.command('tq')
@hook.command('eve')
@hook.command('evestatus')
def evestatus():
	tree = etree.parse("data/ServerStatus.xml")

	if tree.find("result/serverOpen").text == "True":
        	online = "Online"
	else:
		pr = "Server status: Offline."
		return pr

	players = tree.find("result/onlinePlayers")
	pr = "Server status: " + online + "." " Players online: " + players.text
	return pr
