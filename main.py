from data_manager import DataManager
from flight_data import FlightData
from flight_search import FlightSearch
from datetime import datetime, timedelta
from notification_manager import NotificationManager
import time
#This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve the program requirements.

data_manager = DataManager()
flight_search = FlightSearch()
notification_manager = NotificationManager()

for row, destination in enumerate(data_manager.destinations, start=2):
    iata_code = flight_search.get_destination_code(destination["city"])
    if destination["iataCode"] != iata_code:
        destination["iataCode"] = iata_code
        data_manager.fill_iata(row, iata_code)

tomorrow = datetime.now() + timedelta(days=1)
six_month_from_today = datetime.now() + timedelta(days=(6 * 30))
origin_city = "MIA"

for destination in data_manager.destinations:
    cheapest_flight = flight_search.find_flight(origin_city, destination["iataCode"], tomorrow,six_month_from_today)
    if cheapest_flight != None and int(cheapest_flight.price) < int(destination["lowestPrice"]):
        notification_manager.send_sms(cheapest_flight)
