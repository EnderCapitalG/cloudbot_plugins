#Made for cloudbot
#Taken from homero cloudbot plugins, updated and some parts fixed 
#(the original was far from working correctly, at least for me)

from cloudbot import hook
import json
import requests

import lxml.html
from datetime import datetime, timedelta
import time

schedule = []
current_game = ''
epoch = 0

@hook.command('sgdq')
@hook.command('agdq')
def agdq():
	url = "https://api.twitch.tv/kraken/streams/gamesdonequick"
	obj = requests.get(url).json()
	if obj['stream'] is None:
		return "Stream is OFFLINE."

	stream = "Twitch Streamer: gamesdonequick" + " -=- Status: Online -=- Game: " + obj['stream']['game'] + " -=- Title: " + obj['stream']['channel']['status'] + " -=- Viewers: " + str(obj['stream']['viewers'])
	return stream + " Watch LIVE: http://www.twitch.tv/gamesdonequick"

@hook.command('parse')
def parse_agdq_schedule():
	global schedule, current_game
	obj = requests.get("https://api.twitch.tv/kraken/streams/gamesdonequick").json()
	current_game = obj['stream']['game']

	h_t = requests.get("https://gamesdonequick.com/schedule").text
	html = lxml.html.fromstring(h_t)
	table = html.xpath("//tbody[@id='runTable']//tr[not(contains(@id, 'daySplit'))]")	

	gs = []
	for element in table:
		#set timedelta to your timezone relative to UTC
		gtime = datetime.strptime(element.getchildren()[0].text, '%Y-%m-%dT%H:%M:%SZ') - timedelta(hours=5)
		gtime = time.mktime(gtime.timetuple())
		game = element.getchildren()[1].text
		gs.append([gtime, game])

	schedule = gs
	global epoch
	print("Updating AGDQ schedule.")

@hook.command('schedule')
def sched():
	global schedule, current_game, epoch
	#update game for comparison later
	obj = requests.get("https://api.twitch.tv/kraken/streams/gamesdonequick").json()
	current_game = obj['stream']['game']

	#used to reparse the schedule in case of game overruns/short runs (1hr)
	curtime = time.time()
	timediff = curtime - epoch
	if not schedule or timediff > 3600:
		parse_agdq_schedule()
		epoch = curtime
	current = None
	game = schedule[0][1]
	for i, (tm, gm) in enumerate(schedule[1:]):
		if current_game is gm:
			current = gm
			game = schedule[i+2][1]
			return 'AGDQ Currently Playing: {} | Up Next: {}'.format(current, game)
		game = gm

	#game didn't match, find game via time
	now = time.time()
	for i, (tm, gm) in enumerate(schedule[1:]):
		if tm > now:
			current = schedule[i][1]
			game = gm
			return 'AGDQ Currently Playing: {} | Up Next: {}'.format(current, game)

