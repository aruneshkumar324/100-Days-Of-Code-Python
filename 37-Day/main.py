import requests


URL = "https://pixe.la/v1/users"

parameters = {
    "token": "32ewu3dsh34jwe3fdgh34fds4hgfd4we43",
    "username": "arunesh",
    "agreeTermsOfService": "yes",
    "notMinor": "yes"
}

response = requests.post(URL, json=parameters)

print(response.text)
