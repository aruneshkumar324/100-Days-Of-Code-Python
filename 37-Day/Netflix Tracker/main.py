import requests
from datetime import datetime


ENDPOINT_URL = "https://pixe.la/v1/users"
TOKEN = "s2BbyhS3mue7fkF6dN4dhiu3jDJjyKsg"
USERNAME = "arunesh1"
GRAPH_ID = "graph1"

header_token = {
    "X-USER-TOKEN": TOKEN
}


# CREATE USER PROFILE
create_user = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes"
}

# response = requests.post(url=ENDPOINT_URL, json=create_user)
# print(response.text)


#   CREATE GRAPH
GRAPH_URL = f"{ENDPOINT_URL}/{USERNAME}/graphs"

graph_parameter = {
    "id": GRAPH_ID,
    "name": "Netflix Time Watch",
    "unit": "hours",
    "type": "float",
    "color": "momiji",
}

# response = requests.post(url=GRAPH_URL, json=graph_parameter, headers=header_token)
# print(response.text)


# PUT VALUE ON GRAPH
GRAPH_VALUE_URL = f"{ENDPOINT_URL}/{USERNAME}/graphs/{GRAPH_ID}"
today = datetime(year=2022, month=1, day=3)

value_parameter = {
    "date": today.strftime("%Y%m%d"),
    "quantity": "2.11"
}

# response = requests.post(url=GRAPH_VALUE_URL, json=value_parameter, headers=header_token)
# print(response.text)


# EXPLORE

url = f"{ENDPOINT_URL}/{USERNAME}/graphs/{GRAPH_ID}/stats"

response = requests.post(url=url)
print(response.text)




















































