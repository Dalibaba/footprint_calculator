import json
import time


class Route_Metric:
    def __init__(self, type, co2_per_km):
        self.type = type
        self.distance = 0
        self.duration = 0
        self.co2_per_km = co2_per_km

    def extract_metrics_from_json(self, route_json):
        self.duration = route_json["features"][0]["properties"]["summary"]["duration"]
        self.distance = route_json["features"][0]["properties"]["summary"]["distance"]
        self.duration = time.strftime('%H:%M:%S', time.gmtime(self.duration))

    def get_object(self):
        return {self.type: {"distance": self.distance,
                            "duration": self.duration,
                            "co2_emission": (float(self.distance) * float(self.co2_per_km)) / 1000,  # kg
                             }}


class Train_Route_Metric(Route_Metric):
    def __init__(self, type, co2_per_km):
        super().__init__(self, type, co2_per_km)
        self.amount_changes = 0
        self.enter_stations = []
        self.exit_stations = []

    def extract_metrics_from_json(self, route_json):
        route_json = json.loads(route_json.content)
        self.distance = route_json["features"][0]["properties"]["distance"]
        self.duration = route_json["features"][0]["properties"]["time"]
        self.duration = time.strftime('%H:%M:%S', time.gmtime(self.duration))
        instructions = route_json["features"][0]["properties"]["legs"][0]["steps"]

        ENTER = "Enter"
        EXIT = "Exit"
        Station = "Station"

        for instruction in instructions:
            instruction_text = instruction["instruction"]["text"]

            if ENTER in instruction_text and Station in instruction_text:
                split_words = instruction_text.split()
                split_words = split_words[2:len(split_words) - 1]
                station = " ".join(split_words)
                self.enter_station.append(station)

            if EXIT in instruction_text and Station in instruction_text:
                split_words = instruction_text.split()
                split_words = split_words[2:len(split_words) - 1]
                station = " ".join(split_words)
                self.exit_stations.append(station)

    def get_object(self):
        return {self.type: {"distance": self.distance,
                            "duration": self.duration,
                            "co2_emission": (float(self.distance) * float(self.co2_per_km)) / 1000,  # kg
                            "amount_changes": self.amount_changes,
                            "enter_stations": self.enter_stations,
                            "exit_stations": self.exit_stations,
                            }}
