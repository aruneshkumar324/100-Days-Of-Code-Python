import requests


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
