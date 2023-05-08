"""
Interacting my flightAPI from https://aviationstack.com/
"""

import requests
import json


url = "http://api.aviationstack.com/v1/flights"
params = {
    "access_key": "71b8a3f1273c8d7ce386086d7bef9f3b",
    "flight_status": "active"
}

api_result = requests.get(url, params=params)

# check if the request was successful
if api_result.status_code == 200:
    # extract the response data as a dictionary
    api_response = api_result.json()

    for flight in api_response['data']:
    # for flight in api_response['data']:
        live_data = flight.get('live')
        if live_data and not live_data.get('is_ground', True):
            print(u'%s flight %s from %s (%s) to %s (%s) is in the air.' % (
                flight['airline']['name'],
                flight['flight']['iata'],
                flight['departure']['airport'],
                flight['departure']['iata'],
                flight['arrival']['airport'],
                flight['arrival']['iata']))
else:
    print(f"Error: {api_result.status_code} -- {api_result.reason}")




