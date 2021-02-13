import requests

response = requests.get(url='http://api.open-notify.org/iss-now.json')
response.raise_for_status()

data = response.json()
# print(data)

latitude = response.json()['iss_position']['latitude']
longitude = response.json()['iss_position']['longitude']

position = (latitude, longitude)

print(position)