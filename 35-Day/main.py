import requests

# "lat": 13.046396,
#     "lon": 77.723328,

API = "6940d199dd16f53e04bbc0f5896b6c44"

parameters = {
    "lat": -12.462320,
    "lon": 130.840942,
    "appid": API,
    "exclude": "current,minutely,daily"
}


response = requests.get("https://api.openweathermap.org/data/2.5/onecall", params=parameters)
response.raise_for_status()

data = response.json()
hourly_data = data["hourly"]

print(hourly_data)

b = hourly_data[0]["weather"][0]["id"]
# print(b)


# # MY SOLUTION
# will_rain = False
#
# for x in range(0, 12):
#     code = hourly_data[x]["weather"][0]["id"]
#     if code < 700:
#         will_rain = True
#
# if will_rain:
#     print("Bring Umbrella")


# # ANGELA SOLUTION
weather_slice = data["hourly"][:12]
print(weather_slice)

will_rain = False

for x in weather_slice:
    code = x["weather"][0]["id"]
    if code < 700:
        will_rain = True

if will_rain:
    print("Bring Umbrella")













