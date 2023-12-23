import schedule, requests
from datetime import date
from __main__ import notification

## USD EXCHANGE API
base="USD"
out_curr="CLP"
apikey="<apikey>"

def get_usd_exchange():
    start_date=date.today().strftime("%Y-%m-%d")
    end_date=start_date
    url = 'https://api.apilayer.com/exchangerates_data/timeseries?base={0}&start_date={1}&end_date={2}&symbols={3}'.format(base,start_date,end_date,out_curr)
    response = requests.get(url,headers={'apikey':apikey})
    data = response.json()
    print(data)
    curr = "Dolar en Chile:    " + str(int(data["rates"][start_date][out_curr])) + " CLP"
    obj = {"icon": { "x": 1, "y": 10, "value": "stocks" }, "message": { "x": 12, "y": 6, "value": curr}, "remaining_time": 10 }
    
    print("Get USD Exchange ... " + notification(myObj=obj))


def main():
    schedule.every(20).minutes.do(get_usd_exchange)
#    schedule.every(10).seconds.do(get_usd_exchange)
