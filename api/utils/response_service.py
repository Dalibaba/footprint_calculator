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


def get_metrics_from_response(response):
    duration = response["features"][0]["properties"]["summary"]["duration"]
    distance = response["features"][0]["properties"]["summary"]["distance"]

    return duration, distance


def format_response(duration, distance):
    response = {"duration": duration, "distance": distance}
    return response
