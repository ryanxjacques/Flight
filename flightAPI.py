"""
Interacting my flightAPI from https://aviationstack.com/
"""

import requests

url = "http://api.aviationstack.com/v1/flights"
params = {
    "access_key": "71b8a3f1273c8d7ce386086d7bef9f3b"
}

response = requests.get(url, params=params)

# check if the request was successful
if response.status_code == 200:
    # extract the response data as a dictionary
    data = response.json()

    # do something with the response data
    print(data)
else:
    print("Error:", response.status_code)

print(data)



