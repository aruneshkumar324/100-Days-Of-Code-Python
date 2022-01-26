import requests
from datetime import datetime


# DATE & TIME
today = datetime.now()
DATE = today.strftime("%d/%m/%Y")
TIME = today.strftime("%H:%M:%S")


# SHEET RECORD VARIABLES
SHEET_URL = "https://api.sheety.co/7ca8526e1059a9820bcc49c37f3cce71/workoutTracking/workouts"
sheet_header = {
    "Content-Type": "application/json",
}


# NUTRITIONIX VARIABLES
APP_ID = "f86dc823"
API_KEY = "1a00b6aeb51a37957a51d05c282e7af6"
ENDPOINT_URL = "https://trackapi.nutritionix.com/v2/natural/exercise"

GENDER = "male"
AGE = 22
HEIGHT = 157
WEIGHT = 16.2
user_input = input("Tell me which exercises you did: ")

header_parameter = {
    "Content-Type": "application/json",
    "x-app-id": APP_ID,
    "x-app-key": API_KEY
}

body_content = {
    "query": user_input,
    "gender": GENDER,
    "weight_kg": WEIGHT,
    "height_cm": HEIGHT,
    "age": AGE
}

response = requests.post(url=ENDPOINT_URL, headers=header_parameter, json=body_content)
print(response.text)

data = response.json()["exercises"]

for x in data:
    exercise_name = x["name"]
    duration = x["duration_min"]
    calories = x["nf_calories"]

    # ADD ROW IN SHEET
    add_parameter = {
        "workout": {
            "date": DATE,
            "time": TIME,
            "exercise": exercise_name.title(),
            "duration": duration,
            "calories": calories
        }
    }

    add_sheet_response = requests.post(url=SHEET_URL, json=add_parameter, headers=sheet_header, auth=("arunesh", "9534857622"))
    print(add_sheet_response.text)


# FETCH SHEET DATA
sheet_response = requests.get(url=SHEET_URL, auth=("arunesh", "9534857622"))
print(sheet_response.text)


# DELETE SHEET ROW
# delete_sheet_response = requests.delete(url=f"{SHEET_URL}/2", auth=("arunesh", "9534857622"))
# print(delete_sheet_response.status_code)

# Ran 5k and cycled for 20 minutes.



























































