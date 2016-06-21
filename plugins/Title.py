#Made for cloudbot
#Created by ender.capitalg@gmail.com

import requests
from lxml.html import fromstring
from cloudbot import hook

#basic spam protection
lastURL = ''

header = { 'User-Agent' : 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/48.0.2564.97 Safari/537.36' }

@hook.regex(r'http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+')
def titlec(match, nick):
	global lastURL, header
	matchtext = match.group(0).lower()
	#example filters, handled by other plugins
	if 'twitch.tv' in matchtext or 'zkillboard' in matchtext:
		return
	
	#to discard pictures
	picture = matchtext.rsplit('.',1)[-1]
	if 'jpg' in picture or 'png' in picture or 'gif' in picture or 'webm' in picture:
		return

	if matchtext in lastURL:
		return
	req = requests.get(match.group(0), headers=header)
	tree = fromstring(req.content)
	title = tree.findtext('.//title')
	#there exist sites that literally have newlines in their titles because reasons; now also removes leading spaces, since sites like imgur's albums insert about 30???
	title = title.replace('\n', '').replace('\r', '').lstrip(' ')
	return title
