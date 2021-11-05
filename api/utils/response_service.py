import time
import json


def get_metrics_from_response_options(response_options):
    response_dict = {"car": None, "bike": None, "foot": None}
    for response, key in zip(response_options, response_dict):
        duration = response["features"][0]["properties"]["summary"]["duration"]
        distance = response["features"][0]["properties"]["summary"]["distance"]
        duration = time.strftime('%H:%M:%S', time.gmtime(duration))
        metrics = {"duration": duration, "distance": distance}
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


def get_train_route_metadata(response):
    response_json = json.loads(response.content)
    distance = response_json["features"][0]["properties"]["distance"]
    duration = response_json["features"][0]["properties"]["time"]
    instructions = response_json["features"][0]["properties"]["legs"][0]["steps"]

    ENTER = "Enter"
    EXIT = "Exit"
    Station = "Station"

    enter_station = []
    exit_stations = []
    for instruction in instructions:
        instruction_text = instruction["instruction"]["text"]

        if ENTER in instruction_text and Station in instruction_text:
            print(instruction_text)
            split_words = instruction_text.split()
            split_words = split_words[2:len(split_words) - 1]
            station = " ".join(split_words)
            enter_station.append(station)

        if EXIT in instruction_text and Station in instruction_text:
            split_words = instruction_text.split()
            split_words = split_words[2:len(split_words) - 1]
            station = " ".join(split_words)
            exit_stations.append(station)

    metrics = {"duration": duration, "distance": distance,
               "enter_stations": enter_station, "exit_stations": exit_stations,
               "amount_changes": len(enter_station)}
    return metrics
