#Made for cloudbot
#Created by ender.capitalg@gmail.com

from cloudbot import hook

import requests
import re

@hook.command('runescape')
@hook.command('rune')
@hook.command('rs')
def runescape():
	url_us = requests.get("http://www.runescape.com/player_count.js?varname=iPlayerCount&callback=jQuery000000000000000_0000000000&_=0")
	s = "u'" + url_us.text + "'"
	online = re.search('\((.*?)\)', s).group(1)
	return "Runescape players online: " + online
