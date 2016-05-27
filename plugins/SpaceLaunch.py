#Made for cloudbot
#Created by ender.capitalg@gmail.com

from cloudbot import hook
import requests

@hook.command('nextlaunch')
def nextlaunch():
	obj = requests.get("https://launchlibrary.net/1.2/launch/next/1").json()

	name = obj['launches'][0]['name']
	windowstart = obj['launches'][0]['windowstart']
	windowend = obj['launches'][0]['windowend']
	pad = obj['launches'][0]['location']['name']
	probability = str(obj['launches'][0]['probability'])


	ret = "Next Launch: " + name + ". Window start: " + windowstart + " Window end: " + windowend + " -- Launching from: " + pad + ". Launch probability: " + probability + "%."

	return ret

@hook.command('launchurls')
@hook.command('launchvid')
def launchurls():
	obj = requests.get("https://launchlibrary.net/1.2/launch/next/1").json()
	
	url = ''

	for item in obj['launches'][0]['vidURLs']:
		url += item + " "

	return url
