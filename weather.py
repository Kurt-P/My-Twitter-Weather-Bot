#!/usr/bin/python

from sys import argv
from twython import Twython
import commands
import logging

CONSUMER_KEY = ''
CONSUMER_SECRET = ''
ACCESS_KEY = ''
ACCESS_SECRET = ''

# Setup the api object
api = Twython(CONSUMER_KEY, CONSUMER_SECRET, ACCESS_KEY, ACCESS_SECRET)

# Logging DEBUG
logging.basicConfig(filename='umc-weather.log', level=logging.DEBUG)


## TODO ##
# Need to add logic into the script to get data from some sort of RSS
# feed to pipe that to the status. 
