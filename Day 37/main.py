import os
import requests
from datetime import datetime

TOKEN = os.environ['TOKEN']
USERNAME = os.environ['USERNAME']
pixela_endpoint = os.environ['pixela_endpoint']
GRAPH_ID = os.environ['GRAPH_ID']

parameters = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes"
}

# response = requests.post(url=pixela_endpoint, json=parameters)
# print(response.text)

graph_endpoint = f'https://pixe.la/v1/users/{USERNAME}/graphs'

graph_parameters = {
    "id": GRAPH_ID,
    "name": "Reading Graph",
    "unit": "Hours",
    "type": "float",
    "color": "sora"
}

header = {
    'X-USER-TOKEN': TOKEN
}

# response = requests.post(url=graph_endpoint, json=graph_parameters, headers=header)
# print(response.text)

today = datetime(year=2021, month=2, day=21)
print(today.strftime("%Y%m%d"))

pixel_endpoint = f"https://pixe.la//v1/users/{USERNAME}/graphs/{GRAPH_ID}"

pixel_parameters = {
    "date": today.strftime("%Y%m%d"),
    "quantity": '3'
}

# response = requests.post(url=pixel_endpoint, json=pixel_parameters, headers=header)
# print(response.text)

update_endpoint = f"https://pixe.la//v1/users/{USERNAME}/graphs/{GRAPH_ID}/{today.strftime('%Y%m%d')}"

update_parameters = {
    "quantity": "3"
}

response = requests.put(url=update_endpoint, json=update_parameters, headers=header)
print(response.text)

delete_endpoint = f"https://pixe.la//v1/users/{USERNAME}/graphs/{GRAPH_ID}/{today.strftime('%Y%m%d')}"

# response = requests.delete(url=delete_endpoint, headers=header)
# print(response.text)
