import requests
from datetime import datetime


URL = "https://pixe.la/v1/users"
USERNAME = "arunesh"
TOKEN = "32ewu3dsh34jwe3fdgh34fds4hgfd4we43"

parameters = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes"
}

# response = requests.post(URL, json=parameters)
# print(response.text)


# CREATE GRAPH

GRAPH_URL = f"{URL}/{USERNAME}/graphs"
GRAPH_ID = "graph1"

graph_parameter = {
    "id": GRAPH_ID,
    "name": "Cycle Graph",
    "unit": "km",
    "type": "float",
    "color": "ajisai"
}

token_header = {
    "X-USER-TOKEN": TOKEN
}

# response = requests.post(url=GRAPH_URL, json=graph_parameter, headers=token_header)
# print(response.text)


#   ADD RECORD
POST_URL = f"{URL}/{USERNAME}/graphs/{GRAPH_ID}"
print(POST_URL)

today = datetime(year=2022, month=1, day=11)

post_parameter = {
    "date": today.strftime("%Y%m%d"),
    "quantity": "7",
}

# response = requests.post(url=POST_URL, json=post_parameter, headers=token_header)
# print(response.text)


# # UPDATE GRAPH RECORD
# UPDATE_URL = f"{URL}/{USERNAME}/graphs/{GRAPH_ID}/{today.strftime('%Y%m%d')}"
# update_parameter = {
#     "quantity": "2"
# }
# response = requests.put(url=UPDATE_URL, json=update_parameter, headers=token_header)
# print(response.text)

DELETE_URL = f"{URL}/{USERNAME}/graphs/{GRAPH_ID}/{today.strftime('%Y%m%d')}"

response = requests.delete(url=DELETE_URL, headers=token_header)

print(response.text)

