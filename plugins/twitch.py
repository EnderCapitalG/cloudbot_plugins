#Made for cloudbot
#Created by ender.capitalg@gmail.com

from cloudbot import hook
import json
import requests

def twitchp(url):
	url_t = "https://api.twitch.tv/kraken/streams/" + url
	obj = requests.get(url_t).json()
	if obj['stream'] is None:
		return "Streamer " + url + " is OFFLINE."
	stream = "Twitch Streamer: " + url + " -=- Status: Online -=- Game: " + obj['stream']['game'] + " -=- Title: " + obj['stream']['channel']['status'] + " -=- Viewers: " + str(obj['stream']['viewers'])

	return stream

@hook.regex(r'http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+')
def twitch_regex(match, nick):
	matchtext = match.group(0).lower()
	if 'twitch.tv' in matchtext:
		url = matchtext.rsplit('/', 1)[-1]
		return twitchp(url)
