#Made for cloudbot
#Created by ender.capitalg@gmail.com

from cloudbot import hook
import requests
import lxml.html

textTable = []
htmlTable = []

def build_table():
	global textTable, htmlTable
	req = requests.get("http://kiranico.com/en/mhx/item").text
	html = lxml.html.fromstring(req)
	tt = html.xpath("//div[@class='col-lg-2 col-xs-6']/p/a/text()")
	htmlTable = html.xpath("//div[@class='col-lg-2 col-xs-6']/p/a/@href")

	for elem in tt:
		textTable.append(elem.lower())

@hook.command('mhx')
def MHX_Item(text):
	global textTable
	if not textTable:
		build_table()

	i = 0

	for elem in textTable:
		if text.lower() in elem:
			return htmlTable[i]
		i += 1

	#if we got here, no match
	return "No item found."
