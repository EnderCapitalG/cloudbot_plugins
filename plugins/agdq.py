#Made for cloudbot
#Created by ender.capitalg@gmail.com

from cloudbot import hook
import requests

import lxml.html
from datetime import datetime, timedelta
import time
import arrow

schedule = []
current_game = ''
epoch = 0

oauth_token = ""

@hook.command('sgdq')
@hook.command('agdq')
def agdq(nick, host):
	global oauth_token
	url = "https://api.twitch.tv/kraken/streams/gamesdonequick?oauth_token=" + oauth_token
	obj = requests.get(url).json()
	if obj['stream'] is None:
		return "Stream is OFFLINE."

	stream = "Twitch Streamer: gamesdonequick" + " -=- Status: Online -=- Game: " + obj['stream']['game'] + " -=- Title: " + obj['stream']['channel']['status'] + " -=- Viewers: " + str(obj['stream']['viewers'])
	return stream + " Watch LIVE: http://www.twitch.tv/gamesdonequick"

def parse_agdq_schedule():
	global schedule, current_game, oauth_token
	obj = requests.get("https://api.twitch.tv/kraken/streams/gamesdonequick?oauth_token=" + oauth_token).json()
	current_game = obj['stream']['game']

	h_t = requests.get("https://gamesdonequick.com/schedule").text
	html = lxml.html.fromstring(h_t)
	table = html.xpath("//table[@id='runTable']//tbody//tr[not(contains(@class, 'second-row'))]")
	table = table

	gs = []
	for element in table:
		try:
			gtime = arrow.get(element.getchildren()[0].text)
		except arrow.parser.ParserError:
			continue
		game = element.getchildren()[1].text
		gs.append([gtime, game])

	schedule = gs
	print("Updating AGDQ schedule. ")

@hook.command('schedule')
def sched(nick, host, text, notice):
	global oauth_token
	global schedule, current_game, epoch
	#update game for comparison later
	obj = requests.get("https://api.twitch.tv/kraken/streams/gamesdonequick?oauth_token=" + oauth_token).json()
	try:
		current_game = obj['stream']['game']
	except TypeError as e:
		return "Stream offline."

	#used to reparse the schedule in case of game overruns/short runs (15min)
	curtime = arrow.utcnow()
	if epoch is 0:
		#force update
		timediff = 900
	else:
		timediff = (curtime - epoch).seconds
	if not schedule or timediff > 900:
		parse_agdq_schedule()
		epoch = curtime

	#if there's text following it, search in the game list and return time
	if text:
		for i, (tm, gm) in enumerate(schedule[1:]):
			if text.lower() in gm.lower():
				gtime = schedule[i+1][0].format('YYYY/M/D HH:mm:ss')
				now = arrow.utcnow()
				timetil = (schedule[i+1][0] - now).total_seconds()
				time = timetil / 3600
				hours = int(time)
				minutes = int((time*60) % 60)
				seconds = int((time*3600) % 60)
				
				return str(schedule[i+1][1]) + " " + str(gtime) + " UTC. Time until: " + "%d:%02d:%02d" % (hours, minutes, seconds)
			#checking this is hackish right now, not bothered fixing (yet)
			if i+2 is len(schedule):
				notice("Game not found")
				return

	current = None
	game = schedule[0][1]
	for i, (tm, gm) in enumerate(schedule[1:]):
		if current_game is gm:
			current = gm
			game = schedule[i+2][1]
			return 'GDQ Currently Playing: {} | Up Next: {}'.format(current, game)
		game = gm

	#game didn't match, find game via time
	now = arrow.utcnow()
	for i, (tm, gm) in enumerate(schedule[1:]):
		if tm > now:
			current = schedule[i][1]
			game = gm
			return 'GDQ Currently Playing: {} | Up Next: {}'.format(current, game)

@hook.command('donations')
def agdq_donation(nick, host):
	h_t = requests.get("https://gamesdonequick.com/tracker/19").text
	html = lxml.html.fromstring(h_t)
	donation = html.xpath("//small")
	return "Games Done Quick" + donation[0].text.replace('\n', ' ').replace('\r', ' ').replace('\u2014', '-')
