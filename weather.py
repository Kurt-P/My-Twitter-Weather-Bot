#!/usr/bin/python

## The idea for this script was to run it on a Debian/Ubuntu server or desktop
## environment. There are some apps you will most likely need to install for 
## this scripty to work properly. First is easy_setup, which you will
## use to install pip. Then with pip you will need to install twython and
## feedparser. See http://z.umn.edu/l8a (Ubuntu) for more info.

from sys import argv
from twython import Twython ## Connect to Twitter ## NEEDED ## Install with pip
import commands ## Call system commands ## If needed
import logging ## Log errors and success
import feedparser ## Get an RSS feed and parse it ## NEEDED ## Install with pip
import re ## Parse the RSS data with a regular expression

CONSUMER_KEY = ''
CONSUMER_SECRET = ''
ACCESS_KEY = ''
ACCESS_SECRET = ''

## Setup the api object
api = Twython(CONSUMER_KEY, CONSUMER_SECRET, ACCESS_KEY, ACCESS_SECRET)

## Logging DEBUG
logging.basicConfig(filename='umc-weather.log', level=logging.DEBUG)

## Use Yahoo! weather RSS feed to get the weather
## SEE: https://developer.yahoo.com/weather/#request ## Yahoo! API
## SEE: http://woeid.rosselliot.co.nz/ ## WOEID lookup

## Setup the RSS sting
url = 'http://weather.yahooapis.com/forecastrss?w='
woeid = '12782656' ## This will need to be edited to get different locations
rss = url + woeid ## The resulting RSS URL
logging.info(rss) ## Doesn't hurn to log it
data = feedparser.parse(rss)

## Now we parse the data from the RSS to get the current temp
summary = data.entries[0].summary ## Get just the summary
temp = re.split(r'\n',re.sub('<.+?>','',summary)) ## Break the summary down
logging.info(temp)
temp = int(re.findall('[0-9]+',temp[2])[0]) ## Get the current temp
logging.info(temp)

line = 'The current temp is %d' % temp
logging.debug(line)

## Tweet it!
try: ## I don't actually know if this try/catch block will work
    api.update_status(status = line)
    logging.info("Succuss!")
except:
    logging.warn("failed")


## Test
#print data['feed']['title']
#print line
