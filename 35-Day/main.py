import requests


API = "6940d199dd16f53e04bbc0f5896b6c44"

parameters = {
    "lat": 13.046396,
    "lon": 77.723328,
    "appid": API
}

# response = requests.get("https://api.openweathermap.org/data/2.5/onecall?lat=13.046396&lon=77.723328&appid=6940d199dd16f53e04bbc0f5896b6c44")
response = requests.get("https://api.openweathermap.org/data/2.5/onecall", params=parameters)

response.raise_for_status()

print(response.status_code)

data = response.json()
print(data)

hourly_data = data["hourly"]
print(hourly_data)

