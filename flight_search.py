import os
import requests
from datetime import datetime
from flight_data import FlightData

HEADER = {"apikey" : os.environ.get("TEQUILA_KEY")}
TEQUILA_ENDPOINT = "https://tequila-api.kiwi.com"

class FlightSearch:
    #This class is responsible for talking to the Flight Search API.
    def get_destination_code(self,city):
        query = {
            "term":city,
            "location_types":"city"
        }
        response = requests.get(url=f"{TEQUILA_ENDPOINT}/locations/query",params=query, headers=HEADER)
        response.raise_for_status()
        code = response.json()["locations"][0]["code"]
        return code

    def find_flight(self, origin_code, destination_code, date_from, date_to):
        """Find flights based on Iata Code and date"""
        search_endpoint = f"{TEQUILA_ENDPOINT}/v2/search"

        query = {
            "fly_from": origin_code,
            "fly_to": destination_code,
            "date_from": date_from.strftime("%d/%m/%Y"),
            "date_to": date_to.strftime("%d/%m/%Y"),
            "nights_in_dst_from": 7,
            "nights_in_dst_to": 28,
            "flight_type": "round",
            "one_for_city":1,
            "max_stopovers": 3,
            "curr": "USD"
        }

        response = requests.get(url=search_endpoint, params=query, headers=HEADER)
        response.raise_for_status()

        try:
            data = response.json()["data"][0]
        except IndexError:
            print(f"No flights found for {destination_code}.")
            return None

        flight_data = FlightData(
            price=data["price"],
            origin_city=data["cityFrom"],
            origin_airport=data["route"][0]["flyFrom"],
            destination_city=data["cityTo"],
            destination_airport=data["route"][-1]["flyTo"],
            out_date=data["route"][0]["local_departure"].split("T")[0],
            return_date=data["route"][-1]["local_departure"].split("T")[0]
        )
        if len(data["route"]) > 2:
            flight_data.layover = [route["flyFrom"] for route in data["route"]]
            print(f"{flight_data.destination_city}: ${flight_data.price} via {'-'.join(flight_data.layover)}")
        else:
            print(f"{flight_data.destination_city}: ${flight_data.price}")

        return flight_data