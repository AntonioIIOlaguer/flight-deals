# flight-deals

A program to search for cheap flights using a spreadsheet of destination with a price in mind.
With a google spreadhseet with this layout

![image](https://user-images.githubusercontent.com/108564860/185837146-65bbbdba-12b5-4a11-9e48-c37eca01f458.png)

It uses Sheety API to parse the data, and fill the appropriate iataCode for the city using 
Tequilla API by Kiwi.com for flight Data.
It then searches for flights between tomorrow and 6 months from now with roundtrips that return 7-28 days in length.
If the price falls bellow the price listed a notificaiton is sent using a Twillio account 
via an API to send a SMS to a specified number.
