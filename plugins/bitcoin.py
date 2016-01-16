#Made for cloudbot
#Created by ender.capitalg@gmail.com
from cloudbot import hook
import json
import requests

def get_bitcoin():
  data = requests.get("https://www.bitstamp.net/api/ticker/").json()
  t = {
    'low':  float(data['low']),
    'high': float(data['high']),
    'last':  float(data['last']),
  }
  return t

@hook.command('bit')
def bitcoin():
    t = get_bitcoin()
    msg = "Current: " + str(t['last']) + " - 24h High: " + str(t['high']) + " - 24h Low: " + str(t['low'])
    return msg
