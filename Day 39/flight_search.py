import requests

API_ENDPOINT = "https://api.sheety.co/e87c6faabdd61205ee49f30b11c9b043/flightDeals/prices"
TOKEN = "ksnfkslnksnkfllfkmkmnklsmnks"

header = {
    "Authorization": f"Bearer {TOKEN}"
}

class FlightSearch:
    #This class is responsible for talking to the Flight Search API.
    def __init__(self):
        self.response = requests.post(url=API_ENDPOINT, json=body, headers=header)
        print(self.response.text)
        self.data = self.response.json()

    def inserttesting(self):
        for i in range(len(self.data['prices'])):
            body = {
                "price": {
                    "iataCode": 'TESTING'
                }
            }
            