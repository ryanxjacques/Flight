"""
Interacting my flightAPI from https://aviationstack.com/
"""

import requests
from datetime import datetime
from datetime import timezone
import random
import json

#======================== UNCOMMENT TO ACCESS API DATA ===============================
# url = "http://api.aviationstack.com/v1/flights"
# params = {
#     "access_key": "71b8a3f1273c8d7ce386086d7bef9f3b"
# }
#
# api_result = requests.get(url, params=params)
#
#
# # check if the request was successful
# if api_result.status_code == 200:
#     print("Request successful!")
#     # extract the response data as a dictionary
#     api_response = api_result.json()
# ======================== UNCOMMENT TO ACCESS API DATA ===============================



#======================== UNCOMMENT TO SAVE NEW API DATA ===============================
    # Save the api_response to a file to limit api calls for testing
    # with open("api_response.json", "w") as outfile:
    #     json.dump(api_response, outfile, indent=4)
#======================== UNCOMMENT TO SAVE NEW API DATA ===============================

with open("api_response.json", "r") as f:
    api_response = json.load(f)
    # get today's date (timezone - aware)
    today = datetime.now()
    today = today.replace(tzinfo=timezone.utc)

    # chose a random flight from api_response
    flight = random.choice(api_response['data'])

    # format of the departure date
    date_format = "%Y-%m-%dT%H:%M:%S%z"

    # only choose flights that are later than right now
    departure_time = datetime.strptime(flight['departure']['scheduled'], date_format)

    while  departure_time < today:
        print("Had to choose another one")
        flight = random.choice(api_response['data'])

    formatted_time = departure_time.strftime('%m-%d-%Y at %I:%M %p')


    print(f"Congrats, you're going to {flight['arrival']['airport']} ({flight['arrival']['iata']})"
          f" via {flight['departure']['airport']} ({flight['departure']['iata']})!\n"
          f"Departure time: {formatted_time}")


# ======================== UNCOMMENT TO ACCESS API DATA ===============================
# else:
#     print(f"Error: {api_result.status_code} -- {api_result.reason}")
# ======================== UNCOMMENT TO ACCESS API DATA ===============================




