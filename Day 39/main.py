# This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve the program requirements.
from flight_data import FlightData
from flight_search import FlightSearch

class Flight:
    def __init__(self):
        self.flight_data = FlightData()
        self.flight_search = FlightSearch()

flight = Flight()
flight_search = FlightSearch()