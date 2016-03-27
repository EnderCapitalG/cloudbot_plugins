from cloudbot import hook
import requests
import lxml.html

def pullkill(url):
	req = requests.get(url).text
	html = lxml.html.fromstring(req)
	desc = html.xpath("//meta[@name='twitter:description']/@content")
	return desc[0]

@hook.regex(r'(.*:)//(zkillboard.com|www.zkillboard.com)(:[0-9]+)?(.*)')
def zkb(match):
	return pullkill(match.group(0).lower())
