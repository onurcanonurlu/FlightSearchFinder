import requests
from datetime import datetime
from datetime import timedelta

TEQUILA_ENDPOINT = "https://tequila-api.kiwi.com"
TEQUILA_API_KEY = "YOUR TEQUILA API KEY"
SHEETS_ENDPOINT = "YOUR SHEETS ENDPOINT"

today=datetime.now()
six_months_later = datetime.now() + timedelta(days = 180)



class FlightData:
    def __init__(self):
        self.departure_cities = "IST"
        self.price = 0
        self.departure_date = ""
        self.days_to = ""
        self.destination_city = ""
        self.search_data = []

    def setting_parameters(self,travel):
            self.price = int(travel["lowestPrice"])
            self.departure_date = today.strftime("%d/%m/%Y")
            self.days_to = six_months_later.strftime("%d/%m/%Y")
            self.destination_city = travel["iataCode"]
            data_dict = {
                "apikey": TEQUILA_API_KEY,
                "fly_from": self.departure_cities,
                "fly_to": self.destination_city,
                "date_from": self.departure_date,
                "date_to": self.days_to,
                "price_to": self.price,
                "curr" : "TRY",
                "flight_type" : "round",
                "nights_in_dst_from" : 7,
                "nights_in_dst_to" : 28,
                "one_for_city": 1,
                "max_stopovers": 0
            }
            self.search_data.append(data_dict)
            return self.search_data
