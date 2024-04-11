import requests


SHEETY_USERNAME = YOUR_SHEETY_USERNAME
# https://sheety.co/docs/requests.html for better understanding for url
SHEETY_PRICES_ENDPOINT = f"https://api.sheety.co/{SHEETY_USERNAME}/flightDeals/prices" #it's an example


class DataManager:

    def __init__(self):
        self.destination_data = {}

    def get_destination_data(self) -> any:
        """Gets all the data in given sheet in code."""
        response = requests.get(url=SHEETY_PRICES_ENDPOINT)
        data = response.json()
        self.destination_data = data["prices"]
        return self.destination_data

    def update_destination_codes(self) -> None:
        """updates the Google Sheet with the IATA codes."""
        for city in self.destination_data:
            new_data = {
                "price": {
                    "iataCode": city["iataCode"]
                }
            }
            response = requests.put(
                url=f"{SHEETY_PRICES_ENDPOINT}/{city['id']}",
                json=new_data
            )
            print(response.text)
