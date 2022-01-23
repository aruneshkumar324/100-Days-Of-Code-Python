import requests
from twilio.rest import Client


# "lat": 13.046396,
#     "lon": 77.723328,

API = "6940d199dd16f53e04bbc0f5896b6c44"
account_sid = "ACfb9a6b8aa9e4675b0d2abd5179828bb6"
auth_token = "f4e0af510b8c63e2afd1ec3d042aa0c0"

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


b = hourly_data[0]["weather"][0]["id"]

weather_slice = data["hourly"][:12]

will_rain = False

for x in weather_slice:
    code = x["weather"][0]["id"]
    if code < 700:
        will_rain = True

if will_rain:
    client = Client(account_sid, auth_token)
    message = client.messages \
        .create(
        body="Bring Umbrella",
        from_='+16165800849',
        to="+9189718 18410"
    )

    print("Message Sent")

