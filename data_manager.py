import os
import requests
import json

HEADER ={
        "Authorization": f"Bearer {os.environ.get('SHEETY_TOKEN')}"
    }

SHEETY_ENDPOINT = "https://api.sheety.co/9a3505cc84e862e5b2a998a83b107f8e/flightDealsList/prices"

class DataManager:
    #This class is responsible for talking to the Google Sheet.
    def __init__(self) -> None:
        self.response_sheety = requests.get(url=SHEETY_ENDPOINT, headers=HEADER)
        self.response_sheety.raise_for_status()
        self.destinations = self.response_sheety.json()["prices"]

    def fill_iata(self, row=str, code=str) -> None:
        """Takes a row in the spreadsheet and the iataCode to fill"""
        flight_data ={
            "price":{
                "iataCode":code
            }
        }
        PUT_ENDPOINT = f"{SHEETY_ENDPOINT}/{row}"
        self.response_sheety = requests.put(url=PUT_ENDPOINT,json=flight_data, headers=HEADER)
        self.response_sheety.raise_for_status()

