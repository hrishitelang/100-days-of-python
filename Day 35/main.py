import requests
from twilio.rest import Client

KEY = "82dc612e99793a50d4bf7a77f29c6592"

parameters = {
    "lat": -2.529450,
    "lon": -44.296951,
    "exclude": 'current,minutely,daily',
    "appid": KEY
}

response = requests.get('https://api.openweathermap.org/data/2.5/onecall', params=parameters)
response.raise_for_status()

account_sid = "AC3c9761c1f610fe96f2c996069774fcab"
auth_token = "7584fbbdaf5fd06f13593f5d43b68613"

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