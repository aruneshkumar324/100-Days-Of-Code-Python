import requests


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

graph_parameter = {
    "id": "graph1",
    "name": "Cycle Graph",
    "unit": "km",
    "type": "float",
    "color": "ajisai"
}

graph_header = {
    "X-USER-TOKEN": TOKEN
}

response = requests.post(url=GRAPH_URL, json=graph_parameter, headers=graph_header)

print(response.text)




















