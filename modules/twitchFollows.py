import schedule
import twitch
import pytz
from datetime import datetime, date
import time
import sys
from __main__ import notification

# Twitch API 
client_id = '<id>'
client_secret = '<secret>'
channel = 'locopol'

def check_twitch_follows():
    counts = 0
    helix = twitch.Helix(client_id, client_secret)
    followers = helix.user(channel).followers()

    for x in followers:
        counts = counts + 1

    obj = {"icon": { "x": 2, "y": 10, "value": "twitch" }, "message": { "x": 10, "y": 9, "value": " Follows:  " +  str(counts) }, "remaining_time": 10 }

    print("Get Twitch Follows ..." +  notification(myObj=obj))
    
def main():
    schedule.every(60).minutes.do(check_twitch_follows)
#    schedule.every(10).seconds.do(check_twitch_follows)
