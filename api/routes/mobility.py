import os

from flask import Blueprint, jsonify, request

from api.api_calls.api_caller import API_Caller, OpenRouteService, GeoApiFy
from api.api_calls.ors_client import ORS_Client
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

    # get train route
    api_caller_geoapify = GeoApiFy(os.getenv("GEOAPIFY_URL"), os.getenv("GEOAPIFY_API_KEY"))
    response_train = api_caller_geoapify.send_request({"mode": "approximated_transit",
                                                       "coordinates": coordinates})
    train_metrics = response_service.get_train_route_metadata(response_train)

    # add train metrics to metrics
    metrics = response_service.get_metrics_from_response_options(responses_options)
    metrics["train"] = train_metrics
    return jsonify(metrics)
