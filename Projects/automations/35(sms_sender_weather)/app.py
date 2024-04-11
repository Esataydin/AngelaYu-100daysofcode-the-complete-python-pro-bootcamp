# YOU HAVE TO ADD YOUR NUMBER TO TWILIO VERIFIED NUMBERS TO SEND THEM SMS
# for more information: https://www.twilio.com/docs/usage/api
from twilio.rest import Client

import requests


end_point = "https://api.openweathermap.org/data/2.5/forecast"
api_key: str = YOUR_OPEN_WEATHER_MAP_API_KEY

account_sid: str = YOUR_TWILIO_ACCOUNT_SID
auth_token: str = YOUR_TWILIO_AUTH_TOKEN

weather_params = {
    "lat": 0,
    "lon": 0,
    "appid": api_key
}

response = requests.get(end_point, params=weather_params)
response.raise_for_status()
data = response.json()

weather_slice = data["list"][:12]
will_rain: bool = False

for hour_data in weather_slice:
    condition_code = hour_data["weather"][0]["id"]
    if int(condition_code) < 700:
        will_rain = True

if will_rain:
    client = Client(account_sid, auth_token)
    message = client.messages \
        .create(
            body="Bring an umbrella.",
            from_="[TWILIO_NUMBER]",
            to="[TO_NUMBER]"
        )
    print(message.sid)
