import requests
import datetime as dt

MY_LAT = 19.249206
MY_LONG = 72.853555
'''
response = requests.get(url='http://api.open-notify.org/iss-now.json')
response.raise_for_status()

data = response.json()
# print(data)

latitude = response.json()['iss_position']['latitude']
longitude = response.json()['iss_position']['longitude']

position = (latitude, longitude)

print(position)

'''
parameters = {
    'lat': MY_LAT,
    'lng': MY_LONG,
    'formatted': 0
}

response = requests.get('https://api.sunrise-sunset.org/json', params=parameters)
response.raise_for_status()

data = response.json()
sunrise = data["results"]["sunrise"].split('T')[1][:2]
sunset = data["results"]["sunset"].split('T')[1][:2]
print(data)
print(sunrise)
print(sunset)

now = dt.datetime.now()
print(now.hour)