import os
import requests
from datetime import datetime

EXERCISE_ENDPOINT = os.environ.get('EXERCISE')
SHEETY_ENDPOINT = os.environ.get('SHEETY')
API_KEY = os.environ['API_KEY']
APP_ID = os.environ['APP_ID']
# GENDER = input("What is your age? (male/female):")
# WEIGHT = float(input("What is your weight? "))
# HEIGHT = float(input("What is your height? "))
# AGE = int(input("What is your age?"))

exercise_params = {
 "query": input("Tell me which exercises you did:"),
 "gender": "male",
 "weight_kg": "79",
 "height_cm": "177.5",
 "age": "22"
}

header = {
    "x-app-id": APP_ID,
    "x-app-key": API_KEY,
    "Content-Type": "application/json",
    "Authorization": "Bearer ksnfkslnksnkfllfkmkmnklsmnks"
}

response = requests.post(url=EXERCISE_ENDPOINT, json=exercise_params, headers=header)
data = response.json()
print(data)

# a = response.json()['exercises'][0]['name']
# print(a)

for i in range(len(data['exercises'])):
    today = datetime.now()
    date = today.strftime("%d/%m/%Y")
    time = today.strftime("%H:%M:%S")
    body = {
      "workout": {
        "date": date,
        "time": time,
        "exercise": data['exercises'][i]['name'].title(),
        "duration": data['exercises'][i]['duration_min'],
        "calories": data['exercises'][i]['nf_calories']
      }
    }
    response = requests.post(url=SHEETY_ENDPOINT, json=body, headers=header)
    print(response.text)


