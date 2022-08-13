import os
import requests
from datetime import datetime
HEADER = {"apikey" : os.environ.get("TEQUILA_KEY")}
TEQUILA_ENDPOINT = "https://tequila-api.kiwi.com"

class FlightSearch:
    #This class is responsible for talking to the Flight Search API.
    def get_destination_code(self,city):
        self.query = {
            "term":city,
            "location_types":"city"
        }
        self.response = requests.get(url=f"{TEQUILA_ENDPOINT}/locations/query",params=self.query, headers=HEADER)
        self.response.raise_for_status()
        self.code = self.response.json()["locations"][0]["code"]
        return self.code
