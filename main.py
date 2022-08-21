from data_manager import DataManager
from flight_search import FlightSearch
#This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve the program requirements.

data_manager = DataManager()
flight_search = FlightSearch()

for row, destination in enumerate(data_manager.destinations, start=2):
    iata_code = flight_search.get_destination_code(destination["city"])
    if destination["iataCode"] != iata_code:
        destination["iataCode"] = iata_code
        data_manager.fill_iata(row, iata_code)

