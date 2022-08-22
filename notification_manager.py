from flight_data import FlightData
import os
from twilio.rest import Client
import time

account_sid = os.environ.get('TWILIO_ACCOUNT_SID')
auth_token = os.environ.get('TWILIO_AUTH_TOKEN')
MY_TWILIO_NUMBER = os.environ.get('MY_TWILIO_NUM')
RECIPIENT_NUM = os.environ.get('RECIPIENT_NUM')

class NotificationManager:
    #This class is responsible for sending notifications with the deal flight details.
    def send_sms(self, data:FlightData):
        """Takes a flight data then sends a SMS to your phone number"""
        if data.layover != None:
            message_content = (f"Cheap Flight Alert! ✈️ "
                f"\nFly from {data.origin_city} to {data.destination_city} for only ${data.price}"
                f"\nRoute: {'-'.join(data.layover)}"
                f"\nDate of flight: {data.out_date}"
                f"\nReturn flight date: {data.return_date}"
            )
        else:
            message_content = (f"Cheap Flight Alert! ✈️ "
                f"\nFly from {data.origin_city} to {data.destination_city} for only ${data.price}"
                f"\nRoute: {data.origin_airport}-{data.destination_airport}"
                f"\nDate of flight: {data.out_date}"
                f"\nReturn flight date: {data.return_date}"
            )
                        

        client = Client(account_sid, auth_token)

        message = client.messages \
                        .create(
                            body=message_content,
                            from_=MY_TWILIO_NUMBER,
                            to=RECIPIENT_NUM,
                        )
        print(message.status)
        print(message_content)
        #Prevents the message from being mixed up with a 3 second buffer between messages
        time.sleep(2)
