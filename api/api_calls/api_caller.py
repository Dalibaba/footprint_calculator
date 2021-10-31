import requests


class API_Caller(object):
    def __init__(self, api_url, api_key):
        self.api_url = api_url
        self.api_key = api_key
        self.params = {}

    def extend_params(self, location):
        self.params["api_key"] = self.api_key
        self.params["text"] = location

    def send_request(self, location):
        self.extend_params(location)
        response = requests.get(self.api_url, params=self.params)
        return response
