import requests
from abc import ABC, abstractmethod

from requests.structures import CaseInsensitiveDict

headers = CaseInsensitiveDict()
headers["Accept"] = "application/json"

class API_Caller(ABC):
    def __init__(self, api_url, api_key):
        self.api_url = api_url
        self.api_key = api_key
        self.params = {}

    @abstractmethod
    def create_params(self, location):
        pass

    def send_request(self, params):
        self.create_params(params)
        response = requests.get(self.api_url, params=self.params, headers=headers)
        return response


class OpenRouteService(API_Caller):
    def __init__(self, api_url, api_key):
        super().__init__(api_url, api_key)

    def create_params(self, params):
        self.params["api_key"] = self.api_key
        self.params["text"] = params["location"]


class GeoApiFy(API_Caller):
    def __init__(self, api_url, api_key):
        super().__init__(api_url, api_key)

    def create_params(self, params):
        coordinates = self.create_coordinate_string(params["coordinates"])
        self.params["apiKey"] = self.api_key
        self.params["mode"] = params["mode"]
        self.params["waypoints"] = coordinates

    def create_coordinate_string(self, coordinates):
        start_coordinates = coordinates[0]
        destination_coordinates = coordinates[1]
        start_string = str(start_coordinates[1]) + "," + str(start_coordinates[0])
        destination_string = str(destination_coordinates[1]) + "," + str(destination_coordinates[0])
        coordinate_string = start_string + "|" + destination_string
        return coordinate_string
