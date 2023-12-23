import schedule
from googleapiclient.discovery import build
from __main__ import notification

#Youtube API
youtube_apikey = "<apikey>"
youtube_id='<youtube id channel>'
subs = 0

def check_yt_sub():
    global subs
    print("Check Subs ... ")
    # Create YouTube Object
    youtube = build('youtube', 'v3', 
                developerKey=youtube_apikey)
    ch_request = youtube.channels().list(
    part='statistics',
    id=youtube_id)
    # Channel Information
    ch_response = ch_request.execute()
    sub = int(ch_response['items'][0]['statistics']['subscriberCount'])

    if (subs != 0):        
        if (sub > subs):
            val = sub - subs
            obj = {"icon": { "x": 2, "y": 10, "value": "youtube" }, "message": { "x": 10, "y": 12, "value": " +" + str(val)}, "remaining_time": 10 }
            print(notification(myObj=obj))
        elif ( sub < subs):
            val = subs - sub
            obj = {"icon": { "x": 2, "y": 10, "value": "youtube" }, "message": { "x": 10, "y": 12, "value": " -" + str(val)}, "remaining_time": 10 }
            print(notification(myObj=obj))
    subs = sub    
    
def get_yt_subs():
    # Create YouTube Object
    youtube = build('youtube', 'v3', 
                developerKey=youtube_apikey)
    ch_request = youtube.channels().list(
    part='statistics',
    id=youtube_id)
  
    # Channel Information
    ch_response = ch_request.execute()
    sub = ch_response['items'][0]['statistics']['subscriberCount']
    subs = sub

    obj = {"icon": { "x": 2, "y": 10, "value": "youtube" }, "message": { "x": 10, "y": 12, "value": " " + sub + " Subs"}, "remaining_time": 10 }

    print("Get YT Subs ... " + notification(myObj=obj))

def main():
    schedule.every(20).minutes.do(get_yt_subs)
    schedule.every(15).minutes.do(check_yt_sub)
#    schedule.every(5).seconds.do(get_yt_subs)
#    schedule.every(10).seconds.do(check_yt_sub)
