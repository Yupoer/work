import requests
from twilio.rest import Client

api_key = "145a48549e315374e95c4812d1f621da"
OWM_Endpoint = "https://api.openweathermap.org/data/2.5/onecall"
account_sid = "AC4c58bbfb1758b33f1af719b6c93e6983"
auth_token = "59641c6f5969156df94aab23ef5a0532"
trial_number = "+14436029249"
MY_LAT = 24.784241
MY_LONG = 120.967484

weather_parameters = {
    "lat": MY_LAT,
    "lon": MY_LONG,
    "appid": api_key,
    "exclude": "current,minutely,daily"
}

response = requests.get(OWM_Endpoint, params=weather_parameters)
weather_data = response.json()
weather_slice = weather_data["hourly"][:12]

will_rain = False

for hour_data in weather_slice:
    condition_code = hour_data["weather"][0]["id"]
    if int(condition_code) < 700:
        will_rain = True

if will_rain:
    client = Client(account_sid, auth_token)

    message = client.messages \
        .create(
        body="It's going to rain today, Remember to bring an ☂️",
        from_=f"{trial_number}",
        to="+886905734830"
    )

    print(message.status)
