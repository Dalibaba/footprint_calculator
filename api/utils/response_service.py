import json


def get_coordinates_from_response(response):
    data_json = json.loads(response.content)
    coordinates = data_json["features"][0]["geometry"]["coordinates"]
    latitude = coordinates[1]
    longitude = coordinates[0]
    coordinates = {
        "latitude": latitude,
        "longitude": longitude,
    }
    return coordinates
