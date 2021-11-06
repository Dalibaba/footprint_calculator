import os

from flask import Blueprint, jsonify, request

from api.api_calls.api_caller import OpenRouteService, GeoApiFy
from api.api_calls.ors_client import ORS_Client
from api.Route_Metric.metric import Route_Metric, Train_Route_Metric
from api.utils import response_service

mobility = Blueprint('mobility', __name__)


@mobility.route('')
def get_mobility():
    start = request.args.get('start', type=str)
    destination = request.args.get('destination', type=str)
    if not start or not destination:
        return {"message": "start or destination not valid"}, 400
    api_caller_open_route_service = OpenRouteService(os.getenv("ORS_URL"), os.getenv("ORS_API_KEY"))

    # get geocodes of start and response
    response_start = api_caller_open_route_service.send_request({"location": start})
    response_destination = api_caller_open_route_service.send_request({"location": destination})

    # extract geolocation from response
    coordinates_start = response_service.get_coordinates_from_response(response_start)
    coordinates_destination = response_service.get_coordinates_from_response(response_destination)

    # get route information from start to destination
    coordinates = [[coordinates_start["longitude"], coordinates_start["latitude"]],
                   [coordinates_destination["longitude"], coordinates_destination["latitude"]]]
    ors_client = ORS_Client(os.getenv("ORS_API_KEY"), coordinates)
    responses_options = ors_client.send_request()
    # create route instances
    bike_route = Route_Metric("bike", 0)
    car_route = Route_Metric("car", os.getenv("CAR_CO2_GRAM_PER_KM"))
    foot_route = Route_Metric("foot", 0)
    # extract route metrics from json
    bike_route.extract_metrics_from_json(responses_options[0])
    car_route.extract_metrics_from_json(responses_options[1])
    foot_route.extract_metrics_from_json(responses_options[2])

    response_metrics = {**bike_route.get_object(), **car_route.get_object(), **foot_route.get_object()}

    # get train route
    try:

        api_caller_geoapify = GeoApiFy(os.getenv("GEOAPIFY_URL"), os.getenv("GEOAPIFY_API_KEY"))
        response_train = api_caller_geoapify.send_request({"mode": "approximated_transit", "coordinates": coordinates})
        train_route = Train_Route_Metric("train", response_train, os.getenv("TRAIN_CO2_GRAM_PER_KM"))
        # add train metrics to metrics
        response_metrics = {**response_metrics, **train_route.get_object()}
    except:
        print("no train route could be found")

    return jsonify(response_metrics)
