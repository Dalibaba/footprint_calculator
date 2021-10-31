import openrouteservice


class ORS_Client(object):
    def __init__(self, api_key, coordinates):
        self.client = openrouteservice.Client(key=api_key)
        self.coordinates = coordinates
        self.profile_list = ['driving-car', "cycling-regular",
                             "cycling-electric", "foot-walking"]

    def send_request(self):
        response = self.client.directions(coordinates=self.coordinates,
                                          profile= self.profile_list[0],
                                          format='geojson',
                                          units= "km")
        return response
