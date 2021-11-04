import openrouteservice


class ORS_Client(object):
    def __init__(self, api_key, coordinates):
        self.client = openrouteservice.Client(key=api_key)
        self.coordinates = coordinates
        self.profile_list = ['driving-car', "cycling-regular", "foot-walking"]

    def send_request(self):
        # send request for all mobility options
        responses = []
        for profile in self.profile_list:
            response = self.client.directions(coordinates=self.coordinates,
                                              profile=profile,
                                              format='geojson',
                                              units="km")
            responses.append(response)
        return responses
