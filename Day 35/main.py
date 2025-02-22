import os
import requests
from twilio.rest import Client

KEY = os.environ['KEY']
account_sid = os.environ['account_sid']
auth_token = os.environ['auth_token']

parameters = {
    "lat": -2.529450,
    "lon": -44.296951,
    "exclude": 'current,minutely,daily',
    "appid": KEY
}

response = requests.get('https://api.openweathermap.org/data/2.5/onecall', params=parameters)
response.raise_for_status()

data = response.json()
print(data)
for i in range(0,12):
    hourly_weather_id = data['hourly'][i]['weather'][0]['id']
    if hourly_weather_id < 700:
        client = Client(account_sid, auth_token)
        message = client.messages \
            .create(
            body="It's going to rain. Please carry your umbrella today. ☔",
            from_='+12107750561',
            to='+918879561392'
        )
        print(message.status)
        break