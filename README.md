Plugins for the python3 version of cloudbot https://github.com/CloudBotIRC/CloudBot

title.py: scrapes webpage titles and relays to channel (has basic carriage return/linefeed removal for titles as well, can be expanded)

twitch.py: when a twitch channel is linked in chat, it pulls basic data from twitch's API (needs no keys to work) and relays to the channel

comic.py: Weedbot's implementation of comic scripts, needs API keys in config.json file in cloudbot's top directory

evestatus.py: Scrapes Eve Online's public API for the Tranquility server and displays online status as well as player count (WIP, current uses cron job downloaded versions)

bitcoin.py: Scrapes bitstamp's API for current/high/low

agdq.py: Has a command similar to normal twitch parsing from twitch.py; also has a schedule function that compares against the online schedule page at www.gamesdonequick.com

fml.py: Scrapes www.fmylife.com/random (I didn't bother getting API access)
