import requests
from pprint import pprint

API_ENDPOINT = "https://api.sheety.co/e87c6faabdd61205ee49f30b11c9b043/flightDeals/prices"
TOKEN = "ksnfkslnksnkfllfkmkmnklsmnks"

header = {
    "Authorization": f"Bearer {TOKEN}"
}

class FlightData:
    # This class is responsible for structuring the flight data.
    def __init__(self):
        self.response = requests.get(url=API_ENDPOINT, headers=header)
        self.data = self.response.json()
        pprint(self.data)


#flight = FlightData()
