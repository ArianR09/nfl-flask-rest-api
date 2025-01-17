import requests

BASE = "http://127.0.0.1:5000/" # Local host address for API. 

# Test the API by sending a GET request with the 'BASE' URL.

# Player Model
response = requests.get(BASE + "player/Tavon Austin") # String value
print(response.json())

# Draft Pick Model
repsonse = requests.get(BASE + "draftpick/1st") # String value
print(response.json())

# Team Model
response = requests.get(BASE + "team/Denver Broncos") # String value
print(response.json())

# Draft Class Model
response = requests.get(BASE + "draftclass/2000") # Integer value
print(response.json())

# Insert player ID, from Player Model.
response = requests.get(BASE + 'playerid/17891') # Integer value, Aaron Rodgers.
print(response.json())
