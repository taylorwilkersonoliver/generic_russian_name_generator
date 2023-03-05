"""Weather information using the Google Awareness API.

Typical Usage:
    w = Weather()
    w.current_city = "Moscow"
    response = w.current_local_weather()
    print(response)

"""
import pandas as pd
import requests

from config import api_key_openweathermap_org, headers


class Weather:
    """Look up current local weather for a specific city using the API provided by openweathermaps.org.

    Typical Usage:
        w = Weather()
        w.current_city = "Moscow"
        response = w.current_local_weather()
        print(response)
    """
    def __init__(self, *args):
        self.all_cities = \
            pd.DataFrame(pd.read_json('excluded/data/ru.json'), columns=['city', 'lat', 'lng'])
        self.api_key = api_key_openweathermap_org
        self.headers = headers
        self.current_city = args[0]
        self.city_index = 0
        count = 0
        for i in self.all_cities.city:
            if i == self.current_city:
                self.city_index = count
            else:
                count = count + 1
        del count
        self.current_city_lat, self.current_city_lng = \
            self.all_cities.lat[self.city_index], self.all_cities.lng[self.city_index]

    def current_local_weather(self):
        """Look up the local weather for the lat/lng of the current city."""
        url = f"https://api.openweathermap.org/data/2.5/weather?lat=" \
              f"{self.current_city_lat}&lon={self.current_city_lng}&appid={self.api_key}"
        response = requests.get(url, headers=self.headers)
        return response.text
