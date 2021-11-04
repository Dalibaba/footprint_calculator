import json
import os

from flask import Blueprint, jsonify, request

from api.api_calls.api_caller import API_Caller
from api.api_calls.ors_client import ORS_Client
from api.utils import response_service

mobility = Blueprint('mobility', __name__)


@mobility.route('')
def get_mobility():
    start = request.args.get('start', type=str)
    destination = request.args.get('destination', type=str)

    if isinstance(start, str) == False or isinstance(destination, str) == False:
        return {"message": "start or destination not valid"}

    api_caller = API_Caller(os.getenv("GEOCODE_URL"), os.getenv("ORS_API_KEY"))
    # get geocodes of start and response
    response_start = api_caller.send_request(start)
    response_destination = api_caller.send_request(destination)
    # extract geolocation from response
    coordinates_start = response_service.get_coordinates_from_response(response_start)
    coordinates_destination = response_service.get_coordinates_from_response(response_destination)
    # get route information from start to destination
    coordinates = [[coordinates_start["longitude"], coordinates_start["latitude"]],
                   [coordinates_destination["longitude"], coordinates_destination["latitude"]]]
    ors_client = ORS_Client(os.getenv("ORS_API_KEY"), coordinates)
    responses_options = ors_client.send_request()

    response = response_service.get_metrics_from_response_options(responses_options)

    return jsonify(response)
