# Flight Deals Tracker

A Python program that monitors flight deals using Google Sheets and sends SMS alerts when better deals are found. The app uses the Sheety API to store destinations and price thresholds, Kiwi.com’s Tequila API to fetch IATA codes and search flights, and Twilio to send SMS notifications.

## Features
- Spreadsheet‑backed data – reads destination cities and target prices from a Google Sheet via Sheety and updates missing IATA codes by city name.
- ATA code retrieval – queries Kiwi’s Tequila API to find the IATA airport code for each city.
- Flight search – searches round‑trip flights from a home airport (default "MIA") to each destination between tomorrow and six months from today; ensures a stay between 7 and 28 nights and returns the cheapest flight found.
- Layover detection – determines whether the cheapest flight has stopovers and records connecting airports.
- SMS notifications – sends an SMS alert via Twilio with flight details and layover route when the price is below the threshold.
- Extendable design – modular classes for data management, flight search, flight data modelling and notification sending make it easy to swap endpoints or add new features.

## How it Works
1. Set up the spreadsheet: Create a Google Sheet with columns for city, iataCode and lowestPrice. Use Sheety to expose the sheet as a REST API and obtain a bearer token.

![image](https://user-images.githubusercontent.com/108564860/185837146-65bbbdba-12b5-4a11-9e48-c37eca01f458.png)

3. Environment variables: Save your Sheety token (SHEETY_TOKEN), Tequila API key (TEQUILA_KEY), Twilio account SID (TWILIO_ACCOUNT_SID), Twilio auth token (TWILIO_AUTH_TOKEN), Twilio phone number (MY_TWILIO_NUM) and recipient number (RECIPIENT_NUM) as environment variables.
4. Data retrieval: DataManager fetches the current list of destinations from the sheet using a GET request. If any rows have missing IATA codes, FlightSearch requests the code from the Tequila API and DataManager updates the sheet via a PUT request.
5. Flight search: For each destination, FlightSearch.find_flight queries the Tequila search endpoint with parameters for origin, destination, date range, nights stay and currency. It handles cases where no flights are found.
6. Price comparison: The script compares the price of the cheapest flight with the lowestPrice column in the sheet.
7. Notification: If a deal is cheaper, NotificationManager.send_sms constructs a message including the route, price, dates and layover details (if any) and sends it to the recipient via Twilio.



## Setup and Usage
1. Clone the repository
```bash
git clone https://github.com/AntonioIIOlaguer/flight-deals.git
cd flight-deals
```
2. Install Dependencies
  This script uses requests and twilio. Install them via pip:
```bash
pip install requests twilio
```
3. Create your Sheety endpoint (optional)
The SHEETY_ENDPOINT constant inside data_manager.py points to a sample sheet endpoint. Replace it with your own Sheety API endpoint if you use a different Google Sheet.

4. Configure environment variables
Export the required keys and tokens in your terminal or use a .env manager. Example:
```bash
export SHEETY_TOKEN="your_sheety_token"
export TEQUILA_KEY="your_tequila_api_key"
export TWILIO_ACCOUNT_SID="your_twilio_sid"
export TWILIO_AUTH_TOKEN="your_twilio_auth_token"
export MY_TWILIO_NUM="+1234567890"
export RECIPIENT_NUM="+0987654321"
```

5. Run the program
```bash
python main.py
```
The script will update missing IATA codes, search for flights and send SMS alerts for deals cheaper than your specified threshold.

## Customization
-	Origin airport: Modify the origin_city variable in main.py to search from a different departure airport .
- Date range and nights: Adjust the date calculations or query parameters in main.py and flight_search.py to change the search window or length of stay.
- Maximum stopovers: Change the max_stopovers parameter in flight_search.py to control how many connections are allowed.
- Message content: Update the formatting of the SMS in notification_manager.py to include additional details or different wording.

> Note: The repository currently does not include an open‑source license. Please contact the author for permissions if you intend to reuse or modify the code.
