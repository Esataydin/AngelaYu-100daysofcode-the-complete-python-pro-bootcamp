import requests
from datetime import datetime


# These are for examples
GENDER = "male"
WEIGHT_KG = 77
HEIGHT_CM = 182
AGE = 26

APP_ID = YOUR_TRACKAPI_NUTRITIONIX_APP_ID
API_KEY = YOUR_TRACKAPI_NUTRITIONIX_API_KEY

SHEETY_USERNAME = YOUR_SHEETY_USERNAME
SHEETY_BEARER_TOKEN = YOUR_SHEETY_BEARER_TOKEN


# https://trackapi.nutritionix.com/docs/#/default/post_v2_natural_exercise for better understanding for endpoint
exercise_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"

exercise_text: str = input("Tell me which exercises you did: ")

headers = {
    "x-app-id": APP_ID,
    "x-app-key": API_KEY,
}

parameters = {
    "query": exercise_text,
    "gender": GENDER,
    "weight_kg": WEIGHT_KG,
    "height_cm": HEIGHT_CM,
    "age": AGE
}

response = requests.post(url=exercise_endpoint, json=parameters, headers=headers)
result = response.json()
print(result)

# https://sheety.co/docs/requests.html for better understanding the url
sheety_url = f"https://api.sheety.co/{SHEETY_USERNAME}/workout/page1"  #it's an example for better understanding

today_date = datetime.now().strftime("%d/%m/%Y")
now_time = datetime.now().strftime("%X")


bearer_token = SHEETY_BEARER_TOKEN
headers_sheety = {
    "Authorization": f"Bearer {bearer_token}"
}

for exercise in result["exercises"]:
    sheet_inputs = {
        "workout": {
            "date": today_date,
            "time": now_time,
            "exercise": exercise["name"].title(),
            "duration": exercise["duration_min"],
            "calories": exercise["nf_calories"]
        }
    }

    sheet_response = requests.post(sheety_url, json=sheet_inputs, headers=headers_sheety)

    print(sheet_response.text)
