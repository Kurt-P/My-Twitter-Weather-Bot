#!/usr/bin/python

from sys import argv
from twython import Twython ## Connect to Twitter ## NEEDED ## Install with pip
import commands ## Call system commands ## If needed
import logging ## Log errors and success
import feedparser ## Get an RSS feed and parse it ## NEEDED ## Install with pip

CONSUMER_KEY = ''
CONSUMER_SECRET = ''
ACCESS_KEY = ''
ACCESS_SECRET = ''

# Setup the api object
api = Twython(CONSUMER_KEY, CONSUMER_SECRET, ACCESS_KEY, ACCESS_SECRET)

# Logging DEBUG
logging.basicConfig(filename='umc-weather.log', level=logging.DEBUG)

# Use Yahoo! weather RSS feed to get the weather
## SEE: https://developer.yahoo.com/weather/#request ## Yahoo! API
## SEE: http://woeid.rosselliot.co.nz/ ## WOEID lookup
## TODO ## Use two strings to hold the URL and the WOEID info.
location = feedparser.parse('http://weather.yahooapis.com/forecastrss?w=12782656')

## Test
print location['feed']['title']

## TODO ##
# Need to add logic into the script to get data from some sort of RSS
# feed to pipe that to the status. 

## SEE: http://www.tuxradar.com/content/code-project-use-weather-wallpapers ##
