import requests
from datetime import datetime


# response = requests.get("http://api.open-notify.org/iss-now.json")
#
# print(response)
#
# # STATUS CODE
# print(response.status_code)
# response.raise_for_status()
#
#
# # GET DATA
#
# data = response.json()
# print(data)
#
# iss_position = data["iss_position"]
# print(iss_position)
#
# latitude = data["iss_position"]["latitude"]
# longitude = data["iss_position"]["longitude"]
#
# print(latitude)
# print(longitude)


MY_LAT = 13.053511
MY_LONG = 77.718374

parameters = {
    "lat": MY_LAT,
    "lng": MY_LONG,
    "formatted": 0
}

response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
response.raise_for_status()

data = response.json()
print(data)

sunrise = data["results"]["sunrise"].split("T")[1].split(":")[0]
sunset = data["results"]["sunset"].split("T")[1].split(":")[0]
print(sunrise)
print(sunset)


date = datetime.now()
print(date.hour)


# If the ISS is close to my current position
# and it is currently dark
# Then send me an email to tell me to look up.
# BONUS: run the code every 60 seconds.











