#Made for cloudbot
#Created by ender.capitalg@gmail.com

from cloudbot import hook
from lxml import etree
from urllib.request import urlopen
from urllib.error import HTTPError
import time

def titlep(url):
	parser = etree.HTMLParser(remove_blank_text=True)
	with urlopen(url) as f:
		tree = etree.parse(f, parser)

	title = tree.find("head/title")
	temp = title.text.replace('\n', ' ').replace('\r', ' ')
	return temp

#basically to stop reddit from kicking an error back
def resolve_redir(url):
	try:
		return urlopen(url).geturl()
	except HTTPError as e:
		if e.code == 429:
			time.sleep(4);
			return resolve_redir(url)
		raise

@hook.regex(r'http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+')
def titlec(match, nick):
	matchtext = match.group(0).lower()
	#easy example of a filter (also keeps from clashing with twitch.py)
	if 'twitch.tv' in matchtext:
		return
	return titlep(resolve_redir(matchtext))
