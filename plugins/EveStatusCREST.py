#Made for cloudbot
#Created by ender.capitalg@gmail.com

from cloudbot import hook
import requests

@hook.command("eve")
@hook.command("evestatus")
@hook.command("tq")
def tqstatus():
	url_tq = "https://crest-tq.eveonline.com/"
	json = requests.get(url_tq).json()
	if json is None:
		return "Tranquility server status: Offline."

	status = json["serviceStatus"]
	if "online" in status:
		players = json["userCount_str"]
		return "Tranquility server status: Online. Players online: " + players
	
	return "Tranqulity server status: Offline."

@hook.command("sisi")
@hook.command("singularity")
def sisistatus():
	url_tq = "http://crest-sisi.testeveonline.com/"
	json = requests.get(url_tq).json()
	if json is None:
		return "Singularity server status: Offline."

	status = json["serviceStatus"]["eve"]
	if "online" in status:
		players = json["userCounts"]["eve_str"]
		return "Singularity server status: Online. Players online: " + players
	
	return "Singularity server status: Offline."
