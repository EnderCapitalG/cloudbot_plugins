Plugins for the python3 version of cloudbot https://github.com/CloudBotIRC/CloudBot

title.py: scrapes webpage titles and relays to channel (has basic carriage return/linefeed removal for titles as well, can be expanded)

twitch.py: when a twitch channel is linked in chat, it pulls basic data from twitch's API (now needs a key to work) and relays to the channel

comic.py: Weedbot's implementation of comic scripts, needs API keys in config.json file in cloudbot's top directory

evestatus.py: deperecated version of the new EveStatusCREST.py script (used xml and caches)

EveStatusCREST.py: uses CCP's CREST API to pull server status

bitcoin.py: Scrapes bitstamp's API for current/high/low

agdq.py: Has a command similar to normal twitch parsing from twitch.py; also has a schedule function that compares against the online schedule page at www.gamesdonequick.com -- Don't forget to add your API key

fml.py: Scrapes www.fmylife.com/random (I didn't bother getting API access)

SpaceLaunch.py: has commands for both the next upcoming space launch and also to output the video URLs where the launch may be viewed. API from https://launchlibrary.net

runescape.py: Started out as a joke to compare to Eve online player count, went ahead and included it :v
