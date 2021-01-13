from os import path, mkdir

import requests

from urls import URL_GERMANY


class DataHandler:

    def __init__(self):

        self.data_germany = []

    def update_data(self):
        """Getting the latest covid data from different sources"""

        # Creating the data directory if it does not exist
        if not path.exists("data"):
            mkdir("data")

        # Performing an API request, TODO: Manage failed requests
        response = requests.get(URL_GERMANY)
        response_json = response.json()

        print(response_json['fields'])

        german_city_data = response_json['features']

        for current_city in german_city_data:

            current_city_attributes = current_city['attributes']

            # City attributes
            city_name = current_city_attributes['GEN']
            city_cases = current_city_attributes['cases']
            city_deaths = current_city_attributes['deaths']
            city_last_update = current_city_attributes['last_update']
            city_population_count = current_city_attributes['EWZ']
            city_incidence = current_city_attributes['cases7_per_100k']

            if "Neumarkt" in city_name:
                print(city_incidence)



