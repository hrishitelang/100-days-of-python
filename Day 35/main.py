import requests
import os
from twilio.rest import Client

KEY = "82dc612e99793a50d4bf7a77f29c6592"
TWILIO_ACCOUNT_SID = "AC3c9761c1f610fe96f2c996069774fcab"
TWILIO_AUTH_TOKEN = "7584fbbdaf5fd06f13593f5d43b68613"

parameters = {
    "lat": -2.529450,
    "lon": -44.296951,
    "exclude": 'current,minutely,daily',
    "appid": KEY
}

response = requests.get('https://api.openweathermap.org/data/2.5/onecall', params=parameters)
response.raise_for_status()

account_sid = os.environ[TWILIO_ACCOUNT_SID]
auth_token = os.environ[TWILIO_AUTH_TOKEN]
client = Client(account_sid, auth_token)

data = response.json()
print(data)
for i in range(0,12):
    hourly_weather_id = data['hourly'][i]['weather'][0]['id']
    if hourly_weather_id < 700:
        print(f"{i}: id={hourly_weather_id}")
        print('Bring an Umbrella')
# print(hourly_weather)