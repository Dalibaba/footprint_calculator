import json


def get_metrics_from_response_options(response_options):
    response_dict = {"car": None, "bike": None, "foot": None}
    print(response_options)
    for response, key in zip(response_options, response_dict):
        duration = response["features"][0]["properties"]["summary"]["duration"]
        distance = response["features"][0]["properties"]["summary"]["distance"]
        metrics = {"duration": duration, "distance": distance}
        print(metrics)
        response_dict[key] = metrics
    return response_dict


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
