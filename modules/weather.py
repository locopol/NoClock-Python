import urllib.request
import urllib3, json, schedule
from __main__ import notification

#AccuWeather API
accuwtr_apikey = "<apikey>"
weather_countrycode = "CL"
weather_city = "Santiago"

def get_weather():  
    search_address="http://dataservice.accuweather.com/locations/v1/cities/"+weather_countrycode+"/search?apikey="+accuwtr_apikey+"&q="+weather_city+"&details=true"
    with urllib.request.urlopen(search_address) as search_address:
        data=json.loads(search_address.read().decode())
        location_key=data[0]['Key']
    daily_forecastURL="http://dataservice.accuweather.com/currentconditions/v1/"+location_key+"?apikey=" + accuwtr_apikey + '&language=es&metric=true'
    with urllib.request.urlopen(daily_forecastURL) as daily_forecastURL:
        data=json.loads(daily_forecastURL.read().decode())
        for key1 in data:
                if (len(str(key1['WeatherText'])) in range(0, 10)):
                    data = ['  ' + str(key1['Temperature']['Metric']['Value']) + "\u00b0" + str(key1['Temperature']['Metric']['Unit']) + "   " + str(key1['WeatherText']), key1['WeatherIcon']]
                    x_icon = 2
                    y_msg = 9
                else:
                    data = ['  ' + str(key1['Temperature']['Metric']['Value']) + "\u00b0" + str(key1['Temperature']['Metric']['Unit']) + "  " + str(key1['WeatherText']), key1['WeatherIcon']]
                    x_icon = 0
                    y_msg = 7

#            data = ["  " + str(key1['Temperature']['Metric']['Value']) + "\u00b0" + str(key1['Temperature']['Metric']['Unit']) + "  " + str(key1['WeatherText']), key1['WeatherIcon']]
#    data1 = '  23.5\u00b0C  '
#    data2 = 'PARCIALMENTE NUBLADO'

    icon = ''
    if( data[1] in range(1,5)):
        icon = "sunny"
    elif(data[1] in range(5,12)):
        icon = "partlycloudy"
    elif(data[1] in range(12,19)):
        icon = "rain"
    elif(data[1] in range(19,30)):
        icon = "cloud"
    elif(data[1] in range(31,35)):
         icon = "moon"
    elif(data[1] in range(35,39)):
         icon = "cloudymoon"
    elif(data[1] in range(39,45)):
         icon = "rainmoon"

    obj = {"icon": { "x": x_icon, "y": 10, "value": icon }, "message": { "x": 9, "y": y_msg, "value": data[0]}, "remaining_time": 15 }
    
    print("Get Weather ... " + notification(myObj=obj))

def main():
    schedule.every(30).minutes.do(get_weather)
#    schedule.every(10).seconds.do(get_weather)
    
