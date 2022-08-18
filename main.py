from data_manager import DataManager
from flight_search import FlightSearch
#This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve the program requirements.

data_manager = DataManager()
flight_search = FlightSearch()

for destination in data_manager.destinations:
    destination["iataCode"] = flight_search.get_destination_code(destination["city"])

data_manager.fill_iata(data_manager.destinations)

print(data_manager.destinations)