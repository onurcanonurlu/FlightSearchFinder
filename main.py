import requests
from pprint import pprint
from flight_search import FlightSearch

flight_search = FlightSearch()
from data_manager import DataManager

data_manager = DataManager()
from flight_data import FlightData

flight_data = FlightData()
from notification_manager import NotificationManager

notification_manager = NotificationManager()

search_data = []
SHEETS_ENDPOINT = "YOUR SHEETY ENDPOINT"
sheet_data = data_manager.get_destination_data()
for data in requests.get(SHEETS_ENDPOINT).json()["prices"]:
    sheet_data.append(data)
    search_data.append(flight_data.setting_parameters(data))

if sheet_data[0]["iataCode"] == "":
    for row in sheet_data:
        row["iataCode"] = flight_search.get_destination_code(row["city"])
        print(f"sheet_data:\n {sheet_data}")

    data_manager.destination_data = sheet_data
    data_manager.update_destination_codes()
data_data_2 = requests.get(SHEETS_ENDPOINT).json()

print(flight_search.search_for_flights(search_data[0]))

if(flight_search.search_for_flights(search_data[0]))["data"]!= 0:
    flight_price = flight_search.search_for_flights(search_data[0])["data"][0]["price"]
    flight_origin_city = flight_search.search_for_flights(search_data[0])["data"][0]["cityFrom"]
    flight_origin_airport = flight_search.search_for_flights(search_data[0])["data"][0]['flyFrom']
    flight_destination_city = flight_search.search_for_flights(search_data[0])["data"][0]['cityTo']
    flight_destination_airport = flight_search.search_for_flights(search_data[0])["data"][0]["flyTo"]
    flight_out_date = flight_search.search_for_flights(search_data[0])["data"][0]["route"][0]["local_departure"]
    out_date_formatted = str(flight_out_date).split("T")[0]
    flight_return_date = flight_search.search_for_flights(search_data[0])["data"][0]["route"][1]["local_departure"]
    return_date_formatted = str(flight_return_date).split("T")[0]
    notification_manager.send_sms(
      message=f"Low price alert! Only {flight_price} TL to fly from {flight_origin_city}-{flight_origin_airport} to {flight_destination_city}-{flight_destination_airport}, from {out_date_formatted} to {return_date_formatted}."
   )
