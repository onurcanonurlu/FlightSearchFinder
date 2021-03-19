import requests
SHEETS_ENDPOINT = "YOUR SHEETS ENDPOINT"
class DataManager:
    def __init__(self):
        self.destination_data = {}

    def get_destination_data(self):
        data = requests.get(SHEETS_ENDPOINT).json()
        self.destination_data = data["prices"]
        return self.destination_data


    def update_destination_codes(self):
        for city in self.destination_data:
            new_data = {
                "price": {
                    "iataCode": city["iataCode"]
                }
            }
            response = requests.put(
                url=f"{SHEETS_ENDPOINT}/{city['id']}",
                json=new_data
            )
            print(response.text)
