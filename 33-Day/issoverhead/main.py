import requests
from datetime import datetime
import smtplib

MY_LAT = 13.053511
MY_LONG = 77.718374

response = requests.get(url="http://api.open-notify.org/iss-now.json")
response.raise_for_status()
data = response.json()

iss_latitude = float(data["iss_position"]["latitude"])
iss_longitude = float(data["iss_position"]["longitude"])

parameters = {
    "lat": MY_LAT,
    "lng": MY_LONG,
    "formatted": 0,
}

response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
response.raise_for_status()
data = response.json()

sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])

print(sunset)
# print(sunrise)

time_now = datetime.now()
print(time_now.hour)

# if lat <= 5 and lat >= -5 and lng <= 5 and lng >= -5:
if MY_LAT-5 <= iss_latitude >= MY_LAT+5 and MY_LONG-5 <= iss_longitude >= MY_LONG+5:
    # and it is currently dark
    if time_now.hour >= sunset or time_now.hour <= sunrise:
        # Then send me an email to tell me to look up.
        MY_EMAIL = "pythonemailtesting76@gmail.com"
        PASSWORD = "9534857622"
        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(user=MY_EMAIL, password=PASSWORD)
            connection.sendmail(from_addr=MY_EMAIL, to_addrs="pythonemailtesting76@yahoo.com", msg="Subject:ISS\n\nLoop Up")

