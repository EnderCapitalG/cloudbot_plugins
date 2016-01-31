#Made for cloudbot
#Created by ender.capitalg@gmail.com

from cloudbot import hook
from lxml import etree
from urllib.request import urlopen
from urllib.error import HTTPError
import time

#basic spam protection
lastURL = ''

def titlep(url):
	global lastURL
	if url is "failed":
		return
	if url in lastURL:
		return
	lastURL = url
	parser = etree.HTMLParser(remove_blank_text=True)
	with urlopen(url) as f:
		tree = etree.parse(f, parser)
	tree = tree.getroot()
	#apparently the tree can return nonetype as well?
	if tree is None:
		return
	title = tree.find("head/title")
	#check for NoneType, discard if so
	if title is None:
		return
	temp = title.text.replace('\n', ' ').replace('\r', ' ')
	return temp

#basically to stop reddit from kicking an error back
def resolve_redir(url):
	try:
		return urlopen(url).geturl()
	except HTTPError as e:
		if e.code == 429:
			time.sleep(3);
			return resolve_redir(url)
		elif e.code < 600 or e.code > 300:
			print("Titlec: url %s failed with code: %i" % (url, e.code))
			return "failed"
		raise

@hook.regex(r'http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+')
def titlec(match, nick):
	matchtext = match.group(0).lower()
	if 'SHODAN' in nick or 'Steve' in nick or 'TBot' in nick or 'ZyklonB' in nick:
		return
	if 'twitch.tv' in matchtext:
		return
	elif 'youtube.com' in matchtext or 'youtu.be' in matchtext:
		return
	elif 'twitter.com' in matchtext or 'https://t.co' in matchtext:
		return
	return titlep(resolve_redir(matchtext))
