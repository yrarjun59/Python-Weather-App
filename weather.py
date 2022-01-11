import requests
from pprint import pprint

# you can go through https://openweathermap.org sign up & generate a free api key for u
API_KEY = "439e72b4bd9d9a9becab0403a5061758"

location = input("Enter Your Desired Location:-\n")

weather_url =f"http://api.openweathermap.org/data/2.5/weather?q={location}&appid="
final_url = weather_url + API_KEY

weather_data = requests.get(final_url).json()
# print(weather_data)

pprint(weather_data)
