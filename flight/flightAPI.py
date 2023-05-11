"""
Interacting my flightAPI from https://aviationstack.com/
"""

import requests
from datetime import datetime
from datetime import timezone
import random
import json

def generate_flight() -> str:
    """
    Makes a call to "aviantionstack" endpoint "flights" and generates a random
    flight for the user.
    :return: Flight departure and arrival information
    """

    #======================== UNCOMMENT TO ACCESS API DATA ===============================
    url = "http://api.aviationstack.com/v1/flights"

    params = {
        "access_key": "71b8a3f1273c8d7ce386086d7bef9f3b"
    }

    api_result = requests.get(url, params=params)


    # check if the request was successful
    if api_result.status_code == 200:
        print("Request successful!")
        # extract the response data as a dictionary
        api_response = api_result.json()
    # ======================== UNCOMMENT TO ACCESS API DATA ===============================



    #======================== UNCOMMENT TO SAVE NEW API DATA ===============================
        # with open("api_response.json", "w") as outfile:
        #     json.dump(api_response, outfile, indent=4)
    #======================== UNCOMMENT TO SAVE NEW API DATA ===============================


    #======================== UNCOMMENT TO INTERACT WITH JSON FILE ===============================
    with open("../api_response.json", "r") as f:
        api_response = json.load(f)
    # ======================== UNCOMMENT TO INTERACT WITH JSON FILE ===============================
        # get today's date (timezone - aware)
        today = datetime.now()
        today = today.replace(tzinfo=timezone.utc)

        # chose a random flight from api_response
        flight = random.choice(api_response['data'])

        # format of the departure date
        date_format = "%Y-%m-%dT%H:%M:%S%z"

        # only choose flights that are later than right now
        departure_time = datetime.strptime(flight['departure']['scheduled'], date_format)

        while departure_time < today:
            # choose another flight if it isn't later
            flight = random.choice(api_response['data'])

        arrival_time = datetime.strptime(flight['arrival']['scheduled'], date_format)

        formatted_departure_time = departure_time.strftime('%m-%d-%Y at %I:%M %p')

        formatted_arrival_time = departure_time.strftime('%m-%d-%Y at %I:%M %p')

        json_string = f"{{\"arrival\": {{ \"airport\": {flight['arrival']['airport']}, " \
                      f"\"iata\"{flight['arrival']['iata']}"
        
        print(json_string)


        return (f"Congrats, you're going to {flight['arrival']['airport']} ({flight['arrival']['iata']})"
              f" via {flight['departure']['airport']} ({flight['departure']['iata']})!\n"
              f"Departure time: {formatted_time}")



    # ======================== UNCOMMENT TO ACCESS API DATA ===============================
    else:
        print(f"Error: {api_result.status_code} -- {api_result.reason}")
    # ======================== UNCOMMENT TO ACCESS API DATA ===============================