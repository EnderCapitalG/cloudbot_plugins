#Made for cloudbot
#Created by ender.capitalg@gmail.com

from cloudbot import hook
import json
import requests

oauth_token = ""

def twitchp(url):
	global oauth_token
	url_t = "https://api.twitch.tv/kraken/streams/" + url + "?oauth_token=" + oauth_token
	obj = requests.get(url_t).json()
	if obj['stream'] is None:
		return "Streamer " + url + " is OFFLINE."
	stream = "Twitch Streamer: " + url + " -=- Status: Online -=- Game: " + obj['stream']['game'] + " -=- Title: " + obj['stream']['channel']['status'] + " -=- Viewers: " + str(obj['stream']['viewers'])

	return stream

@hook.regex(r'(.*:)//(twitch.tv|www.twitch.tv)(:[0-9]+)?(.*)')
def twitch_regex(match, nick):
	matchtext = match.group(0).lower()
	url = matchtext.rsplit('/', 1)[-1]
	return twitchp(url)
